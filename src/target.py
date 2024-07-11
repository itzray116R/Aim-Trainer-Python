import pygame
import math

class Target:
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
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow = False
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
    
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR_1, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.COLOR_2, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR_1, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.COLOR_2, (self.x, self.y), self.size * 0.4)
        
    def collide(self, x, y):
        distance = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        return distance <= self.size
