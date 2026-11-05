import pygame

class Menu:

    def __init__(self, tela):

        self.tela = tela

        self.background = pygame.image.load(
            "assets/images/background.png"
        ).convert()

        self.background = pygame.transform.scale(
            self.background,
            (800, 600)
        )

        self.titulo = pygame.font.SysFont("Arial", 52, bold=True)
        self.subtitulo = pygame.font.SysFont("Arial", 24)
        self.texto = pygame.font.SysFont("Arial", 26)
        self.pequena = pygame.font.SysFont("Arial", 18)

    def escrever_centro(self, texto, fonte, cor, y):

        render = fonte.render(texto, True, cor)

        rect = render.get_rect(center=(400, y))

        self.tela.blit(render, rect)

    def desenhar(self):

        self.tela.blit(self.background, (0, 0))

        sombra = pygame.Surface((800,600), pygame.SRCALPHA)
        sombra.fill((0,0,0,150))
        self.tela.blit(sombra,(0,0))

        self.escrever_centro(
            "SPACE SURVIVOR",
            self.titulo,
            (255,255,255),
            70
        )

        self.escrever_centro(
            "Destrua 15 naves inimigas para vencer",
            self.subtitulo,
            (255,255,0),
            120
        )

        pygame.draw.line(self.tela,(255,255,255),(170,150),(630,150),2)

        self.escrever_centro(
            "ENTER - INICIAR",
            self.texto,
            (0,255,0),
            190
        )

        self.escrever_centro(
            "ESC - SAIR",
            self.texto,
            (255,100,100),
            230
        )

        pygame.draw.line(self.tela,(255,255,255),(170,260),(630,260),2)

        self.escrever_centro(
            "CONTROLES",
            self.texto,
            (255,255,255),
            300
        )

        controles = [

            "W - Cima",

            "S - Baixo",

            "A - Esquerda",

            "D - Direita",

            "ESPACO - Atirar"

        ]

        y = 340

        for controle in controles:

            self.escrever_centro(
                controle,
                self.pequena,
                (230,230,230),
                y
            )

            y += 28

        pygame.draw.line(self.tela,(255,255,255),(170,495),(630,495),2)

        self.escrever_centro(
            "Desenvolvido por",
            self.pequena,
            (255,255,255),
            525
        )

        self.escrever_centro(
            "Elis Oliveira Souza",
            self.pequena,
            (0,255,255),
            548
        )
