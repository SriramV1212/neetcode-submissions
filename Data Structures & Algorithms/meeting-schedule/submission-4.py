"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda x: x.start)

        print([(interval.start,interval.end) for interval in intervals])

        end_time = None

        for interval in intervals:
            if end_time is None or interval.end >= end_time:
                end_time = interval.end
            else:
                return False

        return True
