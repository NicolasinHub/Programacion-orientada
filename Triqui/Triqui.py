import math
import random


tablero=[]
casillasvacias=[]
TABLERO_FILAS=3
TABLERO_COLUMNAS=3

for i in range(9):
    tablero.append(' ') 
    casillasvacias.append(i)
    

def numero(literal, inferior, superior):
    while True:
        valor=input(literal)
        while(not valor.isnumeric()):
            print("Solo se admiten numeros entre {0} y {1}".format(inferior,superior))
            valor=input(literal)
        coor=int(valor)
        if(coor>=inferior and coor<=superior):
            return coor
        else:
            print("El valor indicado es incorrecto, introduzca un numero entre {0} y {1}".format(inferior,superior))
   
def numeroHermanos(casilla, ficha, v, h):
    f=math.floor(casilla/TABLERO_COLUMNAS)
    c=casilla % TABLERO_COLUMNAS
    fila_nueva=f+v
    if(fila_nueva<0 or fila_nueva>=TABLERO_FILAS):
        return 0
    columna_nueva=c+h
    if(columna_nueva<0 or columna_nueva>=TABLERO_COLUMNAS):
        return 0
    pos=(fila_nueva*TABLERO_COLUMNAS+columna_nueva)
    if(tablero[pos]!=ficha):
        return 0
    else:
        return 1+numeroHermanos(pos,ficha,v,h)
    
    
def hemosGanado(casilla, ficha):
    hermanos=numeroHermanos(casilla,ficha,-1,-1)+numeroHermanos(casilla,ficha,1,1)
    if(hermanos==2):
        return True
    hermanos=numeroHermanos(casilla,ficha,1,-1)+numeroHermanos(casilla,ficha,-1,1)
    if(hermanos==2):
        return True
    hermanos=numeroHermanos(casilla,ficha,-1,0)+numeroHermanos(casilla,ficha,1,0)
    if(hermanos==2):
        return True
    hermanos=numeroHermanos(casilla,ficha,0,-1)+numeroHermanos(casilla,ficha,0,1)
    if(hermanos==2):
        return True    
    
def colocarFicha(ficha):
    print("Dame la posición de una ficha")
    while True:
        fila=numero("Fila entre [1 y 3]: ", 1,3)-1
        columna=numero("Columna entre [1 y 3]: ", 1,3)-1
        casilla=fila*TABLERO_COLUMNAS+columna
        if(tablero[casilla]!=' '):
            print("La casilla esta ocupada")
        else:
            tablero[casilla]=ficha
            return casilla
        
        
def colocarFichaMaquina(ficha, fichaContricante):
    random.shuffle(casillasvacias)
    for casilla in casillasvacias:
        if(hemosGanado(casilla,ficha)):
            tablero[casilla]=ficha
            return casilla
    for casilla in casillasvacias:
        if(hemosGanado(casilla,fichaContricante)):
            tablero[casilla]=ficha
    for casilla in casillasvacias:
        tablero[casilla]=ficha
        return casilla
    
        
def pintarTablero():
    pos=0
    print(("-"*18))
    for fila in range(3):
        for columna in range(3):
            print("| ",tablero[pos]," ", end="")
            pos+=1
        print("|\n",("-"*18))
    
jugadores=[]
numeroJugadores=numero("Numero de jugadores: ", 0,2)
for i in range(numeroJugadores):
    jugadores.append({"nombre":input("Nombre del jugador "+str(i+1)+": "),"tipo":"H"})
for i in range(2-numeroJugadores):
    jugadores.append({"nombre":"Maquina "+str(i+1),"tipo":"M"})
print("\n Empazamos la partida con los jugadores")
for jugador in jugadores:
    print("\t",jugador["nombre"])
empieza=numero("¿Que jugador empieza? [1="+jugadores[0]["nombre"]+",2="+jugadores[1]["nombre"]+"]: ",1,2)
if(empieza==2):
    jugadores.reverse()

continuar=False
fichasenTablero=0
while continuar:
    pintarTablero()
    numJugador=(fichasenTablero&1)
    ficha='X' if numJugador==1 else 'O'
    if(jugadores[numJugador]["tipo"]=="H"):
        casilla=colocarFicha(ficha)
        continuar=False
        print(jugadores[jugador], "¡¡Has ganado!!")
    fichasenTablero+=1
    if(fichasenTablero==9):
        continuar=False
    
pintarTablero()
 