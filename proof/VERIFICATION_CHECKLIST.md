# Verification checklist

## Completed before live handoff

- [x] standalone IC boundary retained; no frontend
- [x] frozen schema rejects silent truncation
- [x] model output is exact-schema / bounded-status only
- [x] validator independently re-derives semantic statuses
- [x] required dimensions fail closed
- [x] real revisions invalidate assessment and approvals
- [x] no-op revisions rejected
- [x] repeated same-pair reassessment rejected
- [x] explicit two-party current-assessment approval required
- [x] canonical domain-separated hash design
- [x] real typed consumer source present
- [x] source/static tests included

## Finishing environment

- [ ] install repository tooling
- [ ] `python scripts/preflight.py`
- [ ] `python -m compileall contracts scripts tests`
- [ ] `genvm-lint check contracts/termlock.py`
- [ ] `genvm-lint check contracts/commitment_gate.py`
- [ ] all Direct Mode tests pass without weakening assertions
- [ ] effective network is `studionet`, chain 61999
- [ ] immutable fixture commit pin verified
- [ ] TermLock finalized deployment
- [ ] two-party session created
- [ ] conflicting required round cannot lock
- [ ] revised round invalidates stale assessment
- [ ] converged current round reaches consensus
- [ ] both parties approve exact current assessment
- [ ] converged approved round locks and emits nonzero 64-hex lock hash
- [ ] CommitmentGate finalized deployment
- [ ] valid pinned gate call succeeds
- [ ] wrong-lock-hash gate call rejected
- [ ] replayed action hash rejected
- [ ] `DEPLOYMENT.md` contains only real proof
- [ ] `python scripts/preflight.py --final`
- [ ] git status clean and final remote inspected
