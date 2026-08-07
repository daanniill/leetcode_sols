# 0. Roman To Integer

[View problem on LeetCode](https://leetcode.com/problems/roman-to-integer/submissions/2098491391/)

- **Difficulty:** Easy
- **Language:** Code
- **Solved:** 2026-08-07 20:23 UTC
- **Runtime:** —
- **Memory:** —

## Interview overview

**Patterns:** Hash Table, String Replacement

Convert Roman numerals to integers by replacing subtractive notation and summing values.

### Solution replay

```mermaid
flowchart TD
  n0["Goal<br/>Converting Roman numerals to integers"]
  n1["Sample input<br/>III"]
  n2["Step 1: Replace none<br/>III"]
  n3["Step 2: Sum I<br/>II = 1 + 1"]
  n4["Step 3: Sum last I<br/>1 + 1 + 1 = 3"]
  n5["Sample output<br/>3, the integer equivalent of III"]
  inv["Invariant<br/>Total value is updated correctly"]
  n0 --> n1 --> n2 --> n3 --> n4 --> n5
  inv -.-> n2
  inv -.-> n3
  inv -.-> n4
```

### Approach

1. Create a hash table to map Roman numerals to integers
2. Replace subtractive notations with additive equivalents
3. Iterate over the modified string and sum the integer values
4. Return the total integer value

### Complexity

- **Time:** O(n), where n is the length of the input string
- **Space:** O(1), as the hash table has a constant size

### Complexity self-check

- **Verdict:** optimal
- **Intended:** O(n) time and O(1) space
- Linear time complexity due to string iteration

### Edge cases

- Empty input string
- Invalid Roman numerals
- Single-character input

_AI-generated with Groq; verify the analysis before relying on it._

---
_Synced by [LeetRepo](https://github.com/)_