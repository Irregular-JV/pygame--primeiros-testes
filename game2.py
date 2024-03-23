import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Configurações Iniciais
pygame.init()
pygame.display.set_caption("Meu Jogo")
logo = pygame.image.load("dyswai5p.png")
pygame.display.set_icon(logo)


largura = 500
altura = 500

relogio =pygame.time.Clock()

# Coordenadas de Movimento
x = largura // 2 - 20
y = 0

x_doVerde = randint(40, 450)
y_doVerde = randint(40, 450)

# Defini o tamanho da janela da tela 
tela = pygame.display.set_mode((largura, altura))

# Loop pincipal do jogo e sempre é infinito para que atualize sempre quando algo acontecer
while True:
    
    relogio.tick(30)
    # Preenche a tela de Branco
    tela.fill((255,255,255))


    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            pygame.quit()
            exit()

        # if eventos.type == KEYDOWN:
        #     if eventos.key == K_a:
        #         x += -20
        #     if eventos.key == K_s:
        #         y += 20
        #     if eventos.key == K_d:
        #         x += 20
        #     if eventos.key == K_w:
        #         y += -20
                
   

    


    # Desenhos na Tela
    tela.blit(logo, (0,0))
    retangulo_vermelho = pygame.draw.rect(tela, (255,0,0), (x, y, 40, 40))
    retangulo_azul = pygame.draw.rect(tela, (0, 255, 0), (x_doVerde, y_doVerde, 40, 40))

    # Movimento do retangulo
    if pygame.key.get_pressed()[K_a]:
        x += -20
        if x < -30:
            x = largura - 10

    if pygame.key.get_pressed()[K_s]:
        y += 20
        if y > altura - 10:
             y = -30

    if pygame.key.get_pressed()[K_d]:
        x += 20
        if x > largura - 10:
            x = -30

    if pygame.key.get_pressed()[K_w]:
        y += -20
        if y < -30:
            y = altura - 30
    
    if retangulo_vermelho.colliderect(retangulo_azul):
        x_doVerde = randint(40, 450)
        y_doVerde = randint(40, 450)
    
    pygame.display.update()