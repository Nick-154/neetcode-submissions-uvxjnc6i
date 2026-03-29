class Solution:
    def isValid(self, s: str) -> bool:
        need = {')':'(',']':'[','}':'{'}
    
        stack = []

        for i in s: 
            if i in need: 
                if not stack or stack[-1] != need[i]:
                    return False

                stack.pop()

            else:

                stack.append(i)
        return len(stack) == 0