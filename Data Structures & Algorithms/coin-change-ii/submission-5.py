class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        # attempt 1. dfs brute force -- TLE (16/25)

        # strategy: make a choice, whether to count its value towards the target
        # and continue making choices until either the target is less that or equal
        # to zero, if its zero, success otherwise, fail. keep track of a pointer 
        # into the coins list to ensure duplicate coin combos are not introduced 

        n = len(coins)

        def attempt1(i, target):
            if i == n:
                return 0

            if target < 0:
                return 0

            if target == 0:
                return 1

            ways = 0
            for j in range(i, n):
                ways += attempt1(j, target - coins[j])

            return ways

        # return attempt1(0, amount)

        # attempt 2. memoized dfs

        # strategy: we can cache the state of making a choice of a certain coin
        # at a certain index, this translates to like making the choice to include
        # that coin at that position

        cache = {}

        def attempt2(i, target):
            if i == n:
                return 0

            if target < 0:
                return 0

            if target == 0:
                return 1

            if (i, target) in cache:
                return cache[(i, target)]

            ways = 0
            for j in range(i, n):
                ways += attempt2(j, target - coins[j])

            cache[(i, target)] = ways
            return ways

        # return attempt2(0, amount)

        # attempt 3. dp somehow

        # strategy: this is very similar to the coin change 1, but instead
        # of tracking the minimum numbers of ways to make a combination, 
        # track the sum of the ways to reach them, which, is the sum of the
        # ways to reach the amount minus the amount of the coin, for all coins 

        # ah we have encountered an issue, this tracks all ways, not distinct
        # ways. i think i see why this is considered a 2D dp problem now...

        # i think we can solve this by keeping track of the amount, and the
        # coins we can choose at that amount, like we did in the memoized 
        # verision. dont know why i thought i could get away without using that
        # extra state

        # dp[j][i] represents the number of ways we 
        # reach the ith amount, with the coins from
        # coins[j:] (or n-j coins) available to us

        # dp[j][i-coin] is the number of ways to reach
        # dp[j][i-coin], in a sense its chosing to add
        # coin[j]

        # dp[j-1][i] is the number of ways to reach
        # dp[j-1][i], in a sense its chosing to ignore
        # adding coin at coins[j]

        def attempt3():

            dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

            for i in range(n+1):
                dp[i][0] = 1

            for j in range(n-1, -1, -1):
                for i in range(1, amount + 1):
                    dp[j][i] = dp[j+1][i]
                    if i - coins[j] >= 0:
                        dp[j][i] += dp[j][i-coins[j]]

            return dp[0][amount]

        return attempt3()
                    



            


