# 0. Search Insert Position

[View problem on LeetCode](https://leetcode.com/problems/search-insert-position/submissions/2098469873/)

- **Difficulty:** Unknown
- **Language:** Code
- **Runtime:** —
- **Memory:** —

## Interview overview

**Patterns:** Binary Search

This solution uses binary search to find the position of a target in a sorted list. If the target is found, its index is returned; otherwise, the index where it should be inserted is returned. The algorithm maintains a search range [l, r] and iteratively narrows it down.

### Solution replay

```mermaid
flowchart TD
  n0["Goal<br/>The goal is to find the position of the target in the sorted list, and the output represents the index where the target should be inserted"]
  n1["Sample input<br/>[1, 3, 5, 6] with target 5"]
  n2["Step 1: l = 0, r = 3<br/>search range: [1, 3, 5, 6]"]
  n3["Step 2: m = 1<br/>compare 3 to 5"]
  n4["Step 3: r = 1<br/>search range: [1, 3]"]
  n5["Step 4: m = 2<br/>compare 5 to 5"]
  n6["Sample output<br/>2, the index where the target 5 is found"]
  inv["Invariant<br/>The search range [l, r] always contains the target if it exists"]
  n0 --> n1 --> n2 --> n3 --> n4 --> n5 --> n6
  inv -.-> n2
  inv -.-> n3
  inv -.-> n4
  inv -.-> n5
```

### Approach

1. Initialize the search range [l, r] to the entire list
2. Calculate the middle index m of the current search range
3. Compare the middle element to the target and adjust the search range accordingly
4. Repeat the comparison and adjustment until the target is found or the search range is empty
5. If the target is not found, return the index where it should be inserted

### Complexity

- **Time:** O(log n) because the algorithm divides the search space in half at each step
- **Space:** O(1) because only a constant amount of space is used

### Complexity self-check

- **Verdict:** optimal
- **Intended:** O(log n) time and O(1) space
- This is the best possible time complexity for searching in a sorted list

### Edge cases

- An empty list
- A list with a single element
- A list where the target is the smallest or largest element

_AI-generated with Groq; verify the analysis before relying on it._

## Personal notes

this is basically just binary search

---
_Synced by [LeetRepo](https://github.com/)_