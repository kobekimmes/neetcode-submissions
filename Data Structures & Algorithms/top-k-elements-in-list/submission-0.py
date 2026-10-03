class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # attempt 1. some sort of bucket sort

        def attempt1():

            freq = {}

            for num in nums:
                freq[num] = freq.get(num, 0) + 1

            sorted_freq = sorted(list(freq.keys()), reverse=True, key=lambda x: freq[x])
            return sorted_freq[:k]

        return attempt1()
