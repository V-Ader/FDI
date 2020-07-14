import random
import pygame

class Particle:

    def __init__(self,mass,x,y,radius=5,vel_x=5,vel_y=5):
        self.mass = 10
        self.x = x
        self.y = y
        self.radius = radius
        self.vel_x = vel_x
        self.vel_y = vel_y

    def draw(self, window):
        pygame.draw.circle(window,(100,0,10),(self.x, self.y), self.radius, 1)

def collide(p1, p2): #if p1 and p2 are colliding, ret True
    min_sq = (p1.radius + p2.radius)**2
    d = (p1.x - p2.x)**2 + (p1.y - p2.y)**2
    if d > min_sq:
        return False
    else:
        return True

def wall_bounce(p, box): #try to bounce off the walls
    if (p.x - p.radius <= 0) or (p.x  + p.radius >= box.width):
        p.vel_x = -p.vel_x
    if (p.y - p.radius <= 0) or (p.y + p.radius >= box.height):
        p.vel_y = -p.vel_y

def p_bounce(p1, p2):
    pass

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
