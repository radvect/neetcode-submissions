from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        
        for num in nums:
            hash_table[num]+=1
            if(hash_table[num]>len(nums)//2):
                return num


              
                