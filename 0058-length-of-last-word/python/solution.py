class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        first_word = []
        for c in reversed(s):
            if c == " " and not first_word:
                continue
            elif c == " ":
                first_word.append(c)
        
                return len(first_word)
            else:
        return len(first_word)
