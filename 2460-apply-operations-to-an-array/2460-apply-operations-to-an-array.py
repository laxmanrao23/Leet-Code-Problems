class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
    
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            else:
                continue
        
        return [nonZero for nonZero in nums if nonZero != 0] + [zero for zero in nums if zero==0]
        
        