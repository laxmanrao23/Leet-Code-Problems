class Solution:
    def capitalizeTitle(self, title: str) -> str:
        k = list(title.split())
        l = []
        m = ''
        for i in k:
            if len(i) > 2:
                l.append(i.title())
            else:
                p = ""
                for j in i:
                    p += j.lower()
                l.append(p)
    
        return " ".join(l)