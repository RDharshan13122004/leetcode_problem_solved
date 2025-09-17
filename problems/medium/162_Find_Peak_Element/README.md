# 162. Find Peak Element

**Difficulty**: Medium  
**Acceptance Rate**: 45.9%  
**Problem Link**: [LeetCode #162](https://leetcode.com/problems/find-peak-element/)

## Problem Description

A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. You may imagine that nums[-1] = nums[n] = -∞.

In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in **O(log n)** time.

## Examples

### Example 1:
```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

### Example 2:
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
```

### Example 3:
```
Input: nums = [1]
Output: 0
Explanation: The single element is always a peak.
```

## Visual Representation

### Example 1: `nums = [1,2,3,1]`
```
Index: 0  1  2  3
Value: 1  2  3  1
       |  |  ^  |
       |  |  |  |
Peak element at index 2 (value 3)
3 > 2 (left neighbor) and 3 > 1 (right neighbor)
```

### Example 2: `nums = [1,2,1,3,5,6,4]`
```
Index: 0  1  2  3  4  5  6
Value: 1  2  1  3  5  6  4
       |  ^  |  |  |  ^  |
       |  |  |  |  |  |  |
Multiple peaks: index 1 (value 2) and index 5 (value 6)
```

## Constraints

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

## Key Insights

1. **Boundary Conditions**: Elements outside the array are considered as -∞
2. **Multiple Solutions**: Any valid peak index is acceptable
3. **O(log n) Requirement**: Must use binary search approach
4. **No Equal Neighbors**: Adjacent elements are always different
5. **Guaranteed Solution**: At least one peak always exists

## Why Binary Search Works

The key insight is that we can always find a peak by moving towards the "uphill" direction:

- If `nums[mid] < nums[mid + 1]`: There must be a peak in the right half
- If `nums[mid] > nums[mid + 1]`: There must be a peak in the left half (including mid)

**Proof**: Since we always move towards increasing elements and the array is finite, we must eventually reach a peak.

## Approach Ideas

### 1. Linear Search (Not Optimal)
- Check each element to see if it's greater than its neighbors
- Time: O(n), Space: O(1)
- Doesn't meet the O(log n) requirement

### 2. Binary Search (Optimal)
- Use binary search to find peak in logarithmic time
- Move towards the "uphill" direction
- Time: O(log n), Space: O(1)

## Binary Search Implementation

```python
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid element is smaller than next element,
        # then peak must be in right half
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            # Peak is in left half (including mid)
            right = mid
    
    return left
```

**Why this works:**
- We're always moving towards increasing values
- When `left == right`, we've found a peak
- The algorithm guarantees convergence to a valid peak

## Step-by-Step Example

For `nums = [1,2,3,1]`:

```
Initial: left=0, right=3
Iteration 1:
  mid = (0+3)//2 = 1
  nums[1]=2 < nums[2]=3 → move right
  left = 2, right = 3

Iteration 2:
  mid = (2+3)//2 = 2  
  nums[2]=3 > nums[3]=1 → move left
  left = 2, right = 2

left == right → return 2
```

For `nums = [1,2,1,3,5,6,4]`:

```
Initial: left=0, right=6
Iteration 1:
  mid = 3, nums[3]=3 < nums[4]=5 → left=4
Iteration 2:  
  mid = 5, nums[5]=6 > nums[6]=4 → right=5
Iteration 3:
  mid = 4, nums[4]=5 < nums[5]=6 → left=5
  
left == right → return 5
```

## Edge Cases

### 1. Single Element
```python
nums = [1] → return 0
# Only element is always a peak
```

### 2. Two Elements
```python
nums = [1, 2] → return 1  # 2 > 1 and 2 > -∞
nums = [2, 1] → return 0  # 2 > -∞ and 2 > 1
```

### 3. Strictly Increasing
```python
nums = [1, 2, 3, 4, 5] → return 4
# Last element is peak (5 > 4 and 5 > -∞)
```

### 4. Strictly Decreasing
```python
nums = [5, 4, 3, 2, 1] → return 0
# First element is peak (-∞ < 5 > 4)
```

### 5. Peak at Beginning/End
```python
nums = [3, 1, 2] → return 0  # 3 is peak
nums = [1, 2, 3] → return 2  # 3 is peak
```

## Alternative Implementation (Recursive)

```python
def findPeakElement(nums):
    def binary_search(left, right):
        if left == right:
            return left
        
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            return binary_search(mid + 1, right)
        else:
            return binary_search(left, mid)
    
    return binary_search(0, len(nums) - 1)
```

## Time and Space Complexity

### Binary Search Solution:
- **Time Complexity**: O(log n) - Required by problem constraints
- **Space Complexity**: O(1) - Iterative approach uses constant space

### Recursive Solution:
- **Time Complexity**: O(log n) 
- **Space Complexity**: O(log n) - Due to recursion call stack

## Common Mistakes

1. **Wrong Mid Calculation**: Using `(left + right) / 2` can cause integer overflow
2. **Incorrect Boundary Updates**: Must ensure convergence to avoid infinite loops
3. **Off-by-one Errors**: Careful with array bounds when checking `nums[mid + 1]`
4. **Not Handling Edge Cases**: Single element, two elements scenarios

## Follow-up Questions

1. **What if we want all peak elements?** Linear scan needed, O(n) time
2. **What about 2D peak finding?** Different algorithm needed (LeetCode 1901)
3. **Can you find minimum element similarly?** Yes, move towards "downhill"
4. **What if duplicates are allowed?** Problem becomes more complex

## Related Problems

- **852. Peak Index in a Mountain Array**: Simplified version with guaranteed mountain shape
- **1901. Find a Peak Element II**: 2D version of the problem
- **153. Find Minimum in Rotated Sorted Array**: Similar binary search pattern
- **33. Search in Rotated Sorted Array**: Another binary search variant

## Tags
- Array
- Binary Search