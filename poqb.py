# poqb.py
# -*- coding: utf-8 -*-

from cube import *
from resolution import *
from random import *

def optimisation_manoeuvres(man):
    """Réduit le nombre de manoeuvres à effectuer
    :param man: la chaîne de caractères représentant les manoeuvres à effectuer
    :return: une chaîne de caractères avec moins de manoeuvres (si possible)
    """

    mouv = ["U", "D", "L", "R", "F", "B"]
    fini = False
    manOpti = list(man)

    while not fini:
        fini = True
        nouvManOpti = ""
        l = len(manOpti)
        i = 0
        while i < l:
            if manOpti[i] in mouv:
                
                # cas "UU", "RR", ...
                if (i+1 < l and manOpti[i] == manOpti[i+1] and i+2 >= l) or (i+2 < l and manOpti[i] == manOpti[i+1] and manOpti[i+2] in mouv):
                    fini = False
                    nouvManOpti += manOpti[i] + "2"
                    i += 1
                        
                # cas "U'U'", "R'R'", ...
                elif i+3 < l and manOpti[i] == manOpti[i+2] and manOpti[i+1] == manOpti[i+3] == "'":
                    fini = False
                    nouvManOpti += manOpti[i] + "2"
                    i += 3
                    
                # cas "U2U", "R2R", ...
                elif (i+2 < l and manOpti[i] == manOpti[i+2] and manOpti[i+1] == "2" and i+3 >= l) or (i+3 < l and manOpti[i] == manOpti[i+2] and manOpti[i+1] == "2" and manOpti[i+3] in mouv):
                    fini = False
                    nouvManOpti += manOpti[i] + "'"
                    i += 2
                    
                # cas "UU2", "RR2", ...
                elif i+2 < l and manOpti[i] == manOpti[i+1] and manOpti[i+2] == "2":
                    fini = False
                    nouvManOpti += manOpti[i] + "'"
                    i += 2
                    
                # cas "U2U'", "R2R'", ...
                elif i+3 < l and manOpti[i] == manOpti[i+2] and manOpti[i+1] == "2" and manOpti[i+3] == "'":
                    fini = False
                    nouvManOpti += manOpti[i]
                    i += 3
                    
                # cas "U'U2", "R'R2", ...
                elif i+3 < l and manOpti[i] == manOpti[i+2] and manOpti[i+1] == "'" and manOpti[i+3] == "2":
                    fini = False
                    nouvManOpti += manOpti[i]
                    i += 3
                    
                # cas "UU'", "RR'", ...
                elif i+2 < l and manOpti[i] == manOpti[i+1] and manOpti[i+2] == "'":
                    fini = False
                    i += 2
                    
                # cas "U'U", "R'R", ...
                elif (i+2 < l and manOpti[i] == manOpti[i+2] and manOpti[i+1] == "'" and i+3 >= l) or (i+3 < l and manOpti[i] == manOpti[i+2] and manOpti[i+1] == "'" and manOpti[i+3] in mouv):
                    fini = False
                    i += 2

                # cas "U2U2", "R2R2", ...
                elif i+3 < l and manOpti[i] == manOpti[i+2] and manOpti[i+1] == manOpti[i+3] == "2":
                    fini = False
                    i += 3

                # pas de simplification possible
                else:
                    nouvManOpti += manOpti[i]
            else:
                nouvManOpti += manOpti[i]
            i += 1
                    
        manOpti = str(nouvManOpti)

    return manOpti


def generator():
    test = cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY")
    for i in range(0,25):
        j = randint(0,5)
        test.turn(j)
    return test.cube_to_color54()



def solve(cube_c54):
    """La fonction principale du projet qui résoud un Rubik's Cube.

    :param cube_c54: passé sous sa forme '54 facettes colorées'
           O G R
           B W Y
           B G B
    G Y Y  O Y O  W O W  G R Y
    O O O  B G B  R R Y  R B W
    W W R  B W Y  G R O  W G R
           Y B R
           G Y W
           B O G
    :return: une chaîne de caractères qui encode la manoeuvre
    qui mène du cube de départ à la permutation monochrome.

    :Example:

    solve('OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG')

    """

    
    c = cube(cube_c54)

    motion=premiere_face_couronne(c)
    motion+=deuxieme_couronne(c)
    motion+=croix(c)
    motion+=correspondance(c)
    motion+=placement_coins(c)
    motion+=orientation_coins(c)
    
    return motion


if __name__=="__main__":
    #cube = 'OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG'
    #print ("Pour la résolution de {}\nExécuter la manoeuvre {}".format(cube, solve(cube)))
    #print(generator())
    
    color54 = input("Entrez une chaîne de 54 caractères valide : ")
    # Ajouter une fonction de contrôle de la chaîne

    sol = solve(color54)
    print(sol)
