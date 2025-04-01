from core.sudoku_grid import SudokuGrid  # Importe la classe 'SudokuGrid' depuis le module 'sudoku_grid' dans le dossier 'core', utilisée pour gérer la grille de Sudoku.
from core.solver import solve_backtracking, solve_brute_force  # Importe les fonctions 'solve_backtracking' et 'solve_brute_force' depuis le module 'solver' dans 'core', utilisées pour résoudre le Sudoku.
from utils.tools import measure_time, print_comparison_table  # Importe les fonctions 'measure_time' et 'print_comparison_table' depuis le module 'tools' dans 'utils', utilisées pour mesurer le temps d'exécution et afficher une table de comparaison.

def run_terminal_solver(filename):
    # Définit la fonction principale qui exécute la résolution d'un Sudoku dans le terminal, en prenant un fichier en entrée.
    print(f"Chargement de la grille depuis : {filename}\n")  # Affiche un message indiquant le chemin du fichier de la grille.
    grid_bt = SudokuGrid(filename)  # Crée une instance de 'SudokuGrid' en chargeant la grille depuis le fichier spécifié pour le backtracking.
    grid_bf = SudokuGrid(filename)  # Crée une autre instance de 'SudokuGrid' en chargeant la même grille depuis le fichier pour la force brute.

    print("Grille initiale :")  # Affiche un message pour indiquer l'affichage de la grille initiale.
    grid_bt.display_terminal()  # Affiche la grille de Sudoku dans le terminal à l'aide de la méthode 'display_terminal' de l'objet 'grid_bt'.

    bt_result, bt_time = measure_time(solve_backtracking, grid_bt)  # Mesure le temps d'exécution de la fonction 'solve_backtracking' sur 'grid_bt' et récupère le résultat et le temps.
    bf_result, bf_time = measure_time(solve_brute_force, grid_bf)  # Mesure le temps d'exécution de la fonction 'solve_brute_force' sur 'grid_bf' et récupère le résultat et le temps.

    print("\nRésultat - Backtracking :")  # Affiche un message indiquant que le résultat du backtracking va être affiché.
    grid_bt.display_terminal()  # Affiche la grille après résolution avec le backtracking.
    print(f"Temps : {bt_time:.4f} s")  # Affiche le temps d'exécution du backtracking avec 4 chiffres après la virgule.

    print("\nRésultat - Force Brute :")  # Affiche un message indiquant que le résultat de la force brute va être affiché.
    grid_bf.display_terminal()  # Affiche la grille après résolution avec la méthode de force brute.
    print(f"Temps : {bf_time:.4f} s")  # Affiche le temps d'exécution de la force brute avec 4 chiffres après la virgule.

    print_comparison_table(bt_result, bt_time, bf_result, bf_time)  # Affiche une table de comparaison des résultats et des temps pour le backtracking et la force brute.

if __name__ == "__main__":  # Vérifie si le script est exécuté directement (pas importé en tant que module).
    print("Choisissez une grille de Sudoku (1 a 5) :")  # Demande à l'utilisateur de choisir un fichier de grille de Sudoku.
    choice = input(">>> ")  # Attend la saisie de l'utilisateur pour choisir une grille (1 à 5).
    path = f"sudokus/exemple{choice}.txt"  # Construit le chemin du fichier de la grille choisi par l'utilisateur (exemple1.txt, exemple2.txt, etc.).
    run_terminal_solver(path)  # Appelle la fonction 'run_terminal_solver' avec le chemin du fichier choisi pour résoudre et afficher la grille.