class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        start_new, end_new = newInterval

        result = []

        i = 0

        while i < len(intervals) and intervals[i][1] < start_new:
            result.append(intervals[i])
            i+=1

        while i < len(intervals) and intervals[i][0] <= end_new:
            start_new = min(start_new, intervals[i][0])
            end_new = max(end_new, intervals[i][1])
            i+=1

        result.append([start_new, end_new])

        while i < len(intervals):
            result.append(intervals[i])
            i+=1

        return result  