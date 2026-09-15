
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            x, y = -heapq.heappop(stones), -heapq.heappop(stones)

            diff = max(x, y) - min(x, y)

            if diff > 0:
                heapq.heappush(stones, -diff)

        return 0 if not stones else -heapq.heappop(stones)

