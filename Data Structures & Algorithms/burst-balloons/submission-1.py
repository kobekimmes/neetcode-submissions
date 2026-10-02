class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # attempt 1. brute force dfs -- super duper brute force -- TLE (22/24)

        def attempt1(arr):
            n = len(arr)

            best = 0
            for i in range(n):
                l = 1 if i == 0 else arr[i-1]
                r = 1 if i == n-1 else arr[i+1]
                
                prod = l * arr[i] * r
                cpy = arr[:]
                del cpy[i]

                best = max(prod + attempt1(cpy), best)

            return best
        
        # return attempt1(nums)

        # attempt 1.5 memoize

        cache = {}

        def attempt1_5(arr):
            n = len(arr)
            t = tuple(arr)

            if t in cache:
                return cache[t]

            best = 0
            for i in range(n):
                l = 1 if i == 0 else arr[i-1]
                r = 1 if i == n-1 else arr[i+1]
                
                prod = l * arr[i] * r
                cpy = arr[:]
                del cpy[i]

                best = max(prod + attempt1_5(cpy), best)
            
            cache[t] = best
            return best

        return attempt1_5(nums)

        # attempt 2. make it better somehow

        # goals: 
        # - not maintain mutated array as state

        

            


        