class Solution:
    def isHappy(self, n: int) -> bool:
        hash = set()
        # hash.add(n)
        while(True):
            if(n == 1):
                return True
            if(n in hash):
                return False
            hash.add(n)
            sum = 0
            while(n>0):
                sum+=(n%10)**2
                n//=10
                print(n, sum)
                

            
            n = sum
            
