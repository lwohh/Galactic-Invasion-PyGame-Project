import pygame,random,sys

# Intialize the pygame
pygame.init()

# create the screen, width/height
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

# background image
  # this image is too big pixel wise
background = pygame.image.load("background.jpg")

# Title Caption and Icon
pygame.display.set_caption("Group 9 Project")
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 8
        self.name = "enemy"
        self.damage = 5
        self.image = pygame.image.load("nuclear-bomb.png")
        # using list for coords
        self.pos = [random.randint(0,736), random.randint(50,150)]
        self.rect = self.image.get_rect(center=(self.pos[0],self.pos[1]))
        self.directions = [True, False]
        self.dir = random.choice(self.directions)
    
    def update(self):
        if not self.dir:
            self.rect.x -= self.speed
        if self.dir:
            self.rect.x += self.speed
        if self.rect.x < 0 and not self.dir:
            self.rect.y += 40
            self.dir = True
        if self.rect.x > 736 and self.dir:
            self.rect.y += 40
            self.dir = False

class bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 8
        self.name = "bullet"
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.state = "ready"
    
    def update(self):
        if self.state == "fire":
            self.rect.y -= self.speed

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.name = "player"
        self.image = pygame.image.load("plane.png")
        self.rect = self.image.get_rect(center=(370,480))
    
    def update(self):
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 736:
            self.rect.x = 736

# sprite groups from classes, enemy, player, bullet
sprite_group = pygame.sprite.Group()
sprite_group.add(Enemy())

player_group = pygame.sprite.Group()
player = player()
player_group.add(player)

bullet_group = pygame.sprite.Group()
bullet1 = bullet()


# timed events, enemy spawning, faster spawning, 
spawn_event = pygame.event.custom_type()
spawn_timer = 3500
pygame.time.set_timer(spawn_event, spawn_timer)

faster_timer_event = pygame.event.custom_type()
timer_event_timer = 10000
pygame.time.set_timer(faster_timer_event, timer_event_timer)

# Game Loop
running = True
while running:
    # background screen color update
    screen.fill((128, 128, 128))
    # Background Image
    screen.blit(background,(0,0))    

    keys = pygame.key.get_pressed()
    # every event gets logged below and you loop through each event, like keystrokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
        if event.type == spawn_event:
            sprite_group.add(Enemy())
            print("new enemy")
        if event.type == faster_timer_event:
            spawn_timer -= 200
            print("spawning faster")
        if event.type == faster_enemy_event:
            Enemy.speed += 25
        if keys[pygame.K_SPACE] and bullet1.state == "ready":
            bullet1.state = "fire"
            bullet_group.add(bullet1)
            bullet1.rect.x = player.rect.x + 16
            bullet1.rect.y = player.rect.y
            
    if bullet1.rect.y < -32:
        bullet1.state = "ready"    
    
    pygame.sprite.groupcollide(bullet_group, sprite_group, False, True)

    sprite_group.draw(screen)
    sprite_group.update()
    bullet_group.draw(screen)
    bullet_group.update()
    player_group.draw(screen)
    player_group.update()
        # calling the plane/enemy ONTO the screen
    pygame.display.flip()
    clock.tick(60)