class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        freq = [False] * len(nums)
        print(freq)
        def backtrack(ansArr):
            if len(ansArr) == len(nums):
                res.append(ansArr[:])
                return
				
            for i in range(len(nums)):
                if not freq[i]:
                    freq[i] = True
                    ansArr.append(nums[i])
                    backtrack(ansArr)
                    ansArr.pop()
                    freq[i] = False

        backtrack([])
        return res
        