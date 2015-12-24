from cube import *
from cubeDisplay import *

# Pour optimiser, anticiper le mouvement suivant et voir si des mouvements peuvent 
# être raccourcis


""" 
A chaque mouvement : rappeler la fonction qui résoud la première couronne

Si face du haut :
	Vérifier si c'est bien placé, sinon on le descend

Si face 1,2,3,4 :
	si c'est sur la partie haute de la face, on la redescends
	si c'est sur la partie basse, la placer --> ascenceur suivant la position

si face 5 :
	le ramener sur une face 1,2,3,4 et faire l'ascenceur à l'aide de go_to_asc1
"""

def couronne1(cube):

	# Utilisation d'un compteur qui compte les mouvements
	# Mouvement est une chaine de caractères contenant la liste des mouvements
	cpt=0
	mouvement=""
	coinW=[1,3,6,8]
	fini = couronne1Done(cube)

	while not fini :
		for i in range(0,len(cube.lCube)):
			for j in [0,2]:
				for k in [0,2]:

				# 1er cas, déjà sur la face up
					if i==0 and cube.lCube[i][j][k] in coinW :
						if bienPlace(j,k) is False :
							# Ce n'est pas bien placé, on descend
							mouvement+=descente0(cube,j,k)
							cpt+=3


					if i in [1,2,3,4]:
						# Cas ou la case blanche est sur le haut d'une face
						if j == 0 and cube.lCube[i][j][k] in coinW :
								# On la descend

# Pour optimiser ici, on peut chercher quand il vaut mieux faire un turn' ou turn
						if j == 2 and cube.lCube[i][j][k] in coinW :
							n=i
							while not pos_asc1(cube,n,j,k):
								cube.turn(5)
								mouvement+="D"
								cpt+=1
								if n == 4 :
									n = 1 
								else :
									n+=1
							ascenceur1(cube,n)

# S'il est sur la partie basse d'une face, et qu'il est blanc, on regarde 
# si on est en pos asc1, sinon on le place


						"""if j == 2 and cube.lCube[i][j][k] :"""
# Si c'est de la même couleur que cube.lCube i 1 1 alors on regarde si
# on est en pos asc2 sinon on le place et on le fait
					if i==5:
				# go_to_asc1(cube,i) -> à modifier pour que ça corresponde bien
		
		fini = couronne1Done(cube)

	return cpt, mouvement 

def couronne1Done(cube) : 
	couronne = liste(range(9,21))
	couronneDone = False 

	if cube.lCube[1][1] == couronne[0:3] and cube.lCube[2][1] == couronne[3:6] and cube.lCube[3][1] == couronne[6:9] and cube.lCube[4][1] == couronne[9:12] :
		couronneDone = True  

# Fonction qui descend un cube blanc de la face up s'il n'est pas bien placé
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



"""def pos_asc1(cube,face):
	if cube.lCube[i][2][2]"""

"""def pos_asc2(cube,i,j,k):
	if cube.lCube[i][j][k] == cube.lCube[i][1][1] :
		if i == 4 and cube.lCube[1][2][0] in coinW :
			return True
		elif cube.lCube[i+1][2][0] in coinW :
			return True
		else : 
			return False
	else : 
		return False"""


# Fonction pour savoir si un cube blanc sur la face up est bien placé
def bienPlace(i,j):
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

def ascenceur1(cube,face):
	if face == 1 :
		cube.turn(2)
		cube.turnInv(1)
		cube.turnInv(2)
		cube.turn(1)

	if face == 2 :
		# R,F',R',F
		cube.turn(3)
		cube.turnInv(2)
		cube.turnInv(3)
		cube.turn(2)

	if face == 3 :
		cube.turn(4)
		cube.turnInv(3)
		cube.turnInv(4)
		cube.turn(3)

	if face == 4 :
		cube.turn(1)
		cube.turnInv(4)
		cube.turnInv(1)
		cube.turn(4)


# On doit faire attention à la face où on se trouve et se ramener à un déplacement par
# rapport à F 
# R,F',R',F de la face mais voir ce que c'est selon les face (F,R,L ou B).

	return "RF'R'F"

def ascenceur2(cube,face):
	if face == 1 :
		cube.turnInv(1)
		cube.turn(2)
		cube.turn(1)
		cube.turnInv(2)

	if face == 2 :
		cube.turnInv(2)
		cube.turn(3)
		cube.turn(2)
		cube.turnInv(3)

	if face == 3 :
		cube.turnInv(3)
		cube.turn(4)
		cube.turn(3)
		cube.turnInv(4)

	if face == 4 :
		cube.turnInv(4)
		cube.turn(1)
		cube.turn(4)
		cube.turnInv(1)

	# On se place sur la face où on a la disposition :
	# F',R,F,R'
	return "F'RFR'"

def go_to_asc1(cube,face):
	if face == 1 :
		cube.turnInv(2)
		cube.turnInv(5)
		cube.turnInv(5)
		cube.turn(2)
		cube.turn(5)

	if face == 2 :
		cube.turnInv(3)
		cube.turnInv(5)
		cube.turnInv(5)
		cube.turn(3)
		cube.turn(5)

	if face == 3 :
		cube.turnInv(4)
		cube.turnInv(5)
		cube.turnInv(5)
		cube.turn(4)
		cube.turn(5)

	if face == 4 : 
		cube.turnInv(1)
		cube.turnInv(5)
		cube.turnInv(5)
		cube.turn(1)
		cube.turn(5)

	# R',D',D',R,D	
	return "R'D'D'RD"

# Fonction pour redescendre un cube s'il est sur la face 1,2,3 ou 4 
def descente1234(cube,j,k):
	if j == 0 and k == 0 :
	# S'il est en 00
		cube.turnInv()
		cube.turnInv(5)
		cube.turn()

	if j == 0 and k == 2 :
	# S'il est en 02
		cube.turnInv()
		cube.turnInv(5)
		cube.turn()

	"""if j == 2 and k == 0 :
	# S'il est en 20
		cube.turnInv()
		cube.turnInv(5)
		cube.turn()

	if j == 2 and k == 2 :
	# S'il est en 22
		cube.turnInv()
		cube.turnInv(5)
		cube.turn()"""

	# Mouvement : R',D',R
