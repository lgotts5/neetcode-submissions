class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dp using matrix + memoization
       
        #make matrix
        memo = [1000000000] * (amount+1)
        
        memo[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if i - c >= 0:
                    memo[i] = min(memo[i], 1 + memo[i-c])

        if memo[amount] == 1000000000:
            return -1
        return memo[amount]