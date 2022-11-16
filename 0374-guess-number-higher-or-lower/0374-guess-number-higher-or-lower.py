class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n + 1
        
        while True:
            mid = (l + r) // 2
            res = guess(mid)
            if res == 0: return mid
            elif res == -1: r = mid - 1
            else: l = mid + 1