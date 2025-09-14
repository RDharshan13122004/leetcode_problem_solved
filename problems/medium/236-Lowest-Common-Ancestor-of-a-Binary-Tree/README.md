# 236. Lowest Common Ancestor of a Binary Tree

**Difficulty**: Medium  
**Acceptance Rate**: 60.8%  
**Problem Link**: [LeetCode #236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## Problem Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself)."

## Examples

### Example 1:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
```

### Example 2:
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
```

### Example 3:
```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

## Visual Representation

```
Example Tree:
        3
      /   \
     5     1
   /  \   /  \
  6    2 0    8
      / \
     7   4

For p=5, q=1: LCA is 3 (root)
For p=5, q=4: LCA is 5 (p itself)
For p=6, q=7: LCA is 5
For p=0, q=8: LCA is 1
```

## Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the tree.

## Definition for a binary tree node

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```

## Key Insights

1. **LCA Definition**: The LCA is the deepest node that has both p and q as descendants
2. **Node as Descendant**: A node can be a descendant of itself
3. **Guaranteed Existence**: Both p and q are guaranteed to exist in the tree
4. **Unique Values**: All node values are unique, so we can compare nodes by value

## Approach Ideas

### 1. Recursive Post-Order Traversal (Optimal)
- Use post-order traversal to explore children before processing current node
- Return the node if it's p or q, or if it's the LCA
- If both left and right subtrees return non-null, current node is LCA
- Time: O(n), Space: O(h) where h is height

### 2. Path Storage
- Find path from root to p and path from root to q
- Compare paths to find the last common node
- Time: O(n), Space: O(h)

### 3. Parent Pointers
- Store parent pointers for all nodes
- Traverse from p upwards, marking visited nodes
- Traverse from q upwards until we find a visited node
- Time: O(n), Space: O(n)

## Recursive Logic Explanation

The recursive approach works based on these cases:

```python
def lowestCommonAncestor(root, p, q):
    # Base case: if root is None, p, or q
    if not root or root == p or root == q:
        return root
    
    # Search in left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    # If both subtrees return non-null, root is LCA
    if left and right:
        return root
    
    # Otherwise, return the non-null result
    return left if left else right
```

**Cases:**
1. **Base Case**: If current node is null, p, or q → return current node
2. **Both Found**: If left subtree returns p/q and right subtree returns q/p → current node is LCA
3. **One Side**: If only one subtree returns non-null → that result contains the LCA

## Step-by-Step Example

For tree with nodes 3,5,1,6,2,0,8,null,null,7,4 and p=5, q=1:

```
1. Start at root (3)
2. Search left subtree (5) → finds p=5, returns 5
3. Search right subtree (1) → finds q=1, returns 1  
4. Both left and right return non-null → root (3) is LCA
```

For p=5, q=4:
```
1. Start at root (3)
2. Search left subtree (5) → eventually finds both 5 and 4, returns 5
3. Search right subtree (1) → finds nothing, returns null
4. Only left returns non-null → LCA is 5
```

## Edge Cases

1. **One node is ancestor of other**: LCA is the ancestor node
2. **Minimum tree**: Two nodes only → root is LCA
3. **Nodes at same level**: LCA is their common ancestor
4. **Deep tree**: Algorithm handles any depth efficiently

## Time and Space Complexity

### Recursive Solution:
- **Time Complexity**: O(n) - In worst case, visit all nodes
- **Space Complexity**: O(h) - Recursion stack depth equals tree height
  - Best case (balanced): O(log n)
  - Worst case (skewed): O(n)

## Related Problems

- **235. Lowest Common Ancestor of a Binary Search Tree**: Optimized for BST properties
- **1644. Lowest Common Ancestor of a Binary Tree II**: When nodes might not exist
- **1650. Lowest Common Ancestor of a Binary Tree III**: When parent pointers are available

## Tags
- Tree
- Depth-First Search
- Binary Tree