class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        print(intervals)

        result = []

        removals = 0

        for i in range(len(intervals)):
            if not result or intervals[i][0] >= result[-1][1]:
                result.append(intervals[i])
            else:
                if intervals[i][1] < result[-1][1]:
                    result[-1] = intervals[i]
                removals+=1

        return removals
        