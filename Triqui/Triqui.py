import math
tablero=[]
TABLERO_FILAS=3
TABLERO_COLUMNAS=3

for i in range(9):
    tablero.append(' ')

def coordenada(literal,inferior,superior):
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


def colocarFicha(ficha):
    print("Dame la posición de una ficha")
    while True:
        fila=coordenada("Fila entre [1 y 3]: ",1,3)-1
        columna=coordenada("Columna entre [1 y 3]: ",1,3)-1
        casilla=fila*3+columna
        if(tablero[casilla]!=' '):
            print("La casilla esta ocupada")
        else:
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
        
def numeroHermanos(casilla, h, v):
    f=math.floor(casilla/TABLERO_COLUMNAS)
    c=casilla % TABLERO_COLUMNAS
    fila_nueva=f+v
    if(fila_nueva<0 or fila_nueva>=TABLERO_FILAS):
        return 0
    columna_nueva=c+v
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
        return true
    hermanos=numeroHermanos(casilla,ficha,1,-1)+numeroHermanos(casilla,ficha,-1,1)
    if(hermanos==2):
        return true
    hermanos=numeroHermanos(casilla,ficha,-1,0)+numeroHermanos(casilla,ficha,1,0)
    if(hermanos==2):
        return true
    hermanos=numeroHermanos(casilla,ficha,0,-1)+numeroHermanos(casilla,ficha,0,1)
    if(hermanos==2):
        return true    
    
jugador1=input("Nombre del jugador 1: ")
jugador2=input("Nombre del jugador 2: ")

continuar=False
fichasenTablero=0
while continuar:
    pintarTablero()
    ficha='X' if (fichasenTablero&1) else 'O'
    casilla=colocarFicha(ficha)
    if(hemosGanado(casilla,ficha)):
        continuar=False
        print("Has ganado")
    fichasenTablero+=1
    if(fichasenTablero==9):
        continuar=False
    
pintarTablero()
 