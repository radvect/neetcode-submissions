class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff = []

        pref.append(1)
        for i in range(1,len(nums)):
            pref.append(nums[i-1]*pref[-1])
        
        suff.insert(0,1)
        for i in range(len(nums)-2,-1,-1):
            suff.insert(0,suff[0]*nums[i+1])

        return [i*j for i,j in zip(pref,suff)]