class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = nums[0]
        dp_min = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            dp_min_copy = dp_min
            dp_min = min(nums[i]*dp_min, nums[i]*dp_max, nums[i])
            dp_max = max(nums[i]*dp_min_copy, nums[i]*dp_max, nums[i])

            res = max(dp_max, res)


        #print(dp)

        return res
