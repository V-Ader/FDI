from particle import *
from box import Box

class Simulation(object):

    def __init__(self):
        particles = []
        box = Box(450,450)

    def add_particles(self,number):
        for i in range(number):
            x = random.randrange(400)
            y = random.randrange(400)
            particles.append(Particle(x,y))


    def test_draw(self):
        pass
