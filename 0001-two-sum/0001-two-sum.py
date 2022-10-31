class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''ans = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j] == target:
                    ans.append(i)
                    
        return ans'''
    
        prevMap = {} # val : index
    
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return