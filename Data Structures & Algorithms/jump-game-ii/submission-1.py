class Solution:
    def jump(self, nums: List[int]) -> int:
        

        # attempt 1. brute force dfs -- TLE (24/25)

        n = len(nums)

        def attempt1(i):
            if i >= n-1:
                return 0

            least = float('inf')
            for j in range(1, nums[i]+1):
                least = min(least, attempt1(i+j)+1)

            return least

        # return attempt1(0)

        # attempt 2. dp it 

        def attempt2():

            dp = [float('inf') for _ in range(n)]
            dp[-1] = 0

            for i in range(n-1, -1, -1):
                for j in range(1, nums[i]+1):
                    if i + j < n:
                        dp[i] = min(dp[i], dp[i+j]+1)

            return dp[0]
        return attempt2()


            

            

            