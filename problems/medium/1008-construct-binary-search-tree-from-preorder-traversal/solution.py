# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        for i in range(0,len(preorder)):
            if not root:
                root = TreeNode(preorder[i])
            else:
                self.insert(root,preorder[i])
        return root

    def insert(self,node,data):
        if data < node.val:
            if node.left:
                self.insert(node.left,data)
            else:
                node.left = TreeNode(data)
        elif data > node.val:
            if node.right:
                self.insert(node.right,data)
            else:
                node.right = TreeNode(data) 