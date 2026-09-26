# Build status

## Current verified state

- TermLock and CommitmentGate preserve the frozen-schema, independent-validator, deterministic lockability, bilateral approval, cancellation, and replay protections.
- `python scripts/preflight.py`: PASS.
- `python -m compileall contracts scripts tests`: PASS.
- Direct Mode: `40 passed, 1 skipped`.
- Stable Studionet / chain 61999 TermLock lifecycle completed for session `1`: conflict rejection, revision invalidation, convergence, bilateral approval, lock, and immutable final state.
- Corrected CommitmentGate deployment completed and live consume proof succeeded; wrong-lock and replay guards were exercised.
- CI fix is pushed: pin `genlayer-test==0.28.0` and seed the deterministic `genvm-universal-v0.2.16.tar.xz` bundle before pytest, preventing the clean-runner download of missing `v0.3.0-rc7`.

## Canonical live addresses

- TermLock: `0xa1132EabEADcC6c517ABE498b51Cec8eBFFD8E3b`
- CommitmentGate: `0x1553918a44b27D93Cd7e8Fc49Fa31582e54a9594`

The previously supplied gate address finalized with a constructor type error and was replaced by the corrected typed deployment. No TermLock redeployment was needed.
