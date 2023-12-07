Fonctionnement de l'IA :
Notre IA utilise la fonction heuristique_amélioré afin d'évaluer un coup à jouer.

Elle attribue une valeur à chaque coup de fonction de plusieurs critères :
    - Notre IA donnera plus de valeur aux jetons se trouvant sur côtés et dans les coins, car ce sont des pièces plus difficile à récupérer
    - Elle donnera plus de valeur aux coups lui permettant d'avoir la meilleur "mobilité", c-a-d le nombre de possibilité de coup dans le futur
    - Elle donnera plus de valeur aux coups lui permettant de creuser l'écart du nombre de jeton avec l'adversaire

De plus, notre IA a deux "modes" :
    - Si notre IA a l'avantage sur son adversaire, elle va essayer de jouer de façon agressif afin de l'éliminer rapidement
    - Si notre IA est en désantavage sur le nombre de pièce, elle va essayer de jouer défensivement en essayant de maximiser ses possibilités
    de coups dans le futur et également de plus jouer les coins et côtés.

Par défaut, lorsque vous exécutez le main.py, vous pouvez jouer directement contre l'IA (qui a 10 secondes de réflexion par défaut), en
écrivant des entiers sur le clavier. Par exemple, si vous souhaitez poser un jeton sur la case ligne 1 colonne 5, il faudra écrire 15 sur
le clavier.

Bon jeu.