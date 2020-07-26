from particle import *
from box import Box
from window import Window
import pygame
import random
import time

class Simulation(object):

    def __init__(self,width=500,height=500):
        self.time_limit = 100 #simulation time limit in sec
        self.speed = 0.2 #defines max absolute speed of particle
        self.radius = 40
        self.particles = []
        self.width = width
        self.height = height
        self.box = Box(width, height)

    def add_particles(self,number):
        for i in range(number):
            pos = (random.randrange(50, 400), random.randrange(50, 400))
            vel = (random.randrange(-1, 1) * self.speed ,
                   random.randrange(-1, 1) * self.speed)
            self.particles.append(Particle(pos, vel, self.radius))

    def add_redparticle(self):
        pos = (0+self.radius, 0+self.box.height-self.radius)
        vel = (random.randrange(0, 1) * self.speed, random.randrange(-1,0) * self.speed)
        self.particles.append(RedParticle(pos,vel,self.radius))

    def test_draw(self):
        cps = 1000 # calculations per sec
        timer = 0
        win = Window(self.width,self.height)
        PGun = ParticleGun((0,0),(0,0))
        clock = pygame.time.Clock()


        self.add_redparticle()
        self.add_particles(10)
        run = True
        timer_start = time.time()
        timer_end = time.time()
        while (timer_end-timer_start < self.time_limit and run == True):
            timer += 1
            time.sleep(1/cps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    PGun.acttivated = True
                    PGun.start = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONUP:
                    PGun.acttivated = False
                    PGun.end = pygame.mouse.get_pos()
                    vel = ((PGun.start[0] - PGun.end[0]) / PGun.scale , (PGun.start[1] - PGun.end[1]) / PGun.scale)
                    self.particles.append(Particle(PGun.start, vel, self.radius))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        mouse_pos = pygame.mouse.get_pos()
                        vel = (random.randrange(-self.speed, self.speed), random.randrange(-self.speed, self.speed))
                        self.particles.append(Particle(mouse_pos, vel, self.radius))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        if len(self.particles) > 0:
                            self.particles.pop()



            if PGun.acttivated == True:
                PGun.end = pygame.mouse.get_pos()


            for p in self.particles:
                p.update(self.box, self.particles)

            if timer % 5 == 0:
                win.refresh(win.win, self.box,self.particles, PGun)

            timer_end = time.time()
        pygame.quit()

    def test_colide(self):
        cps = 1000 # calculations per sec
        timer = 0
        win = Window(self.width,self.height)

        PGun = ParticleGun((0,0),(0,0))
        self.add_particles(10)
        run = True
        timer_start = time.time()
        timer_end = time.time()
        while (timer_end-timer_start < self.time_limit and run == True):
            timer += 1
            time.sleep(1/cps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.particles.append(UberParticle(pygame.mouse.get_pos(),(0,0),self.radius))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        mouse_pos = pygame.mouse.get_pos()
                        vel = (
                         random.randrange(-self.speed, self.speed),
                         random.randrange(-self.speed, self.speed))
                        self.particles.append(Particle(mouse_pos, vel, self.radius))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        if len(self.particles) > 0:
                            self.particles.pop()


            for p in self.particles:
                p.update(self.box, self.particles)

            if timer % 5 == 0:
                win.refresh(win.win, self.box,self.particles, PGun)

            timer_end = time.time()
        pygame.quit()
