#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        super().__init__()
        self.activa = False

    def activar(self):
        self.activa = True
        print("Bomba activada")
    
    def desactivar(self):
        self.activa = False
        print("Bomba desactivada")
    
    def entrar(self):
        if self.activa:
            print("Bomba ha explotado")
        else:
            print("Bomba desactivada, no pasa nada")
    
    def esBomba(self):
        return True



