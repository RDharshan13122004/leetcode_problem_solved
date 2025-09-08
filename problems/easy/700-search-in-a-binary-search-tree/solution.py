# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.recursive_search(root,val)

    def recursive_search(self,node,value):
        if not node:
            return None
        elif node.val == value:
            return node
        elif value < node.val:
            return self.recursive_search(node.left,value)
        elif value > node.val:
            return self.recursive_search(node.right,value)