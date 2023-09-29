import pygame

pygame.init()
pygame.font.init()


#color constants 
WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

DARK_GREEN = (50,240,10)

BLUE = (0, 0, 255)

#frames per second
FPS = 100

WIDTH, HEIGHT = 700, 700

#pixels to be drawn
ROWS, COLS = 200, 200



TOOLBAR_HEIGHT = HEIGHT - WIDTH

#because the toolbar height takes width from height, the usable length for
#height ends up being the same as width, so we can use WIDTH//COLS
#and the height of the pixel willbe the same bacause 700 - 100 = usable height = 600
PIXEL_SIZE = WIDTH//COLS


BG_COLOR = WHITE

DRAW_GRID_LINES = False

def get_font(size):
    return pygame.font.SysFont("comicsans", size)
