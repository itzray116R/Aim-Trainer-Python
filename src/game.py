import pygame
import random
import time
from settings import *
from target import Target
from utils import format_time, get_middle

def draw(win, targets):
    win.fill(BG_COLOR)
    for target in targets:
        target.draw(win)

def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    pygame.draw.rect(win, "grey", (0, 0, WIDTH, TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "black")
    
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "black")
    
    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "black")
    
    lives_label = LABEL_FONT.render(f"Lives: {lives}", 1, "black")
    
    misses_label = LABEL_FONT.render(f"Misses: {misses}", 1, "black")
    
    win.blit(time_label, (5, 5))    
    win.blit(speed_label, (230, 5))
    win.blit(hits_label, (450, 5))
    win.blit(lives_label, (600, 5))

def end_screen(win, elapsed_time, targets_pressed, clicks):
    win.fill(BG_COLOR)
    time_label = LABEL_FONT.render(f"Time: {format_time(elapsed_time)}", 1, "white")
    
    hits_label = LABEL_FONT.render(f"Hits: {targets_pressed}", 1, "white")
    
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = LABEL_FONT.render(f"Speed: {speed} t/s", 1, "white")
    
    accuracy = round(targets_pressed / clicks * 100, 1) if clicks != 0 else 0
    accuracy_label = LABEL_FONT.render(f"Accuracy: {accuracy}%", 1, "white")
    
    win.blit(time_label, (get_middle(time_label), 100))    
    win.blit(speed_label, (get_middle(speed_label), 200))
    win.blit(hits_label, (get_middle(hits_label), 300))
    win.blit(accuracy_label, (get_middle(accuracy_label), 400))
    
    pygame.display.update()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()

def main():
    run = True
    targets = []
    clock = pygame.time.Clock()
    
    target_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()
        
    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)
    
    while run:
        clock.tick(60)
        click = False
        mouse_position = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
                
        for target in targets:
            target.update()
            if target.size <= 0:
                targets.remove(target)
                misses += 1
                
            if click and target.collide(*mouse_position):
                targets.remove(target)
                target_pressed += 1
                
        if misses >= lives:
            end_screen(WIN, elapsed_time, target_pressed, clicks)
            
        draw(WIN, targets)
        draw_top_bar(WIN, elapsed_time, target_pressed, misses)
        pygame.display.update()
        
    pygame.quit()
