# Build status

This file records only checks actually performed in the current handoff environment. It is not deployment proof.

## Implemented before Codex/live-runtime handoff

- hardened frozen-schema validation with rejection instead of silent truncation;
- canonical machine-stable dimension identifiers;
- exact-schema model-output validation;
- independent validator semantic re-evaluation;
- untrusted-input prompt-injection hardening;
- no-op revision rejection;
- stale-assessment invalidation;
- repeated same-pair reassessment rejection;
- explicit two-party approval of the exact current assessment;
- canonical domain-separated schema / assessment / lock hashes;
- restricted non-party creator cancellation after participation;
- typed `CommitmentGate` consumer with lock pinning and replay protection;
- expanded Direct Mode/adversarial test suite;
- strengthened preflight and CI configuration;
- reviewer-facing architecture/invariant/security documentation.

## Still requires the GenLayer-enabled finishing environment

- push the complete source to `BeatyXO/TermLock` and pin the fixtures to that commit;
- run `genvm-lint check` in an environment where the pinned SDK bundle is readable;
- execute live stable Studionet lifecycle on chain 61999;
- deploy TermLock and CommitmentGate;
- produce finalized addresses, transactions, consensus evidence and hashes;
- update `DEPLOYMENT.md` with only those real results;
- run `python scripts/preflight.py --final` after deployment proof is complete.

## Verification performed in Codex finishing environment (2026-09-26)

- `python scripts/preflight.py`: PASS.
- `python -m compileall contracts scripts tests`: PASS.
- `pytest -q`: 40 passed, 1 skipped (live Studionet specification requires network writes).
- `genvm-lint check contracts/termlock.py`: lint rules PASS; SDK validation could not load the cached SDK (`WinError 5: Access is denied`).
- `genvm-lint check contracts/commitment_gate.py`: lint rules PASS; same SDK validation limitation.
- GenLayer CLI network configuration confirmed `studionet`, chain ID `61999`, RPC `https://studio.genlayer.com/api`.
- Stable RPC balance queries failed with transport error `fetch failed`; no live writes/deployments were attempted.
- GitHub CLI reports the saved GitHub token is invalid. Local `.git/config` and index writes are denied by the workspace sandbox, so no commit or push was possible.
