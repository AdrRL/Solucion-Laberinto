#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self, l1, l2):
        self.abierta = False
        self.lado1 = l1
        self.lado2 = l2

    def esPuerta(self):
        return True
    
    def estaCerrada(self):
        return not self.abierta
    
    def abrir(self):
        self.abierta=True

    def entrar(self):
        if self.abierta:
            print("Puedes pasar al otro lado")
        else:
            print("La puerta está cerrada")
    


