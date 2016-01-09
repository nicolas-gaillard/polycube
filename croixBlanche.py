from cube import *
from CubeDisplay import *
from poqb import *

def croixBlanche(cube):

	mouvement=""

	"""
	while(croixBlancheDone(cube) == False):
		print("croix blanche non terminée")
	"""

	listePosition = [0,0,0,0,0,0,0,0]
	listePositionDefinitive = [0,0,[0, 0, 1],0,[0, 1, 0], [0, 1, 2],0,[0, 2, 1]]
	listeFacetteBlanche = [2, 4, 5, 7]
	for facette in listeFacetteBlanche:
		for i in range(0,6):
			for j in range(0,3):
				for k in range(0,3):
					if cube.lCube[i][j][k] == facette:
						print("Facette numéro : "+str(facette)+" position "+str(i), str(j), str(k))
						listePosition[facette] = [i,j,k]
						print(listePosition[facette])
						print(listePositionDefinitive[facette])

	for facette in listeFacetteBlanche:
		#Si la piece est déjà situé sur la face blanche, on fait seulement une rotation de cette face
		if listePosition[facette][0] == 0 :
			while(listePosition[facette] != listePositionDefinitive[facette]):
				cube.turn(0)
				listePosition = position(facette, listePosition)
				print("mouvement de la face  0 pour positionner la facette :"+str(facette))

		#Si la piece est situé sur la face jaune, on la position de facon à pouvoir la placer en deux mouvement
		if listePosition[facette][0] == 5 :
			if facette == 4 :
				while(listePosition[4][2] != listePositionDefinitive[4][2]):
					cube.turn(5)
					listePosition = position(facette, listePosition)
					print("mouvement de la face 5 (facette4)")
				cube.turn(1)
				cube.turn(1)
				print("mouvement x2 face 1")

			if facette == 5 :
				while(listePosition[5][2] != listePositionDefinitive[5][2]):
					cube.turn(5)
					listePosition = position(facette, listePosition)
					print("mouvement de la face 5 (facette5)")
				cube.turn(3)
				cube.turn(3)
				print("mouvement x2 face 3")

			if facette == 2 :
				while(listePosition[2][1] != listePositionDefinitive[2][1]):
					cube.turn(5)
					listePosition = position(facette, listePosition)
					print("mouvement de la face 5 (facette2)")
				cube.turn(4)
				cube.turn(4)
				print("mouvement x2 face 4")

			if facette == 7:
				while(listePosition[7][1] != listePositionDefinitive[7][1]):
					cube.turn(5)
					listePosition = position(facette, listePosition)
					print("mouvement de la face 5 (facette7)")
				cube.turn(2)
				cube.turn(2)
				print("mouvement x2 face 2")

		# Placement de la facette numéro 2 en fonction de la face sur laquelle elle est situé
		if listePosition[2][0] == 2:
			if listePosition[2][1] == 0:
				turn.cube(2)
				turn.cube(0)
				turn.cube(3)
				turn.cubeInv(0)
			if listePosition[2][1] == 2:
				turn.cube(2)
				turn.cube(0)
				turn.cube(3)
				turn.cubeInv(0)
				turn.cubeInv(2)
			if listePosition[2][1] == 1 and listePosition[2][2] == 2:
				turn.cube(0)
				turn.cube(2)
				turn.cubeInv(0)
			if listePosition[2][1] == 1 and listePosition[2][2] == 0:
				turn.cubeInv(0)
				turn.cubeInv(1)
				turn.cube(0)

		if listePosition[2][0] == 3:


			listePosition = position(facette, listePosition)


			
def position(facette, listePosition):
	for i in range(0,6):
			for j in range(0,3):
				for k in range(0,3):
					if cube.lCube[i][j][k] == facette:
						print("Facette numéro : "+str(facette)+" position "+str(i), str(j), str(k))
						listePosition[facette] = [i,j,k]
	return listePosition



def croixBlancheDone(cube):
	""" Cette fonction nous permet de savoir si la croix blanche est terminé ou non
	Pour cela on regarde si au position de la croix blanche il y a bien les 4 facettes
	blanche et celle qui ne bouge pas au centre"""

	return (cube.lCube[0][0][1] == 2 and cube.lCube[0][1][0] == 4 and cube.lCube[0][1][2] == 5 and cube.lCube[0][2][1] == 7)


if __name__ == "__main__" :

	stringCube = generator()
	print(stringCube)
	cube = cube(stringCube)
	print(croixBlancheDone(cube))
	drawCube(cube.cube_to_color54())
	croixBlanche(cube)
	drawCube(cube.cube_to_color54())
	
