# 347. Top K Frequent Elements

**Difficulty**: Medium  
**Acceptance Rate**: 63.7%  
**Problem Link**: [LeetCode #347](https://leetcode.com/problems/top-k-frequent-elements/)

## Problem Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## Examples

### Example 1:
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears 1 time.
The 2 most frequent elements are 1 and 2.
```

### Example 2:
```
Input: nums = [1], k = 1
Output: [1]
```

### Example 3:
```
Input: nums = [1,2], k = 2
Output: [1,2]
Explanation: Both elements have the same frequency, so we return both.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`
- It is guaranteed that the answer is unique.

## Key Insights

1. **Frequency Counting**: First step is to count the frequency of each element
2. **Sorting vs Heap**: Can use sorting or a min-heap to find top k elements
3. **Multiple Valid Answers**: When elements have the same frequency, any order is acceptable
4. **Bucket Sort Optimization**: Can use bucket sort for O(n) time complexity

## Approach Ideas

### 1. Hash Map + Sorting
- Count frequencies using hash map
- Sort by frequency and take top k elements
- Time: O(n log n), Space: O(n)

### 2. Hash Map + Min Heap
- Count frequencies using hash map
- Use a min-heap of size k to track top k frequent elements
- Time: O(n log k), Space: O(n + k)

### 3. Hash Map + Max Heap
- Count frequencies using hash map  
- Use a max-heap to extract top k elements
- Time: O(n + k log n), Space: O(n)

### 4. Bucket Sort (Optimal)
- Count frequencies using hash map
- Create buckets for each possible frequency
- Collect results from highest frequency buckets
- Time: O(n), Space: O(n)

### 5. Quick Select
- Count frequencies using hash map
- Use quickselect algorithm to find kth largest frequency
- Time: O(n) average case, Space: O(n)

## Frequency Analysis Example

For `nums = [1,1,1,2,2,3]`, `k = 2`:

```
Frequency Map: {1: 3, 2: 2, 3: 1}
Sorted by frequency: [(1,3), (2,2), (3,1)]
Top 2 frequent: [1, 2]
```

## Detailed Algorithm Walkthrough

### Min Heap Approach:
```python
import heapq
from collections import Counter

def topKFrequent(nums, k):
    # Count frequencies
    count = Counter(nums)
    
    # Use min heap of size k
    heap = []
    
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for freq, num in heap]
```

### Bucket Sort Approach:
```python
def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    
    # Count frequencies
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    
    # Group numbers by frequency
    for n, c in count.items():
        freq[c].append(n)
    
    # Collect top k elements
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
```

## Time Complexity Analysis

| Approach | Time Complexity | Space Complexity | Notes |
|----------|----------------|------------------|-------|
| Hash Map + Sort | O(n log n) | O(n) | Simple but not optimal |
| Hash Map + Min Heap | O(n log k) | O(n + k) | Good when k << n |
| Hash Map + Max Heap | O(n + k log n) | O(n) | Good when k is large |
| Bucket Sort | O(n) | O(n) | Optimal solution |
| Quick Select | O(n) average | O(n) | Optimal but complex |

## When to Use Each Approach

- **Min Heap**: When k is small compared to number of unique elements
- **Max Heap**: When k is large or when you need all elements sorted by frequency
- **Bucket Sort**: When you want optimal O(n) time and can afford O(n) space
- **Quick Select**: When you want optimal average time but can handle worst-case O(n²)

## Edge Cases

1. **k equals array length**: Return all unique elements
2. **All elements same frequency**: Any k elements are valid
3. **Single element array**: Return that element
4. **k = 1**: Return the most frequent element

## Follow-up

**Q**: Can you solve it in better than O(n log n) time complexity?

**A**: Yes, using bucket sort or quickselect, we can achieve O(n) time complexity.

**Q**: What if the array is very large and doesn't fit in memory?

**A**: Use external sorting or streaming algorithms with approximate counting (like Count-Min Sketch).

## Tags
- Array
- Hash Table
- Divide and Conquer
- Sorting
- Heap (Priority Queue)
- Bucket Sort
- Counting
- Quickselect