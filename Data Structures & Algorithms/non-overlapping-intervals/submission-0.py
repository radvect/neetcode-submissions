class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort(key=lambda intervals: intervals[0])     
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if(intervals[i][0]<merged[-1][1]):
                prev = merged.pop()
                merged.append([prev[0],min(prev[1],intervals[i][1]) ])
                count+=1
            else:
                merged.append(intervals[i]) 

        return count