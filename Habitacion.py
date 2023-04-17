#!/usr/bin/python
#-*- coding: utf-8 -*-

from Contenedor import Contenedor

class Habitacion(Contenedor):
    
    def __init__(self, num):
        self.numero = num
    
    def ponerNorte(self, elemento):
        self.norte = elemento
    
    def ponerSur(self, elemento):
        self.sur = elemento
    
    def ponerEste(self, elemento):
        self.este = elemento
    
    def ponerOeste(self, elemento):
        self.oeste = elemento

