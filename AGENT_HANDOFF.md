# Codex finishing handoff

The repository is intentionally prepared so the remaining work is environment-specific GenLayer execution, not product invention.

## Do not redesign the product

Preserve:

- frozen bounded dimension schema;
- exact-schema semantic classification;
- independent validator re-derivation;
- deterministic required/optional lockability table;
- real-revision invalidation;
- rejection of identical no-op revisions;
- one assessment per exact current term pair;
- explicit Party A + Party B approval of the exact assessment hash;
- deterministic immutable lock hash;
- typed `CommitmentGate` consumption and replay defense;
- no frontend;
- stable Studionet target only.

Only alter architecture when the actual stable GenLayer runtime/linter demonstrates a concrete incompatibility.

## Remaining work

1. Install repository tooling.
2. Run preflight, compilation, GenVM linter and every Direct Mode test.
3. Fix genuine stable-runtime failures without weakening assertions or semantic safeguards.
4. Verify `studionet`, RPC `https://studio.genlayer.com/api`, chain ID `61999` before writes.
5. Execute the full live lifecycle in `tests/test_live_studionet.py` / `proof/VERIFICATION_CHECKLIST.md`.
6. Deploy TermLock and CommitmentGate.
7. Record only real finalized addresses, transaction hashes and hashes in `DEPLOYMENT.md`.
8. Run `python scripts/preflight.py --final`.
9. Push final code and report exact evidence.
