class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(s.split())
        pattern = [i for i in pattern]
        
        mapPS, mapSP = {}, {}
        if len(s)!=len(pattern):
            return False
        
        for c1, c2 in zip(pattern, s):
            if ((c1 in mapPS and mapPS[c1] != c2) or
               (c2 in mapSP and mapSP[c2] != c1)):
                return False
            mapPS[c1] = c2
            mapSP[c2] = c1
        return True