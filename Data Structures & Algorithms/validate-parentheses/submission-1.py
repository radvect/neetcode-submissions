class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {"{":"}", "[":"]", "(":")", "]":None, ")":None, "}":None,} 

        for i in range(len(s)):
            if(len(stack)!=0):

                if(brackets[stack[-1]] == s[i]):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])



        if(len(stack)==0): return True
        else: return False