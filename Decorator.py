#!/usr/bin/python
#-*- coding: utf-8 -*-

from Hoja import Hoja

class Decorator(Hoja):
    
    def __init__(self):
        super().__init__()
        self.component = None
