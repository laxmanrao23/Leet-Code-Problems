class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        nums.append(target)
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        
        left, right = 0, len(nums) - 1
        
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid]==target:
                return mid
            elif target < nums[mid]:
                right -= 1
            else:
                left += 1   
            