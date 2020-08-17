import random
import pygame
import math
import time

class Particle:

    def __init__(self,pos,vel,radius):
        self.x, self.y = pos
        self.pos = pos
        self.vel_x, self.vel_y = vel
        self.radius = radius


    def draw(self, window):
        pygame.draw.circle(window,(0,0,255),(int(self.x), int(self.y)), self.radius, 0)

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
                angle = -math.atan2( self.y - particles[i].y, self.x - particles[i].x ) #calc angle
                v1p = self.vel_x * math.cos(angle) - self.vel_y * math.sin(angle)   #calc rotated x_vel of self
                v2p = particles[i].vel_x * math.cos(angle) - particles[i].vel_y * math.sin(angle)   #calc rotated x_vel of the other one

                v1q = self.vel_x * math.sin(angle) + self.vel_y * math.cos(angle)  #calc rotated y_vel of self
                v2q = particles[i].vel_x * math.sin(angle) + particles[i].vel_y * math.cos(angle)  ##calc rotated y_vel of the other one

                v1p, v2p = v2p, v1p #

                self.vel_x = v1p * math.cos(-angle) - v1q * math.sin(-angle) # rotate back self
                particles[i].vel_x = v2p * math.cos(-angle) - v2q * math.sin(-angle)

                self.vel_y = v1p * math.sin(-angle) + v1q * math.cos(-angle) # rotate back self
                particles[i].vel_y = v2p * math.sin(-angle) + v2q * math.cos(-angle)



    def separate(self, particles):
        #p - part
        for i in range(len(particles)):
            if collide(self, particles[i]):
                d = math.sqrt((self.x - particles[i].x)**2 + (self.y - particles[i].y)**2)
                s = (d - self.radius - particles[i].radius) / 2 + (1/10 * self.radius)

                self.x -= s * (self.x - particles[i].x) / d #move self obj
                self.y -= s * (self.y - particles[i].y) / d

                particles[i].x += s * (self.x - particles[i].x) / d #move the other obj
                particles[i].y += s * (self.y - particles[i].y) / d


    def calculate(self, box, particles):
        self.wall_bounce(box)
        self.p_bounce(particles)
        self.separate(particles)

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y


class RedParticle(Particle):

    def __init__(self, pos,vel, radius):
        super().__init__(pos,vel,radius)
        self.time_list = [0]
        self.particle_velocity = []
        self.index = 0
        self.distance_list = []
        self.time_bbounces = []
        self.begin_simulation = time.time()

    def draw(self, window):
        pygame.draw.circle(window, (255, 0, 0), (int(self.x), int(self.y)), self.radius, 0)

    def p_bounce(self, particles):
        for i in range(len(particles)):
            if collide(self, particles[i]):
                speed = math.sqrt(self.vel_x * self.vel_x + self.vel_y * self.vel_y)
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

             #   d = math.sqrt((self.x - particles[i].x) ** 2 + (self.y - particles[i].y) ** 2)
             #   s = (d - self.radius - particles[i].radius) / 2
                outcome = end - self.begin_simulation
                timeee = outcome - self.time_list[self.index]
                distance = speed * timeee
             #   print(outcome, timeee, distance)
                self.time_list.append(outcome)
               # print(particles[self.index])
                self.distance_list.append(distance)
                self.time_bbounces.append(timeee)
                self.particle_velocity.append(speed)
                self.index += 1


class UberParticle(Particle):
    def __init__(self, pos,vel, radius):
        super().__init__(pos,vel,radius)
        self.particles = []

    def calculate(self, box, particles):
        self.particels = particles
        self.wall_bounce(box)
        self.p_bounce(particles)
        self.separate(particles)

    def move(self):
        self.x,self.y =pygame.mouse.get_pos()

    def draw(self,window):
        pygame.draw.circle(window,(100,0,10),(int(self.x), int(self.y)), self.radius, 1)
        for p in self.particles:
            if collide(self, p):
                pygame.draw.line(window, (0,200,0),(int(self.x), int(self.y)),(int(p.x), int(p.y)))

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

def collide(p1, p2,debugmode=1): #if p1 and p2 are colliding, ret True


    if p1.x == p2.x and p1.y == p2.y:
        return False

    min_sq = (p1.radius + p2.radius)**2
    dist =(p1.x - p2.x)**2 + (p1.y - p2.y)**2
    d = 1/10 * p1.radius

    if (2 * p1.radius > math.sqrt(dist)):
         if debugmode == 1:
             print("Error - collected data to be deleted", time.time())
         return overlap(p1, p2)

    if (2 * p1.radius < math.sqrt(dist)) and (math.sqrt(dist) <= 2 * p1.radius + d):
        return True
    else:
        dist2 =(p1.x + p1.vel_x - p2.x - p2.vel_x)**2 + (p1.y + p1.vel_y - p2.y - p2.vel_y)**2
        if (2 * p1.radius < math.sqrt(dist2)) and (math.sqrt(dist2) <= 2 * p1.radius + d):
            return True
        else:
            return False

def overlap(p1, p2): #if p1 and p2 are colliding, ret True
    if p1.x == p2.x and p1.y == p2.y:
        return False

    min_sq = (p1.radius + p2.radius)**2
    d =(p1.x - p2.x)**2 + (p1.y - p2.y)**2
    if d > min_sq:
        return False
    else:
        return True

def is_separated(particles, p1):
    for i in range(len(particles)):
        if collide(p1,particles[i],0):
            print("//")
            return False
    return True


def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
