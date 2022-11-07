class Solution:
    def maximum69Number (self, num: int) -> int:
        l = str(num)
        
        return int(l.replace("6", "9", 1))
        
        