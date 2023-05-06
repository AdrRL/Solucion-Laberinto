#!/usr/bin/python
#-*- coding: utf-8 -*-

from Orientacion import Orientacion

class Este(Orientacion):
    
    def ponerElemento(self, unEm, unaHab):
        unaHab.este = unEm
