import pygame
import random

class Enemy:

    def __init__(self):

        self.imagem = pygame.image.load(
            "assets/images/enemy.png"
        ).convert_alpha()

        self.imagem = pygame.transform.scale(
            self.imagem,
            (60, 60)
        )

        self.x = random.randint(20, 720)
        self.y = -60

        self.velocidade = random.randint(2, 5)

    def mover(self):

        self.y += self.velocidade

    def desenhar(self, tela):

        tela.blit(self.imagem, (self.x, self.y))

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            60,
            60
        )

    def saiu_da_tela(self):

        return self.y > 620