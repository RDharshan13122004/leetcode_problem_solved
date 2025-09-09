# 82. Remove Duplicates from Sorted List II

**Difficulty**: Medium  
**Acceptance Rate**: N/A  
**Problem Link**: [LeetCode #82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Problem Description

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

**Note**: This problem is different from "Remove Duplicates from Sorted List I" where we keep one copy of each duplicate. Here, we completely remove all nodes that have duplicates.

## Examples

### Example 1:
```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Explanation: 3 and 4 appear more than once, so we remove all occurrences of 3 and 4.
```

### Example 2:
```
Input: head = [1,1,1,2,3]
Output: [2,3]
Explanation: 1 appears more than once, so we remove all occurrences of 1.
```

### Example 3:
```
Input: head = [1,2,2]
Output: [1]
Explanation: 2 appears more than once, so we remove all occurrences of 2.
```

### Example 4:
```
Input: head = [1,1]
Output: []
Explanation: Both nodes have the same value, so we remove all occurrences.
```

## Visual Representation

Example: Given 1->2->3->3->4->4->5, return 1->2->5

```
Original: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
          ^    ^    ^^^^^^^^^^^^ ^^^^    ^
        keep keep   remove all  remove  keep

Result:   1 -> 2 -> 5
```

Example: Given 1->1->1->2->3, return 2->3

```
Original: 1 -> 1 -> 1 -> 2 -> 3
          ^^^^^^^^^      ^    ^
          remove all   keep  keep

Result:   2 -> 3
```

## Constraints

- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`
- The list is guaranteed to be sorted in ascending order.

## Definition for singly-linked list

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Key Insights

1. **Complete Removal**: Unlike the first version of this problem, we need to remove ALL nodes that have duplicates, not just keep one copy.

2. **Dummy Node**: Since the head node itself might be a duplicate that needs to be removed, using a dummy node simplifies the logic.

3. **Two-Pointer Technique**: We need to track both the previous non-duplicate node and the current node being examined.

4. **Sorted Property**: The fact that the list is sorted means all duplicate values will be adjacent to each other.

## Approach Ideas

1. **Dummy Node + Two Pointers**: Use a dummy node to handle edge cases and maintain pointers for the previous safe node and current examination node.

2. **Recursive Approach**: Recursively process the list, skipping all nodes with duplicate values.

3. **Iterative with Flag**: Use a flag to mark when we're in a "duplicate zone" and skip all nodes until we find a different value.

## Time Complexity
- **Time**: O(n) where n is the number of nodes in the linked list
- **Space**: O(1) for iterative approach, O(n) for recursive approach due to call stack

## Edge Cases

- Empty list: `[]` → `[]`
- Single node: `[1]` → `[1]`
- All nodes are duplicates: `[1,1,1,1]` → `[]`
- No duplicates: `[1,2,3,4]` → `[1,2,3,4]`
- Head node is duplicate: `[1,1,2,3]` → `[2,3]`
- Tail nodes are duplicates: `[1,2,3,3]` → `[1,2]`

## Tags
- Linked List
- Two Pointers