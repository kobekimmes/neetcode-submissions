class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # attempt 1. dfs bruteforce -- TLE (11/30)

        # strategy: maintain 2 pointers, p1 and p2, each
        # pointing to a character in s1 or s2, making 
        # the decision to either take from s1 (inc p1)
        # or take from s2 (inc p2), WHEN WE CAN, and
        # if we reach a state that we cannot take either
        # character, just return false, if the sum of p1
        # and p2 equals the length of p3, we return true

        l1, l2, n = len(s1), len(s2), len(s3)

        if l1 + l2 != n:
            return False

        def attempt1(p1, p2):
            if p1 + p2 == n:
                return True

            int1 = False
            int2 = False
            if p1 < l1 and s1[p1] == s3[p1 + p2]:
                int1 = attempt1(p1 + 1, p2)

            if p2 < l2 and s2[p2] == s3[p1 + p2]:
                int2 = attempt1(p1, p2 + 1) 

            return int1 or int2

        # return attempt1(0, 0)

        # attempt 2. dfs memoized -- accepted, but slow

        # strategy: we can cache the pointers, which will
        # map to the interleaveability at that point, so
        # for 2 pointers i, j of s1 and s2, cache[i, j] 
        # will map to whether s1 and s2 can successfully
        # interleave to form s3 for the string s3[:i+j]

        cache = {}

        def attempt2(p1, p2):
            if p1 + p2 == n:
                return True

            if (p1, p2) in cache:
                return cache[(p1, p2)]

            int1 = False
            int2 = False
            if p1 < l1 and s1[p1] == s3[p1 + p2]:
                int1 = attempt2(p1 + 1, p2)

            if p2 < l2 and s2[p2] == s3[p1 + p2]:
                int2 = attempt2(p1, p2 + 1) 

            cache[(p1, p2)] = int1 or int2
            return cache[(p1, p2)]

        # return attempt2(0, 0)

        # attempt 3. dp somehow

        # strategy: we can use a similar idea for storing
        # if s3 can be represented by making choices for
        # including substrings of s1 and s2

        def attempt3():

            dp = [[False for _ in range(l2+1)] for _ in range(l1+1)]
            dp[l1][l2] = True

            for i in range(l1, -1, -1):
                for j in range(l2, -1, -1):
                    if i < l1 and s3[i + j] == s1[i] and dp[i+1][j]:
                        dp[i][j] = True
                    if j < l2 and s3[i + j] == s2[j] and dp[i][j+1]:
                        dp[i][j] = True

            return dp[0][0]

        return attempt3()




            
            
                


