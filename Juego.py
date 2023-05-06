#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
from Laberinto import Laberinto
from Habitacion import Habitacion
from Pared import Pared
from Puerta import Puerta
from Armario import Armario
from Norte import Norte
from Sur import Sur
from Este import Este
from Oeste import Oeste
from Bomba import Bomba
from Bicho import Bicho
from Agresivo import Agresivo
from Perezoso import Perezoso

class Juego:

    #Constructor equivalente al "initialize" de "Juego"
    def __init__(self):
        self.bichos=[]
        self.hilos={}

    #Se ha modificado la puerta
    def laberinto2habitaciones(self):
        self.laberinto = self.fabricarLaberinto()

        habitacion1 = self.fabricarHabitacion(1)
        habitacion2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuerta(habitacion1, habitacion2)

        habitacion1.ponerNorte(self.fabricarPared())
        habitacion1.ponerEste(self.fabricarPared())
        habitacion1.ponerOeste(self.fabricarPared())
        habitacion1.ponerSur(puerta)

        habitacion2.ponerNorte(puerta)
        habitacion2.ponerEste(self.fabricarPared())
        habitacion2.ponerOeste(self.fabricarPared())
        habitacion2.ponerSur(self.fabricarPared())

    #Creación del laberinto esquematizado para la entrega
    def laberinto4habitaciones(self):
        self.laberinto = self.fabricarLaberinto()

        habitacion1 = self.fabricarHabitacion(1)
        habitacion2 = self.fabricarHabitacion(2)
        habitacion3 = self.fabricarHabitacion(3)
        habitacion4 = self.fabricarHabitacion(4)
        puerta1 = self.fabricarPuerta(habitacion1, habitacion2)
        puerta2 = self.fabricarPuerta(habitacion2, habitacion4)
        puerta3 = self.fabricarPuerta(habitacion3, habitacion4)
        puerta4 = self.fabricarPuerta(habitacion1, habitacion3)

        habitacion1.ponerNorte(self.fabricarPared())
        habitacion1.ponerOeste(self.fabricarPared())
        habitacion1.ponerEste(puerta1)
        habitacion1.ponerSur(puerta4)

        habitacion2.ponerNorte(self.fabricarPared())
        habitacion2.ponerEste(self.fabricarPared())
        habitacion2.ponerOeste(puerta1)
        habitacion2.ponerSur(puerta2)
        self.fabricarArmario(habitacion2)
        for i in habitacion2.hijos:
            if i.esArmario():
                i.agregarHijo(self.fabricarBomba())

        habitacion3.ponerOeste(self.fabricarPared())
        habitacion3.ponerSur(self.fabricarPared())
        habitacion3.ponerEste(puerta3)
        habitacion3.ponerNorte(puerta4)
        self.fabricarArmario(habitacion3)

        habitacion4.ponerEste(self.fabricarPared())
        habitacion4.ponerSur(self.fabricarPared())
        habitacion4.ponerNorte(puerta2)
        habitacion4.ponerOeste(puerta3)


    def fabricarHabitacion(self, unNum):
        habitacion = habitacion (unNum)
        return habitacion

    def fabricarLaberinto(self):
        return Laberinto(1)
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self, hab1, hab2):
        return Puerta(hab1, hab2)
    
    def abrirPuertas(self):
        for elemento in self.laberinto.hijos:
            if elemento.esPuerta:
                elemento.abrir()

    def activarBombas(self):
        for elemento in self.laberinto.hijos:
            if elemento.esBomba:
                elemento.activar()
    
    def agregarBicho(self, unBicho):
        self.bichos.append(unBicho)
    
    def cerrarPuertas(self):
        for elemento in self.laberinto.hijos:
            if elemento.esPuerta:
                elemento.abierta = False
    
    def desactivarBombas(self):
        for elemento in self.laberinto.hijos:
            if elemento.esBomba:
                elemento.desactivar()

    def fabricarArmario(self, unCont):
        numero = len(unCont.hijos) + 1
        armario = Armario(numero)
        armario.ponerElemento(self.fabricarNorte(), self.fabricarPared())
        armario.ponerElemento(self.fabricarEste(), self.fabricarPared())
        armario.ponerElemento(self.fabricarOeste(), self.fabricarPared())

        armario.agregarOrientacion(self.fabricarNorte(), self.fabricarSur(), self.fabricarEste(), self.fabricarOeste())

        puerta = Puerta(armario, unCont)
        armario.ponerElemento(Sur(), puerta)

        unCont.agregarHijo(armario)

    def fabricarModoAgresivo(self):
        return Agresivo()

    def fabricarBichoAgresivo(self):
        bicho = Bicho()
        bicho.modo = self.fabricarModoAgresivo()
        bicho.vidas = 10
        bicho.poder = 10
        return bicho
    
    def fabricarModoPerezoso(self):
        return Perezoso()
    
    def fabricarBichoPerezoso(self):
        bicho = Bicho()
        bicho.modo = self.fabricarModoPerezoso()
        bicho.vidas = 10
        bicho.poder = 5
        return bicho

    def fabricarBomba():
        return Bomba()
    
    def fabricarEste():
        return Este()
    def fabricarOeste():
        return Oeste()
    def fabricarNorte():
        return Norte()
    def fabricarSur():
        return Sur()