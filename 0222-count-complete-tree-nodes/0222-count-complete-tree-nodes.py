# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        output = [0]
        if root is None:
            return 0
        def dfs(node,output):
            if not node:
                return
            output[0] +=1
            dfs(node.left,output)
            dfs(node.right,output)

        dfs(root,output)
        return output[0]