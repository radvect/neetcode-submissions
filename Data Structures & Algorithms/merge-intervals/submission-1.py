class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        i = 1
        res.append([intervals[0][0], intervals[0][1]])
        while(i<=len(intervals)-1):
            print(i)
            if(res[-1][1]>=intervals[i][0]):
                new_segm =([res[-1][0], max(res[-1][1], intervals[i][1])])
                res.pop()
                res.append(new_segm)
            else:
                res.append(intervals[i])
            i+=1
        return res