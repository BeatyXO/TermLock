# TermLock

**Consensus-backed semantic convergence and explicit commitment locking for GenLayer.**

TermLock is a standalone reusable Intelligent Contract primitive. Two declared parties independently submit their own natural-language commitments under a creator-frozen semantic dimension schema. GenLayer validators compare those commitments dimension-by-dimension. Deterministic contract logic — not the LLM — decides whether the pair is semantically lockable, and both parties must explicitly approve the exact current assessment before an immutable lock can be formed.

There is **no frontend** in this repository.

## Why it exists

Cryptographic signatures prove who signed bytes. They do not prove that two differently worded commitments express the same material deal. TermLock supplies a narrow protocol for that missing step without turning an LLM into a contract drafter, legal judge, or unrestricted acceptance oracle.

## Protocol boundary

The model may classify only frozen dimensions using this bounded vocabulary:

- `MATCH`
- `CONFLICT`
- `AMBIGUOUS`
- `MISSING_A`
- `MISSING_B`
- `MISSING_BOTH`
- `NOT_APPLICABLE`

The model **cannot**:

- add dimensions;
- omit dimensions;
- rewrite either party's terms;
- infer missing obligations from custom or likely intent;
- approve the agreement;
- set `LOCKED` state;
- decide legal validity or enforceability.

Validators independently re-run the same bounded classification task. Consensus compares only material decision fields `(dimension name, mode, status)`. Explanatory notes are non-consensus metadata.

## Deterministic lifecycle

1. A creator opens a session with exactly two distinct parties and 1–16 frozen dimensions.
2. Dimension identifiers are normalized, bounded, unique, and committed into `schema_hash`.
3. Each party can submit only its own terms.
4. Submissions are content-hashed and revisioned; identical no-op resubmissions are rejected.
5. Once both current submissions exist, anyone may request one consensus assessment for that exact term pair.
6. The assessment is bound to `schema_hash + Party A hash + Party B hash`.
7. A later real revision invalidates the prior assessment and both approvals.
8. Required dimensions lock **only** on `MATCH`.
9. Optional dimensions may be jointly absent or genuinely not applicable, but conflict, ambiguity, or one-sided language still blocks.
10. Party A and Party B must independently approve the exact current `assessment_hash`.
11. `lock_agreement` is then deterministic and creates an immutable `lock_hash`.
12. `CommitmentGate` demonstrates typed IC-to-IC consumption with expected-lock pinning and action replay protection.

## Why explicit approval exists

Semantic convergence is not the same thing as assent. A participant may submit wording for comparison without intending an arbitrary third party to finalize it immediately. TermLock therefore separates:

- **semantic convergence** — consensus-backed;
- **party assent** — deterministic explicit approval;
- **finalization** — deterministic permissionless lock once both approvals exist.

Repeated reassessment of the same exact term pair is rejected, so an outsider cannot repeatedly clear approvals as a griefing mechanism.

## Hash domains

TermLock uses canonical JSON and separate domain labels:

- `TERMLOCK_SCHEMA_V1`
- `TERMLOCK_ASSESSMENT_V1`
- `TERMLOCK_LOCK_V1`

The final lock binds:

- session ID;
- frozen schema hash;
- current Party A terms hash;
- current Party B terms hash;
- current assessment hash.

Consumers should pin the final `lock_hash`, never trust a session ID alone.

## Important privacy note

Party commitment text is stored in Intelligent Contract state. Treat it as public blockchain data. **Do not submit secrets, passwords, private keys, confidential personal information, or material that should remain private.**

## Scope

TermLock establishes protocol-level semantic convergence and explicit approval under a declared comparison schema. It does not establish legal validity, enforceability, capacity, governing law, regulatory compliance, identity verification, or jurisdiction-specific contractual interpretation.

## Stable network target

- network alias: `studionet`
- chain ID: `61999`
- GenLayer RPC: `https://studio.genlayer.com/api`
- explorer: `https://explorer-studio.genlayer.com`

Keep all deployment and integration work on the stable Studionet target above.

## Repository layout

- `contracts/termlock.py` — reusable primitive
- `contracts/commitment_gate.py` — real consumer IC example
- `tests/test_termlock.py` — Direct Mode/adversarial suite
- `tests/test_source_invariants.py` — fast static guards
- `tests/test_live_studionet.py` — live-proof handoff specification
- `fixtures/` — live fixture texts, pinned to an immutable Git commit before live execution
- `docs/` — architecture, invariants, security model
- `scripts/preflight.py` — repository/final-submission gate
- `scripts/pin_fixture_commit.py` — immutable fixture pinning
- `DEPLOYMENT.md` — only real finalized deployment evidence belongs here
- `SUBMISSION.md` — reviewer-facing summary

## Local verification

Install tooling:

```bash
python -m pip install -r requirements-test.txt
```

Run:

```bash
python scripts/preflight.py
python -m compileall contracts scripts tests
genvm-lint check contracts/termlock.py
genvm-lint check contracts/commitment_gate.py
pytest -q
```

The final gate is intentionally stricter:

```bash
python scripts/preflight.py --final
```

It must not pass while immutable fixture markers or pending deployment proof remain.

## Live proof expected before submission

On stable Studionet / chain 61999, the final evidence should show:

1. finalized TermLock deployment;
2. a session created with immutable schema hash;
3. a deliberately conflicting required term that cannot lock;
4. a real revision that invalidates the old assessment;
5. a semantically converged current pair;
6. both parties approving the exact assessment hash;
7. immutable lock creation;
8. finalized CommitmentGate deployment;
9. a correct pinned consume succeeding;
10. wrong-lock-hash consume rejected;
11. replayed action hash rejected.

No address, transaction hash, test count, or live result should be documented unless it was actually produced.
