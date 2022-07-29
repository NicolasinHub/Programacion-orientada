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