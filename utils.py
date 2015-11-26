# utils.py
# -*- coding: utf-8 -*-

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
    
            
    return colored54_ordonne


if __name__ == "__main__":
    """Les tests des fonctions se font ici"""
    
    cube = colored54_to_perm48("OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG")
    
    if "".join(cube) == "BBOGGBYROYOWOWGRYGYYBBRYRWOOBWYGROWGRWWRRWGBOYGB":
        print("Test 1 OK")
    else:
        print("Test 1 KO : " + "".join(cube))

    cube = colored54_to_perm48("GRBGRWBBYRYYOOGOBOWWYGGOYYRBBWOWWGYWBORGRBYYWRGWBOGORR")

    if "".join(cube) == "WYYWOYWWGGRGRBOWBRROYYGWBRGBWOYBBYOBGWGROOGYRBOR":
        print("Test 2 OK")
    else:
        print("Test 2 KO : " + "".join(cube))
