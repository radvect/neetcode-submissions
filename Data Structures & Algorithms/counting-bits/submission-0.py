class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [i for i in range(n+1)]
        res = []
        for elem in arr:
            res_i = 0
            while(elem>0):
                res_i += elem&1
                elem = elem>>1 
            res.append(res_i)
        return res