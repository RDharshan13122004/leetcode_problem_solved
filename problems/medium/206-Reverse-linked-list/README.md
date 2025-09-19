# 206. Reverse Linked List

**Difficulty**: Easy  
**Acceptance Rate**: 73.4%  
**Problem Link**: [LeetCode #206](https://leetcode.com/problems/reverse-linked-list/)

## Problem Description

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Examples

### Example 1:
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Visual Representation:**
```
Original: 1 -> 2 -> 3 -> 4 -> 5 -> null
Reversed: 5 -> 4 -> 3 -> 2 -> 1 -> null
```

### Example 2:
```
Input: head = [1,2]
Output: [2,1]
```

**Visual Representation:**
```
Original: 1 -> 2 -> null
Reversed: 2 -> 1 -> null
```

### Example 3:
```
Input: head = []
Output: []
```

## Constraints

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

## Definition for singly-linked list

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Key Insights

1. **Pointer Manipulation**: Need to reverse the direction of `next` pointers
2. **Three Pointers**: Track previous, current, and next nodes to avoid losing connections
3. **Iterative vs Recursive**: Can be solved both ways with different trade-offs
4. **Edge Cases**: Empty list and single node scenarios
5. **In-place Reversal**: Can reverse without extra space for nodes

## Approach Ideas

### 1. Iterative Three-Pointer (Recommended)
- Use three pointers: prev, curr, next
- Reverse links one by one while maintaining connections
- Time: O(n), Space: O(1)

### 2. Recursive (Stack-based)
- Recursively reverse from the end
- Clean and elegant solution
- Time: O(n), Space: O(n) due to call stack

### 3. Stack-based Iterative
- Push all nodes onto stack, then pop to reverse order
- Time: O(n), Space: O(n)
- Less efficient due to extra space

## Iterative Implementation (Optimal)

```python
def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        next_temp = curr.next  # Store next node
        curr.next = prev       # Reverse the link
        prev = curr            # Move prev forward
        curr = next_temp       # Move curr forward
    
    return prev  # prev is now the new head
```

**Step-by-step logic:**
1. Initialize `prev = None` (new tail) and `curr = head`
2. For each node:
   - Store `next` node before losing it
   - Reverse current node's link to point to `prev`
   - Move `prev` and `curr` one step forward
3. Return `prev` as the new head

## Recursive Implementation

```python
def reverseList(head):
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverseList(head.next)
    
    # Reverse the current connection
    head.next.next = head
    head.next = None
    
    return new_head
```

**Recursive logic:**
1. Base case: if list is empty or has one node, return as-is
2. Recursively reverse the sublist starting from `head.next`
3. Reverse the link between current node and next node
4. Set current node's next to None (it becomes the tail)
5. Return the new head from recursion

## Step-by-Step Iterative Example

For `head = [1,2,3,4,5]`:

```
Initial: prev=null, curr=1->2->3->4->5->null

Step 1: 
  next_temp = 2->3->4->5->null
  curr.next = prev  →  1->null
  prev = 1->null
  curr = 2->3->4->5->null
  
Step 2:
  next_temp = 3->4->5->null
  curr.next = prev  →  2->1->null
  prev = 2->1->null
  curr = 3->4->5->null

Step 3:
  next_temp = 4->5->null
  curr.next = prev  →  3->2->1->null
  prev = 3->2->1->null
  curr = 4->5->null

Step 4:
  next_temp = 5->null
  curr.next = prev  →  4->3->2->1->null
  prev = 4->3->2->1->null
  curr = 5->null

Step 5:
  next_temp = null
  curr.next = prev  →  5->4->3->2->1->null
  prev = 5->4->3->2->1->null
  curr = null

Final: Return prev = 5->4->3->2->1->null
```

## Visual Pointer Movement

```
Before reversal:
null <- prev    curr -> next -> ...
              (1) -> (2) -> (3) -> null

After one iteration:
null <- (1) <- prev    curr -> next -> ...
              (2) -> (3) -> null

After two iterations:
null <- (1) <- (2) <- prev    curr -> next
                              (3) -> null
```

## Algorithm Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Iterative 3-pointer | O(n) | O(1) | Optimal space, intuitive | Need to track multiple pointers |
| Recursive | O(n) | O(n) | Clean, elegant | Call stack overhead |
| Stack-based | O(n) | O(n) | Easy to understand | Extra space for stack |

## Edge Cases

### 1. Empty List
```python
head = None → return None
```

### 2. Single Node
```python
head = [1] → return [1]
# Single node points to itself when reversed
```

### 3. Two Nodes
```python
head = [1,2] → return [2,1]
# Simple pointer swap
```

## Common Mistakes

1. **Losing Next Pointer**: Must store `next` before modifying `curr.next`
2. **Wrong Return Value**: Return `prev`, not `curr` (curr becomes None)
3. **Not Handling Empty List**: Check for `head == None`
4. **Infinite Loops**: Ensure pointers move forward correctly
5. **Memory Management**: In languages with manual memory management, avoid memory leaks

## Follow-up Questions

1. **Can you reverse in groups of k?** LeetCode 25: Reverse Nodes in k-Group
2. **What about reversing only a portion?** LeetCode 92: Reverse Linked List II
3. **Can you do it without changing node values?** Yes, change pointers only
4. **How to reverse a doubly linked list?** Similar but need to handle prev pointers too

## Alternative Recursive Approach

```python
def reverseList(head):
    def helper(prev, curr):
        if not curr:
            return prev
        next_temp = curr.next
        curr.next = prev
        return helper(curr, next_temp)
    
    return helper(None, head)
```

This tail-recursive version is more similar to the iterative approach.

## Time and Space Complexity

### Iterative Solution:
- **Time Complexity**: O(n) - Visit each node exactly once
- **Space Complexity**: O(1) - Only use constant extra variables

### Recursive Solution:
- **Time Complexity**: O(n) - Visit each node exactly once
- **Space Complexity**: O(n) - Call stack depth equals number of nodes

## Related Problems

- **92. Reverse Linked List II**: Reverse nodes from position m to n
- **25. Reverse Nodes in k-Group**: Reverse every k consecutive nodes
- **24. Swap Nodes in Pairs**: Swap every two adjacent nodes
- **234. Palindrome Linked List**: Check if linked list is palindrome

## Tags
- Linked List
- Recursion