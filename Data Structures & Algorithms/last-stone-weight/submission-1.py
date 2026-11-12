class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1: # Keep smashing until there's at most one stone left
            stones.sort() # Sort so the two heaviest stones are at the end of the list
            cur = stones.pop() - stones.pop() # Pop the two heaviest stones and smash them. The first pop is the heaviest, so the difference is never negative
            if cur: # If the stones weren't equal, a stone with the leftover weight remains
                stones.append(cur) # Add the leftover stone back into the list
        return stones[0] if stones else 0 # Return the last stone's weight, or 0 if every stone was destroyed

        # Time Complexity: O(n^2 log n)
        # Space Complexity: O(1)