class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums)-1
        split = 0
        if(len(nums)==1):
            return 0 if nums[0]==target else -1
        if(nums[begin]<nums[end]):
            split = begin
            if(nums[split]==target):
                return 0
        if(nums[begin]>nums[end]):
            while(begin<end-1):
                
                mid = int((end+begin)/2)
                if(nums[begin]>nums[mid]):
                    end = mid
                elif(nums[begin]<nums[mid]):
                    begin = mid
            split = begin+1
        begin =0
        end = len(nums)-1
        if(target == nums[split]):  
            return split
        elif(nums[split]<target and target<=nums[end]):
            begin = split
            end = end
        elif(nums[split]>target):
            return -1
        elif(nums[split]<target and target>nums[end]):
            begin = 0
            end = split-1
        else:
            return -1
        
        while(begin<end-1):
            
            mid = int((end+begin)/2)
            if(target>nums[mid]):
                begin = mid
            elif(target<nums[mid]):
                end = mid
            else:
                return mid
            if(nums[begin]==target):
                return begin
        if(nums[begin]==target):
                return begin
        if(nums[end]==target):
            return end
        return -1
        

            