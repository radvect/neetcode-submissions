class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hash_table = dict.fromkeys(nums, 1)
        max_length = 0
        curr_length = 0
        next_value = -100000
        for i in nums: 
            curr_length = 0
            if(i-1 in hash_table):
                continue
            else:
                next_value = i
                curr_length+=1
                while next_value+1 in hash_table:
                    curr_length+=1
                    next_value+=1
                if(curr_length>max_length):
                    max_length=curr_length


        return max_length