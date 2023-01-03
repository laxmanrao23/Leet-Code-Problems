class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        s_len = len(strs[0])
        ans = 0
        for i in range(s_len):
            s_n = ""
            for s in strs:
                s_n += s[i]
            if s_n != "".join(sorted(s_n)):
                ans += 1
        return ans
        