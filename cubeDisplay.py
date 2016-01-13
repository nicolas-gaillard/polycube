from tkinter import *

def decoupeCouleurs(chaine):

	""" Découpe une chaine de 54 caractères en un tableau de 6 * 9 caractères """

	tab = []

	# première et dernière face
	premiereFace = chaine[:9]
	derniereFace = chaine[-9:]
	chaine = chaine[9:-9]
	tab.append(premiereFace) 

	# découpage des autres faces, les 3 premiers de chaque ligne vont ensemble, etc
	ligne1 = chaine[:12]
	ligne2 = chaine[12:24]
	ligne3 = chaine[24:36]

	# regroupement des lignes en faces
	for i in range(4):
		top = ligne1[i*3:(i*3)+3]
		mid = ligne2[i*3:(i*3)+3]
		bot = ligne3[i*3:(i*3)+3]
		tab.append(top+mid+bot)
	# end for

	# ajout de la dernière face
	tab.append(derniereFace) 
	
	# retour du tableau 
	return tab

# end function


def drawSquare(canvas,topX,topY,width,height,color):

	""" Dessine un carré d'une certaine couleur """

	# correspondance des caractères d'entrée et des couleurs
	if color == 'O': fullColor = 'orange'
	elif color == 'B': fullColor = 'blue'
	elif color == 'G': fullColor = 'green'
	elif color == 'R': fullColor = 'red'
	elif color == 'W': fullColor = 'white'
	elif color == 'Y': fullColor = 'yellow'
	else: fullColor = 'black'

	# création du carré
	canvas.create_rectangle(topX, topY, topX + width, topY + height, fill=fullColor)

# end function



def drawFace(canvas,topX,topY,width,height,colors):

	""" Dessine un une face composée de 9 carrées colorés """

	for x in range(3):
		for y in range(3):
			drawSquare(canvas,(topX + x*(width/3)), (topY + y*(height/3)), width/3,height/3,colors[(3*y)+x])
		# end for
	# end for
# end function



def drawCube(chaine):

	""" Dessine le patron du rukik's cube à partir d'une chaîne de couleur """

	if type(chaine) != str or len(chaine) != 54:
		print("Chaîne incorrecte !")
		return

	# création de la fenêtre tkinter
	fenetre = Tk()
	canvas = Canvas(fenetre,width=1000,height=500,background='white')
	fenetre.bind('<Return>', lambda e: fenetre.destroy())

	# taille et position du patron du cube
	topX = 100
	topY = 100
	width = 99
	height = 99

	tab = decoupeCouleurs(chaine)

	# dessin de la face supérieure
	drawFace(canvas,topX+width,topY,width,height,tab[0])

	# dessin des faces du milieu
	for i in range(4):
		drawFace(canvas,topX+width*i,topY+height,width,height,tab[i+1])
	# end for

	# dessin de la face inférieure
	drawFace(canvas,topX+width,topY+2*height,width,height,tab[5])

	# affichage de la fenêtre tkinter
	canvas.pack()
	fenetre.mainloop()
# end function


# test
#chaine = "OGRBWYBGBGYYOYOWOWGRYOOOBGBRRYRBWWWRBWYGROWGRYBRGYWBOG"
#drawCube(chaine)
