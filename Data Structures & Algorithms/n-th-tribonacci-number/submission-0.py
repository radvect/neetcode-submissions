class Solution:
    def tribonacci(self, n: int) -> int:
        tn = 0
        tn1 = 1
        tn2 =1 
        if(n == 0):
            return 0
        if(n==1):
            return 1
        if(n==2):
            return 1
        for i in range(n):
            ti = tn+tn1+tn2
            tn = tn1
            tn1 = tn2
            tn2 = ti
        return tn