class Solution:
    def isSubsequence(self,s: str,t: str) -> bool:
        i,j=0,0
        while i<len(s) and j< len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
    
Sol_obj = Solution()

print(Sol_obj.isSubsequence("abxyij","axj")) # False

print(Sol_obj.isSubsequence("abc", "ahbgdc")) # True