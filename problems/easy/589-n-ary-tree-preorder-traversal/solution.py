"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        self.display(root,result)
        return result
    def display(self,node,result):
        if not node:
            return result
        result.append(node.val)
        for child in node.children:
            self.display(child,result)
        return result