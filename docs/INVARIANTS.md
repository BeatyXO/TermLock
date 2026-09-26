# Protocol invariants

1. Party A and Party B are distinct non-zero addresses.
2. Session schema is immutable after creation.
3. Schema fields are rejected when oversized; they are never silently truncated.
4. Dimension identifiers are normalized, bounded, and unique.
5. Only declared parties can submit terms.
6. Party A cannot submit Party B's terms and vice versa.
7. Empty or oversized commitments are rejected.
8. Re-submitting byte-identical current terms is rejected as a no-op revision.
9. Every real revision changes the submitting party's current content hash and increments its revision counter.
10. Every real revision invalidates the prior assessment and both approvals.
11. A stale assessment can never lock newer wording.
12. The model must cover the frozen schema exactly once; unknown, duplicate, omitted, or unknown-status rows fail closed.
13. Validators independently re-run the semantic classification task.
14. Consensus-critical material is the dimension name, frozen mode, and semantic status; prose notes do not decide lockability.
15. A REQUIRED dimension locks only on `MATCH`.
16. `MISSING_BOTH` is never silently promoted to `MATCH` for a REQUIRED dimension.
17. OPTIONAL one-sided language, ambiguity, or conflict blocks locking.
18. An assessment is bound to the exact current Party A and Party B term hashes.
19. The same exact current term pair cannot be repeatedly reassessed to clear approvals.
20. Only Party A can approve Party A's side of the assessment.
21. Only Party B can approve Party B's side of the assessment.
22. Both approvals must pin the exact current `assessment_hash`.
23. The AI/LLM never directly sets `LOCKED`.
24. `lock_agreement` is deterministic.
25. `LOCKED` state and `lock_hash` are immutable.
26. An unlocked party may cancel its session; a non-party creator may cancel only before either party participates.
27. A locked agreement cannot be cancelled.
28. Consumer contracts must pin the expected `lock_hash`.
29. `CommitmentGate` rejects malformed hashes, wrong locks, and replayed action hashes.
30. No frontend is part of the primitive.
