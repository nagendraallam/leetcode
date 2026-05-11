class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]

            if buying:
                # Option 1: Buy today (move to selling state)
                # Option 2: Skip today (stay in buying state)
                res = max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))
            else:
                # Option 1: Sell today (move to buying state after 1 day cooldown)
                # Option 2: Skip today (stay in selling state)
                # Note: i + 2 handles the "1 day cooldown"
                res = max(dfs(i + 2, True) + prices[i], dfs(i + 1, False))
            
            memo[(i, buying)] = res
            return res

        return dfs(0, True)