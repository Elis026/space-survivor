import sys
import pygame

from src.config import *
from src.menu import Menu
from src.player import Player
from src.game import Game

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Survivor")

clock = pygame.time.Clock()

menu = Menu(tela)

estado = "MENU"

player = Player()
game = Game(tela, player)

fonte_titulo = pygame.font.SysFont("Arial", 48, bold=True)
fonte_texto = pygame.font.SysFont("Arial", 28)

rodando = True

while rodando:

    clock.tick(FPS)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:
                rodando = False

            elif estado == "MENU":

                if evento.key == pygame.K_RETURN:

                    player = Player()
                    game = Game(tela, player)

                    estado = "JOGO"

            elif estado == "JOGO":

                if evento.key == pygame.K_SPACE:
                    player.atirar()

            elif estado in ("VITORIA", "DERROTA"):

                if evento.key == pygame.K_RETURN:

                    player = Player()
                    game = Game(tela, player)

                    estado = "JOGO"

    if estado == "MENU":

        menu.desenhar()

    elif estado == "JOGO":

        game.atualizar()
        game.desenhar()

        if game.venceu():
            estado = "VITORIA"

        elif game.perdeu():
            estado = "DERROTA"

    elif estado == "VITORIA":

        tela.fill((20,120,40))

        titulo = fonte_titulo.render(
            "VOCE VENCEU!",
            True,
            (255,255,255)
        )

        tela.blit(
            titulo,
            titulo.get_rect(center=(400,180))
        )

        texto = fonte_texto.render(
            "ENTER - Jogar novamente",
            True,
            (255,255,255)
        )

        tela.blit(
            texto,
            texto.get_rect(center=(400,280))
        )

        texto2 = fonte_texto.render(
            "ESC - Sair",
            True,
            (255,255,255)
        )

        tela.blit(
            texto2,
            texto2.get_rect(center=(400,330))
        )

    elif estado == "DERROTA":

        tela.fill((150,20,20))

        titulo = fonte_titulo.render(
            "GAME OVER",
            True,
            (255,255,255)
        )

        tela.blit(
            titulo,
            titulo.get_rect(center=(400,180))
        )

        texto = fonte_texto.render(
            "ENTER - Jogar novamente",
            True,
            (255,255,255)
        )

        tela.blit(
            texto,
            texto.get_rect(center=(400,280))
        )

        texto2 = fonte_texto.render(
            "ESC - Sair",
            True,
            (255,255,255)
        )

        tela.blit(
            texto2,
            texto2.get_rect(center=(400,330))
        )

    pygame.display.flip()

pygame.quit()
sys.exit()