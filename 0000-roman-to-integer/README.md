# 0. Roman To Integer

[View problem on LeetCode](https://leetcode.com/problems/roman-to-integer/submissions/2098491391/)

- **Difficulty:** Easy
- **Language:** Code
- **Solved:** 2026-08-07 20:23 UTC
- **Runtime:** —
- **Memory:** —

## Interview overview

**Patterns:** Problem-specific reasoning

Use problem-specific reasoning to organize the key decisions, then verify the invariants against an edge case.

### Solution replay

```mermaid
flowchart TD
  n0["Goal<br/>Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M."]
  n1["Sample input<br/>s = 'III'"]
  n2["Step 1: Initialize<br/>Create the required working state"]
  n3["Step 2: Process<br/>Update state from the current input"]
  n4["Step 3: Return<br/>Produce the result from the completed state"]
  n5["Sample output<br/>Expected output: 3"]
  inv["Invariant<br/>Each step preserves the information needed to compute the final result."]
  n0 --> n1 --> n2 --> n3 --> n4 --> n5
  inv -.-> n2
  inv -.-> n3
  inv -.-> n4
```

### Approach

1. State the direct approach and identify its bottleneck.
2. Explain why problem-specific reasoning fits the constraints.
3. Walk through one edge case and justify the final complexity.

---
_Synced by [LeetRepo](https://github.com/)_