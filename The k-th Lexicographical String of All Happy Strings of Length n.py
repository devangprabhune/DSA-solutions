class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_happy_strings = 2 ** (n - 1)  # Number of happy strings for each starting character
        if k > 3 * total_happy_strings:  # If k is out of bounds
            return ""

        chars = ['a', 'b', 'c']
        result = []
        k -= 1  # Convert k to 0-based index

        # Construct the k-th happy string
        prev_char = None
        for i in range(n):
            count_per_char = 2 ** (n - 1 - i)  # Possible strings per character choice
            for ch in chars:
                if ch != prev_char:  # Ensure it's a happy string
                    if k < count_per_char:  # k is within this range
                        result.append(ch)
                        prev_char = ch  # Update previous character
                        break
                    k -= count_per_char  # Skip these many strings

        return "".join(result)
