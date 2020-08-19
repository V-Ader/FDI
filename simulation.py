from timeit import default_timer as timer
from particle import *
from box import Box
from window import Window
import pygame
import random
import time
import math

class Simulation(object):

    def __init__(self,width,height,number_particles,speed,radius):
        self.cps = 1000 # calculations per sec

        self.time_limit = 10 #simulation time limit in sec
        self.speed = speed/self.cps #defines max absolute speed of particle
        self.radius = radius
        self.particles = []
        self.width = max(200, width*10)
        self.height = max(200,height*10)
        self.box = Box(self.width, self.height)
        self.number_particles = min(number_particles, 1/4 * (self.box.width * self.box.height))
        self.index = 0

        #poniżej macie parametry do kroku czasu itd,
        self.RedPartSpeed = 0
        self.k = min(self.width,self.height)
        self.time_step = 0
        self.punkt1e = 0

        self.scale = 1 / (min(self.width, self.height) * speed)

    def add_particles(self,number):
        margin = 50
        number = number - 1
        ok = False
        for i in range(number):
            vel = (random.randrange(-10, 10) * self.speed,
                   random.randrange(-10, 10) * self.speed)
            ok = False
            while not ok:
                pos = (random.randrange(self.radius + margin, self.width - self.radius - margin),
                       random.randrange(self.radius + margin, self.height - self.radius - margin))
                if is_separated(self.particles, Particle(pos, vel, self.radius)):
                    ok = True
            self.particles.append(Particle(pos, vel, self.radius))

    def add_redparticle(self):
        margin = 50
        pos = (0+self.radius + margin , 0+self.box.height-self.radius-margin)
        vel = (random.randrange(0,10)*self.speed, -random.randrange(0,10)*self.speed)
        self.particles.append(RedParticle(pos,vel,self.radius))

        #nie wiem czy dodać to do jakiejś funkcji czy coś
        self.RedPartSpeed = math.sqrt((vel[0] * vel[0]) + (vel[1] * vel[1]))
        self.time_step = 1/(self.k * self.RedPartSpeed)
        self.punkt1e = self.time_step * self.number_particles

    def start_bck(self):
        timer = 0

        self.add_redparticle()
        self.add_particles(10)
        run = True

        timer_start = time.time()
        timer_end = time.time()
        while (timer_end-timer_start < self.time_limit and run == True):
            timer += 1
            time.sleep(1/self.cps)

            for p in self.particles:
                p.calculate(self.box, self.particles)

            for p in self.particles:
                p.move()

            timer_end = time.time()

    def start(self):
        timer = 0
        win = Window(self.width,self.height)

        self.add_redparticle()
        self.add_particles(self.number_particles)
        run = True
        timer_start = time.time()
        timer_end = time.time()
        while (timer_end-timer_start < self.time_limit and run == True):
            timer += 1
            time.sleep(1/self.cps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            for p in self.particles:
                p.calculate(self.box, self.particles)

            for p in self.particles:
                p.move()

            if timer % 5 == 0:
                win.refresh(win.win, self.box,self.particles)

            timer_end = time.time()

        result1 = "result_time_list"
        result2 = "result_particle_velocity"
        result3 = "result_distance_list"
        p = open(f'result_simulation_{self.time_limit}.txt', 'a')
        p.write(result1)

        for i in range(len(self.particles[0].time_list)):
            p.write('\n')
            p.write(str(self.particles[0].time_list[i]))  # zapisanie czasu między zderzeniami

        p.write('\n')
        p.write(result2)

        for i in range(len(self.particles[0].particle_velocity)):
            p.write('\n')
            p.write(str(self.particles[0].particle_velocity[i]))  # zapisanie prędkości cząsteczki między zderzeniami

        p.write('\n')
        p.write(result3)

        for i in range(len(self.particles[0].distance_list)):
            p.write('\n')
            p.write(str(self.particles[0].distance_list[i]))  # zapisanie przebytej drogi między zderzeniami

        p.close()
        pygame.quit()
