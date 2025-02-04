from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # Keep track of minimum price seen so far
        max_profit = 0  # Keep track of maximum profit possible
        
        for price in prices:
            # Update minimum price seen so far
            min_price = min(min_price, price)
            # Check if selling at current price gives better profit
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
        
        return max_profit