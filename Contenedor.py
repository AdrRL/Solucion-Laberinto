#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa
import random

class Contenedor(ElementoMapa):
    def __init__(self, num):
        super()
        self.hijos = []
        self.orientaciones = []     #En la solución actual ya no es así
        self.num = num
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None

    def agregarHijo(self, unEm):
        unEm.padre = self
        self.hijos.append(unEm)

    def agregarOrientacion(self, unaOr):
        self.orientaciones.append(unaOr)

    def orientacionAleatoria(self):
        return random.choice(self.orientaciones)

    def ponerElemento(self, unaOr, unEm):
        unaOr.ponerElemento(unEm, self)
    
