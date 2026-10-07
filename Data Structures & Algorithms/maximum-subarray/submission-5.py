class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # attempt 1. brute force dfs -- TLE (21/22)

        n = len(nums)

        def attempt1(i, started):
            if i == n:
                if not started:
                    return -float('inf')
                else:
                    return 0

            start = attempt1(i+1, True) + nums[i] 
            skip = 0 if started else attempt1(i+1, False)
            return max(start, skip)

        # return attempt1(0, False)

        # attempt 2. memoize

        cache = {}

        def attempt2(i, started):
            if i == n:
                if not started:
                    return -float('inf')
                else:
                    return 0
        
            if (i, started) in cache:
                return cache[(i, started)]

            start = attempt2(i+1, True) + nums[i] 
            skip = 0 if started else attempt2(i+1, False)

            cache[(i, started)] = max(start, skip)
            return cache[(i, started)]

        return attempt2(0, False)
