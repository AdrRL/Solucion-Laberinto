#!/usr/bin/python
#-*- coding: utf-8 -*-

from Orientacion import Orientacion

class Oeste(Orientacion):
    
    def ponerElemento(self, unEm, unaHab):
        unaHab.oeste = unEm
