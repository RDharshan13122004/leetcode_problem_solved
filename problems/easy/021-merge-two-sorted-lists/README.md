# 21. Merge Two Sorted Lists

**Difficulty**: Easy  
**Acceptance Rate**: 67.3%  
**Problem Link**: [LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/)

## Problem Description

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

## Definition for singly-linked list

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Examples

### Example 1:
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Example 2:
```
Input: list1 = [], list2 = []
Output: []
```

### Example 3:
```
Input: list1 = [], list2 = [0]
Output: [0]
```
## Constraints

- [Standard constraint format - please refer to LeetCode for specific constraints]

## Tags
Linked List, Recursion