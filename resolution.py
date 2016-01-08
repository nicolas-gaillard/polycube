from cube import *
from CubeDisplay import *
from couronne1 import *

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

def croix_blanche(cube):
    pass

def premiere_face_couronne(cube):
    return couronne1(cube)
    """ Effectue la première face (la face blanche) ainsi que la première couronne

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """


def deuxieme_couronne(cube):
    """ Effectue la deuxième couronne

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """
    pass


def croixTerminee(cube):
    """ Teste l"état du cube pour déterminer si la croix est faite sur la face D (en jaune)

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

    # sequence de retour
    sequence = ""

    # associe un numero de face avec le numero de cube qu'il doit avoir une fois la croix placée
    dic = {1: 30, 2: 33, 3: 36, 4: 39}

    # tant que la croix jaune ne correspond pas avec les côtés adjacents
    fini = False
    while not fini:

        aretes = []
        aretes.append(1) if cube.getFace(1)[2][1] == 30 else aretes.append(0)
        aretes.append(1) if cube.getFace(2)[2][1] == 33 else aretes.append(0)
        aretes.append(1) if cube.getFace(3)[2][1] == 36 else aretes.append(0)
        aretes.append(1) if cube.getFace(4)[2][1] == 39 else aretes.append(0)
        nbAretesBienPlacees = sum(1 for i in aretes if i == 1)

        # cas où la croix est bien placée
        if nbAretesBienPlacees == 4:
            fini = True

        # cas impossible si les étapes précédentes se sont déroulées correctement
        elif nbAretesBienPlacees == 3:
            fini = True
            print("ERREUR")

        # cas où deux séquences de rotations sont nécessaires
        elif nbAretesBienPlacees == 2:
            
            # on cherche si les deux arêtes bien placées se suivent
            succ = False
            for i in range(4):
                succ = succ or (aretes[i] == aretes[(i+1)%4] and aretes[i] == 1)
            # end for

            # si elles se suivent une rotation H ou AH de la face jaune donnera une seule arête bien placée et ça on sait faire
            if succ:
                cube.turn(5)
                sequence += "D"

            # si elles se suivent pas il faut une séquence entière avec une mauvaise face pour revenir sur une configuration à 0 bien placées
            else:
                idFace = 1
                while dic[idFace] == cube.getFace(idFace)[2][1] and idFace < 4:
                    idFace += 1
                # end while
                sequence += rotH(cube,idFace)
            # end if



        # cas le plus simple, une séquence de rotations suffit
        elif nbAretesBienPlacees == 1:

            # on cherche si la rotation est horaire ou antihoraire
            bonneFace = aretes.index(1) + 1
            nextFace = (bonneFace % 4) + 1
            prevFace = ((bonneFace - 2) % 4) + 1
            nextArete = cube.getFace(nextFace)[2][1]

            if dic[prevFace] == nextArete:
                sequence += rotH(cube,bonneFace)
            else:
                sequence += rotAH(cube,bonneFace)
            # end if

        # cas ou aucune arete n"est bien placée
        else:
            cube.turn(5)
            sequence += "D"
    # end while

    return sequence

# end function


def rotAH(cube,face):
    """ Effectue une suite de mouvements destinés à faire tourner 3 des 4 arêtes d'une même face dans le sens antihoraire (AH)

    :param cube: objet de type cube (voir cube.py)
    :param face: la face dont l'arête ne tournera pas
    :return: une chaîne de caractères décrivant les mouvements effectués
    """

    # correspondance entre le numero de face et la lettre du mouvement
    dic = {1: "L", 2: "F", 3: "R", 4: "B"}
    dicInv = {1: "L'", 2: "F'", 3: "R'", 4: "B'"}

    # numero de la face opposée
    opp = ((face+1)%4)+1

    cube.turn(opp)
    cube.turn(5)
    cube.turnInv(opp)
    cube.turn(5)
    cube.turn(opp)
    cube.turn2(5)
    cube.turnInv(opp)
    cube.turn2(5)

    # séquence de retour correspondant à la suite de mouvements
    return dic[opp] + "D" + dicInv[opp] + "D" + dic[opp] + "D2" + dicInv[opp] + "D2"

# end function


def rotH(cube,face):
    """ Effectue une suite de mouvements destinés à faire tourner 3 des 4 arêtes d'une même face dans le sens horaire (H)

    :param cube: objet de type cube (voir cube.py)
    :param face: la face dont l'arête ne tournera pas
    :return: une chaîne de caractères décrivant les mouvements effectués
    """
    # correspondance entre le numero de face et la lettre du mouvement
    dic = {1: "L", 2: "F", 3: "R", 4: "B"}
    dicInv = {1: "L'", 2: "F'", 3: "R'", 4: "B'"}

    # numero de la face opposée
    opp = ((face+1)%4)+1

    cube.turnInv(opp)
    cube.turnInv(5)
    cube.turn(opp)
    cube.turnInv(5)
    cube.turnInv(opp)
    cube.turn2(5)
    cube.turn(opp)
    cube.turn2(5)

    # séquence de retour correspondant à la suite de mouvements
    return dicInv[opp] + "D'" + dic[opp] + "D'" + dicInv[opp] + "D2" + dic[opp] + "D2"
# end function


def placement_coins(cube):
    """ Effectue le placement des coins sur la face jaune, l'orientation sera faite après

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """
    pass   
#end function


def orientation_coins(cube):
    """ Effectue l"orientation des coins autour de la croix

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """
    pass


if __name__ == "__main__":

    # tests pour la correspondance croix jaune
    

    # 1) cube 1 bien placé rot AH ==> checked
    c = cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOOOGRRYRGYBBYYYBYYYGYO")

    # 2) cube 1 bien placé rot H ==> checked
    c = cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOYBRYRRBOOYGGGYYYYYOYB")

    # 3) cube 2 bien placé a la suite ==> checked
    c = cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOYGGYBGRRBYOOOYYYYYBYR")

    # 4) cube 2 bien placé opposés ==> checked
    c = cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOYGYOOYGBBYROGYRYYYBYR")

    # 5) cas parfait le cube est deja resolu
    c = cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY")

    print(c)
    print(correspondance(c))
    print(c)
