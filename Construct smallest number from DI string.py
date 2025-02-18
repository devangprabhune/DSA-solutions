class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        stack = []
        n = len(pattern)

        for i in range(n + 1):
            stack.append(str(i + 1))
            if i == n or pattern[i] == 'I':
                while stack:
                    result.append(stack.pop())

        return ''.join(result)


# Example usage
solution = Solution()
print(solution.smallestNumber("IIIDIDDD"))  # Output: "123549876"
print(solution.smallestNumber("IDID"))  # Output: "13254"