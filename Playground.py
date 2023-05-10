#!/usr/bin/python
#-*- coding: utf-8 -*-

from Juego import Juego

if __name__ == "__main__":
    juego = Juego()
    juego.laberinto4habitaciones()
    print("Número de habitaciones: ", juego.numeroHabitaciones())
    print("Información de las habitaciones \n")
    for i in range(0, juego.numeroHabitaciones()):
        aux = juego.obtenerHabitacion(i)
        print("Habitacion ", i)
        print(type(aux))
        print("Norte    - Pared  : ",  aux.norte.esPared())
        print("Norte    - Puerta : ",  aux.norte.esPuerta())
        print("Sur      - Pared  : ",  aux.sur.esPared())
        print("Sur      - Puerta : ",  aux.sur.esPuerta())
        print("Este     - Pared  : ",  aux.este.esPared())
        print("Este     - Puerta : ",  aux.este.esPuerta())
        print("Oeste    - Pared  : ",  aux.oeste.esPared())
        print("Oeste    - Puerta : ",  aux.oeste.esPuerta())
        print("--------------------")



