from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = []
        summa = 0

        total_number = 0
        # for i in range(len(nums)):
        #     summa+=nums[i]
        #     prefix_sum.append(summa)
        # print(prefix_sum)
        
        hash_s = defaultdict(int)
        hash_s[0] = 1
        for i in range(len(nums)):
            summa+=nums[i]
            total_number += hash_s[summa-k]

            hash_s[summa]  +=1

#print( hash_s)
            
 
            #print(total_number)
                
        return total_number
                
