from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        nn = len(word1)
        m = len(word2)

        last = [-1] * m

        i = nn - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1

            i -= 1

        ans = []
        can_skip = True
        j = 0
