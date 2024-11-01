import pygame,random,sys

# Intialize the pygame
pygame.init()


# create the screen, width/height
screen = pygame.display.set_mode((800,600))


# Title Caption and Icon
pygame.display.set_caption("Group 9 Project: Galactic Invasion")
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)

high_scores = [0,0,0,0,0,0,0,0,0,0]



# Main Menu Function
def main_menu():
    clock = pygame.time.Clock()
    run = True
    pygame.mixer.music.pause()
    while run:
        screen_center = screen.get_width() // 2
        screen.fill((0,0,0))
        # font used for main menu text
        title_font = pygame.font.Font("monogram.ttf", 60)

        # game title text
        title_text = title_font.render("Group 9 Project: Galactic Invasion", False, (255,255,255))
        title_rect = title_text.get_rect(centerx=screen_center, centery=100)

        # button images
        start_img = pygame.image.load("UI - start.png").convert_alpha()
        quit_img = pygame.image.load("UI - quit.png").convert_alpha()
        options_img = pygame.image.load("UI - options.png").convert_alpha()

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
        if start_button.clicked == True:
            loading()

        quit_button = Button(315, 425, quit_img, 1.5)
        quit_button.draw()
        if quit_button.clicked == True:
            sys.exit(0)
        
        options_button = Button(315, 350, options_img, 1.5)
        options_button.draw()
        if options_button.clicked == True:
            paused()

        # blitting title text to screen
        screen.blit(title_text, title_rect.topleft)

        # key and event queue for main menu
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


# Options Menu Function
def paused():
    clock = pygame.time.Clock()
    keep_run = True
    pygame.mixer.music.pause()
    while keep_run:
        screen_center = screen.get_width() // 2
        screen.fill((0,0,0))

        # options menu font
        pause_font = pygame.font.Font("monogram.ttf", 30)

        # button image
        back_img = pygame.image.load("UI - back.png").convert_alpha()

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
            if keys[pygame.K_ESCAPE]:
                keep_run = False
                
        pygame.display.flip()
        clock.tick(60)


# Main Game Function
def game():
    global high_scores
    # enemy class
    class Enemy(pygame.sprite.Sprite):
        # initializes the class, and info for all new objects
        def __init__(self):
            super().__init__()
            self.speed = 8
            self.name = "enemy"
            self.damage = 5
            self.images = [pygame.image.load("enemy.png"), pygame.image.load("enemy_2.png")]
            self.step_index = 0
            self.image = self.images[0]
            self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
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
            
            # animating sprite
            self.image = self.images[self.step_index // 20]
            self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
            self.step_index += 1
            # resets animation index
            if self.step_index >= 40:
                self.step_index = 0
        
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
                    self.speed = 10
                case 3:
                    self.speed = 12
                case 4:
                    self.speed = 14

    # bullet class
    class bullet(pygame.sprite.Sprite):
        # initializes bullet class and variables for all bullet objects
        def __init__(self):
            super().__init__()
            self.speed = 10
            self.old_speed = 10
            self.name = "bullet"
            self.x = 0
            self.y = 0
            self.pwr_up = False
            self.images = [pygame.image.load("laser_f_1.png"), pygame.image.load("laser_f_2.png")]
            
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

            self.image = pygame.transform.scale(self.image, (5*2.75, 12*2.75))

            if level == 2:
                self.old_speed = 12
            elif level == 3:
                self.old_speed = 15
            
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
            self.left = [pygame.image.load("ship_f_1.png"), pygame.image.load("ship_f_11.png")]
            
            self.right = [pygame.image.load("ship_f_5.png"), pygame.image.load("ship_f_55.png")]
            
            self.idle = [pygame.image.load("ship_f_3.png"), pygame.image.load("ship_f_33.png")]

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
                print("power_Up")
                self.pwr_up = True


    # boss class
    class Boss(pygame.sprite.Sprite):
        # initializes the class, and info for all new objects
        def __init__(self):
            super().__init__()
            self.speed = 10
            self.name = "enemy"
            self.damage = 5
            self.images = [pygame.image.load("boss_1.png"), pygame.image.load("boss_2.png")]
            self.step_index = 0
            self.image = self.images[0]
            self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
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
            
            self.image = self.images[self.step_index//20]
            self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
            self.step_index += 1
            if self.step_index >= 40:
                self.step_index = 0
        
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
                    self.speed = 10
                case 3:
                    self.speed = 12
                case 4:
                    self.speed = 14

    # power-up class
    class Powerup(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.speed = 4
            self.pos = [random.randint(0,700), random.randint(10,30)]
            self.animate = [pygame.image.load("pwr_up_f_1.png"), pygame.image.load("pwr_up_f_2.png")]
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
        random_pwr = [1,2,3,4,5,6,7,8,9,10,11,12]
        random_choose = random.choice(random_pwr)

        match random_choose:
            case 1:
                player.power_up()
            case 2:
                bullet1.power_up()
            case 3:
                pygame.sprite.Group.empty(sprite_group)
            case 4:
                player.power_up()
            case 5:
                bullet1.power_up()
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


    clock = pygame.time.Clock()

    # background image
    background = pygame.image.load("background_four.png")
    background = pygame.transform.scale(background, (640 * 1.75, 360 * 1.75))
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

    pwr_up_event = pygame.event.custom_type()
    pwr_up_timer = random.randint(20000, 35000)
    pygame.time.set_timer(pwr_up_event, pwr_up_timer)

    # checks if boss is spawned
    boss_spawned = False

    pwr_down_event = pygame.event.custom_type()
    pwr_down_time = 10000
    pygame.time.set_timer(pwr_down_event, pwr_down_time)


    # main game loop
    running = True
    while running:
        # background screen color update
        screen.fill((128, 128, 128))
        # Background Image
        if level == 1:
            screen.blit(background, (0,0))
        if level == 2:
            screen.blit(level_2_bg, (0,0))
        if level == 3:
            screen.blit(level_3_bg, (0,0))
        screen.blit(score_render, (5,560))
        screen.blit(level_render, (650, 560))

        keys = pygame.key.get_pressed()
        # every event gets logged below and you loop through each event, like keystrokes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
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
                print(bullet1.speed)

            # checks for spacebar pressed, if bullet is ready to be fired, will add bullet1 to the bullet group
            if keys[pygame.K_SPACE] and bullet1.state == "ready":
                bullet1.state = "fire"
                bullet_group.add(bullet1)
                bullet1.rect.x = player.rect.x + 12
                bullet1.rect.y = player.rect.y - 25

        # debug for spawning timer, makes sure it never goes below 0 (which would stop spawning enemies)
        if spawn_timer <= 500:
            spawn_timer == 500

        # when the bullet goes out of bounds, state changes to ready and can be fired again
        if bullet1.rect.y < -32:
            bullet1.state = "ready"    

        # checks if anything in bullet group collides with enemies, if so the enemy and bullet are deleted from groups
        hit_list = pygame.sprite.groupcollide(bullet_group, sprite_group, True, True)

        # checks if sprites are in the hit_list group, if so, score +1, clears group
        if hit_list:
            for i in range(len(hit_list)):
                score += 1
                score_render = score_font.render(f"Score: {str(score)}", False, (0,255,26))
                enemy_defeat.play()
                bullet1.state = "ready"
                hit_list.clear()
        
        # checks for collision with boss, if so, deletes boss and bullet
        hit_boss = pygame.sprite.groupcollide(bullet_group, boss_group, True, True)

        # checks if sprites are in the hit_boss, if so, score +1, clears group
        if hit_boss:
            for i in range(len(hit_boss)):
                score += 1
                score_render = score_font.render(f"Score: {str(score)}", False, (0,255,26))
                enemy_defeat.play()
                boss_spawned = False
                bullet1.state = "ready"
                hit_boss.clear()
        
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

        # changes level every 20 score
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
        pwr_up_group.draw(screen)
        pwr_up_group.update()

        # refreshes the screen and keeps the fps at 60
        pygame.display.flip()
        clock.tick(60)


# Leaderboard Function
def leaderboard():
    global high_scores
    clock = pygame.time.Clock()
    pygame.mixer.music.pause()
    running = True
    while running:
        screen_center = screen.get_width() // 2
        screen.fill((0,0,0))

        # leaderboard font
        score_font = pygame.font.Font("monogram.ttf", 40)

        # title font
        title_font = pygame.font.Font("monogram.ttf", 64)

        # back button image
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


        # leaderboard text
        title = title_font.render("Galactic Invasion Leaderboard", False, (255,255,255))
        title_rect = title.get_rect(centerx=screen_center, centery=25)

        score_1 = score_font.render(f"1 - {high_scores[0]}", False, (255,255,255))
        score_1_rect = score_1.get_rect(centerx=screen_center, centery=100)

        score_2 = score_font.render(f"2 - {high_scores[1]}", False, (255,255,255))
        score_2_rect = score_2.get_rect(centerx=screen_center, centery=150)

        score_3 = score_font.render(f"3 - {high_scores[2]}", False, (255,255,255))
        score_3_rect = score_3.get_rect(centerx=screen_center, centery=200)

        score_4 = score_font.render(f"4 - {high_scores[3]}", False, (255,255,255))
        score_4_rect = score_4.get_rect(centerx=screen_center, centery=250)

        score_5 = score_font.render(f"5 - {high_scores[4]}", False, (255,255,255))
        score_5_rect = score_5.get_rect(centerx=screen_center, centery=300)

        score_6 = score_font.render(f"6 - {high_scores[5]}", False, (255,255,255))
        score_6_rect = score_6.get_rect(centerx=screen_center, centery=350)

        score_7 = score_font.render(f"7 - {high_scores[6]}", False, (255,255,255))
        score_7_rect = score_7.get_rect(centerx=screen_center, centery=400)

        score_8 = score_font.render(f"8 - {high_scores[7]}", False, (255,255,255))
        score_8_rect = score_8.get_rect(centerx=screen_center, centery=450)

        score_9 = score_font.render(f"9 - {high_scores[8]}", False, (255,255,255))
        score_9_rect = score_9.get_rect(centerx=screen_center, centery=500)

        score_10 = score_font.render(f"10 - {high_scores[9]}", False, (255,255,255))
        score_10_rect = score_10.get_rect(centerx=screen_center, centery=550)

        for event in pygame.event.get():
            if event.type == pygame.K_ESCAPE:
                main_menu()
            if event.type == pygame.QUIT:
                sys.exit(0)
        
        back_button = Button(20, 550, back_img, 1.0)
        back_button.draw()
        if back_button.clicked == True:
            main_menu()

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
        pygame.display.flip()
        clock.tick(60)


# Loading Function
def loading():
    screen_center = screen.get_width() // 2
    screen_mid = screen.get_height() // 2
    clock = pygame.time.Clock()
    screen.fill((0,0,0))

    class loading_animate(pygame.sprite.Sprite):
        # initializes the class, and info for all new objects
        def __init__(self):
            super().__init__()
            self.images = [pygame.image.load("loading_1.png"),pygame.image.load("loading_2.png"),pygame.image.load("loading_3.png"),pygame.image.load("loading_4.png"),pygame.image.load("loading_5.png"),pygame.image.load("loading_6.png"),pygame.image.load("loading_7.png"),pygame.image.load("loading_8.png"),pygame.image.load("loading_9.png"),pygame.image.load("loading_10.png")]
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
    
    loading_group = pygame.sprite.Group()
    loading_group.add(loading_animate())

    running = True
    while running:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if keys[pygame.K_ESCAPE]:
                running = False

        loading_group.draw(screen)
        loading_group.update()
        
        pygame.display.flip()
        clock.tick(60)

# begins game
main_menu()