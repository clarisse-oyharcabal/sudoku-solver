import pygame  # Importation de la bibliothèque pygame pour la création du jeu.
import sys  # Importation de la bibliothèque sys pour la gestion des arguments et la sortie du programme.
from core.sudoku_grid import SudokuGrid  # Importation de la classe SudokuGrid à partir du module core.sudoku_grid pour la gestion de la grille de Sudoku.
from core.solver import solve_backtracking  # Importation de la fonction solve_backtracking à partir du module core.solver pour résoudre le Sudoku.

WIDTH, HEIGHT = 540, 600  # Définition de la largeur (540 px) et de la hauteur (600 px) de la fenêtre du jeu.
CELL_SIZE = WIDTH // 9  # Définition de la taille d'une cellule de la grille (largeur de la fenêtre divisé par 9).
FPS = 30  # Nombre d'images par seconde (30 fps) pour la mise à jour de l'écran.

# Définition de couleurs plus originales et modernes en format RGB.
WHITE = (240, 240, 240)  # Blanc clair.
BLACK = (20, 20, 20)  # Noir très foncé.
BLUE = (30, 144, 255)  # Bleu clair.
GREY = (160, 160, 160)  # Gris moyen.
DARK_GREY = (50, 50, 50)  # Gris foncé.
ORANGE = (255, 140, 0)  # Orange vif.
RED = (220, 20, 60)  # Rouge intense.

pygame.init()  # Initialisation de la bibliothèque pygame.
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Création de la fenêtre de jeu avec les dimensions spécifiées.
pygame.display.set_caption("Sudoku Solver - Original")  # Définition du titre de la fenêtre.
title_font = pygame.font.SysFont("comicsansms", 40)  # Police pour le titre du jeu avec taille 40.
font = pygame.font.SysFont("arial", 30)  # Police pour les chiffres et autres textes avec taille 30.
small_font = pygame.font.SysFont("arial", 20)  # Police pour les petits textes avec taille 20.
clock = pygame.time.Clock()  # Création d'un objet horloge pour contrôler le nombre de frames par seconde.

def draw_gradient_background(surface, color1, color2):
    """Dessine un dégradé vertical sur la surface."""
    rect = surface.get_rect()  # Obtient les dimensions de la surface.
    height = rect.height  # Hauteur de la surface.
    for y in range(height):  # Boucle sur chaque pixel en hauteur.
        ratio = y / height  # Calcul du ratio pour la transition de couleur.
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)  # Calcul de la couleur rouge en fonction du ratio.
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)  # Calcul de la couleur verte.
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)  # Calcul de la couleur bleue.
        pygame.draw.line(surface, (r, g, b), (0, y), (rect.width, y))  # Dessine une ligne de la couleur calculée.

def draw_title():
    """Affiche le titre avec un effet d'ombre pour plus d'originalité."""
    title_text = title_font.render("Sudoku Solver", True, ORANGE)  # Crée l'image du texte "Sudoku Solver" en orange.
    shadow_text = title_font.render("Sudoku Solver", True, DARK_GREY)  # Crée l'image du texte en gris foncé pour l'ombre.
    # Ombre décalée
    screen.blit(shadow_text, (WIDTH//2 - shadow_text.get_width()//2 + 2, 3 + 2))  # Dessine l'ombre décalée.
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 2))  # Dessine le texte principal au-dessus de l'ombre.

def draw_grid(grid_obj):
    # Création d'une surface pour le fond de la grille avec dégradé
    grid_surface = pygame.Surface((WIDTH, WIDTH))  # Crée une nouvelle surface pour la grille.
    draw_gradient_background(grid_surface, WHITE, GREY)  # Dessine le fond dégradé sur cette surface.
    screen.blit(grid_surface, (0, 50))  # Affiche la surface dégradée à l'écran à la position (0, 50).
    
    # Dessiner les lignes de la grille
    for i in range(10):  # Pour chaque ligne et colonne de la grille.
        width_line = 3 if i % 3 == 0 else 1  # Ligne plus épaisse tous les 3 indices pour délimiter les sous-grilles.
        pygame.draw.line(screen, BLACK, (0, 50 + i * CELL_SIZE), (WIDTH, 50 + i * CELL_SIZE), width_line)  # Dessine la ligne horizontale.
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 50), (i * CELL_SIZE, 50 + WIDTH), width_line)  # Dessine la ligne verticale.

    # Affichage des chiffres avec effet d'ombre
    for i in range(9):  # Pour chaque ligne de la grille.
        for j in range(9):  # Pour chaque colonne de la grille.
            value = grid_obj.grid[i][j]  # Récupère la valeur dans la grille.
            if value != 0:  # Si la cellule n'est pas vide.
                color = BLUE if grid_obj.original[i][j] else BLACK  # Bleu si c'est une valeur d'origine, noir sinon.
                bold = grid_obj.original[i][j]  # Gras si c'est une valeur d'origine.
                draw_number(value, i, j, color, bold)  # Affiche le chiffre avec la couleur et le style.

def draw_number(num, row, col, color, bold=False):
    """Affiche un chiffre avec une ombre pour un effet 3D."""
    font_to_use = pygame.font.SysFont("arial", 30, bold=bold)  # Crée la police pour afficher les chiffres.
    text = font_to_use.render(str(num), True, color)  # Crée l'image du texte du chiffre avec la couleur spécifiée.
    shadow = font_to_use.render(str(num), True, GREY)  # Crée l'image de l'ombre du texte en gris.
    x = col * CELL_SIZE + (CELL_SIZE // 2 - text.get_width() // 2)  # Calcule la position horizontale pour centrer le texte.
    y = row * CELL_SIZE + 50 + (CELL_SIZE // 2 - text.get_height() // 2)  # Calcule la position verticale pour centrer le texte.
    screen.blit(shadow, (x + 2, y + 2))  # Dessine l'ombre du texte avec un décalage.
    screen.blit(text, (x, y))  # Dessine le texte principal.

def animate_solver(grid_obj):
    """
    Résolution animée avec effet de surbrillance sur la case en cours d'exécution.
    Retourne True si le sudoku est résolu.
    """
    for row in range(9):  # Pour chaque ligne.
        for col in range(9):  # Pour chaque colonne.
            if grid_obj.grid[row][col] == 0:  # Si la cellule est vide.
                for num in range(1, 10):  # Pour chaque chiffre de 1 à 9.
                    if grid_obj.is_valid(row, col, num):  # Si le chiffre est valide dans la case.
                        grid_obj.grid[row][col] = num  # Remplir la cellule avec le chiffre.
                        draw_grid(grid_obj)  # Redessine la grille après le changement.
                        # Dessine un cercle rouge autour de la case en cours.
                        center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + 50 + CELL_SIZE // 2)
                        pygame.draw.circle(screen, RED, center, CELL_SIZE // 2 - 5, 3)
                        pygame.display.update()  # Met à jour l'écran.
                        pygame.time.delay(50)  # Attends 50 ms pour créer l'animation.
                        if animate_solver(grid_obj):  # Appel récursif pour résoudre le Sudoku.
                            return True  # Si le Sudoku est résolu, retourne True.
                        grid_obj.grid[row][col] = 0  # Si la tentative échoue, réinitialise la cellule.
                        draw_grid(grid_obj)  # Redessine la grille sans la modification.
                        pygame.display.update()  # Met à jour l'écran.
                        pygame.time.delay(50)  # Attends à nouveau avant de continuer.
                return False  # Si aucun chiffre valide n'a été trouvé, retourne False.
    return True  # Si la grille est complètement remplie, retourne True (résolu).

def draw_footer(text, color=BLACK):
    """Affiche une barre d'information en bas de l'écran avec fond semi-transparent."""
    footer_bg = pygame.Surface((WIDTH, 30))  # Crée une surface pour le fond de la barre d'information.
    footer_bg.set_alpha(200)  # Applique une transparence au fond de la barre.
    footer_bg.fill(WHITE)  # Remplie la surface avec la couleur blanche.
    screen.blit(footer_bg, (0, HEIGHT - 30))  # Dessine la barre d'information à la position du bas de l'écran.
    footer = small_font.render(text, True, color)  # Crée l'image du texte à afficher dans la barre.
    screen.blit(footer, (10, HEIGHT - 25))  # Dessine le texte dans la barre d'information.

def run_pygame_interface():
    current_grid = None  # Variable pour stocker la grille de Sudoku actuelle.
    running = True  # Condition pour continuer la boucle principale.
    selected = False  # Indicateur pour savoir si une grille a été sélectionnée.

    while running:  # Boucle principale du jeu.
        screen.fill(WHITE)  # Remplie l'écran avec la couleur blanche.
        draw_title()  # Dessine le titre du jeu.
        for event in pygame.event.get():  # Gère les événements (clavier, fermeture de la fenêtre, etc.).
            if event.type == pygame.QUIT:  # Si l'utilisateur ferme la fenêtre.
                running = False  # Quitte la boucle principale.
            if event.type == pygame.KEYDOWN and not selected:  # Si une touche est pressée et aucune grille n'est sélectionnée.
                if event.unicode in ['1', '2', '3', '4', '5']:  # Si la touche correspond à une grille (1 à 5).
                    idx = event.unicode  # Récupère le numéro de la grille sélectionnée.
                    path = f"sudokus/exemple{idx}.txt"  # Crée le chemin du fichier de grille.
                    current_grid = SudokuGrid(path)  # Charge la grille depuis le fichier.
                    selected = True  # Marque que la grille est sélectionnée.
            elif event.type == pygame.KEYDOWN and selected:  # Si une grille est sélectionnée et une touche est pressée.
                if event.key == pygame.K_RETURN:  # Si la touche Entrée est pressée.
                    if current_grid:  # Si une grille est chargée.
                        animate_solver(current_grid)  # Lance la résolution animée du Sudoku.

        if selected and current_grid:  # Si une grille est sélectionnée et existe.
            draw_grid(current_grid)  # Affiche la grille.
            draw_footer("Appuie sur Entrée pour résoudre", GREY)  # Affiche un message dans le footer.
        else:
            draw_footer("Choisis une grille (1 à 5)...", RED)  # Message invitant l'utilisateur à choisir une grille.

        pygame.display.update()  # Met à jour l'affichage de la fenêtre.
        clock.tick(FPS)  # Limite à 30 frames par seconde.

    pygame.quit()  # Quitte pygame proprement.
    sys.exit()  # Ferme le programme.
