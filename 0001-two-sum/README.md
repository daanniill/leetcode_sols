# 1. Two Sum

[View problem on LeetCode](https://leetcode.com/problems/two-sum/submissions/2106010860/)

- **Difficulty:** Easy
- **Language:** Python3
- **Solved:** 2026-08-13 23:40 UTC
- **Runtime:** —
- **Memory:** —

## Problem description

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

## Interview overview

**Patterns:** hash‑map lookup, single‑pass complement search

The solution scans the list once, storing each number with its index in a hash map. For each element it checks if the complement (target‑num) already exists, returning the pair of indices when found.

### Solution replay

```mermaid
flowchart TD
  n0["Goal<br/>You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target."]
  n1["Sample input<br/>nums = [2,7,11,15], target = 9"]
  n2["Step 1: Initialize<br/>Create the required working state"]
  n3["Step 2: Process<br/>Update state from the current input"]
  n4["Step 3: Return<br/>Produce the result from the completed state"]
  n5["Sample output<br/>Expected output: [0,1]"]
  inv["Invariant<br/>Each step preserves the information needed to compute the final result."]
  n0 --> n1 --> n2 --> n3 --> n4 --> n5
  inv -.-> n2
  inv -.-> n3
  inv -.-> n4
```

### Approach

1. Initialize empty hash map
2. Iterate over indices i from 0 to len(nums)-1
3. Compute complement = target - nums[i]
4. If complement is in hash map, return [hashmap[complement], i]
5. Otherwise store nums[i] with index i in the map

### Complexity

- **Time:** O(n) – each element is processed once with O(1) look‑ups
- **Space:** O(n) – worst‑case storage of all elements in the hash map

### Complexity self-check

- **Verdict:** optimal
- **Intended:** O(n) time, O(n) space
- Sorting + two‑pointer could reduce space but changes problem constraints

_AI-generated with Groq; verify the analysis before relying on it._

---
_Synced by [LeetRepo](https://github.com/)_