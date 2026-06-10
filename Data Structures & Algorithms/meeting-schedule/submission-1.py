"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start_invls = [intervals[i].start for i in range(len(intervals))]
        end_invls = [intervals[i].end for i in range(len(intervals))]
        start_invls.sort()
        end_invls.sort()
        
        for i in range(len(intervals)-1):
            if start_invls[i+1] < end_invls[i]:
                return False
        return True

        

