def solve_backtracking(grid_obj):
    # Parcourt chaque ligne (de 0 à 8)
    for row in range(9):
        # Parcourt chaque colonne (de 0 à 8)
        for col in range(9):
            # Vérifie si la case est vide (0 indique une case vide)
            if grid_obj.grid[row][col] == 0:
                # Tente de remplir la case avec un nombre entre 1 et 9
                for num in range(1, 10):
                    # Vérifie si le numéro est valide dans cette position
                    if grid_obj.is_valid(row, col, num):
                        # Assigne le numéro à la case
                        grid_obj.grid[row][col] = num
                        # Appelle récursivement la fonction pour résoudre le reste du Sudoku
                        if solve_backtracking(grid_obj):
                            return True
                        # Si ce n'est pas une solution, réinitialise la case à 0 (backtracking)
                        grid_obj.grid[row][col] = 0
                # Si aucun numéro valide n'est trouvé, retourne False (échoue cette branche)
                return False
    # Si toutes les cases sont remplies correctement, retourne True
    return True


def solve_brute_force(grid_obj):
    from copy import deepcopy  # Importe la fonction deepcopy pour créer une copie du tableau

    def helper(grid):
        # Parcourt chaque ligne du grid
        for row in range(9):
            # Parcourt chaque colonne du grid
            for col in range(9):
                # Vérifie si la case est vide (0 indique une case vide)
                if grid[row][col] == 0:
                    # Tente de remplir la case avec un numéro de 1 à 9
                    for num in range(1, 10):
                        grid[row][col] = num  # Assigne temporairement le numéro à la case
                        # Vérifie si le grid est valide après l'assignation
                        if grid_obj.is_valid_grid(grid):
                            # Appelle récursivement la fonction pour résoudre le reste du Sudoku
                            if helper(grid):
                                return True
                        grid[row][col] = 0  # Si ce n'est pas une solution, réinitialise la case à 0
                    # Si aucun numéro valide n'est trouvé pour cette case, échoue cette branche
                    return False
        # Si toutes les cases sont remplies correctement, retourne True
        return True

    # Crée une copie du grid original pour éviter de modifier directement grid_obj.grid
    temp_grid = deepcopy(grid_obj.grid)
    # Appelle la fonction helper pour résoudre le Sudoku avec la copie du grid
    if helper(temp_grid):
        # Si une solution est trouvée, met à jour grid_obj avec la solution
        grid_obj.grid = temp_grid
        return True
    # Si aucune solution n'est trouvée, retourne False
    return False
