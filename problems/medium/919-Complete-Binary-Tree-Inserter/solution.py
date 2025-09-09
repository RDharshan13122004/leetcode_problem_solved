# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = []

        bfs = [root]
        while bfs:
            node = bfs.pop(0)
            if not node.left or not node.right:
                self.queue.append(node)
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        parent_node = self.queue[0]
        if not parent_node.left:
            parent_node.left = new_node
        elif not parent_node.right:
            parent_node.right = new_node
            self.queue.pop(0)
        
        self.queue.append(new_node)
        return parent_node.val
        
    def get_root(self) -> Optional[TreeNode]:
        return self.root        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()