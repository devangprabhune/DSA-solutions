import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left=0 #start at left
        right=len(cleaned_text)-1 # start from right
        while left< right:
            if cleaned_text[left] != cleaned_text[right]:
                return False
            left+=1
            right-=1
        return True