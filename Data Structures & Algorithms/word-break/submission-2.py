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

        # attempt 2. memoized dfs

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

        return attempt2(0)


