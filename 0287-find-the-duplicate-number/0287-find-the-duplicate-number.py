class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        print(d)
        for key, value in d.items():
            if value > 1:
                return key