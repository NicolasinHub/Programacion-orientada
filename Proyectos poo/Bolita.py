
from turtle import Screen, circle
import pygame

ScreenSize=800,600
BallSize=30
Blanco=255,255,255
Negro=0,0,0
Posicionx=400
Posiciony=300
Posicion=[1, 1]

pygame.init()

screen=pygame.display.set_mode(ScreenSize)
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        
    
    if (BallSize-Posicionx) < Posicionx:
        Posicion[0]= -Posicion[0]
    
    Posicion=
    pygame.display.update()
    screen.fill(Blanco)
    pygame.draw.circle(screen, Negro, (Posicionx,Posiciony), (BallSize))
    pygame.display.flip()  
    clock.tick(20)