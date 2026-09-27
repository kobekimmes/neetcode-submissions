class Solution:
    def rob(self, nums: List[int]) -> int:

        # attempt 1. brute force dfs -- TLE (30/31)

        # strategy: compare the maximums between 
        #   a. choosing to rob a house and skipping the next
        #   b. choose to skip a house

        def attempt1(i):
            if i >= len(nums):
                return 0

            rob = attempt1(i + 2) + nums[i]
            skip = attempt1(i + 1)
            return max(rob, skip)

        # return attempt1(0)

        # attempt 2. memoized dfs -- accepted

        cache = {}

        def attempt2(i):
            if i in cache:
                return cache[i]

            if i >= len(nums):
                return 0

            rob = attempt2(i + 2) + nums[i]
            skip = attempt2(i + 1)

            cache[i] = max(rob, skip)
            return cache[i]

        # return attempt2(0)

        # attempt 3. dp somehow

        # at any location i, the most you could rob would be
        # either the sum of house i's goodies, plus 2 houses back (i-2)
        # or the amount of goodies in i-1's house

        n = len(nums)

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

        return attempt3()
            





        



        