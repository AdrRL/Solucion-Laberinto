#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self, l1, l2):
        self.abierta = False
        self.lado1 = l1
        self.lado2 = l2

