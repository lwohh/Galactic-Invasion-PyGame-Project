import pygame, random, sys

# Intialize the pygame
pygame.init()

# create the screen, width/height
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


#define game variables
rows = 5
cols = 5

# background image
background = pygame.image.load("background.jpg")

# Title Caption and Icon
pygame.display.set_caption("Group 9 Project")
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)

#define colors
red = (255,0,0)
green = (0,255,0)


# enemy class
class Enemy(pygame.sprite.Sprite):
    # initializes the class, and info for all new objects
    def __init__(self):
        super().__init__()
        self.speed = 8
        self.name = "enemy"
        self.damage = 5
        self.image = pygame.image.load("nuclear-bomb.png")
        # using list for coords
        self.pos = [random.randint(0, 736), random.randint(50, 150)]
        self.rect = self.image.get_rect(center=(self.pos[0], self.pos[1]))
        self.directions = [True, False]
        self.dir = random.choice(self.directions)


    def create_aliens(self,enemy):
        for row in range(rows):
            for item in range (cols):
              enemy = Enemy(item * 100)


    # enemy movement method
    def update(self):
        # moves enemy left and right depending on random direction from self.dir
        if not self.dir:
            self.rect.x -= self.speed
        if self.dir:
            self.rect.x += self.speed

        # keeps enemy within bounds
        if self.rect.x < 0 and not self.dir:
            self.rect.y += 40
            self.dir = True
        if self.rect.x > 736 and self.dir:
            self.rect.y += 40
            self.dir = False


# bullet class
class bullet(pygame.sprite.Sprite):
    # initializes bullet class and variables for all bullet objects
    def __init__(self):
        super().__init__()
        self.speed = 8
        self.name = "bullet"
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.state = "ready"

    # bullet movement method
    def update(self):
        if self.state == "fire":
            self.rect.y -= self.speed


# player class
class player(pygame.sprite.Sprite):
    # same as other two classes
    def __init__(self,health):
        super().__init__()
        self.speed = 10
        self.name = "player"
        self.image = pygame.image.load("plane.png")
        self.rect = self.image.get_rect(center=(370, 480))
        self.health_start = health
        self.health_remaining = health

    # player movement method
    def update(self):
        # checks if movement keys have been pressed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed

        # keeps player in bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 736:
            self.rect.x = 736

        #draw health bar
        pygame.draw.rect(screen,red,(self.rect.x,(self.rect.bottom + 10),self.rect.width,15))
        if self.health_remaining > 0:
            pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))
            
# sprite groups from classes, enemy, player, bullet
sprite_group = pygame.sprite.Group()
sprite_group.add(Enemy())

player_group = pygame.sprite.Group()
player = player(3)
player_group.add(player)

bullet_group = pygame.sprite.Group()
bullet1 = bullet()

# timed events, enemy spawning, faster spawning
# creates a custom event
spawn_event = pygame.event.custom_type()
# how long between event triggers (in milliseconds, starts at 3.5 seconds)
spawn_timer = 3500
# sets the timer for this event
pygame.time.set_timer(spawn_event, spawn_timer)

# creates a new custom event
faster_timer_event = pygame.event.custom_type()
# time between event triggers (10 seconds)
timer_event_timer = 10000
# sets the timer for this event
pygame.time.set_timer(faster_timer_event, timer_event_timer)

# Game Loop
running = True
while running:
    # background screen color update
    screen.fill((128, 128, 128))
    # Background Image
    screen.blit(background, (0, 0))

    keys = pygame.key.get_pressed()
    # every event gets logged below and you loop through each event, like keystrokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)

        # every 3.5 seconds a new enemy spawns on the event trigger
        if event.type == spawn_event:
            sprite_group.add(Enemy())
            # debug code, will only go off when event is triggered
            print("new enemy")

        # every 10 seconds the spawn timer will go down 0.2 seconds or 200 milliseconds
        if event.type == faster_timer_event:
            spawn_timer -= 200
            # debug code
            print("spawning faster")

        # checks for spacebar pressed, if bullet is ready to be fired, will add bullet1 to the bullet group
        if keys[pygame.K_SPACE] and bullet1.state == "ready":
            bullet1.state = "fire"
            bullet_group.add(bullet1)
            bullet1.rect.x = player.rect.x + 16
            bullet1.rect.y = player.rect.y

    # when the bullet goes out of bounds, state changes to ready and can be fired again
    if bullet1.rect.y < -32:
        bullet1.state = "ready"

        # checks if anything in bullet group collides with enemies, if so the enemy is deleted from the group and the bullet remains
    pygame.sprite.groupcollide(bullet_group, sprite_group, False, True)

    # .draw is the same as blitting, draws everything in the groups to the screen and activates the update() methods on each group
    sprite_group.draw(screen)
    sprite_group.update()
    bullet_group.draw(screen)
    bullet_group.update()
    player_group.draw(screen)
    player_group.update()

    # refreshes the screen and keeps the fps at 60
    pygame.display.flip()
    clock.tick(60)
