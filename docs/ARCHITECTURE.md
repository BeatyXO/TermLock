# Architecture

## Product boundary

TermLock is a reusable semantic commitment primitive. It is deliberately not a full negotiation application and has no frontend.

## Roles

### Creator

Creates a session and freezes:

- title;
- Party A;
- Party B;
- semantic dimension schema.

The creator is a facilitator, not an agreement controller. Once either party participates, a creator who is not also a party can no longer cancel the session.

### Party A / Party B

Each participant can:

- submit only its own wording;
- make a real revision;
- approve only the exact current consensus assessment;
- cancel an unlocked session.

A party cannot submit for the other side or approve on the other side's behalf.

### Validators

Validators independently classify the same exact current terms under the same frozen schema.

The leader result is accepted only when validators independently re-derive the same material matrix:

`(dimension name, REQUIRED|OPTIONAL mode, semantic status)`

Free-form notes are deliberately excluded from material consensus.

### Deterministic protocol

The deterministic layer owns:

- schema validation;
- revision counters;
- content hashes;
- assessment-currentness;
- lockability table;
- approval state;
- cancellation authorization;
- lock creation;
- consumer-visible lock validation.

The LLM never writes `LOCKED`.

## State machine

```text
OPEN
  | first/second party submissions
  v
READY
  | consensus assessment (one per exact term pair)
  | party approvals
  | deterministic lock
  v
LOCKED

OPEN/READY -- authorized cancellation --> CANCELLED
```

A real term revision while `READY` keeps the session in `READY` once both parties still have terms, but clears:

- assessed Party A hash;
- assessed Party B hash;
- assessment hash/JSON;
- Party A approval;
- Party B approval.

An identical no-op resubmission is rejected instead of incrementing a revision and invalidating current state.

## Frozen schema

Each dimension has:

- a bounded machine-stable identifier using lowercase letters, digits, `_`, or `-`;
- mode `REQUIRED` or `OPTIONAL`;
- bounded semantic criteria.

Schema input is rejected rather than silently truncated.

`schema_hash` is a Keccak digest over canonical JSON with domain `TERMLOCK_SCHEMA_V1`, including title, parties, and the full frozen dimension list.

## Consensus boundary

`build_comparison_prompt` serializes all dynamic content into a canonical JSON payload and tells the model to treat it as untrusted data. This reduces prompt-delimiter ambiguity and makes embedded instructions part of the compared commitment text, not executable instructions.

The model must return exactly one row for every frozen dimension. Unknown, duplicate, omitted, malformed, or unknown-status rows fail closed.

Validators call the model independently and compare only canonical material statuses.

## Lockability table

### REQUIRED

Only `MATCH` is lockable.

All other statuses block:

- `CONFLICT`
- `AMBIGUOUS`
- `MISSING_A`
- `MISSING_B`
- `MISSING_BOTH`
- `NOT_APPLICABLE`

### OPTIONAL

Lockable:

- `MATCH`
- `MISSING_BOTH`
- `NOT_APPLICABLE`

Blocking:

- `CONFLICT`
- `AMBIGUOUS`
- `MISSING_A`
- `MISSING_B`

This ensures an optional term may remain mutually absent, but one-sided or contradictory optional language is not silently ignored.

## Explicit assent

A lockable assessment is necessary but not sufficient.

Both parties must call `approve_current_assessment(session_id, assessment_hash)` for the exact current hash. A real revision clears both approvals. Reassessment of the same exact current pair is rejected, preventing third-party approval-reset griefing.

## Hash hierarchy

### Assessment hash

Domain `TERMLOCK_ASSESSMENT_V1` binds:

- session ID;
- schema hash;
- Party A current terms hash;
- Party B current terms hash;
- canonical material assessment matrix.

### Lock hash

Domain `TERMLOCK_LOCK_V1` binds:

- session ID;
- schema hash;
- Party A terms hash;
- Party B terms hash;
- assessment hash.

Once set, lock state is immutable.

## Consumer architecture

`CommitmentGate` defines a real typed interface and performs:

```python
ITermLock(termlock_address).view().is_locked(session_id, expected_lock_hash)
```

The consumer therefore pins an immutable final commitment rather than reimplementing TermLock logic. It also stores globally consumed action hashes so an accepted downstream action cannot be replayed.
