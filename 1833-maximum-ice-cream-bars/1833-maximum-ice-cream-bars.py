class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        k = sorted(costs)
        c = 0
        i = 0
        while i < len(k) and k[i] <= coins:
                coins = coins - k[i]
                c += 1
                i += 1
        return c
            
            
                
                
            
        