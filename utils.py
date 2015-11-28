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

    :param colored54: les 54 facettes étiquetées par leur couleur (O, W, B, G, Y ou R). On considère que ce paramètre est toujours donné au format attendu (pas de gestion d'erreur)

    :return: le même cube au format à base de permutations de (1..48)
    """

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
            pos = bords_couleur.index([colored54_ordonne[j], colored54_ordonne[i]])
            perm48[i] = bords_pos[pos][1] + 1
            perm48[j] = bords_pos[pos][0] + 1

    # On identifie les coins
    coins_couleur = [["W", "G", "O"], ["W", "B", "O"], ["W", "R", "G"], ["W", "R", "B"], ["Y", "G", "O"], ["Y", "B", "O"], ["Y", "R", "G"], ["Y", "R", "B"]]
    coins_pos = [(0, 8, 19), (2, 16, 17), (5, 11, 10), (7, 13, 14), (45, 28, 39), (47, 36, 37), (40, 31, 30), (42, 33, 34)]

    for p in coins_pos:
        couleurs = (colored54_ordonne[p[0]], colored54_ordonne[p[1]], colored54_ordonne[p[2]])
                        
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
                break
            
            
    return perm48


if __name__ == "__main__":

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

