#!/usr/bin/python
#-*- coding: utf-8 -*-

from Juego import Juego

if __name__ == "__main__":
    juego = Juego()
    juego.laberinto4habitaciones()
    print("Número de habitaciones: ", juego.numeroHabitaciones())
    print("Información de creación de las habitaciones \n")
    for i in range(0, juego.numeroHabitaciones()):
        aux = juego.obtenerHabitacion(i)
        print("Habitacion ", i)
        print("Clase de la habitación:" , type(aux))
        print("Norte    - Pared  : ",  aux.norte.esPared())
        print("Norte    - Puerta : ",  aux.norte.esPuerta())
        print("Sur      - Pared  : ",  aux.sur.esPared())
        print("Sur      - Puerta : ",  aux.sur.esPuerta())
        print("Este     - Pared  : ",  aux.este.esPared())
        print("Este     - Puerta : ",  aux.este.esPuerta())
        print("Oeste    - Pared  : ",  aux.oeste.esPared())
        print("Oeste    - Puerta : ",  aux.oeste.esPuerta())
        print("--------------------")

    print("\nAhora se verán los contenedores correspondientes")
    print("--------------------")
    hab2 = juego.obtenerHabitacion(1)
    print("Habitación 2")
    for aux in hab2.hijos:
        print("Clase del hijo:" , type(aux))
        print("¿Tiene algo dentro? -> ", not len(aux.hijos)==0)
        for aux2 in aux.hijos:
            print("¿Es bomba?", aux2.esBomba())
    
    print("--------------------")
    hab3 = juego.obtenerHabitacion(2)
    print("\nHabitación 3")
    for aux in hab3.hijos:
        print("Clase del hijo:" , type(aux))
        print("¿Tiene algo dentro? -> ", not len(aux.hijos)==0)

    
    print("\n\n----------------------------------")
    print("Interacción con el usuario")
    for i in range(0, juego.numeroHabitaciones()):
        aux = juego.obtenerHabitacion(i)
        aux.entrar()
        aux.norte.entrar()
        aux.este.entrar()
        aux.sur.entrar()
        aux.oeste.entrar()

        print("Abrimos puertas")
        juego.abrirPuertas()
        aux.norte.entrar()
        aux.este.entrar()
        aux.sur.entrar()
        aux.oeste.entrar()
        juego.cerrarPuertas()
        print("------------")
    
    print("La bomba, en habitación 2")
    hab2 = juego.obtenerHabitacion(1)
    for aux in hab2.hijos:
        for aux2 in aux.hijos:
                if aux2.esBomba():
                    aux2.activar()
                aux2.entrar()
    for aux in hab2.hijos:
        for aux2 in aux.hijos:
                if aux2.esBomba():
                    aux2.desactivar()
                aux2.entrar()




