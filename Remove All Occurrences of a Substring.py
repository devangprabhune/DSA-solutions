class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Initialize an empty list to use as our stack
        result_stack = []

        # Store the length of the target substring 
        part_len = len(part)

        # Store the last character of our target part to remove
        part_end_char = part[-1]  # Fixed: Now correctly gets the last character

        # Processing each char in input string
        for current in s:
            # Adding current char to our stack
            result_stack.append(current)

            # Check if we have found our target substring 
            if (current == part_end_char) and len(result_stack) >= part_len:
                # Check if the last 'part_len' characters in stack
                # match our target substring
                if "".join(result_stack[-part_len:]) == part:
                    # Removing the target substring from our stack
                    del result_stack[-part_len:]

        return "".join(result_stack)
    
    def remOccurences(self, s:str, part:str)->str:

        while True:
            index = s.find(part)
            if index == -1:
                break
            s = s[:index]+s[index+len(part):]

        return s
    
sol = Solution()

stg = "yuyiortyuoyyu"
p = "yu"
print(sol.removeOccurrences(stg,p))
 
ing = "tyrshuhsuhfhsy"
rem = "uh"
print(sol.remOccurences(ing,rem))