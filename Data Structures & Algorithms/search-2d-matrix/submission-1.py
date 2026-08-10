class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_begin = 0
        row_end = len(matrix)
        col_begin = 0
        col_end = len(matrix[0])
        selected_row = None
        row_middle = None
        col_middle = None


        while(row_end-row_begin!=1):
            row_middle = int((row_end + row_begin)/2)
            if(target>=matrix[row_middle][0]):
                row_begin = row_middle
            else:
                row_end = row_middle
        selected_row = row_begin

        
        while(col_end-col_begin!=1):
            col_middle = int((col_end + col_begin)/2)
            if(target>matrix[selected_row][col_middle]):
                col_begin = col_middle
            elif(target==matrix[selected_row][col_middle]):
                return True
            else:
                col_end = col_middle


        return matrix[selected_row][col_begin] == target