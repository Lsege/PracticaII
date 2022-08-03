def menunewton():
    print("Ingrese la opción correspondiente")
    print("")
    print("1. Primera ley de newton. ")
    print("2. Segunda ley de newton.")
    print("3. Tercera ley de newton.")

def primera():
    print('''
    Todo cuerpo continúa en su estado de reposo o movimiento uniforme en línea recta, 
    no muy lejos de las fuerzas impresas a cambiar su posición.
    
    Esta ley indica que un cuerpo no cambia su estado inicial 
    al menos que se le aplique una fuerza o series de fuerzas (que no se cancelen entre sí)
     ''')

def segunda():
    m = float(input("Ingrese la masa del objeto "))
    a = float(input("Ingrese la aceleración del objeto "))
    F = m*a
    final = "La fuerza que se emplea en un cuerpo de masa {} para moverlo con una aceleración {} es de: {} "
    print(final.format(m, a, F))

def tercera():
    print('''Con toda acción ocurre siempre una reacción igual y contraria: 
    quiere decir que las acciones mutuas de dos cuerpos siempre son iguales 
    y dirigidas en sentido opuesto.
    
    F12 = -F21''')