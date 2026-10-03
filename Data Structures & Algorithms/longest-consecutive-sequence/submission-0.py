class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # attempt 1. mapping indices

        def attempt1():

            lut = set(nums)
            starts = set()

            for num in nums:
                if (num - 1) not in lut:
                    starts.add(num)

            best = 0

            for start in starts:
                curr_len = 1
                curr = start + 1
                while curr in lut:
                    curr_len += 1
                    curr += 1
                    
                best = max(best, curr_len)
            return best
        
        return attempt1()
                    


