# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def dfs(node):
            if not node:
                val.append("null")
                return 
            val.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        val = []
        dfs(root)
        return ",".join(val)

    def deserialize(self, data):
        def dfs():
            val = next(vals)
            if val == "null":
                return None
            
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        vals = iter(data.split(","))
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))