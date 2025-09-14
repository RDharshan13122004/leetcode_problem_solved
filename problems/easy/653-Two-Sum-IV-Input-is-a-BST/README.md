# 653. Two Sum IV - Input is a BST

**Difficulty**: Easy  
**Acceptance Rate**: 61.0%  
**Problem Link**: [LeetCode #653](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

## Problem Description

Given the root of a binary search tree and an integer `k`, return `true` if there exist two elements in the BST such that their sum is equal to `k`, or `false` otherwise.

## Examples

### Example 1:
```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Explanation: There exist two elements 2 and 7 such that 2 + 7 = 9.
```

### Example 2:
```
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
Explanation: There are no two elements that sum to 28.
```

## Visual Representation

Example Tree:
```
        5
      /   \
     3     6
   /  \     \
  2    4     7

For k = 9:  2 + 7 = 9 → true
For k = 28: No such pair → false
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-10^4 <= Node.val <= 10^4`
- `root` is guaranteed to be a valid binary search tree.
- `-10^5 <= k <= 10^5`

## Definition for a binary tree node

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Key Insights

1. **BST Property**: In-order traversal gives sorted sequence
2. **Two Sum Pattern**: Can apply various two sum techniques
3. **Space-Time Trade-offs**: Multiple approaches with different complexities
4. **Early Termination**: Can stop as soon as pair is found

## Approach Ideas

### 1. Hash Set + DFS
- Traverse the tree and use hash set to check for complement
- Time: O(n), Space: O(n)
- Simple and efficient

### 2. In-order Traversal + Two Pointers
- Convert BST to sorted array via in-order traversal
- Apply two pointers technique on sorted array
- Time: O(n), Space: O(n)
- Leverages BST property directly

### 3. BST Iterator (Advanced)
- Use two iterators (forward and backward) to simulate two pointers
- Time: O(n), Space: O(h) where h is height
- Most space-efficient approach

### 4. Brute Force DFS
- For each node, search entire tree for complement
- Time: O(n²), Space: O(h)
- Not recommended but works

## Hash Set Approach (Recommended)

```python
def findTarget(root, k):
    def dfs(node):
        if not node:
            return False
        
        complement = k - node.val
        if complement in seen:
            return True
        
        seen.add(node.val)
        
        return dfs(node.left) or dfs(node.right)
    
    seen = set()
    return dfs(root)
```

**Advantages:**
- Simple and intuitive
- O(n) time complexity
- Easy to implement and understand

## In-order + Two Pointers Approach

```python
def findTarget(root, k):
    def inorder(node):
        if node:
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
    
    values = []
    inorder(root)
    
    left, right = 0, len(values) - 1
    while left < right:
        current_sum = values[left] + values[right]
        if current_sum == k:
            return True
        elif current_sum < k:
            left += 1
        else:
            right -= 1
    
    return False
```

**Advantages:**
- Leverages BST sorted property
- Clear two-phase approach
- Easy to debug and verify

## BST Iterator Approach (Space Optimized)

```python
def findTarget(root, k):
    class BSTIterator:
        def __init__(self, root, reverse=False):
            self.stack = []
            self.reverse = reverse
            self._push_all(root)
        
        def _push_all(self, node):
            while node:
                self.stack.append(node)
                if self.reverse:
                    node = node.right
                else:
                    node = node.left
        
        def next(self):
            node = self.stack.pop()
            if self.reverse:
                self._push_all(node.left)
            else:
                self._push_all(node.right)
            return node.val
        
        def has_next(self):
            return len(self.stack) > 0
    
    if not root:
        return False
    
    forward = BSTIterator(root, False)  # Ascending
    backward = BSTIterator(root, True)  # Descending
    
    left = forward.next()
    right = backward.next()
    
    while left < right:
        current_sum = left + right
        if current_sum == k:
            return True
        elif current_sum < k:
            if forward.has_next():
                left = forward.next()
            else:
                break
        else:
            if backward.has_next():
                right = backward.next()
            else:
                break
    
    return False
```

## Algorithm Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Hash Set + DFS | O(n) | O(n) | Simple, fast | Uses extra space |
| Inorder + 2 Pointers | O(n) | O(n) | Clear logic | Uses extra space |
| BST Iterator | O(n) | O(h) | Space efficient | Complex implementation |
| Brute Force | O(n²) | O(h) | Simple concept | Too slow |

## Step-by-Step Example

For tree `[5,3,6,2,4,null,7]` and `k = 9`:

### Hash Set Approach:
```
1. Visit 5: seen = {5}, check for 4 (9-5) → not found
2. Visit 3: seen = {5,3}, check for 6 (9-3) → not found  
3. Visit 2: seen = {5,3,2}, check for 7 (9-2) → not found
4. Visit 4: seen = {5,3,2,4}, check for 5 (9-4) → found in seen!
   Return True
```

### Inorder + Two Pointers:
```
1. Inorder: [2, 3, 4, 5, 6, 7]
2. Two pointers: left=0, right=5
3. 2 + 7 = 9 = k → Return True
```

## Edge Cases

1. **Single node**: Return false (need two different elements)
2. **Two nodes**: Check if they sum to k
3. **Empty tree**: Return false
4. **All same values**: Only true if 2 * value = k and tree has ≥2 nodes
5. **Large k**: May not exist in small trees
6. **Negative values**: Algorithm handles normally

## Follow-up Questions

1. **Can you solve it in O(h) space?** Yes, using BST iterator approach
2. **What if values can be repeated?** Same algorithm works
3. **What if we need to find all pairs?** Modify to collect instead of return early
4. **What about k-sum in BST?** Extend to recursive approach with k parameters

## Related Problems

- **1. Two Sum**: Original hash map approach
- **167. Two Sum II**: Sorted array with two pointers  
- **15. 3Sum**: Extension to three numbers
- **18. 4Sum**: Extension to four numbers

## Tags
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Search Tree
- Hash Table
- Two Pointers
- Binary Tree