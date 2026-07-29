class Solution:

    def encode(self, strs: List[str]) -> str:
        p = ""
        for string in strs:
            length = len(string)
            p+=str(length)+"#"+string

        return p
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        
        while(i<len(s)):
            length = ""
            while(s[i].isdigit()):
                length+=s[i]
                i+=1

            length = int(length)
            i+=1
            ans.append(s[i:i+length])
            i+=length
            
        return ans 