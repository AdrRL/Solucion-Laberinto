#!/usr/bin/python
#-*- coding: utf-8 -*-


class Bicho():
    def __init__(self):
        self.vidas = 10     #Datos de ejemplo
        self.poder = 1
        self.modo = None

    def esAgresivo(self):
        return self.modo.esAgresivo
    
    def esPerezoso(self):
        return self.modo.esPerezoso

    def estaVivo(self): #Como es obvio no se ha tenido en cuenta la clase Estado
        return self.vidas > 0
    
    def puedeActuar(self):
        self.modo.actua(self)
    
    def quitarVidas(self, unNum):
        self.vidas = self.vidas - unNum