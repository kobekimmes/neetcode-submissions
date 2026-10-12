from collections import deque

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # attempt 1. dsu kinda

        def attempt1():

            def is_overlap(r1, r2):
                return r1[0] <= r2[1] and r2[0] <= r1[1]

            start = {}
            end = {}

            n = len(s)

            for i in range(n):
                if s[i] not in start:
                    start[s[i]] = i

            for j in range(n-1, -1, -1):
                if s[j] not in end:
                    end[s[j]] = j

            range_map = {ch : (start[ch], end[ch]) for ch in start}
            ranges = deque(range_map.values())

            res = []

            while len(ranges) > 1:
                print(ranges, res)
                r1, r2 = ranges.popleft(), ranges.popleft()

                print(r1, r2)

                if is_overlap(r1, r2):
                    ranges.appendleft((min(r1[0], r2[0]), max(r1[1], r2[1])))
                else:
                    res.append(r1[1] - r1[0] + 1)
                    ranges.appendleft(r2)
            
            last_range = ranges.pop()
            substring_size = last_range[1] - last_range[0] + 1
            res.append(substring_size)
            
            return res
        return attempt1()



        






