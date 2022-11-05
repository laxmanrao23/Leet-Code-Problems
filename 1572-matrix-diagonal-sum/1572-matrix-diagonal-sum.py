class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        ans = 0
        
        for i in range(n):
            ans += mat[i][i]
        for i in range(len(mat) -1, -1, -1):
            if len(mat) and (len(mat) - i -1)==i:
                continue
            ans += mat[len(mat) - i - 1][i]
            
        return ans