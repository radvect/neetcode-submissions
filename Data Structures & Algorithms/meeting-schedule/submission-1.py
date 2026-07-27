"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        first= sorted(intervals, key=lambda x: x.start)
        for i in range(len(first)-1):

            if(first[i].end>first[i+1].start):
                return False
        return True
