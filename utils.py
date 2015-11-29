# utils.py
# -*- coding: utf-8 -*-

from itertools import permutations


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
        return []

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
            return []

    if not (cptO == cptW == cptB == cptG == cptY == cptR == 9):
        return []

    fixes = []
    for i in [4, 22, 25, 28, 31, 49]:
        if colored54[i] in fixes:
            return []
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
                return []

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
            return []


    return perm48

def perm48_to_20cube(perm48):
# perm48 correspond à un tableau de nombres
# Création d'une liste
    cube=[]
# Initialisation de la liste avec que des 0
    for j in perm48:
        cube.append(0)

# A chaque indice i, on l'associe à la bonne pièce suivant la numérotation 
# Très mal optimisé mais comment faire autrement ? Logique des faces ?
# Vu que la liste débute à 0, prendre i-=1
    for in cube :
        if i==1 or i==9 or i==20:
            cube[i]=
        if i==4 or i==10:
            cube[i]=
        if i==6 or i==11 or i==12:
            cube[i]=

        if i==35 or i==43 or i==34:
            cube[i]=
        if i==36 or i==45:
            cube[i]=
        if i==37 or i==48 or i== 38:
            cube[i]=

        if i==31 or i==41 or i==32:
            cube[i]=
        if i==30 or i==44:
            cube[i]=
        if i==29 or i==46 or i==40:
            cube[i]=

        if i==3 or i==17 or i==18:
            cube[i]=
        if i==5 or i==16:
            cube[i]=
        if i==8 or i==15 or i==14:
            cube[i]=
        
        if i==22 or i==23:
            cube[i]=
        if i==7 or i==13:
            cube[i]=
        if i==33 or i==42:
            cube[i]=
        if i==24 or i==25:
            cube[i]=

        if i==26 or i==27:
            cube[i]=
        if i==2 or i==19:
            cube[i]=
        if i==39 or i==47:
            cube[i]=
        if i==28 or i==21:
            cube[i]=

    return cube


def perm_48_to_cycle_48(seq_perm_48):

	seq_1_to_48 = []
	entree_valide = True

	for i in range(1,49):
		seq_1_to_48.append(i)

	for i in range(1,48):
		if i not in seq_perm_48:
			entree_valide = False
			break

	if len(seq_perm_48) != 48:
		entree_valide = False

	if entree_valide == True:
		permutation_total = []
		cycle_total = []

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
			while courant_seq_perm_48 != first_seq_perm_48:
				permutation.append([courant_seq_perm_48,courant_seq_1_to_48])
				#print("Permutation : "+str(permutation))
				supp_seq_1_to_48 = courant_seq_1_to_48
				supp_seq_perm_48 = courant_seq_perm_48
				#print("A supprimer 1to48 : "+str(supp_seq_1_to_48))
				#print("A supprimer perm48 : "+str(supp_seq_perm_48))
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
			for i in range(0,len(permutation)-1):
				if i == 0:
					cycle.append(first_seq_perm_48)
				cycle.append(permutation[i][1])
			if cycle != []:
				cycle_total.append(cycle)
		return cycle_total
	else:
		return -1

# La fonction prend en paramètre le cycle48 ainsi que la liste contenant pour chaque indice i, la bonne face correspondante
def cycle48_to_cycle20(cycle48, face):

# On créé cycle20 qui est identique à cycle48
    cycle20=list(cycle48)

    for i in range(0,len(cycle20)):
        for j in range(0,len(cycle20[i])):
# On remplace la valeur du cycle par sa pièce si elle n'est pas déjà présente dans le cycle
            if face[cycle20[i][j]] not in cycle20 :
                cycle20[i][j]=face[cycle20[i][j]]
# Sinon on supprime l'élément 
            else : 
                cycle20.remove(cycle20[i][j])

    return cycle20

if __name__=="__main__":
