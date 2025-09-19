# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.dfs(root,"",res)
        return res
    def dfs(self,node,string,res):
        if node:
            if node.left or node.right:
                string += f"{node.val}->" 
            if not node.left and not node.right:
                string += f"{node.val}"
                res.append(string)
            if node.left:
                self.dfs(node.left,string,res)
            if node.right:
                self.dfs(node.right,string,res)