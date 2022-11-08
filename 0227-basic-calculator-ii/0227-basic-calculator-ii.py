class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return '0'
        stack=[]
        op = '+'
        num = 0
        for e,i  in enumerate(s):
            if i =="": # ignore spaces in string
                continue
            if i.isdigit():
                num = num * 10 + int(i)  # as string could be "0+123" this 123 will be append to the stack together.
            if i in "+-*/" or e==len(s)-1: # this e==len(s)-1 is because last char in string will be a number and we have to append it too.
                if op =='-':
                    stack.append(-num)
                elif op=='+':
                    stack.append(num)
                elif op=='*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                op=i
                num=0
        #print(stack)
        return sum(stack)
