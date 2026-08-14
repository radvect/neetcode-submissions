class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        
        left = 0
        right = 0

        size = right-left
        

        hash_dict = defaultdict(int)
        
        max_length=0
        while(right<len(s)):
            
            # print(s[right])
            hash_dict[s[right]]+=1

            dominant = max(hash_dict.values())
            replaceble = sum(hash_dict.values()) - dominant

            # print(dominant)
            # print(replaceble)

            while(replaceble>k):
                hash_dict[s[left]]-=1
                left+=1
                dominant = max(hash_dict.values())
                replaceble = sum(hash_dict.values()) - dominant
            max_length = max(max_length, right-left+1)
            right+=1
        return max_length