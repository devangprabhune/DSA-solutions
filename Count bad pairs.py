from collections import Counter
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = Counter()
        total_pairs = 0
        n = len(nums)
        
        for i in range(n):
            # j-nums[j] should equal i-nums[i] for good pairs
            diff = i - nums[i]
            # Add count of previous matching differences (good pairs)
            total_pairs += count[diff]
            # Add this difference to counter
            count[diff] += 1
        
        # Total possible pairs minus good pairs = bad pairs
        return (n * (n-1) // 2) - total_pairs