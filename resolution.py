from cube import *
from CubeDisplay import *

def resolution():
    color54 = input("Entrez une chaîne de 54 caractères valide : ")
    # Ajouter une fonction de contrôle de la chaîne
    cube = cube(color54)
    motion=""

    motion+=premiere_face_couronne(cube)
    motion+=deuxieme_couronne(cube)
    motion+=croix(cube)
    motion+=correspondance(cube)
    motion+=placement_coins(cube)
    motion+=orientation_coins(cube)

    return motion

def premiere_face_couronne(cube):
    """ Effectue la première face (la face blanche) ainsi que la première couronne

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """
    pass


def deuxieme_couronne(cube):
    """ Effectue la deuxième couronne

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """
    pass


def croixTerminee(cube):
    """ Teste l'état du cube pour déterminer si la croix est faite sur la face D (en jaune)

    :param cube: objet de type cube
    :return: True si la croix est faite, False sinon
    """
    faceD = cube.getFace(5)
    jaunes = [42, 44, 45, 47] # facettes jaunes qui doivent former la croix
    croixFaite = False
    
    if faceD[0][1] in jaunes and faceD[1][0] in jaunes and faceD[1][2] in jaunes and faceD[2][1] in jaunes:
        croixFaite = True

    return croixFaite
        

def croix(cube):
    """ Effectue la croix

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """

    mouvements = ""
    jaunes = [42, 44, 45, 47] # facettes jaunes qui doivent former la croix
    fini = croixTerminee(cube)
    
    while not fini:
        faceD = cube.getFace(5)
        if faceD[0][1] in jaunes and faceD[1][0] in jaunes:
            mouvements += "R'D'B'DBR"
            cube.turnInv(3)
            cube.turnInv(5)
            cube.turnInv(4)
            cube.turn(5)
            cube.turn(4)
            cube.turn(3)
            fini = True
        elif faceD[1][0] in jaunes and faceD[2][1] in jaunes:
            mouvements += "F'D'R'DRF"
            cube.turnInv(2)
            cube.turnInv(5)
            cube.turnInv(3)
            cube.turn(5)
            cube.turn(3)
            cube.turn(2)
            fini = True
        elif faceD[2][1] in jaunes and faceD[1][2] in jaunes:
            mouvements += "L'D'F'DFL"
            cube.turnInv(1)
            cube.turnInv(5)
            cube.turnInv(2)
            cube.turn(5)
            cube.turn(2)
            cube.turn(1)
            fini = True
        else:
            fini = False
            if faceD[0][1] in jaunes and faceD[1][2] in jaunes:
                fini = True
                
            mouvements += "B'D'L'DLB"
            cube.turnInv(4)  
            cube.turnInv(5)  
            cube.turnInv(1)   
            cube.turn(5)  
            cube.turn(1)   
            cube.turn(4)
            
            if not fini:
                fini = croixTerminee(cube)
            
    return mouvements
        


def correspondance(cube):
    """ Effectue la correspondance des bords de la croix

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """
    
    # face[1][1] est une constante, elle ne bouge jamais
    # F=Front, D=Down, L=Left, R=Right, B=Back, U=Up
    # Convention : U=White=0, F=Red=2, L=Green=1, R=Blue=3, B=Orange=4, D=Yellow=5

    # sequence de retour
    sequence = ""

    # associe un numero de face avec le numero de cube qu'il doit avoir une fois la croix placée
    dic = {1: 30, 2: 33, 3: 36, 4: 39}

    green = cube.getFace(1)
    red = cube.getFace(2)
    blue = cube.getFace(3)
    orange = cube.getFace(4)
    fini = False

    aretes = []
    nbAretesBienPlacees = 0
    aretes.append(1) if green[2][1] == 30 else aretes.append(0)
    aretes.append(1) if red[2][1] == 33 else aretes.append(0)
    aretes.append(1) if blue[2][1] == 36 else aretes.append(0)
    aretes.append(1) if orange[2][1] == 39 else aretes.append(0)
    nbAretesBienPlacees = sum(1 for i in aretes if i == 1)



    # cas ou la croix est bien placée
    if nbAretesBienPlacees == 4:
        fini = True

    # cas impossible si les étapes précédentes se sont déroulées correctement
    elif nbAretesBienPlacees == 3:
        fini = True
        print("ERREUR")

    # cas où deux séquences de rotations sont nécessaires
    elif nbAretesBienPlacees == 2:
        
        # on cherche si les deux aretes bien placées se suivent
        succ = False
        for i in range(4):
            succ = succ or (arete[i] == arete[(i+1)%4] and arete[i] == 1)
        # end for

        # si elles se suivent une rotation H ou AH de la face jaune donnera une seule arete bien placee et ça on sait faire
        if succ:
            cube.turn(5)

        # si elles se suivent pas il faut une séquence entière avec une mauvaise face pour revenir sur une configuration à aucun bon
        else:
            mauvaiseFace = 1
            while 
            rotH(cube,)
        # end if


    # cas le plus simple, une séquence de rotations suffit
    elif nbAretesBienPlacees == 1:

        # on cherche si la rotation est horaire ou antihoraire
        bonneFace = aretes.index(1) + 1
        nextFace = (bonneFace % 4) + 1
        prevFace = ((bonneFace - 2) % 4) + 1
        nextArete = cube.getFace(nextFace)[2][1]

        if dic[prevFace] == nextArete:
            rotH(cube,bonneFace)
        else:
            rotH(cube,bonneFace)
        # end if
        fini = True
    # end if

    # cas ou aucune arete n'est bien placée
    else:



# end function


def rotAH(cube,face):
    opp = ((face+1)%4)+1
    cube.turn(opp)
    cube.turn(5)
    cube.turnInv(opp)
    cube.turn(5)
    cube.turn(opp)
    cube.turn2(5)
    cube.turnInv(opp)
    cube.turn2(5)
    print(cube)
# end function


def rotH(cube,face):
    opp = ((face+1)%4)+1
    cube.turnInv(opp)
    cube.turnInv(5)
    cube.turn(opp)
    cube.turnInv(5)
    cube.turnInv(opp)
    cube.turn2(5)
    cube.turn(opp)
    cube.turn2(5)
    print(cube)
# end function



def placement_coins(cube):
    """ Effectue le placement des coins autour de la croix

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """
    pass


def orientation_coins(cube):
    """ Effectue l'orientation des coins autour de la croix

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """
    pass


if __name__ == "__main__":
    # tests pour la croix jaune
    
    #cube = cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOYYBYBGYOBOYRRYOGYYGRY")
    cube = cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGBYYOYBRYYORRBYYYYOG")
    print(cube)
    print(croix(cube))
    print(cube)
    correspondance(cube)

