class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # attempt 1. brute force dfs -- TLE (32/34)

        n = len(nums)

        def attempt1(i):
            if i >= n-1:
                return True

            for dist in range(1, nums[i]+1):
                if attempt1(i + dist):
                    return True
            
            return False

        # return attempt1(0)

        # attempt 2. attempt 1 is exploring too many possibilities (dp)

        def attempt2():

            dp = [False for _ in range(n)]
            target = n-1

            for i in range(n-1, -1, -1):
                dp[i] = (nums[i] + i) >= target
                if dp[i]:
                    target = i

            return dp[0]  

        return attempt2()


