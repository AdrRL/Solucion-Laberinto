#!/usr/bin/python
#-*- coding: utf-8 -*-

from Contenedor import Contenedor
from Habitacion import Habitacion

class Laberinto(Contenedor):

    def __init__(self, num):
        super().__init__(num)

    def agregarHabitacion(self, unaHab):
        self.agregarHijo(unaHab)

    def numeroHabitaciones(self):
        contador = 0
        for hijo in self.hijos:
            if hijo.esHabitacion:
                contador += 1
        return contador

    def obtenerHabitacion(self, unNum):
        for hijo in self.hijos:
            if hijo.esHabitacion:
                if hijo.num == unNum:
                    return hijo