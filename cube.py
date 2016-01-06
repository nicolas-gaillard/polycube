# -*- coding: utf-8 -*-

from utils import *
#from CubeDisplay import *

class cube :
    def __init__(self,color54):

        if len(color54)!=54: # Manque à vérifier que color 54 est bien formé, à l'aide d'une boucle
            self.init(input("Chaine non valide, recommencez "))
        else:
            self.perm48=colored54_to_perm48(color54)
            self.color54=color54

# face[1][1] est une constante, elle ne bouge jamais
# F=Front, D=Down, L=Left, R=Right, B=Back, U=Up
# Convention : U=White=0, F=Red=2, L=Green=1, R=Blue=3, B=Orange=4, D=Yellow=5

# On prend indice-1 car la liste perm48 commence à l'indice 0
            self.F=[self.perm48[11:14],[self.perm48[22],'F',self.perm48[23]],self.perm48[31:34]]
            
            self.D=[self.perm48[40:43],[self.perm48[43],'D',self.perm48[44]],self.perm48[45:48]]
            
            self.L=[self.perm48[8:11],[self.perm48[20],'L',self.perm48[21]],self.perm48[28:31]]
            
            self.R=[self.perm48[14:17],[self.perm48[24],'R',self.perm48[25]],self.perm48[34:37]]
            
            self.B=[self.perm48[17:20],[self.perm48[26],'B',self.perm48[27]],self.perm48[37:40]]
            
            self.U=[self.perm48[0:3],[self.perm48[3],'U',self.perm48[4]],self.perm48[5:8]]

            self.lCube=[self.U,self.L,self.F,self.R,self.B,self.D]

    def __str__(self):
        drawCube(self.cube_to_color54())
        return ""

    def afficheFace(self,face):
        print(self.lCube[face])

    def getFace(self,face):
        return self.lCube[face]

    def afficherCube(self):
        print(self.lCube[0])
        print(self.lCube[1])
        print(self.lCube[2])
        print(self.lCube[3])
        print(self.lCube[4])
        print(self.lCube[5])

    def turn(self, face):
        self.turnFace(face)
        self.turnArete(face)

    def turn2(self, face):
        # Fait tourner une face 2 fois (un demi-tour)
        self.turn(face)
        self.turn(face)

    def turnInv(self, face):
        # Fait tourner une face 3 fois (quart de tour inverse)
        self.turn2(face)
        self.turn(face)

    def turnFace(self, face):
        self.echangeFace(face)
    
    def turnArete(self, face):
        if(face == 0):
            self.echangeAreteBlanche()
        elif(face == 1):
            self.echangeAreteVerte()
        elif(face == 2):
            self.echangeAreteRouge()
        elif(face == 3):
            self.echangeAreteBleu()
        elif(face == 4):
            self.echangeAreteOrange()
        else:
            self.echangeAreteJaune()
    

    """
    Pour la fonction ci-dessus, on utilise ce schéma pour identifier à quelle face on associe le chiffre :
           1
        -------
     2  |     |  4
        |     |         on tourne dans le sens horaire 
        -------
           3
    """
    # U=White=0, F=Red=2, L=Green=1, R=Blue=3, B=Orange=4, D=Yellow=5

    def echangeArete(self, couleur1, couleur2, couleur3, couleur4):
        liste = []

        liste.append(self.lCube[couleur4][0][0])
        liste.append(self.lCube[couleur4][1][0])
        liste.append(self.lCube[couleur4][2][0])
        liste.append(self.lCube[couleur3][0][0])
        liste.append(self.lCube[couleur3][0][1])
        liste.append(self.lCube[couleur3][0][2])
        liste.append(self.lCube[couleur2][0][2])
        liste.append(self.lCube[couleur2][1][2])
        liste.append(self.lCube[couleur2][2][2])
        liste.append(self.lCube[couleur1][2][0])
        liste.append(self.lCube[couleur1][2][1])
        liste.append(self.lCube[couleur1][2][2])

        self.lCube[couleur3][0][2]=liste[0]
        self.lCube[couleur3][0][1]=liste[1]
        self.lCube[couleur3][0][0]=liste[2]
        self.lCube[couleur2][0][2]=liste[3]
        self.lCube[couleur2][1][2]=liste[4]
        self.lCube[couleur2][2][2]=liste[5]
        self.lCube[couleur1][2][2]=liste[6]
        self.lCube[couleur1][2][1]=liste[7]
        self.lCube[couleur1][2][0]=liste[8]
        self.lCube[couleur4][0][0]=liste[9]
        self.lCube[couleur4][1][0]=liste[10]
        self.lCube[couleur4][2][0]=liste[11]

    def echangeAreteBlanche(self):
        liste = []
        liste.append(self.lCube[1][0][2])
        liste.append(self.lCube[1][0][1])
        liste.append(self.lCube[1][0][0])
        liste.append(self.lCube[4][0][2])
        liste.append(self.lCube[4][0][1])
        liste.append(self.lCube[4][0][0])
        liste.append(self.lCube[3][0][2])
        liste.append(self.lCube[3][0][1])
        liste.append(self.lCube[3][0][0])
        liste.append(self.lCube[2][0][2])
        liste.append(self.lCube[2][0][1])
        liste.append(self.lCube[2][0][0])

        self.lCube[4][0][2]=liste[0]
        self.lCube[4][0][1]=liste[1]
        self.lCube[4][0][0]=liste[2]
        self.lCube[3][0][2]=liste[3]
        self.lCube[3][0][1]=liste[4]
        self.lCube[3][0][0]=liste[5]
        self.lCube[2][0][2]=liste[6]
        self.lCube[2][0][1]=liste[7]
        self.lCube[2][0][0]=liste[8]
        self.lCube[1][0][2]=liste[9]
        self.lCube[1][0][1]=liste[10]
        self.lCube[1][0][0]=liste[11]

    def echangeAreteVerte(self):
        liste = []
        liste.append(self.lCube[5][0][0])
        liste.append(self.lCube[5][1][0])
        liste.append(self.lCube[5][2][0])
        liste.append(self.lCube[2][0][0])
        liste.append(self.lCube[2][1][0])
        liste.append(self.lCube[2][2][0])
        liste.append(self.lCube[0][0][0])
        liste.append(self.lCube[0][1][0])
        liste.append(self.lCube[0][2][0])
        liste.append(self.lCube[4][2][2])
        liste.append(self.lCube[4][1][2])
        liste.append(self.lCube[4][0][2])

        self.lCube[4][2][2]=liste[0]
        self.lCube[4][1][2]=liste[1]
        self.lCube[4][0][2]=liste[2]
        self.lCube[5][0][0]=liste[3]
        self.lCube[5][1][0]=liste[4]
        self.lCube[5][2][0]=liste[5]
        self.lCube[2][0][0]=liste[6]
        self.lCube[2][1][0]=liste[7]
        self.lCube[2][2][0]=liste[8]
        self.lCube[0][0][0]=liste[9]
        self.lCube[0][1][0]=liste[10]
        self.lCube[0][2][0]=liste[11]

    def echangeAreteRouge(self):
        liste = []
        liste.append(self.lCube[0][2][0])
        liste.append(self.lCube[0][2][1])
        liste.append(self.lCube[0][2][2])
        liste.append(self.lCube[1][0][2])
        liste.append(self.lCube[1][1][2])
        liste.append(self.lCube[1][2][2])
        liste.append(self.lCube[3][0][0])
        liste.append(self.lCube[3][1][0])
        liste.append(self.lCube[3][2][0])
        liste.append(self.lCube[5][0][0])
        liste.append(self.lCube[5][0][1])
        liste.append(self.lCube[5][0][2])

        self.lCube[3][0][0]=liste[0]
        self.lCube[3][1][0]=liste[1]
        self.lCube[3][2][0]=liste[2]
        self.lCube[0][2][2]=liste[3]
        self.lCube[0][2][1]=liste[4]
        self.lCube[0][2][0]=liste[5]
        self.lCube[5][0][2]=liste[6]
        self.lCube[5][0][1]=liste[7]
        self.lCube[5][0][0]=liste[8]
        self.lCube[1][0][2]=liste[9]
        self.lCube[1][1][2]=liste[10]
        self.lCube[1][2][2]=liste[11]

    def echangeAreteBleu(self):
        liste = []
        liste.append(self.lCube[0][0][2])
        liste.append(self.lCube[0][1][2])
        liste.append(self.lCube[0][2][2])
        liste.append(self.lCube[2][0][2])
        liste.append(self.lCube[2][1][2])
        liste.append(self.lCube[2][2][2])
        liste.append(self.lCube[5][0][2])
        liste.append(self.lCube[5][1][2])
        liste.append(self.lCube[5][2][2])
        liste.append(self.lCube[4][2][0])
        liste.append(self.lCube[4][1][0])
        liste.append(self.lCube[4][0][0])

        self.lCube[4][2][0]=liste[0]
        self.lCube[4][1][0]=liste[1]
        self.lCube[4][0][0]=liste[2]
        self.lCube[0][0][2]=liste[3]
        self.lCube[0][1][2]=liste[4]
        self.lCube[0][2][2]=liste[5]
        self.lCube[2][0][2]=liste[6]
        self.lCube[2][1][2]=liste[7]
        self.lCube[2][2][2]=liste[8]
        self.lCube[5][0][2]=liste[9]
        self.lCube[5][1][2]=liste[10]
        self.lCube[5][2][2]=liste[11]

    def echangeAreteOrange(self):
        liste = []
        liste.append(self.lCube[0][0][0])
        liste.append(self.lCube[0][0][1])
        liste.append(self.lCube[0][0][2])
        liste.append(self.lCube[3][0][2])
        liste.append(self.lCube[3][1][2])
        liste.append(self.lCube[3][2][2])
        liste.append(self.lCube[1][0][0])
        liste.append(self.lCube[1][1][0])
        liste.append(self.lCube[1][2][0])
        liste.append(self.lCube[5][2][0])
        liste.append(self.lCube[5][2][1])
        liste.append(self.lCube[5][2][2])

        self.lCube[1][2][0]=liste[0]
        self.lCube[1][1][0]=liste[1]
        self.lCube[1][0][0]=liste[2]
        self.lCube[0][0][0]=liste[3]
        self.lCube[0][0][1]=liste[4]
        self.lCube[0][0][2]=liste[5]
        self.lCube[5][2][0]=liste[6]
        self.lCube[5][2][1]=liste[7]
        self.lCube[5][2][2]=liste[8]
        self.lCube[3][2][2]=liste[9]
        self.lCube[3][1][2]=liste[10]
        self.lCube[3][0][2]=liste[11]

    def echangeAreteJaune(self):
        liste = []
       
        liste.append(self.lCube[2][2][0])
        liste.append(self.lCube[2][2][1])
        liste.append(self.lCube[2][2][2])
        liste.append(self.lCube[3][2][0])
        liste.append(self.lCube[3][2][1])
        liste.append(self.lCube[3][2][2])
        liste.append(self.lCube[4][2][0])
        liste.append(self.lCube[4][2][1])
        liste.append(self.lCube[4][2][2])
        liste.append(self.lCube[1][2][0])
        liste.append(self.lCube[1][2][1])
        liste.append(self.lCube[1][2][2])

        self.lCube[3][2][0]=liste[0]
        self.lCube[3][2][1]=liste[1]
        self.lCube[3][2][2]=liste[2]
        self.lCube[4][2][0]=liste[3]
        self.lCube[4][2][1]=liste[4]
        self.lCube[4][2][2]=liste[5]
        self.lCube[1][2][0]=liste[6]
        self.lCube[1][2][1]=liste[7]
        self.lCube[1][2][2]=liste[8]
        self.lCube[2][2][0]=liste[9]
        self.lCube[2][2][1]=liste[10]
        self.lCube[2][2][2]=liste[11]

    def echangeFace(self, face):
        liste = []
        liste.append(self.lCube[face][0][0])
        liste.append(self.lCube[face][0][1])
        liste.append(self.lCube[face][0][2])
        liste.append(self.lCube[face][1][2])
        liste.append(self.lCube[face][2][2])
        liste.append(self.lCube[face][2][1])
        liste.append(self.lCube[face][2][0])
        liste.append(self.lCube[face][1][0])

        self.lCube[face][0][2] = liste[0]
        self.lCube[face][1][2] = liste[1]
        self.lCube[face][2][2] = liste[2]
        self.lCube[face][2][1] = liste[3]
        self.lCube[face][2][0] = liste[4]
        self.lCube[face][1][0] = liste[5]
        self.lCube[face][0][0] = liste[6]
        self.lCube[face][0][1] = liste[7]

    def cube_to_color54(self):
    
        W=['U',1,2,3,4,5,6,7,8]
        R=['F',12,13,14,23,24,32,33,34]
        B=['R',15,16,17,25,26,35,36,37]
        G=['L',9,10,11,21,22,29,30,31]
        Y=['D',41,42,43,44,45,46,47,48]
        O=['B',18,19,20,27,28,38,39,40]
        
        color54=""

        for k in range(0,3):
            for l in range(0,3):
            
                if self.lCube[0][k][l] in W :
                    color54+="W"
                if self.lCube[0][k][l] in R :
                    color54+="R"
                if self.lCube[0][k][l] in B :
                    color54+="B"
                if self.lCube[0][k][l] in G :
                    color54+="G"
                if self.lCube[0][k][l] in Y :
                    color54+="Y"        
                if self.lCube[0][k][l] in O :
                    color54+="O"
         
        for j in range(0,3):
            for i in range(1,5):
                for m in range(0,3):
                    if self.lCube[i][j][m] in W :
                        color54+="W"
                    if self.lCube[i][j][m] in R :
                        color54+="R"
                    if self.lCube[i][j][m] in B :       
                        color54+="B"
                    if self.lCube[i][j][m] in G :
                        color54+="G"
                    if self.lCube[i][j][m] in Y :
                        color54+="Y"
                    if self.lCube[i][j][m] in O :
                        color54+="O"

        for n in range(0,3):
            for o in range(0,3):
                if self.lCube[5][n][o] in W :
                    color54+="W"
                if self.lCube[5][n][o] in R :
                    color54+="R"
                if self.lCube[5][n][o] in B :
                    color54+="B"
                if self.lCube[5][n][o] in G :
                    color54+="G"
                if self.lCube[5][n][o] in Y :
                    color54+="Y"
                if self.lCube[5][n][o] in O :
                    color54+="O"
        return color54

if __name__=="__main__":
    test=cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY")
    #test.getFace(0)
    test.afficherCube()
    test.turn(5)
    print("appel de la fonction")
    test.afficherCube()
    #test.afficheFace(2)
    #print(cube.listecube[face][0][0])
    #print("FONCTION")
    #test.turnLine(2,0)
    #print(test)
    
