class Solution:
    def isValid(self, s: str) -> bool:
        combos = {'}':'{', ')':'(', ']':'['}
        stack = []

        for c in s:
            if c in combos:
                if stack and stack[-1] == combos[c]:
                    stack.pop()
                else:
                    return False
                stack.append(c)
        
        return True if not stack else False
            else:
