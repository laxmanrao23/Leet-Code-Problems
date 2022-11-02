class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f, l = 0, len(numbers) - 1
        
        sum1 = 0
        while f < l:
            sum1 = numbers[f] + numbers[l]
            if sum1 == target:
                return [f+1, l+1]
            elif sum1 < target:
                f += 1
            else:
                l -= 1
                