# Verification checklist

## Protocol and repository

- [x] standalone IC boundary retained; no frontend
- [x] frozen schema rejects silent truncation
- [x] model output is exact-schema / bounded-status only
- [x] validators independently re-derive semantic statuses
- [x] required dimensions fail closed
- [x] real revisions invalidate assessment and approvals
- [x] no-op revisions rejected
- [x] repeated same-pair reassessment rejected
- [x] explicit two-party current-assessment approval required
- [x] canonical domain-separated hash design
- [x] real typed consumer source present
- [x] source/static tests included
- [x] immutable fixture commit pin verified
- [x] no frontend, secrets, private keys, environment files, or deployment placeholders remain

## Verification and CI

- [x] repository tooling installed and pinned
- [x] `python scripts/preflight.py` passes
- [x] `python -m compileall contracts scripts tests` passes
- [x] `genvm-lint check contracts/termlock.py` passes in clean GitHub Actions
- [x] `genvm-lint check contracts/commitment_gate.py` passes in clean GitHub Actions
- [x] Direct Mode passes: `40 passed, 1 skipped`
- [x] GitHub Actions is green on run `36280036759`
- [x] effective network is stable `studionet`, chain 61999

## Live Studionet lifecycle

- [x] TermLock finalized deployment recorded
- [x] two-party session created
- [x] conflicting REQUIRED round demonstrated non-lockability
- [x] premature lock rejection recorded
- [x] revision invalidated the stale assessment
- [x] revised current round reached semantic convergence
- [x] Party A approved the exact final assessment
- [x] Party B approved the exact final assessment
- [x] one approval remained non-lockable; two approvals became lockable
- [x] approved converged round locked with a nonzero 64-hex lock hash
- [x] final TermLock state is immutable

## CommitmentGate consumer proof

- [x] corrected CommitmentGate finalized deployment recorded
- [x] valid pinned gate call succeeded
- [x] successful action became consumed
- [x] wrong-lock-hash call was rejected without consuming the fresh action
- [x] replayed action hash was rejected

## Final submission state

- [x] `DEPLOYMENT.md` contains real lifecycle proof and no `PENDING` fields
- [x] no `FIXTURE_COMMIT_PLACEHOLDER`, `UNVERIFIED`, or `NOT RUN` markers remain
- [x] final-gate conditions for `python scripts/preflight.py --final` are satisfied
- [x] current remote source was inspected after the final lifecycle/CI push
- [x] canonical deployment source remains unchanged from commit `6a561af6b9f6cf2c7b5f2f6403f1f9175ed00af1`
