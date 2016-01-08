from cube import *
from CubeDisplay import *

def croixBlanche(cube):

	mouvement=""

def croixBlancheDone(cube):
	""" Cette fonction nous permet de savoir si la croix blanche est terminé ou non
	Pour cela on regarde si au position de la croix blanche il y a bien les 4 facettes
	blanche et celle qui ne bouge pas au centre"""
	croixDone = False
	if cube.lCube[0][0][1] == "W" and cube.lCube[0][1][0] == "W" and cube.lCube[0][1][2] == "W" and cube.lCube[0][2][1] == "W"

if __name__ == "__main__" :

	cube = cube("YWBWWWBWYBGOWRGOBWROOYGYRRGYBOGOOYRGORGROWRYBWGYBYBRBG")

	drawCube(cube.cube_to_color54())
