'''
Manu Redd
3105946
EECS 210 
Assignment 6
Nov 9 2023
'''

#sources used: StackOverflow, ChatGPT

def main():
    # Prompt the user for the input file name
    file_name = input("Enter the name of the input file: ")

    # Call the function to parse the Sudoku board from the file and print the input board
    sudoku_board = parse_sudoku_from_file(file_name)

    # Print the input Sudoku board (underscore '_' replaced with 0 for display)
    print(f"\nSudoku board from {file_name} ('_' replaced with 0)\n")
    if sudoku_board:
        for row in sudoku_board:
            print(row)

    # Create a SudokuBoard object with the parsed Sudoku board
    mySudoku = SudokuBoard(sudoku_board)

    # Attempt to solve the Sudoku puzzle
    if mySudoku.rec_solve(0, 0):
        # If a solution is found, print the solved Sudoku board
        print("\nPuzzle Solved!\n")
        for row in mySudoku.grid:
            print(row)
    else:
        # If no solution is found, inform the user
        print("\nNo solution found.\n")

def parse_sudoku_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Split the string into rows
            rows = content.strip().split('\n')

            # Split each row into individual digits or underscores
            # Replace underscores with 0 for easier processing
            sudoku_board = [[int(cell) if cell.isdigit() else int(0) for cell in row.split()] for row in rows]

            return sudoku_board
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

class SudokuBoard:
    def __init__(self, grid):
        self.grid = grid

    def rec_solve(self, row, col):
        # Base case: If the current row is 9 and the current column is 0,
        # the Sudoku puzzle is solved, so return True.
        if row == 9 and col == 0:
            return True

        # If the current cell is not empty (not equal to 0),
        # move to the next cell (right or next row).
        if self.grid[row][col] != 0:
            if col == 8:
                return self.rec_solve(row + 1, 0)
            else:
                return self.rec_solve(row, col + 1)
        else:
            # The current cell is empty, so attempt to fill it with numbers from 1 to 9.
            for num in range(1, 10):
                if self.is_valid(num, row, col):
                    # If the number is valid, fill it in and continue solving.
                    self.grid[row][col] = num
                    if col == 8:
                        if self.rec_solve(row + 1, 0):
                            return True
                    else:
                        if self.rec_solve(row, col + 1):
                            return True
                    # Backtrack by setting the current cell back to 0
                    self.grid[row][col] = 0
            return False

    def is_valid(self, num, row, col):
        # Check if placing 'num' in the current cell is valid
        # based on Sudoku rules (box, row, and column checks).
        # Returns True if valid, False otherwise.

        # Check box
        box_start_row = (row // 3) * 3
        box_start_col = (col // 3) * 3

        for i in range(box_start_row, box_start_row + 3):
            for j in range(box_start_col, box_start_col + 3):
                if self.grid[i][j] == num:
                    return False

        # Check row
        if num in self.grid[row]:
            return False

        # Check column
        if any(i[col] == num for i in self.grid):
            return False

        return True

if __name__ == '__main__':
    main()
