#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
import Laberinto

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
            self.laberinto = json.load(file)


    def laberinto2habitaciones(self):
        Laberinto = new Laberinto()
        pass

