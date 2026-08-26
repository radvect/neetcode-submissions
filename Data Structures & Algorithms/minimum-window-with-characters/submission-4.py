class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        hash_of_t = Counter(t)
        need = len(Counter(t))
        left = 0
        right = -1
        hash_of_s_i = Counter()
        min_size = float("inf")
        proper_str = ""
        have = 0

        while(right<len(s)-1):
            right+=1
            hash_of_s_i[s[right]]+=1
            #print(hash_of_s_i)

            if(s[right] in t and  hash_of_s_i[s[right]]== hash_of_t[s[right]]):
                have+=1

            while((have==(need))):    
                #print(right)
                #print(left)
                if(right-left+1<=min_size):
                    proper_str = s[left:right+1]
                    #print(proper_str)
                    min_size = right-left+1
                if(s[left] in t and  hash_of_s_i[s[left]]== hash_of_t[s[left]]):
                    have-=1
                hash_of_s_i[s[left]]-=1
                left+=1
            
            


        # while((hash_of_t<=(hash_of_s_i))):    

        #     if(right-left+1<=min_size):
        #         proper_str = s[left:right]
        #         print(proper_str)
        #         min_size = right-left+1
        #     hash_of_s_i[s[left]]-=1
        #     left+=1



        return proper_str