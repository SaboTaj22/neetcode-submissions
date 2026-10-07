class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # Two pointers: l is the day we buy, r is the day we sell
        maxP = 0 # Track the best profit seen so far, 0 if no profitable trade exists

        while r < len(prices): # Iterate until the sell pointer runs off the end of the array
            if prices[l] < prices[r]: # If the buy price is lower than the sell price, this is a profitable trade
                profit = prices[r] - prices[l] # Calculate the profit for this trade
                maxP = max(maxP, profit) # Update the max profit if this trade beats the best so far
            else:
                l = r # The sell price is the same or lower, so it's a better day to buy. Move the buy pointer to the current day
            r += 1 # Move the sell pointer forward to the next day
        return maxP # Return the best profit found

        # Time Complexity: O(n)
        # Space Complexity: O(1)