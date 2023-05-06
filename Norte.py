#!/usr/bin/python
#-*- coding: utf-8 -*-

from Orientacion import Orientacion

class Norte(Orientacion):
    
    def ponerElemento(self, unEm, unaHab):
        unaHab.norte = unEm
