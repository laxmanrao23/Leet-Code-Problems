class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        
        for i in arr:
            if i not in d:
                d[i] = 1
            d[i] += 1
        print(d)
        k = [val for i, val in d.items()]
        if len(k)==len(set(k)):
             return True 
        return False
        