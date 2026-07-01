class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_ones= 0
        for i in range(len(nums)):
            if(nums[i]==1):
                curr_ones+=1
                if(i==len(nums)-1 and max_ones<curr_ones):
                    max_ones = curr_ones
            else:
                if(max_ones<curr_ones):
                    max_ones=curr_ones
                curr_ones=0
            


        return max_ones