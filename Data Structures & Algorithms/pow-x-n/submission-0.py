class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n==0):
            return 1
        if(n>0):
            integer = 1 
            for i in range(n):
                integer *=x
            return integer
        if(n<0):
            integer = 1
            for i in range(-n):
                integer /=x
            return integer