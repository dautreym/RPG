import pygame
from pygame.locals import *

# CHOIX PERSONNEL DU PROGRAMMEUR :

# Il est considéré comme plus plaisant de jouer avec le clavier, dont les flèches, qu'avec la souris
# Ainsi pour la suite, tout sera programmé par rapport au clavier 

# La fenêtre aura par défaut les paramètres constants suivants :
# Largeur : 617 pixels = dimensions_fenetre[0]
# Hauteur : 480 pixels = dimensions_fenetre[1]



# CONVENTION POUR UNE VARIABLE D'OPTION :
	# Option à l'indice 0 :
		# 0 : affichage d'un message à gauche
		# 1 : affichage d'une image à gauche 

		# 616 : affichage d'un message à droite
		# 617 : affichage d'une image à droite

	# Option à l'indice 1 :
		# L'image en question, n'existe que si Option à l'indice 0 vaut 1 ou 617

	# Option à l'indice 2 :
		# L'image en question, n'existe que si Option à l'indice 0 vaut 1 ou 617
		# Position de l'image par rapport à un choix, ex. right_arrow 




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


# Pour effectuer plusieurs fois une action en laissant une touche appuyée :
# pygame.key.set_repeat(400, 30)
# 400 est le temps en millisecondes avant d'effectuer un nouveau déplacement
# 30 est le temps en millisecondes entre deux déplacements




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
	background = pygame.image.load("Graphism/Battle_background_1/sprite_16.png").convert_alpha()
	# Dimensions : Largeur : 617 ; Hauteur : 480
	fenetre.blit(background, (0,0))
	# Rafraîchissement de l'écran
	pygame.display.flip()

	return background


def trouver_image_monstre(nom_monstre,nom_niveau_donjon):
	if('Forêt Veur' in nom_niveau_donjon):
		nom_donjon='ForetVeur'
	nom_image = "Graphism/Monstres_RPG_Maker/" + nom_donjon + "/" + nom_monstre + ".png"
	image = pygame.image.load(nom_image).convert_alpha()
	return image


# ATTENTION
# Suite à la fusion des deux fenêtres en une seule, il faut diviser par deux dimensions_fenetre[0]

def initialisation_monstres(fenetre,dimensions_fenetre,equipe_ennemis,region):
	police = pygame.font.SysFont("impact", 23)
	
	message = "***** Recapitulatif *****"
	message = police.render(message, 1, (0,0,0))
	fenetre.blit(message,(100,50))

	images_persos=[]
	positions_persos=[]
	for index in range(equipe_ennemis.len):
		if('Forêt Veur' in equipe_ennemis.nom_niveau_donjon):
		# if(equipe_ennemis.nom_niveau_donjon == 'la Forêt Veur Niveau 1 - Entrée '):
			if(equipe_ennemis.membres[index].pv_actuels > 0):
				perso_tmp = trouver_image_monstre(equipe_ennemis.membres[index].nom, equipe_ennemis.nom_niveau_donjon)
				# pygame.image.load("Graphism/Monstres_RPG_Maker/Orc.png").convert_alpha()
				images_persos.append(perso_tmp)

				position_x_perso_tmp = ((1+index)*dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
				position_y_perso_tmp = 200

				if(equipe_ennemis.membres[index].nom == 'Gardien de la Forêt'):
					# Largeur : 360 pixels ; Hauteur : 276 pixels 
					position_y_perso_tmp = 100
					position_x_perso_tmp = (360+160)*index / equipe_ennemis.len
				if(equipe_ennemis.membres[index].nom == 'Plante Carnivore'):
					position_x_perso_tmp = 100 + (190 + 360)*index / equipe_ennemis.len

				positions_persos.append([position_x_perso_tmp,position_y_perso_tmp])
				fenetre.blit(perso_tmp, [position_x_perso_tmp,position_y_perso_tmp])

				message = equipe_ennemis.membres[index].surnom + " " + equipe_ennemis.membres[index].attribut + " : " + str(equipe_ennemis.membres[index].pv_actuels) + " PV"
				#  sur " + str(equipe_ennemis.membres[index].pv_max_donjons)
				message_2 = "Jauge d'attaque : " + str(equipe_ennemis.membres[index].jauge_attaque)
				
				message = police.render(message, 1, (255,255,255))
				message_2 = police.render(message_2, 1, (255,255,255))

				# FORMULE A RECALCULER POUR UN MEILLEUR AFFICHAGE 
				position_y_message = position_y_perso_tmp + 200 - 15*(index%2)
				if(equipe_ennemis.membres[index].nom == 'Gardien de la Forêt'):
					position_y_message = position_y_perso_tmp + 300 - 15*(index%2)

				fenetre.blit(message,(position_x_perso_tmp,position_y_message))
				fenetre.blit(message_2,(position_x_perso_tmp,position_y_message + 50))
	
	

	# Rafraîchissement de l'écran
	pygame.display.flip()

	return [images_persos,positions_persos]


def initialisation_choice(fenetre,position_choice,police):
	choice = pygame.image.load("Graphism/arrow_reduced.png").convert_alpha()
	fenetre.blit(choice, position_choice)

	message = police.render("Quel monstre voulez-vous attaquer ? ", 1, (255,0,0))
	fenetre.blit(message, (30, 50)) 

	# Rafraîchissement de l'écran
	pygame.display.flip()




def initialisation_print(fenetre,police,liste_de_messages,option):
	# VOIR LA CONVENTION EN HAUT DU FICHIER 

	# ré-ajustement de la variable dans le cas où l'image est positionnée pour faire un choix
	if((option[0] == 1 or option[0] == 617) and option[2] == 0):
		option[2] += 1

	for index in range(len(liste_de_messages)):
		# ne s'applique qu'une fois grâce à la deuxième condition 
		if (option[0] == 1 and index == option[2]):
			fenetre.blit(option[1],(65, 38 + 45*index))
		elif (option[0] == 617 and index == option[2]):
			fenetre.blit(option[1],(617, 38 + 30*index))
		# 617 correspond à la moitié de la fenêtre totale après fusion sur l'axe des abscisses
		
		# ici le 20*index signifie qu'il y a 20 pixels entre chaque ligne !!!
		message_a_afficher = police.render(liste_de_messages[index], 1, (255,0,0))
		if(option[0] == 0):
			fenetre.blit(message_a_afficher, (85, 50 + 30*index))
		elif(option[0] == 616):
			fenetre.blit(message_a_afficher, (617 + 85, 50 + 30*index)) 
		elif(option[0] == 618):
			fenetre.blit(message_a_afficher, (617 + 85, 15 + 30*index)) 
		
	# Rafraîchissement de l'écran
	pygame.display.flip()




# print('C\'est au tour de ... ') est réalisé par l'appel graphism(equipe_ennemis,[0,'C\'est ...'])
def graphism(fenetre,dimensions_fenetre,equipe_ennemis,indication):
	fond = initialisation_background(fenetre)
	monstres = initialisation_monstres(fenetre,dimensions_fenetre,equipe_ennemis,1)
	police = pygame.font.SysFont("arial", 16)
	
	index_targeted_personnage = 0
	right_arrow = pygame.image.load("Graphism/right_arrow.gif").convert_alpha()

	# Code pour indication : liste de deux éléments (un pour le type d'action, l'autre pour le contenu)
	# Si indication[0] = 0 : afficher à gauche une liste de messages contenue dans indication[1]
	# Si indication[0] = 616 : afficher à droite une liste de messages contenue dans indication[1]

	# Si indication[0] = 1 : faire choisir une cible (indication[1] n'est pas évalué)
		# Cohérent car le choix d'une cible se fait à gauche !!

	if(indication[0] == 0):
		# Affichage d'un simple message sur la gauche 
		initialisation_print(fenetre, police, indication[1],[0])

	elif(indication[0] == 616 or indication[0] == 618):
		# Affichage d'un simple message sur la droite
		initialisation_print(fenetre, police, indication[1], [indication[0]])

	# NE SERT QUE DANS LE CAS Où APPELé DEPUIS GRAPHISM_SIMPLE !!!!
	# elif(indication[0] == 617):
	# 	...

	elif(indication[0] == 1):
		position_choice = [(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2, 130]
		index = 0
		while(index < equipe_ennemis.len and equipe_ennemis.membres[index].pv_actuels <= 0):
			# Pour chaque ennemi mort, on décale la flèche vers la droite
			position_choice[0] += (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
			index += 1
		
		initialisation_choice(fenetre,position_choice,police)

		continuer = 1
		valider = 1
		while (continuer == 1 or valider == 1):
			# On parcourt la liste de tous les événements reçus
			for event in pygame.event.get():
				# Liste complète des possibilités à la place de K_RIGHT, LEFT, UP, DOWN :
				# https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1
		
				if event.type == KEYDOWN:
					index = 0
					nb_ennemis_vivants = 0
					while(index < equipe_ennemis.len):
						if(equipe_ennemis.membres[index].pv_actuels > 0):
							nb_ennemis_vivants += 1
						else:
							index_targeted_personnage += 1
						index += 1

					if(equipe_ennemis.len == 3):
					# Si l'utilisateur appuie sur la flèche de droite
						if (nb_ennemis_vivants == 3 and event.key == K_RIGHT):
							# On déplace la flèche de choix selon le choix de l'utilisateur
							position_choice[0] += (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
							if (position_choice[0] == (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2):
								index_targeted_personnage = 0
							elif (position_choice[0] == 2*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2 and equipe_ennemis.len > 1):
								index_targeted_personnage = 1
							elif (position_choice[0] == 3*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2 and equipe_ennemis.len > 1):
								index_targeted_personnage = 2
							else:
								position_choice[0] = (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
								index_targeted_personnage = 0

						elif(nb_ennemis_vivants == 3 and event.key == K_LEFT):
							# On déplace la flèche de choix selon le choix de l'utilisateur
							position_choice[0] -= (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
							if (position_choice[0] == (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2):
								index_targeted_personnage = 0
							elif (position_choice[0] == 2*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2 and equipe_ennemis.len > 1):
								index_targeted_personnage = 1
							elif (position_choice[0] == 3*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2 and equipe_ennemis.len > 1):
								index_targeted_personnage = 2
							else:
								position_choice[0] = 3*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
								index_targeted_personnage = 2
						

						elif(nb_ennemis_vivants == 2 and (event.key == K_LEFT or event.key == K_RIGHT)):
							index_dead_monster = 0
							while(index_dead_monster < equipe_ennemis.len and equipe_ennemis.membres[index_dead_monster].pv_actuels > 0):
								index_dead_monster += 1

							if(index_dead_monster == 2):
								if (position_choice[0] == (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2):
									position_choice[0] = 2*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
									index_targeted_personnage = 1
								elif(position_choice[0] == 2*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2):
									position_choice[0] = (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
									index_targeted_personnage = 0
								else:
									position_choice[0] = (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
									index_targeted_personnage = 0
							
							elif(index_dead_monster == 1):
								if(position_choice[0] == (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2):
									position_choice[0] = 3*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
									index_targeted_personnage = 2
								elif(position_choice[0] == 3*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2):
									position_choice[0] = (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
									index_targeted_personnage = 0
								else:
									position_choice[0] = (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
									index_targeted_personnage = 0

							elif(index_dead_monster == 0):
								if(position_choice[0] == 2*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2):
									position_choice[0] = 3*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
									index_targeted_personnage = 2
								elif(position_choice[0] == 3*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2):
									position_choice[0] = 2*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
									index_targeted_personnage = 1
								else:
									position_choice[0] = 2*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
									index_targeted_personnage = 1


						elif(nb_ennemis_vivants == 1 and (event.key == K_RIGHT or event.key == K_LEFT)):
							index_alive_monster = 0
							while(index_alive_monster < equipe_ennemis.len and equipe_ennemis.membres[index_alive_monster].pv_actuels <= 0):
								index_alive_monster += 1
							position_choice[0] = (index_alive_monster + 1)*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
							index_targeted_personnage = index_alive_monster
					
					elif(equipe_ennemis.len == 2):
						if(nb_ennemis_vivants == 2 and (event.key == K_LEFT or event.key == K_RIGHT)):
							if(position_choice[0] == (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2):
								position_choice[0] = 2*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
								index_targeted_personnage = 1
							elif(position_choice[0] == 2*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2):
								position_choice[0] = (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
								index_targeted_personnage = 0
							else:
								position_choice[0] = (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
								index_targeted_personnage = 0

						elif(nb_ennemis_vivants == 1 and (event.key == K_RIGHT or event.key == K_LEFT)):
							index_alive_monster = 0
							if(equipe_ennemis.membres[index_alive_monster].pv_actuels <= 0):
								index_alive_monster = 1
							position_choice[0] = (1 + index_alive_monster)*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
							index_targeted_personnage = index_alive_monster
					
					elif(equipe_ennemis.len == 1):
						position_choice[0] = (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
						index_targeted_personnage = 0

					# rechargement de la fenêtre
					# indication[1] : le choix retenu,  indication[2] : la liste des messages
					graphism_simple(fenetre,dimensions_fenetre,equipe_ennemis,[616,indication[2]])
					initialisation_print(fenetre, police, indication[2], [617,right_arrow,indication[1]])

			

					if event.key == K_RETURN:
						continuer = 0

				if event.type == KEYUP:
					if event.key == K_RETURN:
						valider = 0


					# Actualisation de la position de la flèche de choix
					fenetre = initialisation_fenetre(dimensions_fenetre)
					fond = initialisation_background(fenetre)
					monstres = initialisation_monstres(fenetre,dimensions_fenetre,equipe_ennemis,1)
					initialisation_choice(fenetre,position_choice,police)
					
					# indication[1] : le choix retenu,  indication[2] : la liste des messages
					graphism_simple(fenetre,dimensions_fenetre,equipe_ennemis,[616,indication[2]])
					initialisation_print(fenetre, police, indication[2], [617,right_arrow,indication[1]])

					# Rafraichissement de l'écran
					pygame.display.flip()

		# Quand le joueur a validé son choix et que ce derneir est correct 
		return index_targeted_personnage




# Simple dans le sens où il ne prend qu'un paramètre et pas d'équipe en paramètre...
def graphism_simple(fenetre,dimensions_fenetre,equipe_ennemis,indication):
	police = pygame.font.SysFont("arial", 16)

	# Choix astucieux : 0 est le premier indice possible
	# donc la flèche de choix sera positionnée en face du premeir choix 
	# ET 0 n'est dans aucune liste de possibilites_capacite_speciale :)
	choix_capacite = 0
	choix_capacite_tmp = 1
	continuer = 1


	# Code pour indication : liste de deux éléments (un pour le type d'action, l'autre pour le contenu)
	# Si indication[0] = 0 : afficher à gauche une liste de messages contenue dans indication[1]
	# Si indication[0] = 616 : afficher à droite une liste de messages contenue dans indication[1]

	# Si indication[0] = 617 : afficher une image à droite 
		# Ici, on affiche right_arrow à droite comme image, en face de choix_capacite
		# On affiche en même temps indication[1] (car indication[0] à 1 permet AUSSI d'afficher des messages)

	# Si indication[0] = 617, on récupère la variable possibilites_capacite_speciale 
	# dans indication[2] qui existera alors TOUJOURS si indication[0] = 617 
	
	right_arrow = pygame.image.load("Graphism/right_arrow.gif").convert_alpha()

	if(indication[0] == 617):
		initialisation_print(fenetre, police, indication[1], [617,right_arrow,choix_capacite])

		possibilites_capacite_speciale=indication[2]
		# noms_capacites_speciales=indication[3]

		while(choix_capacite not in possibilites_capacite_speciale or continuer == 1):
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_DOWN:
						choix_capacite_tmp += 1
						if(choix_capacite_tmp > possibilites_capacite_speciale[len(possibilites_capacite_speciale)-1]):
							choix_capacite_tmp -= possibilites_capacite_speciale[len(possibilites_capacite_speciale)-1]
						
						dimensions_fenetre = [2*617,480]
						fenetre = initialisation_fenetre(dimensions_fenetre)
						graphism(fenetre,dimensions_fenetre,equipe_ennemis,indication)
						graphism_simple(fenetre,dimensions_fenetre,equipe_ennemis,[616,indication[1]])
						initialisation_print(fenetre, police, indication[1], [617,right_arrow,choix_capacite_tmp])
					
					if event.key == K_UP:
						choix_capacite_tmp -= 1
						if(choix_capacite_tmp == 0):
							choix_capacite_tmp = possibilites_capacite_speciale[len(possibilites_capacite_speciale)-1]
						
						dimensions_fenetre = [2*617,480]
						fenetre = initialisation_fenetre(dimensions_fenetre)
						graphism(fenetre,dimensions_fenetre,equipe_ennemis,indication)
						graphism_simple(fenetre,dimensions_fenetre,equipe_ennemis,[616,indication[1]])
						initialisation_print(fenetre, police, indication[1], [617,right_arrow,choix_capacite_tmp])

					if (event.key == K_RETURN or event.key == K_KP_ENTER):
						choix_capacite = choix_capacite_tmp
						if(choix_capacite not in possibilites_capacite_speciale):
							print('\n Dommage!! Essaye encore!! \n (Capacité ', choix_capacite, ' donnée n\'appartient pas à la liste des possibilités ', possibilites_capacite_speciale,')\n')

					
				if event.type == KEYUP:
					if (event.key == K_RETURN or event.key == K_KP_ENTER):
						continuer = 0
					
	elif(indication[0] == 0):
		initialisation_print(fenetre, police, indication[1], [0])

	elif(indication[0] == 616):
		initialisation_print(fenetre, police, indication[1], [616])

	return choix_capacite


































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