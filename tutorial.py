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
TOP_BAR_HEIGHT = 50

LABEL_FONT = pygame.font.SysFont("comicsans", 28)

#lives
lives = 3

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
        
    def collide(self, x, y):
        # Check if the given coordinates are within the target
        distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        return distance <= self.size
        
def draw(win, targets):
    # Fill the window with the background color
    win.fill(BG_COLOR)
    
    # Draw each target in the targets list
    for target in targets:
        target.draw(win)
        
    

def format_time(secs):
    # Convert the elapsed time from seconds to minutes and seconds
    milli = math.floor(int(secs*1000%1000)/10)
    seconds = int(round(secs%60, 1))
    minutes = int(secs // 60)
    
    return f"{minutes:02d}:{seconds:02d}.{milli}"

def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    # Display the elapsed time, targets pressed, and misses at the top of the window
    pygame.draw.rect(win, "grey", (0,0, WIDTH, TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}",1 , "black"
        )
    
    
    win.blit(time_label, (5, 5))

def main():
    run = True
    targets = []  # List to hold all targets
    clock = pygame.time.Clock(); # Create a clock object to control the frame rate
    
    # Initialize game variables
    target_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()
        
    # Set a timer to add a new target at regular intervals
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)
    
    while run:
        
        # Event handling
        clock.tick(60)
        click = False
        mouse_position = pygame.mouse.get_pos()
        elapsed_time = time.time() -start_time
        
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
                
                
            # Handle mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
                
                
        # Update each target in the list
        for target in targets:
            target.update()
            
            # Remove targets that have shrunk to zero size
            if target.size <=0 :
                targets.remove(target)
                misses += 1
                
            # Check for collisions with the mouse click
            if click and target.collide(*mouse_position):
                targets.remove(target)
                target_pressed += 1
                
        # End game if lives == 0
        if misses >= lives:
            run = False
            break
            
        # Draw the current state of the game
        draw(WIN, targets)
        draw_top_bar(WIN, elapsed_time, target_pressed, misses)
        # Update the display
        pygame.display.update()
        
    # Quit the game
    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()