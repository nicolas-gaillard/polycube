# utils.py
# -*- coding: utf-8 -*-

from itertools import permutations
from Cube_Exception import *


def rotation_cube(colored54):
    """Tourne le cube de la manière suivante : L -> F ; F -> R ; R -> B ; b -> L

    :param colored54: le cube au format colored54"""
    
    # On fait tourner les faces L, F, R et B
    for i in [18, 19, 20, 30, 31, 32, 42, 43, 44]:
        colored54.insert(i - 9, colored54.pop(i))
            
    # Puis la face U
    face_u = colored54[:9]
    for i in range(9):
        colored54.pop(0)
            
    for i in [6, 3, 0, 7, 4, 1, 8, 5, 2]:
        colored54.insert(0, face_u[i])

    # Et enfin la face D
    face_d = colored54[45:]
    for i in range(9):
        colored54.pop()

    for i in [6, 3, 0, 7, 4, 1, 8, 5, 2]:
        colored54.append(face_d[i])


def colored54_to_perm48(colored54):
    """Passage du format d'entrée avec les couleurs vers le format à base de permutations de (1..48).

    :param colored54: les 54 facettes étiquetées par leur couleur (O, W, B, G, Y ou R).

    :return: le même cube au format à base de permutations de (1..48), ou une liste vide en cas d'erreur
    """

    # On commence par tester si l'entrée est bien au format attendu
    if len(colored54) != 54:
        raise Cube_Exception("Votre cube ne contient pas 54 faces")
    
    cptO, cptW, cptB, cptG, cptY, cptR = 0, 0, 0, 0, 0, 0
    for c in colored54:
        if c == "O":
            cptO += 1
        elif c == "W":
            cptW += 1
        elif c == "B":
            cptB += 1
        elif c == "G":
            cptG += 1
        elif c == "Y":
            cptY += 1
        elif c == "R":
            cptR += 1
        else:
            raise Cube_Exception("Votre chaine de caractères contient des éléments autres que les couleurs requises")
        
    if not (cptO == cptW == cptB == cptG == cptY == cptR == 9):
        raise Cube_Exception("Votre cube ne contient pas 9 faces pour chaque couleur")

    fixes = []
    for i in [4, 22, 25, 28, 31, 49]:
        if colored54[i] in fixes:
            raise Cube_Exception("Vous avez deux cubes fixes de meme couleur")
        else:
            fixes.append(colored54[i])

    # D'abord on fait tourner le cube pour que la face rouge soit en face et la blanche en haut

    colored54_ordonne = list(colored54)


    # On met le cube fixe blanc en F s'il n'est pas déjà en F, U, B ou D
    if colored54_ordonne[22] == "W" or colored54_ordonne[28] == "W":
        rotation_cube(colored54_ordonne)
            
    # On met le cube fixe blanc en U
    while colored54_ordonne[4] != "W":
        face_b = colored54_ordonne[18:21] + colored54_ordonne[30:33] + colored54_ordonne[42:45]
        face_u = colored54_ordonne[:9]
        face_d = colored54_ordonne[45:]
        face_l = colored54_ordonne[9:12] + colored54_ordonne[21:24] + colored54_ordonne[33:36]
        face_r = colored54_ordonne[15:18] + colored54_ordonne[27:30] + colored54_ordonne[39:42]
        face_f = colored54_ordonne[12:15] + colored54_ordonne[24:27] + colored54_ordonne[36:39]

        face_u.reverse()
        face_b.reverse()
        
        colored54_ordonne = []
        colored54_ordonne.extend(face_f)
        
        for i in [2, 5, 8]:
            colored54_ordonne.append(face_l[i])
        colored54_ordonne.extend(face_d[:3])
        for i in [6, 3, 0]:
            colored54_ordonne.append(face_r[i])
        colored54_ordonne.extend(face_u[:3])
        
        for i in [1, 4, 7]:
            colored54_ordonne.append(face_l[i])
        colored54_ordonne.extend(face_d[3:6])
        for i in [7, 4, 1]:
            colored54_ordonne.append(face_r[i])
        colored54_ordonne.extend(face_u[3:6])
        
        for i in [0, 3, 6]:
            colored54_ordonne.append(face_l[i])
        colored54_ordonne.extend(face_d[6:])
        for i in [8, 5, 2]:
            colored54_ordonne.append(face_r[i])
        colored54_ordonne.extend(face_u[6:])
        
        colored54_ordonne.extend(face_b)


    # On met le cube fixe rouge en F
    while colored54_ordonne[25] != "R":
        rotation_cube(colored54_ordonne)
            
    
    # On retire les facettes fixes
    colored54_ordonne.pop(49)
    colored54_ordonne.pop(31)
    colored54_ordonne.pop(28)
    colored54_ordonne.pop(25)
    colored54_ordonne.pop(22)
    colored54_ordonne.pop(4)


    # On peut maintenant procéder à la numérotation des facettes

    perm48 = [None] * 48  # crée une liste de taille 48 remplie de None

    # On identifie les bords
    bords_couleur = [["G", "R"], ["R", "B"], ["B", "O"], ["O", "G"], ["W", "R"], ["R", "Y"], ["Y", "O"], ["O", "W"], ["W", "G"], ["G", "Y"], ["Y", "B"], ["B", "W"]]
    bords_pos = [(21, 22), (23, 24), (25, 26), (27, 20), (6, 12), (32, 41), (46, 38), (18, 1), (3, 9), (29, 43), (44, 35), (15, 4)]

    for (i, j) in bords_pos:
        couleurs = [colored54_ordonne[i], colored54_ordonne[j]]
        if couleurs in bords_couleur:
            pos = bords_couleur.index(couleurs)
            perm48[i] = bords_pos[pos][0] + 1
            perm48[j] = bords_pos[pos][1] + 1
        else:
            couleurs = [colored54_ordonne[j], colored54_ordonne[i]]
            if couleurs in bords_couleur:
                pos = bords_couleur.index([colored54_ordonne[j], colored54_ordonne[i]])
                perm48[i] = bords_pos[pos][1] + 1
                perm48[j] = bords_pos[pos][0] + 1
            else:
                raise Cube_Exception("Un des cubes aretes est physiquement impossible")

    # On identifie les coins
    coins_couleur = [["W", "G", "O"], ["W", "B", "O"], ["W", "R", "G"], ["W", "R", "B"], ["Y", "G", "O"], ["Y", "B", "O"], ["Y", "R", "G"], ["Y", "R", "B"]]
    coins_pos = [(0, 8, 19), (2, 16, 17), (5, 11, 10), (7, 13, 14), (45, 28, 39), (47, 36, 37), (40, 31, 30), (42, 33, 34)]

    for p in coins_pos:
        couleurs = (colored54_ordonne[p[0]], colored54_ordonne[p[1]], colored54_ordonne[p[2]])
        ajoute = False
                        
        for c in coins_couleur:
            perms_couleur = list(permutations(c))
            try:
                index = perms_couleur.index(couleurs)
            except:
                index = -1

            if index != -1:
                pos = coins_couleur.index(c)
                perm_pos = list(permutations(coins_pos[pos]))
                perm48[p[0]] = perm_pos[index][0] + 1
                perm48[p[1]] = perm_pos[index][1] + 1
                perm48[p[2]] = perm_pos[index][2] + 1
                ajoute = True
                break
            
        if not ajoute:
            raise Cube_Exception("Un des cubes coins est physiquement impossible")
            
            
    return perm48

""" Fonction qui permet d'obtenir l'ensemble des cycles de permutation à partir de la configuration initiale du cube,
jusqu'à la configuration finale """ 
def perm_48_to_cycle_48(seq_perm_48):

	seq_1_to_48 = []
	entree_valide = True
	""" Boucle permettant de remplir la liste allant de 1 à 48 """
	for i in range(1,49):
		seq_1_to_48.append(i)
	""" Boucle permettant de vérifier si la liste initiale contient bien des nombres de 1 à 48 """
	for i in range(1,48):
		if i not in seq_perm_48:
			entree_valide = False
			break
	""" Condition permettant de vérifier si la liste initiale contient bien 48 élements """
	if len(seq_perm_48) != 48:
		entree_valide = False

	""" Condition permettant de vérifier si la liste initiale est valide, si c'est le cas l'algorithme se poursuit, sinon on renvoie -1 """
	if entree_valide == True:
		permutation_total = []
		cycle_total = []
		
		""" Boucle permettant de vérifier qu'il ne reste pas de cycles à traiter """
		while len(seq_1_to_48) > 0:
			courant_seq_1_to_48 = seq_1_to_48[0]
			courant_seq_perm_48 = seq_perm_48[0]
			first_seq_perm_48 = seq_perm_48[0]
			#print("Courant perm48 : "+str(courant_seq_perm_48))
			#print("Courant 1to48 : "+str(courant_seq_1_to_48))
			#print("Premier seq_perm_48 :"+str(first_seq_perm_48))
			permutation = []
			cycle = []
			permutation.append([courant_seq_perm_48,courant_seq_1_to_48])
			#print("Permutation : "+str(permutation))
			supp_seq_1_to_48 = courant_seq_1_to_48
			supp_seq_perm_48 = courant_seq_perm_48
			#print("A supprimer 1to48 : "+str(supp_seq_1_to_48))
			#print("A supprimer perm48 : "+str(supp_seq_perm_48))
			courant_seq_1_to_48 = seq_1_to_48[seq_perm_48.index(supp_seq_1_to_48)]
			courant_seq_perm_48 = seq_perm_48[seq_perm_48.index(supp_seq_1_to_48)]
			#print("Nouveau courant 1to48: "+str(courant_seq_1_to_48))
			#print("Nouveau courant perm48 : "+str(courant_seq_perm_48))
			#print("Ancien seq_1_to_48 : "+str(seq_1_to_48))
			#print("Ancien seq_perm_48 : "+str(seq_perm_48))
			seq_1_to_48.remove(supp_seq_1_to_48)
			seq_perm_48.remove(supp_seq_perm_48)
			#print("Nouveau seq_1_to_48 : "+str(seq_1_to_48))
			#print("Nouveau seq_perm_48 : "+str(seq_perm_48))
			#print("Tant que "+str(courant_seq_1_to_48)+" est different "+str(first_seq_perm_48))

			""" Boucle permettant de vérifier qu'un cycle n'est pas terminé """
			while courant_seq_perm_48 != first_seq_perm_48:
				permutation.append([courant_seq_perm_48,courant_seq_1_to_48])
				#print("Permutation : "+str(permutation))
				supp_seq_1_to_48 = courant_seq_1_to_48
				supp_seq_perm_48 = courant_seq_perm_48
				#print("A supprimer 1to48 : "+str(supp_seq_1_to_48))
				#print("A supprimer perm48 : "+str(supp_seq_perm_48))

				""" Condition permettant d'effectuer la suppression des deux éléments de la derniere permutation """
				if supp_seq_1_to_48 == first_seq_perm_48:
					#print("Ancien seq_1_to_48 : "+str(seq_1_to_48))
					#print("Ancien seq_perm_48 : "+str(seq_perm_48))
					seq_1_to_48.remove(supp_seq_1_to_48)
					seq_perm_48.remove(supp_seq_perm_48)
					#print("Nouveau seq_1_to_48 : "+str(seq_1_to_48))
					#print("Nouveau seq_perm_48 : "+str(seq_perm_48))
					break
				courant_seq_1_to_48 = seq_1_to_48[seq_perm_48.index(supp_seq_1_to_48)]
				courant_seq_perm_48 = seq_perm_48[seq_perm_48.index(supp_seq_1_to_48)]
				#print("Nouveau courant 1to48: "+str(courant_seq_1_to_48))
				#print("Nouveau courant perm48 : "+str(courant_seq_perm_48))
				#print("Ancien seq_1_to_48 : "+str(seq_1_to_48))
				#print("Ancien seq_perm_48 : "+str(seq_perm_48))
				seq_1_to_48.remove(supp_seq_1_to_48)
				seq_perm_48.remove(supp_seq_perm_48)
				#print("Nouveau seq_1_to_48 : "+str(seq_1_to_48))
				#print("Nouveau seq_perm_48 : "+str(seq_perm_48))
			permutation_total.append(permutation)
			""" Boucle permettant de constituer les cycles pour chaque ensemble de permutations """
			for i in range(0,len(permutation)-1):
				if i == 0:
					cycle.append(first_seq_perm_48)
				cycle.append(permutation[i][1])
			""" Condition qui permet de n'ajouter les éléments dans le cycle que si cela est nécessaire """
			if cycle != []:
				cycle_total.append(cycle)
		return cycle_total
	else:
		return -1

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

# Suppression des cycles redondants :
# On créer des listes commençant par le même élement que la liste que l'on étudie, puis on organise les élements suivants dans le même sens
# Si les listes se retrouvent être les mêmes, il y a alors redondances des cycles
# Enfin, on ajoute le numéro des cycles redondants à une listeSupp, puis on lit cette listeSupp pour enlever les cycles de notre liste cycle20 finale
    listeSupp = []
    for a in range(0, len(cycle20)-1):
        for b in range(a+1, len(cycle20)):
            if((len(cycle20[a]) == (len(cycle20[b]))) and a != b):
                liste1 = cycle20[a]
                element1 = liste1[0]
                liste2 = []
                for c in range(0, len(liste1)):
                    if(str(element1) == str(liste1[c])):
                        indice = c
                for d in range(indice, len(liste1)):
                    liste2.append(liste1[d])
                for e in range(0, indice):
                    liste2.append(liste1[e])
                if(liste1 == liste2):
                    listeSupp.append(b)
    cycle20ok = []
    for f in range(0, len(cycle20)):
        if(f not in listeSupp):
            cycle20ok.append(cycle20[f])

# Rajouter une condition pour la supression de cycle similaires
    return cycle20ok

if __name__=="__main__":

	print(" ===== TESTS colored54_to_perm48 =====")
	cube = colored54_to_perm48("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY")

	if cube == list(range(1,49)):
		print("Test rotation 1 OK")
	else:
		print("Test rotation 1 KO : " + str(cube))

	cube = colored54_to_perm48("GGGGGGGGGWWWOOOYYYRRRWWWOOOYYYRRRWWWOOOYYYRRRBBBBBBBBB")

	if cube == list(range(1,49)):
		print("Test rotation 2 OK")
	else:
		print("Test rotation 2 KO : " + str(cube))

	cube = colored54_to_perm48("YYYYYYYYYGGGOOOBBBRRRGGGOOOBBBRRRGGGOOOBBBRRRWWWWWWWWW")

	if cube == list(range(1,49)):
		print("Test rotation 3 OK")
	else:
		print("Test rotation 3 KO : " + str(cube))

	cube = colored54_to_perm48("OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG")
    
	if cube == [37, 36, 40, 30, 22, 17, 47, 12, 38, 44, 18, 3, 39, 6, 11, 23, 46, 29, 45, 48, 26, 25, 24, 42, 33, 2, 19, 27, 35, 5, 41, 31, 13, 20, 1, 21, 14, 8, 4, 34, 32, 7, 9, 16, 28, 43, 10, 15]:
		print("Test rotation + numérotation 1 OK")
	else:
		print("Test rotation + numérotation 1 KO : " + str(cube))

	cube = colored54_to_perm48("GRBGRWBBYRYYOOGOBOWWYGGOYYRBBWOWWGYWBORGRBYYWRGWBOGORR")

	if cube == [1, 42, 43, 4, 19, 41, 7, 3, 9, 10, 32, 31, 13, 17, 18, 2, 35, 34, 33, 20, 45, 44, 30, 5, 16, 23, 22, 36, 8, 39, 48, 37, 26, 46, 40, 25, 11, 6, 21, 14, 38, 27, 29, 47, 24, 15, 28, 12]:
		print("Test rotation + numérotation 2 OK")
	else:
		print("Test rotation + numérotation 2 KO : " + str(cube))

	cube = colored54_to_perm48("GRBGRWBBYRYYOOGOBOWWYGG")

	if cube == []:
		print("Test entrée incorrecte 1 OK")
	else:
		print("Test entrée incorrecte 1 KO : " + str(cube))

	cube = colored54_to_perm48("ABCWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY")

	if cube == []:
		print("Test entrée incorrecte 2 OK")
	else:
		print("Test entrée incorrecte 2 KO : " + str(cube))

	cube = colored54_to_perm48("WWWWWWWWWWWWRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY")

	if cube == []:
		print("Test entrée incorrecte 3 OK")
	else:
		print("Test entrée incorrecte 3 KO : " + str(cube))

	cube = colored54_to_perm48("WWWWWWWWGGGGRRRBBBOOOGWGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY")

	if cube == []:
		print("Test entrée incorrecte 4 OK")
	else:
		print("Test entrée incorrecte 4 KO : " + str(cube))

	cube = colored54_to_perm48("WWWWWWWWWGGGRYRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOORYYYYYYYY")

	if cube == []:
		print("Test entrée incorrecte 5 OK")
	else:
		print("Test entrée incorrecte 5 KO : " + str(cube))

	cube = colored54_to_perm48("WWWWWWWWWGGGRRYBBBOOOGGGRRRBBBOOOGGGRRRBBBOOORYYYYYYYY")

	if cube == []:
		print("Test entrée incorrecte 6 OK")
	else:
		print("Test entrée incorrecte 6 KO : " + str(cube))

	print(" ===== TESTS perm48_to_cycle48 =====")

	print(perm_48_to_cycle_48([37,36,40,30,22,17,47,12,38,44,18,3,39,6,11,23,46,29,45,48,26,25,24,42,33,2,19,27,35,5,41,31,13,20,1,21,14,8,4,34,32,7,9,16,28,43,10,15]))

