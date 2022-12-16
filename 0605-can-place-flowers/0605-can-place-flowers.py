class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        add = [0] + flowerbed + [0]
        
        for i in range(1, len(add)-1):
            if add[i - 1]==0 and add[i]==0 and add[i + 1]==0:
                add[i] = 1
                n -= 1
        return n<=0