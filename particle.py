import random
import pygame

class Particle:

    def __init__(self,pos,vel=(5,5),mass=10,radius=20):
        self.x, self.y = pos
        self.vel_x, self.vel_y = vel
        self.mass = 10
        self.radius = radius


    def draw(self, window):
        pygame.draw.circle(window,(100,0,10),(self.x, self.y), self.radius, 1)

    def wall_bounce(self, box): #try to bounce off the walls
        if (self.x - self.radius <= 0) or (self.x  + self.radius >= box.width):
            self.vel_x = -self.vel_x
        if (self.y - self.radius <= 0) or (self.y + self.radius >= box.height):
            self.vel_y = -self.vel_y

    def p_bounce(self, p2):
        pass

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
