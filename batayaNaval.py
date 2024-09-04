import random

def crearTablero(dimension):
    return [["~"for _ in range(dimension)] for _ in range(dimension)]

def mostrarTablero(tableroDisparosJugador,TableroDisparosOponentes):
    print("\n Tablero de Disparos")
    for fila in tableroDisparosJugador:
        print(" ".join(fila))
    print("\n tablero de Disparos Oponente")
    for fila in TableroDisparosOponentes:
        print(" ".join(fila))
def ponerBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado = False
        while not colocado:
            if jugador == "jugador":
                print(f"colocando {barco ['nombre']} de tamaño {barco['dimension']}")
                fila = int(input("Ingrese la Fila:  "))
                columna=int(input("ingrese la columna:  "))
                orientacion = input("ingrese la orientacion (h para horizontal, v para vertical):  ").lower()
            else:
                fila = random.randint(0,len(tablero)-1)
                columna = random.randint(0,len(tablero)-1)
                orientacion =random.choice(["h","v"])
            
            if validarColocacion(tablero,fila,columna,barco["dimension"],orientacion):
                colocarBarco(tablero,fila,columna,barco["dimension"], orientacion)
                colocado= True
            elif jugador == "jugador":
                print("Colocacion es invalida. Intenta de nuevo")
def validarColocacion(tablero,fila,columna,dimension,orientacion):
    if orientacion == 'h':
        if columna + dimension > len(tablero):
            return False
        for i in range(dimension):
            if tablero[fila][columna+i] !="~":
                return False
    else:
        if fila + dimension>len(tablero):
            return False
        for i in range(dimension):
             if tablero[fila+i][columna] !="~":
                return False
    return True

def colocarBarco(tablero,fila,columna,dimension,orientacion):
    if orientacion == "h":
        for i in range(dimension):
            tablero[fila][columna+i] ="B"
    else:
        for i in range(dimension):
            tablero[fila+i][columna] ="B"
    
def realizarDisparos(tableroOculto, TableroDisparos,fila,columna):
    if tableroOculto[fila][columna] == "B":
        TableroDisparos[fila][columna]="X"
        tableroOculto[fila][columna]="H"
        return "Impacto"
    elif TableroDisparos[fila][columna]=="~":
        TableroDisparos[fila][columna]="O"
       
        return "Agua"
    return "ya disparaste Aqui"
def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:
            return False
    return True
def jugarContraComputadora():
    dimencion=5
    tableroJugador = crearTablero(dimencion)
    tableroComputadora=crearTablero(dimencion)
    tabalroDisparos =crearTablero(dimencion)
    tabalroDisparosComputadora =crearTablero(dimencion)
    barcos=[
        {"nombre":"portaAviones","dimension":3},
        
        {"nombre":"portaAviones","dimension":2}
    ]
    print("coloca tus barcos")
    ponerBarcos(tableroJugador,barcos,"jugador")
    ponerBarcos(tableroComputadora,barcos,"computadora")
    turnoJugador= True
    while True:
        if turnoJugador:
            print("/ tu Turno")
            mostrarTablero(tabalroDisparos,tabalroDisparosComputadora)
            fila = int(input("Ingresa la fila del disparo"))
            columna=int(input("ingresa la columna del disparo"))
            resultado=realizarDisparos(tableroComputadora,tabalroDisparos,fila,columna)
            print(resultado)
            if verificarVictoria(tableroComputadora):
                print("ganaste")
                return "jugador"
        else:
            print("\n Tuno de la computadora")
            fila=random.randint(0,dimencion-1)
            columna=random.randint(0,dimencion-1)
            resultado = realizarDisparos(tableroJugador,tabalroDisparosComputadora,fila,columna)
            print(f"la computadora disparo en ({fila},{columna}: {resultado})")
            if verificarVictoria(tableroComputadora):
                print("la computadora gano")
                return "computadora"
        turnoJugador = not turnoJugador

def jugarDosJugadores():
    dimencion=5
    tableroJugador1 = crearTablero(dimencion)
    tableroJUgador2=crearTablero(dimencion)
    tabalroDisparos1 =crearTablero(dimencion)
    tabalroDisparos2 =crearTablero(dimencion)
    barcos=[
        {"nombre":"portaAviones","dimension":3},
        
        {"nombre":"portaAviones","dimension":2}
  
    ]
    print("coloca tus barcos")
    ponerBarcos(tableroJugador1,barcos,"jugador 1")
    ponerBarcos(tableroJUgador2,barcos,"jugador 2")
    turnoJugador1= True
    while True:
        if turnoJugador1:
            print("/ Turno Jugador 1")
            mostrarTablero(tabalroDisparos1, tabalroDisparos2)
            fila = int(input("Ingresa la fila del disparo"))
            columna=int(input("ingresa la columna del disparo"))
            resultado=realizarDisparos(tableroJUgador2,tabalroDisparos1,fila,columna)
            print(resultado)
            if verificarVictoria(tableroJUgador2):
                print("Jugador 1 gano")
                return "jugador 1"
        else:
            print("\n Tuno del jugador 2")
            mostrarTablero(tabalroDisparos2, tabalroDisparos1)
            fila=int(input("Ingresa la fila del disparo"))
            columna=int(input("ingresa la columna del disparo"))
            resultado = realizarDisparos(tableroJugador1,tabalroDisparos2,fila,columna)
            print(resultado)
            if verificarVictoria(tableroJugador1):
                print("gano el jugador 2")
                return "jugador 2"
        turnoJugador1 = not turnoJugador1
def mostrarMenu():
    print("Bienvenido a Batalla naval")
    print("Selecciona contra quien jugaras.")
    print("1. contra la computadora.")
    print("2. contra otro jugador.")
    print("3. salir.")
def iniciarJuego():
    while True:
        mostrarMenu()
        modo = input("elige una opcion:  ")
        if modo=="1":
            ganador=jugarContraComputadora()
        elif modo =="2":
            ganador= jugarDosJugadores()
        elif modo == "3":
            print("Gracias por jugar")
            break
        else:
            print("opcion invalida seleciona otro numero")
            continue
        print(f"el ganador es: {ganador}")
        jugarNuevo = input("Quiere jugar de nuevo?  (s/n)").lower()
        if jugarNuevo == "s":
            print("salite")
            break
        
        
iniciarJuego()
            
        
        
            
                
    


        
    
    
    
        
        
                


    