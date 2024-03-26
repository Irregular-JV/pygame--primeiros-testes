# Improtando meus arquivos pygame e modulos
import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Inicinado o Pygame
pygame.init()

# Variaveis de controle
largura = 600
altura = 600
x = int(largura/2)
y = 0
x_a = randint(40, 550)
y_a = randint(40, 550)
print(y_a)
pontos = 0

# Taxade de fps
fps = pygame.time.Clock()

# Sistema de pontos 
fonte = pygame.font.SysFont("Arial", 30, True, True)


# Definindo música logo fundo
logo = pygame.image.load("dyswai5p.png")
pygame.display.set_icon(logo)
image_fundo = pygame.image.load('dyswai5p.png')

fundo_som = pygame.mixer.music.load("fundo.mp3")
pygame.mixer.music.play(-1)
colid_music = pygame.mixer.Sound('colid.mp3')

pygame.mixer.music.set_volume(0.25)

# Definir minha tela
tela = pygame.display.set_mode((largura, altura))

# Loop infinito para manter a execução do jogo
while True:
    # Definindo a taxa de fps
    fps.tick(30)

    # Mundando a cor de fundo para branco
    tela.fill((255,255,255))

    # Um for que itera por todos os events do pygame
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            pygame.quit()
            exit()
    # Adicionando o texto e formatando
    meu_texto = f'Pontos:{pontos}'

    # Juntando o texto com a fonte 
    texto_formatado = fonte.render(meu_texto, True, (255,255,255))


    # Movimento do retângulo
    if pygame.key.get_pressed()[K_a]:
        x -= 10
        if x < -30:
            x = largura - 10
    

    if pygame.key.get_pressed()[K_s]:
        y += 10
        if y > altura:
            y = -30
           
    if pygame.key.get_pressed()[K_d]:
        x += 10
        if x > largura:
            x = -30   
           
    if pygame.key.get_pressed()[K_w]:
        y -= 10
        if y < 0:
            y = altura + 30   
           


    # Imagem de fundo
    tela.blit(image_fundo, (0,0))

    # Desenhando meus retangulos na tela 
    retangulo_a = pygame.draw.rect(tela, (255,0, 122), (x,y, 40,40))
    retangulo_b = pygame.draw.rect(tela, (255,122, 0), (x_a,y_a, 40,40))

    # Definindo a colisão com o retangulo
    if retangulo_a.colliderect(retangulo_b):
        x_a = randint(40, 550)
        y_a = randint(40, 550)
        pontos += 1
        colid_music.play()

    # Adicionando o texto na tela
    tela.blit(texto_formatado, (430, 40))

    # Atualiza a tela infinitamente
    pygame.display.update()   
    