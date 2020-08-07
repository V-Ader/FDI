from simulation import *
def param():
    width = int(input("pass width of box: "))
    height = int(input("pass height of box: "))
    number_particles = int(input("pass number of particles in simulation: "))
    speed = float(input("pass maximal speed of particle: "))
    radius = int(input("pass radius of particles: "))
    print(width,height,number_particles)
    sym1 = Simulation(width,height,number_particles,speed,radius)
    sym1.start()

def debug_start():
    sym1 = Simulation(15,15,10,0.05,40)

    sym1.start()

    #sym1.test_colide()
    #sym1.start_bck()

def main():
    #param()
    debug_start()
main()
