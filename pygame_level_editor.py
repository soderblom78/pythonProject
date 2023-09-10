import csv
# import pickle
import pygame
import button
import os

pygame.init()
pygame.mixer.init()

FPS = 60
clock = pygame.time.Clock()


# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption("Level Editor")

# define game variables
ROWS = 16
MAX_COLS = 150
TILE_TYPES = 21
current_tile = 0
level = 0
TILE_SIZE = SCREEN_HEIGHT // ROWS

scroll_left = False
scroll_right = False

scroll = 0
scroll_speed = 1

# define font
font = pygame.font.SysFont("Futura", 30)

# define sound
s = "sound"
mouse_clicked = pygame.mixer.Sound(os.path.join(s, 'mouse_click.wav'))

# load images
sky_img = pygame.image.load("images/backgrounds/sky_cloud.png").convert_alpha()
mountain_img = pygame.image.load("images/backgrounds/mountain.png").convert_alpha()
pine_1_img = pygame.image.load("images/backgrounds/pine1.png").convert_alpha()
pine_2_img = pygame.image.load("images/backgrounds/pine2.png").convert_alpha()
mountain2_img = pygame.image.load("images/backgrounds/forest_1.png").convert_alpha()
# store tiles in a list
tile_list = []
for x in range(21):
    img = pygame.image.load(f"images/tile/{x}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    tile_list.append(img)

save_img = pygame.image.load("images/save_btn.png").convert_alpha()
load_img = pygame.image.load("images/load_btn.png").convert_alpha()

# define colours
GREEN = (0, 204, 0)
WHITE = (255, 255, 255)
RED = (200, 25, 25)
YELLOW = (232, 209, 134)

# create empty tile list
world_data = []

for rows in range(ROWS):
    r = [-1] * MAX_COLS
    world_data.append(r)

# create ground
for tile in range(0, MAX_COLS):
    world_data[ROWS - 1][tile] = 0


# function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_bg():
    screen.fill(GREEN)
    width = sky_img.get_width()
    for x in range(4):
        screen.blit(sky_img, ((x * width) - scroll * 0.5, 0))
        screen.blit(mountain_img, ((x * width) - scroll * 0.7, SCREEN_HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine_1_img, ((x * width) - scroll * 0.7, SCREEN_HEIGHT - pine_1_img.get_height() - 150))
        screen.blit(pine_2_img, ((x * width) - scroll * 0.8, SCREEN_HEIGHT - pine_2_img.get_height()))


# draw grid
def draw_grid():
    # vertical lines
    for c in range(MAX_COLS + 1):
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE - scroll, SCREEN_HEIGHT))
    # horizontal lines
    for c in range(ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, c * TILE_SIZE), (SCREEN_WIDTH, c * TILE_SIZE))


# function for drawing the world tiles
def draw_world():
    for y, row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                screen.blit(tile_list[tile], (x * TILE_SIZE - scroll, y * TILE_SIZE))


# create buttons
save_button = button.Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT + LOWER_MARGIN - 70, save_img, 1)
load_button = button.Button(SCREEN_WIDTH // 2 + 200, SCREEN_HEIGHT + LOWER_MARGIN - 70, load_img, 1)

# make a button list
button_list = []
button_col = 0
button_row = 0
for i in range(len(tile_list)):
    tile_button = button.Button(SCREEN_WIDTH + (75 * button_col) + 50, 75 * button_row + 50, tile_list[i], 1)
    button_list.append(tile_button)
    button_col += 1
    if button_col == 3:
        button_row += 1
        button_col = 0


run = True
while run:
    clock.tick(FPS)

    draw_bg()
    draw_grid()
    draw_world()

    draw_text(f"Level: {level}", font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 90)
    draw_text("Press UP or DOWN to change level", font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 60)

    # save and load data
    if save_button.draw(screen):
        pygame.draw.rect(screen, WHITE, save_button.rect, 5)
        pygame.mixer.Sound.play(mouse_clicked)
        # save level data
        with open(f"level{level}_data.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            for row in world_data:
                writer.writerow(row)

    if load_button.draw(screen):
        # highlight the selected tile
        pygame.draw.rect(screen, WHITE, load_button.rect, 5)
        pygame.mixer.Sound.play(mouse_clicked)
        # load in level data
        # reset scroll back to the start of the level
        scroll = 0

        with open(f"level{level}_data.csv", newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    world_data[x][y] = int(tile)

    # draw tile panels and tiles
    pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

    # chose a tile
    button_count = 0

    for button_count, i in enumerate(button_list):
        if i.draw(screen):
            pygame.mixer.Sound.play(mouse_clicked)
            current_tile = button_count

    # highlight the selected tile
    pygame.draw.rect(screen, RED, button_list[current_tile].rect, 3)

    # scroll the map
    if scroll_left and scroll > 5:
        scroll -= 5 * scroll_speed
    if scroll_right and scroll < (MAX_COLS * TILE_SIZE) - SCREEN_WIDTH:
        scroll += 5 * scroll_speed

    # add new tiles to the screen
    # get mouse position
    pos = pygame.mouse.get_pos()
    x = (pos[0] + scroll) // TILE_SIZE
    y = (pos[1]) // TILE_SIZE

    # check that the coordinates are within the tile area
    if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
        # update tile value
        if pygame.mouse.get_pressed()[0] == 1:
            if world_data[y][x] != current_tile:
                world_data[y][x] = current_tile
                pygame.mixer.Sound.play(mouse_clicked)
        if pygame.mouse.get_pressed()[2] == 1:
            world_data[y][x] = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
            if event.key == pygame.K_DOWN and level > 0:
                level -= 1
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 5

        # keyboard released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1

    pygame.display.update()

pygame.quit()





