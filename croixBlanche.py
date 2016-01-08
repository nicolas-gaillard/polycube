from cube import *
from CubeDisplay import *
from poqb import *

def croixBlanche(cube):

	mouvement=""

	while(croixBlancheDone(cube) == False):
		print("croix blanche non terminée")

def croixBlancheDone(cube):
	""" Cette fonction nous permet de savoir si la croix blanche est terminé ou non
	Pour cela on regarde si au position de la croix blanche il y a bien les 4 facettes
	blanche et celle qui ne bouge pas au centre"""

	return (cube.lCube[0][0][1] == 2 and cube.lCube[0][1][0] == 4 and cube.lCube[0][1][2] == 5 and cube.lCube[0][2][1] == 7)


if __name__ == "__main__" :

	cube = cube("BRBRWBROWWWYBWGROYOYOGGWGROYBBROOGBWGBWBGRYGOOWRYYYYRG")
	print(croixBlancheDone(cube))
	drawCube(cube.cube_to_color54())
