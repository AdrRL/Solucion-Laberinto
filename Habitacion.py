#!/usr/bin/python
#-*- coding: utf-8 -*-

from Contenedor import Contenedor

class Habitacion(Contenedor):
    
    def __init__(self, num):
        super().__init__(num)
    

    def entrar(self):
        print("Estás en la habitacion", self.num)

    def esHabitacion(self):
        return True

