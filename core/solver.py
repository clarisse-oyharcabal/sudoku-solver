def solve_backtracking(grid_obj):
    for row in range(9):
        for col in range(9):
            if grid_obj.grid[row][col] == 0:
                for num in range(1, 10):
                    if grid_obj.is_valid(row, col, num):
                        grid_obj.grid[row][col] = num
                        if solve_backtracking(grid_obj):
                            return True
                        grid_obj.grid[row][col] = 0
                return False
    return True


def solve_brute_force(grid_obj):
    from copy import deepcopy
    def helper(grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        grid[row][col] = num
                        if grid_obj.is_valid_grid(grid):
                            if helper(grid):
                                return True
                        grid[row][col] = 0
                    return False
        return True

    temp_grid = deepcopy(grid_obj.grid)
    if helper(temp_grid):
        grid_obj.grid = temp_grid
        return True
    return False
