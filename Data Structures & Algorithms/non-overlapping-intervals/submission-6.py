class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        removals = 0

        end_time = None

        for i in range(len(intervals)):
            if end_time is None or intervals[i][0] >= end_time:
                end_time = intervals[i][1]
            else:
                end_time = min(end_time, intervals[i][1])
                removals+=1

        return removals
        