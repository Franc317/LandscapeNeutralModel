from tools import *

import random

size = 2000

matrix = []

p = 30

for i in range(size):
    matrix.append(random.randrange(0,100))

matrix_proportion_environment = []

for i in range(len(matrix) - 1):
    if matrix[i] < p:
        matrix_proportion_environment.append(1)
    else:
        matrix_proportion_environment.append(0)


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("landscape neutral model")
icon = pygame.image.load("landscape_icon.png")
pygame.display.set_icon(icon)


#creates a matrix in which each entry i, j is a tuple of colors.
def init_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)


    return grid

#initializing the grid 
grid = init_grid(ROWS, COLS, BG_COLOR)

def draw_grid(win, grid):
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j *PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE),
                             (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0),
                             (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))



def draw(win, grid):
    win.fill(BG_COLOR)
    draw_grid(win, grid)


    pygame.display.update()


run = True
clock = pygame.time.Clock()
drawing_color = BLACK


while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        
        for i in matrix_proportion_environment:
            rows = random.randint(0, ROWS -1)
            cols = random.randint(0,COLS -1)
            pixel_set = matrix_proportion_environment[random.randint(0,len(matrix_proportion_environment) - 1)]
            if pixel_set == 1:
                grid[rows][cols] = drawing_color
            else:
                grid[rows][cols] = WHITE
       


    draw(WIN, grid)





pygame.quit()
