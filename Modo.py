#!/usr/bin/python
#-*- coding: utf-8 -*-

class Modo:

    def esAgresivo(self):
        return False
    
    def esPerezoso(self):
        return False
    
    def dormir(self):
        print("Estoy durmiendo")
    
    def caminar(self, unBicho):
        print("Estoy caminando")    #No se ha implementado la funcionalidad en sí, simplemente la estructura (y mensaje)
    
    def atacar(self, unBicho):
        print("Estoy atacando")     #No se ha implementado la funcionalidad en sí, simplemente la estructura (y mensaje)

    def actua(self, unBicho):
        self.dormir
        self.caminar(unBicho)
        self.atacar(unBicho)
