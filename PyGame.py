import pygame
import math
# import this so you can make the enemy appear randomly
import random

# Intialize the pygame
pygame.init()

# create the screen, width/height
screen = pygame.display.set_mode((800,600))

# background image
  # this image is too big pixel wise
background = pygame.image.load("C:\\Users\\canyon.white\\PycharmProjects\\group9pygame\\assets\\background.jpg")

# Title Caption and Icon
pygame.display.set_caption("Group 9 Project")
icon = pygame.image.load("C:\\Users\\canyon.white\\PycharmProjects\\group9pygame\\assets\\game_icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("C:\\Users\\canyon.white\\PycharmProjects\\group9pygame\\assets\\plane.png")
# to get player to starting point, coordinates below
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("C:\\Users\\canyon.white\\PycharmProjects\\group9pygame\\assets\\nuclear-bomb.png")
# this makes the enemy appear randomly within these parameters
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.1
enemyY_change = 40

# Bullet/Missle
bulletImg = pygame.image.load("C:\\Users\\canyon.white\\PycharmProjects\\group9pygame\\assets\\bullet.png")
# this makes the enemy appear randomly within these parameters
bulletX = 0
bulletY = 480
# X is zero since it only moves on the Y coordinate
bulletX_change = 0
bulletY_change = 0.4
# Ready - you cant see bullet on screen
# Fire - bullet is moving
bullet_state = "ready"


def player(x,y):
    #drawing the player (plane) onto the screen
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    #drawing the enemy (bomb) onto the screen
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16,y + 10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))

clock = pygame.time.Clock()
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
            running = False

        # if keystroke is pressed check whether its right or left. Keydown is pressing any button on keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                  bulletX = playerX
                  fire_bullet(bulletX,bulletY)
        # KEYUP is releasing a key. I'm just checking for the left and right arrow keys
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # so plane stops when you lift up the key
                playerX_change = 0
        if keys[pygame.K_ESCAPE]:
            running = False

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    playerX += playerX_change

    #settings boundaries for the plane
    if playerX <= 0:
        playerX = 0
        #subtracting the pixels of the plane from 800. (64 pixel plane)
    elif playerX >= 736:
        playerX = 736

    # setting boundaries for the enemy bomb. Enemy bomb pic also 64 pixels
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.1
        enemyY += enemyY_change

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    # calling the plane/enemy ONTO the screen
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
    clock.tick()