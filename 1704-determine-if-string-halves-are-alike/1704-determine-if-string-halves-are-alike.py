class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vovels = "aeiou"
        count = 0

        half_index = (len(s) // 2)  # start of second part

        for i, char in enumerate(s.lower()):
            if char in vovels:
                if i < half_index:
                    count += 1
                else:
                    count -= 1
        
        return count == 0
