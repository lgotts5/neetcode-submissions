class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointer keep track of cur range, want to optimize range
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            # Potential profit if selling today
            max_profit = max(max_profit, price - min_price)
            # Update the cheapest buy price so far
            min_price = min(min_price, price)

        return max_profit
