import pygame

class Bullet:

    def __init__(self, x, y):

        self.imagem = pygame.image.load(
            "assets/images/bullet.png"
        ).convert_alpha()

        self.imagem = pygame.transform.scale(
            self.imagem,
            (12, 35)
        )

        self.x = x
        self.y = y

        self.velocidade = 10

    def mover(self):

        self.y -= self.velocidade

    def desenhar(self, tela):

        tela.blit(self.imagem, (self.x, self.y))

    def get_rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            12,
            35
        )