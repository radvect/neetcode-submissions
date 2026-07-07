class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())
        p1 = 0
        p2 = len(s)-1
        print(s)
        if(len(s)==0):
            return True
        while(p1<p2):
            print(p1, p2)
            if(not s[p1].isalpha() and not s[p1].isdigit()):
                p1+=1
                continue
            print(p1, p2)
            if(not s[p2].isalpha() and not s[p2].isdigit() ):
                p2-=1
                continue   
            print(p1, p2) 

            if(s[p1].lower()!=s[p2].lower()):
                return False
            
            # if(p1 == len(s)-1 and p2 == 0):
            #     return True
            
            p1+=1
            p2-=1

            
        return True