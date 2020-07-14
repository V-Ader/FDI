from particle import Particle
from box import Box
from window import Window
import pygame
import random

class Simulation(object):

    def __init__(self,width=500,height=500):
        self.particles = []
        self.width = width
        self.height = height
        self.box = Box(width,height)

    def add_particles(self,number):
        for i in range(number):
            pos = (random.randrange(50, 400), random.randrange(50, 400))
            vel = (random.randrange(-10, 10), random.randrange(-10, 10))
            self.particles.append(Particle(pos, vel))


    def test_draw(self):
        win = Window(self.width,self.height)
        clock = pygame.time.Clock()
        clock.tick(5)

        self.add_particles(10)
        run = True
        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    vel = (random.randrange(-10, 10), random.randrange(-10, 10))
                    self.particles.append(Particle(mouse_pos, vel))

            print("*")
            for p in self.particles:
                p.update(self.box)

            win.refresh(win.win, self.box,self.particles)
