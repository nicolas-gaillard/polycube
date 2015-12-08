# -*- coding: utf-8 -*-

from utils import *

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
    
    def rotateFace(self,face):
        # Face est un int qui fait référence à lCube
        # 0=U, 1=L, 2=F, 3=R, 4=B, 5=D

        #rotation des arêtes
        self.turnArete(face)

        # Placement des coins
        self.lCube[face][0][0],self.lCube[face][0][2]=self.lCube[face][0][2],self.lCube[face][0][0]
        self.lCube[face][0][0],self.lCube[face][2][2]=self.lCube[face][2][2],self.lCube[face][0][0]
        self.lCube[face][0][0],self.lCube[face][2][0]=self.lCube[face][2][0],self.lCube[face][0][0]

        # Placement des arrêtes
        self.lCube[face][0][1],self.lCube[face][1][2]=self.lCube[face][1][2],self.lCube[face][0][0]
        self.lCube[face][0][1],self.lCube[face][2][1]=self.lCube[face][2][1],self.lCube[face][0][1]
        self.lCube[face][0][1],self.lCube[face][1][0]=self.lCube[face][1][0],self.lCube[face][0][1]

    """def rotateEdge(self,face):
        if self.lCube[face]
# Pour chaque face, il faut déterminer quelle face va bouger"""

    def turnLine(self,face,ligne):
        # face et ligne sont des int

        if self.lCube[face] in self.lCube[1:4]:
            if ligne == 1 :
# Faire tourner la ligne du milieu consiste à faire tourner les deux autres
                self.turnLine(face,0)
                self.turnLine(face,2)
            else :
                self.F[ligne],self.R[ligne]=self.R[ligne],self.F[ligne]
                self.F[ligne],self.B[ligne]=self.B[ligne],self.F[ligne]
                self.F[ligne],self.L[ligne]=self.L[ligne],self.F[ligne]

        elif self.lCube[face] == U :
            if ligne ==1 :
                self.turnLine(face,0)
                self.turnLine(face,2)
            elif line==0 :
                self.U[0][0], self.R[0][2]=self.R[0][2], self.U[0][0]
                self.U[0][1], self.R[1][2]=self.R[1][2], self.U[0][1]
                self.U[0][2], self.R[2][2]=self.R[2][2], self.U[0][2]

                self.U[0][0], self.D[2][2]=self.D[2][2], self.U[0][0]
                self.U[0][1], self.D[2][1]=self.D[2][1], self.U[0][1]
                self.U[0][2], self.D[2][0]=self.D[2][0], self.U[0][2]

                self.U[0][0], self.L[2][0]=self.L[2][0], self.U[0][0]
                self.U[0][1], self.L[1][0]=self.L[1][0], self.U[0][1]
                self.U[0][2], self.L[0][0]=self.L[0][0], self.U[0][2]

            else : # line == 2
                self.U[2][0], self.R[0][0]=self.R[0][0], self.U[2][0]
                self.U[2][1], self.R[1][0]=self.R[1][0], self.U[2][1]
                self.U[2][2], self.R[2][0]=self.R[2][0], self.U[2][2]

                self.U[2][0], self.D[0][2]=self.D[0][2], self.U[2][0]
                self.U[2][1], self.D[0][1]=self.D[0][1], self.U[2][1]
                self.U[2][2], self.D[0][0]=self.D[0][0], self.U[2][2]

                self.U[2][0], self.L[2][2]=self.L[2][2], self.U[2][0]
                self.U[2][1], self.L[1][2]=self.L[1][2], self.U[2][1]
                self.U[2][2], self.L[0][2]=self.L[0][2], self.U[2][2]

        else :
            if ligne==0 :
                self.turnLine(self.U,2)
            elif ligne==2: 
                self.turnLine(self.U,0)
            else :
                self.turnLine(self.U,1)

    def cube_to_perm48(self) :
        perm48=[]
        return perm48

    """def turnColumn(self,face,column):
        if self.lCube[face]==self.F or self.lCube[face]==self.U or self.lCube[face]==self.B or self.lCube[face]==self.D :
        
        else :"""
            
    # Rotation de 90° dans le sens des aiguilles d'une face
    def move(self,face):
        self.rotateFace(face)
        return str(self.lCube[face])
        
    # Rotation de 180° dans le sens des aiguilles d'une face
    def move2(self,face):
        self.rotateFace(self.rotateFace(face))
        self.rotateEdge(self.rotateEdge(face))
        return "2"+str(self.lCube[face])
            
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

    
    def turnArete(self, face):
        print("debut turn arete")
        if(face == 0):
            self.echangeArete(4,1,2,3)
        elif(face == 1):
            self.echangeArete(0,4,5,2)
        elif(face == 2):
            self.echangeArete(0,1,5,3)
        elif(face == 3):
            self.echangeArete(0,2,5,4)
        elif(face == 4):
            self.echangeArete(0,3,5,1)
        else:
            self.echangeArete(4,3,2,1)
    

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
        print("echange arete")
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

if __name__=="__main__":
    test=cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY")
    #test.getFace(0)
    test.afficherCube()
    test.rotateFace(2)
    print("appel de la fonction")
    test.afficherCube()
    #test.afficheFace(2)
    #print(cube.listecube[face][0][0])
    #print("FONCTION")
    #test.turnLine(2,0)
    