class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        visited_numbers = set()

        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] not in visited_numbers:
                visited_numbers.add(nums[i])
        
        print(visited_numbers)
        for i in range(1, len(nums)+1):
            if i not in visited_numbers:
                return i
        
        return len(nums) + 1