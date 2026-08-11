class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        
        ans = 0

        left = 0
        right = 0
        dubs = defaultdict(int)
        while(right<len(s)):
            
            dubs[s[right]]+=1

            while(dubs[s[right]] > 1):
                dubs[s[left]]-=1
                left+=1

                
            ans = max(ans,right-left+1)
            right+=1
        return ans


