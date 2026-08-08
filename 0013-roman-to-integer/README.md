# 13. Roman to Integer

[View problem on LeetCode](https://leetcode.com/problems/roman-to-integer/submissions/2098518654/)

- **Difficulty:** Easy
- **Language:** JavaScript
- **Solved:** 2026-08-08 00:05 UTC
- **Runtime:** —
- **Memory:** —

## Interview overview

**Patterns:** Hash Table, Greedy Algorithm

Convert Roman numerals to integers by iterating through the string and adding or subtracting values based on the current and next characters. The conversion uses a dictionary to map Roman numerals to their integer values.

### Solution replay

```mermaid
flowchart TD
  n0["Goal<br/>Converting 'III' to an integer"]
  n1["Sample input<br/>III"]
  n2["Step 1: i=0<br/>res=1"]
  n3["Step 2: i=1<br/>res=2"]
  n4["Step 3: i=2<br/>res=3"]
  n5["Sample output<br/>3, the integer value of 'III'"]
  inv["Invariant<br/>Result is cumulative sum"]
  n0 --> n1 --> n2 --> n3 --> n4 --> n5
  inv -.-> n2
  inv -.-> n3
  inv -.-> n4
```

### Approach

1. Create a dictionary to map Roman numerals to their integer values
2. Initialize a variable to store the result
3. Iterate through the string, comparing each character with the next one
4. Add or subtract the current character's value based on the comparison
5. Add the last character's value to the result

### Complexity

- **Time:** O(n), where n is the length of the string
- **Space:** O(1), as the dictionary has a constant size

### Complexity self-check

- **Verdict:** optimal
- **Intended:** O(n) time and O(1) space
- Linear time complexity due to a single pass through the string

### Edge cases

- Empty string
- Single character
- String with only one type of numeral
- String with subtractive notation (e.g., IV)

_AI-generated with Groq; verify the analysis before relying on it._

---
_Synced by [LeetRepo](https://github.com/)_