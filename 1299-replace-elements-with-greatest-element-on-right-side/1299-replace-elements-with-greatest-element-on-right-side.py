class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = 1
        n =len(arr)
        
        l = []
        while i < n:
            l.append(max(arr[i:n]))
            i += 1
        l.append(-1)
        return l
        