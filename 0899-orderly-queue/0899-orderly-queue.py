class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        
        res = s
        print(res)
        for i in range(0,len(s)):
            s = s[1:] + s[0]
            #print(s)
            res = min(res,s)
                
       # print(res)
        return res