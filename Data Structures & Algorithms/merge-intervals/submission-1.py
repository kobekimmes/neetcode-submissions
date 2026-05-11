class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def overlap(a, b):
            return a[1] >= b[0]

        def combine(a, b):
            return [a[0], max(a[1], b[1])]
        
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        curr_interval = sorted_intervals[0]

        result = []

        for i in range(1, len(sorted_intervals)):
            next_interval = sorted_intervals[i]

            if overlap(curr_interval, next_interval):
                curr_interval = combine(curr_interval, next_interval)

            else:
                result.append(curr_interval)
                curr_interval = next_interval
        
        result.append(curr_interval)
        return result
