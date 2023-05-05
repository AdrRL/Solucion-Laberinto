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


    def fabricarHabitacion(self, unNum):
        habitacion = habitacion (unNum)
        return habitacion

    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self, hab1, hab2):
        return Puerta(hab1, hab2)
