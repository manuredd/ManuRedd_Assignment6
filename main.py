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
        if row == 8 and col == 9:
            print('Puzzle Solved!')
            return
        
        if self.grid[row][col] != '_':
            
            if col == 8:
                return self.rec_solve(row + 1, 0)
                
            else:
                return self.rec_solve(row, col + 1)
                
        else:
            #1
            if self.is_valid(1, row, col):
                self.grid[row][col] = 1
                if col == 8:
                    return self.rec_solve(row + 1, 0)
                else:
                    return self.rec_solve(row, col + 1)
            #2
            if self.is_valid(2, row, col):
                self.grid[row][col] = 2
                if col == 8:
                    return self.rec_solve(row + 1, 0)
                else:
                    return self.rec_solve(row, col + 1)
            #3
            if self.is_valid(3, row, col):
                self.grid[row][col] = 3
                if col == 8:
                    return self.rec_solve(row + 1, 0)
                else:
                    return self.rec_solve(row, col + 1)
            #4
            if self.is_valid(4, row, col):
                self.grid[row][col] = 4
                if col == 8:
                    return self.rec_solve(row + 1, 0)
                else:
                    return self.rec_solve(row, col + 1)
            #5
            if self.is_valid(5, row, col):
                self.grid[row][col] = 5
                if col == 8:
                    return self.rec_solve(row + 1, 0)
                else:
                    return self.rec_solve(row, col + 1)
            #6
            if self.is_valid(6, row, col):
                self.grid[row][col] = 6
                if col == 8:
                    return self.rec_solve(row + 1, 0)
                else:
                    return self.rec_solve(row, col + 1)
            #7
            if self.is_valid(7, row, col):
                self.grid[row][col] = 7
                if col == 8:
                    return self.rec_solve(row + 1, 0)
                else:
                    return self.rec_solve(row, col + 1)
            #8
            if self.is_valid(8, row, col):
                self.grid[row][col] = 8
                if col == 8:
                    return self.rec_solve(row + 1, 0)
                else:
                    return self.rec_solve(row, col + 1)
            #9
            if self.is_valid(9, row, col):
                self.grid[row][col] = 9
                if col == 8:
                    return self.rec_solve(row + 1, 0)
                else:
                    return self.rec_solve(row, col + 1)
                
        return
             

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
            
        return True
        
if __name__ == '__main__':
    main()
