class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        score = []
        for i in range(len(operations)):
            if(operations[i]=="+"):
                a = int(score[-1])
                b = int(score[-2])
                score.append(a+b)
            elif(operations[i]=="D"):
                a = int(score[-1])
                score.append(a*2)
            elif(operations[i]=="C"):
                score.pop()
            else:
                score.append(int(operations[i]))
        print(score)
        return sum(score)
            



        