class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # attempt 1. brute force dfs -- TLE (22/24)

        # strategy: if a number can be included in the subsequence,
        # compare the choices of including it and skipping it, this
        # will restrict which options you can chose in the future,
        # by tracking the last element of the subsequence you chose
        # to include

        n = len(nums)

        def attempt1(i, prev_i):

            if i == n:
                return 0

            # invalid, cannot include since our subsequence
            # must be strictly increase; skip
            if prev_i != -1 and nums[prev_i] >= nums[i]:
                return attempt1(i + 1, prev_i)

            # otherwise, compare the max between including the current
            # val in the subseqence vs. skipping it
            return max(attempt1(i + 1, i) + 1, attempt1(i + 1, prev_i))

        # return attempt1(0, -1)

        # attempt 2. memoized dfs -- accepted but slow

        # the state we need to maintain is what is the maximum current subseqence 
        # at each index of nums, however another thing we need to track is what 
        # the last index (or value) was included, in order to distinguish between
        # being at index i having skipped everything and index i including every
        # element that could be

        cache = {}

        def attempt2(i, prev_i):
            if (i, prev_i) in cache:
                return cache[(i, prev_i)]

            if i == n:
                return 0

            include = 0

            # we can always skip
            skip = attempt2(i + 1, prev_i)

            # we can only include if it remains strictly
            # increasing or if its the first element
            if prev_i == -1 or nums[prev_i] < nums[i]:
                include = attempt2(i + 1, i) + 1

            cache[(i, prev_i)] = max(include, skip)
            return cache[(i, prev_i)]

        return attempt2(0, -1)

        # attempt 3. dp somehow

        # working backwards, maintain the longest subsequence
        # that can be attained at each index, store this in
        # a dp cache, at the end just return the max in dp,
        # which indicates the longest subsequence, which would
        # be starting from index i, but we don't care about that

        def attempt3():

            for i in range(n - 1, -1, -1):
                for j in range(i, n):
                    if nums[i] < nums[j]:
                        dp[i] = max(dp[j] + 1, d[i])
            
            return max(dp)
        
        return attempt3()

            







