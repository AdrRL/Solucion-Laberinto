#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
from Laberinto import Laberinto
from Habitacion import Habitacion
from Pared import Pared
from Puerta import Puerta

class Juego:

        #Código que se recibirá
        #{
	    #    "laberinto":[
		#        {"tipo":"habitacion","num":1,"hijos":[
		#	        {"tipo":"tunel"}
		#        ]},
		#        {"tipo":"habitacion","num":2,"hijos":[
		#	        {"tipo":"armario", "num":1, "hijos":[]}
		#        ]}
	    #    ],
	    #"puertas":[[1,"Sur",2,"Norte"]],
	    #"bichos":[]
        #}


    def __init__(self, archivo):
        self.conf = archivo
        with open(self.conf, 'r', encoding='utf8') as file:
            self.archivo = json.load(file)
        self.bichos=[]
        self.hilos={}


    def laberinto2habitaciones(self):
        self.laberinto = self.fabricarLaberinto()

        habitacion1 = self.fabricarHabitacion(1)
        habitacion2 = self.fabricarHabitacion(2)

        habitacion1.ponerNorte(self.fabricarPared())
        habitacion1.ponerEste(self.fabricarPared())
        habitacion1.ponerOeste(self.fabricarPared())
        habitacion1.ponerSur(self.fabricarPuerta(habitacion1, habitacion2))

        habitacion2.ponerNorte(self.fabricarPuerta(habitacion1, habitacion2))
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
