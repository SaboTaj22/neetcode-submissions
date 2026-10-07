class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 #left pointer at 0, right pointer at the end

        while left <= right: # Iterate until there are no more possibilities left, <= because we check last number when l = r which = midpoint
            middle = left + ((right - left) // 2) # midway point

            if nums[middle] > target: # The middle value is too big, so the target must be in the left half (the array is sorted)
                right = middle - 1 # move pointer to look at all values to the left of the midway point
            elif nums[middle] < target: # The middle value is too small, so the target must be in the right half
                left = middle + 1 # move pointer to look at all values to the right of the midway point
            else:
                return middle # If neither of the above conditions are true, we found the target, return it
        return -1 # Return -1 if there wasn't a result

        # Time Complexity: O(log n)
        # Space Complexity: O(1)