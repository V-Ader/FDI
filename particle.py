import random
class Particle:
    czasteczki = []
    def __init__(self,masa,wspol_X,wspol_Y,promien,pred_poz,pred_pion):
        self.masa = 10
        self.wspol_X = wspol_X
        self.wspol_Y = wspol_Y
        self.promien = promien
        self.pred_poz = pred_poz
        self.pred_pion = pred_pion
    def dodaj(self,ilosc):
        for i in range(ilosc):
            wspol_X = random.randrange(400)
            wspol_Y = random.randrange(400)
            promien = 5
            pred_poz = 5
            pred_pion = 5
            czasteczki.append(Particle(wspol_X, wspol_Y, promien, pred_poz, pred_pion))

ilosc = int(input("podaj ilosc czasteczek: "))
for i in czasteczki:
    print(i.wspol_X,i.wspol_Y,i.promien,i.pred_pion,i.pred_poz)
#tak wygląda przykładowa zamiana
for i in range(2):
    x = int(input("podaj wartosc X: "))
    czasteczki[i].wspol_X = x

for i in czasteczki:
    print(i.wspol_X,i.wspol_Y,i.promien,i.pred_pion,i.pred_poz)

print("tak")