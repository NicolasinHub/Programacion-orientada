import random 
import os

def CrearTablero(fil, col, val):
    tablero=[]
    for i in range(fil):
        tablero.append([])
        for j in range(col):
            tablero[i].append(val)
    return tablero

def MostrarTablero(tablero):
    for fila in tablero:
        for e in fila:
            print(e, end=" ")
        print()
        

columnas=16
filas=12

visible=MostrarTablero(filas,columnas, "-")
oculto=MostrarTablero(filas,columnas,0)


def ColocarMinas(tablero, minas, fil, col):
    minasocultas=[]
    numero=0
    while numero < minas:
        y = random.randint(0,fil-1)
        x = random.randint(0,col-1)
        if tablero[y][x] != 9:
            tablero[y][x] = 9
            numero+=1
            minasocultas.append((y,x))
    return tablero, minasocultas


def Presentacion():
    os.system("cls")
    
    print("**********************")
    print("*                    *")
    print("*     BUSCAMINAS     *")
    print("*  w/a/s/d - MOVERSE *")
    print("*                    *")
    print("*       MOSTRAR      *")
    print("*B/V-marcar/desmarcar*")   
    print("*                    *")
    print("**********************")
    print()
    input(" 'Enter' para empezar...")
    
def Menu():
    print()
    opcion = input("¿w/a/s/d - m - b/v?")
    return opcion

columnas = 16
filas = 12

visible=CrearTablero(filas,columnas, "-")
oculto=CrearTablero(filas, columnas, 0)
oculto, MinasOcultas = ColocarMinas(oculto, 15, filas, columnas)

Presentacion()

y = random.randint(2, filas-3)
x = random.randint(2, columnas-3)

real = visible[y][x]
visible[y][x]= "X"

os.system("cls")
MostrarTablero(visible)

MinasMarcadas=[]

jugando = True

while jugando:
    mov = Menu()
    
    if mov == "w":
        if y == 0:
            y=0
        else:
            visible[y][x] = real
            y -= 1
            real = visible[y][x]
            visible[y][x] = "X"
    elif mov == "s":
        if y == filas-1:
            y = filas-1
        else:
            visible[y][x]=real
            y += 1
            real = visible[y][x]
            visible[y][x] = "X"
    elif mov == "a":
        if x == 0:
            x = 0
        else:
            visible[y][x] = real
            x -= 1
            real = visible[y][x]
            visible[y][x] = "X"
    elif mov == "d":
        if x == columnas-1:
            x = columnas-1
        else:
            visible[y][x] = real
            x += 1
            real = visible[y][x]
            visible[y][x] = "X"
    os.system("cls")
    
    MostrarTablero(visible)        
    
    MinasMarcadas=[]
    jugando = True
    
    while jugando:
        
        mov = Menu()
        
        if mov == "w":
            if y == 0:
                y = 0
            else:
                visible[y][x] = real
                y -= 1
                real = visible[y][x]
                visible[y][x] = "x"
                
        elif mov == "s":
            if y == filas-1:
                y= filas-1
            else:
                visible[y][x] = real
                y += 1
                real = visible[y][x]
                visible[y][x] = "x"
        elif mov == "d":
            if x ==columnas-1:
                x = columnas-1
            else:
                visible[y][x] = real
                x += 1
                real = visible[y][x]
                visible[y][x] = "x"
                
        os.system("cls")
        
        MostrarTablero(visible)
                            
                            