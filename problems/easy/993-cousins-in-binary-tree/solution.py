# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        tobevisited = [root]
        x_found = y_found = False
        while tobevisited:
            size = len(tobevisited)
            
            for _ in range(size):
                node = tobevisited.pop(0)
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                        return False
                if node.left:
                    tobevisited.append(node.left)
                    if x == node.left.val:
                        x_found = True
                    if y == node.left.val:
                        y_found = True
                if node.right:
                    tobevisited.append(node.right)
                    if x == node.right.val:
                        x_found = True
                    if y == node.right.val:
                        y_found = True
            if x_found and y_found:
                return True
            if x_found or y_found:
                return False