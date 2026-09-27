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

        # attempt 2. memoized dfs  -- still TLE (25/27), maybe i am not recording state correctly

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

        return attempt2(0)

            


            

            
