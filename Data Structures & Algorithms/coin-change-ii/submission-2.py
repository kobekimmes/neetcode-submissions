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

        return attempt2(0, amount)

            


