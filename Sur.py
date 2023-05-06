#!/usr/bin/python
#-*- coding: utf-8 -*-

from Orientacion import Orientacion

class Sur(Orientacion):
    
    def ponerElemento(self, unEm, unaHab):
        unaHab.sur = unEm
