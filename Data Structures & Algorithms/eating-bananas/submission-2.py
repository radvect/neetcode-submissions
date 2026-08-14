class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil        
        top = max(piles)
        bottom = 1
        res = 0
        while(bottom<top):
            mid = (top+bottom)//2
            res = 0
            for i in range(len(piles)):
                res +=ceil(piles[i]/mid)
            print("mid ", mid)
            print("bottom ", bottom)
            print("top ", top)
            if(res>h):
                bottom = mid+1
            elif(res<=h):
                top = mid
            # elif(res==h):
            #     return mid
        # print(res)
        return bottom