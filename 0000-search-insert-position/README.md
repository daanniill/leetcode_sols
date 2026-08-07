# 0. Search Insert Position

[View problem on LeetCode](https://leetcode.com/problems/search-insert-position/submissions/2098469873/)

- **Difficulty:** Easy
- **Language:** Code
- **Runtime:** —
- **Memory:** —

## Interview overview

**Patterns:** Binary Search

This solution finds the index where a target value should be inserted in a sorted list to maintain sorted order. It uses a binary search approach to achieve this. The function returns the index of the target if found, or the index where it should be inserted.

### Approach

1. Initialize two pointers, one at the start and one at the end of the list
2. Loop until the two pointers meet, calculating the middle index at each iteration
3. Compare the middle element to the target, adjusting the pointers accordingly
4. If the target is found, return its index; otherwise, continue the loop
5. If the loop ends without finding the target, return the index where the target should be inserted

### Complexity

- **Time:** O(log n), because the solution uses binary search, which divides the search space in half at each step
- **Space:** O(1), because the solution only uses a constant amount of space to store the pointers and the target

### Complexity self-check

- **Verdict:** optimal
- **Intended:** O(log n) time and O(1) space
- This solution is optimal because it uses binary search, which is the most efficient algorithm for searching a sorted list

### Edge cases

- An empty list, in which case the function returns 0
- A list with a single element, in which case the function returns 0 if the target is less than or equal to the element, and 1 otherwise
- A list with duplicate elements, in which case the function returns the index of the first occurrence of the target if it exists, or the index where it should be inserted

_AI-generated with Groq; verify the analysis before relying on it._

## Personal notes

this is basically just binary search

---
_Synced by [LeetRepo](https://github.com/)_