import random
import Mmth

class Particle:
    Particles = []
    def __init__(self,masa,x,y,radius,vel_x,vel_y):
        self.masa = 10
        self.x = x
        self.y = y
        self.radius = radius
        self.vel_x = vel_x
        self.vel_y = vel_y
    def add(self,ilosc):
        for i in range(ilosc):
            x = random.randrange(400)
            y = random.randrange(400)
            radius = 5
            vel_x = 5
            vel_y = 5
            Particle.append(Particle(x,y,radius,vel_x,vel_y))

def collide(p1, p2):
    d = p1.radius + p2.radius

    normal_x = math.abs((p2.x - p1.x) / d)
    normal_y = math.abs((p2.y - p1.y) / d)



#ilosc = int(input("podaj ilosc czasteczek: "))
#for i in czasteczki:
 #   print(i.wspol_X,i.wspol_Y,i.promien,i.pred_pion,i.pred_poz)
#tak wygląda przykładowa zamiana
#for i in range(2):
 #   x = int(input("podaj wartosc X: "))
  #  czasteczki[i].wspol_X = x

#for i in czasteczki:
 #   print(i.wspol_X,i.wspol_Y,i.promien,i.pred_pion,i.pred_poz)

#print("tak")
