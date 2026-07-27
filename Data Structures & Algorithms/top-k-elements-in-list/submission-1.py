class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = dict()
        for i in nums:
            if(i in hash_table):
                hash_table[i]+=1
            else:
                hash_table[i] = 1 
        hash_table_sorted = sorted(hash_table, key = lambda x: hash_table[x],reverse=True)
        return [hash_table_sorted[i] for i in range(k)]