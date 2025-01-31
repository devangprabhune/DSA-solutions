from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # return sorted_s==sorted_t
        count = defaultdict(int)
        #counting the freq of characters in s
        for x in s:
            count[x]+=1
        
        #decrementing the same count freq for each letter in t
        for x in t:
            count[x]-=1
        
        for val in count.values():
            if val!=0:
                return False
        return True
