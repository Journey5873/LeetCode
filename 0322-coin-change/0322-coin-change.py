class Solution(object):
    def coinChange(self, coins, amount):
        dp = [0] + [amount + 1] * amount

        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[amount] if dp[amount] < amount + 1 else -1