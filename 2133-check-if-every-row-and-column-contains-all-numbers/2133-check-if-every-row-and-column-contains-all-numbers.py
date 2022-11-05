class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        valid = set(range(1,n+1))
        
        for i in range(n):
            s1, s2 = set(), set()
            for j in range(n):
                s1.add(matrix[i][j])
                s2.add(matrix[j][i])
            if s1!=valid or s2!=valid:
                return False
        return True
                