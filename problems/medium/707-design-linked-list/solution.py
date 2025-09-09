# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        self.insert(root,val)
        return root

    def insert(self,node,val):
        if val < node.val:
            if node.left:
                self.insert(node.left,val)
            else:
                node.left = TreeNode(val)
        elif val > node.val:
            if node.right:
                self.insert(node.right,val)
            else:
                node.right = TreeNode(val)