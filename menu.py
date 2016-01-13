import os
import webbrowser

from poqb import *
from utils import *
from cube import *
from CubeDisplay import *
from resolution import *

clear = lambda: os.system('cls')
exit = lambda: os.system('exit')


def pageAccueil():
	clear()
	print("  ____         _                      _            ")
	print(" |  _ \  ___  | | _   _   ___  _   _ | |__    ___  ")
	print(" | |_) |/ _ \ | || | | | / __|| | | || '_ \  / _ \ ")
	print(" |  __/| (_) || || |_| || (__ | |_| || |_) ||  __/ ")
	print(" |_|    \___/ |_| \__, | \___| \__,_||_.__/  \___| ")
	print("                  |___/                            ")

def affichageMenu():
    print("/-------                        --------\\")
    print("|                                       |")
    print("| - 1 - Résolution d'un cube aléatoire  |")
    print("| - 2 - Résolution d'un cube précis     |")
    print("| - 3 - Afficher un cube précis         |")
    print("| - 4 - Résolution via alg.cubing.net   |")
    print("| - 5 - README      				       |")
    print("| - 6 - PERFORMANCES      			   |")
    print("| - 0 - Quitter                         |")
    print("|                                       |")
    print("\\-------                        --------/")
    print("")
    choix = input("Que faire ? ")
    choixMenu(int(choix))

def menu():
	clear()
	pageAccueil()
	affichageMenu()

def choixMenu(choix):
    if choix == 1 :
        clear()
        color54 = generator()
        cube = cube(color54)

        print("Affichage du cube à résoudre")
        print(cube)
        print("Chaîne de mouvements : "+solve(generator()))
        os.system("pause")

        pageAccueil()
        affichageMenu()

    elif choix == 2 :
        color54 = input("Entrez une chaine de 54 couleurs correcte : ")
        clear()
        cube = cube(color54)
        print(cube)

        print("Chaîne de mouvements : "+solve(color54))
        os.system("pause")
        pageAccueil()
        affichageMenu()

    elif choix == 3 :
        color54 = input("Entrez une chaîne de 54 couleurs valide : ")
        cube = cube(color54)
        print(cube)

        pageAccueil()
        affichageMenu()

    elif choix == 4 :
        a,b = scramble()
        c=solve(b).replace("'","-")
        webbrowser.open("https://alg.cubing.net/?setup="+a+"&alg="+c)

    elif choix == 5 :
        readme = open("README.md", "r")
        print(readme.read())

        os.system("pause")
        readme.close()

        pageAccueil()
        affichageMenu()

    elif choix == 0 :
        clear()
        print("Merci d'avoir utilisé Polycube")
        exit()
    else :
        menu()
    os.system("pause")
                
                
        
menu()
