class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}

        if(len(s)!=len(t)):
            return False
        else:
            for i in range(len(s)):
                if not s[i] in freq1:
                    freq1[s[i]]=0
                else:freq1[s[i]]+=1
                if not t[i] in freq2:
                    freq2[t[i]]=0
                else: freq2[t[i]]+=1
            return freq1==freq2