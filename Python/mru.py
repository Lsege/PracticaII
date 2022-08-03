def menurectilineos():
    print("Ingrese la opción correspondiente a lo que desea calcular")
    print("")
    print("1. Cálculo de distancia MRU")
    print("2. Cálculo de velocidad MRU")
    print("3. Cálculo de tiempo MRU")
    print("4. Cálculo de distancia MRUV")

def distanciaMRU():
    v = float(input("Ingrese la velocidad: "))
    t = float(input("Ingrese el tiempo: "))
    d = v * t
    final = "La distancia que recorre el objeto con velocidad {} en el tiempo {} es: {}"
    print(final.format(v, t, d))

def velocidadMRU():
    d = float(input("Ingrese la distancia: "))
    t = float(input("Ingrese el tiempo: "))
    while t == 0:
        print("El tiempo no puede ser cero.")
        t = float(input("Ingrese el tiempo nuevamente: "))
    v = d/t
    v = round(v, 2)
    final = "La velocidad que tiene el objeto con que recorre una distancia {} en el tiempo {} es: {}"
    print(final.format(d, t, v))

def tiempoMRU():
    d = float(input("Ingrese la distancia: "))
    v = float(input("Ingrese la velocidad: "))
    while v == 0:
        print("La velocidad no puede ser cero.")
        t = float(input("Ingrese la velocidad nuevamente: "))
    t = d/v
    t = round(t, 2)
    final = "El tiempo que tarda el objeto que recorre una distancia {} en el tiempo {} es de: {}"
    print(final.format(d, v, t))

def distanciaMRUA():
    v0 = float(input("Ingrese la velocidad inicial del objeto "))
    t = float(input("Ingrese el tiempo final del recorrido "))
    a = float(input("Ingrese la aceleración del objeto "))
    d = v0*t + (a/2) * (t**2)
    d = round(d, 2)
    final = "La distancia recorrida final es de {}"
    print(final.format(d))