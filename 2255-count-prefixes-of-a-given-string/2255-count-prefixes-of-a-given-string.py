class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        k = [0 for i in words if s[:len(i)]==i]
        return len(k)