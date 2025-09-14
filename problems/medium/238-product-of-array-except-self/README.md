# 238. Product of Array Except Self

**Difficulty**: Medium  
**Acceptance Rate**: 65.4%  
**Problem Link**: [LeetCode #238](https://leetcode.com/problems/product-of-array-except-self/)

## Problem Description

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

## Examples

### Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: 
- answer[0] = 2*3*4 = 24
- answer[1] = 1*3*4 = 12  
- answer[2] = 1*2*4 = 8
- answer[3] = 1*2*3 = 6
```

### Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
Explanation:
- answer[0] = 1*0*(-3)*3 = 0
- answer[1] = (-1)*0*(-3)*3 = 0
- answer[2] = (-1)*1*(-3)*3 = 9
- answer[3] = (-1)*1*0*3 = 0
- answer[4] = (-1)*1*0*(-3) = 0
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

## Key Insights

1. **No Division Allowed**: Cannot simply calculate total product and divide by each element
2. **Prefix and Suffix Products**: For each position, we need the product of all elements before it and all elements after it
3. **Two-Pass Solution**: First pass calculates prefix products, second pass calculates suffix products
4. **Space Optimization**: Can use the output array to store intermediate results

## Approach Ideas

### 1. Brute Force (Not Allowed)
- For each index, calculate product of all other elements
- Time: O(n²), Space: O(1)
- Violates the O(n) time requirement

### 2. Division Method (Not Allowed)
- Calculate total product, then divide by each element
- Handle zero cases separately
- Not allowed per problem constraints

### 3. Left and Right Arrays
- Create left[] where left[i] = product of all elements to the left of i
- Create right[] where right[i] = product of all elements to the right of i
- result[i] = left[i] * right[i]
- Time: O(n), Space: O(n)

### 4. Optimized Single Array (Optimal)
- Use the result array to first store left products
- Then traverse from right to left, multiplying by running right product
- Time: O(n), Space: O(1) (excluding output array)

## Step-by-Step Walkthrough

For `nums = [1,2,3,4]`:

**Step 1: Calculate Left Products**
```
Index:  0  1  2  3
nums:   1  2  3  4
left:   1  1  2  6
```
- left[0] = 1 (no elements to the left)
- left[1] = 1 (product of elements before index 1)
- left[2] = 1*2 = 2
- left[3] = 1*2*3 = 6

**Step 2: Calculate Right Products and Final Result**
```
Index:     0   1   2  3
left:      1   1   2  6
right:    24  12   4  1
result:   24  12   8  6
```
- Process from right to left with running product
- result[3] = left[3] * 1 = 6
- result[2] = left[2] * 4 = 8
- result[1] = left[1] * 12 = 12
- result[0] = left[0] * 24 = 24

## Edge Cases

1. **Array with zeros**: Handle carefully as they make many products zero
2. **All negative numbers**: Products alternate between positive and negative
3. **Single zero**: Only the position with zero will have non-zero product
4. **Multiple zeros**: All positions will have zero product
5. **Minimum length array**: [a,b] → [b,a]

## Time and Space Complexity

### Optimal Solution:
- **Time Complexity**: O(n) - Two passes through the array
- **Space Complexity**: O(1) - Only using constant extra space (not counting output array)

## Follow-up

Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

**Answer**: Yes, the optimized single array approach achieves this.

## Tags
- Array
- Prefix Sum