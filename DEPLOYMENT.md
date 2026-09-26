# Deployment evidence

Network target: **stable Studionet / chain 61999**  
GenLayer RPC: `https://studio.genlayer.com/api`  
Explorer: `https://explorer-studio.genlayer.com`

This repository does not invent deployment evidence. Fields remain `PENDING` until the finishing environment produces finalized proof.

## Canonical deployment

- TermLock address: `PENDING`
- TermLock deploy tx: `PENDING`
- CommitmentGate address: `PENDING`
- CommitmentGate deploy tx: `PENDING`
- canonical source commit: `PENDING`

## Session / lifecycle proof

- session ID: `PENDING`
- create-session tx: `PENDING`
- Party A initial submission tx: `PENDING`
- Party B conflicting submission tx: `PENDING`
- conflicting assessment tx: `PENDING`
- rejected pre-convergence lock evidence: `PENDING`
- revision tx invalidating stale assessment: `PENDING`
- converged assessment tx: `PENDING`
- Party A assessment-approval tx: `PENDING`
- Party B assessment-approval tx: `PENDING`
- lock tx: `PENDING`

## Consumer proof

- successful pinned consume tx: `PENDING`
- wrong-lock-hash rejection evidence: `PENDING`
- replay rejection evidence: `PENDING`

## Final hashes

- schema hash: `PENDING`
- Party A final terms hash: `PENDING`
- Party B final terms hash: `PENDING`
- final assessment hash: `PENDING`
- final lock hash: `PENDING`

## Verification commands / real results

- `python scripts/preflight.py`: `PENDING`
- `python -m compileall contracts scripts tests`: `PENDING`
- `genvm-lint check contracts/termlock.py`: `PENDING`
- `genvm-lint check contracts/commitment_gate.py`: `PENDING`
- Direct Mode pytest: `PENDING`
- live stable Studionet lifecycle: `PENDING`

Replace `PENDING` only with evidence actually produced. Do not copy sample addresses, hashes, or test counts into this file.

## Codex finishing attempt (2026-09-26)

No deployment was attempted. The GenLayer CLI reported the required stable network configuration (`studionet`, chain ID `61999`, RPC `https://studio.genlayer.com/api`), but read-only balance queries for the available test accounts failed with RPC transport error `fetch failed`. The environment therefore could not establish account funding or submit live transactions. GitHub authentication was invalid and the workspace sandbox denied local Git metadata writes, so the source could not be pushed and fixture references could not yet be pinned. All deployment evidence above remains pending.
