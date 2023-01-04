class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = {}
        c = 0
        for i in tasks:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for val in d.values():
            if val==1:
                return -1
            k = val//3 + min(1, val%3)
            c += k
        return c