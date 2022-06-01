from re import A
import pygame
import random

Blanco=255,255,255
Negro=0,0,0

pygame.init()

screen=pygame.display.set_mode((1200,800))

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    pygame.display.update()
    pygame.draw.circle(screen, Blanco, (600,400),random.randrange(10,50))
    pygame.display.flip()
    
    keyboard=pygame.key.get_pressed()
    if keyboard[pygame.K_a]:
        