class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s.split())
        k = s[::-1]
        l = ""
        for i in k:
            l += i
            l += " "
        return l.rstrip()