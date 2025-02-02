class Solution:
    def mergeAlternatively(self, word1: str, word2: str)->str:
        merged=[]
        i,j=0,0
        while i<len(word1) or j<len(word2):
            if i<len(word1):
                merged.append(word1[i])
                i+=1
            if j<len(word2):
                merged.append(word2[j])
                j+=1
        return ''.join(merged)
    
# Test Cases
solution = Solution()

# Test case 1: Strings of equal length
print(solution.mergeAlternatively("abc", "xyz"))  # Output: "axbycz"

# Test case 2: word1 longer than word2
print(solution.mergeAlternatively("abcd", "xy"))  # Output: "axbycd"

# Test case 3: word2 longer than word1
print(solution.mergeAlternatively("ab", "wxyz"))  # Output: "awbxyz"

# Test case 4: One empty string
print(solution.mergeAlternatively("abc", ""))     # Output: "abc"
print(solution.mergeAlternatively("", "xyz"))     # Output: "xyz"

# Test case 5: Both empty strings
print(solution.mergeAlternatively("", ""))        # Output: ""

# Test case 6: Special characters in strings
print(solution.mergeAlternatively("123", "@#$"))  # Output: "1@2#3$"
    
