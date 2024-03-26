import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()
# Configs do arquivo
pygame.display.set_caption("Meu Jogo")
img = pygame.image.load("img/dyswai5p.png")
pygame.display.set_icon(img)

# Controle de velocidade
relogio = pygame.time.Clock()

# Tela
largura = 600
altura = 600

tela = pygame.display.set_mode((largura, altura))

# Minhas posições
x = int(largura/2 - 25)
y = 0
x_a = randint(30, 550)
y_a = randint(30, 550)

# Sistema de pontos e texto
pontos = 0
font = pygame.font.SysFont('Arial', 25,True, True)

# Adicionando os s0ns
fundo = pygame.mixer.music.load('music/fundo.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
colid = pygame.mixer.Sound('music/colid.mp3')

# Estrutur do game
while True:
    tela.fill((0,0,0))
    texto = f'Pontos: {pontos}'
    junta = font.render(texto, True, (255,255,255))
    relogio.tick(60)
    tela.blit(img, (0,0))
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x += -5
        if x < -35:
            x = largura - 35
    if pygame.key.get_pressed()[K_s]:
        y += 5
        if y > altura:
            y = -35
    
    if pygame.key.get_pressed()[K_d]:
        x += 5
        if x > largura:
            x = -35
    if pygame.key.get_pressed()[K_w]:
        y += -5
        if y < 0:
            y = altura + 35

    retangulo_a = pygame.draw.rect(tela, (255, 44, 32), (x, y, 50, 50))
    retangulo_b = pygame.draw.rect(tela, (0, 44, 98), (x_a, y_a, 50, 50))

    # Colisão
    if retangulo_a.colliderect(retangulo_b):
       x_a = randint(30, 550)
       y_a = randint(30, 550)
       pontos += 1
       colid.play() 
      
    tela.blit(junta, (450, 30))

    pygame.display.update()

    