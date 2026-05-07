class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest_price = float('inf')

        for i,todays_price in enumerate(prices):
            current_profit = todays_price - lowest_price

            if lowest_price > todays_price:
                lowest_price = todays_price

            if current_profit > profit:
                profit = current_profit
        
        return profit

        