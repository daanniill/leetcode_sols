# 344. Reverse String

[View problem on LeetCode](https://leetcode.com/problems/reverse-string/submissions/2113213682/)

- **Difficulty:** Easy
- **Language:** Python3
- **Solved:** 2026-08-19 20:16 UTC
- **Runtime:** 0 ms
- **Memory:** —

## Problem description

Write a function that reverses a string. The input string is given as an array of characters s.

## Interview overview

**Patterns:** two‑pointer technique, in‑place array reversal, element swapping

The solution swaps characters from the ends toward the center using a two‑pointer in‑place approach. It iterates only up to the midpoint, achieving reversal without extra storage.

### Solution replay

```mermaid
flowchart TD
  n0["Goal<br/>Reverse the character array in place so the output is the original order flipped"]
  n1["Sample input<br/>['h','e','l','l','o']"]
  n2["Step 1: i=0 swap 0↔4<br/>['o','e','l','l','h']"]
  n3["Step 2: i=1 swap 1↔3<br/>['o','l','l','e','h']"]
  n4["Step 3: i=2 swap 2↔2 (no change)<br/>['o','l','l','e','h']"]
  n5["Sample output<br/>['o','l','l','e','h'] – the array is fully reversed"]
  inv["Invariant<br/>Elements at symmetric positions from the ends are swapped, the middle element (if any) remains unchanged"]
  n0 --> n1 --> n2 --> n3 --> n4 --> n5
  inv -.-> n2
  inv -.-> n3
  inv -.-> n4
```

### Approach

1. Compute last index `end = len(s)-1`
2. Loop `i` from 0 through `end//2` inclusive
3. Swap `s[i]` with `s[end‑i]` each iteration
4. Continue until the middle is reached

### Complexity

- **Time:** O(n) because each character is visited at most once
- **Space:** O(1) as only a few integer variables are used

### Complexity self-check

- **Verdict:** optimal
- **Intended:** O(n) time, O(1) extra space
- A Python slice `s[::-1]` would also be O(n) time but uses O(n) extra space; this method is optimal for in‑place requirement

### Edge cases

- Empty list []
- Single character ['a']
- Even length list e.g., ['a','b','c','d']
- Odd length list where middle stays unchanged

_AI-generated with Groq; verify the analysis before relying on it._

---
_Synced by [LeetRepo](https://github.com/)_