import pygame

# Initialize pygame and get display info
pygame.init()
infoObject = pygame.display.Info()

# Set the width and height of the screen
screenWidth = infoObject.current_w
screenHeight = infoObject.current_h

# Adjust screen size for gameplay area
WIDTH, HEIGHT = screenWidth - 100, screenHeight - 150

# Create the game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

# Constants for target appearance rate 
TARGET_INCREMENT = 400  # Time in milliseconds between new targets appearing
TARGET_EVENT = pygame.USEREVENT  # Custom event for adding a new target

# Padding to ensure targets spawn within the window
TARGET_PADDING = 30

# Background color of the game window
BG_COLOR = (0, 25, 40)
TOP_BAR_HEIGHT = 50

LABEL_FONT = pygame.font.SysFont("comicsans", 28)

# Lives
lives = 5
