from Editor import Editor
from Game import Game
import pickle




board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]




print("Bienvenue !")
print("[1] : Lancer le jeu")
print("[2] : Lancer l'éditeur de map")
choix = input("Réponse (1 ou 2) : ")
editor = Editor()
if choix == "1":
    map = input("Entrez le nom du fichier de la map : ")
    board = open("boards/{}.txt".format(map), "rb")
    board = pickle.load(board)
    game = Game(board)
    game.init()
elif choix == "2":
    editor.init()
else:
    print("Pas un choix")