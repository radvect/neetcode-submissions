class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        shortest = min([a,b], key=len)
        longest = max([b,a], key=len)
        
        res = ""
        added = 0 
        for i in range(0, len(shortest)):
            if((int(shortest[-1-i])+int(longest[-1-i]) + added) ==0):
                res = "0"+res
            elif((int(shortest[-1-i])+int(longest[-1-i]) + added) ==1):
                res = "1"+res
                added = 0
            elif((int(shortest[-1-i])+int(longest[-1-i]) + added) ==2):
                res = "0"+res
                added = 1
            elif((int(shortest[-1-i])+int(longest[-1-i]) + added) ==3):
                res = "1"+res
                added = 1
        for i in range(len(shortest), len(longest)):
            if((int(longest[-1-i]) + added) ==0):
                res = "0"+res
            elif((int(longest[-1-i]) + added) ==1):
                res = "1"+res
                added = 0
            elif((int(longest[-1-i]) + added) ==2):
                res = "0"+res
                added = 1
        if(added==1):
            res = "1"+res
        return res    