# Space Survivor

Jogo 2D em **Python + pygame**, feito na disciplina de Linguagem de Programação (UNINTER, Engenharia de Software).

Você controla uma nave, atira nos inimigos e precisa fazer **15 pontos** antes de perder as **3 vidas**.

## Como executar

```bash
pip install pygame
python main.py
```

## Controles

| Tecla | Ação |
|---|---|
| W A S D | mover a nave |
| Espaço | atirar |
| Enter | iniciar no menu e jogar de novo ao fim da partida |
| Esc | sair |

## Estrutura

```
main.py          # loop principal e estados (menu / jogo / fim)
src/config.py    # constantes (tela, FPS, cores)
src/menu.py      # tela de menu
src/player.py    # nave do jogador
src/enemy.py     # inimigos
src/bullet.py    # tiros
src/game.py      # regras, colisões, pontos e vidas
assets/images/   # imagens
```

## O que pratiquei

Programação orientada a objetos em Python, laço principal de jogo, tratamento de eventos, detecção de colisão e organização do código em módulos.
