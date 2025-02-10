class Solution:
    def clearDigits1(self, s: str)-> str:
        l = []
        for i in s:
            if(i.isalpha()):
                l.append(i)
            else:
                l.pop()

        return ''.join(l)
    
    def clearDigits2(self, s:str)-> str:
        if not s or s.isdigit():
            return ''
        
        stack = []

        for char in s:
            if char.isdigit() and stack:
                stack.pop()

            else:
                stack.append(char)
        return ''.join(stack)
    

sol = Solution()

print("Result for 'cb34':", sol.clearDigits1("cb34"))  # Expected: ""
print("Result for 'ab3cd5ef':", sol.clearDigits2("ab3cd5ef"))  # Expected: "abef"
print("Result for '123':", sol.clearDigits2("123"))  # Expected: ""
print("Result for 'a1b2c3':", sol.clearDigits1("a1b2c3"))  #


