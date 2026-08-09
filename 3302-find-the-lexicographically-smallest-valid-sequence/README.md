# 3302. Find the Lexicographically Smallest Valid Sequence

[View problem on LeetCode](https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/submissions/2099840524/)

- **Difficulty:** Medium
- **Language:** Python3
- **Solved:** 2026-08-09 03:48 UTC
- **Runtime:** —
- **Memory:** —

## Problem description

You are given two strings word1 and word2.

## Interview overview

**Patterns:** Two-Pointer Technique, String Comparison

This solution finds the lexicographically smallest valid sequence by comparing two input strings. It iterates through the strings from right to left. The goal is to find the longest common suffix.

### Solution replay

```mermaid
flowchart TD
  n0["Goal<br/>Find the lexicographically smallest valid sequence by comparing two strings"]
  n1["Sample input<br/>word1 = 'abc', word2 = 'bc'"]
  n2["Step 1: i = 2, j = 1<br/>last[1] = 2"]
  n3["Step 2: i = 1, j = 0<br/>last[0] = 1"]
  n4["Step 3: i = 0, j = -1<br/>break loop"]
  n5["Sample output<br/>[1, 2], the lexicographically smallest valid sequence"]
  inv["Invariant<br/>pointers move from right to left"]
  n0 --> n1 --> n2 --> n3 --> n4 --> n5
  inv -.-> n2
  inv -.-> n3
  inv -.-> n4
```

### Approach

1. Initialize two pointers at the end of each string
2. Compare characters from right to left and update the last occurrence index
3. Iterate through the second string to construct the result

### Complexity

- **Time:** O(n + m), where n and m are the lengths of the input strings
- **Space:** O(m), for storing the last occurrence index

### Complexity self-check

- **Verdict:** optimal
- **Intended:** O(n + m) time and O(m) space
- linear time complexity is the best for this problem

### Edge cases

- Empty strings
- Strings of different lengths
- Strings with no common characters

_AI-generated with Groq; verify the analysis before relying on it._

---
_Synced by [LeetRepo](https://github.com/)_