class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = len(nums)//2 + 1
        
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i, value in d.items():
            if value>=k:
                return i