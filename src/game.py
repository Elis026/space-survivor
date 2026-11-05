import pygame
from src.enemy import Enemy

class Game:

    def __init__(self, tela, player):

        self.tela = tela
        self.player = player

        self.background = pygame.image.load(
            "assets/images/background.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (800, 600)
        )

        self.inimigos = []

        self.pontos = 0
        self.vidas = 3

        self.fonte = pygame.font.SysFont("Arial", 24, bold=True)

        self.contador = 0

    def atualizar(self):

        self.contador += 1

        # Cria um inimigo a cada 40 frames
        if self.contador >= 40:

            self.inimigos.append(Enemy())

            self.contador = 0

        for inimigo in self.inimigos[:]:

            inimigo.mover()

            # Saiu da tela
            if inimigo.saiu_da_tela():

                self.inimigos.remove(inimigo)
                self.vidas -= 1
                continue

            # Colisão com tiros
            for tiro in self.player.tiros[:]:

                if inimigo.get_rect().colliderect(tiro.get_rect()):

                    if inimigo in self.inimigos:
                        self.inimigos.remove(inimigo)

                    if tiro in self.player.tiros:
                        self.player.tiros.remove(tiro)

                    self.pontos += 1
                    break

    def desenhar(self):

        self.tela.blit(self.background, (0, 0))

        self.player.mover()
        self.player.desenhar(self.tela)

        for inimigo in self.inimigos:
            inimigo.desenhar(self.tela)

        # Barra superior
        pygame.draw.rect(
            self.tela,
            (0, 0, 0),
            (0, 0, 800, 40)
        )

        texto = self.fonte.render(
            f"Pontos: {self.pontos}     Vidas: {self.vidas}     Objetivo: 15",
            True,
            (255,255,255)
        )

        self.tela.blit(texto, (15,8))

    def venceu(self):

        return self.pontos >= 15

    def perdeu(self):

        return self.vidas <= 0