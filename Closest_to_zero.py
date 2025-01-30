from typing import List

class Solution:
    def findClosest(self, nums: List[int])->int:
        if not nums: 
            return None
    
        closest = float('inf')
        for num in nums:
            if abs(num)<abs(closest) or (abs(num)==abs(closest) and num>closest):
                closest = num
        
        return closest
    

"""(abs(num)==abs(closest) and num>closest
this condition give the preference to the positive number between the same absolute values
example: -12020 and +12020 or -1 and +1, the preference will be for +12020, +1"""

"""problem link: https://leetcode.com/problems/find-closest-number-to-zero"""
    
