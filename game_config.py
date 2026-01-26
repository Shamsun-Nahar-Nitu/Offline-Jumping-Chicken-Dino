# Game Configuration File


# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (83, 83, 83)
CLOUD_GRAY = (200, 200, 200)

# Frame rate - controls how fast the game runs
FPS = 60

# Ground settings
GROUND_HEIGHT = 50
GROUND_Y = SCREEN_HEIGHT - GROUND_HEIGHT

# Chicken
GRAVITY = 1.2  # How fast the chicken falls
JUMP_STRENGTH = -20  # Negative because up is negative in pygame
CHICKEN_X = 80  # Chicken's horizontal position (fixed)

# Game speed
INITIAL_GAME_SPEED = 6
SPEED_INCREMENT = 0.005  # How much speed increases per frame

# Obstacle settings
MIN_OBSTACLE_DISTANCE = 300  # Minimum space between obstacles
MAX_OBSTACLE_DISTANCE = 600  # Maximum space between obstacles

# Cloud settings
CLOUD_SPEED = 2
MIN_CLOUD_DISTANCE = 200
MAX_CLOUD_DISTANCE = 400