import pygame
import sys
from core.sudoku_grid import SudokuGrid
from core.solver import solve_backtracking

WIDTH, HEIGHT = 540, 600
CELL_SIZE = WIDTH // 9
FPS = 30

# Définition de couleurs plus originales et modernes
WHITE = (240, 240, 240)
BLACK = (20, 20, 20)
BLUE = (30, 144, 255)
GREY = (160, 160, 160)
DARK_GREY = (50, 50, 50)
ORANGE = (255, 140, 0)
RED = (220, 20, 60)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver - Original")
# Police personnalisée pour le titre
title_font = pygame.font.SysFont("comicsansms", 40)
font = pygame.font.SysFont("arial", 30)
small_font = pygame.font.SysFont("arial", 20)
clock = pygame.time.Clock()

def draw_gradient_background(surface, color1, color2):
    """Dessine un dégradé vertical sur la surface."""
    rect = surface.get_rect()
    height = rect.height
    for y in range(height):
        ratio = y / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        pygame.draw.line(surface, (r, g, b), (0, y), (rect.width, y))

def draw_title():
    """Affiche le titre avec un effet d'ombre pour plus d'originalité."""
    title_text = title_font.render("Sudoku Solver", True, ORANGE)
    shadow_text = title_font.render("Sudoku Solver", True, DARK_GREY)
    # Ombre décalée
    screen.blit(shadow_text, (WIDTH//2 - shadow_text.get_width()//2 + 2, 10 + 2))
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 10))

def draw_grid(grid_obj):
    # Création d'une surface pour le fond de la grille avec dégradé
    grid_surface = pygame.Surface((WIDTH, WIDTH))
    draw_gradient_background(grid_surface, WHITE, GREY)
    screen.blit(grid_surface, (0, 50))
    
    # Dessiner les lignes de la grille
    for i in range(10):
        width_line = 3 if i % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, 50 + i * CELL_SIZE), (WIDTH, 50 + i * CELL_SIZE), width_line)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 50), (i * CELL_SIZE, 50 + WIDTH), width_line)

    # Affichage des chiffres avec effet d'ombre
    for i in range(9):
        for j in range(9):
            value = grid_obj.grid[i][j]
            if value != 0:
                color = BLUE if grid_obj.original[i][j] else BLACK
                bold = grid_obj.original[i][j]
                draw_number(value, i, j, color, bold)

def draw_number(num, row, col, color, bold=False):
    """Affiche un chiffre avec une ombre pour un effet 3D."""
    font_to_use = pygame.font.SysFont("arial", 30, bold=bold)
    text = font_to_use.render(str(num), True, color)
    shadow = font_to_use.render(str(num), True, GREY)
    x = col * CELL_SIZE + (CELL_SIZE // 2 - text.get_width() // 2)
    y = row * CELL_SIZE + 50 + (CELL_SIZE // 2 - text.get_height() // 2)
    screen.blit(shadow, (x + 2, y + 2))
    screen.blit(text, (x, y))

def animate_solver(grid_obj):
    """
    Résolution animée avec effet de surbrillance sur la case en cours d'exécution.
    Retourne True si le sudoku est résolu.
    """
    for row in range(9):
        for col in range(9):
            if grid_obj.grid[row][col] == 0:
                for num in range(1, 10):
                    if grid_obj.is_valid(row, col, num):
                        grid_obj.grid[row][col] = num
                        draw_grid(grid_obj)
                        # Dessine un cercle rouge autour de la case en cours
                        center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + 50 + CELL_SIZE // 2)
                        pygame.draw.circle(screen, RED, center, CELL_SIZE // 2 - 5, 3)
                        pygame.display.update()
                        pygame.time.delay(50)
                        if animate_solver(grid_obj):
                            return True
                        grid_obj.grid[row][col] = 0
                        draw_grid(grid_obj)
                        pygame.display.update()
                        pygame.time.delay(50)
                return False
    return True

def draw_footer(text, color=BLACK):
    """Affiche une barre d'information en bas de l'écran avec fond semi-transparent."""
    footer_bg = pygame.Surface((WIDTH, 30))
    footer_bg.set_alpha(200)
    footer_bg.fill(WHITE)
    screen.blit(footer_bg, (0, HEIGHT - 30))
    footer = small_font.render(text, True, color)
    screen.blit(footer, (10, HEIGHT - 25))

def run_pygame_interface():
    current_grid = None
    running = True
    selected = False

    while running:
        screen.fill(WHITE)
        draw_title()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and not selected:
                if event.unicode in ['1', '2', '3', '4', '5']:
                    idx = event.unicode
                    path = f"sudokus/exemple{idx}.txt"
                    current_grid = SudokuGrid(path)
                    selected = True
            elif event.type == pygame.KEYDOWN and selected:
                if event.key == pygame.K_RETURN:
                    if current_grid:
                        animate_solver(current_grid)

        if selected and current_grid:
            draw_grid(current_grid)
            draw_footer("Appuie sur Entrée pour résoudre", GREY)
        else:
            draw_footer("Choisis une grille (1 à 5)...", RED)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()
