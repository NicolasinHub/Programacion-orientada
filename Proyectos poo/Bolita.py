import pygame

ScreenSize=800,600
Blanco=255,255,255
Negro=0,0,0
Posicionx=400
Posiciony=300
BallSize=20

pygame.init()

screen=pygame.display.set_mode(ScreenSize)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
            