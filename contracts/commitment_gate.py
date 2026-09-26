# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
"""TermLock consumer proving typed IC-to-IC enforcement and replay protection."""

from genlayer import *

ZERO_ADDRESS = "0x" + ("0" * 40)


@gl.contract_interface
class ITermLock:
    class View:
        def is_locked(self, session_id: u256, expected_lock_hash: str) -> bool: ...

    class Write:
        pass


class CommitmentConsumed(gl.Event):
    def __init__(self, action_hash: str, session_id: u256, /, **blob): ...


def valid_hash(value: str) -> bool:
    s = str(value).lower().strip()
    return len(s) == 64 and all(c in "0123456789abcdef" for c in s)


class CommitmentGate(gl.Contract):
    termlock: Address
    consumed: TreeMap[str, bool]

    def __init__(self, termlock: Address):
        if str(termlock).lower() == ZERO_ADDRESS:
            raise gl.vm.UserError("TermLock address cannot be zero")
        self.termlock = termlock

    @gl.public.write
    def consume(self, session_id: u256, expected_lock_hash: str, action_hash: str) -> bool:
        lock_hash = str(expected_lock_hash).lower().strip()
        action = str(action_hash).lower().strip()
        if not valid_hash(lock_hash):
            raise gl.vm.UserError("expected_lock_hash must be 64 hex")
        if not valid_hash(action):
            raise gl.vm.UserError("action_hash must be 64 hex")
        if self.consumed.get(action, False):
            raise gl.vm.UserError("action already consumed")

        locked = ITermLock(self.termlock).view().is_locked(session_id, lock_hash)
        if not locked:
            raise gl.vm.UserError("TermLock commitment not currently valid")

        self.consumed[action] = True
        CommitmentConsumed(action, session_id, lock_hash=lock_hash).emit()
        return True

    @gl.public.view
    def is_consumed(self, action_hash: str) -> bool:
        action = str(action_hash).lower().strip()
        if not valid_hash(action):
            return False
        return self.consumed.get(action, False)
