'''
Manu Redd
3105946
EECS 210 
Assignment 6
Nov 9 2023
'''

def main():
    pass

class SudokuBoard:
    def __init__(self, grid):
        self.grid = grid
        
    def rec_solve(self, row, col):
        if self.grid[row][col] != '_':
            
            if col == 8:
                self.rec_solve(row + 1, 0)
                
            else:
                self.rec_solve(row, col + 1)
    
        else:
            pass
            #main rec ifs
            

    def is_valid(self, num, row, col):
        # check box
        if 0 <= row >= 2:
            
            if 0 <= col >= 2:
                for i in self.grid[0:3]:
                    for element in i[0:3]:
                        if element == num:
                            return False
            elif 3 <= col >= 5:
                for i in self.grid[0:3]:
                    for element in i[3:6]:
                        if element == num:
                            return False
                
            elif 6 <= col >= 8:
                for i in self.grid[0:3]:
                    for element in i[6:]:
                        if element == num:
                            return False
                
        elif 3 <= row >= 5:
            
            if 0 <= col >= 2:
                for i in self.grid[3:6]:
                    for element in i[0:3]:
                        if element == num:
                            return False
                
            elif 3 <= col >= 5:
                for i in self.grid[3:6]:
                    for element in i[3:6]:
                        if element == num:
                            return False
                
            elif 6 <= col >= 8:
                for i in self.grid[3:6]:
                    for element in i[6:]:
                        if element == num:
                            return False
            
        elif 6 <= row >= 8:
            
            if 0 <= col >= 2:
                for i in self.grid[6:]:
                    for element in i[0:3]:
                        if element == num:
                            return False
                
            elif 3 <= col >= 5:
                for i in self.grid[6:]:
                    for element in i[3:6]:
                        if element == num:
                            return False
                
            elif 6 <= col >= 8:
                for i in self.grid[6:]:
                    for element in i[6:]:
                        if element == num:
                            return False
                
        
        # check row
        if num in self.grid[row]:
            return False
             
        # check col
        for i in self.grid:
            if i[col] == num:
                return False
        
if __name__ == '__main__':
    main()
