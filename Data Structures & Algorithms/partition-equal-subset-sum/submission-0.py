class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # attempt 1. brute-force dfs

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

        return attempt1(0, half_total)
