class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(0, len(nums)):
            xor^=nums[i]^i

        return xor^(len(nums))