from Cube import *
from cubeDisplay import *
import resolution


def deuxieme_couronne_terminee(cube):
    """ Teste l'état du cube pour déterminer si la deuxième couronne a été réalisée
    Cela veut dire que la face U(p) est entièrement blanche, et que les faces adjacentes 
    (L(eft),F(ront),R(ight),B(ack)) aient respectivement deux niveaux de couleur verte,
    rouge, bleu et orange

    :param cube: objet de type Cube
    :return: True si la deuxieme couronne est faite, False sinon
    """

    deuxieme_couronne_faite = True

    # Récupération des faces concernées par la deuxième couronne
    faceL = cube.getFace(1)
    faceF = cube.getFace(2)
    faceR = cube.getFace(3)
    faceB = cube.getFace(4)

    vert = [9,10,11,21,22] # Faces vertes lorsque la deuxième couronne est finie
    rouge = [12,13,14,23,24] # Faces rouges lorsque la deuxième couronne est finie
    bleu = [15,16,17,25,26] # Faces bleues lorsque la deuxième couronne est finie
    orange = [18,19,20,27,28] # Faces oranges lorsque la deuxième couronne est finie

    # Si les deux couronnes de la face verte ne sont pas complétées, alors la fonction n'est pas finie
    if faceL[0][0] not in vert or faceL[0][1] not in vert or faceL[0][2] not in vert or faceL[1][0] not in vert or faceL[1][2] not in vert:
        deuxieme_couronne_faite = False

    # Si les deux couronnes de la face rouge ne sont pas complétées, alors la fonction n'est pas finie
    if faceF[0][0] not in rouge or faceF[0][1] not in rouge or faceF[0][2] not in rouge or faceF[1][0] not in rouge or faceF[1][2] not in rouge:
        deuxieme_couronne_faite = False

    # Si les deux couronnes de la face bleue ne sont pas complétées, alors la fonction n'est pas finie
    if faceR[0][0] not in bleu or faceR[0][1] not in bleu or faceR[0][2] not in bleu or faceR[1][0] not in bleu or faceR[1][2] not in bleu :
        deuxieme_couronne_faite = False

    # Si les deux couronnes de la face orange ne sont pas complétées, alors la fonction n'est pas finie
    if faceB[0][0] not in orange or faceB[0][1] not in orange or faceB[0][2] not in orange or faceB[1][0] not in orange or faceB[1][2] not in orange:
        deuxieme_couronne_faite = False

    return deuxieme_couronne_faite



def demarrage_deuxieme_couronne(cube):
    """ Oriente les couleurs de la premiere couronne vers la bonne face 

    :prerequis: la face blanche doit etre faite, ainsi que la premiere couronne
    :param cube: objet de type Cube 
    """

    mouvements = ""

    faceL = cube.getFace(1)

    vert = [9,10,11]

    # Tant que la face verte n'est pas correctement placée, alors aucune des faces ne sont bien placées et on ne peut commencer la résolution de la deuxième couronne
    while faceL[0][0] not in vert and faceL[0][1] not in vert and faceL[0][2] not in vert:
        mouvements += "U"
        cube.turn(0)

    return mouvements



def couronne2(cube):
    """ Effectue la deuxième couronne

    :param cube: objet de type Cube
    :return: une chaîne de caractères décrivant les mouvements à effectuer sur le cube
    """
    mouvements = "" #Chaine de caractères qui recense l'ensemble des mouvements necessaires à la résolution

    mouvements += demarrage_deuxieme_couronne(cube)

    fin = deuxieme_couronne_terminee(cube)
    
    # Ensemble des cubes aretes de chaque face concernée
    arete_vert = [10,21,22,30]
    arete_rouge = [13,23,24,33]
    arete_bleu = [16,25,26,36]
    arete_orange = [19,27,28,39]
    arete_jaune = [42,44,45,47]

    # Tant que la résolution de la deuxième couronne n'est pas finie
    while not fin:
        mvtFait = False
        # Récupération de l'état du cube
        faceL = cube.getFace(1)
        faceF = cube.getFace(2)
        faceR = cube.getFace(3)
        faceB = cube.getFace(4)
        faceD = cube.getFace(5)
        
        # Si la face du cube a placer est verte
        if faceL[2][1] in arete_vert:
            # Et si la face liée est rouge alors il faut effectuer un mouvement a gauche 
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
                mvtFait = True
            # Et si la face liée est orange alors il faut effectuer un mouvement a droite
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
                mvtFait = True
            # Et si la face liée n'est ni rouge, ni orange, ni jaune alors on tourne la face Down
            elif faceD[1][0] not in arete_jaune:
                mouvements += "D"
                cube.turn(5)
                mvtFait = True

        # Si la face du cube a placer est rouge
        if not mvtFait and faceF[2][1] in arete_rouge:
            # Et si la face liée est bleue alors il faut effectuer un mouvement a gauche
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
                mvtFait = True
            # Et si la face liée est verte alors il faut effectuer un mouvement a droite
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
                mvtFait = True
            # Et si la face liée n'est ni bleue, ni verte, ni jaune alors on tourne la face Down
            elif faceD[0][1] not in arete_jaune:
                mouvements += "D"
                cube.turn(5)
                mvtFait = True

        # Si la face du cube a placer est bleue
        if not mvtFait and faceR[2][1] in arete_bleu:
            # Et si la face liée est orange alors il faut effectuer un mouvement a gauche
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
                mvtFait = True
            # Et si la face liée est rouge alors il faut effectuer un mouvement a droite
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
                mvtFait = True
            # Et si la face liée n'est ni orange, ni rouge, ni jaune alors on tourne la face Down
            elif faceD[1][2] not in arete_jaune:
                mouvements += "D"
                cube.turn(5)
                mvtFait = True
                
        # Si la face du cube a placer est orange
        if not mvtFait and faceB[2][1] in arete_orange:
            # Et si la face liée est verte alors il faut effectuer un mouvement a gauche
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
                mvtFait = True
            # Et si la face liée est bleue alors il faut effectuer un mouvement a droite
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
                mvtFait = True
            # Et si la face liée n'est ni verte, ni bleue, ni jaune alors on tourne la face Down
            elif faceD[2][1] not in arete_jaune:
                mouvements += "D"
                cube.turn(5)
                mvtFait = True

        # Si aucun mouvement n'a été réalisé et si on a une croix jaune sur la face down ou 4 faces jaunes sur les faces a placer
        if not mvtFait and (faceL[2][1] in arete_jaune or faceD[1][0] in arete_jaune) and (faceF[2][1] in arete_jaune or faceD[0][1] in arete_jaune) and (faceR[2][1] in arete_jaune or faceD[1][2] in arete_jaune) and (faceB[2][1] in arete_jaune or faceD[2][1] in arete_jaune):
            mvtFait = True
            # On débloque un cube arete mal orientée entre la face Front et Left
            if faceF[1][0] not in arete_rouge or faceL[1][2] not in arete_vert:
                    mouvements += "DLD'L'D'F'DF"
                    cube.turn(5)
                    cube.turn(1)
                    cube.turnInv(5)
                    cube.turnInv(1)
                    cube.turnInv(5)
                    cube.turnInv(2)
                    cube.turn(5)
                    cube.turn(2)
            # On débloque un cube arete mal orientée entre la face Front et Right
            elif faceF[1][2] not in arete_rouge or faceR[1][0] not in arete_bleu:
                    mouvements += "D'R'DRDFD'F'"
                    cube.turnInv(5)
                    cube.turnInv(3)
                    cube.turn(5)
                    cube.turn(3)
                    cube.turn(5)
                    cube.turn(2)
                    cube.turnInv(5)
                    cube.turnInv(2)
            # On débloque un cube arete mal orientée entre la face Right et Back
            elif faceR[1][2] not in arete_bleu or faceB[1][0] not in arete_orange:
                    mouvements += "D'B'DBDRD'R'"
                    cube.turnInv(5)
                    cube.turnInv(4)
                    cube.turn(5)
                    cube.turn(4)
                    cube.turn(5)
                    cube.turn(3)
                    cube.turnInv(5)
                    cube.turnInv(3)
            # On débloque un cube arete mal orientée entre la face Back et Left
            else:
                    mouvements += "DBD'B'D'L'DL"
                    cube.turn(5)
                    cube.turn(4)
                    cube.turnInv(5)
                    cube.turnInv(4)
                    cube.turnInv(5)
                    cube.turnInv(1)
                    cube.turn(5)
                    cube.turn(1)
        # Si aucun mouvement n'a été réalisé alors on tourne la face Down
        if not mvtFait:
            mouvements += "D"
            cube.turn(5)
                
        fin = deuxieme_couronne_terminee(cube)
    return mouvements
