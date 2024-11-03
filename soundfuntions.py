# Initialize pygame mixer
pygame.mixer.init()

def play_background_music(24. Name Entry (2nd-5th).mp3, volume=0.5):

    try:
        # Load the music file
        pygame.mixer.music.load(24. Name Entry (2nd-5th).mp3)

        # Set volume
        pygame.mixer.music.set_volume(volume)

        # Play music in an infinite loop
        pygame.mixer.music.play(-1)

    except pygame.error as e:
        print(f"Error loading or playing music: {e}")

play_background_music()


def dead_enemy(sound_file, volume=0.5):

    # Initialize the mixer and load the sound
    pygame.mixer.init()
    sound = pygame.mixer.Sound(22. Miss.mp3)
    sound.set_volume(volume)

    # Play the sound
    sound.play()

def player_dead(sound_file, volume=0.5):

# Initialize the mixer and load the sound
pygame.mixer.init()
sound = pygame.mixer.Sound(22. Miss.mp3)
sound.set_volume(volume)

# Play the sound
sound.play()

def shoot_sound(sound_file, volume=0.5):

# Initialize the mixer and load the sound
pygame.mixer.init()
sound = pygame.mixer.Sound(13. Fighter -Shot1.mp3)
sound.set_volume(volume)

# Play the sound
sound.play()

def shoot_sound_upgrade(sound_file, volume=0.5):

# Initialize the mixer and load the sound
pygame.mixer.init()
sound = pygame.mixer.Sound(15. Fighter -Shot2.mp3)
sound.set_volume(volume)

# Play the sound
sound.play()

def game_over(sound_file, volume=0.5):

# Initialize the mixer and load the sound
pygame.mixer.init()
sound = pygame.mixer.Sound(03. In-Game Ambience.mp3)
sound.set_volume(volume)

# Play the sound
sound.play()
