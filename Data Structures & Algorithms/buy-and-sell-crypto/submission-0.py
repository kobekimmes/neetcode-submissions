class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_best = 0
        curr_min = prices[0]
        i = 1

        while i < len(prices):
            curr_min = min(prices[i], curr_min)
            curr_best = max(prices[i] - curr_min, curr_best)

            i+=1

        return curr_best







