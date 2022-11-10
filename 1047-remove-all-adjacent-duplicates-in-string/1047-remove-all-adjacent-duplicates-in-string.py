class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        i = 0
        
        while i < len(s):
            if len(stack) != 0 and stack[-1] == s[i]:
                i += 1
                stack.pop()
            else:
                stack.append(s[i])
                i += 1
        return "".join(stack)
        