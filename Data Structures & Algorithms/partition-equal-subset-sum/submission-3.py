class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # attempt 1. brute-force dfs -- PASSED?? beats 100% too?

        # strategy: get the entire sum of nums, then 
        # work through the array making the choice to
        # include it in the sum or not

        n = len(nums)
        total = sum(nums)
        half_total = total // 2

        if total % 2:
            return False

        def attempt1(i, target):
            if i < n:

                if target == 0:
                    return True

                if target < 0:
                    return False

                # check if adding to sum or skipping is valid
                return attempt1(i + 1, target - nums[i]) or attempt1(i + 1, target)

            return False

        # return attempt1(0, half_total)

        # attempt 2. memoized (do i even need to do it?) -- passed beats 100%, what is the solution other people are doing?

        # we can maintain states in a cache to reduce repeated work, 
        # what we want to maintain is whether at some index with some
        # target is a valid partition, concretely maintain a mapping
        # between indices i, and targets t to a boolean if they are 
        # valid

        cache = {}

        def attempt2(i, target):
            if i < n:
            
                if (i, target) in cache:
                    return cache[(i, target)]

                if target == 0:
                    return True

                if target < 0:
                    return False

                cache[(i, target)] = attempt2(i + 1, target - nums[i]) or attempt2(i + 1, target)
                return cache[(i, target)]

            return False

        # return attempt2(0, half_total)

        # attempt 3. dp somehow

        # strategy: maintain a dp cache which stores at a given index,
        # the total sum we can reach up to at that index in nums, use
        # this to inform if the target is reachable by some combination

        def attempt3(target):

            # intialize dp cache of size target+1 all to false
            dp = [False] * (target+1)

            # intialize index at 0 to true, intuitively 
            # this means 0 is always a reachable sum
            dp[0] = True

            for num in nums:

                # for every value from the target 
                # to the number pointed at by j
                # check if it is either:
                #   a. already reachable
                #   b. able to be reached by using num in sum
                for j in range(target, num-1, -1):
                    dp[j] = dp[j] or dp[j - num]

            # return the reachability of the target
            return dp[target]


        return attempt3(half_total)




            

            


