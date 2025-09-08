# 2418. Sort the People

**Difficulty**: Easy 
**Acceptance Rate**: N/A  
**Problem Link**: [LeetCode #2418](https://leetcode.com/problems/sort-the-people/)

## Problem Description

You are given an array of strings `names`, and an array `heights` that consists of distinct positive integers. Both arrays are of length `n`.

For each index `i`, `names[i]` and `heights[i]` denote the name and height of the `i-th` person.

Return `names` sorted in descending order by the people's heights.

## Examples

### Example 1:
```
Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
```

### Example 2:
```
Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
```

## Constraints

- `n == names.length == heights.length`
- `1 <= n <= 10^3`
- `1 <= names[i].length <= 20`
- `1 <= heights[i] <= 10^5`
- `names[i]` consists of lower and upper case English letters.
- All the values of `heights` are distinct.

## Approach Ideas

There are several approaches to solve this problem:

1. **Pair and Sort**: Create pairs of (height, name) and sort by height in descending order
2. **Index Sorting**: Create an array of indices and sort them based on heights
3. **HashMap/Dictionary**: Use a map to associate heights with names, then sort heights

## Key Insights

- Since all heights are distinct, there are no tie-breaking concerns
- We need to maintain the association between names and heights while sorting
- The problem requires descending order (tallest to shortest)

## Tags
- Array
- Hash Table
- String
- Sorting