class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        k = ""
        l = ""
        for i in word1:
            k += i
        for i in word2:
            l += i
        if k==l:
            return True
        return False