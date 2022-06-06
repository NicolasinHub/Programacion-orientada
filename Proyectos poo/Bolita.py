
import sys, pygame
from turtle import Screen, circle
import pygame

ScreenSize=800,600
width, heigth=800, 600
Blanco=255,255,255
Negro=0,0,0
Posicion=[1, 1]

pygame.init()

screen=pygame.display.set_mode(ScreenSize)
clock=pygame.time.Clock()

Ball=pygame.image.load("Bola.jpg")
Ballrect = Ball.get_rect()

while True:
    #pygame.time.delay(2)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        Ballrect=Ballrect.move(Posicion)
    if Ballrect.left < 0 or Ballrect.right > width:
        Posicion[0]= -Posicion[0]
    if Ballrect.top < 0 or Ballrect.bottom > heigth:
        Posicion[1]= -Posicion[1]
        
    
    pygame.display.update()
    screen.fill(Blanco)
    screen.blit(Ball, Ballrect)
    pygame.display.flip()  
    clock.tick(150)