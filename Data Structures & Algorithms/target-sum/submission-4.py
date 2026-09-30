class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # attempt 1. dfs brute force -- TLE (27-28/2522)

        # strategy: for each element in nums, 
        # make the choice whether to subtract
        # it from the target or add it. when we
        # reach the end of nums and our target
        # is 0, count a new way, otherwise dont.

        # since we can only make the binary decision
        # of subtract or add for each element of nums
        # we dont need to concern ourselves with dupes
        # since at each new position it will be different
        # than the one before.

        n = len(nums)

        def attempt1(i, t):
            if i == n:
                return t == 0

            sub = attempt1(i+1, t - nums[i])
            add = attempt1(i+1, t + nums[i])
            
            return add + sub

        # return attempt1(0, target)

        # attempt 2. memoized dps

        # we can maintain the state of the number
        # of ways to sum to a given target for a
        # an index of nums. essentially, for each
        # index of nums, i, we will store the number
        # of ways to reach some target t, i.e 
        # (i, t) -> w(i, t), where w is some function
        # which generates the sum of the ways to 
        # reach i, t

        cache = {}

        def attempt2(i, t):
            if (i, t) in cache:
                return cache[(i, t)]

            if i == n:
                return t == 0

            sub = attempt2(i+1, t - nums[i])
            add = attempt2(i+1, t + nums[i])
            
            cache[(i, t)] = add + sub
            return cache[(i, t)]
        
        return attempt2(0, target)

            




            

