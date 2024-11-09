import pygame,random,sys

# Intialize the pygame
pygame.init()


# create the screen, width/height
screen = pygame.display.set_mode((800,600))

 
# Title Caption and Icon
pygame.display.set_caption("Group 9 Project: Galactic Invasion")
icon = pygame.image.load("UI\\game_icon.png")
pygame.display.set_icon(icon)


# List containing top 10 scores for current game instance, resets once game is FULLY closed
high_scores = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


# Main Menu Function
def main_menu():
    # scene setup, basic variables and debug
    screen.fill((0,0,0))
    clock = pygame.time.Clock()
    pygame.mixer.music.pause()
    background = pygame.image.load("backgrounds\\background_two.png")
    background = pygame.transform.scale(background, (816 * 1.25, 480 * 1.25))


    # main loop
    run = True
    while run:
        # sets screen and finds screen center
        screen_center = screen.get_width() // 2
        screen.blit(background, (0,0))


        # font used for main menu text
        title_font = pygame.font.Font("fonts\\GravityRegular5.ttf", 28)


        # game title text
        title_text = title_font.render("Group 9 Project:", False, (255,255,255))
        title_rect = title_text.get_rect(centerx=screen_center, centery=100)

        title_text_2 = title_font.render("Galactic Invasion", False, (255,255,255))
        title_rect_2 = title_text_2.get_rect(centerx=screen_center, centery=150)


        # button images
        start_img = pygame.image.load("UI\\UI - start.png").convert_alpha()
        quit_img = pygame.image.load("UI\\UI - quit.png").convert_alpha()
        options_img = pygame.image.load("UI\\UI - options.png").convert_alpha()

        # button class
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
        if start_button.clicked:
            loading()

        quit_button = Button(315, 425, quit_img, 1.5)
        quit_button.draw()
        if quit_button.clicked:
            sys.exit(0)
        
        options_button = Button(315, 350, options_img, 1.5)
        options_button.draw()
        if options_button.clicked:
            paused()


        # blitting title text to screen
        screen.blit(title_text, title_rect.topleft)
        screen.blit(title_text_2, title_rect_2.topleft)


        # key and event queue for main menu
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)
                

        # refreshes screen, sets FPS
        pygame.display.flip()
        clock.tick(60)


# Options Menu Function
def paused():
    # scene setup, basic variables, debug
    screen.fill((0,0,0))
    clock = pygame.time.Clock()
    pygame.mixer.music.pause()
    background = pygame.image.load("backgrounds\\background_two.png")
    background = pygame.transform.scale(background, (816 * 1.25, 480 * 1.25))


    # main loop
    keep_run = True
    while keep_run:
        # sets background and finds screen center
        screen_center = screen.get_width() // 2
        screen.blit(background, (0,0))


        # options menu font
        pause_font = pygame.font.Font("fonts\\GravityRegular5.ttf", 13)


        # button image
        back_img = pygame.image.load("UI\\UI - back.png").convert_alpha()


        # button class
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


        # creating button
        back_button = Button(20, 550, back_img, 1.0)
        back_button.draw()
        if back_button.clicked == True:
            keep_run = False


        # options menu text
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


        # blitting options text to screen
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


        # event queue for options menu
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_TAB]:
                keep_run = False
                

        # refreshes screen and sets FPS
        pygame.display.flip()
        clock.tick(60)


# Main Game Function
def game():
    # setting global variables, classes, etc
    global high_scores
    screen.fill((0,0,0))
    clock = pygame.time.Clock()


    # UI
    score = 19
    score_font = pygame.font.Font("fonts\\GravityRegular5.ttf", 18)
    score_render = score_font.render(f"Score: {str(score)}", False, (0,255,26))

    level = 1
    level_font = pygame.font.Font("fonts\\GravityRegular5.ttf", 18)
    level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))


    # enemy class
    class Enemy(pygame.sprite.Sprite):
        # initializes the class, and info for all new objects
        def __init__(self):
            super().__init__()
            self.speed = 8
            self.name = "enemy"
            self.damage = 5
            self.images = [pygame.image.load("assets\\enemy.png"), pygame.image.load("assets\\enemy_2.png")]
            self.step_index = 0
            self.image = self.images[0]
            self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
            # using list for coords
            self.pos = [random.randint(0,736), random.randint(25,100)]
            self.rect = self.image.get_rect(center=(self.pos[0],self.pos[1]))
            self.directions = [True, False]
            self.dir = random.choice(self.directions)
            self.jump = 40

            self.explosion = [pygame.image.load("assets\\explosion_1.png"), pygame.image.load("assets\\explosion_2.png"),pygame.image.load("assets\\explosion_3.png"),pygame.image.load("assets\\explosion_4.png"),pygame.image.load("assets\\explosion_5.png")]
            self.explode_step_index = 0

            self.rect = self.image.get_rect(center=(self.pos[0],self.pos[1]))
            self.exploding = False
        # enemy movement method
        def update(self):
            # moves enemy left and right depending on random direction from self.dir
            if not self.dir and not self.exploding:
                self.rect.x -= self.speed
            if self.dir and not self.exploding:
                self.rect.x += self.speed
            
            # animating sprite
            self.image = self.images[self.step_index // 20]
            self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
            self.step_index += 1
            # resets animation index
            if self.step_index >= 40:
                self.step_index = 0

            if pygame.sprite.collide_rect(self, bullet1):
                self.exploding = True
                explosion_sound.play()
                bullet1.state = "ready"
                bullet1.rect.x = -50
                bullet1.rect.y = -50
                pygame.sprite.Sprite.kill(bullet1)


            if self.exploding:
                self.explode_step_index += 1

                if self.explode_step_index >= 40:
                    self.exploding = False
                    pygame.sprite.Sprite.add(self, hit_list)
                    pygame.sprite.Sprite.remove(self, sprite_group)
                    self.rect.x = -100
                    

                self.image = self.explosion[self.explode_step_index // 10]
                self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))


            # keeps enemy within bounds 
            if self.rect.x < 0 and not self.dir:
                self.rect.y += self.jump
                self.dir = True
            if self.rect.x > 736 and self.dir:
                self.rect.y += self.jump
                self.dir = False
            if self.rect.y > 600:
                for i in range(len(high_scores) - 1):
                    if score > high_scores[i]:
                        high_scores.insert(i, score)
                        high_scores.pop()
                        break
                leaderboard()
            
            match level:
                case 1:
                    self.speed = 8
                case 2:
                    self.speed = 8.5
                case 3:
                    self.speed = 9
                case 4:
                    self.speed = 9.5
                case 5:
                    self.speed = 10
                case 6:
                    self.speed = 10.5
                case 7:
                    self.speed = 11
                case 8:
                    self.speed = 11.5
                case 9:
                    self.speed = 12
                case 10:
                    self.speed = 12.5
                case 11:
                    self.speed = 13
                case 12:
                    self.speed = 13.5
                case _:
                    self.speed = 14


    # bullet class
    class bullet(pygame.sprite.Sprite):
        # initializes bullet class and variables for all bullet objects
        def __init__(self):
            super().__init__()
            self.speed = 10
            self.old_speed = 10
            self.name = "bullet"
            self.x = -50
            self.y = -50
            self.pwr_up = False
            self.images = [pygame.image.load("assets\\laser_f_1.png"), pygame.image.load("assets\\laser_f_2.png")]
            
            self.step_index = 0
            self.image = self.images[self.step_index]
            self.image = pygame.transform.scale(self.image, (5*2.75, 12*2.75))
            self.rect = self.image.get_rect(center=(self.x,self.y))
            self.state = "ready"
    
        # bullet movement method
        def update(self):
            if self.state == "fire":
                self.rect.y -= self.speed
                self.image = self.images[self.step_index // 15]
                self.step_index += 1
            
            if self.step_index >= 30:
                self.step_index = 0

            if self.rect.y <= -32:
                self.state = "ready"

            self.image = pygame.transform.scale(self.image, (5*2.75, 12*2.75))

            match level:
                case 2:
                    self.old_speed = 12
                case 3:
                    self.old_speed = 14
            
        def power_up(self):
            if not self.pwr_up:
                self.old_speed = self.speed
                self.speed += 5
                self.pwr_up = True
            

    # player class 
    class player(pygame.sprite.Sprite):
        # same as other two classes
        def __init__(self):
            super().__init__()
            self.speed = 10
            self.name = "player"
            self.left = [pygame.image.load("assets\\ship_f_1.png"), pygame.image.load("assets\\ship_f_11.png")]
            
            self.right = [pygame.image.load("assets\\ship_f_5.png"), pygame.image.load("assets\\ship_f_55.png")]
            
            self.idle = [pygame.image.load("assets\\ship_f_3.png"), pygame.image.load("assets\\ship_f_33.png")]

            self.step_index = 0
            self.image = self.idle[0]
            self.image = pygame.transform.scale(self.image, (16*2.5, 24*2.5))
            self.rect = self.image.get_rect(center=(370,520))
            self.pwr_up = False

        # player movement method
        def update(self):
            # checks if movement keys have been pressed
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.image = self.right[self.step_index // 15]

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.rect.x -= self.speed
                self.image = self.left[self.step_index // 15]

            if not keys[pygame.K_a] and not keys[pygame.K_d]:
                self.image = self.idle[self.step_index // 15]
            
            self.step_index += 1

            if self.step_index >= 30:
                self.step_index = 0

            self.image = pygame.transform.scale(self.image, (16*2.5, 24*2.5))
            # keeps player in bounds
            if self.rect.x < 0:
                self.rect.x = 0
            if self.rect.x > 736:
                self.rect.x = 736


        def power_up(self):
            if self.pwr_up == False:
                self.speed += 5
                self.pwr_up = True


    # boss class
    class Boss(pygame.sprite.Sprite):
        # initializes the class, and info for all new objects
        def __init__(self):
            super().__init__()
            self.speed = 10
            self.name = "enemy"
            self.damage = 5
            self.images = [pygame.image.load("assets\\boss_1.png"), pygame.image.load("assets\\boss_2.png")]
            self.step_index = 0
            self.image = self.images[0]
            self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
            # using list for coords

            self.explosion = [pygame.image.load("assets\\explosion_1.png"), pygame.image.load("assets\\explosion_2.png"),pygame.image.load("assets\\explosion_3.png"),pygame.image.load("assets\\explosion_4.png"),pygame.image.load("assets\\explosion_5.png")]
            self.explode_step_index = 0

            self.pos = [random.randint(0,736), random.randint(75,100)]
            self.rect = self.image.get_rect(center=(self.pos[0],self.pos[1]))
            self.directions = [True, False]
            self.dir = random.choice(self.directions)
            self.jump = 80
            self.exploding = False
    
        # enemy movement method
        def update(self):
            # moves enemy left and right depending on random direction from self.dir
            if not self.dir and not self.exploding:
                self.rect.x -= self.speed
            if self.dir and not self.exploding:
                self.rect.x += self.speed
            
            self.image = self.images[self.step_index//20]
            self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
            self.step_index += 1
            if self.step_index >= 40:
                self.step_index = 0
            
            if pygame.sprite.collide_rect(self, bullet1):
                self.exploding = True
                explosion_sound.play()
                bullet1.state = "ready"
                bullet1.rect.x = -50
                bullet1.rect.y = -50
                pygame.sprite.Sprite.kill(bullet1)

            if self.exploding:
                self.explode_step_index += 1

                if self.explode_step_index >= 40:
                    self.exploding = False
                    pygame.sprite.Sprite.add(self, hit_boss)
                    pygame.sprite.Sprite.remove(self, boss_group)
                    self.rect.x = -100
                    boss_start.play()
                    

                self.image = self.explosion[self.explode_step_index // 10]
                self.image = pygame.transform.scale(self.image, (16 * 6, 16 * 6))
        
            # keeps enemy within bounds 
            if self.rect.x < 0 and not self.dir:
                self.rect.y += self.jump
                self.dir = True
            if self.rect.x > 736 and self.dir:
                self.rect.y += self.jump
                self.dir = False
            if self.rect.y > 600:
                for i in range(len(high_scores) - 1):
                    if score > high_scores[i]:
                        high_scores.insert(i, score)
                        high_scores.pop()
                        break
                print(high_scores)
                leaderboard()
            
            match level:
                case 1:
                    self.speed = 8
                case 2:
                    self.speed = 8.75
                case 3:
                    self.speed = 9.5
                case 4:
                    self.speed = 10.25
                case 5:
                    self.speed = 11
                case 6:
                    self.speed = 11.75
                case 7:
                    self.speed = 12.5
                case 8:
                    self.speed = 13.25
                case 9:
                    self.speed = 14
                case 10:
                    self.speed = 14.75
                case 11:
                    self.speed = 15.5
                case 12:
                    self.speed = 16.25
                case _:
                    self.speed = 17


    # power-up class
    class Powerup(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.speed = 4
            self.pos = [random.randint(0,700), random.randint(10,30)]
            self.animate = [pygame.image.load("assets\\pwr_up_f_1.png"), pygame.image.load("assets\\pwr_up_f_2.png")]
            self.step_index = 0
            self.image = self.animate[self.step_index]
            self.image = pygame.transform.scale(self.image, (16*2, 16*2))
            self.rect = self.image.get_rect(center=(self.pos[0],self.pos[-1]))
        
        def update(self):
            self.rect.y += self.speed
            self.image = self.animate[self.step_index // 15]
            self.image = pygame.transform.scale(self.image, (16*2, 16*2))
            self.step_index += 1

            if self.step_index >= 30:
                self.step_index = 0
            
            if self.pos[-1] >= 800:
                self.kill()


    # chooses which power up to enable
    def choose_pwr_up():
        global explode
        random_pwr = [1,2,3,4,5,6,7,8,9,10,11,12]
        random_choose = random.choice(random_pwr)

        match random_choose:
            case 1:
                player.power_up()
            case 2:
                bullet1.power_up()
            case 3:
                bullet1.power_up()
            case 4:
                player.power_up()
            case 5:
                player.power_up()
            case 6:
                player.power_up()
            case 7:
                player.power_up()
            case 8:
                bullet1.power_up()
            case 9:
                bullet1.power_up()
            case 10:
                player.power_up()
            case 11:
                player.power_up()
            case 12:
                player.power_up()


    # background images, need to transform some due to size limitations
    background = pygame.image.load("backgrounds\\background_four.png")
    background = pygame.transform.scale(background, (640 * 1.75, 360 * 1.75))
    level_2_bg = pygame.image.load("backgrounds\\Background_space.png")
    level_3_bg = pygame.image.load("backgrounds\\bg_3.png")
    level_4_bg = pygame.image.load("backgrounds\\background_two.png")
    level_4_bg = pygame.transform.scale(level_4_bg, (816 * 1.25, 480 * 1.25))
    level_5_bg = pygame.image.load("backgrounds\\background_five.png")
    level_5_bg = pygame.transform.scale(level_5_bg, (272 * 3.75, 160 * 3.75))
    level_6_bg = pygame.image.load("backgrounds\\background_six.png")
    level_6_bg = pygame.transform.scale(level_6_bg, (272 * 3.75, 160 * 3.75))
    level_7_bg = pygame.image.load("backgrounds\\background_seven.png")
    level_7_bg = pygame.transform.scale(level_7_bg, (272 * 3.75, 160 * 3.75))
    level_8_bg = pygame.image.load("backgrounds\\background_eight.png")
    level_8_bg = pygame.transform.scale(level_8_bg, (272 * 3.75, 160 * 3.75))
    level_9_bg = pygame.image.load("backgrounds\\background_nine.png")
    level_9_bg = pygame.transform.scale(level_9_bg, (272 * 3.75, 160 * 3.75))
    level_10_bg = pygame.image.load("backgrounds\\background_ten.png")
    level_10_bg = pygame.transform.scale(level_10_bg, (272 * 3.75, 160 * 3.75))
    level_11_bg = pygame.image.load("backgrounds\\background_eleven.png")
    level_11_bg = pygame.transform.scale(level_11_bg, (272 * 3.75, 160 * 3.75))
    level_12_bg = pygame.image.load("backgrounds\\background_twelve.png")
    level_12_bg = pygame.transform.scale(level_12_bg, (272 * 3.75, 160 * 3.75))
    

    # sounds
    pygame.mixer.music.load("sounds\\Mecha Collection.wav")
    pygame.mixer.music.set_volume(0.10)
    pygame.mixer.music.play(-1)

    new_level = pygame.mixer.Sound("sounds\\new_level.wav")
    new_level.set_volume(0.25)

    enemy_defeat = pygame.mixer.Sound("sounds\\01. Credit Sound.mp3")
    enemy_defeat.set_volume(0.10)

    explosion_sound = pygame.mixer.Sound("sounds\\explosion_sound.wav")
    explosion_sound.set_volume(0.05)

    shoot_sound = pygame.mixer.Sound("sounds\\13. Fighter -Shot1.mp3")
    shoot_sound.set_volume(0.10)

    boss_start = pygame.mixer.Sound("sounds\\17. Challenging Stage (Start).mp3")
    boss_start.set_volume(0.10)

    boss_appear = pygame.mixer.Sound("sounds\\09. Triple Formation -Appearance.mp3")
    boss_appear.set_volume(0.10)


    # sprite groups from classes for enemy, player, bullet, boss, powerup
    sprite_group = pygame.sprite.Group()
    sprite_group.add(Enemy())

    boss_group = pygame.sprite.Group()

    player_group = pygame.sprite.Group()
    player = player()
    player_group.add(player)

    bullet_group = pygame.sprite.Group()
    bullet1 = bullet()

    pwr_up_group = pygame.sprite.Group()

    hit_list = pygame.sprite.Group()

    hit_boss = pygame.sprite.Group()


    # timed events, enemy spawning, faster spawning
    # creates a custom event
    spawn_event = pygame.event.custom_type()
    # how long between event triggers (in milliseconds, starts at 3.5 seconds)
    spawn_timer = 3500
    # sets the timer for this event
    pygame.time.set_timer(spawn_event, spawn_timer)

    # creates a new custom event
    faster_timer_event = pygame.event.custom_type()
    # time between event triggers (20 seconds)
    timer_event_timer = 20000
    # sets the timer for this event
    pygame.time.set_timer(faster_timer_event, timer_event_timer)

    pwr_up_event = pygame.event.custom_type()
    pwr_up_timer = random.randint(20000, 35000)
    pygame.time.set_timer(pwr_up_event, pwr_up_timer)

    # checks if boss is spawned
    boss_spawned = False

    # removes power up abilities after set time
    pwr_down_event = pygame.event.custom_type()
    pwr_down_time = 10000
    pygame.time.set_timer(pwr_down_event, pwr_down_time)


    # main game loop
    running = True
    while running:
        # background screen color update
        screen.fill((128, 128, 128))
        # Background Images
        match level:
            case 1:
                screen.blit(background, (0,0))
            case 2:
                screen.blit(level_2_bg, (0,0))
            case 3:
                screen.blit(level_3_bg, (0,0))
            case 4:
                screen.blit(level_4_bg, (0,0))
            case 5:
                screen.blit(level_5_bg, (0,0))
            case 6:
               screen.blit(level_6_bg, (0,0))
            case 7:
                screen.blit(level_7_bg, (0,0))
            case 8:
                screen.blit(level_8_bg, (0,0))
            case 9:
                screen.blit(level_9_bg, (0,0))
            case 10:
                screen.blit(level_10_bg, (0,0))
            case 11:
                screen.blit(level_11_bg, (0,0))
            case 12:
                screen.blit(level_12_bg, (0,0))
            case _:
                screen.blit(level_12_bg, (0,0))
            

        # displaying UI
        screen.blit(score_render, (25,560))
        screen.blit(level_render, (635, 560))


        # main event queue
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_TAB]:
                pygame.mixer.music.pause()
                main_menu()

            # every 3.5 seconds a new enemy spawns on the event trigger
            if event.type == spawn_event:
                sprite_group.add(Enemy())
        
            # causes faster spawning for enemies
            if event.type == faster_timer_event:
                spawn_timer -= 150
                pygame.time.set_timer(spawn_event, spawn_timer)

            # spawns in power up sprite, resets random spawn timing so its different every time
            if event.type == pwr_up_event:
                pwr_up_group.add(Powerup())
                pwr_up_timer = random.randint(20000, 35000)
                pygame.time.set_timer(pwr_up_event, pwr_up_timer)
            
            # removes power up abilities
            if event.type == pwr_down_event:
                player.speed = 10
                player.pwr_up = False
                bullet1.speed = bullet1.old_speed
                bullet1.pwr_up = False

            # checks for spacebar pressed, if bullet is ready to be fired, will add bullet1 to the bullet group
            if keys[pygame.K_SPACE] and bullet1.state == "ready":
                bullet1.state = "fire"
                bullet_group.add(bullet1)
                bullet1.rect.x = player.rect.x + 12
                bullet1.rect.y = player.rect.y - 25
                shoot_sound.play()


        # debug for spawning timer, makes sure it never goes below 0 (which would stop spawning enemies)
        if spawn_timer <= 500:
            spawn_timer == 500


        # when the bullet goes out of bounds, state changes to ready and can be fired again
        if bullet1.rect.y < -32:
            bullet1.state = "ready"    


        # collision loops, checks lists for enemies, adds score, then clears the lists
        if hit_list:
            for i in range(len(hit_list)):
                score += 1
                score_render = score_font.render(f"Score: {str(score)}", False, (0,255,26))
                enemy_defeat.play()
                pygame.sprite.Group.empty(hit_list)

        if hit_boss:
            pygame.sprite.Group.empty(bullet_group)
            for i in range(len(hit_boss)):
                score += 1
                score_render = score_font.render(f"Score: {str(score)}", False, (0,255,26))
                boss_spawned = False
                bullet1.state = "ready"
                pygame.sprite.Group.empty(hit_boss)
        

        # checks power up collision
        pwr_list = pygame.sprite.groupcollide(player_group, pwr_up_group, False, True)

        # gives player power ups
        if pwr_list:
            choose_pwr_up()
            pwr_list.clear()


        # spawns boss every 20 score
        if score % 20 == 0 and not boss_spawned and score != 0:
            boss_group.add(Boss())
            boss_spawned = True
            boss_appear.play()


        # changes level every 20 score
        if score >= 0 and score < 20:
            level = 1
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 20 and score < 40:
            level = 2
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 40 and score < 60:
            level = 3
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 60 and score < 80:
            level = 4
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 80 and score < 100:
            level = 5
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 100 and score < 120:
            level = 6
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 120 and score < 140:
            level = 7
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 140 and score < 160:
            level = 8
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 160 and score < 180:
            level = 9
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 180 and score < 200:
            level = 10
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 200 and score < 220:
            level = 11
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        elif score >= 220 and score < 240:
            level = 12
            level_render = level_font.render(f"Level: {str(level)}", False, (0,255,26))
        else: 
            level = 13
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
        pwr_up_group.draw(screen)
        pwr_up_group.update()


        # refreshes the screen and keeps the fps at 60
        pygame.display.flip()
        clock.tick(60)


# Leaderboard Function
def leaderboard():
    # scene setup, basic variables, debug
    global high_scores
    screen.fill((0,0,0))
    background = pygame.image.load("backgrounds\\background_two.png")
    background = pygame.transform.scale(background, (816 * 1.25, 480 * 1.25))
    clock = pygame.time.Clock()
    pygame.mixer.music.pause()

    lose_sound = pygame.mixer.Sound("sounds\\24. Name Entry (2nd-5th).mp3")
    lose_sound.set_volume(0.10)

    lose_sound.play(-1)

    # main loop
    running = True
    while running:
        # sets background, gets screen center
        screen_center = screen.get_width() // 2
        screen.blit(background, (0,0))


        # leaderboard font
        score_font = pygame.font.Font("fonts\\GravityRegular5.ttf", 20)

        # title font
        title_font = pygame.font.Font("fonts\\GravityRegular5.ttf", 26)

        # back button image
        back_img = pygame.image.load("UI\\UI - back.png").convert_alpha()


        # button class
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


        # leaderboard text
        title = title_font.render("Galactic Invasion Leaderboard", False, (255,255,255))
        title_rect = title.get_rect(centerx=screen_center, centery=25)

        score_1 = score_font.render(f"1 - {high_scores[0]}", False, (255,255,255))
        score_1_rect = score_1.get_rect(x=150, y=100)
        score_2 = score_font.render(f"2 - {high_scores[1]}", False, (255,255,255))
        score_2_rect = score_2.get_rect(x=150, y=150)
        score_3 = score_font.render(f"3 - {high_scores[2]}", False, (255,255,255))
        score_3_rect = score_3.get_rect(x=150, y=200)
        score_4 = score_font.render(f"4 - {high_scores[3]}", False, (255,255,255))
        score_4_rect = score_4.get_rect(x=150, y=250)
        score_5 = score_font.render(f"5 - {high_scores[4]}", False, (255,255,255))
        score_5_rect = score_5.get_rect(x=150, y=300)
        score_6 = score_font.render(f"6 - {high_scores[5]}", False, (255,255,255))
        score_6_rect = score_6.get_rect(x=150, y=350)
        score_7 = score_font.render(f"7 - {high_scores[6]}", False, (255,255,255))
        score_7_rect = score_7.get_rect(x=150, y=400)
        score_8 = score_font.render(f"8 - {high_scores[7]}", False, (255,255,255))
        score_8_rect = score_8.get_rect(x=150, y=450)
        score_9 = score_font.render(f"9 - {high_scores[8]}", False, (255,255,255))
        score_9_rect = score_9.get_rect(x=150, y=500)
        score_10 = score_font.render(f"10 - {high_scores[9]}", False, (255,255,255))
        score_10_rect = score_10.get_rect(x=130, y=550)

        score_11 = score_font.render(f"11 - {high_scores[10]}", False, (255,255,255))
        score_11_rect = score_11.get_rect(x=500, y=100)
        score_12 = score_font.render(f"12 - {high_scores[11]}", False, (255,255,255))
        score_12_rect = score_11.get_rect(x=500, y=150)
        score_13 = score_font.render(f"13 - {high_scores[12]}", False, (255,255,255))
        score_13_rect = score_11.get_rect(x=500, y=200)
        score_14 = score_font.render(f"14 - {high_scores[13]}", False, (255,255,255))
        score_14_rect = score_11.get_rect(x=500, y=250)
        score_15 = score_font.render(f"15 - {high_scores[14]}", False, (255,255,255))
        score_15_rect = score_11.get_rect(x=500, y=300)
        score_16 = score_font.render(f"16 - {high_scores[15]}", False, (255,255,255))
        score_16_rect = score_11.get_rect(x=500, y=350)
        score_17 = score_font.render(f"17 - {high_scores[16]}", False, (255,255,255))
        score_17_rect = score_11.get_rect(x=500, y=400)
        score_18 = score_font.render(f"18 - {high_scores[17]}", False, (255,255,255))
        score_18_rect = score_11.get_rect(x=500, y=450)
        score_19 = score_font.render(f"19 - {high_scores[18]}", False, (255,255,255))
        score_19_rect = score_11.get_rect(x=500, y=500)
        score_20 = score_font.render(f"20 - {high_scores[19]}", False, (255,255,255))
        score_20_rect = score_20.get_rect(x=500, y=550)


        # event queue
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if keys[pygame.K_TAB]:
                lose_sound.stop()
                main_menu()
            if event.type == pygame.QUIT:
                sys.exit(0)
        

        # setting up button
        back_button = Button(20, 550, back_img, 1.0)
        back_button.draw()
        if back_button.clicked == True:
            lose_sound.stop()
            main_menu()


        # blitting text to screen
        screen.blit(title, title_rect)
        screen.blit(score_1, score_1_rect.topleft)
        screen.blit(score_2, score_2_rect.topleft)
        screen.blit(score_3, score_3_rect.topleft)
        screen.blit(score_4, score_4_rect.topleft)
        screen.blit(score_5, score_5_rect.topleft)
        screen.blit(score_6, score_6_rect.topleft)
        screen.blit(score_7, score_7_rect.topleft)
        screen.blit(score_8, score_8_rect.topleft)
        screen.blit(score_9, score_9_rect.topleft)
        screen.blit(score_10, score_10_rect.topleft)
        screen.blit(score_11, score_11_rect.topleft) 
        screen.blit(score_12, score_12_rect.topleft)
        screen.blit(score_13, score_13_rect.topleft)
        screen.blit(score_14, score_14_rect.topleft)
        screen.blit(score_15, score_15_rect.topleft)
        screen.blit(score_16, score_16_rect.topleft)
        screen.blit(score_17, score_17_rect.topleft)
        screen.blit(score_18, score_18_rect.topleft)
        screen.blit(score_19, score_19_rect.topleft)
        screen.blit(score_20, score_20_rect.topleft)


        # refreshes screen, sets FPS
        pygame.display.flip()
        clock.tick(60)


# Loading Function
def loading():
    # scene setup, basic variables, debug
    screen.fill((0,0,0))
    screen_center = screen.get_width() // 2
    screen_mid = screen.get_height() // 2
    clock = pygame.time.Clock()


    # loading animation class
    class loading_animate(pygame.sprite.Sprite):
        # initializes the class, and info for all new objects
        def __init__(self):
            super().__init__()
            self.images = [pygame.image.load("UI\\loading_1.png"),pygame.image.load("UI\\loading_2.png"),pygame.image.load("UI\\loading_3.png"),pygame.image.load("UI\\loading_4.png"),pygame.image.load("UI\\loading_5.png"),pygame.image.load("UI\\loading_6.png"),pygame.image.load("UI\\loading_7.png"),pygame.image.load("UI\\loading_8.png"),pygame.image.load("UI\\loading_9.png"),pygame.image.load("UI\\loading_10.png")]
            self.step_index = 0
            self.image = self.images[self.step_index]
            self.image = pygame.transform.scale(self.image, (35 * 9, 16 * 9))
            # using list for coords
            self.rect = self.image.get_rect(center=(screen_center,screen_mid))
    
        def update(self):
            # animating sprite
            self.image = self.images[self.step_index // 10]
            self.image = pygame.transform.scale(self.image, (35 * 9, 16 * 9))
            self.step_index += 1
            # resets animation index
            if self.step_index >= 90:
                game()
    

    # sprite group, setting loading object and font/text
    loading_group = pygame.sprite.Group()
    loading_group.add(loading_animate())

    loading_font = pygame.font.Font("fonts\\GravityRegular5.ttf", 24)
    loading_text = loading_font.render("Loading...", False, (255,255,255))
    loading_rect = loading_text.get_rect(centerx=screen_center,centery=screen_mid + 60)


    # main loop
    running = True
    while running:
        # fills screen
        screen.fill((0,0,0))


        # event queue
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_TAB]:
                running = False


        # draws loading object to screen
        loading_group.draw(screen)
        loading_group.update()


        # blits text to screen
        screen.blit(loading_text, loading_rect.topleft)
        

        # refreshes screen, sets FPS
        pygame.display.flip()
        clock.tick(60)

# begins game in main menu screen
main_menu()