import math
import random
import time
import pygame

# Initialize the game
pygame.init()
infoObject = pygame.display.Info()
# Set the width and height of the screen [width, height]
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

class Target:
    # Constants for target properties
    MAX_SIZE = 30  # Maximum size of the target
    GROWTH_RATE = 0.1  # Rate at which the target grows/shrinks
    COLOR_1 = "red"  # Primary color of the target
    COLOR_2 = "blue"  # Secondary color of the target
    
    def __init__(self, x, y):
        self.x = x  # X position of the target
        self.y = y  # Y position of the target
        self.size = 0  # Initial size of the target
        self.grow = True  # Flag to determine if the target is growing or shrinking
        self.color = Target.COLOR_1  # Initial color of the target
        
    def update(self):
        # Update the size of the target based on its growth rate and direction
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
    
    def draw(self, win):
        # Draw the target with concentric circles
        pygame.draw.circle(win, self.COLOR_1, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.COLOR_2, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR_1, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.COLOR_2, (self.x, self.y), self.size * 0.4)
        
def draw(win, targets):
    # Fill the window with the background color
    win.fill(BG_COLOR)
    
    # Draw each target in the targets list
    for target in targets:
        target.draw(win)
        
    # Update the display
    pygame.display.update()

def main():
    run = True
    targets = []  # List to hold all targets
    
    # Set a timer to add a new target at regular intervals
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            # Add a new target at a random position
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)
                
        # Update each target in the list
        for target in targets:
            target.update()        
                
        # Draw the current state of the game
        draw(WIN, targets)

    pygame.quit()

if __name__ == "__main__":
    main()