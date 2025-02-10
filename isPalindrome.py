class Solution:
    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
    
    def isPalindrome1(self, x:int)->bool:
        strx = str(x)
        left, right = 0, len(strx)-1
        while left<right:
            if strx[left] != strx[right]:
                return False
        return True

sol = Solution()
print("Result for 312321:", sol.isPalindrome1(312321))  # Expected: False
print("Result for 2662:", sol.isPalindrome2(2662))  # Expected: True

