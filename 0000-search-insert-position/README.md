# 0. Search Insert Position

[View problem on LeetCode](https://leetcode.com/problems/search-insert-position/submissions/2098490476/)

- **Difficulty:** Easy
- **Language:** Code
- **Solved:** 2026-08-07 22:00 UTC
- **Runtime:** 0 ms
- **Memory:** —

## Interview overview

**Patterns:** Two Pointers, Sliding Window, Binary Search

Use two pointers to organize the key decisions, then verify the invariants against an edge case.

### Solution replay

```mermaid
flowchart TD
  n0["Goal<br/>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order."]
  n1["Sample input<br/>nums = [1,3,5,6], target = 5"]
  n2["Step 1: Position pointers<br/>Start at the relevant boundaries"]
  n3["Step 2: Compare state<br/>Choose which pointer must move"]
  n4["Step 3: Narrow the search<br/>Repeat until the answer is determined"]
  n5["Sample output<br/>Expected output: 2"]
  inv["Invariant<br/>Everything outside the pointers has already been resolved."]
  n0 --> n1 --> n2 --> n3 --> n4 --> n5
  inv -.-> n2
  inv -.-> n3
  inv -.-> n4
```

### Approach

1. State the direct approach and identify its bottleneck.
2. Explain why two pointers fits the constraints.
3. Walk through one edge case and justify the final complexity.

## Personal notes

this is basically just binary search

---
_Synced by [LeetRepo](https://github.com/)_