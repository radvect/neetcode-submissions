class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp = len(nums)*[-1]
        
        def dfs(index):
            
            nonlocal dp
            if(index>length-1):
                return 0

            if(dp[index]!=-1):
                return dp[index]
            else:
                rob_curr = nums[index]+dfs(index+2)
                skip_curr = dfs(index+1)
            res = max(rob_curr, skip_curr)
            dp[index] = res
            return res
                
        return dfs(0)
        


    

