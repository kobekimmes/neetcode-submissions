class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # attempt 1. brute force dfs -- TLE (23/25)

        l1, l2 = len(word1), len(word2)

        def attempt1(p1, p2):
            # additions; p1 reaches the end of word1 before p2 reaches
            # the end of p2, meaning l1 < l2. therefore, we must perform
            # l2 - p2 additions for the string lengths to match
            if p1 == l1:
                return l2 - p2

            # deletions; p2 reaches the end of word2 before p1 reaches
            # the end of p1, meaning l1 > l2. therefore we must perform
            # l1 - p1 deletions for the string lengths to match
            if p2 == l2:
                return l1 - p1
        
            if word1[p1] == word2[p2]:
                return attempt1(p1 + 1, p2 + 1)

            return min(attempt1(p1 + 1, p2), attempt1(p1, p2 + 1), attempt1(p1 + 1, p2 + 1)) + 1

        # return attempt1(0, 0)

        # attempt 2. memoized dfs

        cache = {}

        def attempt2(p1, p2):
            if p1 == l1:
                return l2 - p2

            if p2 == l2:
                return l1 - p1

            if (p1, p2) in cache:
                return cache[(p1, p2)]

            # we can always perform a 'replacement' type step, since its
            # only counted as an edit if the characters are not the same, 
            # so special case it
            replacements = attempt2(p1 + 1, p2 + 1)
        
            if word1[p1] == word2[p2]:
                return replacements

            inserts = attempt2(p1 + 1, p2)
            deletes = attempt2(p1, p2 + 1)

            cache[(p1, p2)] = min(replacements, inserts, deletes) + 1
            return cache[(p1, p2)]

        return attempt2(0, 0)



            



