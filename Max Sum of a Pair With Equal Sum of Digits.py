from typing import List

# class Solution:
#     def maximumSum(self, nums: List[int]) -> int:
#         # Dictionary to store numbers grouped by their digit sums
#         digit_sum_map = {}
#         max_sum = -1
        
#         for num in nums:
#             # Calculate digit sum for current number
#             curr_digit_sum = sum(int(digit) for digit in str(num))
            
#             # If we've seen this digit sum before
#             if curr_digit_sum in digit_sum_map:
#                 # Update max_sum if this pair gives larger sum
#                 max_sum = max(max_sum, num + digit_sum_map[curr_digit_sum])
#                 # Keep track of largest number with this digit sum
#                 digit_sum_map[curr_digit_sum] = max(num, digit_sum_map[curr_digit_sum])
#             else:
#                 # First time seeing this digit sum
#                 digit_sum_map[curr_digit_sum] = num
        
#         return max_sum

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Create an empty dictionary
        d = {}
        # Initialize result to -1 (for when no pairs found)
        res = -1
        
        # For each number in nums
        for n in nums:
            # Calculate sum of digits
            # Convert number to string, convert each digit back to int, and sum
            digit_sum = sum(int(i) for i in str(n))
            
            # If we find a number with same digit sum
            if digit_sum in d:
                # Update result if current pair sum is larger
                res = max(res, d[digit_sum] + n)
                # Store the larger number
                d[digit_sum] = max(d[digit_sum], n)
            else:
                # First time seeing this digit sum
                d[digit_sum] = n
                
        return res