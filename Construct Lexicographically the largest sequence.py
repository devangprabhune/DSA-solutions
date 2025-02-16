class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def backtrack(index):
            if index == len(result):
                return True
            if result[index] != 0:
                return backtrack(index + 1)

            for num in range(n, 1, -1):
                if not used[num] and index + num < len(result) and result[index + num] == 0:
                    result[index] = result[index + num] = num
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = result[index + num] = 0
                    used[num] = False

            if not used[1]:
                result[index] = 1
                used[1] = True
                if backtrack(index + 1):
                    return True
                result[index] = 0
                used[1] = False

            return False

        backtrack(0)
        return result