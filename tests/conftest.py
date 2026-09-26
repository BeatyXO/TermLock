"""Compatibility helpers for GenLayer Direct Mode."""

import os
import sys
import inspect
import importlib


if sys.platform == "win32":
    _unlink = os.unlink

    def _compat_unlink(path, *args, **kwargs):
        try:
            return _unlink(path, *args, **kwargs)
        except PermissionError:
            callers = [frame.filename.replace("\\", "/") for frame in inspect.stack()]
            if any(name.endswith("/gltest/direct/loader.py") for name in callers):
                return None
            raise

    os.unlink = _compat_unlink


def pytest_runtest_setup(item):
    """Reset GenLayer's single-contract registration between Direct Mode loads."""
    try:
        import gltest.direct.sdk_loader as sdk_loader
        sdk_loader.setup_sdk_paths()
        import genlayer.gl.genvm_contracts as contracts
        contracts.__known_contract__ = None
    except ImportError:
        pass


def pytest_configure(config):
    """Teach current Direct Mode about event emission so contract calls stay real."""
    try:
        from gltest.direct import wasi_mock

        def handle(vm, request):
            if isinstance(request, dict) and "EmitEvent" in request:
                vm._emitted_events = getattr(vm, "_emitted_events", [])
                vm._emitted_events.append(request["EmitEvent"])
                return {"ok": None}
            # Preserve all other Direct Mode dispatch behavior.
            return _original_gl_call(vm, request)

        _original_gl_call = wasi_mock._handle_gl_call
        wasi_mock._handle_gl_call = handle
    except ImportError:
        pass
