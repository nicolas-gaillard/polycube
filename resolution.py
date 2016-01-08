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



def placementOK(cube):
    """ On verifie si les coins sont bien placés

    :param cube: objet de type cube (voir cube.py)
    :return: booléen
    """

    #récupération des faces sauf up qui est finie
    L=cube.getFace(1)
    F=cube.getFace(2)
    R=cube.getFace(3)
    B=cube.getFace(4)
    D=cube.getFace(5)

    #recuperation des coins s'ils sont biens formés
    LFD, RFD , LBD , RBD =[31,32,41] , [34,35,43] , [46,29,40] , [37,38,48]

    #booléen de verification
    coinsOK = False
    bonCoin=[]

    #test du bon placement des différents coins
    if (L[2][0] in LBD) and (D[2][0] in LBD) and (B[2][2] in LBD): #ici le coin LBD
        bonCoin.append('LBD')
    if (L[2][2] in LFD) and (D[0][0] in LFD) and (F[2][0] in LFD): #ici le coin LFD
        bonCoin.append('LFD')
    if (R[2][0] in RFD) and (D[0][2] in RFD) and (F[2][2] in RFD): #ici le coin RFD
        bonCoin.append('RFD')
    if (R[2][2] in RBD) and (D[2][2] in RBD) and (B[2][0] in RBD): #ici le coin RBD
        bonCoin.append('RBD')
        
    #si tous les coins sont biens placés on change le booléen
                    
    if len(bonCoin) == 4: coinsOK = True

    return coinsOK,bonCoin

# end function


def placement_coins(cube):
""" Effectue le placement des coins sur la face jaune, l'orientation sera faite après

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """

    LFD, RFD , LBD , RBD =[31,32,41] , [34,35,43] , [46,29,40] , [37,38,48]
    mvm = ""

    while not placementOK(cube)[0]:
        if placementOK(cube)[1] == []:
            """Il n'y a aucun coin de bien placé donc on peut faire une des formules ci-dessous
            peu importe laquelle qui permettra de placer un coin et d'enchainer"""
            cube.turnInv(4)
            cube.turn(2)
            cube.turnInv(5)
            cube.turn(4)
            cube.turn(5)
            cube.turnInv(2)
            cube.turnInv(5)
            cube.turnInv(4)
            cube.turn(5)
            cube.turn(4)
            mvm+="B'FD'BDF'D'B'DB"

        else:
            if placementOK(cube)[1][0] == 'RFD':    #le coin RFD est bien placé

                #si on doit tourner dans le sens horaire
                if cube.getFace(1)[2][2] in RBD and cube.getFace(2)[2][0] in RBD and cube.getFace(5)[0][0] in RBD :
                    cube.turnInv(4)
                    cube.turn(2)
                    cube.turn(5)
                    cube.turnInv(2)
                    cube.turnInv(5)
                    cube.turn(4)
                    cube.turn(5)
                    cube.turn(2)
                    cube.turnInv(5)
                    cube.turnInv(2)
                    mvm+="B'FDF'D'BDFD'F'"

                # sens antihoraire
                else:
                    cube.turnInv(3)
                    cube.turn(1)
                    cube.turnInv(5)
                    cube.turn(3)
                    cube.turn(5)
                    cube.turnInv(1)
                    cube.turnInv(5)
                    cube.turnInv(3)
                    cube.turn(5)
                    cube.turn(3)
                    mvm += "R'LD'RDL'D'RDR"
                    
                
            elif placementOK(cube)[1][0] == 'LFD':    #le coin LFD est bien placé
                #sens horaire
                if cube.getFace(1)[2][0] in RFD and cube.getFace(4)[2][2] in RFD and cube.getFace(5)[2][0] in RFD :
                    cube.turnInv(3)
                    cube.turn(1)
                    cube.turn(5)
                    cube.turnInv(1)
                    cube.turnInv(5)
                    cube.turn(3)
                    cube.turn(5)
                    cube.turn(1)
                    cube.turnInv(5)
                    cube.turnInv(1)
                    mvm+="R'LDL'D'RDLD'L'"

                #sens antihoraire
                else:
                    cube.turnInv(2)
                    cube.turn(4)
                    cube.turnInv(5)
                    cube.turn(2)
                    cube.turn(5)
                    cube.turnInv(4)
                    cube.turnInv(5)
                    cube.turnInv(2)
                    cube.turn(5)
                    cube.turn(2)
                    mvm+="F'BD'FDB'D'F'DF"

            elif placementOK(cube)[1][0] == 'LBD':    #le coin LBD est bien placé
                #sens horaire
                if cube.getFace(3)[2][2] in LFD and cube.getFace(4)[2][0] in LFD and cube.getFace(5)[2][2] in LFD :
                    cube.turnInv(2)
                    cube.turn(4)
                    cube.turn(5)
                    cube.turnInv(4)
                    cube.turnInv(5)
                    cube.turn(2)
                    cube.turn(5)
                    cube.turn(4)
                    cube.turnInv(5)
                    cube.turnInv(4)
                    mvm+="F'BDB'D'FDBD'B'"

                #sens antihoraire
                else:
                    cube.turnInv(1)
                    cube.turn(3)
                    cube.turnInv(5)
                    cube.turn(1)
                    cube.turn(5)
                    cube.turnInv(3)
                    cube.turnInv(5)
                    cube.turnInv(1)
                    cube.turn(5)
                    cube.turn(1)
                    mvm+="L'RD'LDR'D'L'DL"

            elif placementOK(cube)[1][0] == 'RBD':  #le coin RBD est bien placé
                #sens horaire
                if cube.getFace(2)[2][2] in LBD and cube.getFace(3)[2][0] in LBD and cube.getFace(5)[0][2] in LBD :
                    cube.turnInv(1)
                    cube.turn(3)
                    cube.turn(5)
                    cube.turnInv(3)
                    cube.turnInv(5)
                    cube.turn(1)
                    cube.turn(5)
                    cube.turn(3)
                    cube.turnInv(5)
                    cube.turnInv(3)
                    mvm+="L'RDR'D'LDRD'R'"  

                #sens antihoraire
                else:          
                    cube.turnInv(4)
                    cube.turn(2)
                    cube.turnInv(5)
                    cube.turn(4)
                    cube.turn(5)
                    cube.turnInv(2)
                    cube.turnInv(5)
                    cube.turnInv(4)
                    cube.turn(5)
                    cube.turn(4)
                    mvm+="B'FD'BDF'D'B'DB"
    return mvm       
# end function


def orientation_coins(cube):
    """ Retourne les coins placés pour les mettre dans le bon sens

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """

    mvm = ""
    bas = cube.getFace(5)
    jaunes=[41,43,46,48]

    while not (bas[0][0] in jaunes and bas[0][2] in jaunes and bas[2][0] in jaunes and bas[2][2] in jaunes):
        for face in range(1,4):
            faceOpp = ((face+1)%4)+1
            faceSuiv = (face%4)+1

            if cube.getFace(face)[2][0] in jaunes and cube.getFace(face)[2][2] in jaunes:
                mvm += rotationCoins(cube,face)

            elif cube.getFace(face)[2][2] in jaunes and cube.getFace(faceSuiv)[2][2] in jaunes and cube.getFace(faceOpp)[2][2] in jaunes:
                mvm += rotationCoins(cube,faceOpp)

            elif cube.getFace(face)[2][0] in jaunes and cube.getFace(faceSuiv)[2][0] in jaunes and cube.getFace(faceOpp)[2][0] in jaunes:
                mvm += rotationCoins(cube,face)

            elif cube.getFace(face)[2][0] in jaunes and cube.getFace(faceSuiv)[2][2] in jaunes:
                mvm += rotationCoins(cube,face)

            elif cube.getFace(face)[2][2] in jaunes and cube.getFace(faceOpp)[2][0] in jaunes:
                mvm += rotationCoins(cube,face,False)

    return mvm
# end function


def rotationCoins(cube,face,test=True):
    """la formule pour toutes les rotations a appliquer dans le bon sens"""
    dico = {1: "L", 2: "F", 3: "R", 4: "B"}
    if test:
        faceOpp = ((face+1)%4)+1

        cube.turn(face)
        cube.turn2(5)
        cube.turnInv(face)
        cube.turnInv(5)
        cube.turn(face)
        cube.turnInv(5)
        cube.turnInv(face)
        cube.turnInv(faceOpp)
        cube.turn2(5)
        cube.turn(faceOpp)
        cube.turn(5)
        cube.turnInv(faceOpp)
        cube.turn(5)
        cube.turn(faceOpp)
        return dico[face]+"D2"+dico[face]+"'"+"D'"+dico[face]+"D'"+dico[face]+"'"+dico[faceOpp]+"'D2"+dico[faceOpp]+"D"+dico[faceOpp]+"'D"+dico[faceOpp]

    else:
        faceSuiv = (face%4)+1

        cube.turn(5)
        cube.turn2(faceSuiv)
        cube.turnInv(5)
        cube.turnInv(faceSuiv)
        cube.turn(5)
        cube.turnInv(faceSuiv)
        cube.turnInv(5)
        cube.turnInv(0)
        cube.turn2(faceSuiv)
        cube.turn(0)
        cube.turn(faceSuiv)
        cube.turnInv(0)
        cube.turn(faceSuiv)
        cube.turn(0)
        return "D"+dico[faceSuiv]+"2D'"+dico[faceSuiv]+"'D"+dico[faceSuiv]+"'D'U'"+dico[faceSuiv]+"2U"+dico[faceSuiv]+"U'"+dico[faceSuiv]+"U"

#end function


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