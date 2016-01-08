from cube import *
from CubeDisplay import *
from poqb import *

def croixBlanche(cube):

	mouvement=""

	"""
	while(croixBlancheDone(cube) == False):
		print("croix blanche non terminée")
	"""
	listeFacetteBlanche = [2, 4, 5, 7]
	for facette in listeFacetteBlanche:
		for i in range(0,6):
			for j in range(0,3):
				for k in range(0,3):
					if cube.lCube[i][j][k] == facette:
						print("Facette numéro : "+str(facette)+" position "+str(i), str(j), str(k))

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
	croixBlanche(cube)
	drawCube(cube.cube_to_color54())
	
