# 42. Trapping Rain Water

**Difficulty**: Hard  
**Acceptance Rate**: 59.0%  
**Problem Link**: [LeetCode #42](https://leetcode.com/problems/trapping-rain-water/)

## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

## Examples

### Example 1:
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

### Example 2:
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Visual Representation

For `height = [0,1,0,2,1,0,1,3,2,1,2,1]`:

```
Height:     [0,1,0,2,1,0,1,3,2,1,2,1]
Elevation:    |       ■         ■       ■   ■
              |   ■   ■       ■ ■ ■     ■   ■
              | ■ ■   ■     ■ ■ ■ ■   ■ ■ ■ ■
              |■■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
Index:        0 1 2 3 4 5 6 7 8 9 10 11

Water trapped (W):
              |       W         W       W   W  
              |   ■   W       W ■ ■     W   ■
              | ■ W   ■     ■ W ■ ■   ■ ■ W ■
              |■■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■

Total water: 6 units
```

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 3 * 10^4`

## Key Insights

1. **Water Level**: Water at position i is determined by `min(left_max, right_max) - height[i]`
2. **Boundary Walls**: Water is trapped between higher walls on left and right
3. **No Water at Boundaries**: Leftmost and rightmost positions cannot trap water
4. **Positive Water Only**: Only count positive water amounts

## Approach Ideas

### 1. Brute Force
- For each position, find max height to left and right
- Water trapped = min(left_max, right_max) - current_height
- Time: O(n²), Space: O(1)

### 2. Dynamic Programming
- Precompute left_max and right_max arrays
- Calculate water for each position in single pass
- Time: O(n), Space: O(n)

### 3. Two Pointers (Optimal)
- Use two pointers from both ends
- Move pointer with smaller max height
- Time: O(n), Space: O(1)

### 4. Stack-Based
- Use stack to store indices of bars
- Process bars when current bar is higher than stack top
- Time: O(n), Space: O(n)

## Two Pointers Algorithm Explanation

The optimal approach uses two pointers and the key insight that we only need to know the minimum of left_max and right_max:

```python
def trap(height):
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water
```

**Logic:**
- Move the pointer with smaller height
- If current height ≥ max on that side → update max
- If current height < max on that side → add trapped water

## Step-by-Step Example

For `height = [4,2,0,3,2,5]`:

```
Initial: left=0, right=5, left_max=0, right_max=0
Step 1: height[0]=4 < height[5]=5
        → left_max=4, left=1
Step 2: height[1]=2 < height[5]=5
        → water += 4-2=2, left=2
Step 3: height[2]=0 < height[5]=5
        → water += 4-0=4, left=3
Step 4: height[3]=3 < height[5]=5
        → water += 4-3=1, left=4
Step 5: height[4]=2 > height[5]=5? No, =5 is false
        height[4]=2 < height[5]=5
        → water += 4-2=2, left=5
Final: water = 2+4+1+2 = 9
```

## Different Solutions Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Brute Force | O(n²) | O(1) | Simple logic | Too slow |
| DP Arrays | O(n) | O(n) | Easy to understand | Extra space |
| Two Pointers | O(n) | O(1) | Optimal | Harder to grasp |
| Stack | O(n) | O(n) | Different perspective | Complex implementation |

## Edge Cases

1. **Empty array**: `[]` → `0`
2. **Single element**: `[5]` → `0`
3. **No water trapped**: `[1,2,3,4,5]` → `0`
4. **All same height**: `[3,3,3,3]` → `0`
5. **Valley pattern**: `[3,0,3]` → `3`
6. **Peak pattern**: `[0,3,0]` → `0`

## Follow-up Questions

1. **What if the width of each bar is different?**
2. **What if we want to find the maximum water that can be trapped?**
3. **Can you solve it using only one pass?** (Yes, two pointers approach)

## Tags
- Array
- Two Pointers
- Dynamic Programming
- Stack
- Monotonic Stack