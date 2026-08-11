class Solution:
    def findMin(self, nums: List[int]) -> int:
        begin = 0
        end = len(nums)-1
        if(len(nums)==1):
            return nums[0]
        if(nums[begin]<nums[end]):
            return nums[begin]
        while(begin<end-1):
            
            mid = int((end+begin)/2)
            if(nums[begin]>nums[mid]):
                end = mid
            elif(nums[begin]<nums[mid]):
                begin = mid
            
        return nums[begin+1] if begin<len(nums)  else nums[0]
            