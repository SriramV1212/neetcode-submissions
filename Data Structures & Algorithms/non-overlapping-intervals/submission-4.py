class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        removals = 0

        end_time = None

        for i in range(len(intervals)):
            if not end_time or intervals[i][0] >= end_time:
                end_time = intervals[i][1]
            else:
                if intervals[i][1] < end_time:
                    end_time = intervals[i][1]
                removals+=1

        return removals
        