# 257. Binary Tree Paths

**Difficulty**: Easy  
**Acceptance Rate**: 63.5%  
**Problem Link**: [LeetCode #257](https://leetcode.com/problems/binary-tree-paths/)

## Problem Description

Given the root of a binary tree, return all root-to-leaf paths in any order. A leaf is a node with no children.

## Examples

### Example 1:
```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

**Visual Representation:**
```
   1
 /   \
2     3
 \
  5

Paths:
1 -> 2 -> 5
1 -> 3
```

### Example 2:
```
Input: root = [1]
Output: ["1"]
```

### Example 3:
```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Definition for a binary tree node

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Key Insights

1. **Root-to-Leaf Path**: Start at the root node. Recursively traverse the left and right subtrees of the current node, adding the current node's value to the current path
2. **Leaf Node**: A node with no left and right children
3. **DFS Traversal**: Natural fit for exploring all paths from root to leaves
4. **Path Construction**: Build path string as we traverse, backtrack when needed
5. **String Format**: Paths are represented as "node1->node2->node3"

## Approach Ideas

### 1. DFS with Path Building (Recommended)
- Use DFS to traverse the tree
- Build path string as we go deeper
- When leaf is reached, add complete path to result
- Time: O(n × h), Space: O(n × h)

### 2. DFS with Backtracking
- Maintain a path list and backtrack after exploring each subtree
- Convert path to string format when leaf is reached
- Time: O(n × h), Space: O(h)

### 3. BFS with Path Tracking
- Use queue to store (node, current_path) pairs
- Process level by level until leaves are reached
- Time: O(n × h), Space: O(n × h)

## DFS Path Building Implementation (Recommended)

```python
def binaryTreePaths(root):
    if not root:
        return []
    
    result = []
    
    def dfs(node, path):
        # Base case: leaf node
        if not node.left and not node.right:
            result.append(path)
            return
        
        # Recursively explore left and right subtrees
        if node.left:
            dfs(node.left, path + "->" + str(node.left.val))
        if node.right:
            dfs(node.right, path + "->" + str(node.right.val))
    
    dfs(root, str(root.val))
    return result
```

## DFS with Backtracking Implementation

```python
def binaryTreePaths(root):
    if not root:
        return []
    
    result = []
    path = []
    
    def dfs(node):
        # Add current node to path
        path.append(str(node.val))
        
        # If leaf node, add path to result
        if not node.left and not node.right:
            result.append("->".join(path))
        else:
            # Explore children
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        
        # Backtrack: remove current node from path
        path.pop()
    
    dfs(root)
    return result
```

## BFS Implementation

```python
from collections import deque

def binaryTreePaths(root):
    if not root:
        return []
    
    result = []
    queue = deque([(root, str(root.val))])
    
    while queue:
        node, path = queue.popleft()
        
        # If leaf node, add path to result
        if not node.left and not node.right:
            result.append(path)
        
        # Add children to queue with updated paths
        if node.left:
            queue.append((node.left, path + "->" + str(node.left.val)))
        if node.right:
            queue.append((node.right, path + "->" + str(node.right.val)))
    
    return result
```

## Step-by-Step DFS Example

For tree `[1,2,3,null,5]`:

```
Initial call: dfs(1, "1")

1. At node 1:
   - Not a leaf (has children)
   - Explore left child 2: dfs(2, "1->2")
   
2. At node 2:
   - Not a leaf (has right child 5)
   - No left child to explore
   - Explore right child 5: dfs(5, "1->2->5")
   
3. At node 5:
   - Leaf node! Add "1->2->5" to result
   - Return to node 2
   
4. Back at node 2, done with children, return to node 1

5. At node 1, explore right child 3: dfs(3, "1->3")

6. At node 3:
   - Leaf node! Add "1->3" to result
   
Final result: ["1->2->5", "1->3"]
```

## Algorithm Comparison

| Approach | Time Complexity | Space Complexity | Pros | Cons |
|----------|----------------|------------------|------|------|
| DFS Path Building | O(n × h) | O(n × h) | Simple, intuitive | String concatenation overhead |
| DFS Backtracking | O(n × h) | O(h) | Space efficient | Slightly more complex |
| BFS | O(n × h) | O(n × h) | Level-order exploration | Queue overhead |

Where:
- n = number of nodes
- h = height of tree (average case: log n, worst case: n)

## Edge Cases

1. **Empty tree**: `root = null` → return `[]`
2. **Single node**: `root = [1]` → return `["1"]`
3. **Only left children**: Linear tree going left
4. **Only right children**: Linear tree going right
5. **Complete binary tree**: All levels filled
6. **Negative values**: Handle negative node values correctly

## Time and Space Complexity

### DFS Path Building:
- **Time Complexity**: O(n × h) where n is nodes, h is average path length
  - Visit each node once: O(n)
  - For each leaf, create path string of average length h: O(h)
  - Total: O(n × h)
- **Space Complexity**: O(n × h) for storing all paths

### DFS Backtracking:
- **Time Complexity**: O(n × h)
- **Space Complexity**: O(h) for recursion stack and path array

## Common Mistakes

1. **Forgetting leaf check**: Must verify `not node.left and not node.right`
2. **String format**: Paths should use `"->"` as separator
3. **Empty tree handling**: Return empty list for null root
4. **Path building**: Ensure proper concatenation with arrow symbols
5. **Backtracking errors**: In backtracking approach, must remove node after exploring

## Follow-up Questions

1. **What if we want paths to all nodes, not just leaves?** Modify to add path at every node
2. **What if we want the longest path?** Track maximum length during traversal
3. **Can you do it iteratively?** Yes, using BFS or explicit stack
4. **What about paths with specific sum?** Similar to path sum problems

## Related Problems

- **112. Path Sum**: Check if root-to-leaf path with target sum exists
- **113. Path Sum II**: Find all root-to-leaf paths with target sum
- **129. Sum Root to Leaf Numbers**: Sum all root-to-leaf path numbers
- **437. Path Sum III**: Count paths with target sum (not necessarily root-to-leaf)

## Tags
- Tree
- Depth-First Search
- Breadth-First Search
- String
- Binary Tree
- Backtracking