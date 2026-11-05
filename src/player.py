import pygame
from src.bullet import Bullet

class Player:

    def __init__(self):

        self.imagem = pygame.image.load(
            "assets/images/player.png"
        ).convert_alpha()

        # Tamanho da nave
        self.imagem = pygame.transform.scale(
            self.imagem,
            (70, 70)
        )

        # Posição inicial
        self.x = 365
        self.y = 500

        # Velocidade
        self.velocidade = 6

        # Lista de tiros
        self.tiros = []

    def mover(self):

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_a]:
            self.x -= self.velocidade

        if teclas[pygame.K_d]:
            self.x += self.velocidade

        if teclas[pygame.K_w]:
            self.y -= self.velocidade

        if teclas[pygame.K_s]:
            self.y += self.velocidade

        # Limites da tela
        if self.x < 0:
            self.x = 0

        if self.x > 730:
            self.x = 730

        if self.y < 0:
            self.y = 0

        if self.y > 530:
            self.y = 530

    def atirar(self):

        # Faz o tiro sair aproximadamente do centro da nave
        tiro = Bullet(
            self.x + 34,
            self.y + 5
        )

        self.tiros.append(tiro)

    def desenhar(self, tela):

        tela.blit(self.imagem, (self.x, self.y))

        for tiro in self.tiros[:]:

            tiro.mover()
            tiro.desenhar(tela)

            if tiro.y < -40:
                self.tiros.remove(tiro)