import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Configurações Iniciais
pygame.init()
pygame.display.set_caption("Meu Jogo")
logo = pygame.image.load("dyswai5p.png")
pygame.display.set_icon(logo)

# Músicas
somdefundo = pygame.mixer.music.load('fundo.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

som_colid = pygame.mixer.Sound("colid.mp3")


largura = 500
altura = 500

'''
Para a definição de font segue a ordem dos parametros
1-Nome da fonte
2-tamanho da fonte
3-negrito ou não
4-italico ou não
'''
fonte = pygame.font.SysFont('Arial', 30, True, True )


# Sistema de pontos
pontos = 0
relogio =pygame.time.Clock()

# Coordenadas de Movimento
x = int(largura // 2 - 20)
y = 0

x_doVerde = randint(40, 450)
y_doVerde = randint(40, 450)

# Defini o tamanho da janela da tela 
tela = pygame.display.set_mode((largura, altura))

# Loop pincipal do jogo e sempre é infinito para que atualize sempre quando algo acontecer
while True:
    
    '''Agora vamos definir o que vai está escrito no texto
    Pra isso criamos uma nova variavel e colocamos uma string fomatada com o nome do nosso texto
    e fazemos uma interpolação com a variavel pontos
    '''
    mensagem = f'Pontos: {pontos}'
    # Juntando nosso texto e fonte e adicionando com e outras configs
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    relogio.tick(15)
    # Preenche a tela de Branco
    tela.fill((255,255,255))


    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            pygame.quit()
            exit()

        '''if eventos.type == KEYDOWN:
             if eventos.key == K_a:
                 x += -20
             if eventos.key == K_s:
                 y += 20
             if eventos.key == K_d:
                 x += 20
             if eventos.key == K_w:
                 y += -20'''
                


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
    
    # Colidindo com outro retangulo
    if retangulo_vermelho.colliderect(retangulo_azul):
        x_doVerde = randint(40, 450)
        y_doVerde = randint(40, 450)
        pontos += 1
        som_colid.play()


    tela.blit(texto_formatado, (320, 50))
    pygame.display.update()