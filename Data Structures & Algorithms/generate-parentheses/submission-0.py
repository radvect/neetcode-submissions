class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        path = ""
        
        closing = 0
        opening = 0 

        def backtracking():
            nonlocal path
            nonlocal closing
            nonlocal opening
            if(closing==opening and closing == n):
                res.append(path)
                return
            if(opening<n):
                opening +=1
                path = path + "("
                backtracking()
                opening -=1
                path = path[:-1]
            if(closing<opening):
                closing +=1
                path = path + ")"
                backtracking()
                closing -=1
                path = path[:-1]

        backtracking()
        return res