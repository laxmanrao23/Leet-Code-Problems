class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        l = ""
        p = []
        for i in num:
            l += str(i)
        print(l)
        m = int(l) + k
        
        for i in str(m):
            p.append(int(i))
        return p
            
            
        