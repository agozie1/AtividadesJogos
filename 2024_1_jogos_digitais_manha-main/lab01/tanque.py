from random import seed
from random import random
from random import randint

class Tank(object):
    def __init__(self, name):
        self.name = name    #nome do tanque
        self.alive = True   #para saber se o tanque está vivo ou não
        self.ammo = 5       #para armazenar a munição do tanque
        self.armor = 60     #para armazenar a armadura do tanque

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEADE)" % self.name

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")
    
    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <= 0:
            self.explode()

    def fire_at(self, enemy):
        if self.ammo >=1: #verifica a qtde de balas
            self.ammo -=1 #subtrai uma bala ref a um tiro
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")


meuTanque1 = Tank("nome1")
meuTanque2 = Tank("nome2")
meuTanque3 = Tank("nome3")
meuTanque4 = Tank("nome4")
meuTanque5 = Tank("nome5")


lista =[meuTanque1, meuTanque2, meuTanque3, meuTanque4, meuTanque5]

numero1 = randint( 0 ,len(lista) -1 )
numero2 = randint( 0 ,len(lista)-1 )

lista[numero1].fire_at( lista[numero2] )


        
