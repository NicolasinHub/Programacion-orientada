from re import A
import pygame
import random

Tamaño=1200,800
Blanco=255,255,255
Negro=0,0,0
Posicionx=600
Posiciony=400

pygame.init()

screen=pygame.display.set_mode(Tamaño)

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Posicionx = Posicionx+1
            if event.key == pygame.K_d:
                Posicionx = Posicionx-1
            if event.key == pygame.K_w:
                Posicionx = Posiciony-1
            if event.key == pygame.K_s:
                Posicionx = Posiciony+1
            
    pygame.display.update()
    pygame.draw.circle(screen, Blanco, (Posicionx,Posiciony),random.randrange(10,50))
    pygame.display.flip()   