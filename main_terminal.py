
from core.sudoku_grid import SudokuGrid
from core.solver import solve_backtracking, solve_brute_force
from utils.tools import measure_time, print_comparison_table

def run_terminal_solver(filename):
    print(f"Chargement de la grille depuis : {filename}\n")
    grid_bt = SudokuGrid(filename)
    grid_bf = SudokuGrid(filename)

    print("Grille initiale :")
    grid_bt.display_terminal()

    bt_result, bt_time = measure_time(solve_backtracking, grid_bt)
    bf_result, bf_time = measure_time(solve_brute_force, grid_bf)

    print("\nRésultat - Backtracking :")
    grid_bt.display_terminal()
    print(f"Temps : {bt_time:.4f} s")

    print("\nRésultat - Force Brute :")
    grid_bf.display_terminal()
    print(f"Temps : {bf_time:.4f} s")

    print_comparison_table(bt_result, bt_time, bf_result, bf_time)

if __name__ == "__main__":
    print("Choisissez une grille de Sudoku (1 à 5) :")
    choice = input(">>> ")
    path = f"sudokus/exemple{choice}.txt"
    run_terminal_solver(path)
