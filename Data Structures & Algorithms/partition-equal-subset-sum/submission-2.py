class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # attempt 1. brute-force dfs -- PASSED?? 

        # strategy: get the entire sum of nums, then 
        # work through the array making the choice to
        # include it in the sum or not

        n = len(nums)
        total = sum(nums)
        half_total = total / 2

        if half_total != int(half_total):
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

        # attempt 2. memoized (do i even need to do it?)

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

        return attempt2(0, half_total)


            

            


