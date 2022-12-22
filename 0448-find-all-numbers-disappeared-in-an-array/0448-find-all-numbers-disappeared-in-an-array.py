class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k = set()
        for i in range(1,len(nums)+1):
            k.add(i)
        print(k)
        return list(k-set(nums))