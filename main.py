import Reversi
from random import choice

#Renvoie une valeur, pour un joueur donner, si il est bien parti
#dans la partie ou non
# => la valeur est juste le nombre de pièce en plus ou en moins qu'il a
# face à son adversaire
def evaluate(board,joueur):
    return board.heuristique(joueur)

#Pour le moment, les joueurs jouent de façon aléatoire
def RandomMove(board):
    return choice(board.legal_moves())

#Algorithme mini-max :
def minimax(board,profondeur,player,alpha,beta):
    if profondeur == 0 or board.is_game_over():
        return evaluate(board,player)
    
    legal_moves = board.legal_moves()

    #Pour le joueur noir, nous voulons maximiser le score
    if player == Reversi.Board._BLACK:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board,profondeur - 1,player,alpha,beta)
            board.pop()

            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    
    else:
        #Pour le joueur blanc, nous voulons minimiser le score
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, profondeur - 1, player, alpha, beta)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board,profondeur,player):
    legal_moves = board.legal_moves()
    best_score = float('-inf')

    for move in legal_moves:
        board.push(move)
        score = minimax(board, profondeur - 1, player, float('-inf'), float('inf'))
        board.pop()

        if score > best_score:
            best_score = score
            best_move = move

    return best_move



nb_victoire_noir = 0
nb_victoire_blanc = 0
for j in range(20):
    #Création de la partie
    print("•••••••••••••••••••••••••")
    print("•••••••••••••••••••••••••")
    print("•••••••••••••••••••••••••")
    print("••••••••••Début••••••••••")
    print("•••••••••••••••••••••••••")
    print("•••••••••••••••••••••••••")
    print("•••••••••••••••••••••••••")
    board = Reversi.Board()
    print(board)
    print("Chance de gagner de black (gentil) : ",evaluate(board,Reversi.Board._BLACK))
    print("Chance de gagner de white (méchant) : ",evaluate(board,Reversi.Board._WHITE))

    #Tant que la partie n'est pas fini, les joueurs jouent
    while board.is_game_over() == False:

        if board._nextPlayer == Reversi.Board._BLACK:
            move = best_move(board, 3, Reversi.Board._BLACK)  # Profondeur de recherche 3 (ajustez selon les performances)
            board.push(move)
            # board.push(RandomMove(board))
        # Joueur blanc (IA) joue avec l'algorithme Minimax
        else:
            move = best_move(board, 3, Reversi.Board._WHITE)  # Profondeur de recherche 3 (ajustez selon les performances)
            board.push(move)
            # board.push(RandomMove(board))

        print(board)
        print("Chance de gagner de black (gentil) : ",evaluate(board,Reversi.Board._BLACK))
        print("Chance de gagner de white (méchant) : ",evaluate(board,Reversi.Board._WHITE))



    #On compte le nombre de pièce et on déduit un vainqueur
    if board._nbBLACK>board._nbWHITE:
        nb_victoire_noir = nb_victoire_noir+1
        print("Les noirs ont gagnés")
    else:
        nb_victoire_blanc = nb_victoire_blanc+1
        print("Les blancs ont gagnés")

print("nombre de victoire de l'ia : ",nb_victoire_blanc," , nombre victoire de noir : ", nb_victoire_noir)