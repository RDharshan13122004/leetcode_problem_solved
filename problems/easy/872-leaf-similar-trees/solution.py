# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 =[]
        leaf2 = [] 
        self.leaf(root1,leaf1)
        self.leaf(root2,leaf2)
        return leaf1 == leaf2

    def leaf(self,node,lf):
        if not node.left and not node.right:
            lf.append(node.val)
        if node.left:
            self.leaf(node.left,lf)
        if node.right:
            self.leaf(node.right,lf)