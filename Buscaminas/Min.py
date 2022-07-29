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
    