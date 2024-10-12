import pygame 
import random
import sys

# Intialize the pygame
pygame.init()

# create the screen, width/height
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

# background image
  # this image is too big pixel wise
background = pygame.image.load("assets\\background.jpg")

# Title Caption and Icon
pygame.display.set_caption("Group 9 Project")
icon = pygame.image.load("assets\\game_icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("assets\\plane.png")
playerRect = playerImg.get_rect(center=(370,480))
# to get player to starting point, coordinates below

# Enemy
enemyImg = pygame.image.load("assets\\nuclear-bomb.png")
# this makes the enemy appear randomly within these parameters
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyRect = enemyImg.get_rect(center=(enemyX, enemyY))
# false = left, true = right
directions = [True, False]
enemyDir = random.choice(directions)

# Bullet/Missle
bulletImg = pygame.image.load("assets\\bullet.png")
bulletRect = bulletImg.get_rect(center=(0,700))

# Ready - you cant see bullet on screen
# Fire - bullet is moving
bullet_state = "ready"

def get_enemy_coords():
    global enemyRect, enemyX, enemyY, enemyDir
    enemyDir = random.choice(directions)
    enemyRect.x = enemyX
    enemyRect.y = enemyY

def move_entities():
    global playerRect, bulletRect, enemyRect, enemyDir

    if keys[pygame.K_d]:
        playerRect = playerRect.move(5,0)
    if keys[pygame.K_a]:
        playerRect = playerRect.move(-5,0)
    
    if not enemyDir:
        enemyRect = enemyRect.move(-5,0)
    if enemyDir:
        enemyRect = enemyRect.move(5,0)
    if enemyRect.x < 0 and not enemyDir:
        enemyRect.y += 40
        enemyDir = True
    if enemyRect.x > 736 and enemyDir:
        enemyRect.y += 40
        enemyDir = False

def fire_bullet():
    global bulletRect
    bulletRect = bulletRect.move(0,-5) 

# Game Loop
running = True
while running:
    # background screen color update
    screen.fill((128, 128, 128))
    # Background Image
    screen.blit(background,(0,0))
    screen.blit(bulletImg,bulletRect.topleft)
    screen.blit(playerImg,playerRect.topleft)
    screen.blit(enemyImg, enemyRect.topleft)

    keys = pygame.key.get_pressed()
    # every event gets logged below and you loop through each event, like keystrokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)
        if keys[pygame.K_SPACE] and bullet_state == "ready":
            bulletRect.x = playerRect.x
            bulletRect.y = playerRect.y
            bullet_state = "fire"

    if bullet_state == "fire":
        fire_bullet()
    if bulletRect.y < -32:
        bullet_state = "ready"
        bulletRect.y = 700
    #settings boundaries for the plane
    if playerRect.x <= 0:
        playerRect.x = 0
        #subtracting the pixels of the plane from 800. (64 pixel plane)
    if playerRect.x >= 736:
        playerRect.x = 736
    
    if bulletRect.x <= 0:
        bulletRect.x = 0
    if bulletRect.x >= 750:
        bulletRect.x = 750
    
    if enemyRect.colliderect(bulletRect):
        get_enemy_coords()

    # calling the plane/enemy ONTO the screen
    move_entities()
    pygame.display.update()
    clock.tick(60)