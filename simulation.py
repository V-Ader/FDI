from particle import Particle,ParticleGun
from box import Box
from window import Window
import pygame
import random

class Simulation(object):

    def __init__(self,width=500,height=500):
        self.speed = 2
        self.particles = []
        self.width = width
        self.height = height
        self.box = Box(width,height)

    def add_particles(self,number):
        for i in range(number):
            pos = (random.randrange(50, 400), random.randrange(50, 400))
            vel = (random.randrange(
                -self.speed, self.speed),
                random.randrange(-self.speed, self.speed))
            self.particles.append(Particle(pos, vel))


    def test_draw(self):
        win = Window(self.width,self.height)
        PGun = ParticleGun((0,0),(0,0))
        clock = pygame.time.Clock()

        self.add_particles(5)
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    PGun.acttivated = True
                    PGun.start = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONUP:
                    PGun.acttivated = False
                    PGun.end = pygame.mouse.get_pos()
                    vel = ((PGun.start[0] - PGun.end[0]) / PGun.scale , (PGun.start[1] - PGun.end[1]) / PGun.scale)
                    self.particles.append(Particle(PGun.start, vel))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        mouse_pos = pygame.mouse.get_pos()
                        vel = (random.randrange(-self.speed, self.speed), random.randrange(-self.speed, self.speed))
                        self.particles.append(Particle(mouse_pos, vel))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        if len(self.particles) > 0:
                            self.particles.pop()



            if PGun.acttivated == True:
                PGun.end = pygame.mouse.get_pos()


            for p in self.particles:
                p.update(self.box, self.particles)

            win.refresh(win.win, self.box,self.particles, PGun)
