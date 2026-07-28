class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in temperatures]
        
        for i,temp in enumerate(temperatures):
            if(len(stack)==0):
                stack.append((i,temp))
            else:
                if(stack[-1][1]>=temp):
                    stack.append((i,temp))
                else: 
                    while(len(stack)!=0 and stack[-1][1]<temp):
                        result[stack[-1][0]] = i - stack[-1][0]
                        stack.pop()
                    stack.append((i,temp))
        return result