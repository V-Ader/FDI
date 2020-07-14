from particle import Particle
from box import Box
from window import Window
import pygame
import random

class Simulation(object):

    def __init__(self):
        self.particles = []
        self.box = Box(450,450)

    def add_particles(self,number):
        for i in range(number):
            x = random.randrange(400)
            y = random.randrange(400)
            self.particles.append(Particle(x,y))


    def test_draw(self):
        win = Window()
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

            print("*")
            for p in self.particles:
                p.update(self.box)
                print(p.x, p.y)

            win.refresh(win.win, self.box,self.particles)
