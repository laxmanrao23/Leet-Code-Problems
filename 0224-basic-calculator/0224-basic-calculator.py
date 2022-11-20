class Solution:
    def calculate(self, s: str) -> int:
        output = 0
        curr = 0
        sign = 1
        stack = []

        for ch in s:
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            elif ch in "+-":
                output += (curr * sign)
                curr = 0
                if ch == "-":
                    sign = -1
                else:
                    sign = 1
            elif ch =="(":
                stack.append(output)
                stack.append(sign)
                output = 0
                sign = 1
            elif ch == ")":
                output += curr*sign
                output *= stack.pop()
                output += stack.pop()
                curr = 0
        return output +(curr*sign)