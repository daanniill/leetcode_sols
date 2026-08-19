class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = len(s) - 1
        for i in range(end // 2 + 1):
            s[i], s[end - i] = s[end - i], s[i]
