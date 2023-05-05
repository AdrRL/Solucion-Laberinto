#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
from Laberinto import Laberinto
from Habitacion import Habitacion
from Pared import Pared
from Puerta import Puerta

class Juego:

    #Constructor equivalente al "initialize" de "Juego"
    def __init__(self):
        self.bichos=[]
        self.hilos={}

    #Se ha modificado la puerta
    def laberinto2habitaciones(self):
        self.laberinto = self.fabricarLaberinto()

        habitacion1 = self.fabricarHabitacion(1)
        habitacion2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuerta(habitacion1, habitacion2)

        habitacion1.ponerNorte(self.fabricarPared())
        habitacion1.ponerEste(self.fabricarPared())
        habitacion1.ponerOeste(self.fabricarPared())
        habitacion1.ponerSur(puerta)

        habitacion2.ponerNorte(puerta)
        habitacion2.ponerEste(self.fabricarPared())
        habitacion2.ponerOeste(self.fabricarPared())
        habitacion2.ponerSur(self.fabricarPared())

    #Creación del laberinto esquematizado para la entrega
    def laberinto4habitaciones(self):
        self.laberinto = self.fabricarLaberinto()

        habitacion1 = self.fabricarHabitacion(1)
        habitacion2 = self.fabricarHabitacion(2)
        habitacion3 = self.fabricarHabitacion(3)
        habitacion4 = self.fabricarHabitacion(4)
        puerta1 = self.fabricarPuerta(habitacion1, habitacion2)
        puerta2 = self.fabricarPuerta(habitacion2, habitacion4)
        puerta3 = self.fabricarPuerta(habitacion3, habitacion4)
        puerta4 = self.fabricarPuerta(habitacion1, habitacion3)

        habitacion1.ponerNorte(self.fabricarPared())
        habitacion1.ponerOeste(self.fabricarPared())
        habitacion1.ponerEste(puerta1)
        habitacion1.ponerSur(puerta4)

        habitacion2.ponerNorte(self.fabricarPared())
        habitacion2.ponerEste(self.fabricarPared())
        habitacion2.ponerOeste(puerta1)
        habitacion2.ponerSur(puerta2)

        habitacion3.ponerOeste(self.fabricarPared())
        habitacion3.ponerSur(self.fabricarPared())
        habitacion3.ponerEste(puerta3)
        habitacion3.ponerNorte(puerta4)

        habitacion4.ponerEste(self.fabricarPared())
        habitacion4.ponerSur(self.fabricarPared())
        habitacion4.ponerNorte(puerta2)
        habitacion4.ponerOeste(puerta3)
        

    def fabricarHabitacion(self, unNum):
        habitacion = habitacion (unNum)
        return habitacion

    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self, hab1, hab2):
        return Puerta(hab1, hab2)
