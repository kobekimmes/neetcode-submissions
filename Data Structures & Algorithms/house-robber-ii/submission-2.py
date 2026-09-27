class Solution:
    def rob(self, nums: List[int]) -> int:

        # attempt 1. brute force dfs -- TLE (6/30) -- we have repeated work from just one call, now we are calling it twice

        # strategy: compare the maximums between 
        #   a. choosing to rob a house and skipping the next
        #   b. choose to skip a house
        # then compare the result of doing that for the whole
        # array excluding the first value, and doing it for the
        # whole array excluding the last value. returning the 
        # larger of the 2

        n = len(nums)

        def attempt1(i, limit):
            if i >= limit:
                return 0

            rob = attempt1(i + 2, limit) + nums[i]
            skip = attempt1(i + 1, limit)
            return max(rob, skip)

        # return max(attempt1(0, n-1), attempt1(1, n))

        # attempt 2. memoized dfs -- accepted

        # the state we want to store is the most you can steal at i, but
        # we need to distinguish the two ranges, since the most you can steal
        # at index i for range 1:n is not the same as range 0:n-1

        cache = {}

        if n == 1:
            return nums[0]

        def attempt2(i, limit):
            if (i, limit) in cache:
                return cache[(i, limit)]

            if i >= limit:
                return 0

            rob = attempt2(i + 2, limit) + nums[i]
            skip = attempt2(i + 1, limit)

            cache[(i, limit)] = max(rob, skip)
            return cache[(i, limit)]

        return max(attempt2(1, n), attempt2(0, n-1))

        # attempt 3. dp somehow

        def attempt3():

            dp = [0] * n

            if n == 0:
                return 0
            if n == 1:
                return nums[0]

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

            return dp[n-1]

        # return attempt3()

        def attempt4():

            if n == 0:
                return 0
            if n == 1:
                return nums[0]

            prev2 = nums[0]
            prev1 = max(prev2, nums[1])
            best = prev1

            for i in range(2, n):
                best = max(prev1, prev2 + nums[i])
                prev2 = prev1
                prev1 = best


            return best
        
        return attempt4()
            





        



        