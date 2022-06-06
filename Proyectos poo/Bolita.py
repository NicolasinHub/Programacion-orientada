from turtle import Screen, circle
import pygame
import sys, pygame

ScreenSize=800,600
Blanco=255,255,255
Negro=0,0,0
Posicionx=400
Posiciony=300
BallSize=20
Speed=[1, 1]

pygame.init()

screen=pygame.display.set_mode(ScreenSize)
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
        
    Ball=pygame.image.load("Ball.jpg")
    Ballrect= Ball.get_rect()
        
    pygame.display.update()
    screen.fill(Blanco)
    pygame.display.flip()  
    clock.tick(20)