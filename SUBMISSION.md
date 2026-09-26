# Submission summary

**Title:** TermLock — Consensus-Backed Semantic Agreement & Commitment Locking

TermLock is a standalone reusable GenLayer primitive for proving that two independently authored natural-language commitments converge on the same material deal under a frozen dimension schema. Validators independently classify each required/optional dimension using a bounded status vocabulary; deterministic logic controls lockability and never lets the LLM set agreement state. Required dimensions must be `MATCH`; conflicts, ambiguity, and missing terms remain explicit fail-closed states. Assessments are hash-bound to the exact current schema and both current term hashes, while no-op revisions and repeated same-pair reassessment are rejected to prevent invalidation griefing. Semantic convergence alone is not treated as consent: both parties must explicitly approve the exact current assessment before deterministic immutable locking. The final lock hash commits to schema, both term hashes, and assessment. `CommitmentGate` proves typed IC-to-IC consumption with expected-lock pinning and replay protection.

No frontend is part of this submission.
