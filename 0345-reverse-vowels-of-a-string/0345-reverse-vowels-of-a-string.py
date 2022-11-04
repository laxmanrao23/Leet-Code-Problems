class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [0] * len(s)
        s = list(s)
        print(s)
        j = 0
        
        def isvowel(a):
            l = ["a","A","e","E","i","I","o","O","u","U"]
            if a in l:
                return True
            return False
        
        for i in range(len(s)):
            if isvowel(s[i]):
                vowels[j] = s[i]
                j += 1
        print(vowels)
        for i in range(len(s)):
            if isvowel(s[i]):
                j -= 1
                s[i]=vowels[j]
                
        
        print(s)
        return ''.join(s)