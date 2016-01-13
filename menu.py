import os
import webbrowser
import time

from poqb import *
from utils import *
from Cube import *
from cubeDisplay import *
from resolution import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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
    print("/-------                                 --------\\")
    print("|                                                |")
    print("|     - 1 - Résolution d'un cube aléatoire       |")
    print("|     - 2 - Résolution d'un cube précis          |")
    print("|     - 3 - Afficher un cube précis              |")
    print("|     - 4 - Résolution via alg.cubing.net        |")
    print("|     - 5 - README                               |")
    print("|     - 6 - PERFORMANCES                         |")
    print("|     - 7 - Résolution 100 cubes et performances |")
    print("|     - 0 - Quitter                              |")
    print("|                                                |")
    print("\\-------                                --------/")
    print("")
    choix = input("Que faire ? ")
    choixMenu(choix)

def menu():
	clear()
	pageAccueil()
	affichageMenu()

def choixMenu(choix):
    if choix == "1" :
        clear()
        color54 = generator()
        cube = Cube(color54)

        print("Affichage du cube à résoudre")
        print(cube)
        print("Chaîne de mouvements : "+solve(generator()))
        input("Appuyez sur entrée pour continuer ")

        pageAccueil()
        affichageMenu()

    elif choix == "2" :
        color54 = input("Entrez une chaine de 54 couleurs correcte : ")
        clear()
        cube = Cube(color54)
        print(cube)

        print("Chaîne de mouvements : "+solve(color54))
        input("Appuyez sur entrée pour continuer ")
        pageAccueil()
        affichageMenu()

    elif choix == "3" :
        color54 = input("Entrez une chaîne de 54 couleurs valide : ")
        cube = Cube(color54)
        print(cube)

        pageAccueil()
        affichageMenu()

    elif choix == "4" :
        a,b = scramble()
        c=solve(b).replace("'","-")
        webbrowser.open("https://alg.cubing.net/?setup="+a+"&alg="+c)

        pageAccueil()
        affichageMenu()

    elif choix == "5" :
        readme = open("README.md", "r")
        print(readme.read())

        input("Appuyez sur entrée pour continuer ")
        readme.close()

        pageAccueil()
        affichageMenu()

    elif choix == "6" :
        performance = open("PERFORMANCE.md", "r")
        print(performance.read())

        input("Appuyez sur entrée pour continuer ")
        performance.close()

        pageAccueil()
        affichageMenu()

    elif choix == "7" :
        # Génération des cubes
        print("Génération de 100 cubes...")
        cubes = []
        for i in range(0, 100):
            cubes.append(generator())

        # Résolution des cubes en mesurant le temps d'exécution et le nombre de mouvements
        print("Résolution des 100 cubes...")
        nbMouv = []
        temps = 0
        for i in cubes:
            tDebut = time.clock()
            mouv = solve(i)
            tFin = time.clock()
            
            temps += tFin - tDebut
            nbMouv.append(len(mouv.replace("'", "")))

        moy = sum(nbMouv) / len(nbMouv)
        print("Temps d'exécution : " + str(temps) + " secondes")
        print("Nombre de mouvements moyen : " + str(moy))
        print("Nombre de mouvements maximum : " + str(max(nbMouv)))
        print("Nombre de mouvements minimum : " + str(min(nbMouv)))
        
        input("Appuyez sur entrée pour continuer ")
            
        pageAccueil()
        affichageMenu()
        

    elif choix == "0" :
        clear()
        print("Merci d'avoir utilisé Polycube")
        exit()
    else :
        menu()
                
                
        
menu()
