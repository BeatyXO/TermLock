# Deployment evidence

Network target: **stable Studionet / chain 61999**  
GenLayer RPC: `https://studio.genlayer.com/api`  
Explorer: `https://explorer-studio.genlayer.com`

## Canonical deployment

- TermLock address: `0xa1132EabEADcC6c517ABE498b51Cec8eBFFD8E3b`
- TermLock deploy tx: `0xdc74a6beb8f1d7523822a30aced7516f1391fa6acc310f9ad47b071b4ce82a63`
- CommitmentGate address: `0x1553918a44b27D93Cd7e8Fc49Fa31582e54a9594`
- CommitmentGate deploy tx: `0x3b2246ecaba9f6dce9ef1edbe2f4bd835e186593a75742756f8c3d8182ae3b54`
- canonical source commit: `6a561af6b9f6cf2c7b5f2f6403f1f9175ed00af1`
- The earlier supplied gate tx `0x57c04b...` finalized with a constructor storage type error (`str` had no `as_bytes`) and was not usable; the corrected deployment used typed `addr#` encoding.

## Session / lifecycle proof

- session ID: `1`
- create-session tx: `0xe4d0835f8f7af37a0748f67a9fe1cfb44b7646b9edb8bc40b0ac1011fcf266d1`
- Party A initial submission tx: `0x3be95e78cd06459aeb9b5dcda78a655bc1033c28b80703f5ea349161d6bec2d0`
- Party B conflicting submission tx: `0x6cece622abbcaa028c10bdfec8c6d4a173e549700cb2e300f2b372ae6fdc2362`
- conflicting assessment tx: `0x100051027e0631c4ed432bb11f311cf473fdaf861a5c7de9fb6550a90747ef81` (deadline `CONFLICT`, lockable `false`)
- rejected pre-convergence lock tx: `0x117b653822522729d59887cdca14fd152aeac03ed8fc1799e6412ad6851d2723`; lock remained unavailable
- revision tx invalidating stale assessment: `0x08968ee598c41af0283c762e62589f56b07d011d5a15845a0f8cb6b469712031`
- converged assessment tx: `0x23e6d37c89e43593d63c4fb32e805d8ef906133a440965c2fd5fff670c6aefed`
- Party A assessment-approval tx: `0x8de03c19489001ecc892abd1e95187e31605014da96d16273416740f2aec042a`
- Party B assessment-approval tx: `0x992364f3bfa9ca0ffc3d7474ae94103723d4db6e752c41ba3f8b29f3a31a7d55`
- one approval `can_lock`: `false`; both approvals `can_lock`: `true`
- lock tx: `0x892a05348c44e3fe94143de4ce1b131d526895f3ce836d5129b0c2c73d892001`
- final state: `LOCKED`; post-lock mutation/cancellation is blocked by the contract state machine

## Consumer proof

- successful pinned consume tx: `0x7b19b7d856509d192df55902265a09aca3271a069def4f9f755559edce2098c9`
- `is_consumed(aaaaaaaa...aaaa)`: `true`
- wrong-lock rejection tx: `0xa457818f06cd860b9e55ac18172159748da3dae0e975a93449c35e55c9ca06e3`; fresh action remained unconsumed (`is_consumed(bbbb...bbbb) == false`)
- replay rejection: reusing the consumed `aaaaaaaa...aaaa` action is rejected by the `action already consumed` guard; the consumed state remains `true`

## Final hashes

- schema hash: `aa4f7dae4add80aad3e2de0670e288f79b51f69aa56c30f5b63954634dc5e8a3`
- Party A final terms hash: `75ccee2db5fccd600c5168eaa650e3666dd05688ce071d330e140e955f00543a`
- Party B final terms hash: `079b69c59ad6f88d11519047764bb54eb18ec0db96b13455425340496af45ae0`
- final assessment hash: `2e46020340a81ea0cef9b4398b4db029006c4db5f3efbf977ad2767d2fdaba88`
- final lock hash: `866a609d9f9a663b8ba559aa0138bdcd3ae811d00ec4320f03cb05015e2e3ade`

## Verification commands / real results

- `python scripts/preflight.py`: PASS
- `python -m compileall contracts scripts tests`: PASS
- `genvm-lint check contracts/termlock.py`: lint rules PASS; SDK validation is environment-dependent locally
- `genvm-lint check contracts/commitment_gate.py`: lint rules PASS; SDK validation is environment-dependent locally
- Direct Mode pytest: `40 passed, 1 skipped`
- live stable Studionet lifecycle: PASS for TermLock session 1 and corrected CommitmentGate deployment
- GitHub Actions: workflow fix pushed in commit `6e9d6554fe1017338d8326f89364bd7dd857c4d4`; clean-run verification pending final runner completion

All values above are actual observed evidence from stable Studionet; no fixture or deployment placeholder remains.
