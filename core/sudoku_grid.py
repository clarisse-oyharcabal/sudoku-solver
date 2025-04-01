import copy  # Importation du module 'copy' pour effectuer des copies profondes d'objets

class SudokuGrid:
    def __init__(self, grid_file=None):
        # Initialisation de la grille de Sudoku avec une grille vide (0 dans chaque case)
        self.grid = [[0 for _ in range(9)] for _ in range(9)]  # Crée une grille 9x9 remplie de 0
        # Crée une grille pour marquer les cases originales, toutes initialisées à False
        self.original = [[False for _ in range(9)] for _ in range(9)]
        # Si un fichier est passé en paramètre, charge la grille depuis le fichier
        if grid_file:
            self.load_from_file(grid_file)

    def load_from_file(self, filename):
        # Charge la grille de Sudoku depuis un fichier donné
        with open(filename, 'r') as file:
            lines = file.readlines()  # Lit toutes les lignes du fichier
            for i in range(9):  # Parcourt chaque ligne de la grille
                for j in range(9):  # Parcourt chaque colonne de la ligne
                    char = lines[i][j]  # Lit chaque caractère du fichier
                    if char != '_' and char != '\n':  # Ignore les cases vides (représentées par '_')
                        self.grid[i][j] = int(char)  # Remplit la case avec le nombre (1-9)
                        self.original[i][j] = True  # Marque cette case comme étant originale (pré-remplie)

    def display_terminal(self):
        # Affiche la grille de Sudoku dans la console de manière lisible
        print("Grille Sudoku :\n")
        for i in range(9):  # Parcourt chaque ligne de la grille
            row = ""  # Initialise une chaîne vide pour la ligne
            for j in range(9):  # Parcourt chaque colonne de la ligne
                value = self.grid[i][j]  # Récupère la valeur de la case
                if self.original[i][j]:  # Si la case est originale (pré-remplie)
                    row += f"\033[1m{value}\033[0m "  # Affiche en gras la valeur
                else:
                    row += f"{value if value != 0 else '_'} "  # Affiche '_' si la case est vide
                if j % 3 == 2:  # Ajoute un séparateur "|" toutes les 3 cases
                    row += "| "
            print(row)  # Affiche la ligne
            if i % 3 == 2:  # Ajoute une ligne de séparation toutes les 3 lignes
                print("-" * 25)

    def is_valid(self, row, col, num):
        # Vérifie si un numéro est valide pour une position donnée (row, col)
        if num in self.grid[row]:  # Vérifie si le numéro existe déjà dans la ligne
            return False
        if num in [self.grid[i][col] for i in range(9)]:  # Vérifie si le numéro existe déjà dans la colonne
            return False
        # Calcul des coordonnées du sous-grille 3x3 contenant la case (row, col)
        box_row = row - row % 3
        box_col = col - col % 3
        for i in range(3):  # Parcourt les 3 lignes du sous-grille
            for j in range(3):  # Parcourt les 3 colonnes du sous-grille
                if self.grid[box_row + i][box_col + j] == num:  # Vérifie si le numéro est déjà dans la sous-grille
                    return False
        return True  # Si aucune condition de conflit n'est trouvée, le numéro est valide

    def is_valid_grid(self, grid):
        # Vérifie si une grille (potentiellement modifiée) est valide
        for row in range(9):  # Parcourt chaque ligne de la grille
            for col in range(9):  # Parcourt chaque colonne de la ligne
                num = grid[row][col]  # Récupère la valeur de la case
                if num != 0:  # Si la case n'est pas vide
                    grid[row][col] = 0  # Réinitialise temporairement la case pour vérifier la validité
                    if not self.is_valid(row, col, num):  # Vérifie la validité du numéro dans cette position
                        grid[row][col] = num  # Restaure la valeur dans la case
                        return False  # Si le numéro n'est pas valide, retourne False
                    grid[row][col] = num  # Restaure la valeur de la case
        return True  # Si toutes les cases sont valides, retourne True

    def copy(self):
        # Crée et retourne une copie profonde de l'objet SudokuGrid
        return copy.deepcopy(self)
        # Utilise deepcopy pour s'assurer que les modifications sur la copie n'affectent pas l'original