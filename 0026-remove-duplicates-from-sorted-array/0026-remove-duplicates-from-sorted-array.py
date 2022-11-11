class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """hashmap=set()
        K=0
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap.add(nums[i])
                nums[K]=nums[i]
                K+=1
            else:
                continue         
        return K
        """
        
        d = set()
        m = 0
        for i in range(len(nums)):
            if nums[i] not in d:
                d.add(nums[i])
                nums[m]=nums[i]
                m += 1
            else:
                continue
        return m
        
            
                
            
        
        