"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        tobevisited = [root]
        result = []
        while tobevisited:
            level = []
            next_queue = []
            for node in tobevisited:
                level.append(node.val)
                next_queue.extend(node.children) 
            result.append(level)
            tobevisited = next_queue
        return result
        