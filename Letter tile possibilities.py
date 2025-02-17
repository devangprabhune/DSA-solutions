from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        unique_sequences = set()

        for i in range(1, len(tiles) + 1):
            for perm in permutations(tiles, i):
                unique_sequences.add(''.join(perm))

        return len(unique_sequences)