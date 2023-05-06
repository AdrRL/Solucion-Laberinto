#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    
    def esPared(self):
        return True
    
    def entrar(self):
        print("Has chocado con una pared")
