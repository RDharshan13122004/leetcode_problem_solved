# 919. Complete Binary Tree Inserter

**Difficulty**: Medium  
**Acceptance Rate**: N/A  
**Problem Link**: [LeetCode #919](https://leetcode.com/problems/complete-binary-tree-inserter/)

## Problem Description

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible. Design an algorithm to insert a new node to a complete binary tree keeping it complete after the insertion.

Implement the CBTInserter class:

- `CBTInserter(TreeNode root)` Initializes the data structure with the root of the complete binary tree.
- `int insert(int val)` Inserts a `TreeNode` into the tree with `Node.val == val` so that the tree remains complete, and returns the value of the parent of the inserted node.
- `TreeNode get_root()` Returns the root node of the tree.

## Examples

### Example 1:
```
Input
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
Output
[null, 1, 2, [1, 2, 3, 4]]

Explanation
CBTInserter cbtInserter = new CBTInserter([1, 2]);
cbtInserter.insert(3);  // return 1
cbtInserter.insert(4);  // return 2
cbtInserter.get_root(); // return [1, 2, 3, 4]
```

### Visual Representation:
```
Initial tree:    After insert(3):    After insert(4):
     1                1                    1
    /                / \                  / \
   2                2   3                2   3
                                        /
                                       4
```

## Constraints

- The number of nodes in the tree will be in the range `[1, 1000]`.
- `0 <= Node.val <= 5000`
- `root` is a complete binary tree.
- At most `10^4` calls will be made to `insert` and `get_root`.

## Definition for a binary tree node

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Key Concepts

### Complete Binary Tree Properties:
1. **Level-by-level filling**: All levels are completely filled except possibly the last level
2. **Left-to-right filling**: Nodes in the last level are filled from left to right
3. **Parent-child relationship**: For a node at index `i` in array representation:
   - Left child is at index `2*i + 1`
   - Right child is at index `2*i + 2`
   - Parent is at index `(i-1)//2`

### Insertion Strategy:
- New nodes must be inserted at the leftmost available position in the last level
- If the last level is full, start a new level from the left
- Use level-order traversal to maintain the complete tree property

## Approach Ideas

1. **Array-based approach**: Store all nodes in an array and use array indices to find parent-child relationships
2. **Queue-based approach**: Use a queue to keep track of nodes that can accept new children
3. **Level-order traversal**: Maintain the complete tree structure using BFS

## Time Complexity
- Initialization: O(n) where n is the number of nodes
- Insert: O(1) for each insertion
- Get root: O(1)

## Space Complexity
- O(n) for storing the tree structure

## Tags
- Tree
- Binary Tree
- Design
- Breadth-First Search
- Queue