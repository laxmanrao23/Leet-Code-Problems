class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        l=len(grid)
        for i in range(l):
            for j in range(l):
                if (grid[i][j] != 0) and ((i==j) or (i+j==l-1)):
                    pass
                elif (grid[i][j] == 0) and ((i!=j) and (i+j!=l-1)):
                    pass
                else:
                    return False
        return True