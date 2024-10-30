import pygame,random,sys

# Intialize the pygame
pygame.init()


# create the screen, width/height
screen = pygame.display.set_mode((800,600))


# Title Caption and Icon
pygame.display.set_caption("Group 9 Project: Galactic Invasion")
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)


# main menu
def main_menu():
    clock = pygame.time.Clock()
    run = True
    pygame.mixer.music.pause()
    while run:
        screen_center = screen.get_width() // 2
        screen.fill((0,0,0))
        title_font = pygame.font.Font("monogram.ttf", 60)

        title_text = title_font.render("Group 9 Project: Galactic Invasion", False, (255,255,255))
        title_rect = title_text.get_rect(centerx=screen_center, centery=100)

        start_img = pygame.image.load("UI - start.png").convert_alpha()
        quit_img = pygame.image.load("UI - quit.png").convert_alpha()
        options_img = pygame.image.load("UI - options.png").convert_alpha()

        class Button():
            def __init__(self, x, y, image, scale):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False

            
            def draw(self):
                # draw button on screen
                screen.blit(self.image, (self.rect.x, self.rect.y))

                pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        self.clicked = True
                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False


        # button instances
        start_button = Button(315, 275, start_img, 1.5)
        start_button.draw()
        if start_button.clicked == True:
            game()

        quit_button = Button(315, 425, quit_img, 1.5)
        quit_button.draw()
        if quit_button.clicked == True:
            sys.exit(0)
        
        options_button = Button(315, 350, options_img, 1.5)
        options_button.draw()
        if options_button.clicked == True:
            paused()

        screen.blit(title_text, title_rect.topleft)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)
            if keys[pygame.K_g]:
                pygame.mixer.music.unpause()
                game()
            if keys[pygame.K_i]:
                paused()
                

        pygame.display.flip()
        clock.tick(60)


# pause menu
def paused():
    clock = pygame.time.Clock()
    keep_run = True
    pygame.mixer.music.pause()
    while keep_run:

        screen_center = screen.get_width() // 2
        screen.fill((0,0,0))
        pause_font = pygame.font.Font("monogram.ttf", 30)

        back_img = pygame.image.load("UI - back.png").convert_alpha()


        class Button():
            def __init__(self, x, y, image, scale):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False

            
            def draw(self):
                # draw button on screen
                screen.blit(self.image, (self.rect.x, self.rect.y))

                pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        self.clicked = True
                    if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

        back_button = Button(20, 550, back_img, 1.0)
        back_button.draw()
        if back_button.clicked == True:
            keep_run = False

        instructions_one = pause_font.render("Game Instructions", False, (255,255,255))
        one_rect = instructions_one.get_rect(centerx=screen_center, centery=50)

        instructions_two = pause_font.render("You are a pilot with the main goal of", False, (255,255,255))
        two_rect = instructions_two.get_rect(centerx=screen_center, centery=85)

        instructions_six = pause_font.render("destroying the bombs before they hit the ground!", False, (255,255,255))
        six_rect = instructions_six.get_rect(centerx=screen_center, centery=115)

        key_text = pause_font.render("Keybinds:", False, (255,255,255))
        key_rect = key_text.get_rect(centerx=screen_center, centery=255)

        instructions_three = pause_font.render("\"A\" or \"LEFT\": Move Left | \"D\" or \"RIGHT\": Move Right", False, (255,255,255))
        three_rect = instructions_three.get_rect(centerx=screen_center, centery=290)

        instructions_four = pause_font.render("\"Spacebar\": Fire Bullets", False, (255,255,255))
        four_rect = instructions_four.get_rect(centerx=screen_center, centery=320)

        instructions_five = pause_font.render("If you collide with a bomb, the game is over and you lose.", False, (255,255,255))
        five_rect = instructions_five.get_rect(centerx=screen_center, centery=145)

        instructions_seven = pause_font.render("\"ESC\": Return to Main Menu", False, (255,255,255))
        seven_rect = instructions_seven.get_rect(centerx=screen_center, centery=350)

        instructions_eight = pause_font.render("Difficulty increases gradually per level.", False, (255,255,255))
        eight_rect = instructions_eight.get_rect(centerx=screen_center, centery=460)

        instructions_nine = pause_font.render("Level will increase in 20 score intervals.", False, (255,255,255))
        nine_rect = instructions_nine.get_rect(centerx=screen_center, centery=490)

        boss_instructions = pause_font.render("Bosses will spawn once at levels 20, 40, 60, etc.", False, (255,255,255))
        boss_rect = boss_instructions.get_rect(centerx=screen_center, centery=520)

        screen.blit(instructions_one, one_rect.topleft)
        screen.blit(instructions_two, two_rect.topleft)
        screen.blit(instructions_three, three_rect.topleft)
        screen.blit(instructions_four, four_rect.topleft)
        screen.blit(instructions_five, five_rect.topleft)
        screen.blit(instructions_six, six_rect.topleft)
        screen.blit(key_text, key_rect.topleft)
        screen.blit(instructions_seven, seven_rect.topleft)
        screen.blit(instructions_eight, eight_rect.topleft)
        screen.blit(instructions_nine, nine_rect.topleft)
        screen.blit(boss_instructions, boss_rect.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
                
        pygame.display.flip()
        clock.tick(60)


# Game Loop
def game():
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
            self.pos = [random.randint(0,736), random.randint(25,100)]
            self.rect = self.image.get_rect(center=(self.pos[0],self.pos[1]))
            self.directions = [True, False]
            self.dir = random.choice(self.directions)
            self.jump = 40
    
        # enemy movement method
        def update(self):
            # moves enemy left and right depending on random direction from self.dir
            if not self.dir:
                self.rect.x -= self.speed
            if self.dir:
                self.rect.x += self.speed
        
            # keeps enemy within bounds 
            if self.rect.x < 0 and not self.dir:
                self.rect.y += self.jump
                self.dir = True
            if self.rect.x > 736 and self.dir:
                self.rect.y += self.jump
                self.dir = False
            if self.rect.y > 600:
                sys.exit(0)
            
            match level:
                case 1:
                    self.speed = 8
                case 2:
                    self.speed = 10
                case 3:
                    self.speed = 12
                case 4:
                    self.speed = 14
            print(self.speed)

    # bullet class
    class bullet(pygame.sprite.Sprite):
        # initializes bullet class and variables for all bullet objects
        def __init__(self):
            super().__init__()
            self.speed = 10
            self.name = "bullet"
            self.x = 0
            self.y = 0
            self.image = pygame.image.load("bullet.png")
            self.rect = self.image.get_rect(center=(self.x,self.y))
            self.state = "ready"
    
        # bullet movement method
        def update(self):
            if self.state == "fire":
                self.rect.y -= self.speed

            if level == 2:
                self.speed = 12
            elif level == 3:
                self.speed = 15

    # player class 
    class player(pygame.sprite.Sprite):
        # same as other two classes
        def __init__(self):
            super().__init__()
            self.speed = 10
            self.name = "player"
            self.image = pygame.image.load("plane.png")
            self.rect = self.image.get_rect(center=(370,520))

        # player movement method
        def update(self):
            # checks if movement keys have been pressed
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.rect.x -= self.speed

            # keeps player in bounds
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > 736:
                self.rect.x = 736

    # boss class
    class Boss(pygame.sprite.Sprite):
        # initializes the class, and info for all new objects
        def __init__(self):
            super().__init__()
            self.speed = 10
            self.name = "enemy"
            self.damage = 5
            self.image = pygame.image.load("bomb_boss.png")
            # using list for coords
            self.pos = [random.randint(0,736), random.randint(25,50)]
            self.rect = self.image.get_rect(center=(self.pos[0],self.pos[1]))
            self.directions = [True, False]
            self.dir = random.choice(self.directions)
            self.jump = 80
    
        # enemy movement method
        def update(self):
            # moves enemy left and right depending on random direction from self.dir
            if not self.dir:
                self.rect.x -= self.speed
            if self.dir:
                self.rect.x += self.speed
        
            # keeps enemy within bounds 
            if self.rect.x < 0 and not self.dir:
                self.rect.y += self.jump
                self.dir = True
            if self.rect.x > 736 and self.dir:
                self.rect.y += self.jump
                self.dir = False
            if self.rect.y > 600:
                sys.exit(0)
            
            match level:
                case 1:
                    self.speed = 8
                case 2:
                    self.speed = 10
                case 3:
                    self.speed = 12
                case 4:
                    self.speed = 14

    ss = spritesheet.spritesheet("ship.png")
    image = ss.image_at((0,0,16,24))
    images = []
    images = ss.images_at((0,0,16,24), (16,0,16,24), colorkey=(255,255,255))

    clock = pygame.time.Clock()

    # background image
    background = pygame.image.load("background_one.jpg")
    level_2_bg = pygame.image.load("Background_space.png")
    level_3_bg = pygame.image.load("bg_3.png")


    # sounds
    pygame.mixer.music.load("Mecha Collection.wav")
    pygame.mixer.music.set_volume(0.10)
    pygame.mixer.music.play(-1)

    new_level = pygame.mixer.Sound("new_level.wav")
    new_level.set_volume(0.25)

    enemy_defeat = pygame.mixer.Sound("enemy_defeat.wav")
    enemy_defeat.set_volume(0.10)


    # sprite groups from classes, enemy, player, bullet
    sprite_group = pygame.sprite.Group()
    sprite_group.add(Enemy())

    boss_group = pygame.sprite.Group()

    player_group = pygame.sprite.Group()
    player = player()
    player_group.add(player)

    bullet_group = pygame.sprite.Group()
    bullet1 = bullet()


    # UI
    score = 0
    score_font = pygame.font.Font("monogram.ttf", 48)
    score_render = score_font.render(f"Score: {str(score)}", False, (0,255,26))

    level = 1
    level_font = pygame.font.Font("monogram.ttf", 48)
    level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))


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

    boss_spawn = pygame.event.custom_type()
    spawner = 0
    boss_spawned = False
    boss_defeated = False


    running = True
    while running:
        # background screen color update
        screen.fill((128, 128, 128))
        # Background Image
        if level == 1:
            screen.blit(background,(-600,-200))
        if level == 2:
            screen.blit(level_2_bg, (0,0))
        if level == 3:
            screen.blit(level_3_bg, (0,0))
        screen.blit(score_render, (5,545))
        screen.blit(level_render, (650, 560))
        screen.blit(images, (0,0))

        keys = pygame.key.get_pressed()
        # every event gets logged below and you loop through each event, like keystrokes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                pygame.mixer.music.pause()
                running = False

            # every 3.5 seconds a new enemy spawns on the event trigger
            if event.type == spawn_event:
                sprite_group.add(Enemy())
                # debug code, will only go off when event is triggered
            
            if event.type == boss_spawn:
                boss_group.add(Boss())
                print("boss entered")
                boss_spawned = True
        
            if event.type == faster_timer_event:
                spawn_timer -= 150
                pygame.time.set_timer(spawn_event, spawn_timer)

            # checks for spacebar pressed, if bullet is ready to be fired, will add bullet1 to the bullet group
            if keys[pygame.K_SPACE] and bullet1.state == "ready":
                bullet1.state = "fire"
                bullet_group.add(bullet1)
                bullet1.rect.x = player.rect.x + 24
                bullet1.rect.y = player.rect.y

        # debug for spawning timer, makes sure it never goes below 0 (which would stop spawning enemies)
        if spawn_timer <= 500:
            spawn_timer == 500

        # when the bullet goes out of bounds, state changes to ready and can be fired again
        if bullet1.rect.y < -32:
            bullet1.state = "ready"    

        # checks if anything in bullet group collides with enemies, if so the enemy is deleted from the group and the bullet remains
        hit_list = pygame.sprite.groupcollide(bullet_group, sprite_group, True, True)

        if hit_list:
            print(hit_list)
            for i in range(len(hit_list)):
                score += 1
                score_render = score_font.render(f"Score: {str(score)}", False, (0,255,26))
                enemy_defeat.play()
                bullet1.state = "ready"
                hit_list.clear()
        
        hit_boss = pygame.sprite.groupcollide(bullet_group, boss_group, False, True)

        if hit_boss:
            for i in range(len(hit_boss)):
                score += 1
                score_render = score_font.render(f"Score: {str(score)}", False, (0,255,26))
                enemy_defeat.play()
                boss_spawned = False
                boss_defeated = True
                hit_boss.clear()

        if score % 20 == 0 and not boss_spawned and score != 0:
            spawner = 15
            pygame.time.set_timer(boss_spawn, spawner)
        if boss_spawned:
            spawner = 0
            pygame.time.set_timer(boss_spawn, spawner)
        if not boss_spawned:
            if boss_defeated:
                boss_defeated = False


        if score >= 20 and score < 40:
            level = 2
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 40 and score < 60:
            level = 3
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 60 and score < 80:
            level = 4
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))

        # .draw is the same as blitting, draws everything in the groups to the screen and activates the update() methods on each group
        sprite_group.draw(screen)
        sprite_group.update()
        bullet_group.draw(screen)
        bullet_group.update()
        player_group.draw(screen)
        player_group.update()
        boss_group.draw(screen)
        boss_group.update()

        # refreshes the screen and keeps the fps at 60
        pygame.display.flip()
        clock.tick(60)

main_menu()