# 167. Two Sum II - Input Array Is Sorted

**Difficulty**: Medium  
**Acceptance Rate**: 60.5%  
**Problem Link**: [LeetCode #167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Problem Description

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 < numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

## Examples

### Example 1:
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

### Example 2:
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3. We return [1, 3].
```

### Example 3:
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order.
- `-1000 <= target <= 1000`
- The tests are generated such that there is exactly one solution.

## Key Differences from Two Sum I

1. **Array is sorted**: This enables more efficient algorithms
2. **1-indexed return**: Return indices starting from 1, not 0
3. **Guaranteed solution**: Exactly one solution always exists
4. **Constant space requirement**: Must use O(1) extra space
5. **No hash map allowed**: The constant space constraint eliminates the hash map approach

## Approach Ideas

### 1. Brute Force
- Check all pairs of numbers
- Time: O(n²), Space: O(1)
- Not optimal but meets space constraint

### 2. Binary Search
- For each number, binary search for target - current number
- Time: O(n log n), Space: O(1)
- Better than brute force

### 3. Two Pointers (Optimal)
- Use the sorted property with two pointers from both ends
- Time: O(n), Space: O(1)
- Optimal solution that meets all constraints

## Two Pointers Algorithm Explanation

Since the array is sorted, we can use two pointers approach:

```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # Convert to 1-indexed
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return []  # Should never reach here given constraints
```

**Logic:**
- If sum is too small → move left pointer right to get larger numbers
- If sum is too large → move right pointer left to get smaller numbers
- If sum equals target → found the answer

## Step-by-Step Example

For `numbers = [2,7,11,15]`, `target = 9`:

```
Initial: left=0, right=3
numbers[0] + numbers[3] = 2 + 15 = 17 > 9
→ Move right pointer left: right=2

numbers[0] + numbers[2] = 2 + 11 = 13 > 9  
→ Move right pointer left: right=1

numbers[0] + numbers[1] = 2 + 7 = 9 = target
→ Found answer: [0+1, 1+1] = [1, 2]
```

## Why Two Pointers Works

The sorted property guarantees that:
- Moving left pointer right only increases the sum
- Moving right pointer left only decreases the sum
- We never miss the optimal solution because we systematically explore all possibilities

**Proof of Correctness:**
- If `numbers[i] + numbers[j] < target`, then for all `k < j`, `numbers[i] + numbers[k] < target`
- If `numbers[i] + numbers[j] > target`, then for all `k > i`, `numbers[k] + numbers[j] > target`
- This means we can safely eliminate one side at each step

## Edge Cases

1. **Minimum array**: `[1,2]` with target `3` → `[1,2]`
2. **Negative numbers**: `[-1,0]` with target `-1` → `[1,2]`
3. **Large array**: Algorithm handles efficiently in O(n)
4. **Target at boundaries**: Works for any valid target

## Time and Space Complexity

### Two Pointers Solution:
- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(1) - Only using two pointers

### Comparison with Other Approaches:
| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(n²) | O(1) | Too slow but meets space constraint |
| Binary Search | O(n log n) | O(1) | Better than brute force |
| Two Pointers | O(n) | O(1) | Optimal solution |
| Hash Map | O(n) | O(n) | Violates space constraint |

## Follow-up Questions

1. **What if the array is not sorted?** Use hash map approach from Two Sum I
2. **What if we need all pairs that sum to target?** Modify to continue searching after finding pairs
3. **What if no solution exists?** The problem guarantees a solution, but we could return empty array

## Common Mistakes

1. **Forgetting 1-indexed return**: Must add 1 to both indices
2. **Not handling edge cases**: Consider negative numbers and boundary conditions
3. **Infinite loop**: Ensure pointers move in correct direction
4. **Using extra space**: Hash map violates the constant space requirement

## Related Problems

- **1. Two Sum**: Original version with unsorted array
- **15. 3Sum**: Extension to three numbers
- **16. 3Sum Closest**: Find three numbers closest to target
- **18. 4Sum**: Extension to four numbers

## Tags
- Array
- Two Pointers
- Binary Search