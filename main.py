import Reversi
from random import choice


def RandomMove(b):
    return choice(b.legal_moves())


print("•••••••••••••••••••••••••")
print("•••••••••••••••••••••••••")
print("•••••••••••••••••••••••••")
print("••••••••••Début••••••••••")
print("•••••••••••••••••••••••••")
print("•••••••••••••••••••••••••")
print("•••••••••••••••••••••••••")

board = Reversi.Board()
print(board)

while board.is_game_over() == False:
    board.push(RandomMove(board))
    print(board)

if board._nbBLACK>board._nbWHITE:
    print("Les noirs ont gagnés")
else:
    print("Les blancs ont gagnés")
