# utils.py
# -*- coding: utf-8 -*-

def perm48_to_20cube(perm48):

# perm48 correspond à un tableau de nombres
# Création d'une liste

    cube=[]

# Initialisation de la liste avec que des 0

    for j in range(0,49):
        cube.append(0)

    print(len(cube))

#A chaque indice i, on l'associe à la bonne pièce suivant la numérotation 
#Très mal optimisé mais comment faire autrement ?

    for i in range(0,len(cube)):
        if i==1 or i==9 or i==20:
            cube[perm48[i-1]]="ULB"
        if i==4 or i==10:
            cube[perm48[i-1]]="UL"
        if i==6 or i==11 or i==12:
            cube[perm48[i-1]]="ULF"

        if i==35 or i==43 or i==34:
            cube[perm48[i-1]]="RDF"
        if i==36 or i==45:
            cube[perm48[i-1]]="RD"
        if i==37 or i==48 or i== 38:
            cube[perm48[i-1]]="RDB"

        if i==31 or i==41 or i==32:
            cube[perm48[i-1]]="LDF"
        if i==30 or i==44:
            cube[perm48[i-1]]="LD"
        if i==29 or i==46 or i==40:
            cube[perm48[i-1]]="LDB"

        if i==3 or i==17 or i==18:
            cube[perm48[i-1]]="URB"
        if i==5 or i==16:
            cube[perm48[i-1]]="UR"
        if i==8 or i==15 or i==14:
            cube[perm48[i-1]]="URF"
        
        if i==22 or i==23:
            cube[perm48[i-1]]="LF"
        if i==7 or i==13:
            cube[perm48[i-1]]="UF"
        if i==33 or i==42:
            cube[perm48[i-1]]="FD"
        if i==24 or i==25:
            cube[perm48[i-1]]="FR"

        if i==26 or i==27:
            cube[perm48[i-1]]="RB"
        if i==2 or i==19:
            cube[perm48[i-1]]="UB"
        if i==39 or i==47:
            cube[perm48[i-1]]="DB"
        if i==28 or i==21:
            cube[perm48[i-1]]="LB"

    return cube

# La fonction prend en paramètre le cycle48 ainsi que la liste contenant pour chaque indice i, la bonne face correspondante
def cycle48_to_cycle20(cycle48, cube):

# On créé cycle20 qui est identique à cycle48
    cycle20=list(cycle48)
    #print(cycle20)
    #print(cube)



    for i in range(0,len(cycle20)):
        for j in range(0,len(cycle20[i])):
# On remplace la valeur du cycle par sa pièce si elle n'est pas déjà présente dans le cycle
            #print(i,j)
            #print(cycle20[i][j])
            #print(cube[cycle20[i][j]])
            if cube[cycle20[i][j]] not in cycle20[i] :
                cycle20[i][j]=cube[cycle20[i][j]]
# Sinon on le met à 0 et on le supprime dans une autre boucle
            else : 
                cycle20[i][j]=0

# Suppression des 0 et des cycles doublons :
    for k in range(0,len(cycle20)):
        while 0 in cycle20[k]:
            cycle20[k].remove(0)

# Rajouter une condition pour la supression de cycle similaires
    return cycle20

if __name__=="__main__":
    #print(perm48_to_20cube([37,36,40,30,22,17,47,12,38,44,18,3,39,6,11,23,46,29,45,48,26,25,24,42,33,2,19,27,35,5,41,31,13,20,1,21,14,8,4,34,32,7,9,16,28,43,10,15]))
    perm48=[37,36,40,30,22,17,47,12,38,44,18,3,39,6,11,23,46,29,45,48,26,25,24,42,33,2,19,27,35,5,41,31,13,20,1,21,14,8,4,34,32,7,9,16,28,43,10,15]
    cycle48=[[37,1,35,29,18,11,15,48,20,34,40,3,12,8,38,9,43,46,17,6,14],[36,2,26,21],[30,4,39,13,33,25,22,5],[47,7,42,24,23,16,44,10],[45,19,27,28],[41,31,32]]
    cube=perm48_to_20cube(perm48)
    print(cycle48_to_cycle20(cycle48,cube))
