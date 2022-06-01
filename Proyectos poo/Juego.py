from re import A
import pygame
import random

Tamaño=800,600
Blanco=255,255,255
Negro=0,0,0
Posicionx=400
Posiciony=300

pygame.init()

screen=pygame.display.set_mode(Tamaño)

while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Posicionx = Posicionx-4
            if event.key == pygame.K_d:
                Posicionx = Posicionx+4
            if event.key == pygame.K_w:
                Posicionx = Posiciony-4
            if event.key == pygame.K_s:
                Posicionx = Posiciony+4
            
    pygame.display.update()
    screen.fill(Blanco)
    pygame.draw.circle(screen, Negro, (Posicionx,Posiciony), (20))
    pygame.display.flip()   