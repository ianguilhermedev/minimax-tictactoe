# Jogo da Velha com IA (Minimax)

Jogo da velha em Python, jogado no terminal, contra um bot que usa o algoritmo **minimax** para jogar de forma perfeita.

## Como jogar

```bash
python tic_tac_toe_minmax.py
```

Informe a linha (`X`) e a coluna (`Y`) da jogada (valores de `0` a `2`).

## Como funciona

- `get_ai_move()` testa todas as jogadas livres e escolhe a melhor com base no `minimax()`.
- `minimax()` simula recursivamente as próximas jogadas, alternando entre maximizar o resultado do bot (`X`) e minimizar o do jogador (`O`), até vitória, derrota ou empate.
- `get_winner()` / `board_full()` verificam fim de jogo (linha, coluna, diagonal ou empate).

## Requisitos

Apenas Python 3, sem dependências externas.
