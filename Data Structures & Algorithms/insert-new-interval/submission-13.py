class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key=lambda intervals: intervals[0])
        merged = []
        merged.append(intervals[0])

        for i in range(1, len(intervals)):
            if(intervals[i][0]<=merged[-1][1]):
                prev = merged.pop()
                merged.append([prev[0],max(prev[1],intervals[i][1]) ])
            else:
                merged.append(intervals[i]) 



        return merged