import math
import pygame
from settings import WIDTH

def format_time(secs):
    milli = math.floor(int(secs*1000%1000)/10)
    seconds = int(round(secs%60, 1))
    minutes = int(secs // 60)
    return f"{minutes:02d}:{seconds:02d}.{milli}"

def get_middle(surface):
    return WIDTH // 2 - surface.get_width() // 2
