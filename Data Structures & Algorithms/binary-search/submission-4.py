class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        finish = len(nums)-1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
            
        while(finish-start!=1):
            new_middle = (finish+start)//2
            if(target<nums[new_middle]):
                finish = new_middle
            elif(target>nums[new_middle]):
                start = new_middle
            else: 
                return new_middle
        if(nums[finish]==target):
            return finish
        elif(nums[start]==target):
            return start

        return -1