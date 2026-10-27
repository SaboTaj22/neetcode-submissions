class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # Keep track of the values we've encountered
        
        for i in nums: # Iterate through the array
            if i in hashset: # If the current value is already in the array return True, that means there's a duplicate
                return True 
            hashset.add(i) # If no duplicate found, add to the set
        return False # No duplicates found

        # Time Complexity: O(n)
        # Space Complexity: O(n)