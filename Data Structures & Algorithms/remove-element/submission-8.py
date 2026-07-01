class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        begin =0 
        
        end = len(nums)-1
        if(len(nums)==0):
            print(nums)
            return 0

        if(len(nums)==1):
            if(nums[0]==val):
                print([])
                return 0
            else:
                print(nums)
                return 1









        while(begin<=end):
            if(nums[begin]!=val):
                begin+=1
            else:
                if(nums[end]==val):
                    end-=1
                else:
                    nums[begin]=nums[end]
                    nums[end] = val
        



        return begin #+ int(begin==len(nums)-1)