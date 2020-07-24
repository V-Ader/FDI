import random
import pygame
import math
import time

#zadziala
#zmiana11
class Particle:

    def __init__(self,pos,vel=(5,5),mass=1,radius=40):
        self.x, self.y = pos
        self.vel_x, self.vel_y = vel
        self.mass = mass
        self.radius = radius


    def draw(self, window):
        pygame.draw.circle(window,(100,0,10),(int(self.x), int(self.y)), self.radius, 1)

    def wall_bounce(self, box): #try to bounce off the walls
        if (self.x - self.radius <= 0):
            self.x = self.radius + 1
            self.vel_x = -self.vel_x
        if (self.x  + self.radius >= box.width):
            self.x = box.width - self.radius - 1
            self.vel_x = -self.vel_x
        if (self.y - self.radius <= 0):
            self.y = self.radius + 1
            self.vel_y = -self.vel_y
        if (self.y + self.radius >= box.height):
            self.y = box.height - self.radius - 1
            self.vel_y = -self.vel_y

    def p_bounce(self, particles):
        for i in range(len(particles)):
            if collide(self, particles[i]):
                angle = math.atan2(particles[i].y - self.y, particles[i].x - self.x) #calc angle
                v1p = self.vel_x * math.cos(angle) + self.vel_y * math.sin(angle)   #calc rotated x_vel of self
                v2p = particles[i].vel_x * math.cos(angle) + particles[i].vel_y * math.sin(angle)   #calc rotated x_vel of the other one

                v1q = -self.vel_x * math.sin(angle) + self.vel_y * math.cos(angle)  #calc rotated y_vel of self
                v2q = -particles[i].vel_x * math.sin(angle) + particles[i].vel_y * math.cos(angle)  ##calc rotated y_vel of the other one

                v1p, v2p = v2p, v1p #

                self.vel_x = v1p * math.cos(-angle) + v1q * math.sin(-angle) # rotate back self
                particles[i].vel_x = v2p * math.cos(-angle) + v2q * math.sin(-angle)

                self.vel_y = -v1p * math.sin(-angle) + v1q * math.cos(-angle) # rotate back self
                particles[i].vel_y = -v2p * math.sin(-angle) + v2q * math.cos(-angle)


    def separate(self, particles):
        #p - part
        for i in range(len(particles)):
            if collide(self, particles[i]):
                d = math.sqrt((self.x - particles[i].x)**2 + (self.y - particles[i].y)**2)
                s = (d - self.radius - particles[i].radius) / 2

                self.x += s * (self.x - particles[i].x) / d #move self obj
                self.y += s * (self.y - particles[i].y) / d

                particles[i].x += s * (self.x - particles[i].x) / d #move the other obj
                particles[i].y += s * (self.y - particles[i].y) / d


    def update(self, box, particles):
        self.wall_bounce(box)
        self.p_bounce(particles)
        self.separate(particles)
        self.x += self.vel_x
        self.y += self.vel_y

class RedParticle(Particle):
    def __init__(self, pos,vel):
        super().__init__(pos,vel)
        self.time_list =[]
        self.road = []
    def draw(self, window):
        pygame.draw.circle(window, (255, 0, 0), (int(self.x), int(self.y)), self.radius, 0)

    def p_bounce(self, particles):
        start = time.time()
        for i in range(len(particles)):
            if collide(self, particles[i]):
                angle = math.atan2(particles[i].y - self.y, particles[i].x - self.x) #calc angle
                v1p = self.vel_x * math.cos(angle) + self.vel_y * math.sin(angle)   #calc rotated x_vel of self
                v2p = particles[i].vel_x * math.cos(angle) + particles[i].vel_y * math.sin(angle)   #calc rotated x_vel of the other one

                v1q = -self.vel_x * math.sin(angle) + self.vel_y * math.cos(angle)  #calc rotated y_vel of self
                v2q = -particles[i].vel_x * math.sin(angle) + particles[i].vel_y * math.cos(angle)  ##calc rotated y_vel of the other one

                v1p, v2p = v2p, v1p #

                self.vel_x = v1p * math.cos(-angle) + v1q * math.sin(-angle) # rotate back self
                particles[i].vel_x = v2p * math.cos(-angle) + v2q * math.sin(-angle)

                self.vel_y = -v1p * math.sin(-angle) + v1q * math.cos(-angle) # rotate back self
                particles[i].vel_y = -v2p * math.sin(-angle) + v2q * math.cos(-angle)
                end = time.time()
                outcome = end - start
                self.time_list.append(outcome)


    def separate(self, particles):
        #p - part
        for i in range(len(particles)):
            if collide(self, particles[i]):
                d = math.sqrt((self.x - particles[i].x)**2 + (self.y - particles[i].y)**2)
                s = (d - self.radius - particles[i].radius) / 2

                self.x += s * (self.x - particles[i].x) / d #move self obj
                self.y += s * (self.y - particles[i].y) / d

                particles[i].x += s * (self.x - particles[i].x) / d #move the other obj
                particles[i].y += s * (self.y - particles[i].y) / d
                self.road.append(s)


    def update(self, box, particles):
        self.wall_bounce(box)
        self.p_bounce(particles)
        self.separate(particles)
        self.x += self.vel_x
        self.y += self.vel_y

class ParticleGun:
    def __init__(self,start, end):
        self.start = start
        self.end = end
        self.color = (0,255,0)
        self.acttivated = False
        self.scale = 10

    def draw(self, window):
        if self.acttivated != False:
            pygame.draw.line(window, self.color, self.start, self.end,5)

def overlap(p1, p2):
        k=0
        if p1.x == p2.x and p1.y == p2.y:
            return False

        min_sq = (p1.radius + p2.radius)
        d = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
        if d - k > min_sq:
            return False
        else:
            return True

def collide(p1, p2): #if p1 and p2 are colliding, ret True
    #k = p1.radius/10
    k=0
    if p1.x == p2.x and p1.y == p2.y:
        return False

    min_sq = (p1.radius + p2.radius)
    d = math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)
    if d - k > min_sq:
        return False
    else:
        return True
