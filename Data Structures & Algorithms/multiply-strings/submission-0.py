import math 
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = 0
        
        for j in range( len(num2)-1,-1,-1):
            a+=int(num2[j])*int(num1)*pow(10, len(num2)-1-j)

        print(a)
        return str(a)
