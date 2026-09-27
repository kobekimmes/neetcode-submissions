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

        # attempt 2. memoized dfs

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

        return attempt2(0)



        



        