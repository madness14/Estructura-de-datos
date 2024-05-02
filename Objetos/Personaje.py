class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre, ':', sep='')
        print('Fuerza:', self.fuerza)
        print('Inteligencia:', self.inteligencia)
        print('Defensa:', self.defensa)
        print('Vida', self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        
    def esta_vivo(self):
        return self.vida > 0 
        
    def morir(self):
        self.vida = 0
        print(self.nombre, 'ha muerto :c')
        
    def damage(self, enemigo):
        return self.fuerza - enemigo.defensa    
    
    def atacar(self, enemigo):
        damage = self.damage(enemigo)
        enemigo.vida = enemigo.vida - damage
        print(self.nombre, 'ha hecho', damage, 'puntos de dano a', enemigo.nombre)
        if enemigo.esta_vivo(): 
            print('La vida de', enemigo.nombre, 'es', enemigo.vida)
        else:
            enemigo.morir()

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input('Elige un arma: (1) Acero Valyrio, dam 8. (2) Matadragones, dam 10.\n'))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print('Error')

    def atributos(self):
        super().atributos()
        print('Espada:', self.espada)
    
    def damage(self, enemigo):
        return self.fuerza*self.espada - self.defensa

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    
    def atributos(self):
        super().atributos()
        print('Libro:', self.libro)
    
    def damage(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

def combate(j1, j2):
    turno = 1
    while j1.esta_vivo and j2.esta_vivo():
        print('\nTurno,', turno)
        print('Accion de ', j1.nombre, ':', sep='')
        j1.atacar(j2)
        print('Accion de ', j2.nombre, ':', sep='')
        j2.atacar(j1)
        turno +=1
    if j1.esta_vivo():
        print('\nHa ganado ', j1.nombre)
    elif j2.esta_vivo():
        print('\nHa ganado ', j2.nombre)
    else:
        print('\nEmpate')

najimi = Personaje('Najimi Osana', 20, 20, 5, 100)
#mi_enemigo = Personaje('Komi-san', 8, 5, 3, 5)
guts = Guerrero('Guts', 20, 10, 10, 100, 5)
kokichi = Mago('Kokichi', 20, 15, 10, 100, 5)
#najimi.atributos()
#guts.atributos()
#kokichi.atributos()

combate(kokichi, guts)

#najimi.atacar(guts)
#guts.atacar(kokichi)
#kokichi.atacar(najimi)

#guts.cambiar_arma()
#print(mi_personaje.damage(mi_enemigo))
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()
#mi_personaje.fuerza = 15
#mi_personaje.morir()
#print(mi_personaje.esta_vivo())
#mi_personaje.subir_nivel(1, 2, 0)
#mi_personaje.atributos()