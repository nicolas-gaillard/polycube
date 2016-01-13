Membres de l'équipe
===================

- BOUCHEVREAU Valentin
- BRIAND Kévin
- DORMEVAL Alexandre
- GAILLARD Nicolas
- PETILLON Pierre
- PIGEON Hugo


Objectif du projet
==================

Résoudre un rubik's cube avec un algorithme.

L'algorithme prend en entrée une chaine de 54 caractères, décrivant le cube et ses couleurs, et retourne la liste des mouvements à effectuer pour le résoudre.

Nous avons appliqué l'algorithme manuel (en trois couches successives), en prenant toujours le cube de façon à avoir la face rouge devant et la face blanche au dessus.
Les mouvements donnés en résultat prennent en compte cette configuration, on ne tourne donc jamais le cube.

Les correspondances des mouvements :
- U : Rotation de la face du haut dans le sens horaire
- L : Rotation de la face de gauche dans le sens horaire
- F : Rotation de la face de devant dans le sens horaire
- R : Rotation de la face de droite dans le sens horaire
- B : Rotation de la face de derrière dans le sens horaire
- D : Rotation de la face du bas dans le sens horaire

Un 2 derrière une lettre signifie que l'on fait le mouvement deux fois, une apostrophe signifie qu'on le fait dans le sens antihoraire.