import copy

class SudokuGrid:
    def __init__(self, grid_file=None):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.original = [[False for _ in range(9)] for _ in range(9)]
        if grid_file:
            self.load_from_file(grid_file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i in range(9):
                for j in range(9):
                    char = lines[i][j]
                    if char != '_' and char != '\n':
                        self.grid[i][j] = int(char)
                        self.original[i][j] = True

    def display_terminal(self):
        print("Grille Sudoku :\n")
        for i in range(9):
            row = ""
            for j in range(9):
                value = self.grid[i][j]
                if self.original[i][j]:
                    row += f"\033[1m{value}\033[0m "
                else:
                    row += f"{value if value != 0 else '_'} "
                if j % 3 == 2:
                    row += "| "
            print(row)
            if i % 3 == 2:
                print("-" * 25)

    def is_valid(self, row, col, num):
        if num in self.grid[row]:
            return False
        if num in [self.grid[i][col] for i in range(9)]:
            return False
        box_row = row - row % 3
        box_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[box_row + i][box_col + j] == num:
                    return False
        return True

    def is_valid_grid(self, grid):
        for row in range(9):
            for col in range(9):
                num = grid[row][col]
                if num != 0:
                    grid[row][col] = 0
                    if not self.is_valid(row, col, num):
                        grid[row][col] = num
                        return False
                    grid[row][col] = num
        return True

    def copy(self):
        return copy.deepcopy(self)
