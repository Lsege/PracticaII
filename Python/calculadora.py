from menu import *
from mru import *
from newton import *

menu()
opcion = input()

while opcion != "1" and opcion != "2":
    print("Ingrese un valor válido por favor")
    opcion = input()


if opcion == "1":
    menurectilineos()
    opcion2 = input()
    while opcion2 != "1" and opcion2 != "2" and opcion2 != "3" and opcion2 != "4":
        print("Ingrese un valor válido por favor")
        opcion2 = input()

    if opcion2 == "1":
        distanciaMRU()
    elif opcion2 == "2":
        velocidadMRU()
    elif opcion3 == "3":
        tiempoMRU()
    elif opcion4 == "4":
        distanciaMRUA()
elif opcion == "2":
    menunewton()
    opcion2 = input()
    while opcion != "1" or opcion != "2" or opcion2 != "3":
        print("Ingrese un valor válido por favor")
        opcion2 = input()

    if opcion2 == "1":
        primera()
    elif opcion2 == "2":
        segunda()
    elif opcion2 == "3":
        tercera()



