class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]
        
        for i in s[1:]:
            if len(stack) > 0:
                if i.islower():
                    if ord(stack[-1]) + 32 == ord(i):
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    if i.upper():
                        if ord(stack[-1]) - 32 == ord(i):
                            stack.pop()
                        else:
                            stack.append(i)
            else:
                stack.append(i)
                
        return "".join(stack)
                
        