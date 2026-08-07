# 0. Search Insert Position

[View problem on LeetCode](https://leetcode.com/problems/search-insert-position/)

- **Difficulty:** Unknown
- **Language:** Code
- **Solved:** 2026-08-07 22:00 UTC
- **Runtime:** —
- **Memory:** —

## Interview overview

**Patterns:** Binary Search

This solution finds the index where a target value should be inserted in a sorted list to maintain sorted order. It uses a binary search approach to achieve this. The function returns the index where the target should be inserted.

### Solution replay

```mermaid
flowchart TD
  n0["Goal<br/>Find the index where 5 should be inserted in the sorted list [1, 3, 5, 6] to maintain sorted order"]
  n1["Sample input<br/>[1, 3, 5, 6], 5"]
  n2["Step 1: l = 0, r = 3<br/>l &lt;= r"]
  n3["Step 2: m = 1<br/>nums[m] &lt; target"]
  n4["Step 3: l = 2<br/>l &lt;= r"]
  n5["Step 4: m = 2<br/>nums[m] == target"]
  n6["Sample output<br/>2, the index where 5 is already present"]
  inv["Invariant<br/>The list remains sorted"]
  n0 --> n1 --> n2 --> n3 --> n4 --> n5 --> n6
  inv -.-> n2
  inv -.-> n3
  inv -.-> n4
  inv -.-> n5
```

### Approach

1. Initialize two pointers, left and right, to the start and end of the list
2. Loop until left is less than or equal to right
3. Calculate the middle index and compare the middle element to the target
4. If the middle element is equal to the target, return the middle index
5. If the middle element is greater than the target, update the right pointer to the index before the middle
6. If the middle element is less than the target, update the left pointer to the index after the middle

### Complexity

- **Time:** O(log n), where n is the number of elements in the list, because we divide the search space in half at each step
- **Space:** O(1), because we only use a constant amount of space to store the pointers and the target

### Complexity self-check

- **Verdict:** optimal
- **Intended:** O(log n) time and O(1) space
- This is the best possible time complexity for this problem because we must examine each element at least once in the worst case

### Edge cases

- An empty list
- A list with one element
- A list with duplicate elements
- A target that is less than the smallest element in the list

_AI-generated with Groq; verify the analysis before relying on it._

## Personal notes

this is basically just binary search

---
_Synced by [LeetRepo](https://github.com/)_