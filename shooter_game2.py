import pygame
from pygame import mixer
import os
import random
import csv
import button

mixer.init()
pygame.init()

# setup screen
SIDE_MARGIN = 300
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = int((SCREEN_WIDTH + SIDE_MARGIN) * 0.5)
screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT))
pygame.display.flip()
pygame.display.set_caption("Roggas Shooter Game")

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# def game variables
GRAVITY = 0.7
SCROLL_THRESH = 200
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 29
MAX_LEVELS = 4
screen_scroll = 0
bg_scroll = 0
level = 1
start_game = False
in_game = False
start_intro = False
money_collect = 0
grenades_left = 0
ammo_left = 0
sniper_ammo_left = 0
health_left = 0
sniper_rifle = 0
enemy_position_x = []
enemy_position_y = []

# define player action variables
moving_left = False
moving_right = False
animal_moving_left = False
animal_moving_right = False
shell_moving_left = False
shell_moving_right = False
player_aim = False
aim_moving_left = False
aim_moving_right = False
aim_moving_up = False
aim_moving_down = False
camera_aim_moving_left = False
camera_aim_moving_right = False
camera_aim_moving_up = False
camera_aim_moving_down = False
zoom = 1
climbing = False
shoot = False
grab = False
main_action = False
throw_turtle = False
sniper_shoot = False
grenade = False
grenade_thrown = False


# load music and sounds
pygame.mixer.music.load("sound/music_loop.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1, 0.0, 5000)
jump_fx = pygame.mixer.Sound("sound/jump.wav")
pygame.mixer.Sound.set_volume(jump_fx, 0.2)
shoot_fx = pygame.mixer.Sound("sound/shoot.wav")
pygame.mixer.Sound.set_volume(shoot_fx, 0.2)
grenade_fx = pygame.mixer.Sound("sound/grenade.wav")
pygame.mixer.Sound.set_volume(grenade_fx, 0.2)
coin_fx = pygame.mixer.Sound("sound/coin.wav")
pygame.mixer.Sound.set_volume(coin_fx, 0.2)
coinbag_fx = pygame.mixer.Sound("sound/coin_bag.wav")
pygame.mixer.Sound.set_volume(coinbag_fx, 0.2)
die_fx = pygame.mixer.Sound("sound/player_die.wav")
pygame.mixer.Sound.set_volume(die_fx, 1)
bounce_fx = pygame.mixer.Sound("sound/bounce1.wav")
pygame.mixer.Sound.set_volume(bounce_fx, 0.2)
punch_fx = pygame.mixer.Sound("sound/punch.wav")
pygame.mixer.Sound.set_volume(bounce_fx, 0.2)
collect_fx = pygame.mixer.Sound("sound/collect.wav")
pygame.mixer.Sound.set_volume(bounce_fx, 0.2)
yahoo_fx = pygame.mixer.Sound("sound/yahoo.wav")
pygame.mixer.Sound.set_volume(bounce_fx, 0.2)
hurt_fx = pygame.mixer.Sound("sound/hurt.wav")
pygame.mixer.Sound.set_volume(bounce_fx, 0.2)


# load images
camera_img = pygame.image.load("images/camera.PNG").convert_alpha()
# button images
start_img = pygame.image.load("images/start_btn.png").convert_alpha()
exit_img = pygame.image.load("images/exit_btn.png").convert_alpha()
restart_img = pygame.image.load("images/restart_btn.png").convert_alpha()

# background images
pine1_img = pygame.image.load("images/backgrounds/pine1.png").convert_alpha()
pine2_img = pygame.image.load("images/backgrounds/pine2.png").convert_alpha()
mountain_img = pygame.image.load("images/backgrounds/mountain.png").convert_alpha()
sky_img = pygame.image.load("images/backgrounds/sky_cloud.png").convert_alpha()

# store tiles in a list
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f"images/tile/{x}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

# bullet
bullet_img = pygame.image.load("images/bullet.gif").convert_alpha()
# sniper_bullet
sniper_bullet_img = pygame.image.load("images/sniper_bullet.png").convert_alpha()
# sniper_bullet
sniper_bullet2_img = pygame.image.load("images/sniper_bullet2.png").convert_alpha()
# Aim
aim_img = pygame.image.load("images/aiming.png").convert_alpha()
# Grenade
grenade_img = pygame.image.load("images/Grenade2.gif").convert_alpha()
# broken_box
broken_box_img = pygame.image.load("images/broken_box.png").convert_alpha()
# Pick up boxes
health_box_img = pygame.image.load("images/Health_box2.gif").convert_alpha()
ammo_box_img = pygame.image.load("images/Ammo_box2.gif").convert_alpha()
grenade_box_img = pygame.image.load("images/Grenade_box2.gif").convert_alpha()
moneybag_img = pygame.image.load("images/moneybag.png").convert_alpha()
sniper_img = pygame.image.load("images/sniper_rifle.png").convert_alpha()

angry = ["Hell", "Stupid", "Holy cow!", "Poo on a stick!", "Son of a monkey!", "Phooey!", "holy shit", "bastard"]
happy = ["Wonderful day", "Great", "looking good!", "excellent", "Walking on cloud", "nice!", "amazing", "Beautiful"]
word = []
item_boxes = {
    "Health": health_box_img,
    "Ammo": ammo_box_img,
    "Grenade": grenade_box_img
}

# set background color

RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PINK = (235, 65, 54)
YELLOW = (255, 255, 51)
BG_COLOR = GREEN

# define font
font = pygame.font.SysFont("Futura", 30)


def draw_text(text, font, text_col, x, y, ):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def draw_bg():
    screen.fill(BG_COLOR)
    width = sky_img.get_width()
    for x in range(5):
        screen.blit(sky_img, ((x * width) - bg_scroll * 0.5, 0))
        screen.blit(mountain_img, ((x * width) - bg_scroll * 0.6, SCREEN_HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine1_img, ((x * width) - bg_scroll * 0.7, SCREEN_HEIGHT - pine1_img.get_height() - 150))
        screen.blit(pine2_img, ((x * width) - bg_scroll * 0.8, SCREEN_HEIGHT - pine2_img.get_height()))


def draw_tile_panels():
    pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH + 10, 10, SIDE_MARGIN - 20, SCREEN_HEIGHT - 20))
    screen.blit(camera_img, (SCREEN_WIDTH + 30, 20))


# function to reset level
def reset_level():
    if not in_game:
        money_group.empty()
        sniper_rifle_group.empty()
    grenade_group.empty()
    dancing_girl_group.empty()
    turtle_group.empty()
    bullet_group.empty()
    sniper_bullet_group.empty()
    ball_group.empty()
    enemy_group.empty()
    explosion_group.empty()
    bomb_box_group.empty()
    key_group.empty()
    for item_box in item_box_group:
        if item_box.item_type == "Money_bag":
            if not in_game:
                item_box_group.empty()
        else:
            item_box_group.empty()

    decoration_group.empty()
    ladder_group.empty()
    water_group.empty()
    exit_group.empty()

    # create empty tile list
    data = []
    for row in range(ROWS):
        r = [-1] * COLS
        data.append(r)

    return data


class Money(pygame.sprite.Sprite):
    def __init__(self, money_type, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.money_type = money_type
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # Idle = 0
        self.update_time = pygame.time.get_ticks()

        # load all images for the objects
        animation_types = ["Fixed", "Spinning"]

        for animation in animation_types:
            # reset temporary list of images
            temp_list = []

            # count number of files in folder
            num_of_frames = len(os.listdir(f"images/{self.money_type}/{animation}"))
            for i in range(num_of_frames):
                img = pygame.image.load(f"images/{self.money_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.start_x = x
        self.reset()

    def reset(self):
        self.rect.x = self.start_x

    def update(self):
        self.rect.x += screen_scroll
        self.update_animation()
        self.action = 1

        if self.rect.colliderect(player.rect.x, player.rect.y, player.width, player.height):
            player.money += 1
            coin_fx.play()
            self.kill()

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has past since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset back to start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


class Blood(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        for num in range(1):
            img = pygame.image.load(f"images/blood/{num}.png").convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
            self.images.append(img)
            self.frame_index = 0
            self.image = self.images[self.frame_index]

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        BLOOD_SPEED = 20
        # update explosion animation
        self.counter += 1
        if self.counter >= BLOOD_SPEED:
            self.counter = 0
            self.frame_index += 1
            # if the animation is complete then stop animation
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]


class MovingObjects(pygame.sprite.Sprite):
    def __init__(self, object_type, x, y, scale, direction, speed):
        pygame.sprite.Sprite.__init__(self)
        self.object_type = object_type
        self.speed = speed
        self.flip = False
        self.rolling = False
        self.moving_right = False
        self.direction = direction
        self.vel_y = 0
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # Idle = 0
        self.update_time = pygame.time.get_ticks()

        # load all images for the objects
        animation_types = ["Fixed", "Roll"]

        for animation in animation_types:
            # reset temporary list of images
            temp_list = []

            # count number of files in folder
            num_of_frames = len(os.listdir(f"images/{self.object_type}/{animation}"))
            for i in range(num_of_frames):
                img = pygame.image.load(f"images/{self.object_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()

    def not_moving(self):
        if not self.rolling:
            # reset movement variables
            dx = 0
            dy = 0

            if player.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height) and player.in_air:
                self.update_action(0)
                self.speed = 0
                player.vel_y = -12
                player.jump = False
                player.in_air = True

            if player.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height) and player.vel_y >= 1:
                player.vel_y = 0
                player.in_air = True

            # apply gravity
            self.vel_y += GRAVITY
            if self.vel_y > 30:
                self.vel_y = 0
            dy += self.vel_y

            for tile in world.obstacle_list:
                # check collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                    self.direction *= -1

                # check collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.vel_y >= 0:
                        self.vel_y = 0
                        dy = tile[1].top - self.rect.bottom

            if player.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height) and not player.in_air:
                if player.direction > 0:
                    self.moving_right = True
                else:
                    self.moving_right = False
                self.speed = 5
                self.rolling = True

            # check if fallen of the map
            if self.rect.bottom > SCREEN_HEIGHT:
                self.kill()

            # update rectangle position
            self.rect.y += dy
            self.rect.x += dx

    def move_ball(self):
        dx = 0
        player.speed = 5
        self.speed = 5
        if self.rolling:
            if self.moving_right:
                self.direction = 1
                self.flip = True

            elif not self.moving_right:
                self.direction = -1
                self.flip = False

            self.update_action(1)
            dx = self.speed * self.direction

        self.rect.x += dx

    def ball_collide(self):
        if self.rolling:
            dx = 0
            dx = self.speed * self.direction

            if player.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height) and player.in_air:
                self.rolling = False
                self.update_action(0)
                bounce_fx.play()
                self.speed = 0
                player.vel_y = -12
                player.jump = False
                player.in_air = True

            if player.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height) and not player.in_air:
                dx = 0
                if player.direction > 0 and self.direction > 0 or player.direction < 0 and self.direction > 0:
                    self.moving_right = False
                    player.speed *= -1
                else:
                    self.moving_right = True
                    player.speed *= -1

            for tile in world.obstacle_list:
                # check collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    bounce_fx.play()
                    if self.direction > 0:
                        self.moving_right = False
                    else:
                        self.moving_right = True

            self.rect.x += dx

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has past since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset back to start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

        # scroll
        self.rect.x += screen_scroll


class CollectAction(pygame.sprite.Sprite):
    def __init__(self, action_type, x, y, scale, direction, speed):
        pygame.sprite.Sprite.__init__(self)
        self.action_type = action_type
        self.speed = speed
        self.timer = 0
        self.flip = False
        self.moving_right = False
        self.direction = direction
        self.vel_y = 0
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # Idle = 0
        self.update_time = pygame.time.get_ticks()
        self.explode = False

        # load all images for the objects
        animation_types = ["Fixed", "Animated"]

        for animation in animation_types:
            # reset temporary list of images
            temp_list = []

            # count number of files in folder
            num_of_frames = len(os.listdir(f"images/{self.action_type}/{animation}"))
            for i in range(num_of_frames):
                img = pygame.image.load(f"images/{self.action_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()

    def main_event(self):
        if player.alive:
            if player.jump:
                if random.randint(1, 10) == 1:
                    happy_word = random.choice(happy)
                    if len(word) >= 1:
                        word.clear()
                    else:
                        word.append(happy_word)

            if len(word) == 1:
                draw_text(f"".join(map(str, word)), font, BLACK, SCREEN_WIDTH + 30, 510)

                self.timer += 1
                if self.timer >= 50:
                    self.timer = 0
                    word.clear()

    def event(self):
        if player.alive:
            for dancing_girl in dancing_girl_group:
                if self.action_type != "dancing_girl":
                    dancing_girl.kill()

            if self.action_type == "fist_bump":
                self.update_action(1)
                if self.frame_index == len(self.animation_list[self.action]) - 1:
                    self.timer += 1
                if self.timer > 50:
                    self.kill()
                    heart = CollectAction("heart", SCREEN_WIDTH + 150, 650, 1, 1, 1,)
                    heart_group.add(heart)
                    self.timer = 0
                    dancing_girl = CollectAction("dancing_girl", SCREEN_WIDTH + 150, 650, 0.5, 1, 1,)
                    dancing_girl_group.add(dancing_girl)

            if self.action_type == "heart":
                self.update_action(1)
                draw_text(f"YOU COLLECTED: ", font, BLACK, SCREEN_WIDTH + 50, 510)
                draw_text(f"A HEALTCARE BOX!", font, BLACK, SCREEN_WIDTH + 50, 540)
                self.timer += 1
                if self.timer > 200:
                    self.kill()
                    dancing_girl = CollectAction("dancing_girl", SCREEN_WIDTH + 150, 650, 0.5, 1, 1,)
                    dancing_girl_group.add(dancing_girl)

            if self.action_type == "pool_grenade":
                self.update_action(0)
                draw_text(f"YOU COLLECTED: ", font, BLACK, SCREEN_WIDTH + 50, 510)
                draw_text(f"A GRENADE BOX!", font, BLACK, SCREEN_WIDTH + 50, 540)
                self.timer += 1
                if self.timer > 200:
                    self.kill()
                    explosion = Explosion(self.rect.centerx, self.rect.centery - 75, 2)
                    explosion_group.add(explosion)
                    grenade_fx.play()
                    dancing_girl = CollectAction("dancing_girl", SCREEN_WIDTH + 150, 650, 0.5, 1, 1,)
                    dancing_girl_group.add(dancing_girl)

            if self.action_type == "cowboy":
                self.update_action(0)
                draw_text(f"YOU COLLECTED: ", font, BLACK, SCREEN_WIDTH + 30, 510)
                draw_text(f"AN AMMUNITION BOX!", font, BLACK, SCREEN_WIDTH + 30, 540)
                self.timer += 1
                if self.timer > 200:
                    shoot_fx.play()
                    explosion = Explosion(self.rect.centerx + 100, self.rect.centery, 1)
                    explosion_group.add(explosion)
                    explosion = Explosion(self.rect.centerx - 105, self.rect.centery, 1)
                    explosion_group.add(explosion)
                    self.kill()
                    dancing_girl = CollectAction("dancing_girl", SCREEN_WIDTH + 150, 650, 0.5, 1, 1,)
                    dancing_girl_group.add(dancing_girl)

            if self.action_type == "exploding_box":
                if player.box_explode:
                    self.update_action(1)
                    if self.frame_index == 8:
                        self.explode = True
                if self.explode:
                    draw_text(f"something is hidden in", font, BLACK, SCREEN_WIDTH + 30, 510)
                    draw_text(f"the pile of boards.", font, BLACK, SCREEN_WIDTH + 30, 540)
                    draw_text(f"It looks shiny!", font, BLACK, SCREEN_WIDTH + 30, 570)
                    self.timer += 1
                    if self.timer > 400:
                        player.box_explode = False
                        self.kill()
                        dancing_girl = CollectAction("dancing_girl", SCREEN_WIDTH + 150, 650, 0.5, 1, 1,)
                        dancing_girl_group.add(dancing_girl)
                        self.timer = 0
                        self.explode = False

                else:
                    draw_text(f"What is that?", font, BLACK, SCREEN_WIDTH + 30, 510)
                    draw_text(f"Can I make it explode?", font, BLACK, SCREEN_WIDTH + 30, 540)
                    self.timer += 1
                    if self.timer > 200:
                        self.kill()
                        dancing_girl = CollectAction("dancing_girl", SCREEN_WIDTH + 150, 650, 0.5, 1, 1,)
                        dancing_girl_group.add(dancing_girl)

            if self.action_type == "exit_key":
                key_collected = 1
                self.update_action(1)
                draw_text(f"YOU COLLECTED: ", font, BLACK, SCREEN_WIDTH + 50, 510)
                draw_text(f"AN EXIT KEY!", font, BLACK, SCREEN_WIDTH + 50, 540)
                self.timer += 1
                if self.timer > 200:
                    self.kill()
                    dancing_girl = CollectAction("dancing_girl", SCREEN_WIDTH + 150, 650, 0.5, 1, 1,)
                    dancing_girl_group.add(dancing_girl)

            if self.action_type == "dancing_girl":
                self.update_action(1)

    def update_animation(self):
        if self.explode:
            self.frame_index = 8
        # update animation
        if self.action_type == "exploding_box" and self.frame_index == 1:
            ANIMATION_COOLDOWN = 1000
        else:
            ANIMATION_COOLDOWN = 100
        if self.action_type == "exploding_box" and self.frame_index == 2:
            player.exploding_box_ready = True
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has past since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset back to start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action_type == "exploding_box":
                if self.action == 1:
                    self.frame_index = len(self.animation_list[self.action]) - 1

            if self.action_type == "fist_bump":
                if self.action == 1:
                    self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades, money, sniper_ammo):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.turtle_collision = False
        self.turtle_shell = False
        self.pick_up = False
        self.release = False
        self.sniper_ammo = sniper_ammo
        self.sniper_rifle = False
        self.scale = scale
        self.camera = True
        self.box_explode = False
        self.key_collected = 0
        self.exploding_box_ready = False
        self.zoom_in = False
        self.aim_up = False
        self.aim_down = False
        self.money = money
        self.start_sniper_ammo = sniper_ammo
        self.start_ammo = ammo
        self.shoot_cooldown = 0
        self.remove_enemy_cooldown = 0
        self.grenades = grenades
        self.health = 100
        self.timer = 1000
        self.max_health = self.health
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.climb = False
        self.climb_up = False
        self.climb_down = False
        self.in_air = True
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # Idle = 0
        self.update_time = pygame.time.get_ticks()

        # ai specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
        self.idling = False
        self.idling_counter = 1

        # load all images for the players
        animation_types = ["Idle", "Run", "Jump", "Death", "Shoot", "Hide", "Aim_up", "Aim_down"]

        for animation in animation_types:
            # reset temporary list of images
            temp_list = []

            # count number of files in folder
            num_of_frames = len(os.listdir(f"images/{self.char_type}/{animation}"))
            for i in range(num_of_frames):
                img = pygame.image.load(f"images/{self.char_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()

        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self._layer = self.rect.bottom
        self.pseudo_rect = self.rect.inflate(140, 140)

    def update(self):
        self.update_animation()
        self.check_alive()

        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        if self.remove_enemy_cooldown > 0:
            self.remove_enemy_cooldown -= 1
        if self.char_type == "player":
            if self.camera:
                camera_object = pygame.transform.scale(self.image, (self.width, self.height))
                rect_camera = camera_object.get_rect()
                rect_camera.center = (SCREEN_WIDTH + 150, 100)
                screen.blit(pygame.transform.flip(camera_object, self.flip, False), rect_camera)

    def move(self, moving_left, moving_right):
        # reset movement variables
        screen_scroll = 0
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
            self.move_counter *= 1
            player.camera = True

        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
            self.move_counter *= 1
            player.camera = True

        # jump
        if self.jump is True and self.in_air is False:
            jump_fx.play()
            happy_word = random.choice(happy)
            self.vel_y = -12
            for turtle in turtle_group:
                if turtle.rolling:
                    self.turtle_collision = True
            self.jump = False
            self.in_air = True

        # apply gravity
        self.vel_y += GRAVITY
        if self.vel_y > 30:
            self.vel_y = 0
        dy += self.vel_y

        for tile in world.obstacle_list:
            # check collision in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                self.move_counter = 0
                # if the ai has hit a wall, then make it turn around
                if self.char_type == "enemy":
                    self.direction *= -1

            # check collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.char_type == "enemy":
                    for turtle in turtle_group:
                        if self.turtle_collision:
                            self.health = 0
                # check if below the ground i.e jumping
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground i.e falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # check for collision with bomb_box
        if self.char_type == "player":
            for bomb_box in bomb_box_group:
                bomb_box.collide = False
                if pygame.sprite.spritecollide(self, bomb_box_group, False):
                    bomb_box.collide = True

        # check for collision with water
        if pygame.sprite.spritecollide(self, water_group, False):
            self.health = 0
            die_fx.play()

        # check for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            if player.key_collected > 0:
                level_complete = True
            else:
                draw_text(f"The door is locked,", font, BLACK, SCREEN_WIDTH + 30, 510)
                draw_text(f"you must find a key!", font, BLACK, SCREEN_WIDTH + 30, 540)

        # check if fallen of the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0

        # check if going of the edges of the screen
        if self.char_type == "player":
            if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
                dx = 0
        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        # update scroll based on player position
        if self.char_type == "player":
            if (self.rect.right > SCREEN_WIDTH - SCROLL_THRESH and bg_scroll < (
                    world.level_lenght * TILE_SIZE) - SCREEN_WIDTH) \
                    or (self.rect.left < SCROLL_THRESH and bg_scroll > abs(dx)):
                self.rect.x -= dx
                screen_scroll = -dx

        return screen_scroll, level_complete

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.9 * self.rect.size[0] * self.direction), self.rect.centery - 8,
                            self.direction)
            bullet_group.add(bullet)
            # reduce ammo

            self.ammo -= 1
            shoot_fx.play()

    def sniper_shoot(self):
        if self.shoot_cooldown == 0 and self.sniper_ammo > 0 and self.sniper_rifle:
            self.shoot_cooldown = 20

            # reduce ammo
            self.sniper_ammo -= 1
            shoot_fx.play()

    def grab_turtle(self):
        dy = 0
        if self.pick_up:
            turtle = Animal("turtle", self.rect.centerx + (0.7 * self.rect.size[0] * self.direction), self.rect.centery - 20, 0.9, 1, 5)
            turtle_group.add(turtle)
            turtle.update_action(2)
            turtle.shell = True
            turtle.rolling = False
            for tile in world.obstacle_list:
                # check collision in x direction
                if self.char_type == "player":
                    dx = player.speed * self.direction
                    if tile[1].colliderect(turtle.rect.x + dx, turtle.rect.y, turtle.width, turtle.height):
                        self.speed *= -1

    def ai(self):
        if self.alive and player.alive:
            if self.char_type == "enemy":
                for turtle in turtle_group:
                    if pygame.sprite.collide_rect(enemy, turtle):
                        self.jump = True

                if pygame.sprite.spritecollide(self, aim_group, False):
                    self.camera = False
                    camera_object = pygame.transform.scale(self.image, (self.width * zoom, self.height * zoom))
                    rect_camera = camera_object.get_rect()
                    rect_camera.center = (SCREEN_WIDTH + 150, 100)
                    screen.blit(pygame.transform.flip(camera_object, self.flip, False), rect_camera)
                    self.update_action(0)
                    self.idling = True
                    player.zoom_in = True

                    if aim.target_hit:
                        self.health -= 50
                        player.sniper_rifle = False


                        

                else:
                    player.zoom_in = False
                    self.camera = True

            if not self.idling and random.randint(1, 200) == 1 and self.in_air is False:
                self.update_action(0)
                self.idling = True
                self.idling_counter = 50

            # check if the ai is near the player
            if self.vision.colliderect(
                    player.rect) and self.rect.bottom == player.rect.bottom and self.move_counter != 1:
                # stop running and face the player
                self.update_action(0)
                self.shoot()
            else:
                if not self.idling:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    self.move(ai_moving_left, ai_moving_right)
                    self.update_action(1)  # 1 = run
                    self.move_counter += 1

                    # update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)
                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False
        else:
            if pygame.sprite.spritecollide(self, aim_group, False):
                camera_object = pygame.transform.scale(self.image, (self.width * zoom, self.height * zoom))
                rect_camera = camera_object.get_rect()
                rect_camera.center = (SCREEN_WIDTH + 150, 100)
                screen.blit(pygame.transform.flip(camera_object, self.flip, False), rect_camera)

        # scroll
        self.rect.x += screen_scroll

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has past since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset back to start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)
            if self.char_type == "enemy":
                if self.remove_enemy_cooldown == 0:
                    self.remove_enemy_cooldown = 100
                if 10 > self.remove_enemy_cooldown > 0:
                    self.kill()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


class World:
    def __init__(self):
        self.obstacle_list = []

    def process_data(self, data):
        self.level_lenght = len(data[0])
        # iterate through each value in level data file
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    if 0 <= tile <= 8:
                        self.obstacle_list.append(tile_data)
                    elif 9 <= tile <= 10:  # create water
                        water = Water(img, x * TILE_SIZE, y * TILE_SIZE)
                        water_group.add(water)
                    elif 11 <= tile <= 14:  # create decoration
                        decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_group.add(decoration)
                    elif tile == 15:  # create ladder
                        ladder = Ladder(img, x * TILE_SIZE, y * TILE_SIZE)
                        ladder_group.add(ladder)
                    elif tile == 16:  # create player
                        player = Soldier("player", x * TILE_SIZE, y * TILE_SIZE, 0.1, 5, 20, 5, 0, 0)
                        health_bar = Health_Bar(SCREEN_WIDTH + 20, 250, player.health, player.health)
                        dancing_girl = CollectAction("dancing_girl", SCREEN_WIDTH + 150, 650, 0.5, 1, 1,)
                        dancing_girl_group.add(dancing_girl)
                    elif tile == 17:  # create enemy
                        enemy = Soldier("enemy", x * TILE_SIZE, y * TILE_SIZE, 1.5, 5, 20, 0, 0, 0,)
                        enemy_group.add(enemy)
                    elif tile == 18:  # create ball
                        ball = MovingObjects("ball", x * TILE_SIZE, y * TILE_SIZE + 21, 2, 1, 5)
                        ball_group.add(ball)
                    elif tile == 19:  # create ammo box
                        item_box = ItemBox("Ammo", x * TILE_SIZE, y * TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 20:  # grenade box
                        item_box = ItemBox("Grenade", x * TILE_SIZE, y * TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 21:  # create health box
                        item_box = ItemBox("Health", x * TILE_SIZE, y * TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 22:  # create exit
                        exit = Exit(img, x * TILE_SIZE, y * TILE_SIZE)
                        exit_group.add(exit)

                    elif tile == 23:  # create money
                        money = Money("money", x * TILE_SIZE, y * TILE_SIZE, 0.2)
                        if not in_game:
                            money_group.add(money)
                    elif tile == 24:  # moneybag
                        money_bag = MoneyBag(x * TILE_SIZE, y * TILE_SIZE, 0.15)
                        if not in_game:
                            money_bag_group.add(money_bag)
                    elif tile == 25:  # sniper_rifle
                        sniper_rifle = Sniper_Rifle(x * TILE_SIZE, y * TILE_SIZE, 1)
                        if not in_game:
                            sniper_rifle_group.add(sniper_rifle)
                    elif tile == 26:  # turtle
                        turtle = Animal("turtle", x * TILE_SIZE, y * TILE_SIZE, 0.9, 1, 5)
                        turtle_group.add(turtle)
                    elif tile == 27:  # bomb_box
                        bomb_box = BombBox(img, x * TILE_SIZE, y * TILE_SIZE)
                        bomb_box_group.add(bomb_box)
                    elif tile == 28:  # key
                        key = Key("key", x * TILE_SIZE, y * TILE_SIZE, 0.3)
                        key_group.add(key)

        return player, health_bar, dancing_girl

    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += screen_scroll
            screen.blit(tile[0], tile[1])


class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, x, y, ):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll


class Ladder(pygame.sprite.Sprite):
    def __init__(self, img, x, y, ):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - 1 - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll
        dx = 0
        if self.rect.colliderect(player.rect.x + dx, player.rect.y, player.width, player.height):
            dx = (player.rect.x - player.speed) - self.rect.x
            if - 10 < dx < 10:
                if pygame.sprite.spritecollide(player, ladder_group, False):
                    player.vel_y = 0
                if pygame.sprite.spritecollide(player, ladder_group, False) and player.climb_down:
                    player.vel_y = 1
                if pygame.sprite.spritecollide(player, ladder_group, False) and player.climb_up:
                    player.jump = False
                    player.vel_y = -1


class Water(pygame.sprite.Sprite):
    def __init__(self, img, x, y, ):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll


class Exit(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll


class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y, ):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type
        self.image = item_boxes[self.item_type]

        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        # scroll
        self.rect.x += screen_scroll
        # check if the player picked up a box
        if pygame.sprite.collide_rect(self, player):
            # check what kind of box it was
            if self.item_type == "Health":
                collect_fx.play()
                fist_bump = CollectAction("fist_bump", SCREEN_WIDTH + 150, 650, 0.25, 1, 1,)
                fist_bump_group.add(fist_bump)
                punch_fx.play()
                if player.health >= player.max_health - 25:
                    player.health = player.max_health
                else:
                    player.health += 25
            elif self.item_type == "Ammo":
                collect_fx.play()
                cowboy = CollectAction("cowboy", SCREEN_WIDTH + 150, 650, 0.25, 1, 1,)
                cowboy_group.add(cowboy)
                player.ammo += 15
            elif self.item_type == "Grenade":
                collect_fx.play()
                pool_grenade = CollectAction("pool_grenade", SCREEN_WIDTH + 150, 650, 0.25, 1, 1,)
                pool_grenade_group.add(pool_grenade)
                player.grenades += 3

            # delete the box
            self.kill()


class MoneyBag(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(f"images/moneybag.png").convert_alpha()
        self.image = img
        self.image = pygame.transform.scale(self.image,
                                            (int(img.get_width() * scale), (int(self.image.get_height() * scale))))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

        self.start_x = x
        self.reset()

    def reset(self):
        self.rect.x = self.start_x

    def update(self):
        self.rect.x += screen_scroll
        if pygame.sprite.collide_rect(self, player):
            player.money += 50
            coinbag_fx.play()
            self.kill()


class Sniper_Rifle(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(f"images/sniper_rifle.png").convert_alpha()
        self.image = img
        self.image = pygame.transform.scale(self.image,
                                            (int(img.get_width() * scale), (int(self.image.get_height() * scale))))
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

        self.start_x = x
        self.reset()

    def reset(self):
        self.rect.x = self.start_x

    def update(self):
        self.rect.x += screen_scroll
        if pygame.sprite.collide_rect(self, player):
            collect_fx.play()
            player.sniper_rifle = True
            player.sniper_ammo += 5
            self.kill()


class Health_Bar:
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health

    def draw(self, health):
        # update with new health
        self.health = health
        # calculate health ratio
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(screen, RED, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 150 * ratio, 20))


class Aim(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.direction = 1
        self.speed = 2
        self.flip = False
        self.zoom_in = False
        self.target_locked = False
        self.target_hit = False
        self.vel_y = 1
        self.aiming = False
        self.aim_up = False
        self.aim_down = False
        self.image = aim_img
        self.image = pygame.transform.scale(self.image,
                                            (int(img.get_width() * scale), (int(self.image.get_height() * scale))))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0

        self.camera_object = pygame.transform.scale(self.image, (self.width + zoom, self.height + zoom))
        self.rect_camera = self.camera_object.get_rect()
        self.camera_center_x = SCREEN_WIDTH + 150 + zoom
        self.camera_center_y = 100 - zoom
        self.rect_camera.center = (self.camera_center_x, self.camera_center_y)

    def update(self):
        dx = 0
        dy = 0

        # check if aim has gone of the screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        if self.rect.bottom > SCREEN_HEIGHT or self.rect.top < 0:
            self.kill()

        # check for collision with level
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                self.kill()

    def move_aim(self):
        if self.target_hit:
            player.camera = False
        if player.sniper_rifle:

            # reset movement variables
            dx = 0
            dy = 0
            # assign movement variables if moving left or right
            if aim_moving_left:
                dx = -self.speed * self.direction
                self.rect.x += dx
                if player.direction == 1:
                    if self.rect.centerx < player.rect.centerx - 5:
                        player.direction = -1
                        player.flip = True

            if aim_moving_right:
                dx = self.speed * self.direction
                self.rect.x += dx
                if player.direction == -1:
                    if self.rect.centerx > player.rect.centerx + 5:
                        player.direction = 1
                        player.flip = False

            if aim_moving_up:
                dy = self.vel_y * -self.speed
                self.rect.y += dy
                if self.rect.centery < player.rect.centery - 20:
                    player.aim_up = True
                    player.aim_down = False

            if aim_moving_down:
                dy = self.vel_y * self.speed
                self.rect.y += dy
                if self.rect.centery > player.rect.centery + 20:
                    player.aim_down = True
                    player.aim_up = False

            if (player.rect.centery - 20) < self.rect.centery < (player.rect.centery + 20):
                player.aim_down = False
                player.aim_up = False

            if pygame.sprite.spritecollide(self, enemy_group, False):
                player.camera = False

                if camera_aim_moving_left:
                    dx = -self.speed * self.direction

                if camera_aim_moving_right:
                    dx = self.speed * self.direction

                if camera_aim_moving_up:
                    dy = self.vel_y * -self.speed

                if camera_aim_moving_down:
                    dy = self.vel_y * self.speed

                self.rect_camera.x += dx
                self.rect_camera.y += dy
                screen.blit(pygame.transform.flip(self.camera_object, self.flip, False), self.rect_camera)

                if 1377 - (20 * zoom) < self.rect_camera.x < 1377 + (20 * zoom) and \
                        99 - (30 * zoom) < self.rect_camera.y < 99 + (5 * zoom) and player.sniper_ammo > 0:
                    self.target_locked = True
                else:
                    self.target_locked = False

                if self.target_locked and sniper_shoot:
                    if player.sniper_ammo > 0:
                        blood = Blood(self.rect_camera.centerx, self.rect_camera.centery, 0.5)
                        blood_group.add(blood)
                        shoot_fx.play()
                        self.target_hit = True

                else:
                    self.target_hit = False




class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, ):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.timer = 0
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        # move bullet
        self.rect.x += (self.direction * self.speed) + screen_scroll

        # check if bullets has gone of the screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

        # check for collision with level
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                self.kill()

        # check collision with characters
        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 5
                self.kill()
                die_fx.play()
                if random.randint(1, 5) == 1:
                    angry_word = random.choice(angry)
                    if len(word) >= 1:
                        word.clear()
                    else:
                        word.append(angry_word)
        if len(word) == 1:
            draw_text(f"".join(map(str, word)), font, BLACK, SCREEN_WIDTH + 30, 510)
            self.timer += 1
            if self.timer >= 50:
                self.timer = 0
                word.clear()

        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= 25
                    self.kill()


class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, ):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.vel_y = -5
        self.speed = 7
        self.image = grenade_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = direction

    def update(self):
        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        # update grenade
        self.rect.x += dx + screen_scroll
        self.rect.y += dy

        # check for collision with level
        for tile in world.obstacle_list:
            # check collision with walls
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                self.direction *= -1
                dx = self.direction * self.speed
            # check collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.speed = 0

                # check if below the ground i.e thrown up
                if self.vel_y < 0:
                    self.vel_y = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground i.e falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom

        # update grenade position
        self.rect.x += dx
        self.rect.y += dy

        # countdown timer
        self.timer -= 1
        if self.timer <= 0:
            grenade_fx.play()
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y, 2)
            explosion_group.add(explosion)
            # do damage to anyone that is nearby
            if abs(self.rect.centerx - player.rect.centerx) < TILE_SIZE * 2 and \
                    abs(self.rect.centery - player.rect.centery) < TILE_SIZE * 2:
                player.health -= 50
            for enemy in enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 2 and \
                        abs(self.rect.centery - enemy.rect.centery) < TILE_SIZE * 2:
                    enemy.health -= 50


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        for num in range(6):
            img = pygame.image.load(f"images/explosion/exp{num}.gif").convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
            self.images.append(img)
            self.frame_index = 0
            self.image = self.images[self.frame_index]

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        # scroll
        self.rect.x += screen_scroll
        EXPLOSION_SPEED = 4
        # update explosion animation
        self.counter += 1
        if self.counter >= EXPLOSION_SPEED:
            self.counter = 0
            self.frame_index += 1
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]


class Animal(pygame.sprite.Sprite):
    def __init__(self, animal_type, x, y, scale, direction, speed):
        pygame.sprite.Sprite.__init__(self)
        self.animal_type = animal_type
        self.speed = speed
        self.shell = False
        self.jump = False
        self.in_air = True
        self.turtle_collision = False
        self.timer = 200
        self.rolling = False
        self.moving_right = False
        self.flip = False
        self.direction = direction
        self.vel_y = 0
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # Idle = 0
        self.update_time = pygame.time.get_ticks()
        self.move_counter = 0
        self.idling = False
        self.idling_counter = 1
        self.vision = pygame.Rect(0, 0, 100, 20)

        # load all images for the objects
        animation_types = ["Idle", "Run", "Shell"]

        for animation in animation_types:
            # reset temporary list of images
            temp_list = []

            # count number of files in folder
            num_of_frames = len(os.listdir(f"images/{self.animal_type}/{animation}"))
            for i in range(num_of_frames):
                img = pygame.image.load(f"images/{self.animal_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()

    def animal_move(self, animal_moving_left, animal_moving_right):
        if not self.rolling:
            # reset movement variables
            dx = 0
            dy = 0

            # jump
            if self.jump is True and self.in_air is False:
                self.vel_y = -15
                self.turtle_collision = True
                self.jump = False
                self.in_air = True

            for index1, turtle1 in enumerate(turtle_group):
                for index2, turtle2 in enumerate(turtle_group):
                    if index1 != index2:
                        if pygame.sprite.collide_rect(turtle1, turtle2):
                            if self.shell:
                                self.jump = True

            # assign movement variables if moving left or right
            if animal_moving_left:
                dx = -self.speed
                self.flip = True
                self.direction = -1
                self.move_counter *= 1

            if animal_moving_right:
                dx = self.speed
                self.flip = False
                self.direction = 1
                self.move_counter *= 1

            if player.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height) and player.in_air and not player.pick_up:
                player.release = False
                self.shell = True
                self.update_action(2)
                self.speed = 0
                if not player.pick_up:
                    player.vel_y = -12
                player.jump = False
                player.in_air = True

            if player.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height) and player.vel_y >= 1:
                if not player.pick_up:
                    player.vel_y = 0
                player.in_air = True
                self.shell = True

            # apply gravity
            self.vel_y += GRAVITY
            if self.vel_y > 30:
                self.vel_y = 0
            dy += self.vel_y

            if self.shell and not self.rolling:
                self.timer -= 1
            if self.timer <= 0:
                self.shell = False
                self.update_action(0)
                self.idling = True
                self.speed = 5
                self.timer = 200

            for tile in world.obstacle_list:
                # check collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                    self.direction *= -1
                    if player.pick_up:
                        player.speed *= -1
                        self.speed *= -1

                # check collision in y direction
                if player.pick_up:
                    if self.in_air:
                        if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                            player.pick_up = False
                            player.release = True
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.turtle_collision:
                        self.kill()

                    if player.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height) and player.release:
                        if player.direction > 0 and self.direction > 0 or player.direction < 0 and self.direction > 0:
                            self.moving_right = False
                        else:
                            self.moving_right = True

                        player.release = False
                        self.shell = False

                    if self.vel_y >= 0:
                        self.vel_y = 0
                        dy = tile[1].top - self.rect.bottom
                        self.in_air = False

            if player.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height) and self.shell and not player.in_air and not player.release:
                if grab:
                    player.pick_up = True

                if not grab:
                    if player.direction > 0:
                        self.moving_right = True
                    else:
                        self.moving_right = False
                    self.speed = 5
                    self.rolling = True

            # check if fallen of the map
            if self.rect.bottom > SCREEN_HEIGHT:
                self.kill()

            print(player.vel_y)

            # update rectangle position
            self.rect.y += dy
            self.rect.x += dx

    def move_shell(self):
        dx = 0
        player.speed = 5
        self.speed = 5
        if self.rolling:
            if self.moving_right:
                self.direction = 1
                self.flip = True

            elif not self.moving_right:
                self.direction = -1
                self.flip = False

            self.update_action(2)
            dx = self.speed * self.direction

        self.rect.x += dx

    def animal_collide(self):
        if self.rolling:
            dx = 0
            dx = self.speed * self.direction

            if player.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height) and player.in_air and self.shell:
                player.release = False
                self.shell = True
                self.rolling = False
                self.update_action(2)
                bounce_fx.play()
                self.speed = 0
                player.vel_y = -12
                player.jump = False
                player.in_air = True

            if player.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height) and self.shell and not player.in_air:
                dx = 0
                if player.direction > 0 and self.direction > 0 or player.direction < 0 and self.direction > 0:
                    self.moving_right = False
                    if not player.release:
                        player.speed *= -1
                else:
                    self.moving_right = True
                    if not player.release:
                        player.speed *= -1

            for tile in world.obstacle_list:
                # check collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    bounce_fx.play()

                    if self.direction > 0:
                        self.moving_right = False
                    else:
                        self.moving_right = True

            self.rect.x += dx

    def ai(self):
        dx = 0
        if not self.shell:
            if not self.idling and random.randint(1, 200) == 1:
                self.update_action(0)
                self.idling = True
                self.idling_counter = 50

            elif not self.idling:
                if self.direction == 1:
                    ai_moving_right = True
                else:
                    ai_moving_right = False
                ai_moving_left = not ai_moving_right
                self.animal_move(ai_moving_left, ai_moving_right)
                self.update_action(1)  # 1 = run
                self.move_counter += 1

            if self.move_counter > TILE_SIZE:
                self.direction *= -1
                self.move_counter *= -1
            else:
                self.idling_counter -= 1
                if self.idling_counter <= 0:
                    self.idling = False

            if player.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                if not player.pick_up:
                    player.health -= 0.1

        # scroll
        self.rect.x += screen_scroll

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has past since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset back to start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        dx = 0
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
        if player.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
            if player.pick_up and self.shell:
                self.kill()


class BombBox(pygame.sprite.Sprite):
    def __init__(self, img, x, y, ):
        pygame.sprite.Sprite.__init__(self)
        self.collide = False
        self.explode = False
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll
        if pygame.sprite.spritecollide(player, bomb_box_group, False):
            if len(exploding_box_group) == 0:
                self.collide = True
                exploding_box = CollectAction("exploding_box", SCREEN_WIDTH + 150, 650, 0.25, 1, 1,)
                exploding_box_group.add(exploding_box)

            if len(exploding_box_group) > 1:
                self.collide = False

        for bullet in bullet_group:
            if pygame.sprite.spritecollide(bullet, bomb_box_group, False):
                player.box_explode = True

                if len(exploding_box_group) == 0:
                    exploding_box = CollectAction("exploding_box", SCREEN_WIDTH + 150, 650, 0.25, 1, 1,)
                    exploding_box_group.add(exploding_box)
                    exploding_box.update_action(1)

        if player.exploding_box_ready:
            explosion = Explosion(self.rect.centerx, self.rect.centery, 4)
            explosion_group.add(explosion)
            grenade_fx.play()
            self.kill()
            broken_box = BrokenBox(self.rect.centerx, self.rect.centery, 1.2)
            broken_box_group.add(broken_box)
            player.exploding_box_ready = False


class BrokenBox(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(broken_box_img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += screen_scroll
        if pygame.sprite.spritecollide(player, broken_box_group, False) and not player.box_explode:
            self.kill()
            key = Key("key", self.rect.centerx, self.rect.centery, 0.3)
            key_group.add(key)


class Key(pygame.sprite.Sprite):
    def __init__(self, key_type, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.key_type = key_type
        self.key_collected = 0
        self.vel_y = 0
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # Idle = 0
        self.update_time = pygame.time.get_ticks()

        # load all images for the objects
        animation_types = ["Fixed", "Animated"]

        for animation in animation_types:
            # reset temporary list of images
            temp_list = []

            # count number of files in folder
            num_of_frames = len(os.listdir(f"images/{self.key_type}/{animation}"))
            for i in range(num_of_frames):
                img = pygame.image.load(f"images/{self.key_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        self.update_animation()
        self.rect.x += screen_scroll

        if pygame.sprite.spritecollide(player, key_group, False):
            if not player.box_explode:
                player.key_collected = 1
                collect_fx.play()
                exit_key = CollectAction("exit_key", SCREEN_WIDTH + 150, 650, 0.5, 1, 1,)
                exit_key_group.add(exit_key)
                exit_key.update_action(1)
                exit_key.action_type = "exit_key"
                self.kill()

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has past since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out then reset back to start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


class ScreenFade():
    def __init__(self, direction, colour, speed):
        self.direction = direction
        self.colour = colour
        self.speed = speed
        self.fade_counter = 0

    def fade(self):
        fade_complete = False
        self.fade_counter += self.speed
        if self.direction == 1:  # whole screen fade
            pygame.draw.rect(screen, self.colour, (0 - self.fade_counter, 0, (SCREEN_WIDTH + SIDE_MARGIN) // 2, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.colour,
                             ((SCREEN_WIDTH + SIDE_MARGIN) // 2 + self.fade_counter, 0, (SCREEN_WIDTH + SIDE_MARGIN), SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.colour, (0, 0 - self.fade_counter, (SCREEN_WIDTH + SIDE_MARGIN), SCREEN_HEIGHT // 2))
            pygame.draw.rect(screen, self.colour,
                             (0, SCREEN_HEIGHT // 2 + self.fade_counter, (SCREEN_WIDTH + SIDE_MARGIN), SCREEN_HEIGHT))
        if self.direction == 2:  # vertical screen fade down
            pygame.draw.rect(screen, self.colour, (0, 0, SCREEN_WIDTH, 0 + self.fade_counter))
        if self.fade_counter >= SCREEN_WIDTH:
            fade_complete = True

        return fade_complete


# create screen fades
intro_fade = ScreenFade(1, BLACK, 4)
death_fade = ScreenFade(2, PINK, 4)

# create buttons
start_button = button.Button((SCREEN_WIDTH + SIDE_MARGIN) // 2 - 130, SCREEN_HEIGHT // 2 - 150, start_img, 1)
exit_button = button.Button((SCREEN_WIDTH + SIDE_MARGIN) // 2 - 110, SCREEN_HEIGHT // 2 + 50, exit_img, 1)
restart_button = button.Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, restart_img, 2)

# create sprite groups

blood_group = pygame.sprite.Group()
aim_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()
turtle_group = pygame.sprite.Group()
money_group = pygame.sprite.Group()
money_bag_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
sniper_bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
ladder_group = pygame.sprite.Group()
fist_bump_group = pygame.sprite.Group()
heart_group = pygame.sprite.Group()
pool_grenade_group = pygame.sprite.Group()
cowboy_group = pygame.sprite.Group()
dancing_girl_group = pygame.sprite.Group()
bomb_box_group = pygame.sprite.Group()
broken_box_group = pygame.sprite.Group()
exploding_box_group = pygame.sprite.Group()
key_group = pygame.sprite.Group()
exit_key_group = pygame.sprite.Group()
sniper_rifle_group = pygame.sprite.Group()

# create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)

# load in level data and create world
with open(f"level{level}_data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)

world = World()
player, health_bar, dancing_girl = world.process_data(world_data)

run = True
while run:
    clock.tick(FPS)
    if not start_game:
        # main menu
        screen.fill(BG_COLOR)
        # add buttons
        if start_button.draw(screen):
            start_game = True
            start_intro = True
        if exit_button.draw(screen):
            run = False
    else:
        # update background
        draw_bg()
        # draw world map
        world.draw()

        for enemy in enemy_group:
            enemy.update()
            enemy.draw()

        for turtle in turtle_group:
            turtle.animal_move(animal_moving_left, animal_moving_right)
            turtle.move_shell()
            turtle.animal_collide()
            turtle.update()
            turtle.draw()

        for ball in ball_group:
            ball.not_moving()
            ball.move_ball()
            ball.ball_collide()
            ball.update()
            ball.draw()

        for money in money_group:
            if not player.alive:
                money.reset()

        for sniper in sniper_rifle_group:
            if not player.alive:
                sniper.reset()

        for money_bag in money_bag_group:
            if not player.alive:
                money_bag.reset()

        # update and draw groups
        money_group.update()
        money_bag_group.update()
        bullet_group.update()
        sniper_bullet_group.update()
        grenade_group.update()
        item_box_group.update()
        water_group.update()
        decoration_group.update()
        exit_group.update()
        ladder_group.update()
        bomb_box_group.update()
        broken_box_group.update()
        key_group.update()
        sniper_rifle_group.update()

        key_group.draw(screen)
        bullet_group.draw(screen)
        sniper_bullet_group.draw(screen)
        grenade_group.draw(screen)
        item_box_group.draw(screen)
        water_group.draw(screen)
        decoration_group.draw(screen)
        exit_group.draw(screen)
        money_group.draw(screen)
        money_bag_group.draw(screen)
        ladder_group.draw(screen)
        bomb_box_group.draw(screen)
        broken_box_group.draw(screen)
        sniper_rifle_group.draw(screen)

        draw_tile_panels()
        # show player health
        health_bar.draw(player.health)
        # show ammo
        draw_text(f"AMMO: ", font, BLACK, SCREEN_WIDTH + 20, 300)
        for x in range(player.ammo):
            draw_text(f"{player.ammo}", font, BLACK, SCREEN_WIDTH + 100, 300)
        # show grenade
        draw_text(f"GRENADES: ", font, BLACK, SCREEN_WIDTH + 20, 335)
        for x in range(player.grenades):
            draw_text(f"{player.grenades}", font, BLACK, SCREEN_WIDTH + 145, 335)
        draw_text(f"MONEY: ", font, BLACK, SCREEN_WIDTH + 20, 405)
        for x in range(player.money):
            draw_text(f"{player.money}", font, BLACK, SCREEN_WIDTH + 105, 405)
        # show grenade
        draw_text(f"SNIPER, AMMO: ", font, BLACK, SCREEN_WIDTH + 20, 370)
        for x in range(player.sniper_ammo):
            draw_text(f"{player.sniper_ammo}", font, BLACK, SCREEN_WIDTH + 180, 370)
        # show key
        draw_text(f"KEY: ", font, BLACK, SCREEN_WIDTH + 20, 440)
        for x in range(player.key_collected):
            draw_text(f"{player.key_collected}", font, BLACK, SCREEN_WIDTH + 75, 440)

        player.update()
        player.draw()
        for enemy in enemy_group:
            enemy.ai()

        for turtle in turtle_group:
            turtle.ai()

        for aim in aim_group:
            aim.move_aim()

        aim_group.update()
        aim_group.draw(screen)

        blood_group.update()
        blood_group.draw(screen)

        for dancing_girl in dancing_girl_group:
            dancing_girl.main_event()
            dancing_girl.event()
            dancing_girl_group.update()
            dancing_girl_group.draw(screen)

        for fist_bump in fist_bump_group:
            fist_bump.event()
            fist_bump_group.update()
            fist_bump_group.draw(screen)

        for heart in heart_group:
            heart.event()
            heart_group.update()
            heart_group.draw(screen)

        for exit_key in exit_key_group:
            exit_key.event()
            exit_key_group.update()
            exit_key_group.draw(screen)

        for pool_grenade in pool_grenade_group:
            pool_grenade.event()
            pool_grenade_group.update()
            pool_grenade_group.draw(screen)

        for cowboy in cowboy_group:
            cowboy.event()
            cowboy_group.update()
            cowboy_group.draw(screen)

        for exploding_box in exploding_box_group:
            exploding_box.event()
            exploding_box_group.update()
            exploding_box_group.draw(screen)

        explosion_group.update()
        explosion_group.draw(screen)

        # show intro
        if start_intro:
            if intro_fade.fade():
                start_intro = False
                intro_fade.fade_counter = 0

        # update player actions
        if player.alive:
            # shoot bullets
            if shoot:
                player.shoot()
            elif sniper_shoot:
                player.sniper_shoot()
            elif grab:
                player.grab_turtle()

            # throw grenade
            if grenade and grenade_thrown is False and player.grenades > 0:
                grenade = Grenade(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction),
                                  player.rect.top, player.direction)
                grenade_group.add(grenade)

                # reduce grenades
                player.grenades -= 1
                grenade_thrown = True

            elif player_aim:
                aim = Aim(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction),
                          player.rect.top, 1)
                aim_group.add(aim)

            elif player.in_air:
                player.update_action(2)  # 2 = Jump
            elif moving_left or moving_right:
                player.update_action(1)  # 1 = Run
            else:
                player.update_action(0)  # 0 = Idle
            if player.aim_up:
                player.update_action(6)
            if player.aim_down:
                player.update_action(7)

            screen_scroll, level_complete = player.move(moving_left, moving_right)
            bg_scroll -= screen_scroll
            # check if player has completed the level
            if level_complete:
                health_left = player.health
                in_game = False

                start_intro = True
                level += 1
                bg_scroll = 0
                ammo_left = player.ammo
                sniper_ammo_left = player.sniper_ammo
                money_collect = player.money
                grenades_left = player.grenades
                if player.sniper_rifle:
                    sniper_rifle = 1
                world_data = reset_level()
                if level <= MAX_LEVELS:
                    # load in level data and create world
                    with open(f"level{level}_data.csv", newline="") as csvfile:
                        reader = csv.reader(csvfile, delimiter=",")
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)

                    world = World()
                    player, health_bar, dancing_girl = world.process_data(world_data)
                    player.money = money_collect
                    player.grenades = grenades_left
                    player.ammo = ammo_left
                    player.sniper_ammo = sniper_ammo_left
                    player.health -= (player.health - health_left)
                    if sniper_rifle > 0:
                        player.sniper_rifle = True

        else:

            in_game = True
            money_collect = player.money
            sniper_ammo_left = player.sniper_ammo
            screen_scroll = 0
            if death_fade.fade():
                if restart_button.draw(screen):
                    death_fade.fade_counter = 0
                    start_intro = True
                    bg_scroll = 0
                    if player.sniper_rifle:
                        sniper_rifle = 1

                    world_data = reset_level()
                    # load in level data and create world
                    with open(f"level{level}_data.csv", newline="") as csvfile:
                        reader = csv.reader(csvfile, delimiter=",")
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()

                    player, health_bar, dancing_girl = world.process_data(world_data)
                    player.money = money_collect
                    player.sniper_ammo = sniper_ammo_left
                    if sniper_rifle > 0:
                        player.sniper_rifle = True

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False
        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_b:
                grenade = True
            if event.key == pygame.K_KP_PLUS:
                if zoom < 3:
                    zoom += 0.1
            if event.key == pygame.K_KP_MINUS:
                if zoom > 1:
                    zoom -= 0.1
                elif zoom == 1:
                    zoom = 1
            if event.key == pygame.K_z:
                if enemy.health > 0:
                    if not player.in_air and player.sniper_rifle:
                        player_aim = True
                        zoom = 1
            if event.key == pygame.K_v:
                grab = True

            if event.key == pygame.K_UP and player.alive:
                player.jump = True
                player.climb_up = True
            if event.key == pygame.K_DOWN:
                player.climb_down = True
            if event.key == pygame.K_ESCAPE:
                run = False

        # keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP and player.alive:
                player.jump = False
                player.climb_up = False
            if event.key == pygame.K_DOWN:
                player.climb_down = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_b:
                grenade = False
                grenade_thrown = False
            if event.key == pygame.K_z:

                player_aim = False
                player.aim_up = False
                player.aim_down = False
                for aim in aim_group:
                    aim.kill()
                if player.sniper_ammo > 0:
                    player.sniper_rifle = True
            if event.key == pygame.K_v:
                grab = False
                player.pick_up = False
                player.release = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z] and keys[pygame.K_RIGHT]:
            shoot = False
            player_aim = False
            if player.camera:
                aim_moving_right = True
            else:
                camera_aim_moving_right = True
            moving_right = False
        else:
            aim_moving_right = False
            camera_aim_moving_right = False
        if keys[pygame.K_z] and keys[pygame.K_LEFT]:
            shoot = False
            if player.camera:
                aim_moving_left = True
                camera_aim_moving_left = False
            else:
                camera_aim_moving_left = True
            player_aim = False
            moving_left = False
        else:
            aim_moving_left = False
            camera_aim_moving_left = False
        if keys[pygame.K_z] and keys[pygame.K_UP]:
            shoot = False
            player.jump = False
            if player.camera:
                aim_moving_up = True
                camera_aim_moving_up = False
            else:
                camera_aim_moving_up = True
            player_aim = False
            player.jump = False
        else:
            aim_moving_up = False
            camera_aim_moving_up = False
        if keys[pygame.K_z] and keys[pygame.K_DOWN]:
            shoot = False
            if player.camera:
                aim_moving_down = True
                camera_aim_moving_down = False
            else:
                camera_aim_moving_down = True
            player_aim = False
            player.climb_down = False
        else:
            aim_moving_down = False
            camera_aim_moving_down = False
        if keys[pygame.K_z] and keys[pygame.K_SPACE]:
            sniper_shoot = True
            shoot = False
        else:
            sniper_shoot = False

    pygame.display.update()

pygame.quit()
