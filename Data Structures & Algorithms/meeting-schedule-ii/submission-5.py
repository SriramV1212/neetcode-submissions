"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        heap = []
        max_size = 0

        intervals.sort(key=lambda x : x.start)

        for interval in intervals:

            if heap:
                earliest_available_time = heap[0]

            if heap and interval.start >= earliest_available_time:
                heapq.heappop(heap)
                heapq.heappush(heap,interval.end)
            else:
                heapq.heappush(heap,interval.end)

            max_size = max(max_size, len(heap))

        return max_size
        