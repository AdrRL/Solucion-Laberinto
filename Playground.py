#!/usr/bin/python
#-*- coding: utf-8 -*-

from Juego import Juego

class Playground:

    def main():
        juego = Juego()
        juego.laberinto4habitaciones()

        for i in range(0, len(juego.numeroHabitaciones())):
            aux = juego.obtenerHabitacion(i)
            print("Habitacion ", i)
            print("Norte    - Pared : ",  aux.norte.esPared())
            print("Sur      - Pared : ",  aux.sur.esPared())
            print("Este     - Pared : ",  aux.este.esPared())
            print("Oeste    - Pared : ",  aux.oeste.esPared())
            print("--------------------")


