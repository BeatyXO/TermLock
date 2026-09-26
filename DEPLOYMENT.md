# Deployment evidence

Network target: **stable Studionet / chain 61999**  
GenLayer RPC: `https://studio.genlayer.com/api`  
Explorer: `https://explorer-studio.genlayer.com`

This repository does not invent deployment evidence. Fields remain `PENDING` until the finishing environment produces finalized proof.

## Canonical deployment

- TermLock address: `0xa1132EabEADcC6c517ABE498b51Cec8eBFFD8E3b`
- TermLock deploy tx: `0xdc74a6beb8f1d7523822a30aced7516f1391fa6acc310f9ad47b071b4ce82a63`
- CommitmentGate address: `0x000A997D9850daDBE3A54e6ECCE5b3432bf689B1`
- CommitmentGate deploy tx: `0x57c04b4397233b56e8a01d9526c5cd2aaca3dc6f04e26cbad60b23bbe12e56ba`
- canonical source commit: `6a561af6b9f6cf2c7b5f2f6403f1f9175ed00af1`

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

## Superseded deployments

Earlier deployments are retained in Git history only. The canonical addresses above correspond to the final pushed source state.
