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
    
