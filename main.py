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
def main():
    param()
    #sym1 = Simulation(70,70)

    #sym1.start()

    #sym1.test_colide()
    #sym1.start_bck()
main()
