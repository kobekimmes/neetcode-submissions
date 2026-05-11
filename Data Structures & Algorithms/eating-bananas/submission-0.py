class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        cur_min = r

        while l <= r:

            mid = (l + r) // 2

            n = h
            for p in piles:
                n -= -(-p // mid)
            

            if n >= 0:
                cur_min = mid
                r = mid-1
            else:
                l = mid+1
        
        return cur_min
        



                



