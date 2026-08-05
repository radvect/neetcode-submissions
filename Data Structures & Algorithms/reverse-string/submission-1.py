class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s)-1

        while(left<right):
            buf = str(s[right])
            s[right] = str(s[left])
            s[left] = buf
            
            left+=1
            right-=1
        