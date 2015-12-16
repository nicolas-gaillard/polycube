from cube import *

# Pour optimiser, anticiper le mouvement suivant et voir si des mouvements peuvent 
# être raccourcis


""" 
A chaque modification : recommencer l'algorithme

Si face du haut :
	Vérifier si c'est bien placé, sinon on le descend

Si face 1,2,3,4 :
	si c'est sur la partie haute de la face, on la redescends
	si c'est sur la partie basse, la placer --> ascenceur suivanta la position

si face 5 :
	le ramener sur une face 1,2,3,4 et faire l'ascenceur à l'aide de go_to_asc1
"""

def couronne1(cube):

	# Utilisation d'un compteur qui compte les manipulations
	cpt=0
	coinW=[1,3,6,8]

	for i in range(0,len(cube.lCube)):
		for j in [0,2]:
			for k in [0,2]:
				if cube.lCube[i][j][k] in coinW :
				# 1er cas, déjà sur la face up
					if i==0 :
						if j==0:
							if k==0:
							if k==2:
						if j==2:
							if k==0:
							if k==2:

					if i in [1,2,3,4]:
					if i==5:
						# go_to_asc1(cube,i) -> à modifier pour que ça corresponde bien

				# On regarde s'il est bien placé
				# Sinon on le descend

	return cpt 

"""def pos_asc1(cube,face):
	if cube.lCube[i][2][2]"""

# Fonction pour savoir si un cube blanc sur la face up est bien placé
"""def bien_placer(i,j):
	placer=True
	if([0][i][j]):

	return placer"""

def ascenceur1(cube,face):
	if face == 1 :
		cube.turn(2)
		cube.turnprim(1)
		cube.turnprim(2)
		cube.turn(1)

	if face == 2 :
		# R,F',R',F
		cube.turn(3)
		cube.turnprim(2)
		cube.turnprim(3)
		cube.turn(2)

	if face == 3 :
		cube.turn(4)
		cube.turnprim(3)
		cube.turnprim(4)
		cube.turn(3)

	if face == 4 :
		cube.turn(1)
		cube.turnprim(4)
		cube.turnprim(1)
		cube.turn(4)

	# Le compteur prend +4 du à 4 manipulations
	cpt+=4

# On doit faire attention à la face où on se trouve et se ramener à un déplacement par
# rapport à F 
# R,F',R',F de la face mais voir ce que c'est selon les face (F,R,L ou B).

	return "RF'R'F"

def ascenceur2(cube,face):
	if face == 1 :
		cube.turnprim(1)
		cube.turn(2)
		cube.turn(1)
		cube.turnprim(2)

	if face == 2 :
		cube.turnprim(2)
		cube.turn(3)
		cube.turn(2)
		cube.turnprim(3)

	if face == 3 :
		cube.turnprim(3)
		cube.turn(4)
		cube.turn(3)
		cube.turnprim(4)

	if face == 4 :
		cube.turnprim(4)
		cube.turn(1)
		cube.turn(4)
		cube.turnprim(1)

	# Le compteur prend +4, du à 4 manipulations
	cpt+=4

	# On se place sur la face où on a la disposition :
	# F',R,F,R'
	return "F'RFR'"

def go_to_asc1(cube,face):
	if face == 1 :
		cube.turnprim(2)
		cube.turnprim(5)
		cube.turnprim(5)
		cube.turn(2)
		cube.turn(5)

	if face == 2 :
		cube.turnprim(3)
		cube.turnprim(5)
		cube.turnprim(5)
		cube.turn(3)
		cube.turn(5)

	if face == 3 :
		cube.turnprim(4)
		cube.turnprim(5)
		cube.turnprim(5)
		cube.turn(4)
		cube.turn(5)

	if face == 4 : 
		cube.turnprim(1)
		cube.turnprim(5)
		cube.turnprim(5)
		cube.turn(1)
		cube.turn(5)

	# Le compteur prend +5 du à 5 manipulations 
	cpt+=5

	# R',D',D',R,D	
	return "R'D'D'RD"

def descente(cube):
	# S'il est en 00
	cube.turnprim()
	cube.turnprim(5)
	cube.turn()

	# S'il est en 02
	cube.turnprim()
	cube.turnprim(5)
	cube.turn()

	# S'il est en 20
	cube.turnprim()
	cube.turnprim(5)
	cube.turn()

	# S'il est en 22
	cube.turnprim()
	cube.turnprim(5)
	cube.turn()

	# Mouvement : R',D',R
	pass
