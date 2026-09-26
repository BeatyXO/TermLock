# Deployment evidence

Network target: **stable Studionet / chain 61999**  
GenLayer RPC: `https://studio.genlayer.com/api`  
Explorer: `https://explorer-studio.genlayer.com`

This repository does not invent deployment evidence. Fields remain `PENDING` until the finishing environment produces finalized proof.

## Canonical deployment

- TermLock address: `0x4c6b965F144dC718D79226C52Fe337990830dfa8`
- TermLock deploy tx: `0xde74def1311b42669c38438d6bd059812496c1b7a5dff0c7dba397dd8ffdfdd5`
- CommitmentGate address: `0xC2Cc4417e15009c787E9DA50295a124FB2Ed1B0F`
- CommitmentGate deploy tx: `0x679b0af4a6f88dd2c699079c3a1015b54b6ae9017aaa42c7200e261fc3bbfa2c`
- canonical source commit: `ff2589aa139f7f2bba0fd7d981033e59242233c3`

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
