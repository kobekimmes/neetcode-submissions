class Solution:
    def numDecodings(self, s: str) -> int:
        

        # attempt 1. brute force dfs -- TLE (25/27)

        # strategy: for each digit character,
        # apply the following rules:
        #   if the single-digit is a 0: invalid, move on
        #   else, include its decoding and move on
        #   if the double digit is outisde the range of 10-26: invalid move on,
        #   else, include its decoding and move on

        n = len(s)

        def attempt1(i):
            if i >= n:
                return 1

            single = 0
            double = 0

            if s[i] != '0':
                single = attempt1(i+1)

                if i + 1 < n:
                    if int(s[i:i+2]) in range(10, 27):
                        double = attempt1(i + 2)

            return single + double

        # return attempt1(0)

        # attempt 2. memoized dfs  -- accepted

        cache = {}

        def attempt2(i):
            if i >= n:
                return 1

            if i in cache:
                return cache[i]

            single = 0
            double = 0

            if s[i] != '0':
                single = attempt2(i+1)

                if i + 1 < n:
                    if int(s[i:i+2]) in range(10, 27):
                        double = attempt2(i + 2)

            cache[i] = single + double
            return cache[i]

        # return attempt2(0)

        # attempt 3. real dp somehow

        # strategy: if we are on a valid character digit, i.e non-zero,
        # carry forward the number of valid ways to decode which precedes
        # it, we can do this by looping backwards from the end, additionally
        # for every pair of characters, if they are valid (within range), 
        # sum the ways to decode as if those valid characters were included
        # in the decoding

        def attempt3():

            dp = [0] * (n+1)
            dp[-1] = 1

            for i in range(n-1, -1, -1):
                if s[i] != '0':
                    dp[i] = dp[i+1]
                    
                    if i + 1 < n:
                        if int(s[i:i+2]) in range(10, 27):
                            dp[i] += dp[i+2] 
            
            return dp[0]
    
        return attempt3()
                



            


            

            
