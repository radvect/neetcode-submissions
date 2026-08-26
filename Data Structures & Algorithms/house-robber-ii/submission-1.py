class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     length = len(nums)
    #     dp = len(nums)*[-1]
        
    #     def dfs(index):
            
    #         nonlocal dp
    #         if(index>length-1):
    #             return 0

    #         if(dp[index]!=-1):
    #             return dp[index]
    #         else:
    #             rob_curr = nums[index]+dfs(index+2)
    #             skip_curr = dfs(index+1)
    #         res = max(rob_curr, skip_curr)
    #         dp[index] = res
    #         return res
                
    #     return dfs(0)
        
    def rob(self, nums: List[int]) -> int:
        nums1 = nums[1:]
        nums2 = nums[:-1]
        dp1 = [-1]*len(nums1)
        dp2 = [-1]*len(nums2)

        if(len(nums)==1):
            return nums[0]
        def dfs(index, nums, dp):
            length = len(dp)
            if(index>length-1):
                return 0

            if(dp[index]!=-1):
                return dp[index]
            else:
                rob_curr = nums[index]+dfs(index+2,nums, dp)
                skip_curr = dfs(index+1,nums, dp)
            res = max(rob_curr, skip_curr)
            dp[index] = res
            return res
\
        return max(dfs(0, nums1,dp1), dfs(0, nums2,dp2))
        