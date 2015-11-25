# utils.py
# -*- coding: utf-8 -*-

def colored54_to_perm48(colored54):
    """Passage du format d'entrée avec les couleurs vers le format à base de permutations de (1..48).

    :param colored54: les 54 facettes étiquetées par leur couleur (O, W, B, G, Y ou R). On considère que ce paramètre est toujours donné au format attendu (pas de gestion d'erreur)

    :return: le même cube au format à base de permutations de (1..48)
    """

    # D'abord on fait tourner le cube pour que la face rouge soit en face et la blanche en haut
    # On en profite pour retirer les facettes fixes
    couleurs = ["W", "G", "R", "B", "O", "Y"]
    vert, rouge, bleu, orange, jaune = [], [], [], [], []
    
    colored54_ordonne = []
    
    for c in couleurs:
        tab = colored54_ordonne
        if c == "G":
            tab = vert
        elif c == "R":
            tab = rouge
        elif c == "B":
            tab = bleu
        elif c == "O":
            tab = orange
        elif c == "Y":
            tab = jaune
            
        if colored54[4] == c:
            tab.extend(colored54[:4])
            tab.extend(colored54[5:9])
        elif colored54[22] == c:
            tab.extend(colored54[9:12])
            tab.append(colored54[21])
            tab.append(colored54[23])
            tab.extend(colored54[33:36])
        elif colored54[25] == c:
            tab.extend(colored54[12:15])
            tab.append(colored54[24])
            tab.append(colored54[26])
            tab.extend(colored54[36:39])
        elif colored54[28] == c:
            tab.extend(colored54[15:18])
            tab.append(colored54[27])
            tab.append(colored54[29])
            tab.extend(colored54[39:42])
        elif colored54[31] == c:
            tab.extend(colored54[18:21])
            tab.append(colored54[30])
            tab.append(colored54[32])
            tab.extend(colored54[42:45])
        else:
            tab.extend(colored54[45:49])
            tab.extend(colored54[50:])

    colored54_ordonne.extend(vert[:3])
    colored54_ordonne.extend(rouge[:3])
    colored54_ordonne.extend(bleu[:3])
    colored54_ordonne.extend(orange[:3])
    colored54_ordonne.extend(vert[3:5])
    colored54_ordonne.extend(rouge[3:5])
    colored54_ordonne.extend(bleu[3:5])
    colored54_ordonne.extend(orange[3:5])
    colored54_ordonne.extend(vert[5:])
    colored54_ordonne.extend(rouge[5:])
    colored54_ordonne.extend(bleu[5:])
    colored54_ordonne.extend(orange[5:])
    colored54_ordonne.extend(jaune)
            
    return colored54_ordonne


if __name__=="__main__":
    """Les tests des fonctions se font ici"""
    cube = colored54_to_perm48("OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG")
    if "".join(cube) == "OGRBYBGBOYOWOWGRYGYYBBRYRWOOBWYGROWGRWWRYBRGWBOG":
        print("OK")
    else:
        print("KO : " + "".join(cube))
