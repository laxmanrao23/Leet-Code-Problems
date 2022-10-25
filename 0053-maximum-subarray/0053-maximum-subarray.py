class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''s =[]
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                sub = nums[i:j]
                s.append(sum(sub))
        max1 = s[0]
        for i in range(len(s)-1):
            if s[i] > max1:
                max1 = s[i]
        return max1'''
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
                
        