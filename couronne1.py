from cube import *

# Pour optimiser, anticiper le mouvement suivant et voir si des mouvements peuvent 
# être raccourcis

def couronne1(self,cube):

	# Utilisation d'un compteur qui compte les manipulations
	cpt=0

	coinW=[1,3,6,8]
	for i in range(0,len(cube.lCube)):
		for j in [0,2]:
			for k in [0,2]:
				if cube.lCube[i][j][k] in coinW :
				# 1er cas, déjà sur la face up
					if i==0 :
				# On regarde s'il est bien placé
				# Sinon on le descend

	return cpt 


def ascenceur1(self,face):
	if face == 1 :
		self.turn(2)
		self.turnprim(1)
		self.turnprim(2)
		self.turn(1)

	if face == 2 :
		# R,F',R',F
		self.turn(3)
		self.turnprim(2)
		self.turnprim(3)
		self.turn(2)

	if face == 3 :
		self.turn(4)
		self.turnprim(3)
		self.turnprim(4)
		self.turn(3)

	if face == 4 :
		self.turn(1)
		self.turnprim(4)
		self.turnprim(1)
		self.turn(4)

	# Le compteur prend +4 du à 4 manipulations
	cpt+=4

# On doit faire attention à la face où on se trouve et se ramener à un déplacement par
# rapport à F 
# R,F',R',F de la face mais voir ce que c'est selon les face (F,R,L ou B).

	return "RF'R'F"

def ascenceur2(self,face):
	if face == 1 :
		self.turnprim(1)
		self.turn(2)
		self.turn(1)
		self.turnprim(2)

	if face == 2 :
		self.turnprim(2)
		self.turn(3)
		self.turn(2)
		self.turnprim(3)

	if face == 3 :
		self.turnprim(3)
		self.turn(4)
		self.turn(3)
		self.turnprim(4)

	if face == 4 :
		self.turnprim(4)
		self.turn(1)
		self.turn(4)
		self.turnprim(1)

	# Le compteur prend +4, du à 4 manipulations
	cpt+=4

	# On se place sur la face où on a la disposition :
	# F',R,F,R'
	return "F'RFR'"

def go_to_asc1(self,face):
	if face == 1 :
		self.turnprim(2)
		self.turnprim(5)
		self.turnprim(5)
		self.turn(2)
		self.turn(5)

	if face == 2 :
		self.turnprim(3)
		self.turnprim(5)
		self.turnprim(5)
		self.turn(3)
		self.turn(5)

	if face == 3 :
		self.turnprim(4)
		self.turnprim(5)
		self.turnprim(5)
		self.turn(4)
		self.turn(5)

	if face == 4 : 
		self.turnprim(1)
		self.turnprim(5)
		self.turnprim(5)
		self.turn(1)
		self.turn(5)

	# Le compteur prend +5 du à 5 manipulations 
	cpt+=5

	# R',D',D',R,D	
	return "R'D'D'RD"

def descente(self):
	# S'il est en 00
	self.turnprim()
	self.turnprim(5)
	self.turn()

	# S'il est en 02
	self.turnprim()
	self.turnprim(5)
	self.turn()

	# S'il est en 20
	self.turnprim()
	self.turnprim(5)
	self.turn()

	# S'il est en 22
	self.turnprim()
	self.turnprim(5)
	self.turn()

	# Mouvement : R',D',R
	pass
