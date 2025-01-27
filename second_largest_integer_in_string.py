
    #input consists of alphanumeric string 
    #eg. s = "Ahsh363bbs74bnsj"
    #integers constrained to be 0<=X<10 : 12 is 1 and 2, not tweleve 
class solution:

    def secondHighest(self, s: str) -> int:
        sec_high = float('-inf')
        highest = float('-inf')
        for char in s:
            if char.isdigit():
                num = int(char)

                if num>highest:
                    sec_high = highest
                    highest = num
                elif num>sec_high and num<highest:
                    sec_high = num
                
        return sec_high if sec_high != float('-inf') else -1
        

s = "adh734bs12ja3jn7"
sol = solution()
print(sol.secondHighest(s))