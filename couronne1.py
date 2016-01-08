from cube import *
from CubeDisplay import *

""" 
Stratégie :

Boucle tant que la première couronne n'est pas réalisée

Si face du haut (blanche) :
	- Vérifier si la partie blanche est bien placée, sinon on descend la pièce

Si face 1,2,3,4 :
	- si la pièce est sur la partie haute de la face, on la redescend
	- si c'est sur la partie basse :
		. si c'est sur le coin inférieur gauche : on se place en asc2
		. si c'est sur le coin inférieur droit : on se place en asc1

Si face 5 :
	- La ramener sur une face 1,2,3,4 à l'aide de go_to_asc1 pour ascenceur
"""

def couronne1(cube):
# Utilisation d'un compteur qui compte les mouvements
# Mouvement est une chaine de caractères contenant la liste des mouvements
	#cpt=0
	mouvement=""
	coinW=[1,3,6,8]
	fini = couronne1Done(cube)

	while not fini :
		#print("boucle")
		# Parcours du cube
		for i in range(0,len(cube.lCube)):
			for j in [0,2]:
				for k in [0,2]:

		# 1er cas : case blanche déjà sur la face up
					if i==0 and cube.lCube[i][j][k] in coinW :
						if bienPlace(cube,j,k) is False :
							# Ce n'est pas bien placé, on descend
							mouvement+=descente0(cube,j,k)
							#print("descente0")
							#cpt+=3


					if i in [1,2,3,4]:

		# Deuxième cas, la case blanche est sur le haut d'une face
						if j == 0 and cube.lCube[i][j][k] in coinW :
								# On la descend
							mouvement+=descente1234(cube,i,k)
							#print("descente1234")
							#cpt+=3

# Pour optimiser ici, on peut chercher quand il vaut mieux faire un turn' ou turn

		# Troisième cas, la case blanche est sur la partie basse d'une face :
						if j == 2 and k ==2 and cube.lCube[i][j][k] in coinW :
							# Configuration de l'ascenceur1 :
							n=i
							while not pos_asc1(cube,n):
								cube.turn(5)
								mouvement+="D"
								#cpt+=1
								if n == 4 :
									n = 1 
								else :
									n+=1
							mouvement+=ascenceur1(cube,n)
							#print("ascenceur1")
							#cpt+=4


						if j == 2 and k == 0 and cube.lCube[i][j][k] in coinW :
							# Configuration de l'ascenceur 2 : 
							n=i
							while not pos_asc2(cube,n):
								cube.turn(5)
								mouvement+="D"
								#cpt+=1
								if n == 4 :
									n = 1
								else :
									n+=1
							
							if n == 1 :
								mouvement+=ascenceur2(cube,4)
							else :
								mouvement+=ascenceur2(cube,n-1)
							#print("ascenceur2")
							#cpt+=4


					if i==5 and cube.lCube[i][j][k] in coinW :
						#cpt+=5
						mouvement+=go_to_asc1(cube,j,k)
						#print("go_to_asc1")

	# A voir s'il n'est pas possible de simplifier cette suite de mouvements (5)
		
		#print(fini)
		fini = couronne1Done(cube)
		#print(fini)

	#print("sortie de boucle")
	# return cpt
	return mouvement 

# --------------------------------------------------------------------------
# Fonction qui détermine si la première couronne est réalisée ou non
# Args : objet cube
# Return : Boolean 
def couronne1Done(cube) : 
	couronne = list(range(9,21))
	couronneDone = False 

	if cube.lCube[1][0] == couronne[0:3] and cube.lCube[2][0] == couronne[3:6] and cube.lCube[3][0] == couronne[6:9] and cube.lCube[4][0] == couronne[9:12] :
		couronneDone = True

	return couronneDone
# --------------------------------------------------------------------------
# Fonction qui descend un cube blanc de la face up s'il n'est pas bien placé
# Args : objet cube, position (sur la face blanche)
# Return : String (liste de mouvements)
def descente0(cube,j,k):
	if j == 0 and k == 0 :
		cube.turnInv(1)
		cube.turnInv(5)
		cube.turn(1)
		return "L'D'L"

	if j == 0 and k == 2 :
		cube.turn(3)
		cube.turnInv(5)
		cube.turnInv(3)
		return "RD'R'"

	if j == 2 and k == 0 :
		cube.turn(1)
		cube.turnInv(5)
		cube.turnInv(1)
		return "LD'R'"

	if j == 2 and k == 2 :
		cube.turnInv(3)
		cube.turnInv(5)
		cube.turn(3)
		return "R'D'R"


# --------------------------------------------------------------------------
# Fonction qui permet de savoir si la configuration actuelle permet ascenceur1
# Args : objet cube, face
# Return : Boolean
def pos_asc1(cube,face):
	if face == 4 :
		return coin_couleur(cube,1,0)
	else :
		return coin_couleur(cube,face+1,0)

def pos_asc2(cube,face):
	if face == 1 :
		return coin_couleur(cube,4,2)
	else :
		return coin_couleur(cube,face-1,2)

# --------------------------------------------------------------------------
# Fonction pour savoir si un cube blanc sur la face up est bien placé
# Args : objet cube, position sur une face (j,k)
# Return : Boolean

def bienPlace(cube,i,j):
	if i == 0 and j == 0 and cube.lCube[0][i][j] == 1 :
		return True
	elif i == 0 and j == 2 and cube.lCube[0][i][j] == 3 :
		return True
	elif i == 2 and j == 0 and cube.lCube[0][i][j] == 6 :
		return True
	elif i == 2 and j == 2 and cube.lCube[0][i][j] == 8 :
		return True
	else :
		return False

# --------------------------------------------------------------------------
# Fonction qui renvoie true si le coin est de la même couleur que la face
# Args : objet cube et une position (i,j,k)
# Return : Boolean

def coin_couleur(cube,face,k):
	"""coinR=[15,17]
	coinL=[9,11]
	coinF=[12,14]
	coinB=[18,20]"""

	if face == 1 and (cube.lCube[1][2][k] == 9 or cube.lCube[1][2][k] == 11) :
		return True
	elif face == 2 and (cube.lCube[2][2][k] == 12 or cube.lCube[2][2][k] == 14) :
		return True
	elif face == 3 and (cube.lCube[3][2][k] == 15 or cube.lCube[3][2][k] == 17) :
		return True
	elif face == 4 and (cube.lCube[4][2][k] == 18 or cube.lCube[4][2][k] == 20) :
		return True
	else :
		return False

# --------------------------------------------------------------------------
def ascenceur1(cube,face):	
# face de 1 à 4		
# R,F',R',F en étant devant la face où l'on doit effectuer le mouvement
	if face == 1 :
		cube.turn(2)
		cube.turnInv(1)
		cube.turnInv(2)
		cube.turn(1)
		return "FL'F'L"

	if face == 2 :
		cube.turn(3)
		cube.turnInv(2)
		cube.turnInv(3)
		cube.turn(2)
		return "RF'R'F"

	if face == 3 :
		cube.turn(4)
		cube.turnInv(3)
		cube.turnInv(4)
		cube.turn(3)
		return "BR'B'R"

	if face == 4 :
		cube.turn(1)
		cube.turnInv(4)
		cube.turnInv(1)
		cube.turn(4)
		return "LB'L'B"

# --------------------------------------------------------------------------
def ascenceur2(cube,face):	
# face de 1 à 4		
# F',R,F,R' en étant devant la face où l'on doit effectuer le mouvement
	if face == 1 :
		cube.turnInv(1)
		cube.turn(2)
		cube.turn(1)
		cube.turnInv(2)
		return "L'FLF'"

	if face == 2 :
		cube.turnInv(2)
		cube.turn(3)
		cube.turn(2)
		cube.turnInv(3)
		return "F'RFR'"

	if face == 3 :
		cube.turnInv(3)
		cube.turn(4)
		cube.turn(3)
		cube.turnInv(4)
		return "R'BRB'"

	if face == 4 :
		cube.turnInv(4)
		cube.turn(1)
		cube.turn(4)
		cube.turnInv(1)
		return "B'LBL'"

# --------------------------------------------------------------------------
# Fonction qui ramène une pièce blanche de la face down sur une face 1,2,3,4
# Args : objet cube, position sur la face down (j,k)
# Return : String
def go_to_asc1(cube,j,k):
# R',D',D',R,D par rapport à Front
	if (j == 0 and k == 0) or (j == 2 and k == 0):
		cube.turnInv(1)
		cube.turnInv(5)
		cube.turnInv(5)
		cube.turn(1)
		cube.turn(5)
		return "L'D'D'LD"

	if (j == 0 and k == 2) or (j == 2 and k == 2) :
		cube.turnInv(3)
		cube.turnInv(5)
		cube.turnInv(5)
		cube.turn(3)
		cube.turn(5)
		return "R'D'D'RD"
	

# --------------------------------------------------------------------------
# Fonction pour redescendre un cube s'il est sur la face 1,2,3 ou 4 
# Args : objet cube, face et sa position sur la partie haute (0 ou 2)
# Return : String (liste de mouvements)
def descente1234(cube,i,k):
# Même mouvement que descente0 : R',D',R
# A OPTIMISER
	if (i == 1 and k == 0) or (i == 4 and k == 2) :
		cube.turn(4)
		cube.turnInv(5)
		cube.turnInv(4)
		return "BD'B'"

	if (i == 2 and k == 0) or (i == 1 and k == 2) :
		cube.turn(1)
		cube.turnInv(5)
		cube.turnInv(1)
		return "LD'L'"

	if (i == 2 and k == 2) or (i == 3 and k == 0) :
		cube.turnInv(3)
		cube.turnInv(5)
		cube.turn(3)
		return "R'D'R"

	if (i == 3 and k == 2) or (i == 4 and k == 0) :
		cube.turn(3)
		cube.turnInv(5)
		cube.turnInv(3)
		return "RD'R'"

# --------------------------------------------------------------------------

"""  --- TEST DE LA FONCTION --

if __name__ == "__main__" :
	# Test couronne1Done :
	#cube = cube("WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGBYYOYBRYYORRBYYYYOG")
	#cube = cube("GWBWWWGWGOGOYRYRBYOOWYGOYRRBBYBORBOBWGGWBRBRWOYRGYORGY")

	# Test de fonctions :
	#print(cube.lCube[1][1][2])
	#print(cube)
	#print(bienPlace(cube,2,0))
	#print(cube)
	#print(descente1234(cube,2,0))
	#descente0(cube,2,0)
	#print(cube)

	# Test de couronne : 
	#cube = cube("GWBWWWWWGOGGRRYRBYOOWYGGYRRBBYBORBOGYBRBROBOWOOYGYGRYW")
	#cube = cube("GWBWWWWWGOGRBRYRBYOOWYGGORRBBYBORBOGWBRBYYOROROYYYGWGG")
	cube = cube("YWBWWWBWYBGOWRGOBWROOYGYRRGYBOGOOYRGORGROWRYBWGYBYBRBG")

	drawCube(cube.cube_to_color54())
	print(couronne1(cube))
	drawCube(cube.cube_to_color54())"""

