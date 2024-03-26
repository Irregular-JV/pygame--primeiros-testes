import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.display.set_caption("teste")

largura = 500 
altura = 500

tela = pygame.display.set_mode((largura, altura))

# O : é onde fica o bloco do meu loop tanto do while qunato do for   
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255,44,13), (250, 250, 40, 40)) 
    pygame.draw.circle(tela, (0, 0, 255), (250, 250), (50))
    pygame.draw.line(tela, (0, 255, 0), (200, 50), (50, 50))
    pygame.draw.line(tela, (0, 255, 0), (100, 200), (100, 30), 5 )
    pygame.display.update()
            