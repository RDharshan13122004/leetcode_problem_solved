# 515. Find Largest Value in Each Tree Row

**Difficulty**: Medium  
**Acceptance Rate**: 65.7%  
**Problem Link**: [LeetCode #515](https://leetcode.com/problems/find-largest-value-in-each-tree-row/)

## Problem Description

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

## Examples

### Example 1:
```
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
```

**Visual Representation:**
```
        1
      /   \
     3     2
   /  \     \
  5    3     9

Row 0: [1] → max = 1
Row 1: [3, 2] → max = 3  
Row 2: [5, 3, 9] → max = 9
```

### Example 2:
```
Input: root = [1,2,3]
Output: [1,3]
```

**Visual Representation:**
```
    1
   / \
  2   3

Row 0: [1] → max = 1
Row 1: [2, 3] → max = 3
```

### Example 3:
```
Input: root = [1]
Output: [1]
```

## Constraints

- The number of nodes in the tree will be in the range [0, 10^4]
- -2^31 <= Node.val <= 2^31 - 1

## Definition for a binary tree node

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Key Insights

1. **Level-by-Level Processing**: Need to process tree row by row (level order)
2. **Track Maximum**: For each level, find the maximum value among all nodes
3. **BFS vs DFS**: Can use either breadth-first or depth-first search
4. **Index Mapping**: Row 0 is root, row 1 is children of root, etc.

## Approach Ideas

### 1. Breadth-First Search (BFS) with Queue
- Process nodes level by level using a queue
- For each level, track the maximum value
- Time: O(n), Space: O(w) where w is maximum width

### 2. Depth-First Search (DFS) with Level Tracking  
- Use DFS with level parameter to track current depth
- Maintain result array indexed by level
- Time: O(n), Space: O(h) where h is height

### 3. Level Order Traversal (Classic BFS)
- Use standard level order traversal pattern
- Process all nodes at current level before moving to next
- Time: O(n), Space: O(w)

## BFS Queue Approach (Recommended)

```python
from collections import deque

def largestValues(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        max_val = float('-inf')
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            max_val = max(max_val, node.val)
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(max_val)
    
    return result
```

**Advantages:**
- Natural level-by-level processing using BFS pattern
- Easy to understand and implement
- Handles all edge cases naturally

## DFS Approach with Level Tracking

```python
def largestValues(root):
    if not root:
        return []
    
    result = []
    
    def dfs(node, level):
        if not node:
            return
        
        # Expand result array if this is first node at this level
        if level == len(result):
            result.append(node.val)
        else:
            # Update maximum for this level
            result[level] = max(result[level], node.val)
        
        # Recurse to children at next level
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    
    dfs(root, 0)
    return result
```

**Advantages:**
- More space-efficient for deep trees
- Recursive approach may be more intuitive for some
- No explicit queue management needed

## Step-by-Step BFS Example

For tree `[1,3,2,5,3,null,9]`:

```
Initial: queue = [1], result = []

Level 0:
- Process node 1: max_val = 1
- Add children: queue = [3, 2]
- result = [1]

Level 1:
- Process node 3: max_val = 3
- Process node 2: max_val = max(3, 2) = 3
- Add children: queue = [5, 3, 9]
- result = [1, 3]

Level 2:
- Process node 5: max_val = 5
- Process node 3: max_val = max(5, 3) = 5
- Process node 9: max_val = max(5, 9) = 9
- No children to add
- result = [1, 3, 9]
```

## Algorithm Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| BFS Queue | O(n) | O(w) | Natural level processing | Queue overhead |
| DFS Recursive | O(n) | O(h) | Space efficient for wide trees | Call stack overhead |
| Iterative DFS | O(n) | O(h) | Explicit stack control | More complex implementation |

Where:
- n = number of nodes
- w = maximum width of tree
- h = height of tree

## Edge Cases

1. **Empty tree**: `root = null` → return `[]`
2. **Single node**: `root = [1]` → return `[1]`
3. **Left skewed tree**: All nodes have only left children
4. **Right skewed tree**: All nodes have only right children
5. **Complete binary tree**: All levels filled except possibly last
6. **Negative values**: Handle negative numbers correctly with `float('-inf')`

## Special Considerations

### Handling Negative Numbers:
```python
# Wrong: max_val = 0  # Fails if all nodes are negative
# Correct: 
max_val = float('-inf')  # Works for all cases
```

### Memory Usage:
- **BFS**: Queue size can be O(n) in worst case (complete binary tree last level)
- **DFS**: Call stack depth is O(h), better for wide trees

## Time and Space Complexity

### BFS Solution:
- **Time Complexity**: O(n) - Visit each node exactly once
- **Space Complexity**: O(w) - Queue stores at most one level of nodes

### DFS Solution:
- **Time Complexity**: O(n) - Visit each node exactly once  
- **Space Complexity**: O(h) - Recursion call stack depth

## Follow-up Questions

1. **What if we want smallest value in each row?** Use `float('inf')` and `min()` function
2. **What if we want average value in each row?** Track sum and count for each level
3. **Can you do it without extra space?** No, need to store result array
4. **What about k largest values per row?** Use heap or sorting for each level

## Related Problems

- **102. Binary Tree Level Order Traversal**: Basic level order traversal
- **103. Binary Tree Zigzag Level Order Traversal**: Level order with alternating direction
- **107. Binary Tree Level Order Traversal II**: Bottom-up level order
- **199. Binary Tree Right Side View**: Rightmost value in each row
- **637. Average of Levels in Binary Tree**: Average value in each row

## Tags
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree