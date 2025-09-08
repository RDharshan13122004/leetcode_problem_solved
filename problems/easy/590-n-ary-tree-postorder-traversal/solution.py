"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        self.display(root,result)
        return result
    def display(self,node,result):
        if not node:
            return result
        for child in node.children:
            self.display(child,result)
        result.append(node.val)        
        return result