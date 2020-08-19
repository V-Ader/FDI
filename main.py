from simulation import *
def param():

    width = int(input("pass width of box <20;70>: "))
    height = int(input("pass height of box <20,70>: "))
    number_particles = int(input("pass number of particles in simulation (ok. 10): "))
    speed = float(input("pass maximal speed of particle (ok. 40): "))
    radius = int(input("pass radius of particles (ok. 10 with minimal window sizes, ok. 40 with maximal): "))
    sym1 = Simulation(width,height,number_particles,speed,radius)
    sym1.start()

def debug_start():
    sym1 = Simulation(70,70,10,50,40)
    #sym1.test_draw()
    sym1.start()

    #sym1.test_colide()
    #sym1.start_bck()

def main():
    param()

main()
