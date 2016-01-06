from cube import *
from CubeDisplay import *

def premiere_face_couronne(cube):
    """ Effectue la première face (la face blanche) ainsi que la première couronne

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """
    pass

def deuxieme_couronne_terminee(cube):
    """ Teste l'état du cube pour déterminer si la deuxième couronne a été réalisée
    Cela veut dire que la face U(p) est entièrement blanche, et que les faces adjacentes 
    (L(eft),F(ront),R(ight),B(ack)) aient respectivement deux niveaux de couleur verte,
    rouge, bleu et orange

    :param cube: objet de type cube
    :return: True si la deuxieme couronne est faite, False sinon
    """

    deuxieme_couronne_faite = True

    faceL = cube.getFace(1)
    faceF = cube.getFace(2)
    faceR = cube.getFace(3)
    faceB = cube.getFace(4)

    vert = [9,10,11,21,22]
    rouge = [12,13,14,23,24]
    bleu = [15,16,17,25,26]
    orange = [18,19,20,27,28]

    if faceL[0][0] not in vert or faceL[0][1] not in vert or faceL[0][2] not in vert or faceL[1][0] not in vert or faceL[1][2] not in vert:
        deuxieme_couronne_faite = False

    if faceF[0][0] not in rouge or faceF[0][1] not in rouge or faceF[0][2] not in rouge or faceF[1][0] not in rouge or faceF[1][2] not in rouge:
        deuxieme_couronne_faite = False

    if faceR[0][0] not in bleu or faceR[0][1] not in bleu or faceR[0][2] not in bleu or faceR[1][0] not in bleu or faceR[1][2] not in bleu :
        deuxieme_couronne_faite = False

    if faceB[0][0] not in orange or faceB[0][1] not in orange or faceB[0][2] not in orange or faceB[1][0] not in orange or faceB[1][2] not in orange:
        deuxieme_couronne_faite = False

    return deuxieme_couronne_faite

def demarrage_deuxieme_couronne(cube):
    """ Oriente les couleurs de la premiere couronne vers la bonne face 

    :prerequis: la face blanche doit etre faite, ainsi que la premiere couronne
    :param cube: objet de type cube 
    """

    faceL = cube.getFace(1)

    vert = [9,10,11]

    while faceL[0][0] not in vert and faceL[0][1] not in vert and faceL[0][2] not in vert:
        cube.turn(0)

def deuxieme_couronne(cube):
    """ Effectue la deuxième couronne

    :param cube: objet de type cube (voir cube.py)
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """
    mouvements = ""

    demarrage_deuxieme_couronne(cube)

    fin = deuxieme_couronne_terminee(cube)

    arete_vert = [10,21,22,30]
    arete_rouge = [13,23,24,33]
    arete_bleu = [16,25,26,36]
    arete_orange = [19,27,28,39]

    while fin == False:
        faceL = cube.getFace(1)
        faceF = cube.getFace(2)
        faceR = cube.getFace(3)
        faceB = cube.getFace(4)
        faceD = cube.getFace(5)
        if faceL[2][1] in arete_vert:
            if faceD[1][0] in arete_rouge:
                mouvements += "D'F'DFDLD'L'"
                cube.turnInv(5)
                cube.turnInv(2)
                cube.turn(5)
                cube.turn(2)
                cube.turn(5)
                cube.turn(1)
                cube.turnInv(5)
                cube.turnInv(1)
            elif faceD[1][0] in arete_orange:
                mouvements += "DBD'B'D'L'DL"
                cube.turn(5)
                cube.turn(4)
                cube.turnInv(5)
                cube.turnInv(4)
                cube.turnInv(5)
                cube.turnInv(1)
                cube.turn(5)
                cube.turn(1)
            else:
                if faceF[2][1] not in arete_rouge and faceR[2][1] not in arete_bleu and faceB[2][1] not in arete_orange:
                    mouvements += "D"
                    cube.turn(5)
                pass
        faceL = cube.getFace(1)
        faceF = cube.getFace(2)
        faceR = cube.getFace(3)
        faceB = cube.getFace(4)
        faceD = cube.getFace(5)
        if faceF[2][1] in arete_rouge:
            if faceD[0][1] in arete_bleu:
                mouvements += "D'R'DRDFD'F'"
                cube.turnInv(5)
                cube.turnInv(3)
                cube.turn(5)
                cube.turn(3)
                cube.turn(5)
                cube.turn(2)
                cube.turnInv(5)
                cube.turnInv(2)
            elif faceD[0][1] in arete_vert:
                mouvements += "DLD'L'D'F'DF"
                cube.turn(5)
                cube.turn(1)
                cube.turnInv(5)
                cube.turnInv(1)
                cube.turnInv(5)
                cube.turnInv(2)
                cube.turn(5)
                cube.turn(2)
            else:
                if faceL[2][1] not in arete_vert and faceR[2][1] not in arete_bleu and faceB[2][1] not in arete_orange:
                    mouvements += "D"
                    cube.turn(5)
                pass
        faceL = cube.getFace(1)
        faceF = cube.getFace(2)
        faceR = cube.getFace(3)
        faceB = cube.getFace(4)
        faceD = cube.getFace(5)
        if faceR[2][1] in arete_bleu:
            if faceD[1][2] in arete_orange:
                mouvements += "D'B'DBDRD'R'"
                cube.turnInv(5)
                cube.turnInv(4)
                cube.turn(5)
                cube.turn(4)
                cube.turn(5)
                cube.turn(3)
                cube.turnInv(5)
                cube.turnInv(3)
            elif faceD[1][2] in arete_rouge:
                mouvements += "DFD'F'D'R'DR"
                cube.turn(5)
                cube.turn(2)
                cube.turnInv(5)
                cube.turnInv(2)
                cube.turnInv(5)
                cube.turnInv(3)
                cube.turn(5)
                cube.turn(3)
            else:
                if faceL[2][1] not in arete_vert and faceF[2][1] not in arete_rouge and faceB[2][1] not in arete_orange:
                    mouvements += "D"
                    cube.turn(5)
                pass
        faceL = cube.getFace(1)
        faceF = cube.getFace(2)
        faceR = cube.getFace(3)
        faceB = cube.getFace(4)
        faceD = cube.getFace(5)
        if faceB[2][1] in arete_orange:
            if faceD[2][1] in arete_vert:
                mouvements += "D'L'DLDBD'B'"
                cube.turnInv(5)
                cube.turnInv(1)
                cube.turn(5)
                cube.turn(1)
                cube.turn(5)
                cube.turn(4)
                cube.turnInv(5)
                cube.turnInv(4)
            elif faceD[2][1] in arete_bleu:
                mouvements += "DRD'R'D'B'DB"
                cube.turn(5)
                cube.turn(3)
                cube.turnInv(5)
                cube.turnInv(3)
                cube.turnInv(5)
                cube.turnInv(4)
                cube.turn(5)
                cube.turn(4)
            else:
                if faceL[2][1] not in arete_vert and faceF[2][1] not in arete_rouge and faceR[2][1] not in arete_bleu:
                    mouvements += "D"
                    cube.turn(5)
                pass
        faceL = cube.getFace(1)
        faceF = cube.getFace(2)
        faceR = cube.getFace(3)
        faceB = cube.getFace(4)
        faceD = cube.getFace(5)
        if faceL[2][1] not in arete_vert and faceF[2][1] not in arete_rouge and faceR[2][1] not in arete_bleu and faceB[2][1] not in arete_orange:
            mouvements += "D"
            cube.turn(5)
        faceL = cube.getFace(1)
        faceF = cube.getFace(2)
        faceR = cube.getFace(3)
        faceB = cube.getFace(4)
        faceD = cube.getFace(5)
        if croixTerminee(cube) and fin == False:
            if faceL[2][1] in arete_vert and faceL[1][0] not in arete_vert:
                mouvements += "DBD'B'D'L'DL"
                cube.turn(5)
                cube.turn(4)
                cube.turnInv(5)
                cube.turnInv(4)
                cube.turnInv(5)
                cube.turnInv(1)
                cube.turn(5)
                cube.turn(1)
            elif faceL[2][1] in arete_vert and faceL[1][2] not in arete_vert:
                mouvements += "D'F'DFDLD'L'"
                cube.turnInv(5)
                cube.turnInv(2)
                cube.turn(5)
                cube.turn(2)
                cube.turn(5)
                cube.turn(1)
                cube.turnInv(5)
                cube.turnInv(1)
            elif faceF[2][1] in arete_rouge and faceF[1][0] not in arete_rouge:
                mouvements += "DLD'L'D'F'DF"
                cube.turn(5)
                cube.turn(1)
                cube.turnInv(5)
                cube.turnInv(1)
                cube.turnInv(5)
                cube.turnInv(2)
                cube.turn(5)
                cube.turn(2)
            elif faceF[2][1] in arete_rouge and faceF[1][2] not in arete_rouge:
                mouvements += "D'R'DRDFD'F'"
                cube.turnInv(5)
                cube.turnInv(3)
                cube.turn(5)
                cube.turn(3)
                cube.turn(5)
                cube.turn(2)
                cube.turnInv(5)
                cube.turnInv(2)
            elif faceR[2][1] in arete_bleu and faceR[1][0] not in arete_bleu:
                mouvements += "DFD'F'D'R'DR"
                cube.turn(5)
                cube.turn(2)
                cube.turnInv(5)
                cube.turnInv(2)
                cube.turnInv(5)
                cube.turnInv(3)
                cube.turn(5)
                cube.turn(3)
            elif faceR[2][1] in arete_bleu and faceR[1][2] not in arete_bleu:
                mouvements += "D'B'DBDRD'R'"
                cube.turnInv(5)
                cube.turnInv(4)
                cube.turn(5)
                cube.turn(4)
                cube.turn(5)
                cube.turn(3)
                cube.turnInv(5)
                cube.turnInv(3)
            elif faceB[2][1] in arete_orange and faceB[1][0] not in arete_orange:
                mouvements += "DRD'R'D'B'DB"
                cube.turn(5)
                cube.turn(3)
                cube.turnInv(5)
                cube.turnInv(3)
                cube.turnInv(5)
                cube.turnInv(4)
                cube.turn(5)
                cube.turn(4)
            elif faceB[2][1] in arete_orange and faceB[1][2] not in arete_orange:
                mouvements += "D'L'DLDBD'B'"
                cube.turnInv(5)
                cube.turnInv(1)
                cube.turn(5)
                cube.turn(1)
                cube.turn(5)
                cube.turn(4)
                cube.turnInv(5)
                cube.turnInv(4)
        if fin == False:
            fin = deuxieme_couronne_terminee(cube)
    return mouvements

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
    pass


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
    #tests pour la deuxieme couronne
    cube = cube("WWWWWWWWWGGGRRRBBBOOORGYGRGOBRYOBRGYGYYOOBOYYROGRYBBBY")
    drawCube(cube.cube_to_color54())
    print(deuxieme_couronne(cube))
    drawCube(cube.cube_to_color54())

    # tests pour la croix jaune
    #cube = cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOYYBYBGYOBOYRRYOGYYGRY")
    #cube = cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGBYYOYBRYYORRBYYYYOG")
    print(croix(cube))
    drawCube(cube.cube_to_color54())
    #print(croix(cube))
    