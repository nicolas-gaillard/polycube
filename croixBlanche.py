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
	positionAll(listePosition)


	for i in range(0, 10):
		# Placement de la facette numéro 2 en fonction de la face sur laquelle elle est situé
		# Cas de la face rouge
		if listePosition[2][0] == 2:
			if listePosition[2][1] == 0:
				cube.turnInv(2)
				cube.turnInv(0)
				cube.turnInv(1)
				cube.turn(0)
				cube.turn(1)
				mouvement += "F'U'L'UL"
			if listePosition[2][1] == 2:
				cube.turnInv(5)
				cube.turn(1)
				cube.turnInv(4)
				cube.turnInv(1)
				mouvement += "D'LB'L'"
			if listePosition[2][1] == 1 and listePosition[2][2] == 2:
				cube.turn(0)
				cube.turn(3)
				cube.turnInv(0)
				cube.turnInv(3)
				mouvement += "URU'R'"
			if listePosition[2][1] == 1 and listePosition[2][2] == 0:
				cube.turnInv(0)
				cube.turnInv(1)
				cube.turn(0)
				cube.turn(1)
				mouvement += "U'L'UL"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face bleue
		if listePosition[2][0] == 3:
			if listePosition[2][1] == 1 and listePosition[2][2] == 2:
				cube.turn(4)
				mouvement += "B"
			if listePosition[2][1] == 2:
				cube.turnInv(3)
				cube.turn(4)
				cube.turn(3)
				mouvement += "R'BR"
			if listePosition[2][1] == 1 and listePosition[2][2] == 0:
				cube.turn(3)
				cube.turn(3)
				cube.turn(4)
				cube.turn(3)
				cube.turn(3)
				mouvement += "RRBRR"
			if listePosition[2][1] == 0:
				cube.turn(3)
				cube.turn(4)
				mouvement += "RB"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face verte
		if listePosition[2][0] == 1:
			if listePosition[2][1] == 1 and listePosition[2][2] == 0:
				cube.turnInv(4)
				mouvement += "B'"
			if listePosition[2][1] == 1 and listePosition[2][2] == 2:
				cube.turn(1)
				cube.turn(1)
				cube.turnInv(4)
				cube.turn(1)
				cube.turn(1)
				mouvement += "LLB'LL"
			if listePosition[2][1] == 0:
				cube.turnInv(1)
				cube.turnInv(4)
				mouvement += "L'B'"
			if listePosition[2][1] == 2:
				cube.turn(1)
				cube.turnInv(4)
				cube.turnInv(1)
				mouvement += "LB'L'"
			listePosition = positionAll(listePosition, cube)

		#Cas de la face orange
		if listePosition[2][0] == 4:
			if listePosition[2][1] == 0:
				cube.turn(4)
				cube.turn(4)
				cube.turn(5)
				cube.turn(3)
				cube.turnInv(4)
				cube.turnInv(3)
				mouvement += "BBDRB'R'"
			if listePosition[2][1] == 2:
				cube.turn(5)
				cube.turn(3)
				cube.turnInv(4)
				cube.turnInv(3)
				mouvement += "DRB'R'"
			if listePosition[2][1] == 1 and listePosition[2][2] == 0:
				cube.turnInv(4)
				cube.turn(5)
				cube.turn(3)
				cube.turnInv(4)
				cube.turnInv(3)
				mouvement += "B'DRB'R'"
			if listePosition[2][1] == 1 and listePosition[2][2] == 2:
				cube.turn(4)
				cube.turn(5)
				cube.turn(3)
				cube.turnInv(4)
				cube.turnInv(3)
				mouvement += "BDRB'R'"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face jaune
		if listePosition[2][0] == 5:
			if listePosition[4][1] == 1 and listePosition[4][2] == 2:
				cube.turn(5)
				cube.turn(4)
				cube.turn(4)
				mouvement += "DBB"
			if listePosition[4][1] == 1 and listePosition[4][2] == 0:
				cube.turnInv(5)
				cube.turn(4)
				cube.turn(4)
				mouvement += "D'BB"
			if listePosition[4][1] == 0:
				cube.turn(5)
				cube.turn(5)
				cube.turn(4)
				cube.turn(4)
				mouvement += "DDBB"
			if listePosition[4][1] == 2:
				cube.turn(4)
				cube.turn(4)
				mouvement += "BB"
			listePosition = positionAll(listePosition, cube)

		# Placement de la facette numéro 4 en fonction de la face sur laquelle elle est situé
		# Cas de la face orange
		if listePosition[4][0] == 4:
			if listePosition[4][1] == 1 and listePosition[4][2] == 2:
				cube.turn(1)
				mouvement += "L"
			if listePosition[4][1] == 1 and listePosition[4][2] == 0:
				cube.turn(4)
				cube.turn(4)
				cube.turn(1)
				cube.turn(4)
				cube.turn(4)
				mouvement += "BBLBB"
			if listePosition[4][1] == 0:
				cube.turn(4)
				cube.turn(1)
				mouvement += "BL"
			if listePosition[4][1] == 2:
				cube.turnInv(4)
				cube.turn(1)
				cube.turn(4)
				mouvement += "B'LB"
			listePosition = positionAll(listePosition, cube)

		#Cas de la face rouge
		if listePosition[4][0] == 2:
			if listePosition[4][1] == 0:
				cube.turnInv(2)
				cube.turnInv(1)
				mouvement += "F'L'"
			if listePosition[4][1] == 1 and listePosition[4][2] == 0:
				cube.turnInv(1)
				mouvement += "L'"
			if listePosition[4][1] == 1 and listePosition[4][2] == 2:
				cube.turn(2)
				cube.turn(2)
				cube.turnInv(1)
				cube.turn(2)
				cube.turn(2)
				mouvement += "FFL'FF"
			if listePosition[4][1] == 2:
				cube.turn(2)
				cube.turnInv(1)
				cube.turnInv(2)
				mouvement += "FL'F'"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face verte
		if listePosition[4][0] == 1:
			if listePosition[4][1] == 2:
				cube.turn(5)
				cube.turn(2)
				cube.turnInv(1)
				cube.turnInv(2)
				mouvement += "DFL'F'"
			if listePosition[4][1] == 0:
				cube.turn(1)
				cube.turn(1)
				cube.turn(5)
				cube.turn(2)
				cube.turnInv(1)
				cube.turnInv(2)
				mouvement += "LLDFL'F'"
			if listePosition[4][1] == 1 and listePosition[4][2] == 0:
				cube.turnInv(1)
				cube.turn(5)
				cube.turn(2)
				cube.turnInv(1)
				cube.turnInv(2)
				mouvement += "L'DFL'F'"
			if listePosition[4][1] == 1 and listePosition[4][2] == 2:
				cube.turn(1)
				cube.turn(5)
				cube.turn(2)
				cube.turnInv(1)
				cube.turnInv(2)
				mouvement += "LDFL'F'"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face bleue
		if listePosition[4][0] == 3:
			if listePosition[4][1] == 2:
				cube.turn(5)
				cube.turnInv(4)
				cube.turn(1)
				cube.turn(4)
				mouvement += "DB'LB"
			if listePosition[4][1] == 1 and listePosition[4][2] == 2:
				cube.turn(0)
				cube.turn(4)
				cube.turnInv(0)
				cube.turnInv(4)
				mouvement += "UBU'B'"
			if listePosition[4][1] == 1 and listePosition[4][2] == 0:
				cube.turnInv(0)
				cube.turnInv(1)
				cube.turn(0)
				cube.turn(1)
				mouvement += "U'L'UL"
			if listePosition[4][1] == 0:
				cube.turnInv(3)
				cube.turnInv(0)
				cube.turnInv(1)
				cube.turn(0)
				cube.turn(1)
				mouvement += "R'U'L'UL"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face jaune
		if listePosition[4][0] == 5:
			if listePosition[4][1] == 2:
				cube.turn(5)
				cube.turn(1)
				cube.turn(1)
				mouvement += "DLL"
			if listePosition[4][1] == 1 and listePosition[4][2] == 2:
				cube.turn(5)
				cube.turn(5)
				cube.turn(1)
				cube.turn(1)
				mouvement += "DDLL"
			if listePosition[4][1] == 1 and listePosition[4][2] == 0:
				cube.turn(1)
				cube.turn(1)
				mouvement += "LL"
			if listePosition[4][1] == 0:
				cube.turnInv(5)
				cube.turn(1)
				cube.turn(1)
				mouvement += "D'LL"
			listePosition = positionAll(listePosition, cube)

		# Placement de la facette numéro 5 en fonction de la face sur laquelle elle est situé
		# Cas de la face orange
		if listePosition[5][0] == 4:
			if listePosition[5][1] == 0:
				cube.turnInv(4)
				cube.turnInv(3)
				mouvement += "B'R'"
			if listePosition[5][1] == 2:
				cube.turn(4)
				cube.turnInv(3)
				cube.turnInv(4)
				mouvement += "BR'B'"
			if listePosition[5][1] == 1 and listePosition[5][2] == 0:
				cube.turnInv(3)
				mouvement += "R'"
			if listePosition[5][1] == 1 and listePosition[5][2] == 2:
				cube.turn(4)
				cube.turn(4)
				cube.turnInv(3)
				cube.turn(4)
				cube.turn(4)
				mouvement += "BBR'BB"
			listePosition = positionAll(listePosition, cube)

		#Cas de la face rouge
		if listePosition[5][0] == 2:
			if listePosition[5][1] == 0:
				cube.turn(2)
				cube.turn(3)
				mouvement += "FR"
			if listePosition[5][1] == 2:
				cube.turnInv(2)
				cube.turn(3)
				cube.turn(2)
				mouvement += "F'RF"
			if listePosition[5][1] == 1 and listePosition[5][2] == 2:
				cube.turn(3)
				mouvement += "R"
			if listePosition[5][1] == 1 and listePosition[5][2] == 0:
				cube.turn(2)
				cube.turn(2)
				cube.turn(3)
				cube.turn(2)
				cube.turn(2)
				mouvement += "FFRFF"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face verte
		if listePosition[5][0] == 1:
			if listePosition[5][1] == 2:
				cube.turn(5)
				cube.turnInv(2)
				cube.turn(3)
				cube.turn(2)
				mouvement += "DF'RF"
			if listePosition[5][1] == 0:
				cube.turn(1)
				cube.turn(1)
				cube.turn(5)
				cube.turnInv(2)
				cube.turn(3)
				cube.turn(2)
				mouvement += "LLDF'RF"
			if listePosition[5][1] == 1 and listePosition[5][2] == 2:
				cube.turn(1)
				cube.turn(5)
				cube.turnInv(1)
				cube.turnInv(2)
				cube.turn(3)
				cube.turn(2)
				mouvement += "LDL'F'RF"
			if listePosition[5][1] == 1 and listePosition[5][2] == 0:
				cube.turnInv(1)
				cube.turn(5)
				cube.turn(1)
				cube.turnInv(2)
				cube.turn(3)
				cube.turn(2)
				mouvement += "L'DLF'RF"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face bleue
		if listePosition[5][0] == 3:
			if listePosition[5][1] == 0:
				cube.turn(3)
				cube.turnInv(0)
				cube.turn(4)
				cube.turn(0)
				cube.turnInv(4)
				mouvement += "RU'BUB'"
			if listePosition[5][1] == 0:
				cube.turn(5)
				cube.turn(4)
				cube.turnInv(3)
				cube.turnInv(4)
				mouvement += "DBR'B'"
			if listePosition[5][1] == 1 and listePosition[5][2] == 2:
				cube.turnInv(0)
				cube.turn(4)
				cube.turn(0)
				cube.turnInv(4)
				mouvement += "U'BUB'"
			if listePosition[5][1] == 1 and listePosition[5][2] == 0:
				cube.turn(0)
				cube.turnInv(2)
				cube.turnInv(0)
				cube.turn(1)
				mouvement += "UR'U'L"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face jaune
		if listePosition[5][0] == 5:
			if listePosition[5][1] == 2:
				cube.turnInv(5)
				cube.turn(3)
				cube.turn(3)
				mouvement += "D'RR"
			if listePosition[5][1] == 1 and listePosition[5][2] == 2:
				cube.turn(3)
				cube.turn(3)
				mouvement += "RR"
			if listePosition[5][1] == 1 and listePosition[5][2] == 0:
				cube.turn(5)
				cube.turn(5)
				cube.turn(3)
				cube.turn(3)
				mouvement += "DDRR"
			if listePosition[5][1] == 0:
				cube.turn(5)
				cube.turn(3)
				cube.turn(3)
				mouvement += "DRR"
			listePosition = positionAll(listePosition, cube)

		# Placement de la facette numéro 7 en fonction de la face sur laquelle elle est situé
		# Cas de la face orange
		if listePosition[7][0] == 4:
			if listePosition[7][1] == 2:
				cube.turn(5)
				cube.turnInv(1)
				cube.turn(2)
				cube.turn(1)
				mouvement += "DL'FL"
			if listePosition[7][1] == 0:
				cube.turn(4)
				cube.turn(0)
				cube.turn(1)
				cube.turnInv(0)
				mouvement += "BULU'"
			if listePosition[7][1] == 1 and listePosition[7][2] == 2:
				cube.turn(0)
				cube.turn(1)
				cube.turnInv(0)
				mouvement += "ULU'"
			if listePosition[7][1] == 1 and listePosition[7][2] == 0:
				cube.turnInv(0)
				cube.turnInv(3)
				cube.turn(0)
				mouvement += "U'R'U"
			listePosition = positionAll(listePosition, cube)

		#Cas de la face rouge
		if listePosition[7][0] == 2:
			if listePosition[7][1] == 0:
				cube.turn(2)
				cube.turnInv(0)
				cube.turn(3)
				cube.turn(0)
				mouvement += "FU'RU"
			if listePosition[7][1] == 2:
				cube.turn(5)
				cube.turn(3)
				cube.turnInv(2)
				cube.turnInv(3)
				mouvement += "DRF'R'"
			if listePosition[7][1] == 1 and listePosition[7][2] == 2:
				cube.turnInv(0)
				cube.turn(3)
				cube.turn(0)
				mouvement += "U'RU"
			if listePosition[7][1] == 1 and listePosition[7][2] == 0:
				cube.turn(0)
				cube.turnInv(1)
				cube.turnInv(0)
				mouvement += "UL'U'"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face verte
		if listePosition[7][0] == 1:
			if listePosition[7][1] == 0:
				cube.turn(1)
				cube.turn(2)
				mouvement += "LF"
			if listePosition[7][1] == 2:
				cube.turnInv(1)
				cube.turn(2)
				cube.turn(1)
				mouvement += "L'FL"
			if listePosition[7][1] == 1 and listePosition[7][2] == 2:
				cube.turn(2)
				mouvement += "F"
			if listePosition[7][1] == 1 and listePosition[7][2] == 0:
				cube.turn(0)
				cube.turn(1)
				cube.turn(1)
				cube.turnInv(0)
				cube.turn(2)
				mouvement += "ULLU'F"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face bleue
		if listePosition[7][0] == 3:
			if listePosition[7][1] == 0:
				cube.turnInv(3)
				cube.turnInv(2)
				mouvement += "R'F'"
			if listePosition[7][1] == 1 and listePosition[7][2] == 0:
				cube.turnInv(2)
				mouvement += "F'"
			if listePosition[7][1] == 1 and listePosition[7][2] == 2:
				cube.turnInv(3)
				cube.turnInv(3)
				cube.turnInv(2)
				cube.turnInv(3)
				cube.turnInv(3)
				mouvement += "R'R'F'R'R'"
			if listePosition[7][1] == 2:
				cube.turn(3)
				cube.turnInv(2)
				cube.turnInv(3)
				mouvement += "RF'R'"
			listePosition = positionAll(listePosition, cube)

		# Cas de la face jaune
		if listePosition[7][0] == 5:
			if listePosition[7][1] == 2:
				cube.turn(5)
				cube.turn(5)
				cube.turn(2)
				cube.turn(2)
				mouvement += "DDFF"
			if listePosition[7][1] == 1 and listePosition[7][2] == 2:
				cube.turnInv(5)
				cube.turn(2)
				cube.turn(2)
				mouvement += "D'FF"
			if listePosition[7][1] == 1 and listePosition[7][2] == 0:
				cube.turn(5)
				cube.turn(2)
				cube.turn(2)
				mouvement += "DFF"
			if listePosition[7][1] == 0:
				cube.turn(2)
				cube.turn(2)
				mouvement += "FF"
			listePosition = positionAll(listePosition, cube)

		# Cas d'une face blanche ne correspond pas aux autres faces
		if(croixBlancheDone(cube) == False and listePosition[2][0] == 0 and listePosition[4][0] == 0 and listePosition[5][0] == 0 and listePosition[7][0]):
			if(listePosition[2][1] != 0):
				cube.turn(4)
				mouvement += "B"
			if(listePosition[4][1] != 1 and listePosition[4][2] != 0):
				cube.turn(1)
				mouvement += "L"
			if(listePosition[5][1] != 1 and listePosition[5][2] != 2):
				cube.turn(3)
				mouvement += "R"
			if(listePosition[7][1] != 2):
				cube.turn(2)
				mouvement += "F"
            listePosition = positionAll(listePosition, cube)
        
	return mouvement

def position(facette, listePosition, cube):
	for i in range(0,6):
			for j in range(0,3):
				for k in range(0,3):
					if cube.lCube[i][j][k] == facette:
						print("Facette numéro : "+str(facette)+" position "+str(i), str(j), str(k))
						listePosition[facette] = [i,j,k]
	return listePosition

def positionAll(listePosition):
	listePosition = position(2, listePosition, cube)
	listePosition = position(4, listePosition, cube)
	listePosition = position(5, listePosition, cube)
	listePosition = position(7, listePosition, cube)
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
	print(croixBlanche(cube))
	drawCube(cube.cube_to_color54())