# 240. Search a 2D Matrix II

**Difficulty**: Medium  
**Acceptance Rate**: 51.0%  
**Problem Link**: [LeetCode #240](https://leetcode.com/problems/search-a-2d-matrix-ii/)

## Problem Description

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

## Examples

### Example 1:
```
Input: matrix = [[1,4,7,11,15],
                 [2,5,8,12,19],
                 [3,6,9,16,22],
                 [10,13,14,17,24],
                 [18,21,23,26,30]], target = 5
Output: true
```

### Example 2:
```
Input: matrix = [[1,4,7,11,15],
                 [2,5,8,12,19],
                 [3,6,9,16,22],
                 [10,13,14,17,24],
                 [18,21,23,26,30]], target = 14
Output: true
```

### Example 3:
```
Input: matrix = [[1,4,7,11,15],
                 [2,5,8,12,19],
                 [3,6,9,16,22],
                 [10,13,14,17,24],
                 [18,21,23,26,30]], target = 20
Output: false
```

## Visual Representation

Matrix structure:
```
 1   4   7  11  15
 2   5   8  12  19
 3   6   9  16  22
10  13  14  17  24
18  21  23  26  30
```

Key observation: Starting from top-right corner (15):
- If target < current: move left (smaller values)
- If target > current: move down (larger values)

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n, m <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All the integers in each row are sorted in ascending order.
- All the integers in each column are sorted in ascending order.
- `-10^9 <= target <= 10^9`

## Key Insights

1. **Sorted Properties**: Integers in each row are sorted in ascending from left to right, and integers in each column are sorted in ascending from top to bottom
2. **Strategic Starting Position**: Top-right or bottom-left corners provide optimal elimination
3. **Binary Elimination**: Each comparison eliminates either a row or column
4. **Linear Time Complexity**: Can achieve O(m + n) time complexity

## Approach Ideas

### 1. Brute Force Linear Search
- Check every element in the matrix
- Time: O(m × n), Space: O(1)
- Doesn't utilize sorted properties

### 2. Binary Search on Each Row
- Apply binary search on each row
- Time: O(m × log n), Space: O(1)
- Better but not optimal

### 3. Staircase Search (Optimal)
- Start from top-right or bottom-left corner
- Use sorted properties to eliminate row/column at each step
- Time: O(m + n), Space: O(1)

### 4. Divide and Conquer
- Recursively divide the matrix into quadrants
- Time: O(n^1.58) approximately, Space: O(log n)
- More complex with marginal benefits

## Staircase Search Algorithm (Recommended)

### Starting from Top-Right Corner:
```python
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    row, col = 0, n - 1  # Start from top-right
    
    while row < m and col >= 0:
        current = matrix[row][col]
        
        if current == target:
            return True
        elif current > target:
            col -= 1  # Move left (smaller values)
        else:
            row += 1  # Move down (larger values)
    
    return False
```

### Starting from Bottom-Left Corner:
```python
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    row, col = m - 1, 0  # Start from bottom-left
    
    while row >= 0 and col < n:
        current = matrix[row][col]
        
        if current == target:
            return True
        elif current > target:
            row -= 1  # Move up (smaller values)
        else:
            col += 1  # Move right (larger values)
    
    return False
```

## Why Staircase Search Works

**From Top-Right Corner:**
- Current element is the **largest in its row** and **smallest in its column**
- If `target < current`: target cannot be in current column (all elements below are larger)
- If `target > current`: target cannot be in current row (all elements left are smaller)

**From Bottom-Left Corner:**
- Current element is the **smallest in its row** and **largest in its column**
- Similar elimination logic applies

## Step-by-Step Example

For matrix with target = 14, starting from top-right (15):

```
Step 1: current = 15, target = 14
        15 > 14 → move left, col = 3

Step 2: current = 11, target = 14
        11 < 14 → move down, row = 1

Step 3: current = 12, target = 14
        12 < 14 → move down, row = 2

Step 4: current = 16, target = 14
        16 > 14 → move left, col = 2

Step 5: current = 9, target = 14
        9 < 14 → move down, row = 3

Step 6: current = 14, target = 14
        Found! Return true
```

## Binary Search on Rows Approach

```python
def searchMatrix(matrix, target):
    def binarySearch(row):
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    for row in matrix:
        if row[0] <= target <= row[-1]:  # Optimization
            if binarySearch(row):
                return True
    return False
```

## Algorithm Comparison

| Approach | Time Complexity | Space Complexity | Pros | Cons |
|----------|----------------|------------------|------|------|
| Brute Force | O(m × n) | O(1) | Simple | Doesn't use sorted properties |
| Binary Search/Row | O(m × log n) | O(1) | Better than brute force | Still not optimal |
| Staircase Search | O(m + n) | O(1) | Optimal time, simple | Requires understanding insight |
| Divide & Conquer | O(n^1.58) | O(log n) | Theoretical interest | Complex, no practical benefit |

## Edge Cases

1. **Empty matrix**: `matrix = []` or `matrix = [[]]` → return `false`
2. **Single element**: `matrix = [[1]]`
   - `target = 1` → return `true`
   - `target = 2` → return `false`
3. **Single row**: `matrix = [[1,3,5]]` → binary search
4. **Single column**: `matrix = [[1],[3],[5]]` → linear search
5. **Target smaller than all elements**: Start from top-right, will exit top boundary
6. **Target larger than all elements**: Start from top-right, will exit right boundary

## Time and Space Complexity

### Staircase Search:
- **Time Complexity**: O(m + n) - In worst case, we traverse one full row and one full column
- **Space Complexity**: O(1) - Only using constant extra variables

### Analysis:
- **Best Case**: O(1) - Target found at starting position
- **Average Case**: O(m + n) - Expected to eliminate roughly half the search space
- **Worst Case**: O(m + n) - Traverse from corner to opposite corner

## Follow-up Questions

1. **What if matrix is not sorted by columns?** Use binary search on each row
2. **What if we want to find all occurrences?** Modify to continue search after finding target
3. **Can you do better than O(m + n)?** No, this is optimal for the general case
4. **What about 3D matrices?** Similar principles apply with more dimensions

## Related Problems

- **74. Search a 2D Matrix**: Matrix rows are also globally sorted
- **378. Kth Smallest Element in a Sorted Matrix**: Different search pattern needed
- **1901. Find a Peak Element II**: 2D peak finding problem

## Common Mistakes

1. **Wrong starting corner**: Top-left and bottom-right don't provide elimination benefits
2. **Boundary checks**: Ensure row/col indices stay within bounds
3. **Empty matrix handling**: Check for null/empty matrices before processing
4. **Off-by-one errors**: Be careful with matrix dimensions and indexing

## Tags
- Array
- Binary Search  
- Divide and Conquer
- Matrix