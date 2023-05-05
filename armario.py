#!/usr/bin/python
#-*- coding: utf-8 -*-

from Contenedor import Contenedor

class armario(Contenedor):
    def __init__(self, num):
        super().__init__(num)

    def entrar(self):
        print("Estás en el armario", self.num)
    
    def esArmario(self):
        return True
