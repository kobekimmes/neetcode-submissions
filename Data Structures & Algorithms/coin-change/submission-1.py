class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        # attempt 1. brute force dfs -- TLE (19/39)

        def attempt1(target):
            if target == 0:
                return 0

            if target < 0:
                return amount + 1

            ways = amount + 1
            for coin in coins:
                ways = min(1 + attempt1(target - coin), ways)

            return ways

        # ways = attempt1(amount)
        # return -1 if ways > amount else ways

        # attempt 2. memoized dfs

        # the state we want to capture is, from some amount m, what is the fewest number of coins
        # to produce that amount. maintain a cache of m -> n, where n is the minimum number of coins
        # to sum up to m

        cache = {}

        def attempt2(target):
            if target in cache:
                return cache[target]

            if target == 0:
                return 0

            if target < 0:
                return amount + 1

            ways = amount + 1
            for coin in coins:
                ways = min(1 + attempt2(target - coin), ways)

            cache[target] = ways
            return ways

        ways = attempt2(amount)
        return -1 if ways > amount else ways





