class Solution:
    
    
    def backtrack(self, nums, path, remaining, start):
        if(remaining==0):
            self.result.append(path.copy())
            return
        elif(remaining<0):
            return
        elif(remaining>0):
            for i in range(start, len(nums)):
                path.append(nums[i])
                self.backtrack(nums,path, remaining-nums[i], i)
                path.pop()
                


    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        self.result = []
        

        self.backtrack(nums,[],target, 0)

        return self.result