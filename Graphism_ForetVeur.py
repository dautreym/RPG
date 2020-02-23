import pygame
from pygame.locals import *

# CHOIX PERSONNEL DU PROGRAMMEUR :

# Il est considéré comme plus plaisant de jouer avec le clavier, dont les flèches, qu'avec la souris
# Ainsi pour la suite, tout sera programmé par rapport au clavier 


# POUR CORRIGER LES WARNINGS DUS AU FORMAT DES PNG :
# Dans le dossier où se trouve le png e nquestion, faire la commande :
# find . -type f -name "*.png" -exec convert {} -strip {} \;

# INSTRUCTIONS UTILES :
# police = pygame.font.SysFont("arial", 16)
# argent_txt = police.render((str(argent)+" $"), 1, (255,255,0))
# création d'une variable texte pour le coller à l'écran 
# (str car ça doit etre du texte)
# fenetre.blit(argent_txt, (530, 50)) 
# on colle le texte sur la fenêtre 
# pygame.time.wait(1000)


def initialisation_fenetre(dimensions_fenetre):
	pygame.init()

	# Ouverture de la fenêtre Pygame
	fenetre = pygame.display.set_mode((dimensions_fenetre[0], dimensions_fenetre[1]))

	return fenetre


def initialisation_background(fenetre):

	# Définition de l'image de fond et du sol, chargement et collage de celles-ci
	# Pour l'instant pas de sol (plus classe sans)
	# ground = pygame.image.load("Graphism/Battle_background_2_down/ground_2_06.png").convert_alpha()
	# Dimensions : Largeur : 617 ; Hauteur : 479
	#fenetre.blit(ground, (0,400))
	fond = pygame.image.load("Graphism/Battle_background_1/sprite_16.png").convert_alpha()
	# Dimensions : Largeur : 617 ; Hauteur : 480
	fenetre.blit(fond, (0,0))
	# Rafraîchissement de l'écran
	pygame.display.flip()

	return fond


#position_cerbere = cerbere.get_rect()
#position_cerbere2 = cerbere2.get_rect()
#position_cerbere3 = cerbere3.get_rect()

# Chargement et collage du personnage
# (_alpha pour garder la zone transparente autour du personnage telle quelle)
def initialisation_monstres(fenetre,dimensions_fenetre,equipe_ennemis,nom_niveau,region):
	images_persos=[]
	positions_persos=[]
	for index in range(equipe_ennemis.len):
		if(nom_niveau == 'la Forêt Veur Niveau 1 - Entrée '):
			perso_tmp = pygame.image.load("Graphism/Monstres_RPG_Maker/Orc.png").convert_alpha()
			images_persos.append(perso_tmp)

			position_x_perso_tmp = (1+index)*dimensions_fenetre[1] /3
			position_y_perso_tmp = 200
			positions_persos.append([position_x_perso_tmp,position_y_perso_tmp])

			fenetre.blit(perso_tmp, [position_x_perso_tmp,position_y_perso_tmp])
			# Rafraîchissement de l'écran
			pygame.display.flip()

	return [images_persos,positions_persos]


def initialisation_choice(fenetre,position_choice):
	choice = pygame.image.load("Graphism/arrow_reduced.png").convert_alpha()
	fenetre.blit(choice, position_choice)
	# Rafraîchissement de l'écran
	pygame.display.flip()


def initialisation_fight(fenetre,position_choice,equipe_ennemis,nom_niveau,police):
	initialisation_choice(fenetre,position_choice)
	# Affichage du texte au dessus de l'image :
	message = police.render("Quel monstre voulez-vous attaquer ? ", 1, (255,0,0))
	fenetre.blit(message, (30, 50)) 
	# Rafraîchissement de l'écran
	pygame.display.flip()

	# Pour effectuer plusieurs fois une action en laissant une touche appuyée :
	pygame.key.set_repeat(400, 30)
	# 400 est le temps en millisecondes avant d'effectuer un nouveau déplacement
	# 30 est le temps en millisecondes entre deux déplacements


def graphism(equipe_ennemis,nom_niveau):
	dimensions_fenetre = [617,480]
	fenetre = initialisation_fenetre(dimensions_fenetre)
	fond = initialisation_background(fenetre)
	personnages = initialisation_monstres(fenetre,dimensions_fenetre,equipe_ennemis,nom_niveau,1)
	police = pygame.font.SysFont("arial", 16)
	position_choice = [dimensions_fenetre[1] /3, 130]
	initialisation_fight(fenetre,position_choice,equipe_ennemis,nom_niveau,police)
	index_targeted_personnage = 0

	continuer = 1
	while continuer:
		# On parcourt la liste de tous les événements reçus
		for event in pygame.event.get():
			# Si un de ces événements est de type QUIT
			# QUIT est une constante définie et importée dans pygame.locals
			if event.type == QUIT:
				# On arrête la boucle
				continuer = 0
			# Liste complète des possibilités à la place de QUIT :
			# https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1
		
			if event.type == KEYDOWN:
				# Si l'utilisateur appuie sur la flèche du bas
				if event.key == K_RIGHT:
					# On déplace la flèche de choix selon le choix de l'utilisateur
					if (position_choice[0] == dimensions_fenetre[1] /3):
						position_choice[0] = 2*dimensions_fenetre[1] /3
						index_targeted_personnage = 1
					else:
						position_choice[0] = dimensions_fenetre[1] /3
						index_targeted_personnage = 0

				if event.key == K_LEFT:
                    # On déplace la flèche de choix selon le choix de l'utilisateur
					if (position_choice[0] == dimensions_fenetre[1] /3):
						position_choice[0] = 2*dimensions_fenetre[1] /3
						index_targeted_personnage = 1
					else:
						position_choice[0] = dimensions_fenetre[1] /3
						index_targeted_personnage = 0 


				# Actualisation de la position de la flèche de choix
				fenetre = initialisation_fenetre(dimensions_fenetre)
				fond = initialisation_background(fenetre)
				personnages = initialisation_monstres(fenetre,dimensions_fenetre,equipe_ennemis,nom_niveau,1)
				initialisation_fight(fenetre,position_choice,equipe_ennemis,nom_niveau,police)

				# Rafraichissement de l'écran
				pygame.display.flip()



from Monsters import Sanglier

class Equipe:
    def __init__(self,liste_de_monstres,taille):
        self.membres=liste_de_monstres
        self.len=taille 

monstre1=Sanglier()
while(monstre1.attribut!='Vent'):
    monstre1=Sanglier()
monstre1.surnom='Sanglier vert'

monstre2=Sanglier()
while(monstre2.attribut!='Feu'):
    monstre2=Sanglier()
monstre2.surnom='Sanglier rouge'

equipe_ennemis = Equipe([monstre1,monstre2],2)
graphism(equipe_ennemis,'la Forêt Veur Niveau 1 - Entrée ')

print("\n\n IT WORKS !!!! \n\n")









































''' Intéressant :

		# MOUSEBUTTONDOWN pour le click, UP pour le relâchement
		# event.button peut prendre les valeurs suivantes :
			# 1 : bouton gauche ; 2 : bouton du milieu OU boutons de gauche et de droite ; 3 : bouton de droite
			# 4 : molette vers le haut ; 5 : molette vers le bas
		# event.pos renvoie un tuple (abscisse, ordonnée) à partir de l'angle haut-gauche
		#if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
		#	print("Zone dangereuse")

		if event.type == MOUSEBUTTONDOWN:
			# Si l'utilisateur effectue un click gauche
			if event.button == 1:
				# On change les coordonnées du personnage par celles données par le click
				position_x_cerbere = event.pos[0]
				position_y_cerbere = event.pos[1]

''' 