class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            #print(stack)

            if(i.lstrip('-').isnumeric()):
                stack.append(i)
            else: 
                a = int(stack.pop())
                b = int(stack.pop())
                print(a)
                print(b)
                if(i=="+"):
                    stack.append(a+b)
                elif(i=="-"):
                    stack.append(b-a)
                elif(i=="/"):
                    stack.append(b/a)
                elif(i=="*"):
                    stack.append(a*b)

        return int(stack[-1])