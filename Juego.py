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

    #Se ha modificado la puerta, y reducido las creaciones de paredes por defecto
    def laberinto2habitaciones(self):
        self.laberinto = self.fabricarLaberinto()

        habitacion1 = self.fabricarHabitacion(1)
        habitacion2 = self.fabricarHabitacion(2)
        puerta = self.fabricarPuerta(habitacion1, habitacion2)

        habitacion1.ponerElemento(self.fabricarSur(), puerta)
        habitacion2.ponerElemento(self.fabricarNorte(), puerta)

        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)


    #Creación del laberinto esquematizado para la entrega
    def laberinto4habitaciones(self):
        self.laberinto = self.fabricarLaberinto()

        habitacion1 = self.fabricarHabitacion(0)
        habitacion2 = self.fabricarHabitacion(1)
        habitacion3 = self.fabricarHabitacion(2)
        habitacion4 = self.fabricarHabitacion(3)
        puerta1 = self.fabricarPuerta(habitacion1, habitacion2)
        puerta2 = self.fabricarPuerta(habitacion2, habitacion4)
        puerta3 = self.fabricarPuerta(habitacion3, habitacion4)
        puerta4 = self.fabricarPuerta(habitacion1, habitacion3)

        habitacion1.ponerElemento(self.fabricarEste(), puerta1)
        habitacion1.ponerElemento(self.fabricarSur(), puerta4)

        habitacion2.ponerElemento(self.fabricarOeste(), puerta1)
        habitacion2.ponerElemento(self.fabricarSur(), puerta2)
        self.fabricarArmario(habitacion2)
        for i in habitacion2.hijos:
            if i.esArmario():
                i.agregarHijo(self.fabricarBomba())
        

        habitacion3.ponerElemento(self.fabricarEste(), puerta3)
        habitacion3.ponerElemento(self.fabricarNorte(), puerta4)
        self.fabricarArmario(habitacion3)

        habitacion4.ponerElemento(self.fabricarNorte(), puerta2)
        habitacion4.ponerElemento(self.fabricarOeste(), puerta3)

        self.laberinto.agregarHabitacion(habitacion1)
        self.laberinto.agregarHabitacion(habitacion2)
        self.laberinto.agregarHabitacion(habitacion3)
        self.laberinto.agregarHabitacion(habitacion4)


    def fabricarHabitacion(self, unNum):
        habitacion = Habitacion (unNum)
        habitacion.ponerElemento(self.fabricarNorte(), self.fabricarPared())
        habitacion.ponerElemento(self.fabricarSur(), self.fabricarPared())
        habitacion.ponerElemento(self.fabricarEste(), self.fabricarPared())
        habitacion.ponerElemento(self.fabricarOeste(), self.fabricarPared())

        habitacion.agregarOrientacion(self.fabricarNorte())
        habitacion.agregarOrientacion(self.fabricarSur())
        habitacion.agregarOrientacion(self.fabricarEste())
        habitacion.agregarOrientacion(self.fabricarOeste())

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

        armario.agregarOrientacion(self.fabricarNorte())
        armario.agregarOrientacion(self.fabricarSur())
        armario.agregarOrientacion(self.fabricarEste())
        armario.agregarOrientacion(self.fabricarOeste())

        puerta = self.fabricarPuerta(armario, unCont)
        armario.ponerElemento(self.fabricarSur(), puerta)

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

    def fabricarBomba(self):
        return Bomba()
    
    def fabricarEste(self):
        return Este()
    def fabricarOeste(self):
        return Oeste()
    def fabricarNorte(self):
        return Norte()
    def fabricarSur(self):
        return Sur()
    
    def numeroHabitaciones(self):
        return self.laberinto.numeroHabitaciones()
    
    def obtenerHabitacion(self, unNum):
        return self.laberinto.obtenerHabitacion(unNum)