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



def initialisation_background(fenetre,nom_niveau_donjon):
	# Définition de l'image de fond et du sol, chargement et collage de celles-ci
	# Pour l'instant pas de sol (plus classe sans)
	# ground = pygame.image.load("Graphism/Battle_background_2_down/ground_2_06.png").convert_alpha()
	# Dimensions : Largeur : 617 ; Hauteur : 479
	#fenetre.blit(ground, (0,400))

	if('Forêt Veur' in nom_niveau_donjon):
		if('Niveau 1' in nom_niveau_donjon or 'Niveau 7' in nom_niveau_donjon):
			background = pygame.image.load("Graphism/Battle_background_1/sprite_16.png").convert_alpha()
			ground = pygame.image.load("Graphism/Battle_background_2_down/ground_2_13.png")
		elif('Niveau 2' in nom_niveau_donjon  or 'Niveau 3' in nom_niveau_donjon or 'Niveau 4' in nom_niveau_donjon or 'Niveau 5' in nom_niveau_donjon):
			background = pygame.image.load("Graphism/Battle_background_1/sprite_17.png").convert_alpha()
			ground = pygame.image.load("Graphism/Battle_background_2_down/ground_2_06.png")
		elif('Niveau 6' in nom_niveau_donjon):
			background = pygame.image.load("Graphism/Battle_background_2/background_01.png").convert_alpha()
			ground = pygame.image.load("Graphism/Battle_background_2_down/ground_2_06.png")

	elif('Cratère Ater' in nom_niveau_donjon):
		if('Niveau 1' in nom_niveau_donjon or 'Niveau 2' in nom_niveau_donjon or 'Niveau 3' in nom_niveau_donjon):
			background = pygame.image.load("Graphism/Battle_background_2/background_07.png").convert_alpha()
			ground = pygame.image.load("Graphism/Battle_background_2_down/ground_2_00.png")
		elif('Niveau 6' in nom_niveau_donjon):
			background = pygame.image.load("Graphism/Battle_background_4/background_4_13.png").convert_alpha()
			ground = background
			# ground = pygame.image.load("Graphism/Battle_background_1_down/ground_1_08.png")
		elif('Niveau 4' in nom_niveau_donjon or 'Niveau 5' in nom_niveau_donjon or 'Niveau 7' in nom_niveau_donjon):
			background = pygame.image.load("Graphism/Battle_background_2/background_10.png").convert_alpha()
			ground = pygame.image.load("Graphism/Battle_background_3_down/ground_3_03.png")

	elif('Mont Tagne' in nom_niveau_donjon):
		if('Niveau 1' in nom_niveau_donjon or 'Niveau 4' in nom_niveau_donjon or 'Niveau 5' in nom_niveau_donjon or 'Niveau 6' in nom_niveau_donjon):
			background = pygame.image.load("Graphism/Battle_background_2/background_05.png").convert_alpha()
			ground = pygame.image.load("Graphism/Battle_background_2_down/ground_2_11.png").convert_alpha()
		elif('Niveau 2' in nom_niveau_donjon or 'Niveau 3' in nom_niveau_donjon or 'Niveau 7' in nom_niveau_donjon):
			background = pygame.image.load("Graphism/Battle_background_1/sprite_05.png").convert_alpha()
			ground = pygame.image.load("Graphism/Battle_background_2_down/ground_2_10.png")

	elif('Ruines de Senzargen' in nom_niveau_donjon):
		# Pour les Autels Sacrificiels : Graphism/Battle_background_general_2/general_background_2_8.png
		if('Niveau 1' in nom_niveau_donjon or 'Niveau 4' in nom_niveau_donjon or 'Niveau 5' in nom_niveau_donjon or 'Niveau 7' in nom_niveau_donjon):
			background = pygame.image.load("Graphism/Battle_background_general_2/general_background_2_8.png").convert_alpha()
			ground = pygame.image.load("Graphism/Battle_background_3_down/ground_3_16.png")
		elif('Niveau 2' in nom_niveau_donjon or 'Niveau 3' in nom_niveau_donjon or 'Niveau 6' in nom_niveau_donjon):
			background = pygame.image.load("Graphism/Battle_background_general_2/general_background_2_7.png").convert_alpha()
			ground = pygame.image.load("Graphism/Battle_background_3_down/ground_3_03.png")

	# Dimensions : Largeur : 617 ; Hauteur : 480
	fenetre.blit(ground, (0,140))
	fenetre.blit(background, (0,0))
	# Rafraîchissement de l'écran
	pygame.display.flip()

	return background


def trouver_image_monstre(nom_monstre,nom_niveau_donjon):
	if('Forêt Veur' in nom_niveau_donjon):
		nom_donjon = 'ForetVeur'
	elif('Cratère Ater' in nom_niveau_donjon):
		nom_donjon = 'CratereAter'
	elif('Mont Tagne' in nom_niveau_donjon):
		nom_donjon = 'MontTagne'
	elif('Ruines de Senzargen' in nom_niveau_donjon):
		nom_donjon = 'RuinesSenzargen'
	
	if(nom_monstre == 'Gardien de la Forêt'):
		image = pygame.image.load("Graphism/Monstres_RPG_Maker/ForetVeur/Gardien.png").convert_alpha()
	elif(nom_monstre == 'Plante Carnivore'):
		image = pygame.image.load("Graphism/Monstres_RPG_Maker/ForetVeur/Plante.png").convert_alpha()
	elif(nom_monstre == 'Chauve Souris'):
		image = pygame.image.load("Graphism/Monstres_RPG_Maker/CratereAter/ChauveSouris.png").convert_alpha()
	elif(nom_monstre == 'Soldat Squelette'):
		image = pygame.image.load("Graphism/Monstres_RPG_Maker/CratereAter/Skeleton.png").convert_alpha()
	elif(nom_monstre == 'Dame Harpie'):
		image = pygame.image.load("Graphism/Monstres_RPG_Maker/RuinesSenzargen/DameHarpie.png").convert_alpha()
	elif(nom_monstre == 'Bas Elementaire'):
		image = pygame.image.load("Graphism/Monstres_RPG_Maker/RuinesSenzargen/BasElementaire.png").convert_alpha()
	elif(nom_monstre == 'Haut Elementaire'):
		image = pygame.image.load("Graphism/Monstres_RPG_Maker/RuinesSenzargen/HautElementaire.png").convert_alpha()
	elif(nom_monstre == 'Sylphe'):
		image = pygame.image.load("Graphism/Monstres_RPG_Maker/RuinesSenzargen/Arashi.png").convert_alpha()
	elif(nom_monstre == 'Sylphide'):
		image = pygame.image.load("Graphism/Monstres_RPG_Maker/RuinesSenzargen/Hayate.png").convert_alpha()

	else:
		nom_image = "Graphism/Monstres_RPG_Maker/" + nom_donjon + "/" + nom_monstre + ".png"
		image = pygame.image.load(nom_image).convert_alpha()
		#print("\n\n Nom de l'image : \n",nom_image,"\n\n")
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
	barres_de_vie=[0,0,0]
	barres_de_attaque=[0,0,0]
	
	for index in range(equipe_ennemis.len):
		if('Forêt Veur' in equipe_ennemis.nom_niveau_donjon):
			if(equipe_ennemis.membres[index] != 0 and equipe_ennemis.membres[index].pv_actuels > 0):
				perso_tmp = trouver_image_monstre(equipe_ennemis.membres[index].nom, equipe_ennemis.nom_niveau_donjon)
				# pygame.image.load("Graphism/Monstres_RPG_Maker/Orc.png").convert_alpha() par exemple 
				images_persos.append(perso_tmp)

				position_x_perso_tmp = ((1+index)*dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2 - 30
				position_y_perso_tmp = 200

				if(equipe_ennemis.membres[index].nom == 'Gardien de la Forêt'):
					# Largeur : 360 pixels ; Hauteur : 276 pixels 
					position_y_perso_tmp = 100
					position_x_perso_tmp = (360+160)*index / equipe_ennemis.len
				if(equipe_ennemis.membres[index].nom == 'Plante Carnivore'):
					position_x_perso_tmp = 100 + (190 + 360)*index / equipe_ennemis.len

				positions_persos.append([position_x_perso_tmp,position_y_perso_tmp])
				fenetre.blit(perso_tmp, [position_x_perso_tmp,position_y_perso_tmp])

				barres_de_vie[index] = pygame.image.load("Graphism/trop_des_barres/barre_vie.png").convert_alpha()
				barres_de_attaque[index] = pygame.image.load("Graphism/trop_des_barres/barre_attaque.png").convert_alpha()

				jauge_de_vie = pygame.image.load("Graphism/trop_des_barres/jauge_vie.png").convert_alpha()
				jauge_de_attaque = pygame.image.load("Graphism/trop_des_barres/jauge_attaque.png").convert_alpha()
				jauge_de_vie_actuelle = pygame.transform.scale(jauge_de_vie, (10,100))
				jauge_de_attaque_actuelle = pygame.transform.scale(jauge_de_attaque, (10,100))

				position_x_barre_de_vie = position_x_perso_tmp - 15
				position_y_barre_de_vie = position_y_perso_tmp - 100 - 15*(index%2)
				if(equipe_ennemis.membres[index].nom == 'Gardien de la Forêt'):
					position_x_barre_de_vie += 60
					position_y_barre_de_vie = position_y_perso_tmp - 100
					
				fenetre.blit(barres_de_vie[index], (position_x_barre_de_vie,position_y_barre_de_vie))
				fenetre.blit(barres_de_attaque[index], (position_x_barre_de_vie,position_y_barre_de_vie + 30))

				nb_affichages_vie = int(20*(equipe_ennemis.membres[index].pv_actuels / equipe_ennemis.membres[index].pv_max_donjons))
				# print("\n\n",equipe_ennemis.membres[index].pv_actuels," / ",equipe_ennemis.membres[index].pv_max_donjons," multiplié par 100 divisé par 5 = ",nb_affichages_vie,"\n\n")
				if(nb_affichages_vie == 0 and equipe_ennemis.membres[index].pv_actuels > 0):
					nb_affichages_vie = 1
				
				nb_affichages_attaque = equipe_ennemis.membres[index].jauge_attaque // 5
				
				for index in range(nb_affichages_vie):
					fenetre.blit(jauge_de_vie_actuelle, (position_x_barre_de_vie + 65 +5*index,position_y_barre_de_vie))
				for index in range(nb_affichages_attaque):
					fenetre.blit(jauge_de_attaque_actuelle, (position_x_barre_de_vie + 65 +5*index,position_y_barre_de_vie + 30))
	


		if('Cratère Ater' in equipe_ennemis.nom_niveau_donjon):
			if(equipe_ennemis.membres[index] != 0 and equipe_ennemis.membres[index].pv_actuels > 0):
				perso_tmp = trouver_image_monstre(equipe_ennemis.membres[index].nom, equipe_ennemis.nom_niveau_donjon)
				images_persos.append(perso_tmp)

				position_x_perso_tmp = ((1+index)*dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2 - 30
				position_y_perso_tmp = 200

				#if(equipe_ennemis.membres[index].nom == 'Chauve Souris'):
				#	position_x_perso_tmp = dimensions_fenetre[0]/4
				#	position_y_perso_tmp = dimensions_fenetre[1]/2

				positions_persos.append([position_x_perso_tmp,position_y_perso_tmp])
				fenetre.blit(perso_tmp, [position_x_perso_tmp,position_y_perso_tmp])


				barres_de_vie[index] = pygame.image.load("Graphism/trop_des_barres/barre_vie.png").convert_alpha()
				barres_de_attaque[index] = pygame.image.load("Graphism/trop_des_barres/barre_attaque.png").convert_alpha()

				jauge_de_vie = pygame.image.load("Graphism/trop_des_barres/jauge_vie.png").convert_alpha()
				jauge_de_attaque = pygame.image.load("Graphism/trop_des_barres/jauge_attaque.png").convert_alpha()
				jauge_de_vie_actuelle = pygame.transform.scale(jauge_de_vie, (10,100))
				jauge_de_attaque_actuelle = pygame.transform.scale(jauge_de_attaque, (10,100))

				position_x_barre_de_vie = position_x_perso_tmp - 15
				position_y_barre_de_vie = position_y_perso_tmp - 100 - 15*(index%2)
					
				fenetre.blit(barres_de_vie[index], (position_x_barre_de_vie,position_y_barre_de_vie))
				fenetre.blit(barres_de_attaque[index], (position_x_barre_de_vie,position_y_barre_de_vie + 30))

				nb_affichages_vie = int(20*(equipe_ennemis.membres[index].pv_actuels / equipe_ennemis.membres[index].pv_max_donjons))
				# print("\n\n",equipe_ennemis.membres[index].pv_actuels," / ",equipe_ennemis.membres[index].pv_max_donjons," multiplié par 100 divisé par 5 = ",nb_affichages_vie,"\n\n")
				if(nb_affichages_vie == 0 and equipe_ennemis.membres[index].pv_actuels > 0):
					nb_affichages_vie = 1
				
				nb_affichages_attaque = equipe_ennemis.membres[index].jauge_attaque // 5
				
				for index in range(nb_affichages_vie):
					fenetre.blit(jauge_de_vie_actuelle, (position_x_barre_de_vie + 65 +5*index,position_y_barre_de_vie))
				for index in range(nb_affichages_attaque):
					fenetre.blit(jauge_de_attaque_actuelle, (position_x_barre_de_vie + 65 +5*index,position_y_barre_de_vie + 30))



		if('Mont Tagne' in equipe_ennemis.nom_niveau_donjon):
			if(equipe_ennemis.membres[index] != 0 and equipe_ennemis.membres[index].pv_actuels > 0):
				perso_tmp = trouver_image_monstre(equipe_ennemis.membres[index].nom, equipe_ennemis.nom_niveau_donjon)
				images_persos.append(perso_tmp)

				position_x_perso_tmp = ((1+index)*dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2 - 30
				position_y_perso_tmp = 200

				if(equipe_ennemis.membres[index].nom == 'Slime'): 
					position_y_perso_tmp += 80
				if(equipe_ennemis.membres[index].nom == 'Golem'):
					position_x_perso_tmp = position_x_perso_tmp - 150 + 50*index

				positions_persos.append([position_x_perso_tmp,position_y_perso_tmp])
				fenetre.blit(perso_tmp, [position_x_perso_tmp,position_y_perso_tmp])


				barres_de_vie[index] = pygame.image.load("Graphism/trop_des_barres/barre_vie.png").convert_alpha()
				barres_de_attaque[index] = pygame.image.load("Graphism/trop_des_barres/barre_attaque.png").convert_alpha()

				jauge_de_vie = pygame.image.load("Graphism/trop_des_barres/jauge_vie.png").convert_alpha()
				jauge_de_attaque = pygame.image.load("Graphism/trop_des_barres/jauge_attaque.png").convert_alpha()
				jauge_de_vie_actuelle = pygame.transform.scale(jauge_de_vie, (10,100))
				jauge_de_attaque_actuelle = pygame.transform.scale(jauge_de_attaque, (10,100))

				position_x_barre_de_vie = position_x_perso_tmp - 15
				position_y_barre_de_vie = position_y_perso_tmp - 100 - 15*(index%2)
					
				fenetre.blit(barres_de_vie[index], (position_x_barre_de_vie,position_y_barre_de_vie))
				fenetre.blit(barres_de_attaque[index], (position_x_barre_de_vie,position_y_barre_de_vie + 30))

				nb_affichages_vie = int(20*(equipe_ennemis.membres[index].pv_actuels / equipe_ennemis.membres[index].pv_max_donjons))
				# print("\n\n",equipe_ennemis.membres[index].pv_actuels," / ",equipe_ennemis.membres[index].pv_max_donjons," multiplié par 100 divisé par 5 = ",nb_affichages_vie,"\n\n")
				if(nb_affichages_vie == 0 and equipe_ennemis.membres[index].pv_actuels > 0):
					nb_affichages_vie = 1
				
				nb_affichages_attaque = equipe_ennemis.membres[index].jauge_attaque // 5
				
				for index in range(nb_affichages_vie):
					fenetre.blit(jauge_de_vie_actuelle, (position_x_barre_de_vie + 65 +5*index,position_y_barre_de_vie))
				for index in range(nb_affichages_attaque):
					fenetre.blit(jauge_de_attaque_actuelle, (position_x_barre_de_vie + 65 +5*index,position_y_barre_de_vie + 30))


		if('Ruines de Senzargen' in equipe_ennemis.nom_niveau_donjon):
			if(equipe_ennemis.membres[index] != 0 and equipe_ennemis.membres[index].pv_actuels > 0):
				perso_tmp = trouver_image_monstre(equipe_ennemis.membres[index].nom, equipe_ennemis.nom_niveau_donjon)
				images_persos.append(perso_tmp)

				position_x_perso_tmp = ((1+index)*dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2 - 30
				position_y_perso_tmp = 200

				if(equipe_ennemis.membres[index].nom == 'Elementaire' or equipe_ennemis.membres[index].nom == 'Haut Elementaire'):
					position_x_perso_tmp = position_x_perso_tmp - 150 + 50*index
				if(equipe_ennemis.membres[index].nom == 'Haut Elementaire'):
					position_x_perso_tmp -= 50
				if(equipe_ennemis.membres[index].nom == 'Dame Harpie'):
					position_x_perso_tmp = position_x_perso_tmp - 120 + 50*index
				if(equipe_ennemis.membres[index].nom == 'Sylphe'):
					position_x_perso_tmp -= 200
				if(equipe_ennemis.membres[index].nom == 'Sylphide'):
					position_x_perso_tmp -= 150

				positions_persos.append([position_x_perso_tmp,position_y_perso_tmp])
				fenetre.blit(perso_tmp, [position_x_perso_tmp,position_y_perso_tmp])


				barres_de_vie[index] = pygame.image.load("Graphism/trop_des_barres/barre_vie.png").convert_alpha()
				barres_de_attaque[index] = pygame.image.load("Graphism/trop_des_barres/barre_attaque.png").convert_alpha()

				jauge_de_vie = pygame.image.load("Graphism/trop_des_barres/jauge_vie.png").convert_alpha()
				jauge_de_attaque = pygame.image.load("Graphism/trop_des_barres/jauge_attaque.png").convert_alpha()
				jauge_de_vie_actuelle = pygame.transform.scale(jauge_de_vie, (10,100))
				jauge_de_attaque_actuelle = pygame.transform.scale(jauge_de_attaque, (10,100))

				position_x_barre_de_vie = position_x_perso_tmp - 15
				position_y_barre_de_vie = position_y_perso_tmp - 100 - 15*(index%2)
					
				fenetre.blit(barres_de_vie[index], (position_x_barre_de_vie,position_y_barre_de_vie))
				fenetre.blit(barres_de_attaque[index], (position_x_barre_de_vie,position_y_barre_de_vie + 30))

				nb_affichages_vie = int(20*(equipe_ennemis.membres[index].pv_actuels / equipe_ennemis.membres[index].pv_max_donjons))
				# print("\n\n",equipe_ennemis.membres[index].pv_actuels," / ",equipe_ennemis.membres[index].pv_max_donjons," multiplié par 100 divisé par 5 = ",nb_affichages_vie,"\n\n")
				if(nb_affichages_vie == 0 and equipe_ennemis.membres[index].pv_actuels > 0):
					nb_affichages_vie = 1
				
				nb_affichages_attaque = equipe_ennemis.membres[index].jauge_attaque // 5
				
				for index in range(nb_affichages_vie):
					fenetre.blit(jauge_de_vie_actuelle, (position_x_barre_de_vie + 65 +5*index,position_y_barre_de_vie))
				for index in range(nb_affichages_attaque):
					fenetre.blit(jauge_de_attaque_actuelle, (position_x_barre_de_vie + 65 +5*index,position_y_barre_de_vie + 30))




	# Rafraîchissement de l'écran
	pygame.display.flip()

	return [images_persos,positions_persos]


# On est obligé de transmettre une clé pour enregistrer le relâchement d'une touche
# Si la touche relâchée est un déplacmeent latéral, on actualise la position en x
def initialisation_choice(fenetre,position_choice,nom_monstre,police,key,index_targeted_personnage):
	choice_huge = pygame.image.load("Graphism/viseur-2.png").convert_alpha()
	choice = pygame.transform.scale(choice_huge, (80,80))

	# ATTENTION !!!!!!!!!!!!
	# L'unique inconvénient de Python est l'égalité implicite entre pointeurs de type liste
	# ON NE DOIT DONC SURTOUT PAS FAIRE real_position_choice = position_choice
	# car modifier l'une même dans cette sous-fonction revient à modifier l'autre en global 
	real_position_choice = [0,0]
	real_position_choice[0] = position_choice[0]
	real_position_choice[1] = position_choice[1]


	# Si c'est une abeille (oui... je me déprime :'(  )
	if(nom_monstre == 'Champignon'):
		if(key == K_LEFT or key == K_RIGHT):
			real_position_choice[0] -= 30
		if(real_position_choice[1] > 225):
			real_position_choice[1] -= 30
	
	if(nom_monstre == 'Gardien de la Forêt'):
		choice = pygame.transform.scale(choice_huge, (130,130))
		real_position_choice[1] -= 30
		if(index_targeted_personnage == 0):
			real_position_choice[0] -= 30
		elif(index_targeted_personnage == 1):
			real_position_choice[0] -= 15

	if(nom_monstre == 'Plante Carnivore'):
		choice = pygame.transform.scale(choice_huge, (130,130))
		real_position_choice[1] -= 60
		if(index_targeted_personnage == 0):
			real_position_choice[0] -= 30
		elif(index_targeted_personnage == 1):
			real_position_choice[0] -= 15
		elif(index_targeted_personnage == 2):
			real_position_choice[0] += 15
	
	if(nom_monstre == 'Inugami'):
		choice = pygame.transform.scale(choice_huge, (60,60))
		real_position_choice[0] += 40
		real_position_choice[1] += 20
	
	if(nom_monstre == 'Chauve Souris'):
		real_position_choice[0] -= 20
		real_position_choice[1] -= 40
	
	if(nom_monstre == 'Soldat Squelette'):
		real_position_choice[0] += 5
		real_position_choice[1] -= 30

	if(nom_monstre == 'Imp'):
		real_position_choice[0] -= 10
		real_position_choice[1] -= 60
	
	if(nom_monstre == 'Mastodonte'):
		real_position_choice[0] += 50

	if(nom_monstre == 'Canniboite'):
		real_position_choice[0] -= 25
		real_position_choice[1] -= 25

	if(nom_monstre == 'Golem'):
		if(index_targeted_personnage == 0):
			real_position_choice[0] -= 70
			real_position_choice[1] += 40
		elif(index_targeted_personnage == 1):
			real_position_choice[0] -= 20
			real_position_choice[1] += 40
		elif(index_targeted_personnage == 2):
			real_position_choice[0] += 30
			real_position_choice[1] += 40
	
	if(nom_monstre == 'Dame Harpie'):
		real_position_choice[1] += 80
		if(index_targeted_personnage == 0):
			real_position_choice[0] -= 50
		elif(index_targeted_personnage == 2):
			real_position_choice[0] += 50

	if(nom_monstre == 'Bas Elementaire'):
		real_position_choice[0] -= 10
		real_position_choice[1] -= 10
	
	if(nom_monstre == 'Elementaire' and index_targeted_personnage == 0):
		real_position_choice[0] -= 90
	
	if(nom_monstre == 'Haut Elementaire'):
		real_position_choice[0] -= 50
		if(index_targeted_personnage == 0):
			real_position_choice[0] -= 50
		if(index_targeted_personnage == 2):
			real_position_choice[0] += 50

	if(nom_monstre == 'Sylphe'):
		real_position_choice[0] -= 100
	if(nom_monstre == 'Sylphide'):
		real_position_choice[0] -= 40
		real_position_choice[1] += 40

	#print("\n\n Position choice : ",position_choice,"\n\n Real position choice : ",real_position_choice,"\n\n")
	fenetre.blit(choice, real_position_choice)

	message = police.render("Quel monstre voulez-vous attaquer ? ", 1, (255,0,0))
	if(nom_monstre == 'Gardien de la Forêt'):
		fenetre.blit(message, (10,10))
	else:
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
	fond = initialisation_background(fenetre,equipe_ennemis.nom_niveau_donjon)
	monstres = initialisation_monstres(fenetre,dimensions_fenetre,equipe_ennemis,1)
	police = pygame.font.SysFont("arial", 16)
	right_arrow = pygame.image.load("Graphism/right_arrow.gif").convert_alpha()
	
	# Choix astucieux : 0 est le premier indice possible
	# donc la flèche de choix sera positionnée en face du premier choix 
	# ET 0 n'est dans aucune liste de possibilites_capacite_speciale :)
	choix_capacite = 0
	choix_capacite_tmp = 1

	index_targeted_personnage = 0
	index = 0
	nb_ennemis_vivants = 0
	while(index < equipe_ennemis.len):
		if(equipe_ennemis.membres[index] != 0 and equipe_ennemis.membres[index].pv_actuels > 0):
			nb_ennemis_vivants += 1
		index += 1

	index = 0
	while(index < equipe_ennemis.len):
		if(equipe_ennemis.membres[0].pv_actuels <= 0):
			if(equipe_ennemis.membres[1].pv_actuels <= 0):
				index_targeted_personnage = 2
			else:
				index_targeted_personnage = 1
		# else: index_targeted_personnage est déjà initialisé à 0 
		index += 1

	if(index_targeted_personnage == 3):
		print('Erreur majeure 0\n')
		system.exit()
	
	# Code pour indication : liste de deux éléments (un pour le type d'action, l'autre pour le contenu)
	# Si indication[0] = 0 : afficher à gauche une liste de messages contenue dans indication[1]
	# Si indication[0] = 616 : afficher à droite une liste de messages contenue dans indication[1]

	# Si indication[0] = 1 : faire choisir une cible (indication[1] n'est pas évalué)
		# Cohérent car le choix d'une cible se fait à gauche !!

	# Si indication[0] = 617 : afficher une image à droite 
		# POUR L'INSTANT seulement utilisé pour faire choisir une capacité
			# Ici, on affiche donc right_arrow à droite comme image, en face de choix_capacite
			# On affiche en même temps indication[1] (car indication[0] à 1 permet AUSSI d'afficher des messages)
		# Si indication[0] = 617, on récupère la variable possibilites_capacite_speciale 
			# dans indication[2] qui existera alors TOUJOURS si indication[0] = 617 


	if(indication[0] == 0):
		# Affichage d'un simple message sur la gauche 
		initialisation_print(fenetre, police, indication[1],[0])

	elif(indication[0] == 616 or indication[0] == 618):
		# Affichage d'un simple message sur la droite
		initialisation_print(fenetre, police, indication[1], [indication[0]])




	if(indication[0] == 617):
		# CHOIX D UNE CAPACITE SPECIALE  

		initialisation_print(fenetre, police, indication[1], [617,right_arrow,choix_capacite])
		possibilites_capacite_speciale=indication[2]
		# noms_capacites_speciales=indication[3]
		
		continuer = 1
		valider = 1
		while(choix_capacite not in possibilites_capacite_speciale or (continuer == 1 or valider == 1)):
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					if event.key == K_DOWN:
						choix_capacite_tmp += 1
						if(choix_capacite_tmp > possibilites_capacite_speciale[len(possibilites_capacite_speciale)-1]):
							choix_capacite_tmp -= possibilites_capacite_speciale[len(possibilites_capacite_speciale)-1]
						
						dimensions_fenetre = [2*617,2*480]
						fenetre = initialisation_fenetre(dimensions_fenetre)
						graphism(fenetre,dimensions_fenetre,equipe_ennemis,[616,indication[1]])
						initialisation_print(fenetre, police, indication[1], [617,right_arrow,choix_capacite_tmp])
					
					if event.key == K_UP:
						choix_capacite_tmp -= 1
						if(choix_capacite_tmp == 0):
							choix_capacite_tmp = possibilites_capacite_speciale[len(possibilites_capacite_speciale)-1]
						
						dimensions_fenetre = [2*617,2*480]
						fenetre = initialisation_fenetre(dimensions_fenetre)
						graphism(fenetre,dimensions_fenetre,equipe_ennemis,[616,indication[1]])
						initialisation_print(fenetre, police, indication[1], [617,right_arrow,choix_capacite_tmp])

					if (event.key == K_RETURN):
						choix_capacite = choix_capacite_tmp
						if(choix_capacite not in possibilites_capacite_speciale):
							print('\n Dommage!! Essaye encore!! \n (Capacité ', choix_capacite, ' donnée n\'appartient pas à la liste des possibilités ', possibilites_capacite_speciale,')\n')
						else:
							continuer = 0
					
				if event.type == KEYUP:
					if (event.key == K_RETURN or event.key == K_KP_ENTER):
						valider = 0
		
		return choix_capacite




	elif(indication[0] == 1):
		# CHOIX D UNE CIBLE 


		position_choice = [(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2, 250]
		# Actualisation de la position de la flèche de choix
		fenetre = initialisation_fenetre(dimensions_fenetre)
		fond = initialisation_background(fenetre,equipe_ennemis.nom_niveau_donjon)
		monstres = initialisation_monstres(fenetre,dimensions_fenetre,equipe_ennemis,1)

		# indication[1] : le choix retenu,  indication[2] : la liste des messages
		graphism(fenetre,dimensions_fenetre,equipe_ennemis,[616,indication[2]])
		initialisation_print(fenetre, police, indication[2], [617,right_arrow,indication[1]])

		index = 0
		while(index < equipe_ennemis.len and equipe_ennemis.membres[index].pv_actuels <= 0):
			# Pour chaque ennemi mort, on décale la flèche vers la droite
			position_choice[0] += (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
			index += 1
		
		initialisation_choice(fenetre,position_choice,equipe_ennemis.membres[0].nom,police,K_LEFT,index)
		# Rafraîchissement de l'écran
		# pygame.display.flip()

		continuer = 1
		valider = 1
		while (continuer == 1 or valider == 1):
			# On parcourt la liste de tous les événements reçus
			for event in pygame.event.get():
				# Liste complète des possibilités à la place de K_RIGHT, LEFT, UP, DOWN :
				# https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1
		
				if (event.type == KEYDOWN):
					if(index_targeted_personnage == 3):
						print('Erreur majeure 1\n')
						system.exit()

					if event.key == K_RETURN:
						continuer = 0

					elif(equipe_ennemis.len == 3):
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
							if(index_targeted_personnage == 3):
								print('Erreur majeure 2 \n')
								system.exit()

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
							if(index_targeted_personnage == 3):
								print('Erreur majeure 3 \n')
								system.exit()

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
								if(index_targeted_personnage == 3):
									print('Erreur majeure 4\n')
									system.exit()
							
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
								if(index_targeted_personnage == 3):
									print('Erreur majeure 5\n')
									system.exit()

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
								if(index_targeted_personnage == 3):
									print('Erreur majeure 6\n')
									system.exit()


						elif(nb_ennemis_vivants == 1 and (event.key == K_RIGHT or event.key == K_LEFT)):
							index_alive_monster = 0
							while(index_alive_monster < equipe_ennemis.len and equipe_ennemis.membres[index_alive_monster].pv_actuels <= 0):
								index_alive_monster += 1
							position_choice[0] = (index_alive_monster + 1)*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
							index_targeted_personnage = index_alive_monster
							if(index_targeted_personnage == 3):
								print('Erreur majeure 7\n')
								system.exit()
					
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
							if(index_targeted_personnage == 3):
								print('Erreur majeure 8\n')
								system.exit()

						elif(nb_ennemis_vivants == 1 and (event.key == K_RIGHT or event.key == K_LEFT)):
							index_alive_monster = 0
							if(equipe_ennemis.membres[index_alive_monster].pv_actuels <= 0):
								index_alive_monster = 1
							position_choice[0] = (1 + index_alive_monster)*(dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
							index_targeted_personnage = index_alive_monster
							if(index_targeted_personnage == 3):
								print('Erreur majeure 9\n')
								system.exit()
					
					elif(equipe_ennemis.len == 1):
						position_choice[0] = (dimensions_fenetre[0] / (equipe_ennemis.len + 1))/2
						index_targeted_personnage = 0
						if(index_targeted_personnage == 3):
							print('Erreur majeure 10\n')
							system.exit()

					'''
					LE RAFRAICHISSEMENT SE FAIT EN RELACHANT LA TOUCHE ENFONCEE 

					# Actualisation de la position de la flèche de choix
					fenetre = initialisation_fenetre(dimensions_fenetre)
					fond = initialisation_background(fenetre)
					monstres = initialisation_monstres(fenetre,dimensions_fenetre,equipe_ennemis,1)
					initialisation_choice(fenetre,position_choice,equipe_ennemis.membres[index_targeted_personnage].nom,police, event.key)

					# indication[1] : le choix retenu,  indication[2] : la liste des messages
					graphism(fenetre,dimensions_fenetre,equipe_ennemis,[616,indication[2]])
					initialisation_print(fenetre, police, indication[2], [617,right_arrow,indication[1]])

					# Rafraichissement de l'écran
					# pygame.display.flip()
					'''

				if event.type == KEYUP:
					if event.key == K_RETURN:
						valider = 0

					# Actualisation de la position du viseur de choix
					fenetre = initialisation_fenetre(dimensions_fenetre)
					fond = initialisation_background(fenetre,equipe_ennemis.nom_niveau_donjon)
					monstres = initialisation_monstres(fenetre,dimensions_fenetre,equipe_ennemis,1)
				
					# indication[1] : le choix retenu,  indication[2] : la liste des messages
					graphism(fenetre,dimensions_fenetre,equipe_ennemis,[616,indication[2]])
					initialisation_print(fenetre, police, indication[2], [617,right_arrow,indication[1]])

					initialisation_choice(fenetre,position_choice,equipe_ennemis.membres[index_targeted_personnage].nom,police,event.key,index_targeted_personnage)
					# Rafraîchissement de l'écran
					# pygame.display.flip()

		# Quand le joueur a validé son choix et que ce dernier est correct 
		return index_targeted_personnage












































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