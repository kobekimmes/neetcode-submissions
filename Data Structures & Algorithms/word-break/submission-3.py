class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # attempt 1. brute force dfs -- TLE (27/31)

        def attempt1(i):
            if i == len(s):
                return True

            for word in wordDict:
                wl = len(word)
                if s[i:i+wl] == word:
                    if attempt1(i + wl):
                        return True
            return False

        # return attempt1(0)

        # attempt 1.5. use hashet for constant time lookup

        wordSet = set(wordDict)

        def attempt1_5(i):
            if i == len(s):
                return True

            for j in range(i, len(s)):
                if s[i:j] in wordSet:
                    if attempt1_5(i + 1):
                        return True
            return False


        # attempt 2. memoized dfs -- passed

        # the state we are attempting to cache is whether or not at 
        # some index i, is the word able to be made with the dictionary,
        # since we can use the words as much as we want, it does not
        # restrict us to maintaining any other information, since its a
        # binary yes-no can it be built or not

        cache = {}

        def attempt2(i):
            if i in cache:
                return cache[i]

            if i == len(s):
                return True

            res = False
            for word in wordDict:
                wl = len(word)
                if s[i:i+wl] == word:
                    if attempt2(i + wl):
                        res = True

            cache[i] = res
            return res

        # return attempt2(0)

        # attempt 3. real dp

        # strategy: look at the solution in the solutions tab

        n = len(s)

        def attempt3():

            # maintain dp cache representing indices where a 
            # wordbreak is possible
            dp = [False] * (n + 1)

            # initialize index n, at the end of word to true,
            # indicating that a break between s and "" is valid
            dp[n] = True

            for i in range(n - 1, -1, -1):
                for word in wordDict:
                    
                    wl = len(word)

                    # if s[i:] is found in the dictionary
                    # this means a break here is possible,
                    # but only if there is a valid break at
                    # prior to this word, meaning break at i
                    # with word w, depends on there being a
                    # break at i + len(w)
                    if i + wl <= n and s[i : i + wl] == word:
                        dp[i] = dp[i + wl]
                    
                    # if the break is valid, end early since
                    # we only need to know if a break is valid
                    # in any case not all cases
                    if dp[i]:
                        break

            # return if there is a proper break combination
            return dp[0]
        
        return attempt3()


