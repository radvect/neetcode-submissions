class Solution:

    def backtrack(self,board,word, row, col, letter_ind, visited):
        

        if(row<0 or row>len(board)-1 or col<0 or col>len(board[0])-1):
            return False
        if((row,col) in visited):
            return False
        if(board[row][col]!=word[letter_ind]):
            return False
        
        if(letter_ind==len(word)-1):
            return True

        visited.add((row,col))
        
        found = self.backtrack(board,word,row-1, col, letter_ind+1, visited) or self.backtrack(board,word,row, col-1, letter_ind+1, visited) or self.backtrack(board,word,row+1, col, letter_ind+1, visited) or self.backtrack(board,word,row, col+1, letter_ind+1, visited)
        
        visited.remove((row,col))
        return found



        


    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(self.backtrack(board,word,i,j,0,set())):
                    return True
        return False

        