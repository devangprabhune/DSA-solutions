from collections import defaultdict
import heapq


class NumberContainers:
    def __init__(self):
        # Maps index to number
        self.index_map = {}
        # Maps number to set of indices (using heap for smallest index)
        self.number_map = defaultdict(list)
        
    def change(self, index: int, number: int) -> None:
        # If index already has a number
        if index in self.index_map:
            old_num = self.index_map[index]
            # Remove old index from number's list
            while self.number_map[old_num] and self.number_map[old_num][0] == index:
                heapq.heappop(self.number_map[old_num])
        
        # Update mappings
        self.index_map[index] = number
        heapq.heappush(self.number_map[number], index)
        
    def find(self, number: int) -> int:
        # Remove any invalid indices from heap
        while self.number_map[number] and self.index_map.get(self.number_map[number][0]) != number:
            heapq.heappop(self.number_map[number])
            
        # Return smallest valid index or -1 if none exists
        return self.number_map[number][0] if self.number_map[number] else -1