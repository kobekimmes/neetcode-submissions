class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # attempt 1. brute force dfs -- TLE (22/24)

        n = len(prices)

        def attempt1(today, purchased_at):
            if today >= n:
                return 0

            buy_today = 0
            sell_today = 0
            hold_today = attempt1(today + 1, purchased_at)

            # we can only buy if we haven't bought already
            # then the question is sell or dont sell today
            # get mo money $$$
            if purchased_at != -1:
                todays_profit = prices[today] - prices[purchased_at]
                sell_today = attempt1(today + 2, -1) + todays_profit
            
            # we can BUY $$$$$ money money money 
            else:
                buy_today = attempt1(today + 1, today)

            return max(buy_today, sell_today, hold_today)

        # return attempt1(0, -1)

        # attempt 2. memoized dfs

        # in our cache, we will maintain the state at some index pair i, j,
        # where i is the current "day" and j points at the day we last purchased
        # stock, it also acts a flag determining if we can buy stock on a certain
        # day. this pair will map to the maximum profit we could attain at i, having
        # purchased last purchase stock on day j

        cache = {}

        def attempt2(i, j):
            if i >= n:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            buy = 0
            sell = 0
            hold = attempt2(i + 1, j)

            if j != -1:
                prof = prices[i] - prices[j]
                sell = attempt2(i + 2, -1) + prof
            
            # we can BUY $$$$$ money money money 
            else:
                buy = attempt2(i + 1, i)

            cache[(i, j)] = max(buy, sell, hold)
            return cache[(i, j)]

        return attempt2(0, -1)

            

            




