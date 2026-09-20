class Solution:
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        path = []
        res = []
        def backtracking(start, remaining):
            nonlocal path
            if(remaining<0):
                return 
            if(remaining == 0):
                res.append(path.copy())
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtracking(i,remaining-nums[i])
                path.pop()

        backtracking(0, target)
        return res