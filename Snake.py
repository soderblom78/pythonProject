import pygame

pygame.init()

screen_width = 700
screen_height = 700

surface = pygame.display.set_mode((700, 700))
color = (135, 206, 235)
surface.fill(color)
pygame.display.flip()


pygame.display.set_caption("Platformer")

# load images
sun_img = pygame.image.load("images/sun.png")
bg_img = pygame.image.load("images/favpng_sky-blue-cloud.png")

# define game variables
tile_size = 140


def draw(self):
    for tile in self.tile_list:
        surface.blit(tile[0], tile[1])


class World():
    def _init_(self, data):
        self.tile_list = []

    # load images
    dirt_img = pygame.image.load("images/dirt.png")
    row_count = 0
    for row in data:
        col_count = 0
        for tile in row:
            if tile == 1:
                img = dirt_img
                img_rect = img.get_rect()
                img_rect.x = col_count * tile_size
                img_rect.y = row_count * tile_size
                tile = (img, img_rect)
                self.tile_list.append(tile)
            col_count += 1
        row_count += 1


world_data = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]

world = World(world_data)

run = True
while run:

    surface.blit(bg_img, (0, 0))
    surface.blit(sun_img, (50, 50))

    world.draw()
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False

    pygame.display.update()

pygame.quit()






