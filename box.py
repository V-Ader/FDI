import pygame
import math

class Box:
    # axes
    # 0 - - - - -> width
    # |
    # |
    # |
    # V
    # height
    def __init__(self, width=200, height=200):
        self.width = max(200, width)
        self.height = max(200, height)

    def draw(self,window):
        pygame.draw.rect(window,(100,100,100),(0,0,self.width,self.height))
