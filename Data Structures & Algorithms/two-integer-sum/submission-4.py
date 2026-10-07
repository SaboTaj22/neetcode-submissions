class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # Map each value we've seen to its index

        for i, j in enumerate(nums): # Iterate through the array, tracking both index and value
            if target - j in hashmap: # If the complement (target - current value) was already seen, we've found our pair
                return [hashmap[target - j], i] # Return the index of the complement and the current index
            hashmap[j] = i # If no pair found yet, store the current value and its index

        # Time Complexity: O(n)
        # Space Complexity: O(n)