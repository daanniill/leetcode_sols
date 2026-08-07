# 0. Roman To Integer

[View problem on LeetCode](https://leetcode.com/problems/roman-to-integer/)

- **Difficulty:** Easy
- **Language:** Code
- **Runtime:** 0 ms
- **Memory:** —

## Interview overview

**Patterns:** Hash Table, String Manipulation

The solution converts a Roman numeral string to an integer by replacing subtractive notation with additive notation and then summing the values of each character. It uses a dictionary to map Roman numerals to their integer values. The function iterates over the modified string, adding the value of each character to a running total.

### Approach

1. Create a dictionary to map Roman numerals to their integer values
2. Replace subtractive notation in the input string with additive notation
3. Initialize a variable to store the total integer value
4. Iterate over each character in the modified string, adding its value to the total

### Complexity

- **Time:** O(n)
- **Space:** O(1)

### Edge cases

- Empty string input
- Input string containing only a single Roman numeral
- Input string containing a mix of additive and subtractive notation

_AI-generated with Groq; verify the analysis before relying on it._

---
_Synced by [LeetRepo](https://github.com/)_