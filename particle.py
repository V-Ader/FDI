import random
import pygame

class Particle:

    def __init__(self,x,y,mass=10,radius=20,vel_x=5,vel_y=5):
        self.x = x
        self.y = y
        self.mass = 10
        self.radius = radius
        self.vel_x = vel_x
        self.vel_y = vel_y

    def draw(self, window):
        pygame.draw.circle(window,(100,0,10),(self.x, self.y), self.radius, 1)

    def wall_bounce(self, box): #try to bounce off the walls
        if (self.x - self.radius <= 0) or (self.x  + self.radius >= box.width):
            self.vel_x = -self.vel_x
        if (self.y - self.radius <= 0) or (self.y + self.radius >= box.height):
            self.vel_y = -self.vel_y

    def update(self, box):

        self.wall_bounce(box)
        self.x += self.vel_x
        self.y += self.vel_y



def collide(p1, p2): #if p1 and p2 are colliding, ret True
    min_sq = (p1.radius + p2.radius)**2
    d = (p1.x - p2.x)**2 + (p1.y - p2.y)**2
    if d > min_sq:
        return False
    else:
        return True



def p_bounce(p1, p2):
    pass
