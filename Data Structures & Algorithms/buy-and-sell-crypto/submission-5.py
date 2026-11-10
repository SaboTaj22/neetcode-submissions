class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day_buy, day_sell = 0, 1 # Two pointers: day_buy is the day we buy, day_sell is the day we sell
        max_price = 0 # Track the best profit seen so far, 0 if no profitable trade exists

        while day_sell < len(prices): # Iterate until the sell pointer runs off the end of the array
            if prices[day_buy] < prices[day_sell]: # If the buy price is lower than the sell price, this is a profitable trade
                profit = prices[day_sell] - prices[day_buy] # Calculate the profit for this trade
                max_price = max(max_price, profit) # Update the max profit if this trade beats the best so far
            else:
                day_buy = day_sell # The sell price is the same or lower, so it's a better day to buy. Move the buy pointer to the current day
            day_sell +=1 # Move the sell pointer forward to the next day
        return max_price # Return the best profit found

        # Time Complexity: O(n)
        # Space Complexity: O(1)