import pygame
import sys

pygame.init()

azul = (0,0,255)
vermelho = (255,0,0)
verde = (0,255,0)

tela = pygame.display.set_mode([640,480])
pygame.display.set_caption('Meu Jogo')

xb = 250
yb = 100

xr = 470
yr = 450
velx = 5
vely = 5

time = pygame.time.Clock()

cont = 0
fonte = pygame.font.Font(None,35)
texto = fonte.render(f'pontos:{cont}',True,(0,0,0))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if pygame.key == pygame.K_RIGHT:
                xr += 3
            if pygame.key == pygame.K_LEFT:
                xr -= 3
        if event.type == pygame.KEYUP:
            if pygame.key == pygame.K_RIGHT:
                velx = 0
            if pygame.key == pygame.K_LEFT:
                velx = 0

    xb += velx
    yb += vely

    if xb == 640 or xb == 0:
        velx *= -1
    if yb == 0:
        vely *= -1

    tela.fill(azul)
    tela.blit(texto,(20,20))
    bola = pygame.draw.circle(tela,vermelho,[xb,yb],30)
    raquete = pygame.draw.rect(tela,verde,[xr,yr,140,20])
    if pygame.Rect.colliderect(bola,raquete):
        cont += 1
        vely *= -1
        texto = fonte.render(f'pontos:{cont}',True,(0,0,0))
    pygame.display.flip()
    time.tick(60)

