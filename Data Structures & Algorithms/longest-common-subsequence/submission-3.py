class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # attempt 1. dfs? i feel like this is greedy -- it is not greedy it is dp -- TLE (17/22)

        n = len(text1)
        m = len(text2)

        # we want text1 to be the shorter of the two
        if n > m:
            return self.longestCommonSubsequence(text2, text1)

        def attempt1(i, j, prev_j):
            if i == n:
                return 0

            # if we reach the end of the larger word, we now have to check for
            # the next character in the smaller word (i+1), having unsuccessfully
            # found the character at i, which means we couldn't increase our 
            # subsequence
            if j == m:
                return attempt1(i + 1, prev_j + 1, prev_j)

            # if we have a match between texts, and it falls
            # after the selection made into the subsequence
            # we can add it
            if text1[i] == text2[j] and j > prev_j:
                return max(1 + attempt1(i+1, j+1, j), attempt1(i, j+1, prev_j))
            else:
                return attempt1(i, j+1, prev_j)

        # return attempt1(0, 0, -1)

        # attempt 2. memoized dfs

        # the state we want to maintain is for some tuple of index pair i, j, and prev_j, 
        # where prev_j is the index of the last element we included in the subsequence from
        # the larger word, map to the longest subsequence at that point

        cache = {}

        def attempt2(i, j, prev_j):
            if i == n:
                return 0

            if (i, j, prev_j) in cache:
                return cache[(i, j, prev_j)]

            if j == m:
                # cache a "failed" addition, this character cannot be added
                # to the subsequence, at least from this "state". record it
                cache[(i, j, prev_j)] = attempt2(i + 1, prev_j + 1, prev_j)
            else:
                # we can always skip
                skip = attempt2(i, j+1, prev_j)
                include = 0
                
                # we can only include if we satisfy this
                if text1[i] == text2[j] and j > prev_j:
                    include = 1 + attempt2(i+1, j+1, j)
                
                cache[(i, j, prev_j)] = max(include, skip)
            
            return cache[(i, j, prev_j)]
        
        # return attempt2(0, 0, -1)

        # attempt 3 & 4. fix the bugs in attempt 1 & 2

        # i was over complicating the state by including the prev_j
        # we just need to maintain the two pointers, i, j since j already
        # represents the location of the last element added to the
        # subsequence from the longer string

        def attempt3_and_4(i, j):
            if i == n or j == m:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            # we can always skip (but its less computation to only 
            # skip when we have no match, since we will greedily 
            # choose a match over a non-match since its always better)
            skip = 0
            include = 0
                
            # we can only include if we satisfy this
            if text1[i] == text2[j]:
                include = 1 + attempt3_and_4(i+1, j+1)
            else:
                skip = max(attempt3_and_4(i + 1, j), attempt3_and_4(i, j + 1))

            cache[(i, j)] = max(include, skip)
            return cache[(i, j)]
        
        return attempt3_and_4(0, 0)










            
            

