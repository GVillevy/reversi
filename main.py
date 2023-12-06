import Reversi
from random import choice
import random
import time

#On evalue la situation avec notre heuristique
def evaluate(board, joueur):
    return board.heuristique_ameliore(joueur)

#Pour le moment, les joueurs jouent de façon aléatoire
def RandomMove(board):
    return choice(board.legal_moves())

def minimax(board, profondeur, player, alpha, beta,debut,tempsmax):
    if profondeur == 0 or board.is_game_over() or time.time() - debut > tempsmax:
        return evaluate(board, player)

    legal_moves = board.legal_moves()

    if player == Reversi.Board._BLACK:
        max_eval = float('-inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, profondeur - 1, player, alpha, beta,debut,tempsmax)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, profondeur - 1, player, alpha, beta,debut,tempsmax)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval



def best_move(board, profondeur, player,debut,tempsmax):

    legal_moves = board.legal_moves()
    selected_move = None
    best_score = float('-inf')
    
    for move in legal_moves:
        if time.time() - debut < tempsmax:
            board.push(move)
            score = minimax(board, profondeur - 1, player, float('-inf'), float('inf'),debut,tempsmax)
            board.pop()

            # ajout du noise afin d'avoir un peu d'hasard dans le choix du meilleur coup
            perturbation = random.uniform(-0.1, 0.1)

            if score + perturbation > best_score:
                best_score = score + perturbation
                selected_move = move
    return selected_move




def IAIterativeDeepening(board, tempsmax, player,debut):

    profondeur = 1
    meilleurmove = None

    while time.time() - debut < tempsmax and profondeur<10:
        print("couche atteinte : ", profondeur)
        move = best_move(board, profondeur, player,debut,tempsmax)
        if move is not None:
            meilleurmove = move
        else:
            break  # Sortir de la boucle si aucune réponse trouvée à cette profondeur
        profondeur += 1
    return meilleurmove






nb_victoire_noir = 0
nb_victoire_blanc = 0

#On fait jouer plusieurs parties
nombre_partie = 1

for j in range(nombre_partie):

    board = Reversi.Board()
    print(board)

    while not board.is_game_over():

        if board._nextPlayer == Reversi.Board._BLACK:
            # debut= time.time()
            # print("début de la recherche:",debut)
            # move = IAIterativeDeepening(board, 5, Reversi.Board._BLACK,debut)
            # print(move)
            # print("durée totale de recherche : ", time.time()-debut) 

            
            validmove = False

            while validmove == False and not board.is_game_over():
                moves = board.legal_moves()
                for element in moves:
                    element.pop(0)
                print("liste de coups possible : ", moves)

                while True:
                    try:
                        user_input = input("Entrez votre mouvement (par exemple, '13') pour ligne 1 colonne 3 : ")
                        test = int(user_input)
                        break
                    except ValueError:
                        print('Veuillez entrer un entier valide.')

                user_input = str(user_input)
                if len(list(user_input)) != 2 :
                    print("veuillez entrer un coup valide")
                else:
                    ligne = list(user_input)[0]
                    colonne = list(user_input)[1]
                    if(board.is_valid_move(Reversi.Board._BLACK,int(ligne),int(colonne))):
                        validmove = True
                        move = [1,int(ligne),int(colonne)]
                        print(move)
                    else:
                        print("Coup invalide, re-tentez")

            #move = RandomMove(board)
        else:
            debut= time.time()
            print("début de la recherche:",debut)
            move = IAIterativeDeepening(board, 5, Reversi.Board._WHITE,debut)
            print(move)
            print("durée totale de recherche : ", time.time()-debut)

        board.push(move)
        print(board)

        print("Chance de gagner de black (gentil) : ", evaluate(board, Reversi.Board._BLACK))
        print("Chance de gagner de white (méchant) : ", evaluate(board, Reversi.Board._WHITE))

    if board._nbBLACK > board._nbWHITE:
        nb_victoire_noir += 1
        print("Les noirs ont gagné")
    else:
        nb_victoire_blanc += 1
        print("Les blancs ont gagné")

print("Nombre de victoires de l'IA : ", nb_victoire_blanc, ", nombre de victoires de noir : ", nb_victoire_noir)
