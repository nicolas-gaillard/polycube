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
    print("| - 3 - Afficher un cube                |")
    print("| - 4 - Résolution via alg.cubing.net   |")
    print("| - 5 - README      				       |")
    print("| - 6 - PERFORMANCES      			   |")
    print("| - 7 - Téléchargement en continu       |")
    print("| - 8 - Téléchargement depuis fichier   |")
    print("| - 0 - Quitter                         |")
    print("|                                       |")
    print("\\-------                        --------/")
    print("")
    choix = input("Que faire ?")
    gestionMenu(int(choix))

def menu():
	clear()
	pageAccueil()
	affichageMenu()

def choixMenu(choix):
    if choix == 1 :
    elif choix == 2 :
    elif choix == 3 :
    elif choix == 4 :
    elif choix == 0 :
        clear()
        print("Merci d'avoir utilisé Polycube")
        exit()
    else :
        menu()
    os.system("pause")
                
                
        
menu()
