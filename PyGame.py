import pygame, random, sys, math

# Intialize the pygame
pygame.init()

score = 0
paused = False

# create the screen, width/height
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Font for Pause Screen
font = pygame.font.Font(None, 30)

# background image
# this image is too big pixel wise
background = pygame.image.load("background.jpg")

# Title Caption and Icon
pygame.display.set_caption("Group 9 Project")
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("plane.png")
playerRect = playerImg.get_rect(center=(370, 480))
# to get player to starting point, coordinates below


# Enemy
enemyImg = pygame.image.load("nuclear-bomb.png")
enemylist = []
directions = [True, False]
enemyDir = random.choice(directions)
# this makes the enemy appear randomly within these parameters
for i in range(5):
    enemyX = random.randint(0, 736)
    enemyY = random.randint(50, 150)
    enemyRect = enemyImg.get_rect(center=(enemyX, enemyY))
    # false = left, true = right
    directions = [True, False]
    enemyDir = random.choice(directions)
    enemylist.append(enemyRect)

# Bullet/Missle
bulletImg = pygame.image.load("bullet.png")
bulletRect = bulletImg.get_rect(center=(0, 700))
bulletX = 0
bulletY = 480
# Fire - bullet is moving, Ready - you cant see bullet on screen
bullet_state = "ready"


def get_enemy_coords():
    global enemyRect, enemyX, enemyY, enemyDir
    enemyDir = random.choice(directions)
    enemyRect.x = enemyX
    enemyRect.y = enemyY

def move_entities():
    global playerRect, bulletRect, enemyRect, enemyDir

    if keys[pygame.K_d]:
        playerRect = playerRect.move(8, 0)
    if keys[pygame.K_a]:
        playerRect = playerRect.move(-8, 0)

    if not enemyDir:
        enemyRect = enemyRect.move(-5, 0)
    if enemyDir:
        enemyRect = enemyRect.move(5, 0)
    if enemyRect.x < 0 and not enemyDir:
        enemyRect.y += 40
        enemyDir = True
    if enemyRect.x > 736 and enemyDir:
        enemyRect.y += 40
        enemyDir = False

def fire_bullet():
    global bulletRect
    bulletRect = bulletRect.move(0, -8)


def is_Collision():
    global enemyX
    global enemyY
    global bulletX
    global bulletY

    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY + bulletY, 2)))
    if distance < 130:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    # background screen color update
    screen.fill((128,128,128))

    # Background Image
    screen.blit(background, (0,0))
    screen.blit(bulletImg, bulletRect.topleft)
    screen.blit(playerImg, playerRect.topleft)
    screen.blit(enemyImg, enemyRect.topleft)

    keys = pygame.key.get_pressed()
    # every event gets logged below and you loop through each event, like keystrokes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_p:
                paused = True
            if event.key == pygame.K_g and paused:
                paused = False

    if not paused:

        if keys[pygame.K_SPACE] and bullet_state == "ready":
            bulletRect.x = playerRect.x
            bulletRect.y = playerRect.y
            bullet_state = "fire"

        if bullet_state == "fire":
           fire_bullet()
        if bulletRect.y < -32:
           bullet_state = "ready"
           bulletRect.y = 700
    # settings boundaries for the plane
        if playerRect.x <= 0:
            playerRect.x = 0
        # subtracting the pixels of the plane from 800. (64 pixel plane)
        if playerRect.x >= 736:
            playerRect.x = 736

        if bulletRect.x <= 0:
            bulletRect.x = 0
        if bulletRect.x >= 750:
            bulletRect.x = 750

        if enemyRect.colliderect(bulletRect):
             get_enemy_coords()

    # Collision check
        for enemyRect in enemylist:
             if enemyRect.colliderect(bulletRect) and bullet_state == "fire":
                 bulletRect.y = 700
                 bullet_state = "ready"
                 enemyRect.y = random.randint(50, 150)
                 enemyRect.x = random.randint(0, 736)
                 score += 1
                 print("Score:", score)

    # calling the plane/enemy ONTO the screen
        move_entities()

 # Press P to Pause Text to screen
        text_surface = font.render("Press P to Pause", True, (255,255,255))
        text_rect = text_surface.get_rect(topleft=(10,10))
        screen.blit(text_surface, text_rect)


        pygame.display.flip()
        clock.tick(60)
    else:
        screen.fill((0,0,0))

        instructions_text = font.render("Game Instructions", True, (255, 255, 255))
        instructions_rect = instructions_text.get_rect(centerx=screen.get_width() // 2, centery=100)
        screen.blit(instructions_text, instructions_rect)

        instruction1_text = font.render("You are a pilot with a main goal to destroy the bombs before the hit the ground.", True, (255,255,255))
        instruction1_rect = instruction1_text.get_rect(centerx=screen.get_width() // 2, centery=200)
        screen.blit(instruction1_text, instruction1_rect)

        instruction2_text = font.render("Use \"A\" to move left and \"D\" to move right.", True, (255,255,255))
        instruction2_rect = instruction2_text.get_rect(centerx=screen.get_width() // 2, centery=250)
        screen.blit(instruction2_text, instruction2_rect)

        instruction3_text = font.render("Press the \"Space Bar\" to fire bullets at the bombs", True, (255, 255, 255))
        instruction3_rect = instruction3_text.get_rect(centerx=screen.get_width() // 2, centery=300)
        screen.blit(instruction3_text, instruction3_rect)

        instruction4_text = font.render("If you collide with a bomb, the game is over and you lose.", True, (255, 255, 255))
        instruction4_rect = instruction4_text.get_rect(centerx=screen.get_width() // 2, centery=350)
        screen.blit(instruction4_text, instruction4_rect)

        return_text = font.render("Press \"G\" to return back to the game.", True, (255,255,255))
        return_rect = return_text.get_rect(centerx=screen.get_width() // 2, centery=450)
        screen.blit(return_text, return_rect)

        pygame.display.flip()

pygame.quit()
sys.exit()



