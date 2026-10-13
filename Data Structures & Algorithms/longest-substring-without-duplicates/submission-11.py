class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        right = 0

        s_hash = {}
        max_length = 0
        
        while(right<len(s)):
            
            while(s[right] in s_hash):
                char = s[left]
                s_hash.pop(char, None)
                left+=1
            #print(left, right)
            s_hash[s[right]] = True
            max_length = max(max_length, right-left+1)
            right+=1
        return max_length


                    