# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:41:34 2019

@author: marin
"""

''' if need help : https://programmation360.com/programmation-orientee-objet-python/ '''

import random
import math
import sys
from ast import literal_eval

from Graphism_ForetVeur import *

#from Runes_and_Objects import *
#from Dungeon import *


'''
from Base import *
from Dungeon import *
from Functions import *
from Inventory_and_Teams import *
from Runes_and_Objects import *
'''
# CORIIGER LES .POP!!!!

class Monstre:
    def __init__(self, nom_donne, attribut_donne, classe_donnee, niveau_donne, pv_donnes, pv_actuels_donnes, attaque_donnee, defense_donnee, vitesse_donnee):
        self.nom=nom_donne
        self.surnom=nom_donne
        self.type='Monstre'
        self.attribut=attribut_donne
        self.classe=classe_donnee
        self.niveau=niveau_donne
        self.pv=pv_donnes
        self.pv_actuels=pv_actuels_donnes
        self.pv_max_donjons=0
        self.attaque=attaque_donnee
        self.attaque_actuelle=attaque_donnee
        self.attaque_max_donjons=0
        self.defense=defense_donnee
        self.defense_actuelle=defense_donnee
        self.defense_max_donjons=0
        self.vitesse=vitesse_donnee
        self.vitesse_actuelle=vitesse_donnee
        self.vitesse_max_donjons=0
        self.taux_coup_superficiel=0
        self.taux_coup_critique=0.15
        self.taux_coup_critique_actuel=self.taux_coup_critique
        self.taux_coup_critique_max_donjons=0
        self.dommages_critiques=0.5
        self.dommages_critiques_actuels=self.dommages_critiques
        self.dommages_critiques_max_donjons=0
        self.resistance=0.15
        self.resistance_actuelle=self.resistance
        self.resistance_max_donjons=0
        self.precision=0
        self.precision_actuelle=self.precision
        self.precision_max_donjons=0

        self.statistiques=[self.pv,self.attaque,self.defense,self.vitesse,self.taux_coup_critique,self.dommages_critiques,self.resistance,self.precision]
        self.statistiques_actuelles=[self.pv_actuels,self.attaque_actuelle,self.defense_actuelle,self.vitesse_actuelle,self.taux_coup_critique_actuel,self.dommages_critiques_actuels,self.resistance_actuelle,self.precision_actuelle]
        self.statistiques_max_donjons=[self.pv_max_donjons,self.attaque_max_donjons,self.defense_max_donjons,self.vitesse_max_donjons,self.taux_coup_critique_max_donjons,self.dommages_critiques_max_donjons,self.resistance_max_donjons,self.precision_max_donjons]

        self.immunite_max_donjons=0
        self.tours_immunite_max_donjons=0
        self.vol_de_vie_max_donjons=0
        self.regeneration_max_donjons=0
        self.taux_contre_attaque_max_donjons=0
        self.chances_de_stun_max_donjons=0
        self.tour_supplementaire_max_donjons=0
        self.chances_tour_supplementaire_max_donjons=0
        self.immortalite_max_donjons=0
        self.tours_immortalite_max_donjons=0

        self.eveil=0
        self.indice_stockage_base=999

        self.equipement_rune_haut=0
        self.equipement_rune_haut_droite=0
        self.equipement_rune_bas_droite=0
        self.equipement_rune_bas=0
        self.equipement_rune_bas_gauche=0
        self.equipement_rune_haut_gauche=0
        self.equipement=[self.equipement_rune_haut,self.equipement_rune_haut_droite,self.equipement_rune_bas_droite,self.equipement_rune_bas,self.equipement_rune_bas_gauche,self.equipement_rune_haut_gauche]
        self.XP_avant_prochain_niveau=self.trouver_XP_initiale()

        self.bonus_de_runes_en_pv=0
        self.bonus_de_runes_en_pourcentage_de_pv=0
        self.bonus_de_runes_en_attaque=0
        self.bonus_de_runes_en_pourcentage_de_attaque=0
        self.bonus_de_runes_en_defense=0
        self.bonus_de_runes_en_pourcentage_de_defense=0
        self.bonus_de_runes_en_vitesse=0            
        self.bonus_de_runes_en_taux_de_coup_critique=0
        self.bonus_de_runes_en_dommages_critiques=0
        self.bonus_de_runes_en_resistance=0
        self.bonus_de_runes_en_precision=0
        self.bonus_de_runes=[self.bonus_de_runes_en_pv,self.bonus_de_runes_en_pourcentage_de_pv,self.bonus_de_runes_en_attaque,self.bonus_de_runes_en_pourcentage_de_attaque,self.bonus_de_runes_en_defense,self.bonus_de_runes_en_pourcentage_de_defense,self.bonus_de_runes_en_vitesse,self.bonus_de_runes_en_taux_de_coup_critique,self.bonus_de_runes_en_dommages_critiques,self.bonus_de_runes_en_resistance,self.bonus_de_runes_en_precision]

        self.bonus_de_runes_en_immunite=0
        self.bonus_de_runes_en_tours_immunite=0
        self.bonus_de_runes_en_vol_de_vie=0
        self.bonus_de_runes_en_regeneration=0
        self.bonus_de_runes_en_taux_contre_attaque=0
        self.bonus_de_runes_en_chances_de_stun=0
        self.bonus_de_runes_en_tour_supplementaire=0
        self.bonus_de_runes_en_chances_tour_supplementaire=0
        self.bonus_de_runes_en_immortalite=0
        self.bonus_de_runes_en_tours_immortalite=0
        
        self.jauge_attaque=0
        self.presence_leader_skill=0
        self.presence_passif_1=0
        self.presence_passif_2=0
        self.reduction_de_degats=0
        self.nb_coups_subis=0        
        self.vol_de_vie=0
        self.determination=0        
        self.chances_tour_supplementaire=0
        self.tour_supplementaire=0
        self.tour_supplementaire_tmp=0

        self.tours_bonus_attaque=0
        self.tours_bonus_defense=0
        self.tours_bonus_vitesse=0
        self.tours_bonus_taux_coup_critique=0        
        self.regeneration=0
        self.tours_regeneration=0
        self.taux_contre_attaque=0
        self.contre_attaque=0
        self.tours_contre_attaque=0
        self.immunite=0
        self.tours_immunite=0        
        self.invincibilite=0
        self.tours_invincibilite=0        
        self.immortalite=0
        self.tours_immortalite=0
        self.reflexion_dommages=0
        self.pourcentage_reflexion_dommages=0
        self.tours_reflexion_dommages=0        
        self.endurance=0
        self.tours_endurance=0
        self.provocation=0
        self.tours_provocation=0
        self.chances_de_stun=0
        
        self.malus_attaque=0
        self.tours_malus_attaque=0
        self.malus_defense=0        
        self.tours_malus_defense=0        
        self.malus_vitesse=0        
        self.tours_malus_vitesse=0
        self.bonus_taux_coup_superficiel=0
        self.tours_bonus_taux_coup_superficiel=0
        self.immunite_aux_bonus=0
        self.tours_immunite_aux_bonus=0
        self.bombe=0
        self.tours_avant_explosion=0
        self.degats_des_bombes=0
        self.provoque=0
        self.tours_provoque=0
        self.peut_jouer=1
        self.stun=0
        self.gel=0
        self.sommeil=0
        self.tours_sommeil=0
        self.marques_degats_continus=0
        self.intensite_degats_continus=0
        self.incandescence=0
        self.niveau_incandescence=0
        self.perturbation_recup=0
        self.tours_perturbation_recup=0
        self.silencieux=0
        self.tours_silencieux=0
        self.marque=0
        self.tours_marque=0
        self.sans_passif=0
        self.tours_sans_passif=0
        self.sans_resurrection=0
        self.tours_sans_resurrection=0
        
    def __str__(self):
        # AFFICHAGE BROKEN 
        # AFFICHER self.statistiques_actuelles[index] sur self.statistiques[index]
        # AFFICHER self.bonus_de_runes[index]
        return ' Nom : '+str(self.nom)+'\n Surnom : '+str(self.surnom)+'\n Attribut : '+str(self.attribut)+'\n Classe : '+str(self.classe)+' étoile(s) \n Niveau : '+str(self.niveau)+'\n PV : '+str(self.pv_actuels)+' sur '+str(self.pv)+' (+ '+str(self.bonus_de_runes[0]+self.pv*self.bonus_de_runes[1])+')\n Attaque : '+str(self.attaque_actuelle)+' sur '+str(self.attaque)+' (+ '+str(self.bonus_de_runes[2]+self.attaque*self.bonus_de_runes[3])+')\n Défense : '+str(self.defense_actuelle)+' sur '+str(self.defense)+' (+ '+str(self.bonus_de_runes[4]+self.defense*self.bonus_de_runes[5])+')\n Vitesse : '+str(self.vitesse_actuelle)+' sur '+str(self.vitesse)+' (+ '+str(self.bonus_de_runes[6])+')\n Taux de coup critique : '+str(100*self.taux_coup_critique_actuel)+'% sur '+str(100*self.taux_coup_critique)+'% (+ '+str(100*self.bonus_de_runes[7])+'%)\n Dommages critiques : '+str(100*self.dommages_critiques_actuels)+'% sur '+str(100*self.dommages_critiques)+'% (+ '+str(100*self.bonus_de_runes[8])+'%)\n Résistance : '+str(100*self.resistance_actuelle)+'% sur '+str(100*self.resistance)+'% (+ '+str(100*self.bonus_de_runes[9])+'%)\n Précision : '+str(100*self.precision_actuelle)+'% sur '+str(100*self.precision)+'% (+ '+str(100*self.bonus_de_runes[10])+'%)\n Expérience requise avant le prochain niveau : '+str(self.XP_avant_prochain_niveau)+'\n'


    def actualiser_stats_de_listes_a_simples(self):
        self.pv=self.statistiques[0]
        self.attaque=self.statistiques[1]
        self.defense=self.statistiques[2]
        self.vitesse=self.statistiques[3]
        self.taux_coup_critique=self.statistiques[4]
        self.dommages_critiques=self.statistiques[5]
        self.resistance=self.statistiques[6]
        self.precision=self.statistiques[7]

        self.pv_actuels=self.statistiques_actuelles[0]
        self.attaque_actuelle=self.statistiques_actuelles[1]
        self.defense_actuelle=self.statistiques_actuelles[2]
        self.vitesse_actuelle=self.statistiques_actuelles[3]
        self.taux_coup_critique_actuel=self.statistiques_actuelles[4]
        self.dommages_critiques_actuels=self.statistiques_actuelles[5]
        self.resistance_actuelle=self.statistiques_actuelles[6]
        self.precision_actuelle=self.statistiques_actuelles[7]

        self.pv_max_donjons=self.statistiques_max_donjons[0]
        self.attaque_max_donjons=self.statistiques_max_donjons[1]
        self.defense_max_donjons=self.statistiques_max_donjons[2]
        self.vitesse_max_donjons=self.statistiques_max_donjons[3]
        self.taux_coup_critique_max_donjons=self.statistiques_max_donjons[4]
        self.dommages_critiques_max_donjons=self.statistiques_max_donjons[5]
        self.resistance_max_donjons=self.statistiques_max_donjons[6]
        self.precision_max_donjons=self.statistiques_max_donjons[7]

        self.bonus_de_runes_en_pv=self.bonus_de_runes[0]
        self.bonus_de_runes_en_pourcentage_de_pv=self.bonus_de_runes[1]
        self.bonus_de_runes_en_attaque=self.bonus_de_runes[2]
        self.bonus_de_runes_en_pourcentage_de_attaque=self.bonus_de_runes[3]
        self.bonus_de_runes_en_defense=self.bonus_de_runes[4]
        self.bonus_de_runes_en_pourcentage_de_defense=self.bonus_de_runes[5]
        self.bonus_de_runes_en_vitesse=self.bonus_de_runes[6]
        self.bonus_de_runes_en_taux_de_coup_critique=self.bonus_de_runes[7]
        self.bonus_de_runes_en_dommages_critiques=self.bonus_de_runes[8]
        self.bonus_de_runes_en_resistance=self.bonus_de_runes[9]
        self.bonus_de_runes_en_precision=self.bonus_de_runes[10]

        self.equipement_rune_haut=self.equipement[0]
        self.equipement_rune_haut_droite=self.equipement[1]
        self.equipement_rune_bas_droite=self.equipement[2]
        self.equipement_rune_bas=self.equipement[3]
        self.equipement_rune_bas_gauche=self.equipement[4]
        self.equipement_rune_haut_gauche=self.equipement[5]

    
    def actualiser_stats_de_simples_a_listes(self):
        self.statistiques=[self.pv,self.attaque,self.defense,self.vitesse,self.taux_coup_critique,self.dommages_critiques,self.resistance,self.precision]
        self.statistiques_actuelles=[self.pv_actuels,self.attaque_actuelle,self.defense_actuelle,self.vitesse_actuelle,self.taux_coup_critique_actuel,self.dommages_critiques_actuels,self.resistance_actuelle,self.precision_actuelle]
        self.statistiques_max_donjons=[self.pv_max_donjons,self.attaque_max_donjons,self.defense_max_donjons,self.vitesse_max_donjons,self.taux_coup_critique_max_donjons,self.dommages_critiques_max_donjons,self.resistance_max_donjons,self.precision_max_donjons]
        self.bonus_de_runes=[self.bonus_de_runes_en_pv,self.bonus_de_runes_en_pourcentage_de_pv,self.bonus_de_runes_en_attaque,self.bonus_de_runes_en_pourcentage_de_attaque,self.bonus_de_runes_en_defense,self.bonus_de_runes_en_pourcentage_de_defense,self.bonus_de_runes_en_vitesse,self.bonus_de_runes_en_taux_de_coup_critique,self.bonus_de_runes_en_dommages_critiques,self.bonus_de_runes_en_resistance,self.bonus_de_runes_en_precision]
        self.equipement=[self.equipement_rune_haut,self.equipement_rune_haut_droite,self.equipement_rune_bas_droite,self.equipement_rune_bas,self.equipement_rune_bas_gauche,self.equipement_rune_haut_gauche]





    def recoit_degats(self,degats):
        self.pv_actuels=self.pv_actuels-degats
        if (self.pv_actuels <= 0):
            self.pv_actuels=0
        
    def etre_soigne(self,montant):
        montant=Arrondir.a_l_unite(montant)
        if(self.nom=='LoupGarou' and self.attribut=='Feu'):
            montant=2*montant
        if(montant > 0 and self.perturbation_recup <= 0):
            pv_actuels_tmp=self.pv_actuels
            if (montant+self.pv_actuels >= self.pv_max_donjons):
                if(self.pv_actuels < self.pv_max_donjons):
                    self.pv_actuels=self.pv_max_donjons
                    print(self.surnom,self.attribut,' récupère ',self.pv_max_donjons-pv_actuels_tmp,'points de vie!! \n')
            else:
                self.pv_actuels+=montant
                print(self.surnom,self.attribut,' récupère ',montant,'points de vie!! \n')
    
    
    def soigner_monstre_entre_deux_vagues(self):
        self.jauge_attaque=0
        self.tour_supplementaire_tmp=0
        self.nb_coups_subis=0
        self.reduction_de_degats=0
        self.taux_coup_superficiel=0

        self.immunite=self.immunite_max_donjons
        self.tours_immunite=self.tours_immunite_max_donjons
        self.vol_de_vie=self.vol_de_vie_max_donjons
        self.regeneration=self.regeneration_max_donjons
        self.taux_contre_attaque=self.taux_contre_attaque_max_donjons
        self.chances_de_stun=self.chances_de_stun_max_donjons
        self.tour_supplementaire=self.tour_supplementaire_max_donjons
        self.chances_tour_supplementaire=self.chances_tour_supplementaire_max_donjons
        self.immortalite=self.immortalite_max_donjons
        self.tours_immortalite=self.tours_immortalite_max_donjons

        self.tours_bonus_attaque=0
        self.tours_bonus_defense=0
        self.tours_bonus_vitesse=0
        self.tours_bonus_taux_coup_critique=0        
        self.tours_regeneration=0
        self.contre_attaque=0
        self.tours_contre_attaque=0
        self.immunite=0
        self.tours_immunite=0
        self.invincibilite=0
        self.tours_invincibilite=0   
        self.immortalite=0
        self.tours_immortalite=0 
        
        if(not (self.nom == 'Golem' and self.attribut == 'Ténèbres')):
            self.pourcentage_reflexion_dommages=0
            self.tours_reflexion_dommages=0
            self.reflexion_dommages=0
        else:
            self.pourcentage_reflexion_dommages=0.15
            self.tours_reflexion_dommages=0
            self.reflexion_dommages=1 
        if((self.nom == 'Golem' and (self.attribut == 'Feu' or self.attribut == 'Eau')) or self.nom == 'Mastodonte'):
            self.passif_active=0
        if(self.nom == 'Serpent' and self.attribut == 'Lumière'):
            self.nb_effets_renforcement=0
            
        self.endurance=0
        self.tours_endurance=0
        self.provocation=0
        self.tours_provocation=0
        
        self.tours_malus_attaque=0
        self.tours_malus_defense=0        
        self.tours_malus_vitesse=0       
        self.bonus_taux_coup_superficiel=0
        self.tours_bonus_taux_coup_superficiel=0
        self.immunite_aux_bonus=0
        self.tours_immunite_aux_bonus=0
        self.bombe=0
        self.tours_avant_explosion=0
        self.degats_des_bombes=0
        self.provoque=0
        self.tours_provoque=0
        self.peut_jouer=1
        self.stun=0
        self.gel=0
        self.sommeil=0
        self.tours_sommeil=0
        self.marques_degats_continus=0
        self.intensite_degats_continus=0
        self.perturbation_recup=0
        self.tours_perturbation_recup=0
        self.silencieux=0
        self.tours_silencieux=0
        self.marque=0
        self.tours_marque=0
        self.sans_passif=0
        self.tours_sans_passif=0
        self.sans_resurrection=0
        self.tours_sans_resurrection=0
        
    
    # A CHANGER POUR CONSERVER PASSIFS DE CERTAINS MONSTRES
    def soigner_monstre(self):
        for index in range(len(self.statistiques)):
            self.statistiques_actuelles[index]=self.statistiques[index]
        self.actualiser_stats_de_listes_a_simples()

        self.taux_coup_superficiel=0
        self.jauge_attaque=0
        self.tour_supplementaire_tmp=0
        self.nb_coups_subis=0
        self.reduction_de_degats=0

        self.immunite=0
        self.tours_immunite=0
        self.vol_de_vie=0
        self.regeneration=0
        self.taux_contre_attaque=0
        self.chances_de_stun=0
        self.tour_supplementaire=0
        self.chances_tour_supplementaire=0
        self.immortalite=0
        self.tours_immortalite=0

        self.tours_bonus_attaque=0
        self.tours_bonus_defense=0
        self.tours_bonus_vitesse=0
        self.tours_bonus_taux_coup_critique=0        
        self.tours_regeneration=0
        self.contre_attaque=0
        self.tours_contre_attaque=0
        self.immunite=0
        self.tours_immunite=0
        self.invincibilite=0
        self.tours_invincibilite=0   
        self.immortalite=0
        self.tours_immortalite=0 
        
        if(not (self.nom == 'Golem' and self.attribut == 'Ténèbres')):
            self.pourcentage_reflexion_dommages=0
            self.tours_reflexion_dommages=0
            self.reflexion_dommages=0
        else:
            self.pourcentage_reflexion_dommages=0.15
            self.tours_reflexion_dommages=0
            self.reflexion_dommages=1 
        if((self.nom == 'Golem' and (self.attribut == 'Feu' or self.attribut == 'Eau')) or self.nom == 'Mastodonte'):
            self.passif_active=0
        if(self.nom == 'Serpent' and self.attribut == 'Lumière'):
            self.nb_effets_renforcement=0
            
        self.endurance=0
        self.tours_endurance=0
        self.provocation=0
        self.tours_provocation=0
        
        self.tours_malus_attaque=0
        self.tours_malus_defense=0        
        self.tours_malus_vitesse=0       
        self.bonus_taux_coup_superficiel=0
        self.tours_bonus_taux_coup_superficiel=0
        self.immunite_aux_bonus=0
        self.tours_immunite_aux_bonus=0
        self.bombe=0
        self.tours_avant_explosion=0
        self.degats_des_bombes=0
        self.provoque=0
        self.tours_provoque=0
        self.peut_jouer=1
        self.stun=0
        self.gel=0
        self.sommeil=0
        self.tours_sommeil=0
        self.marques_degats_continus=0
        self.intensite_degats_continus=0
        self.perturbation_recup=0
        self.tours_perturbation_recup=0
        self.silencieux=0
        self.tours_silencieux=0
        self.marque=0
        self.tours_marque=0
        self.sans_passif=0
        self.tours_sans_passif=0
        self.sans_resurrection=0
        self.tours_sans_resurrection=0


    def reset_monstre(nom_creature):
        # Faire un or pour les noms séparés
        if(nom_creature == 'Slime'):
            creature=Slime()
        if(nom_creature == 'GardienForet' or nom_creature == 'Gardien de la Forêt'):
            creature=GardienForet()
        if(nom_creature == 'Champignon'):
            creature=Champignon()
        if(nom_creature == 'Spectre'):
            creature=Spectre()
        if(nom_creature == 'Canniboite'):
            creature=Canniboite()
        if(nom_creature == 'Crapoxique'):
            creature=Crapoxique()
        if(nom_creature == 'Sacasable'):
            creature=Sacasable()
        if(nom_creature == 'BasElementaire' or nom_creature == 'Bas Elementaire'):
            creature=BasElementaire()
        if(nom_creature == 'Sanglier'):
            creature=Sanglier()
        if(nom_creature == 'PlanteCarnivore' or nom_creature == 'Plante Carnivore'):
            creature=PlanteCarnivore()
        if(nom_creature == 'BoiteDePandore' or nom_creature == 'Boite de Pandore'):
            creature=BoiteDePandore()
        if(nom_creature == 'SoldatSquelette' or nom_creature == 'Soldat Squelette'):
            creature=SoldatSquelette()
        if(nom_creature == 'ChauveSouris' or nom_creature == 'Chauve Souris'):
            creature=ChauveSouris()
        if(nom_creature == 'Scorpion'):
            creature=Scorpion()
        if(nom_creature == 'Imp'):
            creature=Imp()
        if(nom_creature == 'Lutin'):
            creature=Lutin()
        if(nom_creature == 'Yeti'):
            creature=Yeti()
        if(nom_creature == 'Cerbere'):
            creature=Cerbere()
        if(nom_creature == 'OursDeGuerre' or nom_creature == 'Ours de Guerre'):
            creature=OursDeGuerre()
        if(nom_creature == 'Elementaire'):
            creature=Elementaire()
        if(nom_creature == 'Garuda'):
            creature=Garuda()
        if(nom_creature == 'Harpie'):
            creature=Harpie()
        if(nom_creature == 'Salamandre'):
            creature=Salamandre()
        if(nom_creature == 'Esprit'):
            creature=Esprit()
        if(nom_creature == 'Viking'):
            creature=Viking()
        if(nom_creature == 'Chevalier'):
            creature=Chevalier()
        if(nom_creature == 'Fee'):
            creature=Fee()
        if(nom_creature == 'DameHarpie' or nom_creature == 'Dame Harpie'):
            creature=DameHarpie()
        if(nom_creature == 'Inugami'):
            creature=Inugami()
        if(nom_creature == 'Golem'):
            creature=Golem()
        if(nom_creature == 'Mastodonte'):
            creature=Mastodonte()
        if(nom_creature == 'Serpent'):
            creature=Serpent()
        if(nom_creature == 'Griffon'):
            creature=Griffon()
        if(nom_creature == 'Inferno'):
            creature=Inferno()
        if(nom_creature == 'HautElementaire' or nom_creature == 'Haut Elementaire'):
            creature=HautElementaire()
        if(nom_creature == 'OursDeCombat' or nom_creature == 'Ours de Combat'):
            creature=OursDeCombat()
        if(nom_creature == 'LoupGarou' or nom_creature == 'Loup Garou'):
            creature=LoupGarou()
        if(nom_creature == 'Elfe'):
            creature=Elfe()
        if(nom_creature == 'ChevalierMagique' or nom_creature == 'Chevalier Magique'):
            creature=ChevalierMagique()
        if(nom_creature == 'Vampire'):
            creature=Vampire()
        if(nom_creature == 'Sylphe'):
            creature=Sylphe()
        if(nom_creature == 'Sylphide'):
            creature=Sylphide()
        if(nom_creature == 'Phénix'):
            creature=Phenix()
        return creature





















    def afficher_equipement_monstre(self,position):
        print('\n')
        positions=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']
        positions_a_afficher=['haut','haut à droite','bas à droite','bas','bas à gauche','haut à gauche']
        for index in range(len(self.equipement)):
            if(self.equipement[index] != 0 and positions[index] == position):
                print('La rune en ',positions_a_afficher[index],' de ',self.surnom,'est : \n',self.equipement[index],'\n')
            elif(positions[index] == position):
                print(self.surnom,' n\'a aucune rune équipée en ',positions_a_afficher[index],' pour le moment.\n')
        print('\n')

    def afficher_equipement_monstre_complet(self):
        print('\n')
        positions=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']
        positions_a_afficher=['haut','haut à droite','bas à droite','bas','bas à gauche','haut à gauche']
        for index in range(len(self.equipement)):
            if(self.equipement[index] != 0):
                print('La rune en ',positions_a_afficher[index],' de ',self.surnom,'est : \n',self.equipement[index],'\n')
            else:
                print(self.surnom,' n\'a aucune rune équipée en ',positions_a_afficher[index],' pour le moment.\n')
        print('\n')




    def desequiper_sans_affichage(self,place_rune_choisie):
        self.malus_famille_de_runes()

        '''
        monstre_choisi.pv-=Arrondir.a_l_unite(monstre_choisi.bonus_de_runes_en_pv+monstre_choisi.pv*monstre_choisi.bonus_de_runes_en_pourcentage_de_pv)
        monstre_choisi.attaque-=Arrondir.a_l_unite(monstre_choisi.bonus_de_runes_en_attaque+monstre_choisi.attaque*monstre_choisi.bonus_de_runes_en_pourcentage_de_attaque)
        monstre_choisi.defense-=Arrondir.a_l_unite(monstre_choisi.bonus_de_runes_en_defense+monstre_choisi.defense*monstre_choisi.bonus_de_runes_en_pourcentage_de_defense)
        monstre_choisi.vitesse-=Arrondir.a_l_unite(monstre_choisi.bonus_de_runes_en_vitesse)
        monstre_choisi.taux_coup_critique-=Arrondir.au_centieme(monstre_choisi.bonus_de_runes_en_taux_de_coup_critique)
        monstre_choisi.dommages_critiques-=Arrondir.au_centieme(monstre_choisi.bonus_de_runes_en_dommages_critiques)
        monstre_choisi.resistance-=Arrondir.au_centieme(monstre_choisi.bonus_de_runes_en_resistance)
        monstre_choisi.precision-=Arrondir.au_centieme(monstre_choisi.bonus_de_runes_en_precision)
        '''

        for index in range(len(self.equipement)):
            if(place_rune_choisie == index):
                rune_supprimee=self.equipement[index]
                self.equipement[index]=0
                # RETIRER LES GAINS DE LA RUNE AU MONSTRE !!!!

        if(rune_supprimee!=0):
            for index in range(len(rune_supprimee.gains)):
                self.bonus_de_runes[index]-=rune_supprimee.gains[index]

        self.bonus_famille_de_runes()
        self.actualiser_stats_de_simples_a_listes()

        '''
        monstre_choisi.pv+=Arrondir.a_l_unite(monstre_choisi.bonus_de_runes_en_pv+monstre_choisi.pv*monstre_choisi.bonus_de_runes_en_pourcentage_de_pv)
        monstre_choisi.attaque+=Arrondir.a_l_unite(monstre_choisi.bonus_de_runes_en_attaque+monstre_choisi.attaque*monstre_choisi.bonus_de_runes_en_pourcentage_de_attaque)
        monstre_choisi.defense+=Arrondir.a_l_unite(monstre_choisi.bonus_de_runes_en_defense+monstre_choisi.defense*monstre_choisi.bonus_de_runes_en_pourcentage_de_defense)
        monstre_choisi.vitesse+=Arrondir.a_l_unite(monstre_choisi.bonus_de_runes_en_vitesse)
        monstre_choisi.taux_coup_critique+=Arrondir.au_centieme(monstre_choisi.bonus_de_runes_en_taux_de_coup_critique)
        monstre_choisi.dommages_critiques+=Arrondir.au_centieme(monstre_choisi.bonus_de_runes_en_dommages_critiques)
        monstre_choisi.resistance+=Arrondir.au_centieme(monstre_choisi.bonus_de_runes_en_resistance)
        monstre_choisi.precision+=Arrondir.au_centieme(monstre_choisi.bonus_de_runes_en_precision)
        '''

        for index in range(len(self.statistiques)):
            self.statistiques_actuelles[index]=self.statistiques[index]

        return rune_supprimee









    def bonus_famille_de_runes(self):
        types_runes_equipees=[]
        for index in range(len(self.equipement)):
            if(self.equipement[index] != 0):
                types_runes_equipees.append(self.equipement[index].categorie)

        '''
        monstre.pv-=Arrondir.a_l_unite(monstre.bonus_de_runes_en_pv+monstre.pv*monstre.bonus_de_runes_en_pourcentage_de_pv)
        monstre.attaque-=Arrondir.a_l_unite(monstre.bonus_de_runes_en_attaque+monstre.attaque*monstre.bonus_de_runes_en_pourcentage_de_attaque)
        monstre.defense-=Arrondir.a_l_unite(monstre.bonus_de_runes_en_defense+monstre.defense*monstre.bonus_de_runes_en_pourcentage_de_defense)
        monstre.vitesse-=Arrondir.a_l_unite(monstre.bonus_de_runes_en_vitesse)
        monstre.taux_coup_critique-=Arrondir.au_centieme(monstre.bonus_de_runes_en_taux_de_coup_critique)
        monstre.dommages_critiques-=Arrondir.au_centieme(monstre.bonus_de_runes_en_dommages_critiques)
        monstre.resistance-=Arrondir.au_centieme(monstre.bonus_de_runes_en_resistance)
        monstre.precision-=Arrondir.au_centieme(monstre.bonus_de_runes_en_precision)
        '''

        compteur_Energie=0
        compteur_Colere=0
        compteur_Tenace=0
        compteur_Veloce=0
        compteur_Lame=0
        compteur_Rage=0
        compteur_Sniper=0
        compteur_Illumination=0
        compteur_Volonte=0
        compteur_Vampirique=0
        compteur_Desespoir=0
        compteur_Vengeance=0
        compteur_Violence=0

        compteur_Transcendance=0
        compteur_Extase=0
        compteur_Destruction=0
        compteur_Domination=0
        compteur_Inebranlable=0
        compteur_Sublimation=0
        compteur_Incandescence=0
        compteur_Determination=0
        # FAIRE OSMOSE POUR BONUS SUR L'ENSEMBLE DE L'EQUIPE
        # FAIRE RUNES IRREELLES (COMBINENT TOUS LES BONUS POSSIBLE)

        if ('Energie' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Energie'):
                    compteur_Energie+=1
        if (compteur_Energie >= 2):
            if(compteur_Energie >= 4):
                if(compteur_Energie == 6):
                    bonus_energie=0.45
                else:
                    bonus_energie=0.3
            else:
                bonus_energie=0.15
        else:
            bonus_energie=0
        self.bonus_de_runes_en_pourcentage_de_pv+=bonus_energie

        if ('Colere' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Colere'):
                    compteur_Colere+=1
        if (compteur_Colere >= 4):
            bonus_colere=0.35
        else:
            bonus_colere=0
        self.bonus_de_runes_en_pourcentage_de_attaque+=bonus_colere


        if ('Tenace' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Tenace'):
                    compteur_Tenace+=1
        if (compteur_Tenace >= 2):
            if(compteur_Tenace >= 4):
                if(compteur_Tenace == 6):
                    bonus_tenacite=0.45
                else:
                    bonus_tenacite=0.3
            else:
                bonus_tenacite=0.15
        else:
            bonus_tenacite=0
        self.bonus_de_runes_en_pourcentage_de_defense+=bonus_tenacite


        if ('Veloce' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Veloce'):
                    compteur_Veloce+=1
        if(compteur_Veloce >= 4):
            bonus_velocite=0.25
        else:
            bonus_velocite=0
        self.bonus_de_runes_en_vitesse+=Arrondir.a_l_unite(bonus_velocite*self.vitesse)


        if ('Lame' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Lame'):
                    compteur_Lame+=1
        if (compteur_Lame >= 2):
            if(compteur_Lame >= 4):
                if(compteur_Lame == 6):
                    bonus_lame=0.36
                else:
                    bonus_lame=0.24
            else:
                bonus_lame=0.12
        else:
            bonus_lame=0
        self.bonus_de_runes_en_taux_de_coup_critique+=bonus_lame


        if ('Rage' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Rage'):
                    compteur_Rage+=1
        if(compteur_Rage >= 4):
            bonus_dommages_critiques=0.4
        else:
            bonus_dommages_critiques=0
        self.bonus_de_runes_en_dommages_critiques+=bonus_dommages_critiques


        if ('Precision' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Precision'):
                    compteur_Sniper+=1
        if (compteur_Sniper >= 2):
            if(compteur_Sniper >= 4):
                if(compteur_Sniper == 6):
                    bonus_precision=0.6
                else:
                    bonus_precision=0.4
            else:
                bonus_precision=0.2
        else:
            bonus_precision=0
        self.bonus_de_runes_en_precision+=bonus_precision


        if ('Resistance' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Resistance'):
                    compteur_Illumination+=1
        if (compteur_Illumination >= 2):
            if(compteur_Illumination >= 4):
                if(compteur_Illumination == 6):
                    bonus_resistance=0.6
                else:
                    bonus_resistance=0.4
            else:
                bonus_resistance=0.2
        else:
            bonus_resistance=0
        self.bonus_de_runes_en_resistance+=bonus_resistance


        if ('Vengeance' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Vengeance'):
                    compteur_Vengeance+=1
        if (compteur_Vengeance >= 2):
            if(compteur_Vengeance >= 4):
                if(compteur_Vengeance == 6):
                    bonus_vengeance=0.6
                else:
                    bonus_vengeance=0.4
            else:
                bonus_vengeance=0.2
        else:
            bonus_vengeance=0
        self.bonus_de_runes_en_taux_contre_attaque+=bonus_vengeance


        if ('Volonté' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Volonté'):
                    compteur_Volonte+=1
        if (compteur_Volonte >= 2):
            if(compteur_Volonte >= 4):
                if(compteur_Volonte == 6):
                    bonus_immunite=4
                else:
                    bonus_immunite=3
            else:
                bonus_immunite=2
        else:
            bonus_immunite=0
        if(bonus_immunite!=0):
            self.bonus_de_runes_en_immunite=1
            self.bonus_de_runes_en_tours_immunite=max(bonus_immunite,self.bonus_de_runes_en_tours_immunite)


        if ('Vampirique' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Vampirique'):
                    compteur_Vampirique+=1
        if(compteur_Illumination >= 4):
            bonus_vol_de_vie=35
        else:
            bonus_vol_de_vie=0
        self.bonus_de_runes_en_vol_de_vie+=bonus_vol_de_vie


        if ('Desespoir' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Desespoir'):
                    compteur_Desespoir+=1
        if(compteur_Desespoir >= 4):
            bonus_chances_de_stun=0.25
        else:
            bonus_chances_de_stun=0
        self.bonus_de_runes_en_chances_de_stun+=bonus_chances_de_stun


        if ('Violence' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Violence'):
                    compteur_Violence+=1
        if(compteur_Violence >= 4):
            bonus_chances_tour_supplementaire=0.22
        else:
            bonus_chances_tour_supplementaire=0
        self.bonus_de_runes_en_chances_tour_supplementaire+=bonus_chances_tour_supplementaire


        if ('Transcendance' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Transcendance'):
                    compteur_Transcendance+=1
        if(compteur_Transcendance == 6):
            bonus_transcendance=0.15
        else:
            bonus_transcendance=0
        self.bonus_de_runes_en_pourcentage_de_pv+=bonus_transcendance
        self.bonus_de_runes_en_pourcentage_de_attaque+=bonus_transcendance
        self.bonus_de_runes_en_pourcentage_de_defense+=bonus_transcendance
        self.bonus_de_runes_en_vitesse+=Arrondir.a_l_unite(bonus_transcendance*self.vitesse)
        self.bonus_de_runes_en_taux_de_coup_critique+=bonus_transcendance
        self.bonus_de_runes_en_dommages_critiques+=bonus_transcendance
        self.bonus_de_runes_en_precision+=bonus_transcendance
        self.bonus_de_runes_en_resistance+=bonus_transcendance


        if ('Extase' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Extase'):
                    compteur_Extase+=1
        if(compteur_Extase == 6):
            self.bonus_de_runes_en_tour_supplementaire+=1


        if ('Destruction' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Destruction'):
                    compteur_Destruction+=1
        if (compteur_Destruction >= 2):
            if(compteur_Destruction >= 4):
                if(compteur_Destruction == 6):
                    bonus_attaque=0.7
                    bonus_vitesse=0.5
                else:
                    bonus_attaque=0.35
                    bonus_vitesse=0.25
            else:
                bonus_attaque=0.1
                bonus_vitesse=0.1
        else:
            bonus_attaque=0
            bonus_vitesse=0
        self.bonus_de_runes_en_pourcentage_de_attaque+=bonus_attaque
        self.bonus_de_runes_en_vitesse+=Arrondir.a_l_unite(bonus_vitesse*self.vitesse)


        if ('Domination' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Domination'):
                    compteur_Domination+=1
        if (compteur_Domination >= 2):
            if(compteur_Domination >= 4):
                if(compteur_Domination == 6):
                    bonus_immortalite=4
                else:
                    bonus_immortalite=3
            else:
                bonus_immortalite=2
        else:
            bonus_immortalite=0
        if(bonus_immortalite!=0):
            self.bonus_de_runes_en_immortalite=1
            self.bonus_de_runes_en_tours_immortalite=max(bonus_immortalite,self.bonus_de_runes_en_tours_immortalite)


        if ('Inébranlable' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Inébranlable'):
                    compteur_Inebranlable+=1
        if(compteur_Inebranlable == 6):
            self.bonus_de_runes_en_immunite=1


        if ('Détermination' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Détermination'):
                    compteur_Determination+=1
        if(compteur_Determination == 6):
            self.determination=1


        if ('Incandescence' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Incandescence'):
                    compteur_Incandescence+=1
        if (compteur_Incandescence >= 2):
            if(compteur_Incandescence >= 4):
                if(compteur_Incandescence == 6):
                    bonus_incandescence=4
                else:
                    bonus_incandescence=3
            else:
                bonus_incandescence=2
        else:
            bonus_incandescence=0
        if(bonus_incandescence>0):
            self.incandescence=1
            self.niveau_incandescence=bonus_incandescence


        if ('Sublimation' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Sublimation'):
                    compteur_Sublimation+=1
        if (compteur_Sublimation >= 2):
            if(compteur_Sublimation >= 4):
                if(compteur_Sublimation == 6):
                    bonus_recup=0.45
                else:
                    bonus_recup=0.3
            else:
                bonus_recup=0.15
        else:
            bonus_recup=0
        self.bonus_de_runes_en_regeneration+=bonus_recup


        '''
        monstre.pv+=Arrondir.a_l_unite(monstre.bonus_de_runes_en_pv+monstre.pv*monstre.bonus_de_runes_en_pourcentage_de_pv)
        monstre.attaque+=Arrondir.a_l_unite(monstre.bonus_de_runes_en_attaque+monstre.attaque*monstre.bonus_de_runes_en_pourcentage_de_attaque)
        monstre.defense+=Arrondir.a_l_unite(monstre.bonus_de_runes_en_defense+monstre.defense*monstre.bonus_de_runes_en_pourcentage_de_defense)
        monstre.vitesse+=Arrondir.a_l_unite(monstre.bonus_de_runes_en_vitesse)
        monstre.taux_coup_critique+=Arrondir.au_centieme(monstre.bonus_de_runes_en_taux_de_coup_critique)
        monstre.dommages_critiques+=Arrondir.au_centieme(monstre.bonus_de_runes_en_dommages_critiques)
        monstre.resistance+=Arrondir.au_centieme(monstre.bonus_de_runes_en_resistance)
        monstre.precision+=Arrondir.au_centieme(monstre.bonus_de_runes_en_precision)
        '''

        for index in range(len(self.statistiques_actuelles)):
            self.statistiques_actuelles[index]=self.statistiques[index]
        self.actualiser_stats_de_listes_a_simples()



    def malus_famille_de_runes(self):
        types_runes_equipees=[]
        for index in range(len(self.equipement)):
            if(self.equipement[index] != 0):
                types_runes_equipees.append(self.equipement[index].categorie)

        '''
        monstre.pv-=Arrondir.a_l_unite(monstre.bonus_de_runes_en_pv+monstre.pv*monstre.bonus_de_runes_en_pourcentage_de_pv)
        monstre.attaque-=Arrondir.a_l_unite(monstre.bonus_de_runes_en_attaque+monstre.attaque*monstre.bonus_de_runes_en_pourcentage_de_attaque)
        monstre.defense-=Arrondir.a_l_unite(monstre.bonus_de_runes_en_defense+monstre.defense*monstre.bonus_de_runes_en_pourcentage_de_defense)
        monstre.vitesse-=Arrondir.a_l_unite(monstre.bonus_de_runes_en_vitesse)
        monstre.taux_coup_critique-=Arrondir.au_centieme(monstre.bonus_de_runes_en_taux_de_coup_critique)
        monstre.dommages_critiques-=Arrondir.au_centieme(monstre.bonus_de_runes_en_dommages_critiques)
        monstre.resistance-=Arrondir.au_centieme(monstre.bonus_de_runes_en_resistance)
        monstre.precision-=Arrondir.au_centieme(monstre.bonus_de_runes_en_precision)
        '''

        compteur_Energie=0
        compteur_Colere=0
        compteur_Tenace=0
        compteur_Veloce=0
        compteur_Lame=0
        compteur_Rage=0
        compteur_Sniper=0
        compteur_Illumination=0
        compteur_Volonte=0
        compteur_Vampirique=0
        compteur_Desespoir=0
        compteur_Vengeance=0
        compteur_Violence=0

        compteur_Transcendance=0
        compteur_Extase=0
        compteur_Destruction=0
        compteur_Domination=0
        compteur_Inebranlable=0
        compteur_Sublimation=0
        compteur_Incandescence=0
        compteur_Determination=0
        # FAIRE OSMOSE POUR BONUS SUR L'ENSEMBLE DE L'EQUIPE
        # FAIRE RUNES IRREELLES (COMBINENT TOUS LES BONUS POSSIBLE)

        if ('Energie' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Energie'):
                    compteur_Energie+=1
        if (compteur_Energie >= 2):
            if(compteur_Energie >= 4):
                if(compteur_Energie == 6):
                    bonus_energie=0.45
                else:
                    bonus_energie=0.3
            else:
                bonus_energie=0.15
        else:
            bonus_energie=0
        self.bonus_de_runes_en_pourcentage_de_pv-=bonus_energie


        if ('Colere' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Colere'):
                    compteur_Colere+=1
        if (compteur_Colere >= 4):
            bonus_colere=0.35
        else:
            bonus_colere=0
        self.bonus_de_runes_en_pourcentage_de_attaque-=bonus_colere


        if ('Tenace' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Tenace'):
                    compteur_Tenace+=1
        if (compteur_Tenace >= 2):
            if(compteur_Tenace >= 4):
                if(compteur_Tenace == 6):
                    bonus_tenacite=0.45
                else:
                    bonus_tenacite=0.3
            else:
                bonus_tenacite=0.15
        else:
            bonus_tenacite=0
        self.bonus_de_runes_en_pourcentage_de_defense-=bonus_tenacite


        if ('Veloce' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Veloce'):
                    compteur_Veloce+=1
        if(compteur_Veloce >= 4):
            bonus_velocite=0.25
        else:
            bonus_velocite=0
        self.bonus_de_runes_en_vitesse-=Arrondir.a_l_unite(bonus_velocite*self.vitesse)


        if ('Lame' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Lame'):
                    compteur_Lame+=1
        if (compteur_Lame >= 2):
            if(compteur_Lame >= 4):
                if(compteur_Lame == 6):
                    bonus_lame=0.36
                else:
                    bonus_lame=0.24
            else:
                bonus_lame=0.12
        else:
            bonus_lame=0
        self.bonus_de_runes_en_taux_de_coup_critique-=bonus_lame


        if ('Rage' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Rage'):
                    compteur_Rage+=1
        if(compteur_Rage >= 4):
            bonus_dommages_critiques=0.4
        else:
            bonus_dommages_critiques=0
        self.bonus_de_runes_en_dommages_critiques-=bonus_dommages_critiques


        if ('Precision' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Precision'):
                    compteur_Sniper+=1
        if (compteur_Sniper >= 2):
            if(compteur_Sniper >= 4):
                if(compteur_Sniper == 6):
                    bonus_precision=0.6
                else:
                    bonus_precision=0.4
            else:
                bonus_precision=0.2
        else:
            bonus_precision=0
        self.bonus_de_runes_en_precision-=bonus_precision


        if ('Resistance' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Resistance'):
                    compteur_Illumination+=1
        if (compteur_Illumination >= 2):
            if(compteur_Illumination >= 4):
                if(compteur_Illumination == 6):
                    bonus_resistance=0.6
                else:
                    bonus_resistance=0.4
            else:
                bonus_resistance=0.2
        else:
            bonus_resistance=0
        self.bonus_de_runes_en_resistance-=bonus_resistance


        if ('Vengeance' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Vengeance'):
                    compteur_Vengeance+=1
        if (compteur_Vengeance >= 2):
            if(compteur_Vengeance >= 4):
                if(compteur_Vengeance == 6):
                    bonus_vengeance=0.6
                else:
                    bonus_vengeance=0.4
            else:
                bonus_vengeance=0.2
        else:
            bonus_vengeance=0
        self.bonus_de_runes_en_taux_contre_attaque-=bonus_vengeance


        if ('Volonté' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Volonté'):
                    compteur_Volonte+=1
        if (compteur_Volonte >= 2):
            if(compteur_Volonte >= 4):
                if(compteur_Volonte == 6):
                    bonus_immunite=4
                else:
                    bonus_immunite=3
            else:
                bonus_immunite=2
        else:
            bonus_immunite=0
        if(bonus_immunite!=0):
            self.bonus_de_runes_en_immunite=0
            self.bonus_de_runes_en_tours_immunite=0


        if ('Vampirique' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Vampirique'):
                    compteur_Vampirique+=1
        if(compteur_Illumination >= 4):
            bonus_vol_de_vie=35
        else:
            bonus_vol_de_vie=0
        self.bonus_de_runes_en_vol_de_vie-=bonus_vol_de_vie


        if ('Desespoir' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Desespoir'):
                    compteur_Desespoir+=1
        if(compteur_Desespoir >= 4):
            bonus_chances_de_stun=0.25
        else:
            bonus_chances_de_stun=0
        self.bonus_de_runes_en_chances_de_stun-=bonus_chances_de_stun


        if ('Violence' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Violence'):
                    compteur_Violence+=1
        if(compteur_Violence >= 4):
            bonus_chances_tour_supplementaire=0.22
        else:
            bonus_chances_tour_supplementaire=0
        self.bonus_de_runes_en_chances_tour_supplementaire-=bonus_chances_tour_supplementaire


        if ('Transcendance' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Transcendance'):
                    compteur_Transcendance+=1
        if(compteur_Transcendance == 6):
            bonus_transcendance=0.15
        else:
            bonus_transcendance=0
        self.bonus_de_runes_en_pourcentage_de_pv-=bonus_transcendance
        self.bonus_de_runes_en_pourcentage_de_attaque-=bonus_transcendance
        self.bonus_de_runes_en_pourcentage_de_defense-=bonus_transcendance
        self.bonus_de_runes_en_vitesse-=Arrondir.a_l_unite(bonus_transcendance*self.vitesse)
        self.bonus_de_runes_en_taux_de_coup_critique-=bonus_transcendance
        self.bonus_de_runes_en_dommages_critiques-=bonus_transcendance
        self.bonus_de_runes_en_precision-=bonus_transcendance
        self.bonus_de_runes_en_resistance-=bonus_transcendance


        if ('Extase' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Extase'):
                    compteur_Extase+=1
        if(compteur_Extase == 6):
            self.bonus_de_runes_en_tour_supplementaire-=1


        if ('Destruction' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Destruction'):
                    compteur_Destruction+=1
        if (compteur_Destruction >= 2):
            if(compteur_Destruction >= 4):
                if(compteur_Destruction == 6):
                    bonus_attaque=0.7
                    bonus_vitesse=0.5
                else:
                    bonus_attaque=0.35
                    bonus_vitesse=0.25
            else:
                bonus_attaque=0.1
                bonus_vitesse=0.1
        else:
            bonus_attaque=0
            bonus_vitesse=0
        self.bonus_de_runes_en_pourcentage_de_attaque-=bonus_attaque
        self.bonus_de_runes_en_vitesse-=Arrondir.a_l_unite(bonus_vitesse*self.vitesse)


        if ('Domination' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Domination'):
                    compteur_Domination+=1
        if (compteur_Domination >= 2):
            if(compteur_Domination >= 4):
                if(compteur_Domination == 6):
                    bonus_immortalite=4
                else:
                    bonus_immortalite=3
            else:
                bonus_immortalite=2
        else:
            bonus_immortalite=0
        if(bonus_immortalite!=0):
            self.bonus_de_runes_en_immortalite=0
            self.bonus_de_runes_en_tours_immortalite=0


        if ('Inébranlable' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Inébranlable'):
                    compteur_Inebranlable+=1
        if(compteur_Inebranlable == 6):
            self.bonus_de_runes_en_immunite=0


        if ('Détermination' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Détermination'):
                    compteur_Determination+=1
        if(compteur_Determination == 6):
            self.determination=0


        if ('Incandescence' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Incandescence'):
                    compteur_Incandescence+=0
        if (compteur_Incandescence >= 2):
            if(compteur_Incandescence >= 4):
                if(compteur_Incandescence == 6):
                    bonus_incandescence=4
                else:
                    bonus_incandescence=3
            else:
                bonus_incandescence=2
        else:
            bonus_incandescence=0
        if(bonus_incandescence>0):
            self.incandescence=0
            self.niveau_incandescence=0


        if ('Sublimation' in types_runes_equipees):
            for index in range(len(types_runes_equipees)):
                if (types_runes_equipees[index]=='Sublimation'):
                    compteur_Sublimation+=1
        if (compteur_Sublimation >= 2):
            if(compteur_Sublimation >= 4):
                if(compteur_Sublimation == 6):
                    bonus_recup=0.45
                else:
                    bonus_recup=0.3
            else:
                bonus_recup=0.15
        else:
            bonus_recup=0
        self.bonus_de_runes_en_regeneration-=bonus_recup


        '''
        monstre.pv+=Arrondir.a_l_unite(monstre.bonus_de_runes_en_pv+monstre.pv*monstre.bonus_de_runes_en_pourcentage_de_pv)
        monstre.attaque+=Arrondir.a_l_unite(monstre.bonus_de_runes_en_attaque+monstre.attaque*monstre.bonus_de_runes_en_pourcentage_de_attaque)
        monstre.defense+=Arrondir.a_l_unite(monstre.bonus_de_runes_en_defense+monstre.defense*monstre.bonus_de_runes_en_pourcentage_de_defense)
        monstre.vitesse+=Arrondir.a_l_unite(monstre.bonus_de_runes_en_vitesse)
        monstre.taux_coup_critique+=Arrondir.au_centieme(monstre.bonus_de_runes_en_taux_de_coup_critique)
        monstre.dommages_critiques+=Arrondir.au_centieme(monstre.bonus_de_runes_en_dommages_critiques)
        monstre.resistance+=Arrondir.au_centieme(monstre.bonus_de_runes_en_resistance)
        monstre.precision+=Arrondir.au_centieme(monstre.bonus_de_runes_en_precision)
        '''

        for index in range(len(self.statistiques_actuelles)):
            self.statistiques_actuelles[index]=self.statistiques[index]
        self.actualiser_stats_de_listes_a_simples()














    def calculer_XP_amelioration(self):
        XP_donnee_LV1_min=800
        XP_donnee_LV1_max=1210
        XP_donnee_LV2_min=1760
        XP_donnee_LV2_max=3086
        XP_donnee_LV3_min=3200
        XP_donnee_LV3_max=6204
        XP_donnee_LV4_min=6724
        XP_donnee_LV4_max=13851
        XP_donnee_LV5_min=16000
        XP_donnee_LV5_max=43708
        XP_donnee_LV6_min=44001
        XP_donnee_LV6_max=139356
        XP_donnee_min=[XP_donnee_LV1_min,XP_donnee_LV2_min,XP_donnee_LV3_min,XP_donnee_LV4_min,XP_donnee_LV5_min,XP_donnee_LV6_min]
        XP_donnee_max=[XP_donnee_LV1_max,XP_donnee_LV2_max,XP_donnee_LV3_max,XP_donnee_LV4_max,XP_donnee_LV5_max,XP_donnee_LV6_max]
        if(self.niveau == 1):
            XP_a_recevoir=XP_donnee_min[self.classe-1]
        elif(self.niveau_max_de_la_classe_atteint()):
            XP_a_recevoir=XP_donnee_max[self.classe-1]
        else:
            ecart=XP_donnee_max[self.classe-1]-XP_donnee_min[self.classe-1]
            nb_passages_en_niveau=9+(5*self.classe)
            XP_a_recevoir=XP_donnee_min[self.classe-1]+ecart*((self.niveau-1)/nb_passages_en_niveau)
        
        XP_a_recevoir=Arrondir.a_l_unite(XP_a_recevoir)
        return XP_a_recevoir


    def recevoir_XP(self,XP_gagnee):
        print(self.surnom,'reçoit',XP_gagnee,'points d expérience!!')
        while(XP_gagnee >= self.XP_avant_prochain_niveau and not self.niveau_max_de_la_classe_atteint()):
            XP_gagnee -= self.XP_avant_prochain_niveau
            self.monter_en_niveau()
        if(self.niveau_max_de_la_classe_atteint() == False):
            self.XP_avant_prochain_niveau -= XP_gagnee
            print('Il manque à',self.surnom,self.XP_avant_prochain_niveau,' points d expérience avant le prochain niveau!! \n')


    def trouver_XP_avant_prochain_niveau(self):
        XP_requise_LV1=[460,516,579,650,728,818,918,1029,1155,1296,1455,1631,1831,2054]
        XP_requise_LV2=[552,619,695,779,875,981,1102,1235,1386,1555,1745,1958,2197,2465,2765,3103,3481,3906,4423]
        XP_requise_LV3=[662,743,834,936,1049,1178,1321,1483,1663,1866,2094,2350,2636,2957,3319,3723,4178,4687,5307,6009,6802,7703,8720,9962]
        XP_requise_LV4=[796,892,1002,1124,1261,1415,1587,1781,1998,2243,2515,2823,3167,3553,3987,4473,5019,5631,6376,7219,8172,9254,10476,11969,13673,15619,17844,20386,23495]
        XP_requise_LV5=[952,1068,1199,1344,1509,1693,1899,2131,2392,2682,3010,3378,3789,4252,4770,5352,6006,6738,7628,8638,9779,11072,12535,14321,16360,18690,21350,24392,28113,32404,37348,43048,49617,57188]
        XP_requise_LV6=[1150,1290,1447,1624,1823,2044,2294,2574,2888,3240,3635,4079,4576,5135,5762,6464,7252,8138,9214,10431,11811,13371,15140,17296,19758,22572,25786,29458,33954,39134,45107,51990,59924,69068,76085,83816,92332,101712,112046]
        XP_requise=[XP_requise_LV1,XP_requise_LV2,XP_requise_LV3,XP_requise_LV4,XP_requise_LV5,XP_requise_LV6]
        
        XP_avant_prochain_niveau=XP_requise[self.classe-1][self.niveau-1]
        return XP_avant_prochain_niveau


    def trouver_XP_initiale(self):
        XP_requise_LV1=[460,516,579,650,728,818,918,1029,1155,1296,1455,1631,1831,2054]
        XP_requise_LV2=[552,619,695,779,875,981,1102,1235,1386,1555,1745,1958,2197,2465,2765,3103,3481,3906,4423]
        XP_requise_LV3=[662,743,834,936,1049,1178,1321,1483,1663,1866,2094,2350,2636,2957,3319,3723,4178,4687,5307,6009,6802,7703,8720,9962]
        XP_requise_LV4=[796,892,1002,1124,1261,1415,1587,1781,1998,2243,2515,2823,3167,3553,3987,4473,5019,5631,6376,7219,8172,9254,10476,11969,13673,15619,17844,20386,23495]
        XP_requise_LV5=[952,1068,1199,1344,1509,1693,1899,2131,2392,2682,3010,3378,3789,4252,4770,5352,6006,6738,7628,8638,9779,11072,12535,14321,16360,18690,21350,24392,28113,32404,37348,43048,49617,57188]
        XP_requise_LV6=[1150,1290,1447,1624,1823,2044,2294,2574,2888,3240,3635,4079,4576,5135,5762,6464,7252,8138,9214,10431,11811,13371,15140,17296,19758,22572,25786,29458,33954,39134,45107,51990,59924,69068,76085,83816,92332,101712,112046]
        XP_requise=[XP_requise_LV1,XP_requise_LV2,XP_requise_LV3,XP_requise_LV4,XP_requise_LV5,XP_requise_LV6]
        XP_avant_prochain_niveau=XP_requise[self.classe-1][self.niveau-1]
        return XP_avant_prochain_niveau


    def niveau_max_de_la_classe_atteint(self):
        if(self.niveau >= (10+5*self.classe)):
            summum=True
        else:
            summum=False
        return summum






    def monter_en_niveau(self):
        self.niveau+=1
        self.malus_famille_de_runes()
        print('Félicitations!! ',self.surnom,self.attribut,' est désormais niveau ',self.niveau,'!!')
        str(input(' > '))
        
        if(self.niveau_max_de_la_classe_atteint()):
            print(self.surnom,' a atteint le niveau max de sa classe et doit désormais évoluer pour pouvoir passer en niveau!!')
            self.XP_avant_prochain_niveau=999999999
        else:
            self.XP_avant_prochain_niveau=self.trouver_XP_avant_prochain_niveau()
            nb_passages_niveau=9+5*self.classe
            
            if(self.classe == 1):
                pv_min=self.pv_min_1
                attaque_min=self.attaque_min_1
                defense_min=self.defense_min_1
                pv_max=self.pv_max_1
                attaque_max=self.attaque_max_1
                defense_max=self.defense_max_1
            if(self.classe == 2):
                pv_min=self.pv_min_2
                attaque_min=self.attaque_min_2
                defense_min=self.defense_min_2
                pv_max=self.pv_max_2
                attaque_max=self.attaque_max_2
                defense_max=self.defense_max_2
            if(self.classe == 3):
                pv_min=self.pv_min_3
                attaque_min=self.attaque_min_3
                defense_min=self.defense_min_3
                pv_max=self.pv_max_3
                attaque_max=self.attaque_max_3
                defense_max=self.defense_max_3
            if(self.classe == 4):
                pv_min=self.pv_min_4
                attaque_min=self.attaque_min_4
                defense_min=self.defense_min_4
                pv_max=self.pv_max_4
                attaque_max=self.attaque_max_4
                defense_max=self.defense_max_4
            if(self.classe == 5):
                pv_min=self.pv_min_5
                attaque_min=self.attaque_min_5
                defense_min=self.defense_min_5
                pv_max=self.pv_max_5
                attaque_max=self.attaque_max_5
                defense_max=self.defense_max_5
            if(self.classe == 6):
                pv_min=self.pv_min_6
                attaque_min=self.attaque_min_6
                defense_min=self.defense_min_6
                pv_max=self.pv_max_6
                attaque_max=self.attaque_max_6
                defense_max=self.defense_max_6

            bonus_pv=Arrondir.a_l_unite((pv_max-pv_min)/nb_passages_niveau)
            bonus_attaque=Arrondir.a_l_unite((attaque_max-attaque_min)/nb_passages_niveau)
            bonus_defense=Arrondir.a_l_unite((defense_max-defense_min)/nb_passages_niveau)
            #print('\n\n Bonus PV : ',bonus_pv,'\n Bonus attaque : ',bonus_attaque,'\n Bonus defense : ',bonus_defense,'\n\n')
            
            self.pv+=bonus_pv
            self.attaque+=bonus_attaque
            self.defense+=bonus_defense
            if(self.niveau_max_de_la_classe_atteint()==True):
                self.pv=pv_max
                self.attaque=attaque_max
                self.defense=defense_max
            if(self.pv > 0):
                self.pv_actuels+=bonus_pv
            self.attaque_actuelle+=bonus_attaque
            self.defense_actuelle+=bonus_defense

        self.actualiser_stats_de_simples_a_listes()
        self.bonus_famille_de_runes()
        ''' Actualise le gain en pourcentage de pv des runes et les applique '''
        self.actualiser_stats_de_simples_a_listes()
        print(self)


    def monter_en_niveau_sans_affichage(self):
        self.niveau+=1
        self.malus_famille_de_runes()
        if(self.niveau_max_de_la_classe_atteint()):
            self.XP_avant_prochain_niveau=999999999
        else:
            self.XP_avant_prochain_niveau=self.trouver_XP_avant_prochain_niveau()
            nb_passages_niveau=9+5*self.classe
            
            if(self.classe == 1):
                pv_min=self.pv_min_1
                attaque_min=self.attaque_min_1
                defense_min=self.defense_min_1
                pv_max=self.pv_max_1
                attaque_max=self.attaque_max_1
                defense_max=self.defense_max_1
            if(self.classe == 2):
                pv_min=self.pv_min_2
                attaque_min=self.attaque_min_2
                defense_min=self.defense_min_2
                pv_max=self.pv_max_2
                attaque_max=self.attaque_max_2
                defense_max=self.defense_max_2
            if(self.classe == 3):
                pv_min=self.pv_min_3
                attaque_min=self.attaque_min_3
                defense_min=self.defense_min_3
                pv_max=self.pv_max_3
                attaque_max=self.attaque_max_3
                defense_max=self.defense_max_3
            if(self.classe == 4):
                pv_min=self.pv_min_4
                attaque_min=self.attaque_min_4
                defense_min=self.defense_min_4
                pv_max=self.pv_max_4
                attaque_max=self.attaque_max_4
                defense_max=self.defense_max_4
            if(self.classe == 5):
                pv_min=self.pv_min_5
                attaque_min=self.attaque_min_5
                defense_min=self.defense_min_5
                pv_max=self.pv_max_5
                attaque_max=self.attaque_max_5
                defense_max=self.defense_max_5
            if(self.classe == 6):
                pv_min=self.pv_min_6
                attaque_min=self.attaque_min_6
                defense_min=self.defense_min_6
                pv_max=self.pv_max_6
                attaque_max=self.attaque_max_6
                defense_max=self.defense_max_6

            bonus_pv=Arrondir.a_l_unite((pv_max-pv_min)/nb_passages_niveau)
            bonus_attaque=Arrondir.a_l_unite((attaque_max-attaque_min)/nb_passages_niveau)
            bonus_defense=Arrondir.a_l_unite((defense_max-defense_min)/nb_passages_niveau)

            self.pv+=bonus_pv
            self.attaque+=bonus_attaque
            self.defense+=bonus_defense
            if(self.niveau_max_de_la_classe_atteint()):
                self.pv=pv_max
                self.attaque=attaque_max
                self.defense=defense_max
            if(self.pv > 0):
                self.pv_actuels+=bonus_pv
            self.attaque_actuelle+=bonus_attaque
            self.defense_actuelle+=bonus_defense

        self.actualiser_stats_de_simples_a_listes()
        self.bonus_famille_de_runes()
        self.actualiser_stats_de_simples_a_listes()




    ''' Tester si ça marche avec plusieurs évolutions successives mais j'en doute '''
    ''' Sauvegarder aussi l'écart entre la classe actuelle et la classe après reset '''
    ''' Gestion de l'équipement différente puisque désormais non relié directement aux stats du monstres '''
    def evoluer(self):
        # Le monstre va être reset lors de son évolution.
        # Pas besoin donc de faire un self.malus_famille_de_runes()
        equipement=[]
        for index in range(6):
            equipement.append(self.desequiper_sans_affichage(index))            
        attribut=self.attribut

        while(self.attribut!=attribut):
            self=self.reset_monstre(self.nom)

        if(self.classe == 1):
            pv_min=self.pv_min_2
            attaque_min=self.attaque_min_2
            defense_min=self.defense_min_2
        if(self.classe == 2):
            pv_min=self.pv_min_3
            attaque_min=self.attaque_min_3
            defense_min=self.defense_min_3
        if(self.classe == 3):
            pv_min=self.pv_min_4
            attaque_min=self.attaque_min_4
            defense_min=self.defense_min_4
        if(self.classe == 4):
            pv_min=self.pv_min_5
            attaque_min=self.attaque_min_5
            defense_min=self.defense_min_5
        if(self.classe == 5):
            pv_min=self.pv_min_6
            attaque_min=self.attaque_min_6
            defense_min=self.defense_min_6

        self.pv = pv_min
        self.pv_actuels = pv_min
        self.pv_max_donjons = pv_min

        self.attaque = attaque_min
        self.attaque_actuelle = attaque_min
        self.attaque_max_donjons = attaque_min

        self.defense = defense_min
        self.defense_actuelle = defense_min
        self.defense_max_donjons = defense_min

        self.niveau=1
        self.classe+=1
        self.XP_avant_prochain_niveau=self.trouver_XP_initiale()
                
        self.actualiser_stats_de_simples_a_listes()

        for index in range(6):
            if(equipement[index] != 0):
                equipement[index].equiper_sans_affichage(self,index)
        
        self.bonus_famille_de_runes()

        self.bonus_de_runes_en_pv+=Arrondir.a_l_unite(self.pv*self.bonus_de_runes_en_pourcentage_de_pv)
        self.bonus_de_runes_en_attaque+=Arrondir.a_l_unite(self.attaque*self.bonus_de_runes_en_pourcentage_de_attaque)
        self.bonus_de_runes_en_defense+=Arrondir.a_l_unite(self.defense*self.bonus_de_runes_en_pourcentage_de_defense)
        
        self.pv_actuels=self.pv
        self.attaque_actuelle=self.attaque
        self.defense_actuelle=self.defense
        self.vitesse_actuelle=self.vitesse
        self.taux_coup_critique_actuel=self.taux_coup_critique
        self.dommages_critiques_actuels=self.dommages_critiques
        self.resistance_actuelle=self.resistance
        self.precision_actuelle=self.precision
    
        self.actualiser_stats_de_simples_a_listes()


















    def calcul_dommages(self,multiplicateur,bonus_skill,cible):
        degats_infliges=self.attaque_actuelle*multiplicateur*(1+bonus_skill)
        intensite_coup=random.randint(1,100)
        if(self.priorite_elementaire(cible)):
            if(intensite_coup>=100-(15+100*self.taux_coup_critique_actuel)):
                degats_infliges+=Arrondir.a_l_unite(self.attaque_actuelle*multiplicateur*self.dommages_critiques_actuels)
            else:
                degats_infliges+=Arrondir.a_l_unite(0.3*degats_infliges)
        elif(cible.priorite_elementaire(self)):
            if(intensite_coup<=50+100*self.taux_coup_superficiel):
                degats_infliges-=Arrondir.a_l_unite(0.3*degats_infliges)
        cible.nb_coups_subis+=1
        return degats_infliges


    def reduction_dommages(self,degats_infliges):
        facteur_reduction_de_degats=1000/(1140+3.5*self.defense_actuelle)
        degats_infliges=Arrondir.a_l_unite(degats_infliges*facteur_reduction_de_degats)
        ''' Ne pas oublier d'enlever la réduction de dégâts naturelle du monstre attaqué '''
        degats_infliges-=self.reduction_de_degats*degats_infliges
        return degats_infliges


    def affichage_du_type_de_coup(self,multiplicateur,bonus_skill,degats,cible):
        type_de_coup='Normal'
        degats_infliges=self.attaque_actuelle*multiplicateur*(1+bonus_skill)
        
        if(degats == (degats_infliges-Arrondir.a_l_unite(0.3*degats_infliges))):
            type_de_coup='Superficiel'
            print('Coup superficiel!!')
        elif(degats == (degats_infliges+Arrondir.a_l_unite(self.attaque_actuelle*multiplicateur*self.dommages_critiques_actuels))):
            type_de_coup='Critique'
            print('Coup critique!!')
        elif(degats == (degats_infliges+Arrondir.a_l_unite(0.3*degats_infliges))):
            type_de_coup='Dévastateur'
            print('Coup dévastateur!!')
        return type_de_coup


    def debut_de_tour(self):
        if(self.tours_regeneration > 0):
            if(self.perturbation_recup > 0):
                self.tours_perturbation_recup-=1
            else:
                montant=Arrondir.a_l_unite(self.regeneration*self.pv_max_donjons)
                pv_actuels_tmp=self.pv_actuels
                if(montant+self.pv_actuels >= self.pv_max_donjons):
                    self.pv_actuels=self.pv_max_donjons
                    print(self.surnom,self.attribut,'récupère',self.pv_max_donjons-pv_actuels_tmp,'points de vie grâce à sa régénération!!\n')
                else:
                    self.pv_actuels+=montant
                    print(self.surnom,self.attribut,'récupère',montant,'points de vie grâce à sa régénération!!\n')
        
        elif(self.regeneration > 0):
            if(self.perturbation_recup <= 0):
                montant=Arrondir.a_l_unite(self.regeneration*self.pv_max_donjons)
                pv_actuels_tmp=self.pv_actuels
                if(montant+self.pv_actuels >= self.pv_max_donjons):
                    self.pv_actuels=self.pv_max_donjons
                    print(self.surnom,self.attribut,'récupère',self.pv_max_donjons-pv_actuels_tmp,'points de vie grâce à sa régénération!!\n')
                else:
                    self.pv_actuels+=montant
                    print(self.surnom,self.attribut,'récupère',montant,'points de vie grâce à sa régénération!!\n')
        
        if(self.bombe > 0):
            if(self.tours_avant_explosion == 0):
                self.pv_actuels-=self.degats_des_bombes
                self.bombe=0
                self.stun=1
        if(self.stun > 0):
            self.peut_jouer=0
            self.stun=0
        if(self.gel > 0):
            self.peut_jouer=0
            self.gel=0
        if(self.sommeil > 0):
            self.peut_jouer=0
            self.tours_sommeil-=1
            if(self.tours_sommeil <= 0):
                self.sommeil=0
        if(self.intensite_degats_continus > 0):
            if(self.pv_actuels > 0):
                self.pv_actuels-=math.floor(self.marques_degats_continus*(0.05*self.pv_max_donjons))
                print(self.surnom,' perd ',math.floor(self.marques_degats_continus*(0.05*self.pv_max_donjons)),' PV à cause des dégâts continus!! \n')
            self.intensite_degats_continus-=1
        if(self.intensite_degats_continus == 0):
            self.marques_degats_continus=0

        if(self.tours_bonus_attaque > 0):
            self.tours_bonus_attaque-=1
            if(self.tours_bonus_attaque == 0):
                if(self.tours_malus_attaque <= 0):
                    self.attaque_actuelle=self.attaque_max_donjons
                else:
                    self.attaque_actuelle=self.attaque_max_donjons-(0.5*self.attaque_actuelle)
        
        if(self.tours_bonus_defense > 0):
            self.tours_bonus_defense-=1
            if(self.tours_bonus_defense == 0):
                if(self.tours_malus_defense <= 0):
                    self.defense_actuelle=self.defense_max_donjons
                else:
                    self.defense_actuelle=self.defense_max_donjons-(0.7*self.defense_actuelle)
        
        if(self.tours_bonus_vitesse > 0):
            self.tours_bonus_vitesse-=1
            if(self.tours_bonus_vitesse == 0):
                if(self.tours_malus_vitesse <= 0):
                    self.vitesse_actuelle=self.vitesse_max_donjons
                else:
                    self.vitesse_actuelle=self.vitesse_max_donjons-(0.3*self.vitesse_actuelle)
        
        if(self.tours_bonus_taux_coup_critique > 0):
            self.tours_bonus_taux_coup_critique-=1
            if(self.tours_bonus_taux_coup_critique == 0):
                self.taux_coup_critique_actuel=self.taux_coup_critique_max_donjons
        
        if(self.tours_regeneration > 0):
            self.tours_regeneration-=1
            if(self.tours_regeneration == 0):
                self.regeneration=0
        
        if(self.tours_contre_attaque > 0):
            self.tours_contre_attaque-=1
            if(self.tours_contre_attaque == 0):
                self.contre_attaque=0
        
        if(self.taux_contre_attaque > 0):
            reussite_effet=(random.randint(1,100))/100
            if(reussite_effet <= self.taux_contre_attaque):
                self.contre_attaque=1
                self.tours_contre_attaque=max(1,self.tours_contre_attaque)
        
        if(self.tours_immunite > 0):
            self.tours_immunite-=1
            if(self.tours_immunite == 0):
                self.immunite=0
        
        if(self.tours_invincibilite > 0):
            self.tours_invincibilite-=1
            if(self.tours_invincibilite == 0):
                self.invincibilite=0
        
        if(self.tours_immortalite > 0):
            self.tours_immortalite-=1
            if(self.tours_immortalite == 0):
                self.immortalite=0
        
        if(self.tours_reflexion_dommages > 0):
            self.tours_reflexion_dommages-=1
            if(self.tours_reflexion_dommages == 0):
                self.reflexion_dommages=0
        
        if(self.tours_endurance > 0):
            self.tours_endurance-=1
            if(self.tours_endurance == 0):
                self.endurance=0
        
        if(self.tours_provocation > 0):
            self.tours_provocation-=1
            if(self.tours_provocation == 0):
                self.provocation=0

        if(self.tours_malus_attaque > 0):
            self.tours_malus_attaque-=1
            if(self.tours_malus_attaque == 0):
                if(self.tours_bonus_attaque <= 0):
                    self.attaque_actuelle=self.attaque_max_donjons
                else:
                    self.attaque_actuelle=self.attaque_max_donjons+(0.5*self.attaque_actuelle)
        
        if(self.tours_malus_defense > 0):
            self.tours_malus_defense-=1
            if(self.tours_malus_defense == 0):
                if(self.tours_bonus_defense <= 0):
                    self.defense_actuelle=self.defense_max_donjons
                else:
                    self.defense_actuelle=self.defense_max_donjons+(0.7*self.defense_actuelle)
        
        if(self.tours_malus_vitesse > 0):
            self.tours_malus_vitesse-=1
            if(self.tours_malus_vitesse == 0):
                if(self.tours_bonus_vitesse <= 0):
                    self.vitesse_actuelle=self.vitesse_max_donjons
                else:
                    self.vitesse_actuelle=self.vitesse_max_donjons+(0.3*self.vitesse_actuelle)
        
        if(self.tours_bonus_taux_coup_superficiel > 0):
            self.tours_bonus_taux_coup_superficiel-=1
            if(self.tours_bonus_taux_coup_superficiel == 0):
                self.bonus_taux_coup_superficiel=0
        
        if(self.tours_immunite_aux_bonus > 0):
            self.tours_immunite_aux_bonus-=1
            if(self.tours_immunite_aux_bonus == 0):
                self.immunite_aux_bonus=0
        
        if(self.tours_provoque > 0):
            self.tours_provoque-=1
            if(self.tours_provoque == 0):
                self.provoque=0
        
        if(self.tours_perturbation_recup > 0):
            self.tours_perturbation_recup-=1
            if(self.tours_perturbation_recup == 0):
                self.perturbation_recup=0
        
        if(self.tours_silencieux > 0):
            self.tours_silencieux-=1
            if(self.tours_silencieux == 0):
                self.silencieux=0
        
        if(self.tours_marque > 0):
            self.tours_marque-=1
            if(self.tours_marque == 0):
                self.marque=0
        
        if(self.tours_sans_passif > 0):
            self.tours_sans_passif-=1
            if(self.tours_sans_passif == 0):
                self.sans_passif=0
        
        if(self.tours_sans_resurrection > 0):
            self.tours_sans_resurrection-=1
            if(self.tours_sans_resurrection == 0):
                self.sans_resurrection=0

    def appliquer_passifs_fin_de_tour(self,cible,team_attaquant,team_cible):
        if(cible.pv_actuels > 0):
            for index in range(team_cible.len):
                if(team_cible.membres[index].nom == 'Elfe' and team_cible.membres[index].attribut == 'Ténèbres' and team_cible.membres[index].sans_passif <= 0):
                    team_cible.membres[index].contre_attaque(team_cible.leader)

            if((cible.nom == 'LoupGarou' or cible.nom == 'Loup Garou') and cible.attribut == 'Ténèbres' and cible.sans_passif <= 0):
                cible.retour_de_coup(self)
            if(cible.nom == 'Elfe' and cible.attribut == 'Vent' and cible.sans_passif <= 0):
                cible.fin_mouvement_esquive(team_cible)
        
        else:
            # Si cible.pv_actuels <= 0 :
            if(cible.nom == 'Vampire' and cible.attribut == 'Lumière' and cible.sans_passif <= 0):
                cible.immortalite(team_cible)

        if((self.nom == 'ChevalierMagique' or self.nom == 'Chevalier Magique') and self.attribut == 'Lumière' and self.sans_passif <= 0):
            self.altruisme(cible,team_attaquant)
        if(self.nom == 'Phénix' and self.attribut == 'Ténèbres'):
            self.enfer(cible)
        if(cible.nom == 'Phénix' and cible.attribut == 'Feu'):
            self.resurrection(team_cible)


    def appliquer_passifs_fin_de_tour_si_pas_offense(self,team_attaquant):
        if(self.nom == 'Phénix' and self.attribut == 'Feu'):
            self.eternite(team_attaquant)


    ''' ATTENTION DEFINITION DE TEAM MODIFIEE '''
    def action_allies(self,team_allies,team_ennemis):
        ''' ACTUALISER TOUTES LES CAPACITES ANORMALES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! '''
        ''' FONCTION A OPTIMISER... Faire beaucoup plus de fonctions auxiliaires!!!! '''

        capacites_anormales=[SoldatSquelette.slash,ChauveSouris.ultrason,Lutin.deceleration,OursDeGuerre.rugissement,Salamandre.tremblement,Chevalier.abnegation,OursDeGuerre.abnegation,Elementaire.renforcement,Garuda.resurgir,Garuda.lumiere,Esprit.guerison,Esprit.sphere_spirituelle,Fee.soin,Fee.double_fleche,Fee.pluie_douleur,Fee.benediction,DameHarpie.plumes,DameHarpie.danse,Inugami.coop,Inugami.hurlement,Golem.corps_de_lave,Golem.corps_de_glace,Golem.mur_de_fer,Mastodonte.pluie_de_gravats,Mastodonte.armure_de_glace,Serpent.tsunami,Serpent.orage,Griffon.tornade,Inferno.deflagration,Inferno.orage,Elfe.fleches,Elfe.pluie,ChevalierMagique.projectiles,ChevalierMagique.drain,Griffon.acceleration,Inferno.adrenaline,OursDeCombat.cri,Elfe.strategie,ChevalierMagique.combo,ChevalierMagique.tempete,ChevalierMagique.vortex,Phenix.blizzard,Phenix.tempete,Phenix.purification,Sylphe.tourbillon,Sylphe.nuit,Sylphe.cyclone,Sylphe.blizzard,Sylphe.phenix,Sylphide.bourrasque,Sylphide.bourrasque2,Sylphide.conjuration,Sylphide.bouclier,Sylphide.benediction,Sylphide.benediction_lumiere]
        capacites_multicibles=[SoldatSquelette.slash,ChauveSouris.ultrason,Lutin.deceleration,OursDeGuerre.rugissement,Salamandre.tremblement,Chevalier.abnegation,Fee.double_fleche,Fee.pluie_douleur,DameHarpie.plumes,Golem.corps_de_lave,Golem.corps_de_glace,Mastodonte.pluie_de_gravats,Serpent.tsunami,Serpent.orage,Griffon.tornade,Inferno.deflagration,Inferno.orage,Elfe.fleches,Elfe.pluie,ChevalierMagique.projectiles,ChevalierMagique.drain,Phenix.blizzard,Phenix.tempete,Phenix.purification,Sylphe.tourbillon,Sylphe.nuit,Sylphe.cyclone,Sylphe.blizzard,Sylphe.phenix]
        capacites_multicibles_multi_equipes=[Sylphide.bourrasque,Sylphide.bourrasque2] # (sylphe,equipe_ennemie,equipe_alliee)
        capacites_hit_multicibles=[ChevalierMagique.combo,ChevalierMagique.tempete]

        capacites_soin_allie=[Esprit.guerison,Fee.soin,Sylphide.benediction]
        capacites_soin_allie_avec_hit=[Esprit.sphere_spirituelle,ChevalierMagique.vortex] # (esprit,Team_allies,cible)
        capacites_protection_allie=[]
        capacites_renforcement_allie=[Garuda.resurgir]
        capacites_resurrection_allie=[Garuda.lumiere] # Prend Team_allies comme argument

        capacites_renforcement_perso=[OursDeGuerre.abnegation,Elementaire.renforcement,Golem.mur_de_fer,Mastodonte.armure_de_glace]
        capacites_renforcement_equipe=[Fee.benediction,DameHarpie.danse,Inugami.hurlement,Griffon.acceleration,Inferno.adrenaline,OursDeCombat.cri,Elfe.strategie,Sylphide.benediction_lumiere,Sylphide.bouclier,Sylphide.conjuration] # Same
        capacites_attaque_en_groupe=[Inugami.coop] # (inugami,Team_allies,cible)

        passifs_debut_de_tour=[Serpent.renforcement,Elfe.mouvement_esquive,ChevalierMagique.feu_vengeur]
        passifs_fin_de_tour=[Chevalier.urgence,Golem.barriere,Mastodonte.peau_dure,Elfe.fin_mouvement_esquive,Vampire.soif_de_sang]

        self.tour_supplementaire_tmp+=self.tour_supplementaire
        if(self.chances_tour_supplementaire > 0):
            reussite_effet=(random.randint(1,100))/100
            if(reussite_effet <= self.chances_tour_supplementaire):
                self.tour_supplementaire_tmp+=1

        # La fonction graphism sera utilisée pour la partie gauche de la fenêtre
        # La fonction graphism_simple sera utilisée pour la partie droite de la fenêtre 
        dimensions_fenetre = [2*617,480]
        fenetre = initialisation_fenetre(dimensions_fenetre)

        message = "C'est au tour de " + self.surnom + " " + self.attribut + " : "
        graphism(fenetre,dimensions_fenetre,team_ennemis,[618,[message]])
        # print("C'est au tour de ", self.surnom, self.attribut, " : ", "\n")
        while(self.tour_supplementaire_tmp >= 0):
            self.debut_de_tour()
            if(self.pv_actuels > 0):
                if(self.peut_jouer == 1):
                    if(team_ennemis.is_alive()):
                        if((self.presence_passif_1 == 1) and (self.sans_passif <= 0)  and (self.passif_1 in passifs_debut_de_tour)):
                            self.passif_1(team_allies)
                        if((self.presence_passif_2 == 1) and (self.sans_passif <= 0)  and (self.passif_2 in passifs_debut_de_tour)):
                            self.passif_2(team_allies)
                        if(self.provoque <= 0):
                            # Réinitialise les positions possibles pour les ennemis
                            # Doit surement pouvoir s'optimiser avec des .pop et des .append...
                            place_leader=0
                            place_membre_1=1
                            place_membre_2=2

                            if(team_ennemis.len == 1):
                                positions_ennemis=['du centre']
                                possibilites_cible=[0]
                            
                            elif(team_ennemis.len == 2):
                                if(team_ennemis.membres[0].pv_actuels <= 0):
                                    positions_ennemis=['de droite']
                                    possibilites_cible=[0]
                                    place_leader=3
                                    place_membre_1=0
                                elif(team_ennemis.membres[1].pv_actuels <= 0):
                                    positions_ennemis=['de gauche']
                                    possibilites_cible=[0]
                                    place_membre_1=3
                                else:
                                    positions_ennemis=['de gauche','de droite']
                                    possibilites_cible=[0,1]
                            
                            elif(team_ennemis.len == 3):
                                if(team_ennemis.membres[0].pv_actuels <= 0 and team_ennemis.membres[1].pv_actuels <= 0):
                                    positions_ennemis=['de droite']
                                    possibilites_cible=[0]
                                    place_leader=3
                                    place_membre_1=3
                                    place_membre_2=0
                                elif(team_ennemis.membres[0].pv_actuels <=0 and team_ennemis.membres[2].pv_actuels <= 0):
                                    positions_ennemis=['du centre']
                                    possibilites_cible=[0]
                                    place_leader=3
                                    place_membre_1=0
                                    place_membre_2=3
                                elif(team_ennemis.membres[1].pv_actuels <= 0 and team_ennemis.membres[2].pv_actuels <= 0):
                                    positions_ennemis=['de gauche']
                                    possibilites_cible=[0]
                                    place_leader=0
                                    place_membre_1=3
                                    place_membre_2=3
                                elif(team_ennemis.membres[0].pv_actuels <= 0):
                                    positions_ennemis=['du centre','de droite']
                                    possibilites_cible=[0,1]
                                    place_leader=3
                                    place_membre_1=0
                                    place_membre_2=1
                                elif(team_ennemis.membres[1].pv_actuels <= 0):
                                    positions_ennemis=['de gauche','de droite']
                                    possibilites_cible=[0,1]
                                    place_leader=0
                                    place_membre_1=3
                                    place_membre_2=1
                                elif(team_ennemis.membres[2].pv_actuels <= 0):
                                    positions_ennemis=['de gauche','du centre']
                                    possibilites_cible=[0,1]
                                    place_leader=0
                                    place_membre_1=1
                                    place_membre_2=3
                                else:
                                    positions_ennemis=['de gauche','du centre','de droite']
                                    possibilites_cible=[0,1,2]
                            
                            '''
                            if(place_leader < 3):
                                print(team_ennemis.membres[0].surnom,positions_ennemis[place_leader],' = ',place_leader,'(',team_ennemis.membres[0].pv_actuels,'PV restants)')
                            if(team_ennemis.len > 1 and place_membre_1 < 3):
                                print(team_ennemis.membres[1].surnom,positions_ennemis[place_membre_1],' = ',place_membre_1,'(',team_ennemis.membres[1].pv_actuels,'PV restants)')
                            if(team_ennemis.len > 2 and place_membre_2 < 3):
                                print(team_ennemis.membres[2].surnom,positions_ennemis[place_membre_2],' = ',place_membre_2,'(',team_ennemis.membres[2].pv_actuels,'PV restants)')
                            '''

                            retour_choix_capacite_speciale = self.choisir_capacite_speciale(fenetre,dimensions_fenetre,team_ennemis,team_allies)

                            capacite_choisie = retour_choix_capacite_speciale[0]
                            indice_capacite_choisie = retour_choix_capacite_speciale[1]
                            liste_de_messages = retour_choix_capacite_speciale[2]

                            if((capacite_choisie not in capacites_anormales) or (capacite_choisie in capacites_soin_allie_avec_hit) or (capacite_choisie in capacites_attaque_en_groupe) or (capacite_choisie in capacites_hit_multicibles)):
                                '''
                                entree=input('Quelle cible voulez-vous attaquer ? ')
                                while(not Security.is_decimal(entree)):
                                    entree=input('Quelle cible voulez-vous attaquer ? ')
                                indice_cible=int(entree)
                                while(indice_cible not in possibilites_cible):
                                    entree=input('Quelle cible voulez-vous attaquer ? ')
                                    while(not Security.is_decimal(entree)):
                                        entree=input('Quelle cible voulez-vous attaquer ? ')
                                    indice_cible=int(entree)
                                '''
                                indice_cible = graphism(fenetre,dimensions_fenetre,team_ennemis, [1,indice_capacite_choisie,liste_de_messages])
                                # print('\n\n Indice cible : ',indice_cible,'\n\n')

                                '''
                                if(indice_cible == place_leader):
                                    cible=team_ennemis.membres[0]
                                elif(indice_cible == place_membre_1):
                                    cible=team_ennemis.membres[1]
                                elif(indice_cible == place_membre_2):
                                    cible=team_ennemis.membres[2]
                                '''
                                cible = team_ennemis.membres[indice_cible]


                                pv_avant_degats=cible.pv_actuels
                                if ((capacite_choisie not in capacites_soin_allie_avec_hit) and (capacite_choisie not in capacites_attaque_en_groupe) and (capacite_choisie not in capacites_hit_multicibles)):
                                    capacite_choisie(self,cible)
                                elif(capacite_choisie in capacites_hit_multicibles):
                                    capacite_choisie(self,team_ennemis,cible)
                                else:
                                    capacite_choisie(self,team_allies,cible)
                                    
                                if(cible.reflexion_dommages > 0):
                                    degats_subis=pv_avant_degats-cible.pv_actuels
                                    degats_renvoyes=Arrondir.a_l_unite(cible.pourcentage_reflexion_dommages*degats_subis)
                                    cible.pv_actuels+=degats_renvoyes # oui c'est bien un +
                                    if(self.immortalite <= 0):
                                        print('\n',self.surnom,self.attribut,' reçoit la réflexion des dégâts!!')
                                        print(self.surnom,self.attribut,' subit ',degats_renvoyes,' points de dégâts!!')
                                        self.pv_actuels-=degats_renvoyes
                                    else:
                                        print(self.surnom,self.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                                    if(self.pv_actuels <= 0):
                                        print(self.surnom,self.attribut,' est mort!! \n')
                                    else:
                                        print('Il reste ',self.pv_actuels,' point(s) de vie sur',self.pv_max_donjons,' à ',self.surnom,self.attribut,'!! \n')
                                if(cible.contre_attaque > 0 and cible.pv_actuels > 0):
                                    if (degats_subis <= 0):
                                        degats_subis=1
                                    print('\n',cible.surnom,cible.attribut,' effectue une contre-attaque sur ',self.surnom,self.attribut,'!!')
                                    if(self.immortalite <= 0):
                                        pv_attaquant_avant_dommages=self.pv_actuels
                                        cible.capacite1(cible,self)
                                        ecart=self.pv_actuels-pv_attaquant_avant_dommages
                                        self.pv_actuels+=Arrondir.a_l_unite(0.25*ecart) # seulement 75% des dégâts sont subis
                                    else:
                                        print(self.surnom,self.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                                    if(self.pv_actuels <= 0):
                                        print(self.surnom,self.attribut,' est mort!! \n')
                                    else:
                                        print('Il reste ',self.pv_actuels,' point(s) de vie sur',self.pv_max_donjons,' à ',self.surnom,self.attribut,'!! \n')

                                self.appliquer_passifs_fin_de_tour(cible,team_allies,team_ennemis)

                            else:
                                if((capacite_choisie in capacites_soin_allie) or (capacite_choisie in capacites_protection_allie) or (capacite_choisie in capacites_renforcement_allie)):
                                    possibilites_choix_allie=[]
                                    for index in range(team_allies.len):
                                        if(team_allies.membres[index].pv_actuels > 0):
                                            print('Il reste ',team_allies.membres[index].pv_actuels,' PV à l allié ',index,':',team_allies.membres[index].surnom,team_allies.membres[index].attribut,' sur ',team_allies.membres[index].pv_max_donjons)
                                            possibilites_choix_allie.append(index)
                                            
                                    if(capacite_choisie in capacites_soin_allie):
                                        entree=input('Quel allié voulez-vous soigner ? ')
                                        while(not Security.is_decimal(entree)):
                                            entree=input('Quel allié voulez-vous soigner ? ')
                                        choix=int(entree)
                                        while(choix not in possibilites_choix_allie):
                                            entree=input('Quel allié voulez-vous soigner ? ')
                                            while(not Security.is_decimal(entree)):
                                                entree=input('Quel allié voulez-vous soigner ? ')
                                            choix=int(entree)
                                        capacite_choisie(self,team_allies.membres[choix])
                                        
                                    elif(capacite_choisie in capacites_protection_allie):
                                        entree=input('Quel allié voulez-vous protéger ? ')
                                        while(not Security.is_decimal(entree)):
                                            entree=input('Quel allié voulez-vous protéger ? ')
                                        choix=int(entree)
                                        while(choix not in possibilites_choix_allie):
                                            entree=input('Quel allié voulez-vous protéger ? ')
                                            while(not Security.is_decimal(entree)):
                                                entree=input('Quel allié voulez-vous protéger ? ')
                                            choix=int(entree)
                                        capacite_choisie(self,team_allies.membres[choix])
                                            
                                    else:
                                        entree=input('Quel allié voulez-vous renforcer ? ')
                                        while(not Security.is_decimal(entree)):
                                            entree=input('Quel allié voulez-vous renforcer ? ')
                                        choix=int(entree)
                                        while(choix not in possibilites_choix_allie):
                                            entree=input('Quel allié voulez-vous renforcer ? ')
                                            while(not Security.is_decimal(entree)):
                                                entree=input('Quel allié voulez-vous renforcer ? ')
                                            choix=int(entree)
                                        capacite_choisie(self,team_allies.membres[choix])

                                if(capacite_choisie in capacites_renforcement_perso):
                                    capacite_choisie(self)

                                if((capacite_choisie in capacites_resurrection_allie) or (capacite_choisie in capacites_renforcement_equipe)):
                                    capacite_choisie(team_allies)

                                if(capacite_choisie in capacites_multicibles):
                                    capacite_choisie(self,team_ennemis)

                                if(capacite_choisie in capacites_multicibles_multi_equipes):
                                    capacite_choisie(self,team_ennemis,team_allies)

                        else:
                            for index in range(team_ennemis.len):
                                if(team_ennemis.membres[index].indice_provocation > 0):
                                    cible=team_ennemis.membres[index]
                            else:
                                possibilites_provocation=[]
                                for index in range(team_ennemis.len):
                                    if(team_ennemis.membres[index].pv_actuels > 0):
                                        possibilites_provocation.append(index)
                                indice_provocation=possibilites_provocation[random.randint(0,len(possibilites_provocation)-1)]
                                cible=team_ennemis.membres[indice_provocation]
                                    
                            print(self.surnom,self.attribut,' attaque ',cible.surnom,cible.attribut,' avec sa capacité : ',self.capacite1_nom,' à cause de sa provocation!!\n')
                            capacite_choisie=self.capacite1
                            if((capacite_choisie not in capacites_multicibles) and (capacite_choisie not in capacites_soin_allie_avec_hit) and (capacite_choisie not in capacites_hit_multicibles)):
                                capacite_choisie(self,cible)
                            elif(capacite_choisie in capacites_soin_allie_avec_hit):
                                capacite_choisie(self,team_allies,cible)
                            elif(capacite_choisie in capacites_hit_multicibles):
                                capacite_choisie(self,team_ennemis,cible)
                            else:
                                capacite_choisie(self,team_ennemis)

                            self.appliquer_passifs_fin_de_tour(cible,team_allies,team_ennemis)
                        self.appliquer_passifs_fin_de_tour_si_pas_offense(team_allies)

                else:
                    if(self.tours_sommeil > 0):
                        print(self.surnom,self.attribut,' est endormi(e)!!\n')
                    else:
                        print(self.surnom,self.attribut,' se reprend. \n')
                    self.peut_jouer=1
            else:
                print('\n ',self.surnom,self.attribut,'est mort!! \n')
            self.tour_supplementaire_tmp-=1


        if((self.presence_passif_1 == 1) and (self.sans_passif <= 0)  and (self.passif_1 in passifs_fin_de_tour)):
            self.passif_1(team_allies)
        if((self.presence_passif_2 == 1) and (self.sans_passif <= 0)  and (self.passif_2 in passifs_fin_de_tour)):
            self.passif_2(team_allies)

        self.fin_de_tour()
        if (self.perturbation_recup <= 0):
            self.etre_soigne(math.floor((self.regeneration*self.pv_max_donjons)/100))
        if(self.tour_supplementaire_tmp >= 0):
            print("C'est encore au tour de ", self.surnom,self.attribut, " : ", "\n")
            self.jauge_attaque+=100
        
        
    ''' INTRODUIRE VARIABLE 0 ou 1 POUR CAPACITES RESURRECTION ET Fee.DoubleFleche etc. '''
    ''' DANS FONCTION, SELON 0 OU 1, LAISSER LE CHOIX OU NON AU JOUEUR '''
    def action_ennemis(self,team_allies,team_ennemis):
        ''' ACTUALISER TOUTES LES CAPACITES ANORMALES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! '''
        ''' FAIRE DEUX FONCTIONS action = PAS UNE BONNE IDEE => EN FAIRE UNE SEULE EN JOUANT AVEC LES VARIABLES '''
        ''' FONCTION A OPTIMISER... Faire beaucoup plus de fonctions auxiliaires!!!! '''

        capacites_anormales=[SoldatSquelette.slash,ChauveSouris.ultrason,Lutin.deceleration,OursDeGuerre.rugissement,Salamandre.tremblement,Chevalier.abnegation,OursDeGuerre.abnegation,Elementaire.renforcement,Garuda.resurgir,Garuda.lumiere,Esprit.guerison,Esprit.sphere_spirituelle,Fee.soin,Fee.double_fleche,Fee.pluie_douleur,Fee.benediction,DameHarpie.plumes,DameHarpie.danse,Inugami.coop,Inugami.hurlement,Golem.corps_de_lave,Golem.corps_de_glace,Golem.mur_de_fer,Mastodonte.pluie_de_gravats,Mastodonte.armure_de_glace,Serpent.tsunami,Serpent.orage,Griffon.tornade,Inferno.deflagration,Inferno.orage,Elfe.fleches,Elfe.pluie,ChevalierMagique.projectiles,ChevalierMagique.drain,Griffon.acceleration,Inferno.adrenaline,OursDeCombat.cri,Elfe.strategie,ChevalierMagique.combo,ChevalierMagique.tempete,ChevalierMagique.vortex,Phenix.blizzard,Phenix.tempete,Phenix.purification,Sylphe.tourbillon,Sylphe.nuit,Sylphe.cyclone,Sylphe.blizzard,Sylphe.phenix,Sylphide.bourrasque,Sylphide.bourrasque2,Sylphide.conjuration,Sylphide.bouclier,Sylphide.benediction,Sylphide.benediction_lumiere]
        capacites_multicibles=[SoldatSquelette.slash,ChauveSouris.ultrason,Lutin.deceleration,OursDeGuerre.rugissement,Salamandre.tremblement,Chevalier.abnegation,Fee.double_fleche,Fee.pluie_douleur,DameHarpie.plumes,Golem.corps_de_lave,Golem.corps_de_glace,Mastodonte.pluie_de_gravats,Serpent.tsunami,Serpent.orage,Griffon.tornade,Inferno.deflagration,Inferno.orage,Elfe.fleches,Elfe.pluie,ChevalierMagique.projectiles,ChevalierMagique.drain,Phenix.blizzard,Phenix.tempete,Phenix.purification,Sylphe.tourbillon,Sylphe.nuit,Sylphe.cyclone,Sylphe.blizzard,Sylphe.phenix]
        capacites_multicibles_multi_equipes=[Sylphide.bourrasque,Sylphide.bourrasque2] # (sylphe,equipe_ennemie,equipe_alliee)
        capacites_hit_multicibles=[ChevalierMagique.combo,ChevalierMagique.tempete]

        capacites_soin_allie=[Esprit.guerison,Fee.soin,Sylphide.benediction]
        capacites_soin_allie_avec_hit=[Esprit.sphere_spirituelle,ChevalierMagique.vortex] # (esprit,Team_allies,cible)
        capacites_protection_allie=[]
        capacites_renforcement_allie=[Garuda.resurgir]
        capacites_resurrection_allie=[Garuda.lumiere] # Prend Team_allies comme argument

        capacites_renforcement_perso=[OursDeGuerre.abnegation,Elementaire.renforcement,Golem.mur_de_fer,Mastodonte.armure_de_glace]
        capacites_renforcement_equipe=[Fee.benediction,DameHarpie.danse,Inugami.hurlement,Griffon.acceleration,Inferno.adrenaline,OursDeCombat.cri,Elfe.strategie,Sylphide.benediction_lumiere,Sylphide.bouclier,Sylphide.conjuration] # Same
        capacites_attaque_en_groupe=[Inugami.coop] # (inugami,Team_allies,cible)

        passifs_debut_de_tour=[Serpent.renforcement,Elfe.mouvement_esquive,ChevalierMagique.feu_vengeur]
        passifs_fin_de_tour=[Chevalier.urgence,Golem.barriere,Mastodonte.peau_dure,Elfe.fin_mouvement_esquive,Vampire.soif_de_sang]

        self.tour_supplementaire_tmp+=self.tour_supplementaire
        if(self.chances_tour_supplementaire > 0):
            reussite_effet=(random.randint(1,100))/100
            if(reussite_effet<=self.chances_tour_supplementaire):
                self.tour_supplementaire_tmp+=1

        print("C'est au tour de ", self.surnom, self.attribut, " : ", "\n")
        while(self.tour_supplementaire_tmp >= 0):
            self.debut_de_tour()
            if(self.pv_actuels > 0):
                if(self.peut_jouer == 1):
                    if(team_allies.is_alive()):
                        if((self.presence_passif_1 == 1) and (self.sans_passif <= 0) and (self.passif_1 in passifs_debut_de_tour)):
                            self.passif_1(team_ennemis)
                        if((self.presence_passif_2 == 1) and (self.sans_passif <= 0)  and (self.passif_2 in passifs_debut_de_tour)):
                            self.passif_2(team_ennemis)
                        if(self.provoque <= 0):
                            capacite_choisie=self.choisir_capacite_speciale_sans_affichage()
                            if((capacite_choisie not in capacites_anormales) or (capacite_choisie in capacites_soin_allie_avec_hit) or (capacite_choisie in capacites_attaque_en_groupe) or (capacite_choisie in capacites_hit_multicibles)):
                                possibilites_cible=[]
                                for index in range(team_allies.len):
                                    if(team_allies.membres[index].pv_actuels > 0):
                                        possibilites_cible.append(index)
                                indice_cible=possibilites_cible[random.randint(0,len(possibilites_cible)-1)]
                                cible_allie=team_allies.membres[indice_cible]
                                ''' Dans un premier temps, l'attaque se fait de manière aléatoire '''
                                ''' Un jour je regarderai les priorités élémentaires pour faire une vraie IA '''
                                
                                pv_avant_degats=cible_allie.pv_actuels
                                if ((capacite_choisie not in capacites_soin_allie_avec_hit) and (capacite_choisie not in capacites_attaque_en_groupe) and (capacite_choisie not in capacites_hit_multicibles)):
                                    capacite_choisie(self,cible_allie)
                                elif(capacite_choisie in capacites_hit_multicibles):
                                    capacite_choisie(self,team_allies,cible_allie)
                                else:
                                    capacite_choisie(self,team_ennemis,cible_allie)
                                    
                                if(cible_allie.reflexion_dommages > 0):
                                    degats_subis=pv_avant_degats-cible_allie.pv_actuels
                                    degats_renvoyes=Arrondir.a_l_unite(cible_allie.pourcentage_reflexion_dommages*degats_subis)
                                    cible_allie.pv_actuels+=degats_renvoyes # oui c'est bien un +
                                    if(self.immortalite <= 0):
                                        print('\n',self.surnom,self.attribut,' reçoit la réflexion des dégâts!!')
                                        print(self.surnom,self.attribut,' subit ',degats_renvoyes,' points de dégâts!!')
                                        self.pv_actuels-=degats_renvoyes
                                    else:
                                        print(self.surnom,self.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                                    if(self.pv_actuels <= 0):
                                        print(self.surnom,self.attribut,' est mort!! \n')
                                    else:
                                        print('Il reste ',self.pv_actuels,' point(s) de vie sur',self.pv_max_donjons,' à ',self.surnom,self.attribut,'!! \n')
                                if(cible_allie.contre_attaque > 0 and cible_allie.pv_actuels > 0):
                                    if (degats_subis <= 0):
                                        degats_subis=1
                                    print('\n',cible_allie.surnom,cible_allie.attribut,' effectue une contre-attaque sur ',self.surnom,self.attribut,'!!')
                                    if(self.immortalite <= 0):
                                        pv_attaquant_avant_dommages=self.pv_actuels
                                        cible_allie.capacite1(cible_allie,self)
                                        ecart=self.pv_actuels-pv_attaquant_avant_dommages
                                        self.pv_actuels+=Arrondir.a_l_unite(0.25*ecart) # seulement 75% des dégâts sont subis
                                    else:
                                        print(self.surnom,self.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                                    if(self.pv_actuels <= 0):
                                        print(self.surnom,self.attribut,' est mort!! \n')
                                    else:
                                        print('Il reste ',self.pv_actuels,' point(s) de vie sur',self.pv_max_donjons,' à ',self.surnom,self.attribut,'!! \n')    

                                self.appliquer_passifs_fin_de_tour(cible_allie,team_ennemis,team_allies)

                            else:
                                if((capacite_choisie in capacites_soin_allie) or (capacite_choisie in capacites_protection_allie) or (capacite_choisie in capacites_renforcement_allie)):
                                    possibilites_choix_allie=[]
                                    for index in range(team_ennemis.len):
                                        if(team_ennemis.membres[index].pv_actuels > 0):
                                            possibilites_choix_allie.append(index)
                                    
                                    # ATTENTION 
                                    # ici cible_allie fait référence à un allié de l'attaquant = un ennemi
                                    choix=possibilites_choix_allie[random.randint(0,len(possibilites_choix_allie)-1)]
                                    cible_allie=team_ennemis.membres[choix]
                                        
                                    if((capacite_choisie in capacites_soin_allie) or (capacite_choisie in capacites_protection_allie)):
                                        capacite_choisie(self,cible_allie)
                                    else:
                                        capacite_choisie(cible_allie)

                                if(capacite_choisie in capacites_renforcement_perso):
                                    capacite_choisie(self)

                                if((capacite_choisie in capacites_resurrection_allie) or (capacite_choisie in capacites_renforcement_equipe)):
                                    capacite_choisie(team_ennemis)

                                if(capacite_choisie in capacites_multicibles):
                                    capacite_choisie(self,team_allies)

                                if(capacite_choisie in capacites_multicibles_multi_equipes):
                                    capacite_choisie(self,team_allies,team_ennemis)

                        else:
                            cible_trouvee=False
                            for index in range(team_allies.len):
                                if(team_allies.membres[index].indice_provocation > 0):
                                    cible_allie=team_allies.membres[index]
                                    cible_trouvee=True
                            if(not cible_trouvee):
                                possibilites_provocation=[]
                                for index in range(team_allies.len):
                                    if(team_allies.membres[index].pv_actuels > 0):
                                        possibilites_provocation.append(index)
                                indice_provocation=possibilites_provocation[random.randint(0,len(possibilites_provocation)-1)]
                                    
                            print(self.surnom,self.attribut,' attaque ',cible_allie.surnom,cible_allie.attribut,' avec sa capacité : ',self.capacite1_nom,' à cause de sa provocation!!\n')
                            capacite_choisie=self.capacite1
                            if((capacite_choisie not in capacites_multicibles) and (capacite_choisie not in capacites_soin_allie_avec_hit) and (capacite_choisie not in capacites_hit_multicibles)):
                                capacite_choisie(self,cible_allie)
                            elif(capacite_choisie in capacites_soin_allie_avec_hit):
                                capacite_choisie(self,team_ennemis,cible_allie)
                            elif(capacite_choisie in capacites_hit_multicibles):
                                capacite_choisie(self,team_allies,cible_allie)
                            else:
                                capacite_choisie(self,team_allies)

                            self.appliquer_passifs_fin_de_tour(cible_allie,team_ennemis,team_allies)
                        self.appliquer_passifs_fin_de_tour_si_pas_offense(team_allies)

                else:
                    if(self.tours_sommeil > 0):
                        print(self.surnom,self.attribut,' est endormi(e)!!\n')
                    else:
                        print(self.surnom,self.attribut,' se reprend. \n')
                    self.peut_jouer=1
            else:
                print('\n ',self.surnom,self.attribut,'est mort!! \n')
            self.tour_supplementaire_tmp-=1

        if((self.presence_passif_1 == 1) and (self.sans_passif <= 0)  and (self.passif_1 in passifs_fin_de_tour)):
            self.passif_1(team_ennemis)
        if((self.presence_passif_2 == 1) and (self.sans_passif <= 0)  and (self.passif_2 in passifs_fin_de_tour)):
            self.passif_2(team_ennemis)

        self.fin_de_tour()
        if (self.perturbation_recup <= 0):
            self.etre_soigne(math.floor((self.regeneration*self.pv_max_donjons)/100))
        if(self.tour_supplementaire_tmp >= 0):
            print("C'est encore au tour de ", self.surnom,self.attribut, " : ", "\n")
            self.jauge_attaque+=100 

        '''
        #  Algorithmes Ordre des Actions :
        #V 1) Debut de tour =
        #V      Regeneration bonus
        #V      Bombe (stun pendant 1 tour)
        #V      Evaluer le stun, le sommeil et le gel
        #V      Degats continus
        #V      Application des bonus/malus (se fait lors de l'application des capacites)
        #V      Diminuer de 1 les tours bonus/malus
        #V      Si < 0, faire = 0

        #V 2) Action
        #V      Choisir une capacite
        #V      Si aucune provocation adverse
        #V      Ou si attaquant pas provoque
        #V         Choisir une cible
        #V      Appliquer la compétence à la cible
        #V      Infliger la réflexion de dommage
        #V      Activer la régénération passive si dispo et pas bloquée
        #V      Evaluer contre-attaque, l'appliquer si besoin
        #V          Counter COMPETENCE 1 * 75%
        #V      Evaluer le tour supplémentaire
        #V      Eventuellement tout recommencer
        '''






























    def procedure_attaque(self,degats,cible):
        if (degats <= 0):
            degats=1
        if(cible.immortalite <= 0):
            if(cible.nom == 'Serpent' and cible.attribut == 'Vent' and self.attribut == 'Feu' and cible.sans_passif <= 0):
                degats=Arrondir.a_l_unite(degats/2)
            if(cible.nom == 'Griffon' and cible.sans_passif <= 0):
                if(cible.attribut == 'Lumière' and self.attribut == 'Ténèbres'):
                    degats=Arrondir.a_l_unite(degats/2)
                if(cible.attribut == 'Ténèbres' and self.attribut == 'Lumière'):
                    degats=Arrondir.a_l_unite(degats/2)
            cible.recoit_degats(degats)
            print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
            if(cible.tours_sommeil > 0):
                print(cible.surnom,cible.attribut,' se réveille!!\n')
                cible.tours_sommeil=0
                cible.sommeil=0
                cible.peut_jouer=1
            if (self.perturbation_recup <= 0):
                self.etre_soigne(math.floor(self.vol_de_vie*degats/100))
        else:
            print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if (cible.pv_actuels <= 0):
            print(cible.surnom,cible.attribut,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')


    # +1 pour certains effets pour pouvoir bénéficier des bonus/malus s'ils ne durent qu'un tour 

    def slow_down(self,nb_tours):
        if(self.immunite <= 0):
            print(self.surnom,self.attribut,' voit sa vitesse diminuer pour ',nb_tours,' tour(s)!! \n')
            self.vitesse_actuelle-=Arrondir.a_l_unite(0.3*self.vitesse_actuelle)
            self.tours_malus_vitesse=max(self.tours_malus_vitesse,nb_tours)

    def speed_up(self,nb_tours):
        if(self.immunite_aux_bonus <= 0):
            print(self.surnom,self.attribut,' voit sa vitesse augmenter pour ',nb_tours,' tour(s)!! \n')
            self.vitesse_actuelle+=Arrondir.a_l_unite(0.3*self.vitesse_actuelle)
            self.tours_bonus_vitesse=max(self.tours_bonus_vitesse,nb_tours)

    def def_break(self,nb_tours):
        if(self.immunite <= 0):
            print(self.surnom,self.attribut,' voit sa défense diminuer pour ',nb_tours,' tour(s)!! \n')
            self.defense_actuelle-=Arrondir.a_l_unite(0.7*self.defense_actuelle)
            self.tours_malus_defense=max(self.tours_malus_defense,nb_tours)

    def tanky(self,nb_tours):
        if(self.immunite_aux_bonus <= 0):
            print(self.surnom,self.attribut,' voit sa défense augmenter pour ',nb_tours,' tour(s)!! \n')
            self.defense_actuelle+=Arrondir.a_l_unite(0.7*self.defense_actuelle)
            self.tours_bonus_defense=max(self.tours_bonus_defense,nb_tours)

    def atk_break(self,nb_tours):
        if(self.immunite <= 0):
            print(self.surnom,self.attribut,' voit son attaque diminuer pour ',nb_tours,' tour(s)!! \n')
            self.attaque_actuelle-=Arrondir.a_l_unite(0.5*self.attaque_actuelle)
            self.tours_malus_attaque=max(self.tours_malus_attaque,nb_tours+1)

    def rise(self,nb_tours):
        if(self.immunite_aux_bonus <= 0):
            print(self.surnom,self.attribut,' voit son attaque augmenter pour ',nb_tours,' tour(s)!! \n')
            self.attaque_actuelle+=Arrondir.a_l_unite(0.5*self.attaque_actuelle)
            self.tours_bonus_attaque=max(self.tours_bonus_attaque,nb_tours+1)

    def espada(self,nb_tours):
        if(self.immunite_aux_bonus <= 0):
            print(self.surnom,self.attribut,' voit ses chances d\'infliger un coup critique augmenter pour ',nb_tours,' tour(s)!! \n')
            self.taux_coup_critique_actuel+=0.3
            self.tours_bonus_taux_coup_critique=max(self.tours_bonus_taux_coup_critique,nb_tours+1)

    def bonus_coup_superficiel(self,nb_tours):
        if(self.immunite <= 0):
            print(self.surnom,self.attribut,' voit ses chances d\'infliger un coup superficiel augmenter pour ',nb_tours,' tour(s)!! \n')
            self.bonus_taux_coup_superficiel+=0.5
            self.tours_bonus_taux_coup_superficiel=max(self.tours_bonus_taux_coup_superficiel,nb_tours+1)

    def degats_continus(self,nb_marques,nb_tours):
        if(self.immunite <= 0):
            if(nb_marques == 1):
                print(self.surnom,self.attribut,' reçoit une marque de dégats continus pour ',nb_tours,' tour(s)!! \n')
            elif(nb_marques == 2):
                print(self.surnom,self.attribut,' reçoit deux marques de dégats continus pour ',nb_tours,' tour(s)!! \n')
            elif(nb_marques == 3):
                print(self.surnom,self.attribut,' reçoit trois marques de dégâts continus pour ',nb_tours,' tour(s)!! \n')
            self.marques_degats_continus+=nb_marques
            self.intensite_degats_continus=max(nb_tours,self.intensite_degats_continus)

    def immunity(self,nb_tours):
        if(self.immunite_aux_bonus <= 0):
            print(self.surnom,self.attribut,' reçoit l\'immunité aux effets négatifs pour ',nb_tours,' tour(s)!! \n')
            self.immunite=1
            self.tours_immunite=max(self.tours_immunite,nb_tours)

    def sommeil(self,nb_tours):
        if(self.immunite <= 0):
            print(self.surnom,self.attribut,' s\'endort pour ',nb_tours,' tour(s)!! \n')
            self.sommeil=1
            self.tours_sommeil=max(self.tours_sommeil,nb_tours)

    def perturbation_recuperation(self,nb_tours):
        if(self.immunite <= 0):
            print(self.surnom,self.attribut,' voit sa récupération de points de vie perturbée pour ',nb_tours,' tour(s)!! \n')
            self.perturbation_recup=1
            self.tours_perturbation_recup=max(self.tours_perturbation_recup,nb_tours)

    def retirer_un_bonus(self):
        if(self.nb_effets_renforcement() > 0):
            print(self.surnom,self.attribut,'perd l\'un de ses bonus!! \n')
            if(self.tours_bonus_attaque>0):
                self.tours_bonus_attaque=0
                if(self.tours_malus_attaque <= 0):
                    self.attaque_actuelle=self.attaque_max_donjons
                else:
                    self.attaque_actuelle=self.attaque_max_donjons-(0.5*self.attaque_actuelle)
            elif(self.tours_bonus_defense > 0):
                self.tours_bonus_defense=0
                if(self.tours_malus_defense <= 0):
                    self.defense_actuelle=self.defense_max_donjons
                else:
                    self.defense_actuelle=self.defense_max_donjons-(0.5*self.defense_actuelle)
            elif(self.tours_bonus_vitesse > 0):
                self.tours_bonus_vitesse=0
                if(self.tours_malus_vitesse <= 0):
                    self.vitesse_actuelle=self.vitesse_max_donjons
                else:
                    self.vitesse_actuelle=self.vitesse_max_donjons-(0.5*self.vitesse_actuelle)
            elif(self.tours_bonus_taux_coup_critique > 0):
                self.tours_bonus_taux_coup_critique=0
                self.taux_coup_critique_actuel=self.taux_coup_critique
            elif(self.tours_regeneration > 0):
                self.tours_regeneration=0
            elif(self.tours_contre_attaque > 0):
                self.tours_contre_attaque=0
            elif(self.tours_immunite > 0):
                self.tours_immunite=0
                self.immunite=0
            elif(self.tours_invincibilite > 0):
                self.tours_invincibilite=0
                self.invincibilite=0
            elif(self.tours_immortalite > 0):
                self.tours_immortalite=0
                self.immortalite=0
            elif(self.tours_reflexion_dommages > 0):
                self.tours_reflexion_dommages=0
            elif(self.tours_endurance > 0):
                self.tours_endurance=0
                self.endurance=0
            elif(self.tours_provocation > 0):
                self.tours_provocation=0
                self.provocation=0

    def nb_effets_renforcement(self): # pas de s pour ne pas utiliser la même variable que ci-dessous
        nb_effets_renforcements=0
        if(self.tours_bonus_attaque > 0):
            nb_effets_renforcements+=1
        if(self.tours_bonus_defense > 0):
            nb_effets_renforcements+=1
        if(self.tours_bonus_vitesse > 0):
            nb_effets_renforcements+=1
        if(self.tours_bonus_taux_coup_critique > 0):
            nb_effets_renforcements+=1
        if(self.tours_regeneration > 0):
            nb_effets_renforcements+=1
        if(self.tours_contre_attaque > 0):
            nb_effets_renforcements+=1
        if(self.tours_immunite > 0):
            nb_effets_renforcements+=1
        if(self.tours_invincibilite > 0):
            nb_effets_renforcements+=1
        if(self.tours_immortalite > 0):
            nb_effets_renforcements+=1
        if(self.tours_reflexion_dommages > 0):
            nb_effets_renforcements+=1
        if(self.tours_endurance > 0):
            nb_effets_renforcements+=1
        if(self.tours_provocation > 0):
            nb_effets_renforcements+=1
        return nb_effets_renforcements

    def retirer_un_malus(self):
        if(self.nb_effets_nocif() > 0):
            print(self.surnom,self.attribut,'perd l\'un de ses malus!! \n')
            if(self.tours_malus_attaque > 0):
                self.tours_malus_attaque=0
                if(self.tours_bonus_attaque <= 0):
                    self.attaque_actuelle=self.attaque_max_donjons
                else:
                    self.attaque_actuelle=self.attaque_max_donjons+(0.5*self.attaque_actuelle)
            elif(self.tours_malus_defense > 0):
                self.tours_malus_defense=0
                if(self.tours_bonus_defense <= 0):
                    self.defense_actuelle=self.defense_max_donjons
                else:
                    self.defense_actuelle=self.defense_max_donjons+(0.7*self.defense_actuelle)
            elif(self.tours_malus_vitesse > 0):
                self.tours_malus_vitesse=0
                if(self.tours_bonus_vitesse <= 0):
                    self.vitesse_actuelle=self.vitesse_max_donjons
                else:
                    self.vitesse_actuelle=self.vitesse_max_donjons+(0.3*self.vitesse_actuelle)
            elif(self.tours_bonus_taux_coup_superficiel > 0):
                self.bonus_taux_coup_superficiel=0
                self.tours_bonus_taux_coup_superficiel=0
            elif(self.tours_immunite_aux_bonus > 0):
                self.immunite_aux_bonus=0
                self.tours_immunite_aux_bonus=0
            elif(self.tours_avant_explosion > 0):
                self.bombe=0
                self.tours_avant_explosion=0
            elif(self.tours_provoque > 0):
                self.provoque=0
                self.tours_provoque=0
            elif(self.stun > 0):
                self.stun=0
                self.peut_jouer=1
            elif(self.gel > 0):
                self.gel=0
                self.peut_jouer=1
            elif(self.tours_sommeil > 0):
                self.sommeil=0
                self.tours_sommeil=0
                self.peut_jouer=1
            elif(self.intensite_degats_continus > 0):
                self.marques_degats_continus=0
                self.intensite_degats_continus=0
            elif(self.tours_perturbation_recup > 0):
                self.perturbation_recup=0
                self.tours_perturbation_recup=0
            elif(self.tours_silencieux > 0):
                self.silencieux=0
                self.tours_silencieux=0
            elif(self.tours_marque > 0 or self.marque > 0):
                self.marque=0
                self.tours_marque=0
            elif(self.tours_sans_passif > 0):
                self.sans_passif=0
                self.tours_sans_passif=0

    def nb_effets_nocif(self): # idem
        nb_effets_nocifs=0
        if(self.tours_malus_attaque > 0):
            nb_effets_nocifs+=1
        if(self.tours_malus_defense > 0):
            nb_effets_nocifs+=1
        if(self.tours_malus_vitesse > 0):
            nb_effets_nocifs+=1
        if(self.tours_bonus_taux_coup_superficiel > 0):
            nb_effets_nocifs+=1
        if(self.tours_immunite_aux_bonus > 0):
            nb_effets_nocifs+=1
        if(self.tours_avant_explosion > 0):
            nb_effets_nocifs+=1
        if(self.tours_provoque > 0):
            nb_effets_nocifs+=1
        if(self.stun > 0):
            nb_effets_nocifs+=1
        if(self.gel > 0):
            nb_effets_nocifs+=1
        if(self.sommeil > 0):
            nb_effets_nocifs+=1
        if(self.marques_degats_continus > 0):
            nb_effets_nocifs+=1
        if(self.perturbation_recup > 0):
            nb_effets_nocifs+=1
        if(self.silencieux > 0):
            nb_effets_nocifs+=1
        if(self.marque > 0):
            nb_effets_nocifs+=1
        if(self.sans_passif > 0):
            nb_effets_nocifs+=1
        return nb_effets_nocifs


    def soigner_de_tous_les_maux(self):
        self.tours_malus_attaque=0
        if(self.tours_bonus_attaque <= 0):
            self.attaque_actuelle=self.attaque_max_donjons
        else:
            self.attaque_actuelle=self.attaque_max_donjons+(0.5*self.attaque_actuelle)
        self.tours_malus_defense=0
        if(self.tours_bonus_defense <= 0):
            self.defense_actuelle=self.defense_max_donjons
        else:
            self.defense_actuelle=self.defense_max_donjons+(0.7*self.defense_actuelle)
        self.tours_malus_vitesse=0
        if(self.tours_bonus_vitesse <= 0):
            self.vitesse_actuelle=self.vitesse_max_donjons
        else:
            self.vitesse_actuelle=self.vitesse_max_donjons+(0.3*self.vitesse_actuelle)
        self.bonus_taux_coup_superficiel=0
        self.tours_bonus_taux_coup_superficiel=0
        self.immunite_aux_bonus=0
        self.tours_immunite_aux_bonus=0
        self.bombe=0
        self.tours_avant_explosion=0
        self.provoque=0
        self.tours_provoque=0
        self.stun=0
        self.peut_jouer=1
        self.gel=0
        self.sommeil=0
        self.tours_sommeil=0
        self.marques_degats_continus=0
        self.intensite_degats_continus=0
        self.perturbation_recup=0
        self.tours_perturbation_recup=0
        self.silencieux=0
        self.tours_silencieux=0
        self.marque=0
        self.tours_marque=0
        self.sans_passif=0
        self.tours_sans_passif=0

    def soigner_de_tous_les_biens(self):
        self.tours_bonus_attaque=0
        if(self.tours_malus_attaque <= 0):
            self.attaque_actuelle=self.attaque_max_donjons
        else:
            self.attaque_actuelle=self.attaque_max_donjons-(0.5*self.attaque_actuelle)
        self.tours_bonus_defense=0
        if(self.tours_malus_defense <= 0):
            self.defense_actuelle=self.defense_max_donjons
        else:
            self.defense_actuelle=self.defense_max_donjons-(0.7*self.defense_actuelle)
        self.tours_bonus_vitesse=0
        if(self.tours_malus_vitesse <= 0):
            self.vitesse_actuelle=self.vitesse_max_donjons
        else:
            self.vitesse_actuelle=self.vitesse_max_donjons-(0.3*self.vitesse_actuelle)
        self.tours_bonus_taux_coup_critique=0
        self.taux_coup_critique_actuel=self.taux_coup_critique_max_donjons
        self.tours_regeneration=0
        self.regeneration=0
        self.tours_contre_attaque=0
        self.contre_attaque=0
        self.tours_immunite=0
        self.immunite=0
        self.tours_invincibilite=0
        self.invincibilite=0
        self.tours_immortalite=0
        self.immortalite=0
        self.tours_reflexion_dommages=0
        self.reflexion_dommages=0
        self.tours_endurance=0
        self.endurance=0
        self.tours_provocation=0
        self.provocation=0

    def initialiser_stats_max_donjons(self):
        self.pv_max_donjons=self.pv
        self.attaque_max_donjons=self.attaque
        self.defense_max_donjons=self.defense
        self.vitesse_max_donjons=self.vitesse
        self.taux_coup_critique_max_donjons=self.taux_coup_critique
        self.dommages_critiques_max_donjons=self.dommages_critiques
        self.resistance_max_donjons=self.resistance
        self.precision_max_donjons=self.precision

        self.immunite_max_donjons=self.immunite
        self.tours_immunite_max_donjons=self.tours_immunite
        self.vol_de_vie_max_donjons=self.vol_de_vie
        self.regeneration_max_donjons=self.regeneration
        self.taux_contre_attaque_max_donjons=self.taux_contre_attaque
        self.chances_de_stun_max_donjons=self.chances_de_stun
        self.tour_supplementaire_max_donjons=self.tour_supplementaire
        self.chances_tour_supplementaire_max_donjons=self.chances_tour_supplementaire
        self.immortalite_max_donjons=self.immortalite
        self.tours_immortalite_max_donjons=self.tours_immortalite

    def preparer_au_combat(self):
        if(self!=0):
            self.actualiser_stats_de_simples_a_listes()
            #self.actualiser_stats_de_listes_a_simples() # Corrige les bonus_de_runes_en_pv et autres
            self.initialiser_stats_max_donjons() # Réinitialise les stats max donjons = pas de cumulation

            self.pv_max_donjons+=self.bonus_de_runes_en_pv
            self.pv_max_donjons+=Arrondir.a_l_unite(self.pv*self.bonus_de_runes_en_pourcentage_de_pv)
            self.attaque_max_donjons+=self.bonus_de_runes_en_attaque
            self.attaque_max_donjons+=Arrondir.a_l_unite(self.attaque*self.bonus_de_runes_en_pourcentage_de_attaque)
            self.defense_max_donjons+=self.bonus_de_runes_en_defense
            self.defense_max_donjons+=Arrondir.a_l_unite(self.defense*self.bonus_de_runes_en_pourcentage_de_defense)
            self.vitesse_max_donjons+=self.bonus_de_runes_en_vitesse
            self.taux_coup_critique_max_donjons+=self.bonus_de_runes_en_taux_de_coup_critique
            self.dommages_critiques_max_donjons+=self.bonus_de_runes_en_dommages_critiques
            self.resistance_max_donjons+=self.bonus_de_runes_en_resistance
            self.precision_max_donjons+=self.bonus_de_runes_en_precision
            self.immunite_max_donjons+=self.bonus_de_runes_en_immunite
            self.tours_immunite_max_donjons+=self.bonus_de_runes_en_tours_immunite
            self.vol_de_vie_max_donjons+=self.bonus_de_runes_en_vol_de_vie
            self.regeneration_max_donjons+=self.bonus_de_runes_en_regeneration
            self.taux_contre_attaque_max_donjons+=self.bonus_de_runes_en_taux_contre_attaque
            self.chances_de_stun_max_donjons+=self.bonus_de_runes_en_chances_de_stun
            self.tour_supplementaire_max_donjons+=self.bonus_de_runes_en_tour_supplementaire
            self.chances_tour_supplementaire_max_donjons+=self.bonus_de_runes_en_chances_tour_supplementaire
            self.immortalite_max_donjons+=self.bonus_de_runes_en_immortalite
            self.tours_immortalite_max_donjons+=self.bonus_de_runes_en_tours_immortalite

            self.pv_actuels=self.pv_max_donjons
            self.attaque_actuelle=self.attaque_max_donjons
            self.defense_actuelle=self.defense_max_donjons
            self.vitesse_actuelle=self.vitesse_max_donjons
            self.taux_coup_critique_actuel=self.taux_coup_critique_max_donjons
            self.dommages_critiques_actuels=self.dommages_critiques_max_donjons
            self.resistance_actuelle=self.resistance_max_donjons
            self.precision_actuelle=self.precision_max_donjons
            self.immunite=self.immunite_max_donjons
            self.tours_immunite=self.tours_immunite_max_donjons
            self.vol_de_vie=self.vol_de_vie_max_donjons
            self.regeneration=self.regeneration_max_donjons
            self.taux_contre_attaque=self.taux_contre_attaque_max_donjons
            self.chances_de_stun=self.chances_de_stun_max_donjons
            self.tour_supplementaire=self.tour_supplementaire_max_donjons
            self.chances_tour_supplementaire=self.chances_tour_supplementaire_max_donjons
            self.immortalite=self.immortalite_max_donjons
            self.tours_immortalite=self.tours_immortalite_max_donjons
            




    def priorite_elementaire(self,cible):
        Avantage=False
        if(self.attribut == 'Feu' and cible.attribut == 'Vent'):
            Avantage=True
        if(self.attribut == 'Vent' and cible.attribut == 'Eau'):
            Avantage=True
        if(self.attribut == 'Eau' and cible.attribut == 'Feu'):
            Avantage=True
        if(self.attribut == 'Lumière' and cible.attribut == 'Ténèbres'):
            Avantage=True
        if(self.attribut == 'Ténèbres' and cible.attribut == 'Lumière'):
            Avantage=True
        return Avantage

    def choisir_capacite_speciale(self,fenetre,dimensions_fenetre,team_ennemis,team_allies):
        liste_de_messages = ["Vous pouvez utiliser l'une des capacités suivantes : "]
        # print('\n Vous pouvez utiliser l\'une des capacités suivantes : ')
        possibilites_capacite_speciale=[]
        
        if (self.etat_cap1 == 'dispo'):
            liste_de_messages.append("Capacité 1 : " + self.capacite1_nom)
            # print(self.capacite1_nom,' = 1')
            possibilites_capacite_speciale.append(1)
        else:
            liste_de_messages.append(" ")
        if(self.silencieux <= 0):
            if(self.nb_capacites >= 2):
                if (self.etat_cap2 == 'dispo'):
                    liste_de_messages.append("Capacité 2 : " + self.capacite2_nom)
                    # print(self.capacite2_nom,' = 2')
                    possibilites_capacite_speciale.append(2)
                else:
                    liste_de_messages.append(" ")
            if(self.nb_capacites >= 3):
                if (self.etat_cap3 == 'dispo'):
                    liste_de_messages.append("Capacité 3 : " + self.capacite3_nom)
                    # print(self.capacite3_nom,' = 3')
                    possibilites_capacite_speciale.append(3)
                else:
                    liste_de_messages.append(" ")
            if(self.nb_capacites >= 4):
                if (self.etat_cap4 == 'dispo'):
                    liste_de_messages.append("Capacité 4 : " + self.capacite4_nom)
                    # print(self.capacite4_nom,' = 4')
                    possibilites_capacite_speciale.append(4)
                else:
                    liste_de_messages.append(" ")
        
        liste_de_messages.append('***** Recapitulatif *****')
        
        # Supprimer de ici 
        noms_capacites_speciales = ['***** Récapitulatif *****']
        noms_capacites_speciales.append("Capacité 1 : " + self.capacite1_nom)
        if(self.nb_capacites >= 2):
            noms_capacites_speciales.append("Capacité 2 : " + self.capacite2_nom)
        if(self.nb_capacites >= 3):
            noms_capacites_speciales.append("Capacité 3 : " + self.capacite3_nom)
        if(self.nb_capacites >= 4):
            noms_capacites_speciales.append("Capacité 4 : " + self.capacite4_nom)
        # A là + dans le for ci-dessous 

        for index in range(team_allies.len):
            liste_de_messages.append(team_allies.membres[index].surnom + " " + team_allies.membres[index].attribut  + " : " + str(team_allies.membres[index].pv_actuels) + " PV sur " + str(team_allies.membres[index].pv_max_donjons))
            liste_de_messages.append('Jauge d\'attaque : ' + str(team_allies.membres[index].jauge_attaque))
            noms_capacites_speciales.append(team_allies.membres[index].surnom + " " + team_allies.membres[index].attribut  + " : " + str(team_allies.membres[index].pv_actuels) + " PV sur " + str(team_allies.membres[index].pv_max_donjons))
            noms_capacites_speciales.append('Jauge d\'attaque : ' + str(team_allies.membres[index].jauge_attaque))
        liste_de_messages.append('*************************')
        noms_capacites_speciales.append('*************************')
        graphism_simple(fenetre,dimensions_fenetre,team_ennemis,[616,liste_de_messages])
        choix = graphism_simple(fenetre,dimensions_fenetre,team_ennemis,[617,liste_de_messages,possibilites_capacite_speciale])

        '''
        entree=input('Quelle capacité voulez-vous utiliser ? ')
        while(not Security.is_decimal(entree)):
            entree=input('\nQuelle capacité voulez-vous utiliser ? ')
        choix=int(entree)
        while(choix not in possibilites_capacite_speciale):
            entree=input('\nQuelle capacité voulez-vous utiliser ? ')
            while(not Security.is_decimal(entree)):
                entree=input('\nQuelle capacité voulez-vous utiliser ? ')
            choix=int(entree)
        '''

        if (choix == 1):
            capacite_choisie=self.capacite1
            self.attente1=self.temps_recharge1
            self.etat_cap1='Non dispo'
        elif (choix == 2):
            capacite_choisie=self.capacite2
            self.attente2=self.temps_recharge2
            self.etat_cap2='Non dispo'
        elif (choix == 3):
            capacite_choisie=self.capacite3
            self.attente3=self.temps_recharge3
            self.etat_cap3='Non dispo'
        elif (choix == 4):
            capacite_choisie=self.capacite4
            self.attente4=self.temps_recharge4
            self.etat_cap4='Non dispo'
        
        return [capacite_choisie, choix, liste_de_messages]



    def choisir_capacite_speciale_sans_affichage(self):
        possibilites_capacite_speciale=[]
        if (self.etat_cap1 == 'dispo'):
            possibilites_capacite_speciale.append(1)
        if(self.silencieux <= 0):
            if(self.nb_capacites >= 2):
                if (self.etat_cap2 == 'dispo'):
                    possibilites_capacite_speciale.append(2)
            if(self.nb_capacites >= 3):
                if (self.etat_cap3 == 'dispo'):
                    possibilites_capacite_speciale.append(3)
            if(self.nb_capacites >= 4):
                if(self.etat_cap4 == 'dispo'):
                    possibilites_capacite_speciale.append(4)
        
        indice_aleatoire=random.randint(0,len(possibilites_capacite_speciale)-1)
        while(possibilites_capacite_speciale[indice_aleatoire] not in possibilites_capacite_speciale):
            indice_aleatoire=random.randint(0,len(possibilites_capacite_speciale)-1)
        choix=possibilites_capacite_speciale[indice_aleatoire]
        
        if (choix == 1):
            capacite_choisie=self.capacite1
            self.attente1=self.temps_recharge1
            self.etat_cap1='Non dispo'
        elif (choix == 2):
            capacite_choisie=self.capacite2
            self.attente2=self.temps_recharge2
            self.etat_cap2='Non dispo'
        elif (choix == 3):
            capacite_choisie=self.capacite3
            self.attente3=self.temps_recharge3
            self.etat_cap3='Non dispo'
        elif (choix == 4):
            capacite_choisie=self.capacite4
            self.attente4=self.temps_recharge4
            self.etat_cap4='Non dispo'
        return capacite_choisie


    def fin_de_tour(self):
        self.attente1-=1
        if (self.attente1 <= 0):
            self.etat_cap1='dispo'
            self.attente1=0

        if(self.nb_capacites >= 2):
            self.attente2-=1
            if (self.attente2 <= 0):
                self.etat_cap2='dispo'
                self.attente2=0

        if(self.nb_capacites >= 3):
            self.attente3-=1
            if (self.attente3 <= 0):
                self.etat_cap3='dispo'
                self.attente3=0

        if(self.nb_capacites >= 4):
            self.attente4-=1
            if (self.attente4 <= 0):
                self.etat_cap4='dispo'
                self.attente4=0

        self.jauge_attaque-=100










class Slime(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent']
        indice_element=random.randint(0,2)
        Monstre.__init__(self,'Slime',element[indice_element],1,1,450,450,30,60,102)

        self.pv_min_1=450
        self.attaque_min_1=30
        self.defense_min_1=60
        self.pv_min_2=720
        self.attaque_min_2=48
        self.defense_min_2=96
        self.pv_min_3=1095
        self.attaque_min_3=73
        self.defense_min_3=145
        self.pv_min_4=1575
        self.attaque_min_4=105
        self.defense_min_4=209
        self.pv_min_5=2145
        self.attaque_min_5=143
        self.defense_min_5=285
        self.pv_min_6=2910
        self.attaque_min_6=194
        self.defense_min_6=387

        self.pv_max_1=900
        self.attaque_max_1=60
        self.defense_max_1=120
        self.pv_max_2=1365
        self.attaque_max_2=91
        self.defense_max_2=182
        self.pv_max_3=1965
        self.attaque_max_3=131
        self.defense_max_3=262
        self.pv_max_4=2670
        self.attaque_max_4=178
        self.defense_max_4=356
        self.pv_max_5=3630
        self.attaque_max_5=242
        self.defense_max_5=484
        self.pv_max_6=4935
        self.attaque_max_6=329
        self.defense_max_6=659

        self.nb_capacites=1

        self.capacite1=Slime.ecrasement
        self.capacite1_nom='Ecrasement'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

    def ecrasement(self,cible):
        print('\n',self.surnom,self.attribut,'saute en l air et retombe de tout son poids sur ',cible.surnom,cible.attribut,'!!\n')
        degats=35+self.calcul_dommages(3.3,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.3,self.capacite1_bonus_skill,degats-35,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite == 0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.3,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste <= 100*limite_reussite):
                cible.slow_down(1)


class GardienForet(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent']
        indice_element=random.randint(0,2)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Gardien de la Forêt',element[indice_element],1,1,585,585,33,48,88)

            self.pv_min_1=585
            self.attaque_min_1=33
            self.defense_min_1=48
            self.pv_min_2=930
            self.attaque_min_2=53
            self.defense_min_2=77
            self.pv_min_3=1425
            self.attaque_min_3=80
            self.defense_min_3=116
            self.pv_min_4=2040
            self.attaque_min_4=115
            self.defense_min_4=168
            self.pv_min_5=2775
            self.attaque_min_5=157
            self.defense_min_5=228
            self.pv_min_6=3780
            self.attaque_min_6=213
            self.defense_min_6=310

            self.pv_max_1=1170
            self.attaque_max_1=66
            self.defense_max_1=96
            self.pv_max_2=1770
            self.attaque_max_2=100
            self.defense_max_2=145
            self.pv_max_3=2550
            self.attaque_max_3=144
            self.defense_max_3=209
            self.pv_max_4=3480
            self.attaque_max_4=196
            self.defense_max_4=285
            self.pv_max_5=4725
            self.attaque_max_5=266
            self.defense_max_5=387
            self.pv_max_6=6420
            self.attaque_max_6=362
            self.defense_max_6=527

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Gardien de la Forêt',element[indice_element],1,1,570,570,32,50,88)

            self.pv_min_1=570
            self.attaque_min_1=32
            self.defense_min_1=50
            self.pv_min_2=915
            self.attaque_min_2=51
            self.defense_min_2=80
            self.pv_min_3=1380
            self.attaque_min_3=78
            self.defense_min_3=121
            self.pv_min_4=1995
            self.attaque_min_4=112
            self.defense_min_4=175
            self.pv_min_5=2715
            self.attaque_min_5=152
            self.defense_min_5=238
            self.pv_min_6=3675
            self.attaque_min_6=207
            self.defense_min_6=323

            self.pv_max_1=1140
            self.attaque_max_1=64
            self.defense_max_1=100
            self.pv_max_2=1725
            self.attaque_max_2=97
            self.defense_max_2=152
            self.pv_max_3=2490
            self.attaque_max_3=140
            self.defense_max_3=218
            self.pv_max_4=3390
            self.attaque_max_4=190
            self.defense_max_4=297
            self.pv_max_5=4605
            self.attaque_max_5=258
            self.defense_max_5=404
            self.pv_max_6=6255
            self.attaque_max_6=351
            self.defense_max_6=549

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Gardien de la Forêt',element[indice_element],1,1,555,555,36,47,88)

            self.pv_min_1=555
            self.attaque_min_1=36
            self.defense_min_1=47
            self.pv_min_2=885
            self.attaque_min_2=57
            self.defense_min_2=75
            self.pv_min_3=1350
            self.attaque_min_3=87
            self.defense_min_3=114
            self.pv_min_4=1935
            self.attaque_min_4=126
            self.defense_min_4=164
            self.pv_min_5=2640
            self.attaque_min_5=171
            self.defense_min_5=223
            self.pv_min_6=3585
            self.attaque_min_6=232
            self.defense_min_6=304

            self.pv_max_1=1110
            self.attaque_max_1=72
            self.defense_max_1=94
            self.pv_max_2=1680
            self.attaque_max_2=109
            self.defense_max_2=142
            self.pv_max_3=2415
            self.attaque_max_3=157
            self.defense_max_3=205
            self.pv_max_4=3300
            self.attaque_max_4=214
            self.defense_max_4=279
            self.pv_max_5=4485
            self.attaque_max_5=291
            self.defense_max_5=379
            self.pv_max_6=6090
            self.attaque_max_6=395
            self.defense_max_6=516

        self.nb_capacites=1

        self.capacite1=GardienForet.branche
        self.capacite1_nom='Coup de branche'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

    def branche(self,cible):
        print('\n',self.surnom,self.attribut,' frappe ',cible.surnom,cible.attribut,' avec une branche!!\n')
        degats=self.calcul_dommages(3.6,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.6,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite == 0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.15,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste <= 100*limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1


class Champignon(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent']
        indice_element=random.randint(0,2)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Champignon',element[indice_element],1,1,630,630,46,32,104)

            self.pv_min_1=630
            self.attaque_min_1=46
            self.defense_min_1=32
            self.pv_min_2=1005
            self.attaque_min_2=73
            self.defense_min_2=51
            self.pv_min_3=1530
            self.attaque_min_3=112
            self.defense_min_3=78
            self.pv_min_4=2205
            self.attaque_min_4=161
            self.defense_min_4=112
            self.pv_min_5=3000
            self.attaque_min_5=219
            self.defense_min_5=152
            self.pv_min_6=4065
            self.attaque_min_6=297
            self.defense_min_6=207

            self.pv_max_1=1260
            self.attaque_max_1=92
            self.defense_max_1=64
            self.pv_max_2=1905
            self.attaque_max_2=139
            self.defense_max_2=97
            self.pv_max_3=2745
            self.attaque_max_3=201
            self.defense_max_3=140
            self.pv_max_4=3750
            self.attaque_max_4=273
            self.defense_max_4=190
            self.pv_max_5=5085
            self.attaque_max_5=371
            self.defense_max_5=258
            self.pv_max_6=6915
            self.attaque_max_6=505
            self.defense_max_6=351

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Champignon',element[indice_element],1,1,615,615,49,32,104)

            self.pv_min_1=615
            self.attaque_min_1=49
            self.defense_min_1=30
            self.pv_min_2=975
            self.attaque_min_2=78
            self.defense_min_2=48
            self.pv_min_3=1485
            self.attaque_min_3=119
            self.defense_min_3=73
            self.pv_min_4=2145
            self.attaque_min_4=171
            self.defense_min_4=105
            self.pv_min_5=2925
            self.attaque_min_5=233
            self.defense_min_5=143
            self.pv_min_6=3975
            self.attaque_min_6=316
            self.defense_min_6=194

            self.pv_max_1=1230
            self.attaque_max_1=98
            self.defense_max_1=60
            self.pv_max_2=1860
            self.attaque_max_2=148
            self.defense_max_2=91
            self.pv_max_3=2685
            self.attaque_max_3=214
            self.defense_max_3=131
            self.pv_max_4=3660
            self.attaque_max_4=291
            self.defense_max_4=178
            self.pv_max_5=4965
            self.attaque_max_5=396
            self.defense_max_5=242
            self.pv_max_6=6750
            self.attaque_max_6=538
            self.defense_max_6=329

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Champignon',element[indice_element],1,1,690,690,45,29,104)

            self.pv_min_1=690
            self.attaque_min_1=45
            self.defense_min_1=29
            self.pv_min_2=1095
            self.attaque_min_2=72
            self.defense_min_2=46
            self.pv_min_3=1680
            self.attaque_min_3=109
            self.defense_min_3=70
            self.pv_min_4=2415
            self.attaque_min_4=157
            self.defense_min_4=101
            self.pv_min_5=3285
            self.attaque_min_5=214
            self.defense_min_5=138
            self.pv_min_6=4455
            self.attaque_min_6=291
            self.defense_min_6=187

            self.pv_max_1=1380
            self.attaque_max_1=90
            self.defense_max_1=58
            self.pv_max_2=2085
            self.attaque_max_2=136
            self.defense_max_2=88
            self.pv_max_3=3015
            self.attaque_max_3=196
            self.defense_max_3=127
            self.pv_max_4=4095
            self.attaque_max_4=267
            self.defense_max_4=172
            self.pv_max_5=5565
            self.attaque_max_5=363
            self.defense_max_5=234
            self.pv_max_6=7575
            self.attaque_max_6=494
            self.defense_max_6=318

        self.nb_capacites=1

        self.capacite1=Champignon.spore
        self.capacite1_nom='Spore Toxique'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

    def spore(self,cible):
        print('\n',self.surnom,self.attribut,' projette des spores toxiques sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.0,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.0,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite == 0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste <= 100*limite_reussite):
                cible.degats_continus(1,1)


class Spectre(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Ténèbres']
        indice_element=random.randint(0,3)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Spectre',element[indice_element],1,1,705,705,47,26,101)

            self.pv_min_1=705
            self.attaque_min_1=47
            self.defense_min_1=26
            self.pv_min_2=1125
            self.attaque_min_2=75
            self.defense_min_2=42
            self.pv_min_3=1710
            self.attaque_min_3=114
            self.defense_min_3=63
            self.pv_min_4=2460
            self.attaque_min_4=164
            self.defense_min_4=91
            self.pv_min_5=3345
            self.attaque_min_5=223
            self.defense_min_5=124
            self.pv_min_6=4560
            self.attaque_min_6=304
            self.defense_min_6=168

            self.pv_max_1=1410
            self.attaque_max_1=94
            self.defense_max_1=52
            self.pv_max_2=2130
            self.attaque_max_2=142
            self.defense_max_2=79
            self.pv_max_3=3075
            self.attaque_max_3=205
            self.defense_max_3=113
            self.pv_max_4=4185
            self.attaque_max_4=279
            self.defense_max_4=154
            self.pv_max_5=5685
            self.attaque_max_5=379
            self.defense_max_5=210
            self.pv_max_6=4560
            self.attaque_max_6=304
            self.defense_max_6=168

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Spectre',element[indice_element],1,1,720,720,44,28,101)

            self.pv_min_1=720
            self.attaque_min_1=44
            self.defense_min_1=28
            self.pv_min_2=1155
            self.attaque_min_2=70
            self.defense_min_2=45
            self.pv_min_3=1740
            self.attaque_min_3=107
            self.defense_min_3=68
            self.pv_min_4=2520
            self.attaque_min_4=154
            self.defense_min_4=98
            self.pv_min_5=3420
            self.attaque_min_5=209
            self.defense_min_5=133
            self.pv_min_6=4650
            self.attaque_min_6=284
            self.defense_min_6=181

            self.pv_max_1=1440
            self.attaque_max_1=88
            self.defense_max_1=56
            self.pv_max_2=2175
            self.attaque_max_2=133
            self.defense_max_2=85
            self.pv_max_3=3135
            self.attaque_max_3=192
            self.defense_max_3=122
            self.pv_max_4=4275
            self.attaque_max_4=261
            self.defense_max_4=166
            self.pv_max_5=5805
            self.attaque_max_5=355
            self.defense_max_5=226
            self.pv_max_6=7905
            self.attaque_max_6=483
            self.defense_max_6=307

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Spectre',element[indice_element],1,1,675,675,48,27,101)

            self.pv_min_1=675
            self.attaque_min_1=48
            self.defense_min_1=27
            self.pv_min_2=1080
            self.attaque_min_2=77
            self.defense_min_2=43
            self.pv_min_3=1635
            self.attaque_min_3=116
            self.defense_min_3=65
            self.pv_min_4=2355
            self.attaque_min_4=168
            self.defense_min_4=94
            self.pv_min_5=3210
            self.attaque_min_5=228
            self.defense_min_5=128
            self.pv_min_6=4365
            self.attaque_min_6=310
            self.defense_min_6=174

            self.pv_max_1=1350
            self.attaque_max_1=96
            self.defense_max_1=54
            self.pv_max_2=2040
            self.attaque_max_2=145
            self.defense_max_2=82
            self.pv_max_3=2940
            self.attaque_max_3=209
            self.defense_max_3=118
            self.pv_max_4=4005
            self.attaque_max_4=285
            self.defense_max_4=160
            self.pv_max_5=5445
            self.attaque_max_5=387
            self.defense_max_5=218
            self.pv_max_6=7410
            self.attaque_max_6=527
            self.defense_max_6=296

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Spectre',element[indice_element],1,1,630,630,49,29,101)

            self.pv_min_1=630
            self.attaque_min_1=49
            self.defense_min_1=29
            self.pv_min_2=1005
            self.attaque_min_2=78
            self.defense_min_2=46
            self.pv_min_3=1530
            self.attaque_min_3=119
            self.defense_min_3=70
            self.pv_min_4=2205
            self.attaque_min_4=171
            self.defense_min_4=101
            self.pv_min_5=3000
            self.attaque_min_5=233
            self.defense_min_5=138
            self.pv_min_6=4065
            self.attaque_min_6=316
            self.defense_min_6=187

            self.pv_max_1=1260
            self.attaque_max_1=98
            self.defense_max_1=58
            self.pv_max_2=1905
            self.attaque_max_2=148
            self.defense_max_2=88
            self.pv_max_3=2745
            self.attaque_max_3=214
            self.defense_max_3=127
            self.pv_max_4=3750
            self.attaque_max_4=291
            self.defense_max_4=172
            self.pv_max_5=5085
            self.attaque_max_5=396
            self.defense_max_5=234
            self.pv_max_6=6915
            self.attaque_max_6=538
            self.defense_max_6=318

        self.nb_capacites=1

        self.capacite1=Spectre.persecution
        self.capacite1_nom='Persécution'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

    def persecution(self,cible):
        print('\n',self.surnom,self.attribut,' frappe ',cible.surnom,cible.attribut,' avec sa lanterne!!\n')
        degats=self.calcul_dommages(3.4,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.4,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite == 0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste <= 100*limite_reussite):
                cible.bonus_coup_superficiel(1)


class Canniboite(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Ténèbres']
        indice_element=random.randint(0,3)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Canniboite',element[indice_element],1,1,465,465,38,51,86)

            self.pv_min_1=465
            self.attaque_min_1=38
            self.defense_min_1=51
            self.pv_min_2=735
            self.attaque_min_2=61
            self.defense_min_2=81
            self.pv_min_3=1125
            self.attaque_min_3=92
            self.defense_min_3=124
            self.pv_min_4=1620
            self.attaque_min_4=133
            self.defense_min_4=178
            self.pv_min_5=2205
            self.attaque_min_5=181
            self.defense_min_5=242
            self.pv_min_6=3000
            self.attaque_min_6=245
            self.defense_min_6=329

            self.pv_max_1=930
            self.attaque_max_1=76
            self.defense_max_1=102
            self.pv_max_2=1410
            self.attaque_max_2=115
            self.defense_max_2=155
            self.pv_max_3=2025
            self.attaque_max_3=166
            self.defense_max_3=223
            self.pv_max_4=2760
            self.attaque_max_4=226
            self.defense_max_4=303
            self.pv_max_5=3750
            self.attaque_max_5=307
            self.defense_max_5=412
            self.pv_max_6=5100
            self.attaque_max_6=417
            self.defense_max_6=560

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Canniboite',element[indice_element],1,1,525,525,33,52,86)

            self.pv_min_1=525
            self.attaque_min_1=33
            self.defense_min_1=52
            self.pv_min_2=840
            self.attaque_min_2=53
            self.defense_min_2=83
            self.pv_min_3=1275
            self.attaque_min_3=80
            self.defense_min_3=126
            self.pv_min_4=1830
            self.attaque_min_4=115
            self.defense_min_4=182
            self.pv_min_5=2490
            self.attaque_min_5=157
            self.defense_min_5=247
            self.pv_min_6=3390
            self.attaque_min_6=213
            self.defense_min_6=336

            self.pv_max_1=1050
            self.attaque_max_1=66
            self.defense_max_1=104
            self.pv_max_2=1590
            self.attaque_max_2=100
            self.defense_max_2=158
            self.pv_max_3=2295
            self.attaque_max_3=144
            self.defense_max_3=227
            self.pv_max_4=3120
            self.attaque_max_4=196
            self.defense_max_4=309
            self.pv_max_5=4245
            self.attaque_max_5=266
            self.defense_max_5=420
            self.pv_max_6=5670
            self.attaque_max_6=362
            self.defense_max_6=571

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Canniboite',element[indice_element],1,1,540,540,34,50,86)

            self.pv_min_1=540
            self.attaque_min_1=34
            self.defense_min_1=50
            self.pv_min_2=855
            self.attaque_min_2=54
            self.defense_min_2=80
            self.pv_min_3=1305
            self.attaque_min_3=82
            self.defense_min_3=121
            self.pv_min_4=1890
            self.attaque_min_4=119
            self.defense_min_4=175
            self.pv_min_5=2565
            self.attaque_min_5=162
            self.defense_min_5=238
            self.pv_min_6=3480
            self.attaque_min_6=220
            self.defense_min_6=323

            self.pv_max_1=1080
            self.attaque_max_1=68
            self.defense_max_1=100
            self.pv_max_2=1635
            self.attaque_max_2=103
            self.defense_max_2=152
            self.pv_max_3=2355
            self.attaque_max_3=148
            self.defense_max_3=218
            self.pv_max_4=3210
            self.attaque_max_4=202
            self.defense_max_4=297
            self.pv_max_5=4365
            self.attaque_max_5=274
            self.defense_max_5=404
            self.pv_max_6=5925
            self.attaque_max_6=373
            self.defense_max_6=549

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Canniboite',element[indice_element],1,1,555,555,37,46,86)

            self.pv_min_1=555
            self.attaque_min_1=37
            self.defense_min_1=46
            self.pv_min_2=885
            self.attaque_min_2=59
            self.defense_min_2=73
            self.pv_min_3=1350
            self.attaque_min_3=90
            self.defense_min_3=112
            self.pv_min_4=1935
            self.attaque_min_4=129
            self.defense_min_4=161
            self.pv_min_5=2640
            self.attaque_min_5=176
            self.defense_min_5=219
            self.pv_min_6=3585
            self.attaque_min_6=239
            self.defense_min_6=297

            self.pv_max_1=1110
            self.attaque_max_1=74
            self.defense_max_1=92
            self.pv_max_2=1680
            self.attaque_max_2=112
            self.defense_max_2=139
            self.pv_max_3=2415
            self.attaque_max_3=161
            self.defense_max_3=201
            self.pv_max_4=3300
            self.attaque_max_4=220
            self.defense_max_4=273
            self.pv_max_5=4485
            self.attaque_max_5=299
            self.defense_max_5=371
            self.pv_max_6=6090
            self.attaque_max_6=406
            self.defense_max_6=505

        self.nb_capacites=1

        self.capacite1=Canniboite.morsure
        self.capacite1_nom='Morsure'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

    def morsure(self,cible):
        print('\n',self.surnom,self.attribut,' mord ',cible.surnom,cible.attribut,'de toutes ses forces!!\n')
        degats=self.calcul_dommages(3.6,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.6,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite == 0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste <= 100*limite_reussite):
                cible.def_break(1)


class Crapoxique(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Ténèbres']
        indice_element=random.randint(0,3)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Crapoxique',element[indice_element],1,1,765,765,33,36,100)

            self.pv_min_1=765
            self.attaque_min_1=33
            self.defense_min_1=36
            self.pv_min_2=1215
            self.attaque_min_2=53
            self.defense_min_2=57
            self.pv_min_3=1860
            self.attaque_min_3=80
            self.defense_min_3=87
            self.pv_min_4=2670
            self.attaque_min_4=115
            self.defense_min_4=126
            self.pv_min_5=3630
            self.attaque_min_5=157
            self.defense_min_5=171
            self.pv_min_6=4935
            self.attaque_min_6=213
            self.defense_min_6=232

            self.pv_max_1=1530
            self.attaque_max_1=66
            self.defense_max_1=72
            self.pv_max_2=2325
            self.attaque_max_2=100
            self.defense_max_2=109
            self.pv_max_3=3345
            self.attaque_max_3=144
            self.defense_max_3=157
            self.pv_max_4=4545
            self.attaque_max_4=196
            self.defense_max_4=214
            self.pv_max_5=6180
            self.attaque_max_5=266
            self.defense_max_5=291
            self.pv_max_6=8400
            self.attaque_max_6=362
            self.defense_max_6=395

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Canniboite',element[indice_element],1,1,750,750,34,36,100)

            self.pv_min_1=750
            self.attaque_min_1=34
            self.defense_min_1=36
            self.pv_min_2=1200
            self.attaque_min_2=54
            self.defense_min_2=57
            self.pv_min_3=1815
            self.attaque_min_3=82
            self.defense_min_3=87
            self.pv_min_4=2625
            self.attaque_min_4=119
            self.defense_min_4=126
            self.pv_min_5=3570
            self.attaque_min_5=162
            self.defense_min_5=171
            self.pv_min_6=4845
            self.attaque_min_6=220
            self.defense_min_6=232

            self.pv_max_1=1500
            self.attaque_max_1=68
            self.defense_max_1=72
            self.pv_max_2=2280
            self.attaque_max_2=103
            self.defense_max_2=109
            self.pv_max_3=3270
            self.attaque_max_3=148
            self.defense_max_3=157
            self.pv_max_4=4455
            self.attaque_max_4=202
            self.defense_max_4=214
            self.pv_max_5=6060
            self.attaque_max_5=274
            self.defense_max_5=291
            self.pv_max_6=4845
            self.attaque_max_6=220
            self.defense_max_6=232

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Crapoxique',element[indice_element],1,1,735,735,38,33,100)

            self.pv_min_1=735
            self.attaque_min_1=38
            self.defense_min_1=33
            self.pv_min_2=1170
            self.attaque_min_2=61
            self.defense_min_2=53
            self.pv_min_3=1785
            self.attaque_min_3=92
            self.defense_min_3=80
            self.pv_min_4=2565
            self.attaque_min_4=133
            self.defense_min_4=115
            self.pv_min_5=3495
            self.attaque_min_5=181
            self.defense_min_5=157
            self.pv_min_6=4740
            self.attaque_min_6=245
            self.defense_min_6=213

            self.pv_max_1=1470
            self.attaque_max_1=76
            self.defense_max_1=66
            self.pv_max_2=2220
            self.attaque_max_2=115
            self.defense_max_2=100
            self.pv_max_3=3210
            self.attaque_max_3=166
            self.defense_max_3=144
            self.pv_max_4=4365
            self.attaque_max_4=226
            self.defense_max_4=196
            self.pv_max_5=5940
            self.attaque_max_5=307
            self.defense_max_5=266
            self.pv_max_6=8070
            self.attaque_max_6=417
            self.defense_max_6=362

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Crapoxique',element[indice_element],1,1,735,735,38,33,100)

            self.pv_min_1=735
            self.attaque_min_1=38
            self.defense_min_1=33
            self.pv_min_2=1170
            self.attaque_min_2=61
            self.defense_min_2=53
            self.pv_min_3=1785
            self.attaque_min_3=92
            self.defense_min_3=80
            self.pv_min_4=2565
            self.attaque_min_4=133
            self.defense_min_4=115
            self.pv_min_5=3495
            self.attaque_min_5=181
            self.defense_min_5=157
            self.pv_min_6=4740
            self.attaque_min_6=245
            self.defense_min_6=213

            self.pv_max_1=1470
            self.attaque_max_1=76
            self.defense_max_1=66
            self.pv_max_2=2220
            self.attaque_max_2=115
            self.defense_max_2=100
            self.pv_max_3=3210
            self.attaque_max_3=166
            self.defense_max_3=144
            self.pv_max_4=4365
            self.attaque_max_4=226
            self.defense_max_4=196
            self.pv_max_5=5940
            self.attaque_max_5=307
            self.defense_max_5=266
            self.pv_max_6=8070
            self.attaque_max_6=417
            self.defense_max_6=362

        self.nb_capacites=1

        self.capacite1=Crapoxique.bave
        self.capacite1_nom='Jet de bave'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

    def bave(self,cible):
        print('\n',self.surnom,self.attribut,' jette sa bave toxique sur ',cible.surnom,cible.attribut,'!!\n')
        degats=30+self.calcul_dommages(3.4,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.4,self.capacite1_bonus_skill,degats-30,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite == 0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste <= 100*limite_reussite):
                print(cible.surnom,cible.attribut,' perd 15% de sa jauge d\'attaque!!\n')
                cible.jauge_attaque-=max(15,Arrondir.a_l_unite(0.15*cible.jauge_attaque))


class Sacasable(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Ténèbres']
        indice_element=random.randint(0,3)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Sacasable',element[indice_element],1,1,402,402,41,51,102)

            self.pv_min_1=420
            self.attaque_min_1=41
            self.defense_min_1=51
            self.pv_min_2=675
            self.attaque_min_2=65
            self.defense_min_2=81
            self.pv_min_3=1020
            self.attaque_min_3=99
            self.defense_min_3=124
            self.pv_min_4=1470
            self.attaque_min_4=143
            self.defense_min_4=178
            self.pv_min_5=1995
            self.attaque_min_5=195
            self.defense_min_5=242
            self.pv_min_6=2715
            self.attaque_min_6=265
            self.defense_min_6=329

            self.pv_max_1=840
            self.attaque_max_1=82
            self.defense_max_1=102
            self.pv_max_2=1275
            self.attaque_max_2=124
            self.defense_max_2=155
            self.pv_max_3=1830
            self.attaque_max_3=179
            self.defense_max_3=223
            self.pv_max_4=2490
            self.attaque_max_4=244
            self.defense_max_4=303
            self.pv_max_5=3390
            self.attaque_max_5=331
            self.defense_max_5=412
            self.pv_max_6=4605
            self.attaque_max_6=450
            self.defense_max_6=560

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Sacasable',element[indice_element],1,1,390,390,40,54,102)

            self.pv_min_1=390
            self.attaque_min_1=40
            self.defense_min_1=54
            self.pv_min_2=630
            self.attaque_min_2=64
            self.defense_min_2=86
            self.pv_min_3=945
            self.attaque_min_3=97
            self.defense_min_3=131
            self.pv_min_4=1365
            self.attaque_min_4=140
            self.defense_min_4=189
            self.pv_min_5=1860
            self.attaque_min_5=190
            self.defense_min_5=257
            self.pv_min_6=2520
            self.attaque_min_6=258
            self.defense_min_6=349

            self.pv_max_1=780
            self.attaque_max_1=80
            self.defense_max_1=108
            self.pv_max_2=1185
            self.attaque_max_2=121
            self.defense_max_2=164
            self.pv_max_3=1695
            self.attaque_max_3=175
            self.defense_max_3=236
            self.pv_max_4=2310
            self.attaque_max_4=238
            self.defense_max_4=321
            self.pv_max_5=3150
            self.attaque_max_5=323
            self.defense_max_5=436
            self.pv_max_6=4275
            self.attaque_max_6=439
            self.defense_max_6=593

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Sacasable',element[indice_element],1,1,405,405,38,55,102)

            self.pv_min_1=405
            self.attaque_min_1=38
            self.defense_min_1=55
            self.pv_min_2=645
            self.attaque_min_2=61
            self.defense_min_2=88
            self.pv_min_3=975
            self.attaque_min_3=92
            self.defense_min_3=133
            self.pv_min_4=1410
            self.attaque_min_4=133
            self.defense_min_4=192
            self.pv_min_5=1920
            self.attaque_min_5=181
            self.defense_min_5=261
            self.pv_min_6=2610
            self.attaque_min_6=245
            self.defense_min_6=355

            self.pv_max_1=810
            self.attaque_max_1=76
            self.defense_max_1=110
            self.pv_max_2=1230
            self.attaque_max_2=115
            self.defense_max_2=167
            self.pv_max_3=1770
            self.attaque_max_3=166
            self.defense_max_3=240
            self.pv_max_4=2400
            self.attaque_max_4=226
            self.defense_max_4=327
            self.pv_max_5=3270
            self.attaque_max_5=307
            self.defense_max_5=444
            self.pv_max_6=4440
            self.attaque_max_6=417
            self.defense_max_6=604

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Sacasable',element[indice_element],1,1,435,435,39,52,102)

            self.pv_min_1=435
            self.attaque_min_1=39
            self.defense_min_1=52
            self.pv_min_2=690
            self.attaque_min_2=62
            self.defense_min_2=83
            self.pv_min_3=1050
            self.attaque_min_3=95
            self.defense_min_3=126
            self.pv_min_4=1515
            self.attaque_min_4=136
            self.defense_min_4=182
            self.pv_min_5=2070
            self.attaque_min_5=185
            self.defense_min_5=247
            self.pv_min_6=2805
            self.attaque_min_6=252
            self.defense_min_6=336

            self.pv_max_1=870
            self.attaque_max_1=78
            self.defense_max_1=104
            self.pv_max_2=1320
            self.attaque_max_2=118
            self.defense_max_2=158
            self.pv_max_3=1905
            self.attaque_max_3=170
            self.defense_max_3=227
            self.pv_max_4=2580
            self.attaque_max_4=232
            self.defense_max_4=309
            self.pv_max_5=3510
            self.attaque_max_5=315
            self.defense_max_5=420
            self.pv_max_6=4770
            self.attaque_max_6=428
            self.defense_max_6=571

        self.nb_capacites=1

        self.capacite1=Sacasable.sable
        self.capacite1_nom='Jet de Sable'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

    def sable(self,cible):
        print('\n',self.surnom,self.attribut,' jette du sable sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.5,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.5,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite == 0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.3,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste <= 100*limite_reussite):
                cible.sommeil(1)


class BasElementaire(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Bas Elementaire',element[indice_element],1,1,570,570,44,38,100)

            self.pv_min_1=570
            self.attaque_min_1=44
            self.defense_min_1=38
            self.pv_min_2=915
            self.attaque_min_2=70
            self.defense_min_2=61
            self.pv_min_3=1380
            self.attaque_min_3=107
            self.defense_min_3=92
            self.pv_min_4=1995
            self.attaque_min_4=154
            self.defense_min_4=133
            self.pv_min_5=2715
            self.attaque_min_5=209
            self.defense_min_5=181
            self.pv_min_6=3675
            self.attaque_min_6=284
            self.defense_min_6=245

            self.pv_max_1=1140
            self.attaque_max_1=88
            self.defense_max_1=76
            self.pv_max_2=1725
            self.attaque_max_2=133
            self.defense_max_2=115
            self.pv_max_3=2490
            self.attaque_max_3=192
            self.defense_max_3=166
            self.pv_max_4=3390
            self.attaque_max_4=261
            self.defense_max_4=226
            self.pv_max_5=4605
            self.attaque_max_5=355
            self.defense_max_5=307
            self.pv_max_6=6255
            self.attaque_max_6=483
            self.defense_max_6=417

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Bas Elementaire',element[indice_element],1,1,540,540,48,36,100)

            self.pv_min_1=540
            self.attaque_min_1=48
            self.defense_min_1=36
            self.pv_min_2=855
            self.attaque_min_2=77
            self.defense_min_2=57
            self.pv_min_3=1305
            self.attaque_min_3=116
            self.defense_min_3=87
            self.pv_min_4=1890
            self.attaque_min_4=168
            self.defense_min_4=126
            self.pv_min_5=2565
            self.attaque_min_5=228
            self.defense_min_5=171
            self.pv_min_6=3480
            self.attaque_min_6=310
            self.defense_min_6=232

            self.pv_max_1=1080
            self.attaque_max_1=96
            self.defense_max_1=72
            self.pv_max_2=1635
            self.attaque_max_2=145
            self.defense_max_2=109
            self.pv_max_3=2355
            self.attaque_max_3=209
            self.defense_max_3=157
            self.pv_max_4=3210
            self.attaque_max_4=285
            self.defense_max_4=214
            self.pv_max_5=4365
            self.attaque_max_5=387
            self.defense_max_5=291
            self.pv_max_6=5925
            self.attaque_max_6=527
            self.defense_max_6=395

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Bas Elementaire',element[indice_element],1,1,600,600,46,34,100)

            self.pv_min_1=600
            self.attaque_min_1=46
            self.defense_min_1=34
            self.pv_min_2=960
            self.attaque_min_2=73
            self.defense_min_2=54
            self.pv_min_3=1455
            self.attaque_min_3=112
            self.defense_min_3=82
            self.pv_min_4=2100
            self.attaque_min_4=161
            self.defense_min_4=119
            self.pv_min_5=2850
            self.attaque_min_5=219
            self.defense_min_5=162
            self.pv_min_6=3870
            self.attaque_min_6=297
            self.defense_min_6=220

            self.pv_max_1=1200
            self.attaque_max_1=92
            self.defense_max_1=68
            self.pv_max_2=1815
            self.attaque_max_2=139
            self.defense_max_2=103
            self.pv_max_3=2625
            self.attaque_max_3=201
            self.defense_max_3=148
            self.pv_max_4=3570
            self.attaque_max_4=273
            self.defense_max_4=202
            self.pv_max_5=4845
            self.attaque_max_5=371
            self.defense_max_5=274
            self.pv_max_6=6585
            self.attaque_max_6=505
            self.defense_max_6=373

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Bas Elementaire',element[indice_element],1,1,525,525,53,32,100)

            self.pv_min_1=525
            self.attaque_min_1=53
            self.defense_min_1=32
            self.pv_min_2=840
            self.attaque_min_2=85
            self.defense_min_2=51
            self.pv_min_3=1275
            self.attaque_min_3=128
            self.defense_min_3=78
            self.pv_min_4=1830
            self.attaque_min_4=185
            self.defense_min_4=112
            self.pv_min_5=2490
            self.attaque_min_5=252
            self.defense_min_5=152
            self.pv_min_6=3390
            self.attaque_min_6=342
            self.defense_min_6=207

            self.pv_max_1=1050
            self.attaque_max_1=106
            self.defense_max_1=64
            self.pv_max_2=1590
            self.attaque_max_2=161
            self.defense_max_2=97
            self.pv_max_3=2295
            self.attaque_max_3=231
            self.defense_max_3=140
            self.pv_max_4=3120
            self.attaque_max_4=315
            self.defense_max_4=190
            self.pv_max_5=4245
            self.attaque_max_5=428
            self.defense_max_5=258
            self.pv_max_6=5760
            self.attaque_max_6=582
            self.defense_max_6=351

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Bas Elementaire',element[indice_element],1,1,585,585,43,38,100)

            self.pv_min_1=585
            self.attaque_min_1=43
            self.defense_min_1=38
            self.pv_min_2=930
            self.attaque_min_2=69
            self.defense_min_2=61
            self.pv_min_3=1425
            self.attaque_min_3=104
            self.defense_min_3=92
            self.pv_min_4=2040
            self.attaque_min_4=150
            self.defense_min_4=133
            self.pv_min_5=2775
            self.attaque_min_5=204
            self.defense_min_5=181
            self.pv_min_6=3780
            self.attaque_min_6=278
            self.defense_min_6=245

            self.pv_max_1=1170
            self.attaque_max_1=86
            self.defense_max_1=76
            self.pv_max_2=1770
            self.attaque_max_2=130
            self.defense_max_2=115
            self.pv_max_3=2550
            self.attaque_max_3=188
            self.defense_max_3=166
            self.pv_max_4=3480
            self.attaque_max_4=255
            self.defense_max_4=226
            self.pv_max_5=4725
            self.attaque_max_5=347
            self.defense_max_5=307
            self.pv_max_6=6420
            self.attaque_max_6=472
            self.defense_max_6=417

        self.nb_capacites=2

        self.capacite1=BasElementaire.sphere
        self.capacite1_nom='Sphères élémentaires'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

        self.capacite2=BasElementaire.frappes
        self.capacite2_nom='Frappes élémentaires'
        self.capacite2_bonus_skill=0
        self.temps_recharge2=3
        self.attente2=0
        self.etat_cap2='dispo'

    def sphere(self,cible):
        print('\n',self.surnom,self.attribut,' jette deux orbes élémentaires sur ',cible.surnom,cible.attribut,'!!\n')
        for index in range(2):
            degats=self.calcul_dommages(1.9,self.capacite1_bonus_skill,cible)
            self.affichage_du_type_de_coup(1.9,self.capacite1_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite == 0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.2,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste <= 100*limite_reussite):
                    cible.atk_break(2)

    def frappes(self,cible):
        print('\n',self.surnom,self.attribut,' frappe quatre fois ',cible.surnom,cible.attribut,'!!\n')
        for index in range(4):
            degats=self.calcul_dommages(1.3,self.capacite2_bonus_skill,cible)
            self.affichage_du_type_de_coup(1.3,self.capacite2_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite == 0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.3,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste <= 100*limite_reussite):
                    cible.def_break(2)

''' A REFAIRE '''
'''
class Angelmon(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)
        Monstre.__init__(self,'Angelmon',element[indice_element],1,1,15,15,1,1,0)

        self.type='Matériel'
        self.taux_coup_critique=0
        self.dommages_critiques=0
        self.resistance=0
        self.precision=0

        self.pv_min_1=15
        self.attaque_min_1=1
        self.defense_min_1=1

        self.pv_max_1=30
        self.attaque_max_1=2
        self.defense_max_1=2

        self.capacite1=Angelmon.XP
        self.capacite1_nom='Ingrédient de qualité'

    def XP(angelmon):
        XP_donnee_min=1600
        XP_donnee_max=19360
        if(angelmon.niveau==1):
            XP_recue=XP_donnee_min
        elif(Donjon.Niveau_max_de_la_classe_atteint(angelmon)==True):
            XP_recue=XP_donnee_max
        else:
            ecart=XP_donnee_max-XP_donnee_min
            nb_passages_en_niveau=9+(5*angelmon.classe)
            XP_recue=XP_donnee_min+ecart*((angelmon.niveau-1)/nb_passages_en_niveau)
        XP_recue=Arrondir.a_l_unite(XP_recue)
        return XP_recue


class Devilmon(Monstre):
    def __init__(self):
        Monstre.__init__(self,'Devilmon','Ténèbres',1,1,15,15,1,1,0)

        self.type='Matériel'
        self.taux_coup_critique=0
        self.dommages_critiques=0
        self.resistance=0
        self.precision=0

        self.pv_min_1=15
        self.attaque_min_1=1
        self.defense_min_1=1

        self.pv_max_1=30
        self.attaque_max_1=2
        self.defense_max_1=2

        self.capacite1=Angelmon.Bonus
        self.capacite1_nom='Ingrédient de qualité'

    def Bonus():
        bonus_degats_skill=0.05
        bonus_precision_skill=0.1
        bonus_temps_de_reduction=-1
        return [bonus_degats_skill,bonus_precision_skill,bonus_temps_de_reduction]


class RoiAngelmon(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)
        Monstre.__init__(self,'Roi Angelmon',element[indice_element],1,1,15,15,1,1,0)

        self.type='Matériel'
        self.taux_coup_critique=0
        self.dommages_critiques=0
        self.resistance=0
        self.precision=0

        self.pv_min_1=15
        self.attaque_min_1=1
        self.defense_min_1=1

        self.pv_max_1=30
        self.attaque_max_1=2
        self.defense_max_1=2

        self.capacite1=RoiAngelmon.XP_double
        self.capacite1_nom='Ingrédient de qualité'

    def XP_double(roi_angelmon):
        XP_donnee_min=1600
        XP_donnee_max=19360
        if(roi_angelmon.niveau==1):
            XP_recue=XP_donnee_min
        elif(Donjon.Niveau_max_de_la_classe_atteint(roi_angelmon)==True):
            XP_recue=XP_donnee_max
        else:
            ecart=XP_donnee_max-XP_donnee_min
            nb_passages_en_niveau=9+(5*roi_angelmon.classe)
            XP_recue=XP_donnee_min+ecart*((roi_angelmon.niveau-1)/nb_passages_en_niveau)
        XP_recue=Arrondir.a_l_unite(2*XP_recue)
        return XP_recue
'''

class Sanglier(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent']
        indice_element=random.randint(0,2)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Sanglier',element[indice_element],2,1,1170,1170,73,64,93)

            self.pv_min_2=1170
            self.attaque_min_2=73
            self.defense_min_2=64
            self.pv_min_3=1785
            self.attaque_min_3=112
            self.defense_min_3=97
            self.pv_min_4=2565
            self.attaque_min_4=161
            self.defense_min_4=140
            self.pv_min_5=3495
            self.attaque_min_5=219
            self.defense_min_5=190
            self.pv_min_6=4740
            self.attaque_min_6=297
            self.defense_min_6=258

            self.pv_max_2=2220
            self.attaque_max_2=139
            self.defense_max_2=121
            self.pv_max_3=3210
            self.attaque_max_3=201
            self.defense_max_3=175
            self.pv_max_4=4365
            self.attaque_max_4=273
            self.defense_max_4=238
            self.pv_max_5=3495
            self.attaque_max_5=219
            self.defense_max_5=190
            self.pv_max_6=8070
            self.attaque_max_6=505
            self.defense_max_6=439

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Sanglier',element[indice_element],2,1,1215,1215,72,62,93)

            self.pv_min_2=1215
            self.attaque_min_2=72
            self.defense_min_2=62
            self.pv_min_3=1860
            self.attaque_min_3=109
            self.defense_min_3=95
            self.pv_min_4=2670
            self.attaque_min_4=157
            self.defense_min_4=136
            self.pv_min_5=3630
            self.attaque_min_5=214
            self.defense_min_5=185
            self.pv_min_6=4935
            self.attaque_min_6=291
            self.defense_min_6=252

            self.pv_max_2=2325
            self.attaque_max_2=136
            self.defense_max_2=118
            self.pv_max_3=3345
            self.attaque_max_3=196
            self.defense_max_3=170
            self.pv_max_4=4545
            self.attaque_max_4=267
            self.defense_max_4=232
            self.pv_max_5=6180
            self.attaque_max_5=363
            self.defense_max_5=315
            self.pv_max_6=8400
            self.attaque_max_6=494
            self.defense_max_6=428

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Sanglier',element[indice_element],2,1,1170,1170,73,64,93)

            self.pv_min_2=1170
            self.attaque_min_2=73
            self.defense_min_2=64
            self.pv_min_3=1785
            self.attaque_min_3=112
            self.defense_min_3=97
            self.pv_min_4=2565
            self.attaque_min_4=161
            self.defense_min_4=140
            self.pv_min_5=3495
            self.attaque_min_5=219
            self.defense_min_5=190
            self.pv_min_6=4740
            self.attaque_min_6=297
            self.defense_min_6=258

            self.pv_max_2=2220
            self.attaque_max_2=139
            self.defense_max_2=121
            self.pv_max_3=3210
            self.attaque_max_3=201
            self.defense_max_3=175
            self.pv_max_4=4365
            self.attaque_max_4=273
            self.defense_max_4=238
            self.pv_max_5=5940
            self.attaque_max_5=371
            self.defense_max_5=323
            self.pv_max_6=8070
            self.attaque_max_6=505
            self.defense_max_6=439

        self.nb_capacites=1

        self.capacite1=Sanglier.charge
        self.capacite1_nom='Charge'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

    def charge(self,cible):
        print('\n',self.surnom,self.attribut,' charge sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.5,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.5,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite == 0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.15,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste <= 100*limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1


class PlanteCarnivore(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Ténèbres']
        indice_element=random.randint(0,3)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Plante Carnivore',element[indice_element],2,1,1395,1395,70,53,95)

            self.pv_min_2=1395
            self.attaque_min_2=70
            self.defense_min_2=53
            self.pv_min_3=2115
            self.attaque_min_3=107
            self.defense_min_3=80
            self.pv_min_4=3045
            self.attaque_min_4=154
            self.defense_min_4=115
            self.pv_min_5=4140
            self.attaque_min_5=209
            self.defense_min_5=157
            self.pv_min_6=5625
            self.attaque_min_6=284
            self.defense_min_6=213

            self.pv_max_2=2640
            self.attaque_max_2=133
            self.defense_max_2=100
            self.pv_max_3=3795
            self.attaque_max_3=192
            self.defense_max_3=144
            self.pv_max_4=5175
            self.attaque_max_4=261
            self.defense_max_4=196
            self.pv_max_5=7020
            self.attaque_max_5=355
            self.defense_max_5=266
            self.pv_max_6=9555
            self.attaque_max_6=483
            self.defense_max_6=362

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Plante Carnivore',element[indice_element],2,1,1485,1485,67,49,95)

            self.pv_min_2=1485
            self.attaque_min_2=67
            self.defense_min_2=49
            self.pv_min_3=2250
            self.attaque_min_3=102
            self.defense_min_3=75
            self.pv_min_4=3240
            self.attaque_min_4=147
            self.defense_min_4=108
            self.pv_min_5=4425
            self.attaque_min_5=200
            self.defense_min_5=147
            self.pv_min_6=6000
            self.attaque_min_6=271
            self.defense_min_6=200

            self.pv_max_2=2820
            self.attaque_max_2=127
            self.defense_max_2=94
            self.pv_max_3=4065
            self.attaque_max_3=183
            self.defense_max_3=135
            self.pv_max_4=5520
            self.attaque_max_4=250
            self.defense_max_4=184
            self.pv_max_5=7500
            self.attaque_max_5=339
            self.defense_max_5=250
            self.pv_max_6=10215
            self.attaque_max_6=461
            self.defense_max_6=340

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Plante Carnivore',element[indice_element],2,1,1410,1410,64,57,95)

            self.pv_min_2=1410
            self.attaque_min_2=64
            self.defense_min_2=57
            self.pv_min_3=2145
            self.attaque_min_3=97
            self.defense_min_3=87
            self.pv_min_4=3090
            self.attaque_min_4=140
            self.defense_min_4=126
            self.pv_min_5=4200
            self.attaque_min_5=190
            self.defense_min_5=171
            self.pv_min_6=5715
            self.attaque_min_6=258
            self.defense_min_6=232

            self.pv_max_2=2685
            self.attaque_max_2=121
            self.defense_max_2=109
            self.pv_max_3=3870
            self.attaque_max_3=175
            self.defense_max_3=157
            self.pv_max_4=5265
            self.attaque_max_4=238
            self.defense_max_4=214
            self.pv_max_5=7140
            self.attaque_max_5=323
            self.defense_max_5=291
            self.pv_max_6=9720
            self.attaque_max_6=439
            self.defense_max_6=395

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Plante Carnivore',element[indice_element],2,1,1440,1440,62,57,95)

            self.pv_min_2=1440
            self.attaque_min_2=62
            self.defense_min_2=57
            self.pv_min_3=2175
            self.attaque_min_3=95
            self.defense_min_3=87
            self.pv_min_4=3135
            self.attaque_min_4=136
            self.defense_min_4=126
            self.pv_min_5=4275
            self.attaque_min_5=185
            self.defense_min_5=171
            self.pv_min_6=5805
            self.attaque_min_6=252
            self.defense_min_6=232

            self.pv_max_2=2730
            self.attaque_max_2=118
            self.defense_max_2=109
            self.pv_max_3=3930
            self.attaque_max_3=170
            self.defense_max_3=157
            self.pv_max_4=5340
            self.attaque_max_4=232
            self.defense_max_4=214
            self.pv_max_5=7260
            self.attaque_max_5=315
            self.defense_max_5=291
            self.pv_max_6=9885
            self.attaque_max_6=428
            self.defense_max_6=395

        self.nb_capacites=1

        self.capacite1=PlanteCarnivore.fouet
        self.capacite1_nom='Fouet Liane'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

    def fouet(self,cible):
        self.vol_de_vie+=30
        print('\n',self.surnom,self.attribut,' fouette ',cible.surnom,cible.attribut,' avec une liane!!\n')
        degats=self.calcul_dommages(3.5,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.5,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        self.vol_de_vie-=30


class BoiteDePandore(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Boite de Pandore',element[indice_element],2,1,1275,1275,56,75,92)

            self.pv_min_2=1275
            self.attaque_min_2=56
            self.defense_min_2=75
            self.pv_min_3=1920
            self.attaque_min_3=85
            self.defense_min_3=114
            self.pv_min_4=2775
            self.attaque_min_4=122
            self.defense_min_4=164
            self.pv_min_5=3780
            self.attaque_min_5=166
            self.defense_min_5=223
            self.pv_min_6=5130
            self.attaque_min_6=226
            self.defense_min_6=304

            self.pv_max_2=2415
            self.attaque_max_2=106
            self.defense_max_2=142
            self.pv_max_3=3465
            self.attaque_max_3=153
            self.defense_max_3=205
            self.pv_max_4=4725
            self.attaque_max_4=208
            self.defense_max_4=279
            self.pv_max_5=6420
            self.attaque_max_5=283
            self.defense_max_5=379
            self.pv_max_6=5130
            self.attaque_max_6=384
            self.defense_max_6=516

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Boite de Pandore',element[indice_element],2,1,1200,1200,48,88,92)

            self.pv_min_2=1200
            self.attaque_min_2=48
            self.defense_min_2=88
            self.pv_min_3=1815
            self.attaque_min_3=73
            self.defense_min_3=133
            self.pv_min_4=2625
            self.attaque_min_4=105
            self.defense_min_4=192
            self.pv_min_5=3570
            self.attaque_min_5=143
            self.defense_min_5=261
            self.pv_min_6=4845
            self.attaque_min_6=194
            self.defense_min_6=355

            self.pv_max_2=2280
            self.attaque_max_2=91
            self.defense_max_2=167
            self.pv_max_3=3270
            self.attaque_max_3=131
            self.defense_max_3=240
            self.pv_max_4=4455
            self.attaque_max_4=178
            self.defense_max_4=327
            self.pv_max_5=6060
            self.attaque_max_5=242
            self.defense_max_5=444
            self.pv_max_6=8235
            self.attaque_max_6=329
            self.defense_max_6=604

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Boite de Pandore',element[indice_element],2,1,1320,1320,46,81,92)

            self.pv_min_2=1320
            self.attaque_min_2=46
            self.defense_min_2=81
            self.pv_min_3=1995
            self.attaque_min_3=70
            self.defense_min_3=124
            self.pv_min_4=2880
            self.attaque_min_4=101
            self.defense_min_4=178
            self.pv_min_5=3915
            self.attaque_min_5=138
            self.defense_min_5=242
            self.pv_min_6=5325
            self.attaque_min_6=187
            self.defense_min_6=329

            self.pv_max_2=2505
            self.attaque_max_2=88
            self.defense_max_2=155
            self.pv_max_3=3600
            self.attaque_max_3=127
            self.defense_max_3=223
            self.pv_max_4=4905
            self.attaque_max_4=172
            self.defense_max_4=303
            self.pv_max_5=6660
            self.attaque_max_5=234
            self.defense_max_5=412
            self.pv_max_6=9060
            self.attaque_max_6=318
            self.defense_max_6=560

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Boite de Pandore',element[indice_element],2,1,1290,1290,51,78,92)

            self.pv_min_2=1290
            self.attaque_min_2=51
            self.defense_min_2=78
            self.pv_min_3=1965
            self.attaque_min_3=78
            self.defense_min_3=119
            self.pv_min_4=2835
            self.attaque_min_4=112
            self.defense_min_4=171
            self.pv_min_5=3855
            self.attaque_min_5=152
            self.defense_min_5=233
            self.pv_min_6=5235
            self.attaque_min_6=207
            self.defense_min_6=316

            self.pv_max_2=2460
            self.attaque_max_2=97
            self.defense_max_2=148
            self.pv_max_3=3540
            self.attaque_max_3=140
            self.defense_max_3=214
            self.pv_max_4=4815
            self.attaque_max_4=190
            self.defense_max_4=291
            self.pv_max_5=6540
            self.attaque_max_5=258
            self.defense_max_5=396
            self.pv_max_6=8895
            self.attaque_max_6=351
            self.defense_max_6=538

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Boite de Pandore',element[indice_element],2,1,1320,1320,46,81,92)

            self.pv_min_2=1320
            self.attaque_min_2=46
            self.defense_min_2=81
            self.pv_min_3=1995
            self.attaque_min_3=70
            self.defense_min_3=124
            self.pv_min_4=2880
            self.attaque_min_4=101
            self.defense_min_4=178
            self.pv_min_5=3915
            self.attaque_min_5=138
            self.defense_min_5=242
            self.pv_min_6=5325
            self.attaque_min_6=187
            self.defense_min_6=329

            self.pv_max_2=2505
            self.attaque_max_2=88
            self.defense_max_2=155
            self.pv_max_3=3600
            self.attaque_max_3=127
            self.defense_max_3=223
            self.pv_max_4=4905
            self.attaque_max_4=172
            self.defense_max_4=303
            self.pv_max_5=6660
            self.attaque_max_5=234
            self.defense_max_5=412
            self.pv_max_6=9060
            self.attaque_max_6=318
            self.defense_max_6=560

        self.nb_capacites=1

        self.capacite1=BoiteDePandore.morsure
        self.capacite1_nom='Morsure'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

    def morsure(self,cible):
        print('\n',self.surnom,self.attribut,' mord ',cible.surnom,cible.attribut,'de toutes ses forces!!\n')
        degats=self.calcul_dommages(3.8,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.8,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite == 0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste <= 100*limite_reussite):
                cible.retirer_un_bonus()


class SoldatSquelette(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent']
        indice_element=random.randint(0,2)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Soldat Squelette',element[indice_element],2,1,1005,1005,70,78,99)

            self.pv_min_2=1005
            self.attaque_min_2=70
            self.defense_min_2=78
            self.pv_min_3=1530
            self.attaque_min_3=107
            self.defense_min_3=119
            self.pv_min_4=2205
            self.attaque_min_4=154
            self.defense_min_4=171
            self.pv_min_5=3000
            self.attaque_min_5=209
            self.defense_min_5=233
            self.pv_min_6=4065
            self.attaque_min_6=284
            self.defense_min_6=316

            self.pv_max_2=1905
            self.attaque_max_2=133
            self.defense_max_2=148
            self.pv_max_3=2745
            self.attaque_max_3=192
            self.defense_max_3=214
            self.pv_max_4=3750
            self.attaque_max_4=261
            self.defense_max_4=291
            self.pv_max_5=5085
            self.attaque_max_5=355
            self.defense_max_5=396
            self.pv_max_6=6915
            self.attaque_max_6=483
            self.defense_max_6=538

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Soldat Squelette',element[indice_element],2,1,1080,1080,64,80,99)

            self.pv_min_2=1080
            self.attaque_min_2=64
            self.defense_min_2=80
            self.pv_min_3=1635
            self.attaque_min_3=97
            self.defense_min_3=121
            self.pv_min_4=2355
            self.attaque_min_4=140
            self.defense_min_4=175
            self.pv_min_5=3210
            self.attaque_min_5=190
            self.defense_min_5=238
            self.pv_min_6=4365
            self.attaque_min_6=258
            self.defense_min_6=323

            self.pv_max_2=2040
            self.attaque_max_2=121
            self.defense_max_2=152
            self.pv_max_3=2940
            self.attaque_max_3=175
            self.defense_max_3=218
            self.pv_max_4=4005
            self.attaque_max_4=238
            self.defense_max_4=297
            self.pv_max_5=5445
            self.attaque_max_5=323
            self.defense_max_5=404
            self.pv_max_6=7410
            self.attaque_max_6=439
            self.defense_max_6=549

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Soldat Squelette',element[indice_element],2,1,1050,1050,69,77,99)

            self.pv_min_2=1050
            self.attaque_min_2=69
            self.defense_min_2=77
            self.pv_min_3=1605
            self.attaque_min_3=104
            self.defense_min_3=116
            self.pv_min_4=2310
            self.attaque_min_4=150
            self.defense_min_4=168
            self.pv_min_5=3135
            self.attaque_min_5=204
            self.defense_min_5=228
            self.pv_min_6=4260
            self.attaque_min_6=278
            self.defense_min_6=310

            self.pv_max_2=1995
            self.attaque_max_2=130
            self.defense_max_2=145
            self.pv_max_3=2880
            self.attaque_max_3=188
            self.defense_max_3=209
            self.pv_max_4=3915
            self.attaque_max_4=255
            self.defense_max_4=285
            self.pv_max_5=5325
            self.attaque_max_5=347
            self.defense_max_5=387
            self.pv_max_6=7245
            self.attaque_max_6=472
            self.defense_max_6=527

        self.nb_capacites=2

        self.capacite1=SoldatSquelette.entaille
        self.capacite1_nom='Entaille'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

        self.capacite2=SoldatSquelette.slash
        self.capacite2_nom='Slash Circulaire'
        self.capacite2_bonus_skill=0
        self.temps_recharge2=4
        self.attente2=0
        self.etat_cap2='dispo'

    def entaille(self,cible):
        print('\n',self.surnom,self.attribut,' tranche ',cible.surnom,cible.attribut,' avec son épée!!\n')
        degats=self.calcul_dommages(3.8,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.8,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite == 0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste <= 100*limite_reussite):
                cible.atk_break(2)

    def slash(self,equipe_ennemie):
        for index in range(equipe_ennemie.len):
            print('\n',self.surnom,self.attribut,' tranche toute l\'équipe ennemie avec une attaque circulaire!!\n')
            if (equipe_ennemie.membres[index].pv_actuels > 0):
                print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' reçoit l\'attaque circulaire!!')
                degats=self.calcul_dommages(2.4,self.capacite2_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(2.4,self.capacite2_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(self.priorite_elementaire(equipe_ennemie.membres[index])):
                    equipe_ennemie.membres[index].perturbation_recuperation(2)


class ChauveSouris(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent']
        indice_element=random.randint(0,2)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Chauve Souris',element[indice_element],2,1,930,930,102,51,105)

            self.pv_min_2=930
            self.attaque_min_2=102
            self.defense_min_2=51
            self.pv_min_3=1425
            self.attaque_min_3=155
            self.defense_min_3=78
            self.pv_min_4=2040
            self.attaque_min_4=223
            self.defense_min_4=112
            self.pv_min_5=2775
            self.attaque_min_5=304
            self.defense_min_5=152
            self.pv_min_6=3780
            self.attaque_min_6=413
            self.defense_min_6=207

            self.pv_max_2=1770
            self.attaque_max_2=194
            self.defense_max_2=97
            self.pv_max_3=2550
            self.attaque_max_3=279
            self.defense_max_3=140
            self.pv_max_4=3480
            self.attaque_max_4=380
            self.defense_max_4=190
            self.pv_max_5=4725
            self.attaque_max_5=517
            self.defense_max_5=258
            self.pv_max_6=6420
            self.attaque_max_6=703
            self.defense_max_6=351

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Chauve Souris',element[indice_element],2,1,960,960,96,56,105)

            self.pv_min_2=960
            self.attaque_min_2=96
            self.defense_min_2=56
            self.pv_min_3=1455
            self.attaque_min_3=145
            self.defense_min_3=85
            self.pv_min_4=2100
            self.attaque_min_4=209
            self.defense_min_4=122
            self.pv_min_5=2850
            self.attaque_min_5=285
            self.defense_min_5=166
            self.pv_min_6=3870
            self.attaque_min_6=387
            self.defense_min_6=226

            self.pv_max_2=1815
            self.attaque_max_2=182
            self.defense_max_2=106
            self.pv_max_3=2625
            self.attaque_max_3=262
            self.defense_max_3=153
            self.pv_max_4=3570
            self.attaque_max_4=356
            self.defense_max_4=208
            self.pv_max_5=4845
            self.attaque_max_5=484
            self.defense_max_5=283
            self.pv_max_6=6585
            self.attaque_max_6=659
            self.defense_max_6=384

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Chauve Souris',element[indice_element],2,1,975,975,101,49,105)

            self.pv_min_2=975
            self.attaque_min_2=101
            self.defense_min_2=49
            self.pv_min_3=1485
            self.attaque_min_3=153
            self.defense_min_3=75
            self.pv_min_4=2145
            self.attaque_min_4=220
            self.defense_min_4=108
            self.pv_min_5=2925
            self.attaque_min_5=299
            self.defense_min_5=147
            self.pv_min_6=3975
            self.attaque_min_6=407
            self.defense_min_6=200

            self.pv_max_2=1860
            self.attaque_max_2=191
            self.defense_max_2=94
            self.pv_max_3=2685
            self.attaque_max_3=275
            self.defense_max_3=135
            self.pv_max_4=3660
            self.attaque_max_4=374
            self.defense_max_4=184
            self.pv_max_5=4965
            self.attaque_max_5=509
            self.defense_max_5=250
            self.pv_max_6=6750
            self.attaque_max_6=692
            self.defense_max_6=340

        self.nb_capacites=2

        self.capacite1=ChauveSouris.morsure
        self.capacite1_nom='Morsure'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

        self.capacite2=ChauveSouris.ultrason
        self.capacite2_nom='Ultrason'
        self.capacite2_bonus_skill=0
        self.temps_recharge2=4
        self.attente2=0
        self.etat_cap2='dispo'

    def morsure(self,cible):
        print('\n',self.surnom,self.attribut,' mord ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.6,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.6,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite == 0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste <= 100*limite_reussite):
                cible.def_break(2)

    def ultrason(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,'projette des ultrason sur l équipe ennemie!!\n')
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels > 0):
                print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,'reçoit les ultrasons!!')
                degats=self.calcul_dommages(3.2,self.capacite2_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(3.2,self.capacite2_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite == 0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(0.75,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste <= 100*limite_reussite):
                        print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' perd 30% de sa jauge d\'attaque!!\n')
                        equipe_ennemie.membres[index].jauge_attaque-=max(30,Arrondir.a_l_unite(0.3*equipe_ennemie.membres[index].jauge_attaque))


class Scorpion(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent']
        indice_element=random.randint(0,2)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Scorpion',element[indice_element],2,1,915,915,62,93,103)

            self.pv_min_2=915
            self.attaque_min_2=62
            self.defense_min_2=93
            self.pv_min_3=1380
            self.attaque_min_3=95
            self.defense_min_3=141
            self.pv_min_4=1995
            self.attaque_min_4=136
            self.defense_min_4=203
            self.pv_min_5=2715
            self.attaque_min_5=185
            self.defense_min_5=276
            self.pv_min_6=3675
            self.attaque_min_6=252
            self.defense_min_6=375

            self.pv_max_2=1725
            self.attaque_max_2=118
            self.defense_max_2=176
            self.pv_max_3=2490
            self.attaque_max_3=170
            self.defense_max_3=253
            self.pv_max_4=3390
            self.attaque_max_4=232
            self.defense_max_4=345
            self.pv_max_5=4605
            self.attaque_max_5=315
            self.defense_max_5=468
            self.pv_max_6=6255
            self.attaque_max_6=428
            self.defense_max_6=637

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Scorpion',element[indice_element],2,1,960,960,64,88,103)

            self.pv_min_2=960
            self.attaque_min_2=64
            self.defense_min_2=88
            self.pv_min_3=1455
            self.attaque_min_3=97
            self.defense_min_3=133
            self.pv_min_4=2100
            self.attaque_min_4=140
            self.defense_min_4=192
            self.pv_min_5=2850
            self.attaque_min_5=190
            self.defense_min_5=261
            self.pv_min_6=3870
            self.attaque_min_6=258
            self.defense_min_6=355

            self.pv_max_2=1815
            self.attaque_max_2=121
            self.defense_max_2=167
            self.pv_max_3=2625
            self.attaque_max_3=175
            self.defense_max_3=240
            self.pv_max_4=3570
            self.attaque_max_4=238
            self.defense_max_4=327
            self.pv_max_5=4845
            self.attaque_max_5=323
            self.defense_max_5=444
            self.pv_max_6=6585
            self.attaque_max_6=439
            self.defense_max_6=604

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Scorpion',element[indice_element],2,1,1005,1005,65,83,103)

            self.pv_min_2=1005
            self.attaque_min_2=65
            self.defense_min_2=83
            self.pv_min_3=1530
            self.attaque_min_3=99
            self.defense_min_3=126
            self.pv_min_4=2205
            self.attaque_min_4=143
            self.defense_min_4=182
            self.pv_min_5=3000
            self.attaque_min_5=195
            self.defense_min_5=247
            self.pv_min_6=4065
            self.attaque_min_6=265
            self.defense_min_6=336

            self.pv_max_2=1905
            self.attaque_max_2=124
            self.defense_max_2=158
            self.pv_max_3=2745
            self.attaque_max_3=179
            self.defense_max_3=227
            self.pv_max_4=3750
            self.attaque_max_4=244
            self.defense_max_4=309
            self.pv_max_5=5085
            self.attaque_max_5=331
            self.defense_max_5=420
            self.pv_max_6=6915
            self.attaque_max_6=450
            self.defense_max_6=571

        self.nb_capacites=1

        self.capacite1=Scorpion.griffe
        self.capacite1_nom='Double Griffes'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

    def griffe(self,cible):
        print('\n',self.surnom,self.attribut,' griffe deux fois ',cible.surnom,cible.attribut,'!!\n')
        for index in range(2):
            degats=self.calcul_dommages(1.8,self.capacite1_bonus_skill,cible)
            self.affichage_du_type_de_coup(1.8,self.capacite1_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    cible.degats_continus(1,1)


class Imp(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Imp',element[indice_element],2,1,930,930,88,65,114)

            self.pv_min_2=930
            self.attaque_min_2=88
            self.defense_min_2=65
            self.pv_min_3=1425
            self.attaque_min_3=133
            self.defense_min_3=99
            self.pv_min_4=2040
            self.attaque_min_4=192
            self.defense_min_4=143
            self.pv_min_5=2775
            self.attaque_min_5=261
            self.defense_min_5=195
            self.pv_min_6=3780
            self.attaque_min_6=355
            self.defense_min_6=265

            self.pv_max_2=1770
            self.attaque_max_2=167
            self.defense_max_2=124
            self.pv_max_3=2550
            self.attaque_max_3=240
            self.defense_max_3=179
            self.pv_max_4=3480
            self.attaque_max_4=327
            self.defense_max_4=244
            self.pv_max_5=4725
            self.attaque_max_5=444
            self.defense_max_5=331
            self.pv_max_6=6420
            self.attaque_max_6=604
            self.defense_max_6=450

            self.nb_capacites=2

            self.capacite1=Imp.lance
            self.capacite1_nom='Coup de Lance'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Imp.perforation
            self.capacite2_nom='Perforation'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Imp',element[indice_element],2,1,675,675,94,77,110)

            self.pv_min_2=675
            self.attaque_min_2=94
            self.defense_min_2=77
            self.pv_min_3=1020
            self.attaque_min_3=143
            self.defense_min_3=116
            self.pv_min_4=1470
            self.attaque_min_4=206
            self.defense_min_4=168
            self.pv_min_5=1995
            self.attaque_min_5=280
            self.defense_min_5=228
            self.pv_min_6=2715
            self.attaque_min_6=381
            self.defense_min_6=310

            self.pv_max_2=1275
            self.attaque_max_2=179
            self.defense_max_2=145
            self.pv_max_3=1830
            self.attaque_max_3=258
            self.defense_max_3=209
            self.pv_max_4=2490
            self.attaque_max_4=351
            self.defense_max_4=285
            self.pv_max_5=3390
            self.attaque_max_5=476
            self.defense_max_5=387
            self.pv_max_6=4605
            self.attaque_max_6=648
            self.defense_max_6=527

            self.nb_capacites=2

            self.capacite1=Imp.lance
            self.capacite_nNom='Coup de Lance'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Imp.sphere_infernale
            self.capacite2_nom='Sphère Infernale'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Imp',element[indice_element],2,1,735,735,96,70,115)

            self.pv_min_2=735
            self.attaque_min_2=96
            self.defense_min_2=70
            self.pv_min_3=1125
            self.attaque_min_3=145
            self.defense_min_3=107
            self.pv_min_4=1620
            self.attaque_min_4=209
            self.defense_min_4=154
            self.pv_min_5=2205
            self.attaque_min_5=285
            self.defense_min_5=209
            self.pv_min_6=3000
            self.attaque_min_6=387
            self.defense_min_6=284

            self.pv_max_2=1410
            self.attaque_max_2=182
            self.defense_max_2=133
            self.pv_max_3=2025
            self.attaque_max_3=262
            self.defense_max_3=192
            self.pv_max_4=2760
            self.attaque_max_4=356
            self.defense_max_4=261
            self.pv_max_5=3750
            self.attaque_max_5=484
            self.defense_max_5=355
            self.pv_max_6=5100
            self.attaque_max_6=659
            self.defense_max_6=483

            self.nb_capacites=2

            self.capacite1=Imp.lance
            self.capacite1_nom='Coup de Lance'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Imp.perforation
            self.capacite2_nom='Perforation'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Imp',element[indice_element],2,1,1050,1050,81,64,112)

            self.pv_min_2=1050
            self.attaque_min_2=81
            self.defense_min_2=64
            self.pv_min_3=1605
            self.attaque_min_3=124
            self.defense_min_3=97
            self.pv_min_4=2310
            self.attaque_min_4=178
            self.defense_min_4=140
            self.pv_min_5=3135
            self.attaque_min_5=242
            self.defense_min_5=190
            self.pv_min_6=4260
            self.attaque_min_6=329
            self.defense_min_6=258

            self.pv_max_2=1995
            self.attaque_max_2=155
            self.defense_max_2=121
            self.pv_max_3=2880
            self.attaque_max_3=223
            self.defense_max_3=175
            self.pv_max_4=3915
            self.attaque_max_4=303
            self.defense_max_4=238
            self.pv_max_5=5325
            self.attaque_max_5=412
            self.defense_max_5=323
            self.pv_max_6=7245
            self.attaque_max_6=560
            self.defense_max_6=439

            self.nb_capacites=2

            self.capacite1=Imp.lance
            self.capacite1_nom='Coup de Lance'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Imp.sphere_infernale
            self.capacite2_nom='Sphère Infernale'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Imp',element[indice_element],2,1,960,960,88,64,113)

            self.pv_min_2=960
            self.attaque_min_2=88
            self.defense_min_2=64
            self.pv_min_3=1455
            self.attaque_min_3=133
            self.defense_min_3=97
            self.pv_min_4=2100
            self.attaque_min_4=192
            self.defense_min_4=140
            self.pv_min_5=2850
            self.attaque_min_5=261
            self.defense_min_5=190
            self.pv_min_6=3870
            self.attaque_min_6=355
            self.defense_min_6=258

            self.pv_max_2=1815
            self.attaque_max_2=167
            self.defense_max_2=121
            self.pv_max_3=2625
            self.attaque_max_3=240
            self.defense_max_3=175
            self.pv_max_4=3570
            self.attaque_max_4=327
            self.defense_max_4=238
            self.pv_max_5=4845
            self.attaque_max_5=444
            self.defense_max_5=323
            self.pv_max_6=6585
            self.attaque_max_6=604
            self.defense_max_6=439

            self.nb_capacites=2

            self.capacite1=Imp.lance
            self.capacite1_nom='Coup de Lance'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Imp.perforation
            self.capacite2_nom='Perforation'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'


    def lance(self,cible):
        print('\n',self.surnom,self.attribut,' plante sa lance dans ',cible.surnom,cible.attribut,'!!\n')
        degats=-20+self.calcul_dommages(3.7,self.capacite1_bonus_skill,cible)
        type_coup=self.affichage_du_type_de_coup(3.7,self.capacite1_bonus_skill,degats+20,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(type_coup=='Critique'):
            self.speed_up(2)

    def sphere_infernale(self,cible):
        print('\n',self.surnom,self.attribut,' projette une sphère infernale sur ',cible.surnom,cible.attribut,'!!\n')
        degats=50+self.calcul_dommages(4.8,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(4.8,self.capacite2_bonus_skill,degats-50,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.pv_actuels>0):
            if(self.attribut=='Lumière'):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1
            elif(self.attribut=='Eau'):
                print(cible.surnom,cible.attribut,' est gelé(e)!! \n')
                cible.gel=1

    def perforation(self,cible):
        print('\n',self.surnom,self.attribut,' plante profondément sa lance dans le coeur de ',cible.surnom,cible.attribut,'!!\n')
        self.taux_coup_critique_actuel+=50
        degats=50+self.calcul_dommages(5.2,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(5.2,self.capacite2_bonus_skill,degats-50,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        self.taux_coup_critique_actuel-=50


class Lutin(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Lutin',element[indice_element],2,1,885,885,93,64,110)

            self.pv_min_2=885
            self.attaque_min_2=93
            self.defense_min_2=64
            self.pv_min_3=1350
            self.attaque_min_3=141
            self.defense_min_3=97
            self.pv_min_4=1935
            self.attaque_min_4=203
            self.defense_min_4=140
            self.pv_min_5=2640
            self.attaque_min_5=276
            self.defense_min_5=190
            self.pv_min_6=3585
            self.attaque_min_6=375
            self.defense_min_6=258

            self.pv_max_2=1680
            self.attaque_max_2=176
            self.defense_max_2=121
            self.pv_max_3=2415
            self.attaque_max_3=253
            self.defense_max_3=175
            self.pv_max_4=3300
            self.attaque_max_4=345
            self.defense_max_4=238
            self.pv_max_5=4485
            self.attaque_max_5=468
            self.defense_max_5=323
            self.pv_max_6=6090
            self.attaque_max_6=637
            self.defense_max_6=439

            self.nb_capacites=2

            self.capacite1=Lutin.sphere_sacree
            self.capacite1_nom='Sphère Sacrée'
            self.capacite1BonusSkill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Lutin.ignition
            self.capacite2_nom='Ignition'
            self.capacite2BonusSkill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Lutin',element[indice_element],2,1,1200,1200,72,64,110)

            self.pv_min_2=1200
            self.attaque_min_2=72
            self.defense_min_2=64
            self.pv_min_3=1815
            self.attaque_min_3=109
            self.defense_min_3=97
            self.pv_min_4=2625
            self.attaque_min_4=157
            self.defense_min_4=140
            self.pv_min_5=3570
            self.attaque_min_5=214
            self.defense_min_5=190
            self.pv_min_6=4845
            self.attaque_min_6=291
            self.defense_min_6=258

            self.pv_max_2=2280
            self.attaque_max_2=136
            self.defense_max_2=121
            self.pv_max_3=3270
            self.attaque_max_3=196
            self.defense_max_3=175
            self.pv_max_4=4455
            self.attaque_max_4=267
            self.defense_max_4=238
            self.pv_max_5=6060
            self.attaque_max_5=363
            self.defense_max_5=323
            self.pv_max_6=8235
            self.attaque_max_6=494
            self.defense_max_6=439

            self.nb_capacites=2

            self.capacite1=Lutin.sphere_sacree
            self.capacite1_nom='Sphère Sacrée'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Lutin.deceleration
            self.capacite2_nom='Décélération'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Lutin',element[indice_element],2,1,1080,1080,69,75,110)

            self.pv_min_2=1080
            self.attaque_min_2=69
            self.defense_min_2=75
            self.pv_min_3=1635
            self.attaque_min_3=104
            self.defense_min_3=114
            self.pv_min_4=2355
            self.attaque_min_4=150
            self.defense_min_4=164
            self.pv_min_5=3210
            self.attaque_min_5=204
            self.defense_min_5=223
            self.pv_min_6=4365
            self.attaque_min_6=278
            self.defense_min_6=304

            self.pv_max_2=2040
            self.attaque_max_2=130
            self.defense_max_2=142
            self.pv_max_3=2940
            self.attaque_max_3=188
            self.defense_max_3=205
            self.pv_max_4=4005
            self.attaque_max_4=255
            self.defense_max_4=279
            self.pv_max_5=5445
            self.attaque_max_5=347
            self.defense_max_5=379
            self.pv_max_6=7410
            self.attaque_max_6=472
            self.defense_max_6=516

            self.nb_capacites=2

            self.capacite1=Lutin.sphere_sacree
            self.capacite1_nom='Sphère Sacrée'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Lutin.deceleration
            self.capacite2_nom='Décélération'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Lutin',element[indice_element],2,1,1050,1050,80,65,110)

            self.pv_min_2=1050
            self.attaque_min_2=80
            self.defense_min_2=65
            self.pv_min_3=1605
            self.attaque_min_3=121
            self.defense_min_3=99
            self.pv_min_4=2310
            self.attaque_min_4=175
            self.defense_min_4=143
            self.pv_min_5=3135
            self.attaque_min_5=238
            self.defense_min_5=195
            self.pv_min_6=4260
            self.attaque_min_6=323
            self.defense_min_6=265

            self.pv_max_2=1995
            self.attaque_max_2=152
            self.defense_max_2=124
            self.pv_max_3=2880
            self.attaque_max_3=218
            self.defense_max_3=179
            self.pv_max_4=3915
            self.attaque_max_4=297
            self.defense_max_4=244
            self.pv_max_5=5325
            self.attaque_max_5=404
            self.defense_max_5=331
            self.pv_max_6=7245
            self.attaque_max_6=549
            self.defense_max_6=450

            self.nb_capacites=2

            self.capacite1=Lutin.sphere_sacree
            self.capacite1_nom='Sphère Sacrée'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Lutin.ignition
            self.capacite2_nom='Ignition'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Lutin',element[indice_element],2,1,1005,1005,86,62,110)

            self.pv_min_2=1005
            self.attaque_min_2=86
            self.defense_min_2=62
            self.pv_min_3=1530
            self.attaque_min_3=131
            self.defense_min_3=95
            self.pv_min_4=2205
            self.attaque_min_4=189
            self.defense_min_4=136
            self.pv_min_5=3000
            self.attaque_min_5=257
            self.defense_min_5=185
            self.pv_min_6=4065
            self.attaque_min_6=349
            self.defense_min_6=252

            self.pv_max_2=1905
            self.attaque_max_2=164
            self.defense_max_2=118
            self.pv_max_3=2745
            self.attaque_max_3=236
            self.defense_max_3=170
            self.pv_max_4=3750
            self.attaque_max_4=321
            self.defense_max_4=232
            self.pv_max_5=5085
            self.attaque_max_5=436
            self.defense_max_5=315
            self.pv_max_6=6915
            self.attaque_max_6=593
            self.defense_max_6=428

            self.nb_capacites=2

            self.capacite1=Lutin.sphere_sacree
            self.capacite1_nom='Sphère Sacrée'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Lutin.deceleration
            self.capacite2_nom='Décélération'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

    def sphere_sacree(self,cible):
        print('\n',self.surnom,self.attribut,' projette une sphère sacrée sur ',cible.surnom,cible.attribut,'!!\n')
        degats=20+self.calcul_dommages(3.6,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.6,self.capacite1_bonus_skill,degats-20,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.slow_down(2)

    def deceleration(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,'lance un sort de décélération sur l équipe ennemie!!\n')
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels>0):
                print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,'reçoit le sort de décélération!!')
                degats=self.calcul_dommages(2.1,self.capacite2_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(2.1,self.capacite2_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(0.8,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        self.slow_down(equipe_ennemie.membres[index],2)

    def Ignition(self,cible):
        print('\n',self.surnom,self.attribut,' réduit ',cible.surnom,cible.attribut,' en cendres avec un sort de feu!!\n')
        degats=90+self.calcul_dommages(4.6,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(4.6,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        cible.degats_continus(1,3)


class Yeti(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Yeti',element[indice_element],2,1,1155,1155,75,64,100)

            self.pv_min_2=1155
            self.attaque_min_2=75
            self.defense_min_2=64
            self.pv_min_3=1740
            self.attaque_min_3=114
            self.defense_min_3=97
            self.pv_min_4=2520
            self.attaque_min_4=164
            self.defense_min_4=140
            self.pv_min_5=3420
            self.attaque_min_5=223
            self.defense_min_5=190
            self.pv_min_6=4650
            self.attaque_min_6=304
            self.defense_min_6=258

            self.pv_max_2=2175
            self.attaque_max_2=142
            self.defense_max_2=121
            self.pv_max_3=3135
            self.attaque_max_3=205
            self.defense_max_3=175
            self.pv_max_4=4275
            self.attaque_max_4=279
            self.defense_max_4=238
            self.pv_max_5=5805
            self.attaque_max_5=379
            self.defense_max_5=323
            self.pv_max_6=7905
            self.attaque_max_6=516
            self.defense_max_6=439

            self.nb_capacites=2

            self.capacite1=Yeti.poing
            self.capacite1_nom='Poing d Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Yeti.ecrasement
            self.capacite2_nom='Ecrasement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Yeti',element[indice_element],2,1,1335,1335,53,73,100)

            self.pv_min_2=1335
            self.attaque_min_2=53
            self.defense_min_2=73
            self.pv_min_3=2040
            self.attaque_min_3=80
            self.defense_min_3=112
            self.pv_min_4=2940
            self.attaque_min_4=115
            self.defense_min_4=161
            self.pv_min_5=3990
            self.attaque_min_5=157
            self.defense_min_5=219
            self.pv_min_6=5430
            self.attaque_min_6=213
            self.defense_min_6=297

            self.pv_max_2=2550
            self.attaque_max_2=100
            self.defense_max_2=139
            self.pv_max_3=3660
            self.attaque_max_3=144
            self.defense_max_3=201
            self.pv_max_4=4995
            self.attaque_max_4=196
            self.defense_max_4=273
            self.pv_max_5=6780
            self.attaque_max_5=266
            self.defense_max_5=371
            self.pv_max_6=9225
            self.attaque_max_6=362
            self.defense_max_6=505

            self.nb_capacites=2

            self.capacite1=Yeti.poing
            self.capacite1_nom='Poing d Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Yeti.smash
            self.capacite2_nom='Smash Lourd'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Yeti',element[indice_element],2,1,1155,1155,61,78,100)

            self.pv_min_2=1155
            self.attaque_min_2=61
            self.defense_min_2=78
            self.pv_min_3=1740
            self.attaque_min_3=92
            self.defense_min_3=119
            self.pv_min_4=2520
            self.attaque_min_4=133
            self.defense_min_4=171
            self.pv_min_5=3420
            self.attaque_min_5=181
            self.defense_min_5=233
            self.pv_min_6=4650
            self.attaque_min_6=245
            self.defense_min_6=316

            self.pv_max_2=2175
            self.attaque_max_2=115
            self.defense_max_2=148
            self.pv_max_3=3135
            self.attaque_max_3=166
            self.defense_max_3=214
            self.pv_max_4=4275
            self.attaque_max_4=226
            self.defense_max_4=291
            self.pv_max_5=5805
            self.attaque_max_5=307
            self.defense_max_5=396
            self.pv_max_6=7905
            self.attaque_max_6=417
            self.defense_max_6=538

            self.nb_capacites=2

            self.capacite1=Yeti.poing
            self.capacite1_nom='Poing d Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Yeti.smash
            self.capacite2_nom='Smash Lourd'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Yeti',element[indice_element],2,1,1095,1095,56,86,100)

            self.pv_min_2=1085
            self.attaque_min_2=56
            self.defense_min_2=86
            self.pv_min_3=1680
            self.attaque_min_3=85
            self.defense_min_3=131
            self.pv_min_4=2415
            self.attaque_min_4=122
            self.defense_min_4=189
            self.pv_min_5=3285
            self.attaque_min_5=166
            self.defense_min_5=257
            self.pv_min_6=4455
            self.attaque_min_6=226
            self.defense_min_6=349

            self.pv_max_2=2085
            self.attaque_max_2=106
            self.defense_max_2=164
            self.pv_max_3=3015
            self.attaque_max_3=153
            self.defense_max_3=236
            self.pv_max_4=4095
            self.attaque_max_4=208
            self.defense_max_4=321
            self.pv_max_5=5565
            self.attaque_max_5=283
            self.defense_max_5=436
            self.pv_max_6=7575
            self.attaque_max_6=384
            self.defense_max_6=593

            self.nb_capacites=2

            self.capacite1=Yeti.poing
            self.capacite1_nom='Poing d Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Yeti.smash
            self.capacite2_nom='Smash Lourd'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Yeti',element[indice_element],3,1,2250,2250,99,114,100)

            self.pv_min_3=2250
            self.attaque_min_3=99
            self.defense_min_3=114
            self.pv_min_4=3240
            self.attaque_min_4=143
            self.defense_min_4=164
            self.pv_min_5=4425
            self.attaque_min_5=195
            self.defense_min_5=223
            self.pv_min_6=6000
            self.attaque_min_6=265
            self.defense_min_6=304

            self.pv_max_3=4065
            self.attaque_max_3=179
            self.defense_max_3=205
            self.pv_max_4=5520
            self.attaque_max_4=244
            self.defense_max_4=279
            self.pv_max_5=7500
            self.attaque_max_5=331
            self.defense_max_5=379
            self.pv_max_6=10215
            self.attaque_max_6=450
            self.defense_max_6=516

            self.nb_capacites=2

            self.capacite1=Yeti.poing
            self.capacite1_nom='Poing d Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Yeti.ecrasement
            self.capacite2_nom='Ecrasement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

    def poing(self,cible):
        print('\n',self.surnom,self.attribut,' écrase son poing monstrueux sur ',cible.surnom,cible.attribut,'!!\n')
        for index in range(2):
            degats=20+self.calcul_dommages(1.9,self.capacite1_bonus_skill,cible)
            self.affichage_du_type_de_coup(1.9,self.capacite1_bonus_skill,degats-20,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    cible.slow_down(1)

    def smash(self,cible):
        print('\n',self.surnom,self.attribut,' frappe violemment ',cible.surnom,cible.attribut,'!!\n')
        for index in range(2):
            degats=(Arrondir.a_l_unite(1.5*self.defense_actuelle))+self.calcul_dommages(1.5,self.capacite2_bonus_skill,cible)
            self.affichage_du_type_de_coup(1.5,self.capacite2_bonus_skill,degats-(Arrondir.a_l_unite(1.5*self.defense_actuelle)),cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.3,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                    cible.stun=1

    def ecrasement(self,cible):
        print('\n',self.surnom,self.attribut,' écrase ',cible.surnom,cible.attribut,' de tout son poids!!\n')
        for index in range(2):
            degats=(Arrondir.a_l_unite(0.28*self.pv_max_donjons))+self.calcul_dommages(2.0,self.capacite2_bonus_skill,cible)
            self.affichage_du_type_de_coup(2.0,self.capacite2_bonus_skill,degats-(Arrondir.a_l_unite(0.28*self.pv_max_donjons)),cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    cible.slow_down(2)


class Cerbere(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Cerbere',element[indice_element],2,1,915,915,99,56,109)

            self.pv_min_2=915
            self.attaque_min_2=99
            self.defense_min_2=56
            self.pv_min_3=1380
            self.attaque_min_3=150
            self.defense_min_3=85
            self.pv_min_4=1995
            self.attaque_min_4=216
            self.defense_min_4=122
            self.pv_min_5=2715
            self.attaque_min_5=295
            self.defense_min_5=166
            self.pv_min_6=3675
            self.attaque_min_6=400
            self.defense_min_6=226

            self.pv_max_2=1725
            self.attaque_max_2=188
            self.defense_max_2=106
            self.pv_max_3=2490
            self.attaque_max_3=271
            self.defense_max_3=153
            self.pv_max_4=3390
            self.attaque_max_4=368
            self.defense_max_4=208
            self.pv_max_5=4605
            self.attaque_max_5=500
            self.defense_max_5=283
            self.pv_max_6=6255
            self.attaque_max_6=681
            self.defense_max_6=384

            self.nb_capacites=2

            self.capacite1=Cerbere.morsure
            self.capacite1_nom='Morsure'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Cerbere.double_morsure
            self.capacite2_nom='Double Morsure'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Cerbere',element[indice_element],2,1,975,975,89,61,114)

            self.pv_min_2=975
            self.attaque_min_2=89
            self.defense_min_2=61
            self.pv_min_3=1485
            self.attaque_min_3=136
            self.defense_min_3=92
            self.pv_min_4=2145
            self.attaque_min_4=196
            self.defense_min_4=133
            self.pv_min_5=2925
            self.attaque_min_5=266
            self.defense_min_5=181
            self.pv_min_6=3975
            self.attaque_min_6=362
            self.defense_min_6=245

            self.pv_max_2=1860
            self.attaque_max_2=170
            self.defense_max_2=115
            self.pv_max_3=2685
            self.attaque_max_3=244
            self.defense_max_3=166
            self.pv_max_4=3660
            self.attaque_max_4=333
            self.defense_max_4=226
            self.pv_max_5=4965
            self.attaque_max_5=452
            self.defense_max_5=307
            self.pv_max_6=6750
            self.attaque_max_6=615
            self.defense_max_6=417

            self.nb_capacites=2

            self.capacite1=Cerbere.morsure
            self.capacite1_nom='Morsure'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Cerbere.embuscade
            self.capacite2_nom='Embuscade'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Cerbere',element[indice_element],2,1,1035,1035,96,51,112)

            self.pv_min_2=1035
            self.attaque_min_2=96
            self.defense_min_2=51
            self.pv_min_3=1560
            self.attaque_min_3=145
            self.defense_min_3=78
            self.pv_min_4=2250
            self.attaque_min_4=209
            self.defense_min_4=112
            self.pv_min_5=3060
            self.attaque_min_5=285
            self.defense_min_5=152
            self.pv_min_6=4170
            self.attaque_min_6=387
            self.defense_min_6=207

            self.pv_max_2=1950
            self.attaque_max_2=182
            self.defense_max_2=97
            self.pv_max_3=2820
            self.attaque_max_3=262
            self.defense_max_3=140
            self.pv_max_4=3825
            self.attaque_max_4=356
            self.defense_max_4=190
            self.pv_max_5=5205
            self.attaque_max_5=484
            self.defense_max_5=258
            self.pv_max_6=7080
            self.attaque_max_6=659
            self.defense_max_6=351

            self.nb_capacites=2

            self.capacite1=Cerbere.morsure
            self.capacite1_nom='Morsure'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Cerbere.double_morsure
            self.capacite2_nom='Double Morsure'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Cerbere',element[indice_element],2,1,1080,1080,89,54,110)

            self.pv_min_2=1080
            self.attaque_min_2=89
            self.defense_min_2=54
            self.pv_min_3=1635
            self.attaque_min_3=136
            self.defense_min_3=82
            self.pv_min_4=2355
            self.attaque_min_4=196
            self.defense_min_4=119
            self.pv_min_5=3210
            self.attaque_min_5=266
            self.defense_min_5=162
            self.pv_min_6=4365
            self.attaque_min_6=362
            self.defense_min_6=220

            self.pv_max_2=2040
            self.attaque_max_2=170
            self.defense_max_2=103
            self.pv_max_3=2940
            self.attaque_max_3=244
            self.defense_max_3=148
            self.pv_max_4=4005
            self.attaque_max_4=333
            self.defense_max_4=202
            self.pv_max_5=5445
            self.attaque_max_5=452
            self.defense_max_5=274
            self.pv_max_6=7410
            self.attaque_max_6=615
            self.defense_max_6=373

            self.nb_capacites=2

            self.capacite1=Cerbere.morsure
            self.capacite1_nom='Morsure'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Cerbere.double_morsure
            self.capacite2_nom='Double Morsure'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Cerbere',element[indice_element],3,1,1380,1380,167,104,112)

            self.pv_min_3=1380
            self.attaque_min_3=167
            self.defense_min_3=104
            self.pv_min_4=1995
            self.attaque_min_4=241
            self.defense_min_4=150
            self.pv_min_5=2715
            self.attaque_min_5=328
            self.defense_min_5=204
            self.pv_min_6=3675
            self.attaque_min_6=446
            self.defense_min_6=278

            self.pv_max_3=2490
            self.attaque_max_3=301
            self.defense_max_3=188
            self.pv_max_4=3390
            self.attaque_max_4=410
            self.defense_max_4=255
            self.pv_max_5=4605
            self.attaque_max_5=557
            self.defense_max_5=347
            self.pv_max_6=6255
            self.attaque_max_6=758
            self.defense_max_6=472

            self.nb_capacites=2

            self.capacite1=Cerbere.morsure
            self.capacite1_nom='Morsure'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Cerbere.embuscade
            self.capacite2_nom='Embuscade'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

    def morsure(self,cible):
        self.vol_de_vie+=30
        print('\n',self.surnom,self.attribut,' mord ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.6,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.6,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        self.vol_de_vie-=30

    def double_morsure(self,cible):
        print('\n',self.surnom,self.attribut,' mords deux fois ',cible.surnom,cible.attribut,'!!\n')
        for index in range(2):
            degats=self.calcul_dommages(3.7,self.capacite2_bonus_skill,cible)
            self.affichage_du_type_de_coup(3.7,self.capacite2_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)

    def embuscade(self,cible):
        print('\n',self.surnom,self.attribut,' lacère ',cible.surnom,cible.attribut,' à une vitesse incroyable!!\n')
        degats=2*(140+self.vitesse_actuelle+self.capacite2_bonus_skill)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        self.speed_up(2)


class OursDeGuerre(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Ours de Guerre',element[indice_element],2,1,1125,1125,78,62,101)

            self.pv_min_2=1125
            self.attaque_min_2=78
            self.defense_min_2=62
            self.pv_min_3=1710
            self.attaque_min_3=119
            self.defense_min_3=95
            self.pv_min_4=2460
            self.attaque_min_4=171
            self.defense_min_4=136
            self.pv_min_5=3345
            self.attaque_min_5=233
            self.defense_min_5=185
            self.pv_min_6=4560
            self.attaque_min_6=316
            self.defense_min_6=252

            self.pv_max_2=2130
            self.attaque_max_2=148
            self.defense_max_2=118
            self.pv_max_3=3075
            self.attaque_max_3=214
            self.defense_max_3=170
            self.pv_max_4=4185
            self.attaque_max_4=291
            self.defense_max_4=232
            self.pv_max_5=5685
            self.attaque_max_5=396
            self.defense_max_5=315
            self.pv_max_6=7740
            self.attaque_max_6=538
            self.defense_max_6=428

            self.nb_capacites=2

            self.capacite1=OursDeGuerre.griffe
            self.capacite1_nom='Griffe Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=OursDeGuerre.rugissement
            self.capacite2_nom='Rugissement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=5
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Ours de Guerre',element[indice_element],3,1,2325,2325,85,124,101)

            self.pv_min_3=2325
            self.attaque_min_3=85
            self.defense_min_3=124
            self.pv_min_4=3345
            self.attaque_min_4=122
            self.defense_min_4=178
            self.pv_min_5=4560
            self.attaque_min_5=166
            self.defense_min_5=242
            self.pv_min_6=6195
            self.attaque_min_6=226
            self.defense_min_6=329

            self.pv_max_3=4185
            self.attaque_max_3=153
            self.defense_max_3=223
            self.pv_max_4=5700
            self.attaque_max_4=208
            self.defense_max_4=303
            self.pv_max_5=7755
            self.attaque_max_5=283
            self.defense_max_5=412
            self.pv_max_6=10545
            self.attaque_max_6=384
            self.defense_max_6=560

            self.nb_capacites=2

            self.capacite1=OursDeGuerre.griffe
            self.capacite1_nom='Griffe Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=OursDeGuerre.abnegation
            self.capacite2_nom='Abnégation'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=5
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Ours de Guerre',element[indice_element],2,1,1290,1290,54,75,101)

            self.pv_min_2=1290
            self.attaque_min_2=54
            self.defense_min_2=75
            self.pv_min_3=1965
            self.attaque_min_3=82
            self.defense_min_3=114
            self.pv_min_4=2835
            self.attaque_min_4=119
            self.defense_min_4=164
            self.pv_min_5=3855
            self.attaque_min_5=162
            self.defense_min_5=223
            self.pv_min_6=5235
            self.attaque_min_6=220
            self.defense_min_6=304

            self.pv_max_2=2460
            self.attaque_max_2=103
            self.defense_max_2=142
            self.pv_max_3=3540
            self.attaque_max_3=148
            self.defense_max_3=205
            self.pv_max_4=4815
            self.attaque_max_4=202
            self.defense_max_4=279
            self.pv_max_5=6540
            self.attaque_max_5=274
            self.defense_max_5=379
            self.pv_max_6=8895
            self.attaque_max_6=373
            self.defense_max_6=516

            self.nb_capacites=2

            self.capacite1=OursDeGuerre.griffe
            self.capacite1_nom='Griffe Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=OursDeGuerre.abnegation
            self.capacite2_nom='Abnégation'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=5
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Ours de Guerre',element[indice_element],3,1,2250,2250,75,138,101)

            self.pv_min_3=2250
            self.attaque_min_3=75
            self.defense_min_3=138
            self.pv_min_4=3240
            self.attaque_min_4=108
            self.defense_min_4=199
            self.pv_min_5=4425
            self.attaque_min_5=147
            self.defense_min_5=271
            self.pv_min_6=6000
            self.attaque_min_6=200
            self.defense_min_6=368

            self.pv_max_3=4065
            self.attaque_max_3=135
            self.defense_max_3=249
            self.pv_max_4=5520
            self.attaque_max_4=184
            self.defense_max_4=339
            self.pv_max_5=7500
            self.attaque_max_5=250
            self.defense_max_5=460
            self.pv_max_6=10215
            self.attaque_max_6=340
            self.defense_max_6=626

            self.nb_capacites=2

            self.capacite1=OursDeGuerre.griffe
            self.capacite1_nom='Griffe Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=OursDeGuerre.abnegation
            self.capacite2_nom='Abnégation'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=5
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Ours de Guerre',element[indice_element],2,1,1080,1080,48,96,101)

            self.pv_min_2=1080
            self.attaque_min_2=48
            self.defense_min_2=96
            self.pv_min_3=1635
            self.attaque_min_3=73
            self.defense_min_3=145
            self.pv_min_4=2355
            self.attaque_min_4=105
            self.defense_min_4=209
            self.pv_min_5=3210
            self.attaque_min_5=143
            self.defense_min_5=285
            self.pv_min_6=4365
            self.attaque_min_6=194
            self.defense_min_6=387

            self.pv_max_2=2040
            self.attaque_max_2=91
            self.defense_max_2=182
            self.pv_max_3=2940
            self.attaque_max_3=131
            self.defense_max_3=262
            self.pv_max_4=4005
            self.attaque_max_4=178
            self.defense_max_4=356
            self.pv_max_5=5445
            self.attaque_max_5=242
            self.defense_max_5=484
            self.pv_max_6=7410
            self.attaque_max_6=329
            self.defense_max_6=659

            self.nb_capacites=2

            self.capacite1=OursDeGuerre.griffe
            self.capacite1_nom='Griffe Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=OursDeGuerre.rugissement
            self.capacite2_nom='Rugissement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=5
            self.attente2=0
            self.etat_cap2='dispo'

    def griffe(self,cible):
        print('\n',self.surnom,self.attribut,' griffe violemment ',cible.surnom,cible.attribut,'!!\n')
        degats=(Arrondir.a_l_unite(0.15*self.pv_max_donjons))+self.calcul_dommages(1.7,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(1.7,self.capacite1_bonus_skill,degats-(Arrondir.a_l_unite(0.15*self.pv_max_donjons)),cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                print(cible.surnom,cible.attribut,' perd un quart de sa jauge d\'attaque!!\n')
                cible.jauge_attaque-=max(25,Arrondir.a_l_unite(0.25*cible.jauge_attaque))

    def rugissement(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' rugit sur l équipe ennemie!!\n')
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels>0):
                print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,'reçoit le rugissement!!')
                degats=Arrondir.a_l_unite(0.2*self.pv_max_donjons)
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(1,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        equipe_ennemie.membres[index].atk_break(2)

    def abnegation(self):
        if(self.pv_actuels>0):
            print('\n',self.surnom,self.attribut,' érige une barrière spirituelle!!\n')
            if (self.perturbation_recup<=0):
                montant=Arrondir.a_l_unite(0.3*self.pv_max_donjons)
                self.etre_soigne(montant)
            else:
                print('La récupération de points de vie de ',self.surnom,self.attribut,' est actuellement entravée!! \n')
            print('Il reste ',self.pv_actuels,' point(s) de vie sur',self.pv_max_donjons,' à ',self.surnom,self.attribut,'!! \n')
            self.tanky(2)


class Elementaire(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Elementaire',element[indice_element],2,1,1035,1035,80,67,106)

            self.pv_min_2=1035
            self.attaque_min_2=80
            self.defense_min_2=67
            self.pv_min_3=1560
            self.attaque_min_3=121
            self.defense_min_3=102
            self.pv_min_4=2250
            self.attaque_min_4=175
            self.defense_min_4=147
            self.pv_min_5=3060
            self.attaque_min_5=238
            self.defense_min_5=200
            self.pv_min_6=4170
            self.attaque_min_6=323
            self.defense_min_6=271

            self.pv_max_2=1950
            self.attaque_max_2=152
            self.defense_max_2=127
            self.pv_max_3=2820
            self.attaque_max_3=218
            self.defense_max_3=183
            self.pv_max_4=3825
            self.attaque_max_4=297
            self.defense_max_4=250
            self.pv_max_5=5205
            self.attaque_max_5=404
            self.defense_max_5=339
            self.pv_max_6=7080
            self.attaque_max_6=549
            self.defense_max_6=461

            self.nb_capacites=2

            self.capacite1=Elementaire.griffe
            self.capacite1_nom='Griffe Elementaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Elementaire.explosion
            self.capacite2_nom='Explosion Elementaire'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Elementaire',element[indice_element],2,1,915,915,99,56,106)

            self.pv_min_2=915
            self.attaque_min_2=99
            self.defense_min_2=56
            self.pv_min_3=1380
            self.attaque_min_3=150
            self.defense_min_3=85
            self.pv_min_4=1995
            self.attaque_min_4=216
            self.defense_min_4=122
            self.pv_min_5=2715
            self.attaque_min_5=295
            self.defense_min_5=166
            self.pv_min_6=3675
            self.attaque_min_6=400
            self.defense_min_6=26

            self.pv_max_2=1725
            self.attaque_max_2=188
            self.defense_max_2=106
            self.pv_max_3=2490
            self.attaque_max_3=271
            self.defense_max_3=153
            self.pv_max_4=3390
            self.attaque_max_4=368
            self.defense_max_4=208
            self.pv_max_5=4605
            self.attaque_max_5=500
            self.defense_max_5=283
            self.pv_max_6=6255
            self.attaque_max_6=681
            self.defense_max_6=384

            self.nb_capacites=2

            self.capacite1=Elementaire.griffe
            self.capacite1_nom='Griffe Elementaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Elementaire.explosion
            self.capacite2_nom='Explosion Elementaire'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Elementaire',element[indice_element],2,1,855,855,104,54,106)

            self.pv_min_2=855
            self.attaque_min_2=104
            self.defense_min_2=54
            self.pv_min_3=1305
            self.attaque_min_3=158
            self.defense_min_3=82
            self.pv_min_4=1890
            self.attaque_min_4=227
            self.defense_min_4=119
            self.pv_min_5=2565
            self.attaque_min_5=309
            self.defense_min_5=162
            self.pv_min_6=3480
            self.attaque_min_6=420
            self.defense_min_6=220

            self.pv_max_2=1635
            self.attaque_max_2=197
            self.defense_max_2=103
            self.pv_max_3=2355
            self.attaque_max_3=284
            self.defense_max_3=148
            self.pv_max_4=3210
            self.attaque_max_4=386
            self.defense_max_4=202
            self.pv_max_5=4365
            self.attaque_max_5=525
            self.defense_max_5=274
            self.pv_max_6=5925
            self.attaque_max_6=714
            self.defense_max_6=373

            self.nb_capacites=2

            self.capacite1=Elementaire.griffe
            self.capacite1_nom='Griffe Elementaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Elementaire.renforcement
            self.capacite2_nom='Renforcement Elementaire'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Elementaire',element[indice_element],3,1,1680,1680,138,114,106)

            self.pv_min_3=1680
            self.attaque_min_3=138
            self.defense_min_3=114
            self.pv_min_4=2415
            self.attaque_min_4=199
            self.defense_min_4=164
            self.pv_min_5=3285
            self.attaque_min_5=271
            self.defense_min_5=223
            self.pv_min_6=4455
            self.attaque_min_6=368
            self.defense_min_6=304

            self.pv_max_3=3015
            self.attaque_max_3=249
            self.defense_max_3=205
            self.pv_max_4=4095
            self.attaque_max_4=339
            self.defense_max_4=279
            self.pv_max_5=5565
            self.attaque_max_5=460
            self.defense_max_5=379
            self.pv_max_6=7575
            self.attaque_max_6=626
            self.defense_max_6=516

            self.nb_capacites=2

            self.capacite1=Elementaire.griffe
            self.capacite1_nom='Griffe Elementaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Elementaire.explosion
            self.capacite2_nom='Explosion Elementaire'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Elementaire',element[indice_element],3,1,1710,1710,150,99,106)

            self.pv_min_3=1710
            self.attaque_min_3=150
            self.defense_min_3=99
            self.pv_min_4=2460
            self.attaque_min_4=216
            self.defense_min_4=143
            self.pv_min_5=3345
            self.attaque_min_5=295
            self.defense_min_5=195
            self.pv_min_6=4560
            self.attaque_min_6=400
            self.defense_min_6=265

            self.pv_max_3=3075
            self.attaque_max_3=271
            self.defense_max_3=179
            self.pv_max_4=4185
            self.attaque_max_4=368
            self.defense_max_4=244
            self.pv_max_5=5685
            self.attaque_max_5=500
            self.defense_max_5=331
            self.pv_max_6=7740
            self.attaque_max_6=681
            self.defense_max_6=450

            self.nb_capacites=2

            self.capacite1=Elementaire.griffe
            self.capacite1_nom='Griffe Elementaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Elementaire.renforcement
            self.capacite2_nom='Renforcement Elementaire'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

    def griffe(self,cible):
        print('\n',self.surnom,self.attribut,' tranche ',cible.surnom,cible.attribut,' avec ses griffes acérées!!\n')
        degats=self.calcul_dommages(3.5,self.capacite1_bonus_skill,cible)
        type_coup=self.affichage_du_type_de_coup(3.5,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(type_coup=='Critique'):
            cible.degats_continus(1,2)

    def explosion(self,cible):
        print('\n',self.surnom,self.attribut,' désintègre ',cible.surnom,cible.attribut,'dans une explosion élémentaire!!\n')
        degats=(Arrondir.a_l_unite(0.1*self.pv_max_donjons))+self.calcul_dommages(4.1,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(4.1,self.capacite2_bonus_skill,degats-(Arrondir.a_l_unite(0.1*self.pv_max_donjons)),cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)

    def renforcement(self):
        print('\n',self.surnom,self.attribut,' se renforce avec de l énergie naturelle!!\n')
        self.rise(3)
        self.espada(3)


class Garuda(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Garuda',element[indice_element],2,1,960,960,64,88,92)

            self.pv_min_2=960
            self.attaque_min_2=64
            self.defense_min_2=88
            self.pv_min_3=1455
            self.attaque_min_3=97
            self.defense_min_3=133
            self.pv_min_4=2100
            self.attaque_min_4=140
            self.defense_min_4=192
            self.pv_min_5=2850
            self.attaque_min_5=190
            self.defense_min_5=261
            self.pv_min_6=3870
            self.attaque_min_6=258
            self.defense_min_6=355

            self.pv_max_2=1815
            self.attaque_max_2=121
            self.defense_max_2=167
            self.pv_max_3=2625
            self.attaque_max_3=175
            self.defense_max_3=240
            self.pv_max_4=3570
            self.attaque_max_4=238
            self.defense_max_4=327
            self.pv_max_5=4845
            self.attaque_max_5=323
            self.defense_max_5=444
            self.pv_max_6=6585
            self.attaque_max_6=439
            self.defense_max_6=604

            self.nb_capacites=2

            self.capacite1=Garuda.assaut
            self.capacite1_nom='Assaut Aérien'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Garuda.fire_ball
            self.capacite2_nom='Boule de Feu'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Garuda',element[indice_element],2,1,1515,1515,49,65,90)

            self.pv_min_2=1515
            self.attaque_min_2=49
            self.defense_min_2=65
            self.pv_min_3=2295
            self.attaque_min_3=75
            self.defense_min_3=99
            self.pv_min_4=3300
            self.attaque_min_4=108
            self.defense_min_4=143
            self.pv_min_5=4485
            self.attaque_min_5=147
            self.defense_min_5=195
            self.pv_min_6=6105
            self.attaque_min_6=200
            self.defense_min_6=265

            self.pv_max_2=2865
            self.attaque_max_2=94
            self.defense_max_2=124
            self.pv_max_3=4125
            self.attaque_max_3=135
            self.defense_max_3=179
            self.pv_max_4=5610
            self.attaque_max_4=184
            self.defense_max_4=244
            self.pv_max_5=7635
            self.attaque_max_5=250
            self.defense_max_5=331
            self.pv_max_6=10380
            self.attaque_max_6=340
            self.defense_max_6=450

            self.nb_capacites=2

            self.capacite1=Garuda.assaut
            self.capacite1_nom='Assaut Aérien'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Garuda.resurgir
            self.capacite2_nom='Resurgir'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Garuda',element[indice_element],2,1,1050,1050,62,83,90)

            self.pv_min_2=1050
            self.attaque_min_2=62
            self.defense_min_2=83
            self.pv_min_3=1605
            self.attaque_min_3=95
            self.defense_min_3=126
            self.pv_min_4=2310
            self.attaque_min_4=136
            self.defense_min_4=182
            self.pv_min_5=3135
            self.attaque_min_5=185
            self.defense_min_5=247
            self.pv_min_6=4260
            self.attaque_min_6=252
            self.defense_min_6=336

            self.pv_max_2=1995
            self.attaque_max_2=118
            self.defense_max_2=158
            self.pv_max_3=2880
            self.attaque_max_3=170
            self.defense_max_3=227
            self.pv_max_4=3915
            self.attaque_max_4=232
            self.defense_max_4=309
            self.pv_max_5=5325
            self.attaque_max_5=315
            self.defense_max_5=420
            self.pv_max_6=7245
            self.attaque_max_6=428
            self.defense_max_6=571

            self.nb_capacites=2

            self.capacite1=Garuda.assaut
            self.capacite1_nom='Assaut Aérien'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Garuda.thunder_ball
            self.capacite2_nom='Boule de Foudre'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Garuda',element[indice_element],3,1,1920,1920,114,121,94)

            self.pv_min_3=1920
            self.attaque_min_3=114
            self.defense_min_3=121
            self.pv_min_4=2775
            self.attaque_min_4=164
            self.defense_min_4=175
            self.pv_min_5=3780
            self.attaque_min_5=223
            self.defense_min_5=238
            self.pv_min_6=5130
            self.attaque_min_6=304
            self.defense_min_6=323

            self.pv_max_3=3465
            self.attaque_max_3=205
            self.defense_max_3=218
            self.pv_max_4=4725
            self.attaque_max_4=279
            self.defense_max_4=297
            self.pv_max_5=6420
            self.attaque_max_5=379
            self.defense_max_5=404
            self.pv_max_6=8730
            self.attaque_max_6=516
            self.defense_max_6=549

            self.nb_capacites=3

            self.capacite1=Garuda.assaut
            self.capacite1_nom='Assaut Aérien'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Garuda.resurgir
            self.capacite2_nom='Resurgir'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Garuda.lumiere
            self.capacite3_nom='Lumière de Résurrection'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=7
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Garuda',element[indice_element],2,1,1095,1095,65,77,92)

            self.pv_min_2=1095
            self.attaque_min_2=65
            self.defense_min_2=77
            self.pv_min_3=1680
            self.attaque_min_3=99
            self.defense_min_3=116
            self.pv_min_4=2415
            self.attaque_min_4=143
            self.defense_min_4=168
            self.pv_min_5=3285
            self.attaque_min_5=195
            self.defense_min_5=228
            self.pv_min_6=4455
            self.attaque_min_6=265
            self.defense_min_6=310

            self.pv_max_2=2085
            self.attaque_max_2=124
            self.defense_max_2=145
            self.pv_max_3=3015
            self.attaque_max_3=179
            self.defense_max_3=209
            self.pv_max_4=4095
            self.attaque_max_4=244
            self.defense_max_4=285
            self.pv_max_5=5565
            self.attaque_max_5=331
            self.defense_max_5=387
            self.pv_max_6=7575
            self.attaque_max_6=450
            self.defense_max_6=527

            self.nb_capacites=2

            self.capacite1=Garuda.assaut
            self.capacite1_nom='Assaut Aérien'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Garuda.shadow_ball
            self.capacite2_nom='Balle Ombre'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

    def assaut(self,cible):
        print('\n',self.surnom,self.attribut,' plonge en piquée sur ',cible.surnom,cible.attribut,'!!\n')
        degats=(-15)+self.calcul_dommages(3.7,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.7,self.capacite1_bonus_skill,degats+15,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.24,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1

    def fire_ball(self,cible):
        print('\n',self.surnom,self.attribut,' projette une boule de feu sur ',cible.surnom,cible.attribut,'!!\n')
        degats=50+self.calcul_dommages(4.8,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(4.8,self.capacite2_bonus_skill,degats-50,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.degats_continus(1,3)

    def thunder_ball(self,cible):
        print('\n',self.surnom,self.attribut,' projette une boule de foudre sur ',cible.surnom,cible.attribut,'!!\n')
        degats=50+self.calcul_dommages(4.8,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(4.8,self.capacite2_bonus_skill,degats-50,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1

    def shadow_ball(self,cible):
        print('\n',self.surnom,self.attribut,' projette une boule de feu sur ',cible.surnom,cible.attribut,'!!\n')
        degats=50+self.calcul_dommages(4.8,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(4.8,self.capacite2_bonus_skill,degats-50,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.degats_continus(1,3)

    def resurgir(allie):
        print('\n',allie.surnom,allie.attribut,'reçoit un tour supplémentaire!!')
        allie.rise(1)
        allie.espada(1)
        allie.jauge_attaque+=100

    def lumiere(equipe_alliee):
        print('\nGaruda Lumière enveloppe toute l\'équipe dans une lumière de résurrection!! \n')
        possibilites_resurrection=[]
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels<=0):
                if(equipe_alliee.membres[index].sans_resurrection<=0):
                    possibilites_resurrection.append(index)
                    print('L\'allié ',index,' : ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' peut revenir à la vie!!')
                else:
                    print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' a été maudit et ne peut donc pas revenir à la vie...\n')
            else:
                if (equipe_alliee.membres[index].perturbation_recup<=0):
                    equipe_alliee.membres[index].etre_soigne(0.2*equipe_alliee.membres[index].pv_max_donjons)
                else:
                    print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces!!\n')
        if(len(possibilites_resurrection)!=0):
            ''' OUI, QUAND UN ENNEMI UTILISE CETTE CAPACITE, ON PEUT CHOISIR POUR LUI, NORMAL!! '''
            entree=input('Qui voulez-vous ramener à la vie ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Qui voulez-vous ramener à la vie ? ')
            choix_resurrection=int(entree)
            while(choix_resurrection not in possibilites_resurrection):
                entree=input('Qui voulez-vous ramener à la vie ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('Qui voulez-vous ramener à la vie ? ')
                choix_resurrection=int(entree)
            print(equipe_alliee.membres[choix_resurrection].surnom,equipe_alliee.membres[choix_resurrection].attribut,' revient à la vie!! \n')
            equipe_alliee.membres[choix_resurrection].pv_actuels=Arrondir.a_l_unite(0.2*equipe_alliee.membres[index].pv_max_donjons)
            equipe_alliee.membres[choix_resurrection].soigner_de_tous_les_maux()
            equipe_alliee.membres[choix_resurrection].etat='vivant'


class Harpie(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Harpie',element[indice_element],2,1,1320,1320,64,64,105)

            self.pv_min_2=1320
            self.attaque_min_2=64
            self.defense_min_2=64
            self.pv_min_3=1995
            self.attaque_min_3=97
            self.defense_min_3=97
            self.pv_min_4=2880
            self.attaque_min_4=140
            self.defense_min_4=140
            self.pv_min_5=3915
            self.attaque_min_5=190
            self.defense_min_5=190
            self.pv_min_6=5325
            self.attaque_min_6=258
            self.defense_min_6=258

            self.pv_max_2=2505
            self.attaque_max_2=121
            self.defense_max_2=121
            self.pv_max_3=3600
            self.attaque_max_3=175
            self.defense_max_3=175
            self.pv_max_4=4905
            self.attaque_max_4=238
            self.defense_max_4=238
            self.pv_max_5=6660
            self.attaque_max_5=323
            self.defense_max_5=323
            self.pv_max_6=9060
            self.attaque_max_6=439
            self.defense_max_6=439

            self.nb_capacites=2

            self.capacite1=Harpie.kick
            self.capacite1_nom='Double Kick'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Harpie.plumes
            self.capacite2_nom='Plumes Tranchantes'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Harpie',element[indice_element],2,1,960,960,77,75,105)

            self.pv_min_2=960
            self.attaque_min_2=77
            self.defense_min_2=75
            self.pv_min_3=1455
            self.attaque_min_3=116
            self.defense_min_3=114
            self.pv_min_4=2100
            self.attaque_min_4=168
            self.defense_min_4=164
            self.pv_min_5=2850
            self.attaque_min_5=228
            self.defense_min_5=223
            self.pv_min_6=3870
            self.attaque_min_6=310
            self.defense_min_6=304

            self.pv_max_2=1815
            self.attaque_max_2=145
            self.defense_max_2=142
            self.pv_max_3=2625
            self.attaque_max_3=209
            self.defense_max_3=205
            self.pv_max_4=3570
            self.attaque_max_4=285
            self.defense_max_4=279
            self.pv_max_5=4845
            self.attaque_max_5=387
            self.defense_max_5=379
            self.pv_max_6=6585
            self.attaque_max_6=527
            self.defense_max_6=516

            self.nb_capacites=2

            self.capacite1=Harpie.kick
            self.capacite1_nom='Double Kick'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Harpie.plumes
            self.capacite2_nom='Plumes Tranchantes'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Harpie',element[indice_element],2,1,1035,1035,81,65,107)

            self.pv_min_2=1035
            self.attaque_min_2=81
            self.defense_min_2=65
            self.pv_min_3=1560
            self.attaque_min_3=124
            self.defense_min_3=99
            self.pv_min_4=2250
            self.attaque_min_4=178
            self.defense_min_4=143
            self.pv_min_5=3060
            self.attaque_min_5=242
            self.defense_min_5=195
            self.pv_min_6=4170
            self.attaque_min_6=329
            self.defense_min_6=265

            self.pv_max_2=1950
            self.attaque_max_2=155
            self.defense_max_2=124
            self.pv_max_3=2820
            self.attaque_max_3=223
            self.defense_max_3=179
            self.pv_max_4=3825
            self.attaque_max_4=303
            self.defense_max_4=244
            self.pv_max_5=5205
            self.attaque_max_5=412
            self.defense_max_5=331
            self.pv_max_6=7080
            self.attaque_max_6=560
            self.defense_max_6=450

            self.nb_capacites=2

            self.capacite1=Harpie.kick
            self.capacite1_nom='Double Kick'
            self.capacite1BonusSkill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Harpie.hurlement
            self.capacite2_nom='Hurlement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Harpie',element[indice_element],3,1,1890,1890,126,112,104)

            self.pv_min_3=1890
            self.attaque_min_3=126
            self.defense_min_3=112
            self.pv_min_4=2730
            self.attaque_min_4=182
            self.defense_min_4=161
            self.pv_min_5=3705
            self.attaque_min_5=247
            self.defense_min_5=219
            self.pv_min_6=5040
            self.attaque_min_6=336
            self.defense_min_6=297

            self.pv_max_3=3405
            self.attaque_max_3=227
            self.defense_max_3=201
            self.pv_max_4=4635
            self.attaque_max_4=309
            self.defense_max_4=273
            self.pv_max_5=6300
            self.attaque_max_5=420
            self.defense_max_5=371
            self.pv_max_6=8565
            self.attaque_max_6=571
            self.defense_max_6=505

            self.nb_capacites=2

            self.capacite1=Harpie.kick
            self.capacite1_nom='Double Kick'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Harpie.hurlement
            self.capacite2_nom='Hurlement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Harpie',element[indice_element],3,1,1860,1860,126,114,103)

            self.pv_min_3=1860
            self.attaque_min_3=126
            self.defense_min_3=114
            self.pv_min_4=2670
            self.attaque_min_4=182
            self.defense_min_4=164
            self.pv_min_5=3630
            self.attaque_min_5=247
            self.defense_min_5=223
            self.pv_min_6=4935
            self.attaque_min_6=336
            self.defense_min_6=304

            self.pv_max_3=3345
            self.attaque_max_3=227
            self.defense_max_3=205
            self.pv_max_4=4545
            self.attaque_max_4=309
            self.defense_max_4=279
            self.pv_max_5=6180
            self.attaque_max_5=420
            self.defense_max_5=379
            self.pv_max_6=8400
            self.attaque_max_6=571
            self.defense_max_6=516

            self.nb_capacites=3

            self.capacite1=Harpie.kick
            self.capacite1_nom='Double Kick'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Harpie.plumes
            self.capacite2_nom='Plumes Tranchantes'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Harpie.danse_celeste
            self.capacite3_nom='Danse Céleste'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=4
            self.attente3=0
            self.etat_cap3='dispo'

    def kick(self,cible):
        print('\n',self.surnom,self.attribut,' frappe deux fois ',cible.surnom,cible.attribut,'!!\n')
        for index in range(2):
            degats=self.calcul_dommages(1.9,self.capacite1_bonus_skill,cible)
            self.affichage_du_type_de_coup(1.9,self.capacite1_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    cible.atk_break(2)

    def hurlement(self,cible):
        print('\n',self.surnom,self.attribut,'pousse un hurlement strident!!\n')
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle+0.5)
            if(effet_nefaste<=100*limite_reussite):
                cible.stun=1
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.degats_continus(1,3)
            else:
                print(cible.surnom,cible.attribut,' résiste au hurlement!! \n')
        else:
            print(cible.surnom,cible.attribut,' est immunisé(e) contre les effets néfastes!!\n')

    def plumes(self,cible):
        print('\n',self.surnom,self.attribut,' projette une nuée de plumes tranchantes sur ',cible.surnom,cible.attribut,'!!\n')
        for index in range(3):
            degats=self.calcul_dommages(1.9,self.capacite2_bonus_skill,cible)
            self.affichage_du_type_de_coup(1.9,self.capacite2_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.perturbation_recuperation(2)

    def danse_celeste(self,cible):
        print('\n',self.surnom,self.attribut,' entame une dance céleste et lacère plusieurs fois ',cible.surnom,cible.attribut,'!!\n')
        for index in range(4):
            degats=self.calcul_dommages(2,self.capacite3_bonus_skill,cible)
            self.affichage_du_type_de_coup(2,self.capacite3_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.3,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    cible.def_break(2)


class Salamandre(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Salamandre',element[indice_element],3,1,1680,1680,119,133,98)

            self.pv_min_3=1680
            self.attaque_min_3=119
            self.defense_min_3=133
            self.pv_min_4=2415
            self.attaque_min_4=171
            self.defense_min_4=192
            self.pv_min_5=3285
            self.attaque_min_5=233
            self.defense_min_5=261
            self.pv_min_6=4455
            self.attaque_min_6=316
            self.defense_min_6=355

            self.pv_max_3=3015
            self.attaque_max_3=214
            self.defense_max_3=240
            self.pv_max_4=4095
            self.attaque_max_4=291
            self.defense_max_4=327
            self.pv_max_5=5565
            self.attaque_max_5=396
            self.defense_max_5=444
            self.pv_max_6=7575
            self.attaque_max_6=538
            self.defense_max_6=604

            self.nb_capacites=3

            self.capacite1=Salamandre.tourbillon
            self.capacite1_nom='Tourbillon'
            self.capacite1BonusSkill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Salamandre.ecrasement
            self.capacite2_nom='Ecrasement'
            self.capacite2BonusSkill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Salamandre.tremblement
            self.capacite3_nom='Tremblement de Terre'
            self.capacite3BonusSkill=0
            self.temps_recharge3=6
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Salamandre',element[indice_element],2,1,960,960,65,86,98)

            self.pv_min_2=960
            self.attaque_min_2=65
            self.defense_min_2=86
            self.pv_min_3=1455
            self.attaque_min_3=99
            self.defense_min_3=131
            self.pv_min_4=2100
            self.attaque_min_4=143
            self.defense_min_4=189
            self.pv_min_5=2850
            self.attaque_min_5=195
            self.defense_min_5=257
            self.pv_min_6=3870
            self.attaque_min_6=265
            self.defense_min_6=349

            self.pv_max_2=1815
            self.attaque_max_2=124
            self.defense_max_2=164
            self.pv_max_3=2625
            self.attaque_max_3=179
            self.defense_max_3=236
            self.pv_max_4=3570
            self.attaque_max_4=244
            self.defense_max_4=321
            self.pv_max_5=4845
            self.attaque_max_5=331
            self.defense_max_5=436
            self.pv_max_6=6585
            self.attaque_max_6=450
            self.defense_max_6=593

            self.nb_capacites=2

            self.capacite1=Salamandre.tourbillon
            self.capacite1_nom='Tourbillon'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Salamandre.ecrasement
            self.capacite2_nom='Ecrasement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Salamandre',element[indice_element],2,1,975,975,77,73,98)

            self.pv_min_2=975
            self.attaque_min_2=77
            self.defense_min_2=73
            self.pv_min_3=1485
            self.attaque_min_3=116
            self.defense_min_3=112
            self.pv_min_4=2145
            self.attaque_min_4=168
            self.defense_min_4=161
            self.pv_min_5=2925
            self.attaque_min_5=228
            self.defense_min_5=219
            self.pv_min_6=3975
            self.attaque_min_6=310
            self.defense_min_6=297

            self.pv_max_2=1860
            self.attaque_max_2=145
            self.defense_max_2=139
            self.pv_max_3=2685
            self.attaque_max_3=209
            self.defense_max_3=201
            self.pv_max_4=3660
            self.attaque_max_4=285
            self.defense_max_4=273
            self.pv_max_5=4965
            self.attaque_max_5=387
            self.defense_max_5=371
            self.pv_max_6=6750
            self.attaque_max_6=527
            self.defense_max_6=505

            self.nb_capacites=2

            self.capacite1=Salamandre.tourbillon
            self.capacite1_nom='Tourbillon'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Salamandre.tempete
            self.capacite2_nom='Tempête de Sable'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Salamandre',element[indice_element],2,1,1080,1080,67,77,98)

            self.pv_min_2=1080
            self.attaque_min_2=67
            self.defense_min_2=77
            self.pv_min_3=1635
            self.attaque_min_3=102
            self.defense_min_3=116
            self.pv_min_4=2355
            self.attaque_min_4=147
            self.defense_min_4=168
            self.pv_min_5=3210
            self.attaque_min_5=200
            self.defense_min_5=228
            self.pv_min_6=4365
            self.attaque_min_6=271
            self.defense_min_6=310

            self.pv_max_2=2040
            self.attaque_max_2=127
            self.defense_max_2=145
            self.pv_max_3=2940
            self.attaque_max_3=183
            self.defense_max_3=209
            self.pv_max_4=4005
            self.attaque_max_4=250
            self.defense_max_4=285
            self.pv_max_5=5445
            self.attaque_max_5=339
            self.defense_max_5=387
            self.pv_max_6=7410
            self.attaque_max_6=461
            self.defense_max_6=527

            self.nb_capacites=2

            self.capacite1=Salamandre.tourbillon
            self.capacite1_nom='Tourbillon'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Salamandre.ecrasement
            self.capacite2_nom='Ecrasement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Salamandre',element[indice_element],2,1,1035,1035,65,81,98)

            self.pv_min_2=1035
            self.attaque_min_2=65
            self.defense_min_2=81
            self.pv_min_3=1560
            self.attaque_min_3=99
            self.defense_min_3=124
            self.pv_min_4=2250
            self.attaque_min_4=143
            self.defense_min_4=178
            self.pv_min_5=3060
            self.attaque_min_5=195
            self.defense_min_5=242
            self.pv_min_6=4170
            self.attaque_min_6=265
            self.defense_min_6=329

            self.pv_max_2=1950
            self.attaque_max_2=124
            self.defense_max_2=155
            self.pv_max_3=2820
            self.attaque_max_3=179
            self.defense_max_3=223
            self.pv_max_4=3825
            self.attaque_max_4=244
            self.defense_max_4=303
            self.pv_max_5=5205
            self.attaque_max_5=331
            self.defense_max_5=412
            self.pv_max_6=7080
            self.attaque_max_6=450
            self.defense_max_6=560

            self.nb_capacites=2

            self.capacite1=Salamandre.tourbillon
            self.capacite1_nom='Tourbillon'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Salamandre.tempete
            self.capacite2_nom='Tempête de Sable'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

    def tourbillon(self,cible):
        print('\n',self.surnom,self.attribut,' engloutit ',cible.surnom,cible.attribut,'dans un tourbillon magique!!\n')
        degats=15+self.calcul_dommages(3.5,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.5,self.capacite1_bonus_skill,degats-15,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.atk_break(2)

    def ecrasement(self,cible):
        print('\n',self.surnom,self.attribut,' écrase violemment ',cible.surnom,cible.attribut,'!!\n')
        degats=(Arrondir.a_l_unite(3*self.defense_actuelle))+self.calcul_dommages(2.4,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(2.4,self.capacite2_bonus_skill,degats-(Arrondir.a_l_unite(3*self.defense_actuelle)),cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.slow_down(2)

    def tempete(self,cible):
        print('\n',self.surnom,self.attribut,' engloutit ',cible.surnom,cible.attribut,'dans une violente tempête!!\n')
        degats=(Arrondir.a_l_unite(2.8*self.defense_actuelle))+self.calcul_dommages(2.5,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(2.5,self.capacite2_bonus_skill,degats-(Arrondir.a_l_unite(2.8*self.defense_actuelle)),cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.degats_continus(1,3)

    def tremblement(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' secoue toute l équipe ennemie avec un puissant séisme!!\n')
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels>0):
                print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,'reçoit le tremblement de terre!!')
                degats=(Arrondir.a_l_unite(2.1*self.defense_actuelle))+self.calcul_dommages(2,self.capacite3_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(2,self.capacite3_bonus_skill,degats-(Arrondir.a_l_unite(2.1*self.defense_actuelle)),equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(1,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' voit sa jauge d\'attaque diminuer de moitié!! \n')
                        equipe_ennemie.membres[index].jauge_attaque-=max(50,Arrondir.a_l_unite(0.5*equipe_ennemie.membres[index].jauge_attaque))


class Esprit(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Esprit',element[indice_element],2,1,960,960,65,86,98)

            self.pv_min_2=960
            self.attaque_min_2=65
            self.defense_min_2=86
            self.pv_min_3=1455
            self.attaque_min_3=99
            self.defense_min_3=131
            self.pv_min_4=2100
            self.attaque_min_4=143
            self.defense_min_4=189
            self.pv_min_5=2850
            self.attaque_min_5=195
            self.defense_min_5=257
            self.pv_min_6=3870
            self.attaque_min_6=265
            self.defense_min_6=349

            self.pv_max_2=1815
            self.attaque_max_2=124
            self.defense_max_2=164
            self.pv_max_3=2625
            self.attaque_max_3=179
            self.defense_max_3=236
            self.pv_max_4=3570
            self.attaque_max_4=244
            self.defense_max_4=321
            self.pv_max_5=4845
            self.attaque_max_5=331
            self.defense_max_5=436
            self.pv_max_6=6585
            self.attaque_max_6=450
            self.defense_max_6=593

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Esprit',element[indice_element],2,1,840,840,75,85,98)

            self.pv_min_2=840
            self.attaque_min_2=75
            self.defense_min_2=85
            self.pv_min_3=1275
            self.attaque_min_3=114
            self.defense_min_3=128
            self.pv_min_4=1830
            self.attaque_min_4=164
            self.defense_min_4=185
            self.pv_min_5=2490
            self.attaque_min_5=223
            self.defense_min_5=252
            self.pv_min_6=3390
            self.attaque_min_6=304
            self.defense_min_6=342

            self.pv_max_2=1590
            self.attaque_max_2=142
            self.defense_max_2=161
            self.pv_max_3=2295
            self.attaque_max_3=205
            self.defense_max_3=231
            self.pv_max_4=3120
            self.attaque_max_4=279
            self.defense_max_4=315
            self.pv_max_5=4245
            self.attaque_max_5=379
            self.defense_max_5=428
            self.pv_max_6=5760
            self.attaque_max_6=516
            self.defense_max_6=582

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Esprit',element[indice_element],2,1,1050,1050,65,80,98)

            self.pv_min_2=1050
            self.attaque_min_2=65
            self.defense_min_2=80
            self.pv_min_3=1605
            self.attaque_min_3=99
            self.defense_min_3=121
            self.pv_min_4=2310
            self.attaque_min_4=143
            self.defense_min_4=175
            self.pv_min_5=3135
            self.attaque_min_5=195
            self.defense_min_5=238
            self.pv_min_6=4260
            self.attaque_min_6=265
            self.defense_min_6=323

            self.pv_max_2=1995
            self.attaque_max_2=124
            self.defense_max_2=152
            self.pv_max_3=2880
            self.attaque_max_3=179
            self.defense_max_3=218
            self.pv_max_4=3915
            self.attaque_max_4=244
            self.defense_max_4=297
            self.pv_max_5=5325
            self.attaque_max_5=331
            self.defense_max_5=404
            self.pv_max_6=7245
            self.attaque_max_6=450
            self.defense_max_6=549

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Esprit',element[indice_element],2,1,975,975,69,81,98)

            self.pv_min_2=975
            self.attaque_min_2=69
            self.defense_min_2=81
            self.pv_min_3=1485
            self.attaque_min_3=104
            self.defense_min_3=124
            self.pv_min_4=2145
            self.attaque_min_4=150
            self.defense_min_4=178
            self.pv_min_5=2925
            self.attaque_min_5=204
            self.defense_min_5=242
            self.pv_min_6=3975
            self.attaque_min_6=278
            self.defense_min_6=329

            self.pv_max_2=1860
            self.attaque_max_2=130
            self.defense_max_2=155
            self.pv_max_3=2685
            self.attaque_max_3=188
            self.defense_max_3=223
            self.pv_max_4=3660
            self.attaque_max_4=255
            self.defense_max_4=303
            self.pv_max_5=4965
            self.attaque_max_5=347
            self.defense_max_5=412
            self.pv_max_6=6750
            self.attaque_max_6=472
            self.defense_max_6=560

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Esprit',element[indice_element],2,1,885,885,72,85,98)

            self.pv_min_2=885
            self.attaque_min_2=72
            self.defense_min_2=85
            self.pv_min_3=1350
            self.attaque_min_3=109
            self.defense_min_3=128
            self.pv_min_4=1935
            self.attaque_min_4=157
            self.defense_min_4=185
            self.pv_min_5=2640
            self.attaque_min_5=214
            self.defense_min_5=252
            self.pv_min_6=3585
            self.attaque_min_6=291
            self.defense_min_6=342

            self.pv_max_2=1680
            self.attaque_max_2=136
            self.defense_max_2=161
            self.pv_max_3=2415
            self.attaque_max_3=196
            self.defense_max_3=231
            self.pv_max_4=3300
            self.attaque_max_4=267
            self.defense_max_4=315
            self.pv_max_5=4485
            self.attaque_max_5=363
            self.defense_max_5=428
            self.pv_max_6=6090
            self.attaque_max_6=494
            self.defense_max_6=582

            '''
            Vérifier qu'ils ont tous la même deuxième capacité
            Capacité 2 légèrement différente selon attribut mais effet très similaire... IsOkay
            '''

        self.nb_capacites=2

        self.capacite1=Esprit.sphere_spirituelle
        self.capacite1_nom='Sphère Spirituelle'
        self.capacite1_bonus_skill=0
        self.temps_recharge1=1
        self.attente1=0
        self.etat_cap1='dispo'

        self.capacite2=Esprit.guerison
        self.capacite2_nom='Guérison'
        self.capacite2_bonus_skill=0
        self.temps_recharge2=3
        self.attente2=0
        self.etat_cap2='dispo'

    def sphere_spirituelle(self,equipe_alliee,cible):
        print('\n',self.surnom,self.attribut,' projette une sphère spirituelle sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.5,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.5,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        nb_allies=equipe_alliee.len
        if(nb_allies>0):
            pv_min=equipe_alliee.membres[0].pv_actuels
            indice_allie_a_soigner=0
            index=0
            while(index <= nb_allies-1):
                if(equipe_alliee.membres[index].pv_actuels<pv_min):
                    pv_min=equipe_alliee.membres[index].pv_actuels
                    indice_allie_a_soigner=index
                index+=1
            montant=Arrondir.a_l_unite(0.15*equipe_alliee.membres[indice_allie_a_soigner].pv_max_donjons)
            equipe_alliee.membres[indice_allie_a_soigner].etre_soigne(montant)
        ''' Verifier que la jauge d'attaque ne réaugmente pas immédiatement ex. de 15 '''
        ''' Askip non '''

    def guerison(self,allie):
        print('\n',self.surnom,self.attribut,' soigne ',allie.surnom,allie.attribut,'et lui-même!!\n')
        if (allie.pv_actuels>0):
            allie.soigner_de_tous_les_maux()
            print(allie.surnom,allie.attribut,'est débarrassé de tous les effets négatifs qui l affectaient!!')
            montant=allie.pv_max_donjons*(0.2+self.capacite2_bonus_skill)
            allie.etre_soigne(montant)
        elif (allie.pv_actuels<=0):
            print(allie.surnom,allie.attribut,' est mort!! \n')
        print('Il reste ',allie.pv_actuels,' point(s) de vie sur',allie.pv_max_donjons,' à ',allie.surnom,allie.attribut,'!! \n')
        self.soigner_de_tous_les_maux()
        print(self.surnom,self.attribut,'est débarrassé de tous les effets négatifs qui l affectaient!!')
        montant=self.pv_max_donjons*(0.2+self.capacite2BonusSkill)
        self.etre_soigne(montant)
        print('Il reste ',self.pv_actuels,' point(s) de vie sur',self.pv_max_donjons,' à ',self.surnom,self.attribut,'!! \n')


class Viking(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Viking',element[indice_element],3,1,1635,1635,112,143,96)

            self.pv_min_3=1635
            self.attaque_min_3=112
            self.defense_min_3=143
            self.pv_min_4=2355
            self.attaque_min_4=162
            self.defense_min_4=206
            self.pv_min_5=3210
            self.attaque_min_5=219
            self.defense_min_5=280
            self.pv_min_6=4365
            self.attaque_min_6=297
            self.defense_min_6=381

            self.pv_max_3=2940
            self.attaque_max_3=201
            self.defense_max_3=258
            self.pv_max_4=4005
            self.attaque_max_4=273
            self.defense_max_4=351
            self.pv_max_5=5445
            self.attaque_max_5=371
            self.defense_max_5=476
            self.pv_max_6=7410
            self.attaque_max_6=505
            self.defense_max_6=648

            self.nb_capacites=2

            self.capacite1=Viking.hache
            self.capacite1_nom='Lancer de Hache'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Viking.meurtre
            self.capacite2_nom='Folie Meurtrière'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Viking.encouragement
            self.anti_leader_skill=Viking.anti_encouragement

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Viking',element[indice_element],2,1,855,855,75,83,96)

            self.pv_min_2=855
            self.attaque_min_2=75
            self.defense_min_2=83
            self.pv_min_3=1305
            self.attaque_min_3=114
            self.defense_min_3=126
            self.pv_min_4=1890
            self.attaque_min_4=164
            self.defense_min_4=182
            self.pv_min_5=2565
            self.attaque_min_5=223
            self.defense_min_5=247
            self.pv_min_6=3480
            self.attaque_min_6=304
            self.defense_min_6=336

            self.pv_max_2=1635
            self.attaque_max_2=142
            self.defense_max_2=158
            self.pv_max_3=2355
            self.attaque_max_3=205
            self.defense_max_3=227
            self.pv_max_4=3210
            self.attaque_max_4=279
            self.defense_max_4=309
            self.pv_max_5=4365
            self.attaque_max_5=379
            self.defense_max_5=420
            self.pv_max_6=5925
            self.attaque_max_6=516
            self.defense_max_6=571

            self.nb_capacites=2

            self.capacite1=Viking.hache
            self.capacite1_nom='Lancer de Hache'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Viking.multiple_hache
            self.capacite2_nom='Multiples Lancers de Haches'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Viking',element[indice_element],2,1,1050,1050,65,80,96)

            self.pv_min_2=1050
            self.attaque_min_2=65
            self.defense_min_2=80
            self.pv_min_3=1605
            self.attaque_min_3=99
            self.defense_min_3=121
            self.pv_min_4=2310
            self.attaque_min_4=143
            self.defense_min_4=175
            self.pv_min_5=3135
            self.attaque_min_5=195
            self.defense_min_5=238
            self.pv_min_6=4260
            self.attaque_min_6=265
            self.defense_min_6=323

            self.pv_max_2=1995
            self.attaque_max_2=124
            self.defense_max_2=152
            self.pv_max_3=2880
            self.attaque_max_3=179
            self.defense_max_3=218
            self.pv_max_4=3915
            self.attaque_max_4=244
            self.defense_max_4=297
            self.pv_max_5=5325
            self.attaque_max_5=331
            self.defense_max_5=404
            self.pv_max_6=7245
            self.attaque_max_6=450
            self.defense_max_6=549

            self.nb_capacites=2

            self.capacite1=Viking.hache
            self.capacite1_nom='Lancer de Hache'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Viking.meurtre
            self.capacite2_nom='Folie Meurtrière'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Viking',element[indice_element],2,1,975,975,69,81,96)

            self.pv_min_2=975
            self.attaque_min_2=69
            self.defense_min_2=81
            self.pv_min_3=1485
            self.attaque_min_3=104
            self.defense_min_3=124
            self.pv_min_4=2145
            self.attaque_min_4=150
            self.defense_min_4=178
            self.pv_min_5=2925
            self.attaque_min_5=204
            self.defense_min_5=242
            self.pv_min_6=3975
            self.attaque_min_6=278
            self.defense_min_6=329

            self.pv_max_2=1860
            self.attaque_max_2=130
            self.defense_max_2=155
            self.pv_max_3=2685
            self.attaque_max_3=188
            self.defense_max_3=223
            self.pv_max_4=3660
            self.attaque_max_4=255
            self.defense_max_4=303
            self.pv_max_5=4965
            self.attaque_max_5=347
            self.defense_max_5=412
            self.pv_max_6=6750
            self.attaque_max_6=472
            self.defense_max_6=560

            self.nb_capacites=2

            self.capacite1=Viking.hache
            self.capacite1_nom='Lancer de Hache'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Viking.multiple_hache
            self.capacite2_nom='Multiples Lancers de Haches'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        ''' Manque 1 quelque part   Total = 363 pas 364     Copier SummonersWorld pour Feu et Ténèbres '''
        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Viking',element[indice_element],3,1,1815,1815,114,128,96)

            self.pv_min_3=1815
            self.attaque_min_3=115
            self.defense_min_3=128
            self.pv_min_4=2625
            self.attaque_min_4=165
            self.defense_min_4=185
            self.pv_min_5=3570
            self.attaque_min_5=223
            self.defense_min_5=252
            self.pv_min_6=4845
            self.attaque_min_6=304
            self.defense_min_6=342

            self.pv_max_3=3270
            self.attaque_max_3=206
            self.defense_max_3=231
            self.pv_max_4=4455
            self.attaque_max_4=279
            self.defense_max_4=315
            self.pv_max_5=6060
            self.attaque_max_5=379
            self.defense_max_5=428
            self.pv_max_6=8235
            self.attaque_max_6=516
            self.defense_max_6=582

            self.nb_capacites=2

            self.capacite1=Viking.hache
            self.capacite1_nom='Lancer de Hache'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Viking.meurtre
            self.capacite2_nom='Folie Meurtrière'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

    def hache(self,cible):
        print('\n',self.surnom,self.attribut,' lance une hache sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.7,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.7,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.3,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.degats_continus(1,3)

    def meurtre(self,cible):
        print('\n',self.surnom,self.attribut,' entre dans une folie meurtrière et pourfend ',cible.surnom,cible.attribut,' de sa hache!!\n')
        rage=4+3.5*(1-(self.pv_actuels/self.pv_max_donjons))
        degats=self.calcul_dommages(rage,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(rage,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.def_break(2)

    def multiple_hache(self,cible):
        print('\n',self.surnom,self.attribut,' lance trois haches sur ',cible.surnom,cible.attribut,'!!\n')
        for index in range(3):
            degats=self.calcul_dommages(2.1,self.capacite2_bonus_skill,cible)
            type_coup=self.affichage_du_type_de_coup(2.1,self.capacite2_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(type_coup=='Critique'):
                print(self.surnom,self.attribut,' voit sa jauge d\'attaque augmenter de 15%!!\n')
                self.jauge_attaque+=max(15,Arrondir.a_l_unite(0.15*self.jauge_attaque))
                
    def encouragement(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].attaque_actuelle+=Arrondir.a_l_unite(0.15*equipe_alliee.membres[index].attaque_max_donjons)
            equipe_alliee.membres[index].attaque_max_donjons+=Arrondir.a_l_unite(0.15*equipe_alliee.membres[index].attaque_max_donjons)
            print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 15%!!')
            print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].attaque_actuelle,'\n')

    def anti_encouragement(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].attaque_actuelle-=Arrondir.a_l_unite(0.15*equipe_alliee.membres[index].attaque_max_donjons)


class Chevalier(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Chevalier',element[indice_element],3,1,1965,1965,116,116,97)

            self.pv_min_3=1965
            self.attaque_min_3=116
            self.defense_min_3=116
            self.pv_min_4=2835
            self.attaque_min_4=168
            self.defense_min_4=168
            self.pv_min_5=3855
            self.attaque_min_5=228
            self.defense_min_5=228
            self.pv_min_6=5235
            self.attaque_min_6=310
            self.defense_min_6=310

            self.pv_max_3=3540
            self.attaque_max_3=209
            self.defense_max_3=209
            self.pv_max_4=4815
            self.attaque_max_4=285
            self.defense_max_4=285
            self.pv_max_5=6540
            self.attaque_max_5=387
            self.defense_max_5=387
            self.pv_max_6=8895
            self.attaque_max_6=527
            self.defense_max_6=527

            self.nb_capacites=3

            self.capacite1=Chevalier.clivage_terrestre
            self.capacite1_nom='Clivage Terrestre'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Chevalier.clivage_marin
            self.capacite2_nom='Clivage Marin'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Chevalier.abnegation
            self.capacite3_nom='Abnégation'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Chevalier',element[indice_element],2,1,1200,1200,64,72,97)

            self.pv_min_2=1200
            self.attaque_min_2=64
            self.defense_min_2=72
            self.pv_min_3=1815
            self.attaque_min_3=97
            self.defense_min_3=109
            self.pv_min_4=2625
            self.attaque_min_4=140
            self.defense_min_4=157
            self.pv_min_5=3570
            self.attaque_min_5=190
            self.defense_min_5=214
            self.pv_min_6=4845
            self.attaque_min_6=258
            self.defense_min_6=291

            self.pv_max_2=2280
            self.attaque_max_2=121
            self.defense_max_2=136
            self.pv_max_3=3270
            self.attaque_max_3=175
            self.defense_max_3=196
            self.pv_max_4=4455
            self.attaque_max_4=238
            self.defense_max_4=267
            self.pv_max_5=6060
            self.attaque_max_5=323
            self.defense_max_5=363
            self.pv_max_6=8235
            self.attaque_max_6=439
            self.defense_max_6=494

            self.nb_capacites=2

            self.capacite1=Chevalier.clivage_terrestre
            self.capacite1_nom='Clivage Terrestre'
            self.capacite1_bonus_skill=0
            self.temsp_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Chevalier.provocation
            self.capacite2_nom='Provocation'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Chevalier',element[indice_element],2,1,1275,1275,65,65,97)

            self.pv_min_2=1275
            self.attaque_min_2=65
            self.defense_min_2=65
            self.pv_min_3=1920
            self.attaque_min_3=99
            self.defense_min_3=99
            self.pv_min_4=2775
            self.attaque_min_4=143
            self.defense_min_4=143
            self.pv_min_5=3780
            self.attaque_min_5=195
            self.defense_min_5=195
            self.pv_min_6=5130
            self.attaque_min_6=265
            self.defense_min_6=265

            self.pv_max_2=2415
            self.attaque_max_2=124
            self.defense_max_2=124
            self.pv_max_3=3465
            self.attaque_max_3=179
            self.defense_max_3=179
            self.pv_max_4=4725
            self.attaque_max_4=244
            self.defense_max_4=244
            self.pv_max_5=6420
            self.attaque_max_5=331
            self.defense_max_5=331
            self.pv_max_6=8730
            self.attaque_max_6=450
            self.defense_max_6=450

            self.nb_capacites=2

            self.capacite1=Chevalier.clivage_terrestre
            self.capacite1_nom='Clivage Terrestre'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Chevalier.clivage_marin
            self.capacite2_nom='Clivage Marin'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Chevalier',element[indice_element],3,1,1890,1890,126,112,97)

            self.pv_min_3=1890
            self.attaque_min_3=126
            self.defense_min_3=112
            self.pv_min_4=2730
            self.attaque_min_4=182
            self.defense_min_4=161
            self.pv_min_5=3705
            self.attaque_min_5=247
            self.defense_min_5=219
            self.pv_min_6=5040
            self.attaque_min_6=336
            self.defense_min_6=297

            self.pv_max_3=3405
            self.attaque_max_3=227
            self.defense_max_3=201
            self.pv_max_4=4635
            self.attaque_max_4=309
            self.defense_max_4=273
            self.pv_max_5=6300
            self.attaque_max_5=420
            self.defense_max_5=371
            self.pv_max_6=8565
            self.attaque_max_6=571
            self.defense_max_6=505

            self.nb_capacites=2

            self.capacite1=Chevalier.clivage_terrestre
            self.capacite1_nom='Clivage Terrestre'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Chevalier.clivage_marin
            self.capacite2_nom='Clivage Marin'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Chevalier.chevalerie
            self.anti_passif_1=Chevalier.anti_chevalerie

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Chevalier',element[indice_element],3,1,1920,1920,107,128,97)

            self.pv_min_3=1920
            self.attaque_min_3=107
            self.defense_min_3=128
            self.pv_min_4=2775
            self.attaque_min_4=154
            self.defense_min_4=185
            self.pv_min_5=3780
            self.attaque_min_5=209
            self.defense_min_5=252
            self.pv_min_6=5130
            self.attaque_min_6=284
            self.defense_min_6=342

            self.pv_max_3=3465
            self.attaque_max_3=192
            self.defense_max_3=231
            self.pv_max_4=4725
            self.attaque_max_4=261
            self.defense_max_4=315
            self.pv_max_5=6420
            self.attaque_max_5=355
            self.defense_max_5=428
            self.pv_max_6=8730
            self.attaque_max_6=483
            self.defense_max_6=582

            self.nb_capacites=2

            self.capacite1=Chevalier.clivage_terrestre
            self.capacite1_nom='Clivage Terrestre'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Chevalier.provocation
            self.capacite2_nom='Provocation'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Chevalier.urgence

    def clivage_terrestre(self,cible):
        print('\n',self.surnom,self.attribut,' fend ',cible.surnom,cible.attribut,' avec son épée!!\n')
        degats=Arrondir.a_l_unite(0.18*self.pv_max_donjons)+self.calcul_dommages(1,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(1,self.capacite1_bonus_skill,degats-Arrondir.a_l_unite(0.18*self.pv_max_donjons),cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.4,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.def_break(2)

    def clivage_marin(self,cible):
        print('\n',self.surnom,self.attribut,' fend deux fois ',cible.surnom,cible.attribut,' de son épée!!\n')
        for index in range(2):
            degats=(Arrondir.a_l_unite(0.12*self.pv_max_donjons))+self.calcul_dommages(1,self.capacite2_bonus_skill,cible)
            self.affichage_du_type_de_coup(1,self.capacite2_bonus_skill,degats-(Arrondir.a_l_unite(0.12*self.pv_max_donjons)),cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    cible.atk_break(2)

    def provocation(self,cible):
        print('\n',self.surnom,self.attribut,' provoque ',cible.surnom,cible.attribut,'!!\n')
        degats=(Arrondir.a_l_unite(0.26*self.pv_max_donjons))+self.calcul_dommages(1.9,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(1.9,self.capacite2_bonus_skill,degats-(Arrondir.a_l_unite(0.26*self.pv_max_donjons)),cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.8,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                print(cible.surnom,cible.attribut,'est provoquée!! \n')
                cible.provoque=1
                cible.tours_provoque=max(2,cible.tours_provoque)
                self.provocation=1
                self.tours_provocation=2

    def abnegation(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' provoque toute l équipe ennemie!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.membres[index].pv_actuels>0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.8,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,'devient provoqué!!')
                    equipe_ennemie.membres[index].provoque=1
                    equipe_ennemie.membres[index].tours_provoque=max(2,equipe_ennemie.membres[index].tours_provoque)
                    self.provocation=1
                    self.tours_provocation=2
        self.tanky(3)

    def chevalerie(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].reduction_de_degats+=0.2
            print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit sa réduction de dégâts augmenter de 20%!!')
            print('La réduction de dégâts de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].reduction_de_degats,'!!\n')

    def anti_chevalerie(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].reduction_de_degats-=0.2

    def urgence(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Chevalier' and equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].attente1-=equipe_alliee.membres[index].nb_coups_subis
                if(equipe_alliee.membres[index].attente1<0):
                    equipe_alliee.membres[index].attente1=0
                equipe_alliee.membres[index].attente2-=equipe_alliee.membres[index].nb_coups_subis
                if(equipe_alliee.membres[index].attente2<0):
                    equipe_alliee.membres[index].attente2=0
                equipe_alliee.membres[index].nb_coups_subis=0


class Fee(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Fee',element[indice_element],3,1,1920,1920,124,112,101)

            self.pv_min_3=1920
            self.attaque_min_3=124
            self.defense_min_3=112
            self.pv_min_4=2775
            self.attaque_min_4=178
            self.defense_min_4=161
            self.pv_min_5=3780
            self.attaque_min_5=242
            self.defense_min_5=219
            self.pv_min_6=5130
            self.attaque_min_6=329
            self.defense_min_6=297

            self.pv_max_3=3465
            self.attaque_max_3=223
            self.defense_max_3=201
            self.pv_max_4=4725
            self.attaque_max_4=303
            self.defense_max_4=273
            self.pv_max_5=6420
            self.attaque_max_5=412
            self.defense_max_5=371
            self.pv_max_6=8730
            self.attaque_max_6=560
            self.defense_max_6=505

            self.nb_capacites=3

            self.capacite1=Fee.tourbillon
            self.capacite1_nom='Tourbillon'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Fee.double_fleche
            self.capacite2_nom='Double Flèche'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Fee.pluie_douleur
            self.capacite3_nom='Pluie de Douleur'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=6
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Fee',element[indice_element],3,1,1815,1815,107,136,103)

            self.pv_min_3=1815
            self.attaque_min_3=107
            self.defense_min_3=136
            self.pv_min_4=2625
            self.attaque_min_4=154
            self.defense_min_4=196
            self.pv_min_5=3570
            self.attaque_min_5=209
            self.defense_min_5=266
            self.pv_min_6=4845
            self.attaque_min_6=284
            self.defense_min_6=362

            self.pv_max_3=3270
            self.attaque_max_3=192
            self.defense_max_3=244
            self.pv_max_4=4455
            self.attaque_max_4=261
            self.defense_max_4=333
            self.pv_max_5=6060
            self.attaque_max_5=355
            self.defense_max_5=452
            self.pv_max_6=8235
            self.attaque_max_6=483
            self.defense_max_6=615

            self.nb_capacites=2

            self.capacite1=Fee.tourbillon
            self.capacite1_nom='Tourbillon'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Fee.soin
            self.capacite2_nom='Soin'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Fee.support
            self.anti_leader_skill=Fee.anti_support

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Fee',element[indice_element],2,1,1080,1080,77,67,103)

            self.pv_min_2=1080
            self.attaque_min_2=77
            self.defense_min_2=67
            self.pv_min_3=1635
            self.attaque_min_3=116
            self.defense_min_3=102
            self.pv_min_4=2355
            self.attaque_min_4=168
            self.defense_min_4=147
            self.pv_min_5=3210
            self.attaque_min_5=228
            self.defense_min_5=200
            self.pv_min_6=4365
            self.attaque_min_6=310
            self.defense_min_6=271

            self.pv_max_2=2040
            self.attaque_max_2=145
            self.defense_max_2=127
            self.pv_max_3=2940
            self.attaque_max_3=209
            self.defense_max_3=183
            self.pv_max_4=4005
            self.attaque_max_4=285
            self.defense_max_4=250
            self.pv_max_5=5445
            self.attaque_max_5=387
            self.defense_max_5=339
            self.pv_max_6=7410
            self.attaque_max_6=527
            self.defense_max_6=461

            self.nb_capacites=2

            self.capacite1=Fee.tourbillon
            self.capacite1_nom='Tourbillon'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Fee.soin
            self.capacite2_nom='Soin'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Fee',element[indice_element],3,1,2040,2040,136,92,100)

            self.pv_min_3=2040
            self.attaque_min_3=136
            self.defense_min_3=92
            self.pv_min_4=2940
            self.attaque_min_4=196
            self.defense_min_4=133
            self.pv_min_5=3990
            self.attaque_min_5=266
            self.defense_min_5=181
            self.pv_min_6=5430
            self.attaque_min_6=362
            self.defense_min_6=245

            self.pv_max_3=3660
            self.attaque_max_3=244
            self.defense_max_3=166
            self.pv_max_4=4995
            self.attaque_max_4=333
            self.defense_max_4=226
            self.pv_max_5=6780
            self.attaque_max_5=452
            self.defense_max_5=307
            self.pv_max_6=9225
            self.attaque_max_6=615
            self.defense_max_6=417

            self.nb_capacites=3

            self.capacite1=Fee.tourbillon
            self.capacite1_nom='Tourbillon'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Fee.soin
            self.capacite2_nom='Soin'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Fee.benediction
            self.capacite3_nom='Bénédiction de lumière'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=4
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Fee.support
            self.anti_leader_skill=Fee.anti_support

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Fee',element[indice_element],2,1,1035,1035,78,69,101)

            self.pv_min_2=1035
            self.attaque_min_2=78
            self.defense_min_2=69
            self.pv_min_3=1560
            self.attaque_min_3=119
            self.defense_min_3=104
            self.pv_min_4=2250
            self.attaque_min_4=171
            self.defense_min_4=150
            self.pv_min_5=3060
            self.attaque_min_5=233
            self.defense_min_5=204
            self.pv_min_6=4170
            self.attaque_min_6=316
            self.defense_min_6=278

            self.pv_max_2=1950
            self.attaque_max_2=148
            self.defense_max_2=130
            self.pv_max_3=2820
            self.attaque_max_3=214
            self.defense_max_3=188
            self.pv_max_4=3825
            self.attaque_max_4=291
            self.defense_max_4=255
            self.pv_max_5=5205
            self.attaque_max_5=396
            self.defense_max_5=347
            self.pv_max_6=7080
            self.attaque_max_6=538
            self.defense_max_6=472

            self.nb_capacites=2

            self.capacite1=Fee.tourbillon
            self.capacite1_nom='Tourbillon'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Fee.double_fleche
            self.capacite2_nom='Double Flèche'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

    def tourbillon(self,cible):
        print('\n',self.surnom,self.attribut,' balaye trois fois ',cible.surnom,cible.attribut,' avec un tourbillon magique!!\n')
        for index in range(3):
            degats=self.calcul_dommages(1.2,self.capacite1_bonus_skill,cible)
            self.affichage_du_type_de_coup(1.2,self.capacite1_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.2,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    if(self.attribut=='Eau'):
                        print(cible.surnom,cible.attribut,' est gelé(e)!! \n')
                        cible.gel=1
                    else:
                        print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                        cible.stun=1

    def soin(self,allie):
        print('\n',self.surnom,self.attribut,' soigne ',allie.surnom,allie.attribut,'!!\n')
        if (allie.pv_actuels>0):
            allie.soigner_de_tous_les_maux()
            print(allie.surnom,allie.attribut,'est débarrassé de tous les effets négatifs qui l affectaient!!')
            montant=self.attaque*(4+self.capacite2_bonus_skill)
            allie.etre_soigne(montant)
        elif (allie.pv_actuels<=0):
            print(allie.surnom,allie.attribut,' est mort!! \n')
        print('Il reste ',allie.pv_actuels,' point(s) de vie sur',allie.pv_max_donjons,' à ',allie.surnom,allie.attribut,'!! \n')

    # ignore la contre-attaque et la réflexion de dommages
    def double_fleche(self,equipe_ennemie):
        ''' ON PEUT CHOISIR POUR L ENNEMI !!! :( '''
        positions_ennemis=['de gauche','du centre','de droite']
        index=0
        while(index < equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels <= 0):
                equipe_ennemie.pop(index)
                positions_ennemis.pop(index)
                index-=1
            index+=1
        possibilites_cible=[]
        print('Vos ennemis sont : ')
        for index in range(equipe_ennemie.len):
            print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,positions_ennemis[index],' = ',index,'(',equipe_ennemie.membres[index].pv_actuels,'PV restants)')
            possibilites_cible.append(index)
        entree=input('Quelle cible voulez-vous attaquer ? ')
        while(not Security.is_decimal(entree)):
            entree=input('Quelle cible voulez-vous attaquer ? ')
        indice_cible=int(entree)
        while(indice_cible not in possibilites_cible):
            entree=input('Quelle cible voulez-vous attaquer ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Quelle cible voulez-vous attaquer ? ')
            indice_cible=int(entree)
        cible=equipe_ennemie.membres[indice_cible]
        print('\n',self.surnom,self.attribut,' tire une première flèche magique sur ',cible.surnom,cible.attribut,'!! \n')
        degats=self.calcul_dommages(3.4,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.4,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)

        if (equipe_ennemie.is_alive()):
            print('\n',self.surnom,self.attribut,' tire une deuxième flèche magique aléatoire sur l équipe ennemie!!\n')
            indice_cible_random=random.randint(0,equipe_ennemie.len-1)
            while(equipe_ennemie.membres[indice_cible_random].pv_actuels<=0):
                indice_cible_random=random.randint(0,equipe_ennemie.len-1)
            cible_2=equipe_ennemie.membres[indice_cible_random]
            degats=self.calcul_dommages(3.4,self.capacite2_bonus_skill,cible_2)
            self.affichage_du_type_de_coup(3.4,self.capacite2_bonus_skill,degats,cible_2)
            degats=self.reduction_dommages(cible_2,degats)
            self.procedure_attaque(degats,cible_2)
            ''' La comparaison s'effectue bien, même si les PV actuels ne sont plus les mêmes '''
            if(cible==cible_2):
                print(cible_2.surnom,cible_2.attribut,' est étourdi(e)!! \n')
                cible_2.stun=1

    def pluie_douleur(self,equipe_ennemie):
        nb_attaques=random.randint(4,6)
        print('\n',self.surnom,self.attribut,' attaque toute l\'équipe ennemie avec une pluie de flèches magiques aléatoires!!\n')
        for index in range(nb_attaques):
            if(equipe_ennemie.is_alive()):
                indice_cible=random.randint(0,equipe_ennemie.len-1)
                while(equipe_ennemie.membres[indice_cible].pv_actuels<=0):
                    indice_cible=random.randint(0,equipe_ennemie.len-1)
                cible=equipe_ennemie.membres[indice_cible]
                degats=self.calcul_dommages(0.85*equipe_ennemie.len,self.capacite3_bonus_skill,cible)
                self.affichage_du_type_de_coup(0.85,self.capacite3_bonus_skill,0.85*equipe_ennemie.len,cible)
                degats=cible.reduction_dommages(degats)
                self.procedure_attaque(degats,cible)
                if(cible.immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(0.2,cible.resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        cible.slow_down(2)

    def benediction(equipe_alliee):
        print('\nToute l\'équipe est bénie par la Déesse de la Lumière!!\n')
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels>0):
                if(equipe_alliee.membres[index].perturbation_recup>0):
                    print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces!!\n')
                else:
                    montant=Arrondir.a_l_unite(0.2*equipe_alliee.membres[index].pv_max_donjons)
                    equipe_alliee.membres[index].etre_soigne(montant)
                equipe_alliee.membres[index].jauge_attaque+=max(20,Arrondir.a_l_unite(0.2*equipe_alliee.membres[index].jauge_attaque))
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit sa jauge d\'attaque augmenter de 20%!!')
            else:
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est mort!! \n')
            print('\n')

    def support(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].resistance_max_donjons+=0.2
            equipe_alliee.membres[index].resistance_actuelle+=0.2
            print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 20%!!')
            print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].resistance_actuelle,'\n')

    def anti_support(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].resistance_actuelle-=0.2


class DameHarpie(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Dame Harpie',element[indice_element],3,1,1485,1485,170,95,102)

            self.pv_min_3=1485
            self.attaque_min_3=170
            self.defense_min_3=95
            self.pv_min_4=2145
            self.attaque_min_4=244
            self.defense_min_4=136
            self.pv_min_5=2925
            self.attaque_min_5=333
            self.defense_min_5=185
            self.pv_min_6=3975
            self.attaque_min_6=452
            self.defense_min_6=252

            self.pv_max_3=2685
            self.attaque_max_3=306
            self.defense_max_3=170
            self.pv_max_4=3660
            self.attaque_max_4=416
            self.defense_max_4=232
            self.pv_max_5=4965
            self.attaque_max_5=565
            self.defense_max_5=315
            self.pv_max_6=6750
            self.attaque_max_6=769
            self.defense_max_6=428

            self.nb_capacites=2

            self.capacite1=DameHarpie.griffe
            self.capacite1_nom='Griffe Céleste'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=DameHarpie.plumes
            self.capacite2_nom='Pluie de Plumes'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=DameHarpie.aura_flamboyante
            self.anti_leader_skill=DameHarpie.anti_aura_flamboyante

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Dame Harpie',element[indice_element],3,1,1710,1710,148,102,104)

            self.pv_min_3=1710
            self.attaque_min_3=148
            self.defense_min_3=102
            self.pv_min_4=2460
            self.attaque_min_4=213
            self.defense_min_4=147
            self.pv_min_5=3345
            self.attaque_min_5=290
            self.defense_min_5=200
            self.pv_min_6=4560
            self.attaque_min_6=394
            self.defense_min_6=271

            self.pv_max_3=3075
            self.attaque_max_3=266
            self.defense_max_3=183
            self.pv_max_4=4185
            self.attaque_max_4=362
            self.defense_max_4=250
            self.pv_max_5=5685
            self.attaque_max_5=492
            self.defense_max_5=339
            self.pv_max_6=7740
            self.attaque_max_6=670
            self.defense_max_6=461

            self.nb_capacites=3

            self.capacite1=DameHarpie.griffe
            self.capacite1_nom='Griffe Céleste'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=DameHarpie.serres
            self.capacite2_nom='Serres Céleste'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=DameHarpie.laceration
            self.capacite3_nom='Lacération Céleste'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=4
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Dame Harpie',element[indice_element],3,1,1860,1860,141,99,104)

            self.pv_min_3=1860
            self.attaque_min_3=141
            self.defense_min_3=99
            self.pv_min_4=2670
            self.attaque_min_4=203
            self.defense_min_4=143
            self.pv_min_5=3630
            self.attaque_min_5=276
            self.defense_min_5=195
            self.pv_min_6=4935
            self.attaque_min_6=375
            self.defense_min_6=265

            self.pv_max_3=3345
            self.attaque_max_3=253
            self.defense_max_3=179
            self.pv_max_4=4545
            self.attaque_max_4=345
            self.defense_max_4=244
            self.pv_max_5=6180
            self.attaque_max_5=468
            self.defense_max_5=331
            self.pv_max_6=8400
            self.attaque_max_6=637
            self.defense_max_6=450

            self.nb_capacites=3

            self.capacite1=DameHarpie.griffe
            self.capacite1_nom='Griffe Céleste'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=DameHarpie.plumes
            self.capacite2_nom='Pluie de Plumes'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=DameHarpie.laceration2
            self.capacite3_nom='Lacération Céleste'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=4
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Dame Harpie',element[indice_element],3,1,1560,1560,150,109,104)

            self.pv_min_3=1560
            self.attaque_min_3=150
            self.defense_min_3=109
            self.pv_min_4=2250
            self.attaque_min_4=216
            self.defense_min_4=157
            self.pv_min_5=3060
            self.attaque_min_5=295
            self.defense_min_5=214
            self.pv_min_6=4170
            self.attaque_min_6=400
            self.defense_min_6=291

            self.pv_max_3=2820
            self.attaque_max_3=271
            self.defense_max_3=196
            self.pv_max_4=3825
            self.attaque_max_4=368
            self.defense_max_4=267
            self.pv_max_5=5205
            self.attaque_max_5=500
            self.defense_max_5=363
            self.pv_max_6=7080
            self.attaque_max_6=681
            self.defense_max_6=494

            self.nb_capacites=3

            self.capacite1=DameHarpie.griffe
            self.capacite1_nom='Griffe Céleste'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=DameHarpie.plumes
            self.capacite2_nom='Pluie de Plumes'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=DameHarpie.danse
            self.capacite3_nom='Danse Divine'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Dame Harpie',element[indice_element],3,1,1605,1605,155,102,103)

            self.pv_min_3=1605
            self.attaque_min_3=155
            self.defense_min_3=102
            self.pv_min_4=2310
            self.attaque_min_4=223
            self.defense_min_4=147
            self.pv_min_5=3135
            self.attaque_min_5=304
            self.defense_min_5=200
            self.pv_min_6=4260
            self.attaque_min_6=413
            self.defense_min_6=271

            self.pv_max_3=2880
            self.attaque_max_3=279
            self.defense_max_3=183
            self.pv_max_4=3915
            self.attaque_max_4=380
            self.defense_max_4=250
            self.pv_max_5=5325
            self.attaque_max_5=517
            self.defense_max_5=339
            self.pv_max_6=7245
            self.attaque_max_6=703
            self.defense_max_6=461

            self.nb_capacites=2

            self.capacite1=DameHarpie.griffe
            self.capacite1_nom='Griffe Céleste'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=DameHarpie.serres
            self.capacite2_nom='Serres Céleste'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=DameHarpie.aura_demoniaque
            self.anti_leader_skill=DameHarpie.anti_aura_demoniaque

    def griffe(self,cible):
        print('\n',self.surnom,self.attribut,' griffe sauvagement ',cible.surnom,cible.attribut,'!!\n')
        degats=(-20)+self.calcul_dommages(3.7,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.7,self.capacite1_bonus_skill,degats+20,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.def_break(2)

    def serres(self,cible):
        print('\n',self.surnom,self.attribut,' lacère sauvagement ',cible.surnom,cible.attribut,' avec ses serres!!\n')
        for index in range(2):
            degats=self.calcul_dommages(2.7,self.capacite2_bonus_skill,cible)
            Type_coup=self.affichage_du_type_de_coup(2.7,self.capacite2_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(Type_coup=='Critique'):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1

    def plumes(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' attaque toute l\'équipe ennemie avec une pluie de plumes tranchantes aléatoires!!\n')
        nb_ennemis_vivants=0
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.membres[index].pv_actuels>0):
                nb_ennemis_vivants+=1
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive()):
                indice_cible=random.randint(0,equipe_ennemie.len-1)
                while(equipe_ennemie.membres[indice_cible].pv_actuels<=0):
                    indice_cible=random.randint(0,equipe_ennemie.len-1)
                cible=equipe_ennemie.membres[indice_cible]
                ''' Peut monter jusqu'à 7.8 dans les donjons OMG '''
                degats=self.calcul_dommages(2.6*nb_ennemis_vivants,self.capacite2_bonus_skill,cible)
                self.affichage_du_type_de_coup(2.6*nb_ennemis_vivants,self.capacite2_bonus_skill,degats,cible)
                degats=cible.reduction_dommages(degats)
                self.procedure_attaque(degats,cible)

    def danse(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].jauge_attaque+=max(30,Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].jauge_attaque))
            print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,'voit sa jauge d\'attaque augmenter de 30!!')
            equipe_alliee.membres[index].espada(3)

    def laceration(self,cible):
        print('\n',self.surnom,self.attribut,' fend les cieux pour lacérer mortellement ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(7,self.capacite3_bonus_skill,cible)
        self.affichage_du_type_de_coup(7,self.capacite3_bonus_skill,degats,cible)
        degats+=Arrondir.a_l_unite(self.attaque_actuelle*7*self.dommages_critiques_actuels)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)

    def laceration2(self,cible):
        print('\n',self.surnom,self.attribut,' fend les cieux pour lacérer mortellement ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(7,self.capacite3_bonus_skill,cible)
        self.affichage_du_type_de_coup(7,self.capacite3_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        print(cible.surnom,cible.attribut,' est étourdi(e)!!\n')
        cible.stun=1
        cible.def_break(2)

    def aura_flamboyante(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Feu'):
                equipe_alliee.membres[index].attaque_actuelle+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].attaque_max_donjons)
                equipe_alliee.membres[index].attaque_max_donjons+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].attaque_max_donjons)
                print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 30%!!')
                print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].attaque_actuelle,'\n')

    def aura_demoniaque(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].attaque_actuelle+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].attaque_max_donjons)
                equipe_alliee.membres[index].attaque_max_donjons+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].attaque_max_donjons)
                print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 30%!!')
                print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].attaque_actuelle,'\n')

    def anti_aura_flamboyante(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Feu'):
                equipe_alliee.membres[index].attaque_actuelle-=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].attaque_max_donjons)

    def anti_aura_demoniaque(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].attaque_actuelle-=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].attaque_max_donjons)


class Inugami(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Inugami',element[indice_element],3,1,1860,1860,136,104,107)

            self.pv_min_3=1860
            self.attaque_min_3=136
            self.defense_min_3=104
            self.pv_min_4=2670
            self.attaque_min_4=196
            self.defense_min_4=150
            self.pv_min_5=3630
            self.attaque_min_5=266
            self.defense_min_5=204
            self.pv_min_6=4935
            self.attaque_min_6=362
            self.defense_min_6=278

            self.pv_max_3=3345
            self.attaque_max_3=244
            self.defense_max_3=188
            self.pv_max_4=4545
            self.attaque_max_4=333
            self.defense_max_4=255
            self.pv_max_5=6180
            self.attaque_max_5=452
            self.defense_max_5=347
            self.pv_max_6=8400
            self.attaque_max_6=615
            self.defense_max_6=472

            self.nb_capacites=2

            self.capacite1=Inugami.griffe
            self.capacite1_nom='Griffe Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Inugami.coop
            self.capacite2_nom='Attaque en groupe'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Inugami',element[indice_element],3,1,2115,2115,109,114,107)

            self.pv_min_3=2115
            self.attaque_min_3=109
            self.defense_min_3=114
            self.pv_min_4=3045
            self.attaque_min_4=157
            self.defense_min_4=164
            self.pv_min_5=4140
            self.attaque_min_5=214
            self.defense_min_5=223
            self.pv_min_6=5625
            self.attaque_min_6=291
            self.defense_min_6=304

            self.pv_max_3=3795
            self.attaque_max_3=196
            self.defense_max_3=205
            self.pv_max_4=5175
            self.attaque_max_4=267
            self.defense_max_4=279
            self.pv_max_5=7020
            self.attaque_max_5=363
            self.defense_max_5=379
            self.pv_max_6=9555
            self.attaque_max_6=494
            self.defense_max_6=516

            self.nb_capacites=2

            self.capacite1=Inugami.griffe
            self.capacite1_nom='Griffe Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Inugami.coop
            self.capacite2_nom='Attaque en groupe'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Inugami.chef_de_meute_eau
            self.anti_leader_skill=Inugami.anti_chef_de_meute_eau

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Inugami',element[indice_element],3,1,1815,1815,102,141,107)

            self.pv_min_3=1815
            self.attaque_min_3=102
            self.defense_min_3=141
            self.pv_min_4=2625
            self.attaque_min_4=147
            self.defense_min_4=203
            self.pv_min_5=3570
            self.attaque_min_5=200
            self.defense_min_5=276
            self.pv_min_6=4845
            self.attaque_min_6=271
            self.defense_min_6=375

            self.pv_max_3=3270
            self.attaque_max_3=183
            self.defense_max_3=253
            self.pv_max_4=4455
            self.attaque_max_4=250
            self.defense_max_4=345
            self.pv_max_5=6060
            self.attaque_max_5=339
            self.defense_max_5=468
            self.pv_max_6=8235
            self.attaque_max_6=461
            self.defense_max_6=637

            self.nb_capacites=2

            self.capacite1=Inugami.griffe
            self.capacite1_nom='Griffe Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Inugami.entaille
            self.capacite2_nom='Entaille Vicieuse'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Inugami.chef_de_meute_vent
            self.anti_leader_skill=Inugami.anti_chef_de_meute_vent

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Inugami',element[indice_element],3,1,1995,1995,97,133,107)

            self.pv_min_3=1995
            self.attaque_min_3=97
            self.defense_min_3=133
            self.pv_min_4=2880
            self.attaque_min_4=140
            self.defense_min_4=192
            self.pv_min_5=3925
            self.attaque_min_5=190
            self.defense_min_5=261
            self.pv_min_6=5325
            self.attaque_min_6=258
            self.defense_min_6=355

            self.pv_max_3=3600
            self.attaque_max_3=175
            self.defense_max_3=240
            self.pv_max_4=4905
            self.attaque_max_4=238
            self.defense_max_4=327
            self.pv_max_5=6660
            self.attaque_max_5=323
            self.defense_max_5=444
            self.pv_max_6=9060
            self.attaque_max_6=439
            self.defense_max_6=604

            self.nb_capacites=3

            self.capacite1=Inugami.griffe
            self.capacite1_nom='Griffe Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Inugami.entaille
            self.capacite2_nom='Entaille Vicieuse'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Inugami.hurlement
            self.capacite3_nom='Hurlement'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Inugami',element[indice_element],3,1,1815,1815,128,114,107)

            self.pv_min_3=1815
            self.attaque_min_3=128
            self.defense_min_3=114
            self.pv_min_4=2625
            self.attaque_min_4=185
            self.defense_min_4=164
            self.pv_min_5=3570
            self.attaque_min_5=252
            self.defense_min_5=223
            self.pv_min_6=4845
            self.attaque_min_6=342
            self.defense_min_6=304

            self.pv_max_3=3270
            self.attaque_max_3=231
            self.defense_max_3=205
            self.pv_max_4=4455
            self.attaque_max_4=315
            self.defense_max_4=279
            self.pv_max_5=6060
            self.attaque_max_5=428
            self.defense_max_5=379
            self.pv_max_6=8235
            self.attaque_max_6=582
            self.defense_max_6=516

            self.nb_capacites=3

            self.capacite1=Inugami.griffe
            self.capacite1_nom='Griffe Acier'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Inugami.coop
            self.capacite2_nom='Attaque en groupe'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Inugami.laceration
            self.capacite3_nom='Lacération Profonde'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=4
            self.attente3=0
            self.etat_cap3='dispo'

    ''' Pour toutes les compétences suivantes '''
    ''' La condition marche car on ne peut pas renommer son montre 'Inugami bleu Royal' '''
    ''' Les espaces n'étant pas autorisés dans les surnoms, il est impossible de tricher '''

    def griffe(self,cible):
        print('\n',self.surnom,self.attribut,' griffe sauvagement ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.7,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.7,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        ''' On n'utilise pas Procedure_attaque ici car passif Aneantissement :
        tour_supplementaire_tmp augmente de 1 si la cible est tuée '''
        if (degats<=0):
            degats=1
        if(cible.immortalite<=0):
            cible.recoit_degats(degats)
            print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
            if (self.perturbation_recup<=0):
                self.etre_soigne(math.floor(self.vol_de_vie*degats/100))
        else:
            print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if (cible.pv_actuels<=0 and (self.attribut=='Feu' or self.surnom=='Inugami bleu Royal')):
            self.tour_supplementaire_tmp+=1
        elif(cible.pv_actuels<=0):
            print(cible.surnom,cible.attribut,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.def_break(2)

    def entaille(self,cible):
        print('\n',self.surnom,self.attribut,' lacère profondément ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(5.5,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(5.5,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        if (degats<=0):
            degats=1
        if(cible.immortalite<=0):
            cible.recoit_degats(degats)
            print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
            if (self.perturbation_recup<=0):
                self.etre_soigne(math.floor(self.vol_de_vie*degats/100))
        else:
            print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if (cible.pv_actuels<=0 and (self.attribut=='Feu' or self.surnom=='Inugami bleu Royal')):
            self.tour_supplementaire_tmp+=1
        elif(cible.pv_actuels<=0):
            print(cible.surnom,cible.attribut,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')
        cible.soigner_de_tous_les_biens()
        print(cible.surnom,cible.attribut,' perd tous les bonus qu\'il avait!! \n')

    def coop(self,equipe_alliee,cible):
        possibilites_coop=[]
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels>0 and (equipe_alliee.membres[index]!=self)):
                possibilites_coop.append(index)
        if(len(possibilites_coop)>0):
            indice_random=random.randint(0,len(possibilites_coop)-1)
            indice=possibilites_coop[indice_random]
            allie=equipe_alliee.membres[indice]
            print('\n',self.surnom,self.attribut,' et ',allie.surnom,allie.attribut,' lancent une attaque combinée sur ',cible.surnom,cible.attribut,'!!\n')
            degats=self.calcul_dommages(3.7,self.capacite2_bonus_skill,cible)
            self.affichage_du_type_de_coup(3.7,self.capacite2_bonus_skill,degats,cible)
            degats2=allie.calcul_dommages(3.7,allie.capacite1_bonus_skill,cible)
            allie.affichage_du_type_de_coup(3.7,allie.capacite1_bonus_skill,degats2,cible)
            degats+=degats2
            degats=cible.reduction_dommages(degats)
            if (degats<=0):
                degats=1
            if(cible.immortalite<=0):
                cible.recoit_degats(degats)
                print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
                if (self.perturbation_recup<=0):
                    self.etre_soigne(math.floor(self.vol_de_vie*degats/100))
            else:
                print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
            if (cible.pv_actuels<=0 and (self.attribut=='Feu' or self.surnom=='Inugami bleu Royal')):
                self.tour_supplementaire_tmp+=1
            elif(cible.pv_actuels<=0):
                print(cible.surnom,cible.attribut,' est mort!! \n')
            else:
                print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')

    def hurlement(equipe_alliee):
        print('\nToute l\'équipe est galvanisée par un hurlement sauvage!!\n')
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels>0):
                if(equipe_alliee.membres[index].perturbation_recup<=0):
                    montant=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].pv_max_donjons)
                    equipe_alliee.membres[index].etre_soigne(montant)
                equipe_alliee.membres[index].jauge_attaque+=max(30,Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].jauge_attaque))
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,'voit sa jauge d\'attaque augmenter de 30%!!')

    def laceration(self,cible):
        print('\n',self.surnom,self.attribut,' lacère profondément ',cible.surnom,cible.attribut,' en rouvrant ses cicatrices!!\n')
        degats=self.calcul_dommages(5.7,self.capacite3_bonus_skill,cible)
        self.affichage_du_type_de_coup(5.7,self.capacite3_bonus_skill,degats,cible)
        for index in range(cible.nb_effets_nocif()):
            degats+=Arrondir.a_l_unite(0.5*degats)
        degats=cible.reduction_dommages(degats)
        if (degats<=0):
            degats=1
        if(cible.immortalite<=0):
            cible.recoit_degats(degats)
            print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
            if (self.perturbation_recup<=0):
                self.etre_soigne(math.floor(self.vol_de_vie*degats/100))
        else:
            print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if (cible.pv_actuels<=0 and (self.attribut=='Feu' or self.surnom=='Inugami bleu Royal')):
            self.tour_supplementaire_tmp+=1
        elif(cible.pv_actuels<=0):
            print(cible.surnom,cible.attribut,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')

    def chef_de_meute_eau(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].vitesse_actuelle+=Arrondir.a_l_unite(0.23*equipe_alliee.membres[index].vitesse_max_donjons)
                equipe_alliee.membres[index].vitesse_max_donjons+=Arrondir.a_l_unite(0.23*equipe_alliee.membres[index].vitesse_max_donjons)
                print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 23%!!')
                print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].vitesse_actuelle,'\n')

    def chef_de_meute_vent(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Vent'):
                equipe_alliee.membres[index].vitesse_actuelle+=Arrondir.a_l_unite(0.23*equipe_alliee.membres[index].vitesse_max_donjons)
                equipe_alliee.membres[index].vitesse_max_donjons+=Arrondir.a_l_unite(0.23*equipe_alliee.membres[index].vitesse_max_donjons)
                print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 23%!!')
                print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].vitesse_actuelle,'\n')

    def anti_chef_de_meute_eau(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].vitesse_actuelle-=Arrondir.a_l_unite(0.23*equipe_alliee.membres[index].vitesse_max_donjons)

    def anti_chef_de_meute_vent(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Vent'):
                equipe_alliee.membres[index].vitesse_actuelle-=Arrondir.a_l_unite(0.23*equipe_alliee.membres[index].vitesse_max_donjons)


class Golem(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Golem',element[indice_element],3,1,1995,1995,80,150,88)

            self.pv_min_3=1995
            self.attaque_min_3=80
            self.defense_min_3=150
            self.pv_min_4=2880
            self.attaque_min_4=115
            self.defense_min_4=216
            self.pv_min_5=3915
            self.attaque_min_5=157
            self.defense_min_5=295
            self.pv_min_6=5325
            self.attaque_min_6=213
            self.defense_min_6=400

            self.pv_max_3=3600
            self.attaque_max_3=144
            self.defense_max_3=271
            self.pv_max_4=4905
            self.attaque_max_4=196
            self.defense_max_4=368
            self.pv_max_5=6660
            self.attaque_max_5=266
            self.defense_max_5=500
            self.pv_max_6=9060
            self.attaque_max_6=362
            self.defense_max_6=681

            self.nb_capacites=2

            self.capacite1=Golem.impact
            self.capacite1_nom='Impact'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Golem.corps_de_lave
            self.capacite2_nom='Corps de Lave'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Golem.barriere
            self.passif_active=0

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Golem',element[indice_element],3,1,2220,2220,73,143,86)

            self.pv_min_3=2220
            self.attaque_min_3=73
            self.defense_min_3=143
            self.pv_min_4=3195
            self.attaque_min_4=105
            self.defense_min_4=206
            self.pv_min_5=4350
            self.attaque_min_5=143
            self.defense_min_5=280
            self.pv_min_6=5910
            self.attaque_min_6=194
            self.defense_min_6=381

            self.pv_max_3=3990
            self.attaque_max_3=131
            self.defense_max_3=258
            self.pv_max_4=5430
            self.attaque_max_4=178
            self.defense_max_4=351
            self.pv_max_5=7380
            self.attaque_max_5=242
            self.defense_max_5=476
            self.pv_max_6=10050
            self.attaque_max_6=329
            self.defense_max_6=648

            self.nb_capacites=2

            self.capacite1=Golem.impact
            self.capacite1_nom='Impact'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Golem.corps_de_glace
            self.capacite2_nom='Corps de Glace'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Golem.barriere
            self.passif_active=0

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Golem',element[indice_element],3,1,2325,2325,82,126,91)

            self.pv_min_3=2325
            self.attaque_min_3=82
            self.defense_min_3=126
            self.pv_min_4=3345
            self.attaque_min_4=119
            self.defense_min_4=182
            self.pv_min_5=4560
            self.attaque_min_5=162
            self.defense_min_5=247
            self.pv_min_6=6195
            self.attaque_min_6=220
            self.defense_min_6=336

            self.pv_max_3=4185
            self.attaque_max_3=148
            self.defense_max_3=227
            self.pv_max_4=5700
            self.attaque_max_4=202
            self.defense_max_4=309
            self.pv_max_5=7755
            self.attaque_max_5=274
            self.defense_max_5=420
            self.pv_max_6=10545
            self.attaque_max_6=373
            self.defense_max_6=571

            self.nb_capacites=2

            self.capacite1=Golem.impact
            self.capacite1_nom='Impact'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Golem.mur_de_fer
            self.capacite2_nom='Mur de Fer'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=5
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Golem.tank_de_vent
            self.anti_leader_skill=Golem.anti_tank_de_vent

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Golem',element[indice_element],3,1,2145,2145,75,145,90)

            self.pv_min_3=2145
            self.attaque_min_3=75
            self.defense_min_3=145
            self.pv_min_4=3090
            self.attaque_min_4=108
            self.defense_min_4=209
            self.pv_min_5=4200
            self.attaque_min_5=147
            self.defense_min_5=285
            self.pv_min_6=5715
            self.attaque_min_6=200
            self.defense_min_6=387

            self.pv_max_3=3870
            self.attaque_max_3=135
            self.defense_max_3=262
            self.pv_max_4=5265
            self.attaque_max_4=184
            self.defense_max_4=356
            self.pv_max_5=7140
            self.attaque_max_5=250
            self.defense_max_5=484
            self.pv_max_6=9720
            self.attaque_max_6=340
            self.defense_max_6=659

            self.nb_capacites=2

            self.capacite1=Golem.impact
            self.capacite1_nom='Impact'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Golem.mur_de_fer
            self.capacite2_nom='Mur de Fer'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=5
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Golem.tank_de_lumiere
            self.anti_leader_skill=Golem.anti_tank_de_lumiere

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Golem',element[indice_element],3,1,2040,2040,85,143,88)

            self.pv_min_3=2040
            self.attaque_min_3=85
            self.defense_min_3=143
            self.pv_min_4=2940
            self.attaque_min_4=122
            self.defense_min_4=206
            self.pv_min_5=3990
            self.attaque_min_5=166
            self.defense_min_5=280
            self.pv_min_6=5430
            self.attaque_min_6=226
            self.defense_min_6=381

            self.pv_max_3=3660
            self.attaque_max_3=153
            self.defense_max_3=258
            self.pv_max_4=4995
            self.attaque_max_4=208
            self.defense_max_4=351
            self.pv_max_5=6780
            self.attaque_max_5=283
            self.defense_max_5=476
            self.pv_max_6=9225
            self.attaque_max_6=384
            self.defense_max_6=648

            self.nb_capacites=2

            self.capacite1=Golem.impact
            self.capacite1_nom='Impact'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Golem.corps_de_lave
            self.capacite2_nom='Corps de Ténèbres'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.pourcentage_reflexion_dommages=0.15
            self.reflexion_dommages=1


    def impact(self,cible):
        print('\n',self.surnom,self.attribut,' projette une onde de choc dévastatrice sur ',cible.surnom,cible.attribut,'!!\n')
        degats=(Arrondir.a_l_unite(2.5*self.defense_actuelle))+self.calcul_dommages(1.8,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(1.8,self.capacite1_bonus_skill,degats-(Arrondir.a_l_unite(2.5*(self.defense_actuelle))),cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.25,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1
            limite_reussite_2=Calcul.taux_reussite_effet(0.1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite_2):
                print(cible.surnom,cible.attribut,' est provoqué par ',self.surnom,self.attribut,' pour un tour!! \n')
                cible.provoque=1
                cible.tours_provoque=max(2,cible.tours_provoque)
                self.provocation=1
                self.tours_provocation=2

    def corps_de_lave(self,equipe_ennemie):
        if(self.attribut=='Feu'):
            print('\n',self.surnom,self.attribut,' écrase toute l\'équipe ennemie avec son corps de lave!!\n')
        elif(self.attribut=='Ténèbres'):
            print('\n',self.surnom,self.attribut,' écrase toute l\'équipe ennemie avec son corps de ténèbres!!\n')
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels>0):
                degats=(Arrondir.a_l_unite(2.5*self.defense_actuelle))+self.calcul_dommages(1.8,self.capacite2_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(1.8,self.capacite2_bonus_skill,degats-(Arrondir.a_l_unite(2.5*self.defense_actuelle)),equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    ''' CHECK SI LA PROBA EST DE 100 % OU DE 50 %, MEME SI 100 % FAIRE PREC ET RES '''
                    equipe_ennemie.membres[index].degats_continus(1,3)

    def corps_de_glace(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' écrase toute l\'équipe ennemie avec son corps de glace!!\n')
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels>0):
                degats=(Arrondir.a_l_unite(2.5*self.defense_actuelle))+self.calcul_dommages(2.5,self.capacite2_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(2.5,self.capacite2_bonus_skill,degats-(Arrondir.a_l_unite(2.5*self.defense_actuelle)),equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(0.5,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' est gelé(e)!! \n')
                        equipe_ennemie.membres[index].gel=1

    def mur_de_fer(self):
        print('\n',self.surnom,self.attribut,' se transforme en mur de fer!!\n')
        self.tanky(3)
        self.immunity(3)
        print('Sa jauge d\'attaque augmente à nouveau immédiatement!! \n')
        self.jauge_attaque+=max(50,Arrondir.a_l_unite(0.5*self.jauge_attaque))


    def barriere(equipe_alliee):
        liste_noms_alternatifs=['Golem rouge','Grand golem rouge','Golem rouge géant','Golem rouge Royal','Golem bleu','Grand golem bleu','Golem bleu géant']
        for index in range(equipe_alliee.len):
            if((equipe_alliee.membres[index].nom=='Golem' and (equipe_alliee.membres[index].attribut=='Feu' or equipe_alliee.membres[index].attribut=='Eau')) or (equipe_alliee.membres[index].nom in liste_noms_alternatifs)):
                if(equipe_alliee.membres[index].passif_active!=1 and equipe_alliee.membres[index].pv_actuels<=0.5*equipe_alliee.membres[index].pv_max_donjons):
                    print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit sa réduction de dégâts augmenter!!\n')
                    equipe_alliee.membres[index].reduction_de_degats+=0.5
                    equipe_alliee.membres[index].passif_active=1


    def tank_de_vent(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Vent'):
                equipe_alliee.membres[index].pv_actuels+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].pv_max_donjons)
                equipe_alliee.membres[index].pv_max_donjons+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].pv_max_donjons)
                print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 30%!!')
                print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].pv_actuels,'\n')

    def tank_de_lumiere(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Lumière'):
                equipe_alliee.membres[index].pv_actuels+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].pv_max_donjons)
                equipe_alliee.membres[index].pv_max_donjons+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].pv_max_donjons)
                print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 30%!!')
                print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].pv_actuels,'\n')

    def anti_tank_de_vent(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Vent'):
                equipe_alliee.membres[index].pv_actuels-=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].pv_max_donjons)

    def anti_tank_de_lumiere(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Lumière'):
                equipe_alliee.membres[index].pv_actuels-=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].pv_max_donjons)



''' Mettre des dégâts en fonction de la vitesse et / ou de la défense pour les augmenter'''
''' Rajouter un effet à charge du genre si cible est stun '''
''' Genre reçoit l\'immunité et augmente la défense pour deux ou trois tours '''

class Mastodonte(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Mastodonte',element[indice_element],3,1,1995,1995,80,150,92)

            self.pv_min_3=2325
            self.attaque_min_3=82
            self.defense_min_3=126
            self.pv_min_4=3345
            self.attaque_min_4=119
            self.defense_min_4=182
            self.pv_min_5=4560
            self.attaque_min_5=162
            self.defense_min_5=247
            self.pv_min_6=6195
            self.attaque_min_6=220
            self.defense_min_6=336

            self.pv_max_3=4185
            self.attaque_max_3=148
            self.defense_max_3=227
            self.pv_max_4=5700
            self.attaque_max_4=202
            self.defense_max_4=309
            self.pv_max_5=7755
            self.attaque_max_5=274
            self.defense_max_5=420
            self.pv_max_6=10545
            self.attaque_max_6=373
            self.defense_max_6=571

            self.nb_capacites=2

            self.capacite1=Mastodonte.corne
            self.capacite1_nom='Coup de Corne'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Mastodonte.pluie_de_gravats
            self.capacite2_nom='Pluie de Gravats'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Mastodonte.peau_dure
            self.passif_active=0

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Mastodonte',element[indice_element],3,1,2220,2220,73,143,90)

            self.pv_min_3=2145
            self.attaque_min_3=75
            self.defense_min_3=145
            self.pv_min_4=3090
            self.attaque_min_4=108
            self.defense_min_4=209
            self.pv_min_5=4200
            self.attaque_min_5=147
            self.defense_min_5=285
            self.pv_min_6=5715
            self.attaque_min_6=200
            self.defense_min_6=387

            self.pv_max_3=3870
            self.attaque_max_3=135
            self.defense_max_3=262
            self.pv_max_4=5265
            self.attaque_max_4=184
            self.defense_max_4=356
            self.pv_max_5=7140
            self.attaque_max_5=250
            self.defense_max_5=484
            self.pv_max_6=9720
            self.attaque_max_6=340
            self.defense_max_6=659

            self.nb_capacites=2

            self.capacite1=Mastodonte.corne
            self.capacite1_nom='Coup de Corne'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Mastodonte.armure_de_glace
            self.capacite2_nom='Armure de Glace'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Mastodonte.peau_dure
            self.passif_active=0

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Mastodonte',element[indice_element],3,1,2325,2325,82,126,95)

            self.pv_min_3=2220
            self.attaque_min_3=73
            self.defense_min_3=143
            self.pv_min_4=3195
            self.attaque_min_4=105
            self.defense_min_4=206
            self.pv_min_5=4350
            self.attaque_min_5=143
            self.defense_min_5=280
            self.pv_min_6=5910
            self.attaque_min_6=194
            self.defense_min_6=381

            self.pv_max_3=3990
            self.attaque_max_3=131
            self.defense_max_3=258
            self.pv_max_4=5430
            self.attaque_max_4=178
            self.defense_max_4=351
            self.pv_max_5=7380
            self.attaque_max_5=242
            self.defense_max_5=476
            self.pv_max_6=10050
            self.attaque_max_6=329
            self.defense_max_6=648

            self.nb_capacites=2

            self.capacite1=Mastodonte.corne
            self.capacite1_nom='Coup de Corne'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Mastodonte.charge
            self.capacite2_nom='Charge Dévastatrice'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Mastodonte.peau_dure
            self.passif_active=0

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Mastodonte',element[indice_element],3,1,2145,2145,75,145,94)

            self.pv_min_3=1995
            self.attaque_min_3=80
            self.defense_min_3=150
            self.pv_min_4=2880
            self.attaque_min_4=115
            self.defense_min_4=216
            self.pv_min_5=3915
            self.attaque_min_5=157
            self.defense_min_5=295
            self.pv_min_6=5325
            self.attaque_min_6=213
            self.defense_min_6=400

            self.pv_max_3=3600
            self.attaque_max_3=144
            self.defense_max_3=271
            self.pv_max_4=4905
            self.attaque_max_4=196
            self.defense_max_4=368
            self.pv_max_5=6660
            self.attaque_max_5=266
            self.defense_max_5=500
            self.pv_max_6=9060
            self.attaque_max_6=362
            self.defense_max_6=681

            self.nb_capacites=2

            self.capacite1=Mastodonte.corne
            self.capacite1_nom='Coup de Corne'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Mastodonte.charge
            self.capacite2_nom='Charge Dévastatrice'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Mastodonte.peau_dure
            self.passif_active=0

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Mastodonte',element[indice_element],3,1,2040,2040,85,143,92)

            self.pv_min_3=2040
            self.attaque_min_3=85
            self.defense_min_3=143
            self.pv_min_4=2940
            self.attaque_min_4=122
            self.defense_min_4=206
            self.pv_min_5=3990
            self.attaque_min_5=166
            self.defense_min_5=280
            self.pv_min_6=5430
            self.attaque_min_6=226
            self.defense_min_6=381

            self.pv_max_3=3660
            self.attaque_max_3=153
            self.defense_max_3=258
            self.pv_max_4=4995
            self.attaque_max_4=208
            self.defense_max_4=351
            self.pv_max_5=6780
            self.attaque_max_5=283
            self.defense_max_5=476
            self.pv_max_6=9225
            self.attaque_max_6=384
            self.defense_max_6=648

            self.nb_capacites=2

            self.capacite1=Mastodonte.corne
            self.capacite1_nom='Coup de Corne'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Mastodonte.pluie_de_gravats
            self.capacite2_nom='Pluie de Gravats'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Mastodonte.peau_dure
            self.passif_active=0


    def corne(self,cible):
        print('\n',self.surnom,self.attribut,' envoie valdinguer ',cible.surnom,cible.attribut,' d\'un puissant coup de corne!!\n')
        degats=self.calcul_dommages(4,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(4,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1

    def pluie_de_gravats(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' déclenche une pluie de gravats!!\n')
        nb_ennemis_vivants=0
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.membres[index].pv_actuels>0):
                nb_ennemis_vivants+=1
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels>0):
                print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' reçoit la pluie de gravats!!')
                degats=self.calcul_dommages(2.4*nb_ennemis_vivants,self.capacite2_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(2.4*nb_ennemis_vivants,self.capacite2_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])

    def charge(self,cible):
        print('\n',self.surnom,self.attribut,' charge sur ',cible.surnom,cible.attribut,' à pleine vitesse!!\n')
        degats=4*self.vitesse_actuelle+self.calcul_dommages(1.6,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(1.6,self.capacite2_bonus_skill,degats-4*self.vitesse_actuelle,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.8,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1

    def armure_de_glace(self):
        print('\n',self.surnom,self.attribut,' se renforce d\'une armure de glace!!\n')
        self.tanky(3)
        self.immunity(3)
        print('Il renverra une partie des dégâts subis pour trois tours!! \n')
        self.reflexion_dommages=1
        self.pourcentage_reflexion_dommages+=0.15
        self.tours_reflexion_dommages=max(self.tours_reflexion_dommages,3)

    def peau_dure(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Mastodonte' or equipe_alliee.membres[index].nom=='Mastodonte noir Royal'):
                if(equipe_alliee.membres[index].passif_active!=1 and equipe_alliee.membres[index].pv_actuels<=0.5*equipe_alliee.membres[index].pv_max_donjons):
                    print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit sa défense augmenter!!\n')
                    equipe_alliee.membres[index].defense_actuelle+=equipe_alliee.membres[index].defense_max_donjons
                    equipe_alliee.membres[index].passif_active=1


class Serpent(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Serpent',element[indice_element],3,1,2325,2325,112,97,99)

            self.pv_min_3=2325
            self.attaque_min_3=112
            self.defense_min_3=97
            self.pv_min_4=3345
            self.attaque_min_4=161
            self.defense_min_4=140
            self.pv_min_5=4560
            self.attaque_min_5=219
            self.defense_min_5=190
            self.pv_min_6=6195
            self.attaque_min_6=297
            self.defense_min_6=258

            self.pv_max_3=4185
            self.attaque_max_3=201
            self.defense_max_3=175
            self.pv_max_4=5700
            self.attaque_max_4=273
            self.defense_max_4=238
            self.pv_max_5=7755
            self.attaque_max_5=371
            self.defense_max_5=323
            self.pv_max_6=10545
            self.attaque_max_6=545
            self.defense_max_6=439

            self.nb_capacites=2

            self.capacite1=Serpent.morsure
            self.capacite1_nom='Morsure'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Serpent.deflagration
            self.capacite2_nom='Déflagration'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Serpent.tank_arena
            self.anti_leader_skill=Serpent.anti_tank_arena

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Serpent',element[indice_element],3,1,1920,1920,114,121,99)

            self.pv_min_3=1920
            self.attaque_min_3=114
            self.defense_min_3=121
            self.pv_min_4=2775
            self.attaque_min_4=164
            self.defense_min_4=175
            self.pv_min_5=3780
            self.attaque_min_5=223
            self.defense_min_5=238
            self.pv_min_6=5130
            self.attaque_min_6=304
            self.defense_min_6=323

            self.pv_max_3=3465
            self.attaque_max_3=205
            self.defense_max_3=218
            self.pv_max_4=4725
            self.attaque_max_4=279
            self.defense_max_4=297
            self.pv_max_5=6420
            self.attaque_max_5=379
            self.defense_max_5=404
            self.pv_max_6=8730
            self.attaque_max_6=516
            self.defense_max_6=549

            self.nb_capacites=3

            self.capacite1=Serpent.morsure
            self.capacite1_nom='Morsure'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Serpent.deflagration
            self.capacite2_nom='Déflagration'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Serpent.tsunami
            self.capacite3_nom='Raz de Marée'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=4
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Serpent',element[indice_element],3,1,2220,2220,116,99,99)

            self.pv_min_3=2220
            self.attaque_min_3=116
            self.defense_min_3=99
            self.pv_min_4=3195
            self.attaque_min_4=168
            self.defense_min_4=143
            self.pv_min_5=4350
            self.attaque_min_5=228
            self.defense_min_5=195
            self.pv_min_6=5910
            self.attaque_min_6=310
            self.defense_min_6=265

            self.pv_max_3=3990
            self.attaque_max_3=209
            self.defense_max_3=179
            self.pv_max_4=5430
            self.attaque_max_4=285
            self.defense_max_4=244
            self.pv_max_5=7380
            self.attaque_max_5=387
            self.defense_max_5=331
            self.pv_max_6=10050
            self.attaque_max_6=527
            self.defense_max_6=450

            self.nb_capacites=2

            self.capacite1=Serpent.morsure
            self.capacite1_nom='Morsure'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Serpent.orage
            self.capacite2_nom='Orage d\'Eclairs'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Serpent.coupe_feu

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Serpent',element[indice_element],3,1,2115,2115,109,114,99)

            self.pv_min_3=2115
            self.attaque_min_3=109
            self.defense_min_3=114
            self.pv_min_4=3045
            self.attaque_min_4=157
            self.defense_min_4=164
            self.pv_min_5=4140
            self.attaque_min_5=214
            self.defense_min_5=223
            self.pv_min_6=5625
            self.attaque_min_6=291
            self.defense_min_6=304

            self.pv_max_3=3795
            self.attaque_max_3=196
            self.defense_max_3=205
            self.pv_max_4=5175
            self.attaque_max_4=267
            self.defense_max_4=279
            self.pv_max_5=7020
            self.attaque_max_5=363
            self.defense_max_5=379
            self.pv_max_6=9555
            self.attaque_max_6=494
            self.defense_max_6=516

            self.nb_capacites=2

            self.capacite1=Serpent.morsure
            self.capacite1_nom='Morsure'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Serpent.deflagration
            self.capacite2_nom='Déflagration'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Serpent.renforcement
            self.nb_effets_renforcement=0

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Serpent',element[indice_element],3,1,1995,1995,124,107,99)

            self.pv_min_3=1995
            self.attaque_min_3=124
            self.defense_min_3=107
            self.pv_min_4=2880
            self.attaque_min_4=178
            self.defense_min_4=154
            self.pv_min_5=3915
            self.attaque_min_5=242
            self.defense_min_5=209
            self.pv_min_6=5325
            self.attaque_min_6=329
            self.defense_min_6=284

            self.pv_max_3=3600
            self.attaque_max_3=223
            self.defense_max_3=192
            self.pv_max_4=4905
            self.attaque_max_4=303
            self.defense_max_4=261
            self.pv_max_5=6660
            self.attaque_max_5=412
            self.defense_max_5=355
            self.pv_max_6=9060
            self.attaque_max_6=560
            self.defense_max_6=483

            self.nb_capacites=2

            self.capacite1=Serpent.morsure
            self.capacite1_nom='Morsure'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Serpent.orage
            self.capacite2_nom='Orage d\'Eclairs'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Serpent.tank_arena
            self.anti_leader_skill=Serpent.anti_tank_arena

    def morsure(self,cible):
        print('\n',self.surnom,self.attribut,' mord profondément ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(4,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(4,self.capacite1_bonus_skill,degats,cible)
        degats=self.reduction_ommages(cible,degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.75,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.retirer_un_bonus()

    def deflagration(self,cible):
        print('\n',self.surnom,self.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'une puissante déflagration!!\n')
        for index in range(3):
            degats=self.calcul_dommages(0.8,self.capacite2_bonus_skill,cible)
            self.affichage_du_type_de_coup(0.8,self.capacite2_bonus_skill,degats,cible)
            degats+=Arrondir.a_l_unite(0.08*self.pv_max_donjons)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.3,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    print(cible.surnom,cible.attribut,' voit sa jauge d\'attaque diminuer de 30%!!\n')
                    cible.jauge_attaque-=max(30,Arrondir.a_l_unite(0.3*cible.jauge_attaque))

    def tsunami(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' attaque toute l\'équipe ennemie avec un terrifiant raz de marée!!\n')
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels>0):
                print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' reçoit le tsunami!!')
                degats=Arrondir.a_l_unite(0.28*self.pv_max_donjons)
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' voit sa jauge d\'attaque diminuer de 30%!!\n')
                    equipe_ennemie.membres[index].jauge_attaque-=max(30,Arrondir.a_l_unite(0.3*equipe_ennemie.membres[index].jauge_attaque))

    def orage(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' attaque toute l\'équipe ennemie avec un orage d\'éclairs!!\n')
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels>0):
                print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' reçoit la foudre!!')
                degats=self.calcul_dommages(1,self.capacite2_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(1,self.capacite2_bonus_skill,degats,equipe_ennemie.membres[index])
                degats+=Arrondir.a_l_unite(0.16*self.pv_max_donjons)
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(1,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        self.slow_down(equipe_ennemie.membres[index],2)
                
    def tank_arena(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].pv_actuels+=Arrondir.a_l_unite(0.21*equipe_alliee.membres[index].pv_max_donjons)
            equipe_alliee.membres[index].pv_max_donjons+=Arrondir.a_l_unite(0.21*equipe_alliee.membres[index].pv_max_donjons)
            print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 21%!!')
            print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].pv_actuels,'\n')

    def anti_tank_arena(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].pv_actuels-=Arrondir.a_l_unite(0.21*equipe_alliee.membres[index].pv_max_donjons)

    def coupe_feu(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Serpent' and equipe_alliee.membres[index].attribut=='Vent'):
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,'subira deux fois moins de dégâts face à l\'Attribut Feu!!')

    def renforcement(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Serpent' and equipe_alliee.membres[index].attribut=='Lumière'):
                print('\n(Ré)actualisation du passif... ')
                equipe_alliee.membres[index].defense_actuelle-=Arrondir.a_l_unite(0.2*equipe_alliee.membres[index].defense_max_donjons*equipe_alliee.membres[index].nb_effets_renforcement)
                equipe_alliee.membres[index].attaque_actuelle-=Arrondir.a_l_unite(0.2*equipe_alliee.membres[index].attaque_max_donjons*equipe_alliee.membres[index].nb_effets_renforcement)
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' perd ',20*equipe_alliee.membres[index].nb_effets_renforcement,'% d\'attaque et de défense grâce à son passif!! \n')
                equipe_alliee.membres[index].nb_effets_renforcement=min(equipe_alliee.membres[index].nb_coups_subis,10)
                equipe_alliee.membres[index].defense_actuelle+=Arrondir.a_l_unite(0.2*equipe_alliee.membres[index].defense_max_donjons*equipe_alliee.membres[index].nb_effets_renforcement)
                equipe_alliee.membres[index].attaque_actuelle+=Arrondir.a_l_unite(0.2*equipe_alliee.membres[index].attaque_max_donjons*equipe_alliee.membres[index].nb_effets_renforcement)
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' gagne ',20*equipe_alliee.membres[index].nb_effets_renforcement,'% d\'attaque et de défense grâce à son passif car il a désormais subis ',equipe_alliee.membres[index].nb_effets_renforcement,' coups!! \n')


class Griffon(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Griffon',element[indice_element],3,1,1815,1815,114,128,110)

            self.pv_min_3=1815
            self.attaque_min_3=114
            self.defense_min_3=128
            self.pv_min_4=2625
            self.attaque_min_4=164
            self.defense_min_4=185
            self.pv_min_5=3570
            self.attaque_min_5=223
            self.defense_min_5=252
            self.pv_min_6=4845
            self.attaque_min_6=304
            self.defense_min_6=342

            self.pv_max_3=3270
            self.attaque_max_3=205
            self.defense_max_3=231
            self.pv_max_4=4455
            self.attaque_max_4=279
            self.defense_max_4=315
            self.pv_max_5=6060
            self.attaque_max_5=379
            self.defense_max_5=428
            self.pv_max_6=8235
            self.attaque_max_6=516
            self.defense_max_6=582

            self.nb_capacites=3

            self.capacite1=Griffon.griffes
            self.capacite1_nom='Griffes'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Griffon.ecrasement
            self.capacite2_nom='Ecrasement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Griffon.tornade
            self.capacite3_nom='Tornade'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Griffon',element[indice_element],3,1,2550,2550,73,121,110)

            self.pv_min_3=2550
            self.attaque_min_3=73
            self.defense_min_3=121
            self.pv_min_4=3660
            self.attaque_min_4=105
            self.defense_min_4=175
            self.pv_min_5=4995
            self.attaque_min_5=143
            self.defense_min_5=238
            self.pv_min_6=6780
            self.attaque_min_6=194
            self.defense_min_6=323

            self.pv_max_3=4590
            self.attaque_max_3=131
            self.defense_max_3=218
            self.pv_max_4=6240
            self.attaque_max_4=178
            self.defense_max_4=297
            self.pv_max_5=8475
            self.attaque_max_5=242
            self.defense_max_5=404
            self.pv_max_6=11535
            self.attaque_max_6=329
            self.defense_max_6=549

            self.nb_capacites=2

            self.capacite1=Griffon.griffes
            self.capacite1_nom='Griffes'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Griffon.laceration
            self.capacite2_nom='Lacération'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Griffon.water_power
            self.anti_leader_skill=Griffon.anti_water_power

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Griffon',element[indice_element],3,1,2070,2070,85,141,110)

            self.pv_min_3=2070
            self.attaque_min_3=85
            self.defense_min_3=141
            self.pv_min_4=2985
            self.attaque_min_4=122
            self.defense_min_4=203
            self.pv_min_5=4065
            self.attaque_min_5=166
            self.defense_min_5=276
            self.pv_min_6=5520
            self.attaque_min_6=226
            self.defense_min_6=375

            self.pv_max_3=3735
            self.attaque_max_3=153
            self.defense_max_3=253
            self.pv_max_4=5085
            self.attaque_max_4=208
            self.defense_max_4=345
            self.pv_max_5=6900
            self.attaque_max_5=283
            self.defense_max_5=468
            self.pv_max_6=9390
            self.attaque_max_6=384
            self.defense_max_6=637

            self.nb_capacites=3

            self.capacite1=Griffon.griffes
            self.capacite1_nom='Griffes'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Griffon.laceration
            self.capacite2_nom='Lacération'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Griffon.acceleration
            self.capacite3_nom='Accélération'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Griffon',element[indice_element],3,1,2175,2175,97,121,110)

            self.pv_min_3=2175
            self.attaque_min_3=97
            self.defense_min_3=121
            self.pv_min_4=3135
            self.attaque_min_4=140
            self.defense_min_4=175
            self.pv_min_5=4275
            self.attaque_min_5=190
            self.defense_min_5=238
            self.pv_min_6=5805
            self.attaque_min_6=258
            self.defense_min_6=323

            self.pv_max_3=3930
            self.attaque_max_3=175
            self.defense_max_3=218
            self.pv_max_4=5340
            self.attaque_max_4=238
            self.defense_max_4=297
            self.pv_max_5=7260
            self.attaque_max_5=323
            self.defense_max_5=404
            self.pv_max_6=9885
            self.attaque_max_6=439
            self.defense_max_6=549

            self.nb_capacites=2

            self.capacite1=Griffon.griffes
            self.capacite1_nom='Griffes'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Griffon.ecrasement
            self.capacite2_nom='Ecrasement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Griffon.bouclier_lumiere

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Griffon',element[indice_element],3,1,2325,2325,99,109,110)

            self.pv_min_3=2325
            self.attaque_min_3=99
            self.defense_min_3=109
            self.pv_min_4=3345
            self.attaque_min_4=143
            self.defense_min_4=157
            self.pv_min_5=4560
            self.attaque_min_5=195
            self.defense_min_5=214
            self.pv_min_6=6195
            self.attaque_min_6=265
            self.defense_min_6=291

            self.pv_max_3=4185
            self.attaque_max_3=179
            self.defense_max_3=196
            self.pv_max_4=5700
            self.attaque_max_4=244
            self.defense_max_4=267
            self.pv_max_5=7755
            self.attaque_max_5=331
            self.defense_max_5=363
            self.pv_max_6=10545
            self.attaque_max_6=450
            self.defense_max_6=494

            self.nb_capacites=2

            self.capacite1=Griffon.griffes
            self.capacite1_nom='Griffes'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Griffon.laceration
            self.capacite2_nom='Lacération'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Griffon.bouclier_tenebres

    def griffes(self,cible):
        print('\n',self.surnom,self.attribut,' griffe profondément ',cible.surnom,cible.attribut,'!!\n')
        degats=Arrondir.a_l_unite((90+self.vitesse_actuelle)/0.55)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)

    def laceration(self,cible):
        print('\n',self.surnom,self.attribut,' découpe ',cible.surnom,cible.attribut,' en morceaux!!\n')
        degats=self.calcul_dommages(5.1,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(5.1,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.def_break(2)
                cible.atk_break(2)

    def ecrasement(self,cible):
        print('\n',self.surnom,self.attribut,' s\'écrase de tout son poids sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.5,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.5,self.capacite2_bonus_skill,degats,cible)
        degats+=Arrondir.a_l_unite(0.18*cible.pv_max_donjons)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        print(self.surnom,self.attribut,' est heurté par le contrecoup!!')
        print(self.surnom,self.attribut,' subit ',Arrondir.a_l_unite(0.1*self.pv_max_donjons),' points de dégâts!!')
        self.pv_actuels-=Arrondir.a_l_unite(0.1*self.pv_max_donjons)
        if(self.pv_actuels<=0):
            print(self.surnom,self.attribut,' est mort!!')
        print('\n')

    def tornade(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' balaye toute l\'équipe ennemie avec une violente tornade!!\n')
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels>0):
                print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' reçoit la tornade!!')
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(1,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    self.slow_down(equipe_ennemie.membres[index],2)
                limite_reussite_2=Calcul.taux_reussite_effet(0.5,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite_2):
                    print('\n',equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' voit sa jauge d\'attaque diminuer de 30%!!')
                    equipe_ennemie.membres[index].jauge_attaque-=max(30,Arrondir.a_l_unite(0.3*equipe_ennemie.jauge_attaque))

    def acceleration(equipe_alliee):
        print('\nUn vent bénéfique vient accélérer toute l\'équipe!!\n')
        for index in range(equipe_alliee.len):
            if (equipe_alliee.membres[index].pv_actuels>0):
                self.speed_up(equipe_alliee.membres[index],2)
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit sa jauge d\'attaque augmenter de 30%!!\n')
                equipe_alliee.membres[index].jauge_attaque+=max(30,Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].jauge_attaque))

    def bouclier_lumiere(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Griffon' and equipe_alliee.membres[index].attribut=='Lumière'):
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit sa résistance augmenter!!\n')
                equipe_alliee.membres[index].resistance_actuelle+=0.2
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' subira deux fois moins de dégâts face à l\'Attribut Ténèbres!!')

    def anti_bouclier_lumiere(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Griffon' and equipe_alliee.membres[index].attribut=='Lumière'):
                equipe_alliee.membres[index].resistance_actuelle-=0.2

    def bouclier_tenebres(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Griffon' and equipe_alliee.membres[index].attribut=='Ténèbres'):
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit son vol de vie augmenter!!\n')
                equipe_alliee.membres[index].vol_de_vie+=20
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' subira deux fois moins de dégâts face à l\'Attribut Lumière!!')

    def anti_bouclier_tenebres(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Griffon' and equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].vol_de_vie-=20

    def water_power(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].attaque_actuelle+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].attaque_max_donjons)
                equipe_alliee.membres[index].attaque_max_donjons+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].attaque_max_donjons)
                print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 30%!!')
                print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].attaque_actuelle,'\n')

    def anti_water_power(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].attaque_actuelle-=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].attaque_max_donjons)


class Inferno(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Inferno',element[indice_element],3,1,1380,1380,182,90,94)

            self.pv_min_3=1380
            self.attaque_min_3=182
            self.defense_min_3=90
            self.pv_min_4=1995
            self.attaque_min_4=262
            self.defense_min_4=129
            self.pv_min_5=2715
            self.attaque_min_5=356
            self.defense_min_5=176
            self.pv_min_6=3675
            self.attaque_min_6=484
            self.defense_min_6=239

            self.pv_max_3=2490
            self.attaque_max_3=327
            self.defense_max_3=161
            self.pv_max_4=3390
            self.attaque_max_4=446
            self.defense_max_4=220
            self.pv_max_5=4605
            self.attaque_max_5=605
            self.defense_max_5=299
            self.pv_max_6=6255
            self.attaque_max_6=823
            self.defense_max_6=406

            self.nb_capacites=2

            self.capacite1=Inferno.frappe
            self.capacite1_nom='Frappe'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Inferno.deflagration
            self.capacite2_nom='Déflagration'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Inferno.critique_enflammee
            self.anti_leader_skill=Inferno.anti_critique_enflammee

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Inferno',element[indice_element],3,1,1425,1425,160,109,96)

            self.pv_min_3=1425
            self.attaque_min_3=160
            self.defense_min_3=109
            self.pv_min_4=2040
            self.attaque_min_4=230
            self.defense_min_4=157
            self.pv_min_5=2775
            self.attaque_min_5=314
            self.defense_min_5=214
            self.pv_min_6=3780
            self.attaque_min_6=426
            self.defense_min_6=291

            self.pv_max_3=2550
            self.attaque_max_3=288
            self.defense_max_3=196
            self.pv_max_4=3480
            self.attaque_max_4=392
            self.defense_max_4=267
            self.pv_max_5=4725
            self.attaque_max_5=533
            self.defense_max_5=363
            self.pv_max_6=6420
            self.attaque_max_6=725
            self.defense_max_6=494

            self.nb_capacites=3

            self.capacite1=Inferno.frappe
            self.capacite1_nom='Frappe'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Inferno._perforation
            self.capacite2_nom='Perforation'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Inferno.adrenaline
            self.capacite3_nom='Adrénaline'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Inferno._critique_gelee
            self.anti_leader_skill=Inferno.anti_critique_gelee

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Inferno',element[indice_element],3,1,1305,1305,167,109,97)

            self.pv_min_3=1305
            self.attaque_min_3=167
            self.defense_min_3=109
            self.pv_min_4=1890
            self.attaque_min_4=241
            self.defense_min_4=157
            self.pv_min_5=2565
            self.attaque_min_5=328
            self.defense_min_5=214
            self.pv_min_6=3480
            self.attaque_min_6=446
            self.defense_min_6=291

            self.pv_max_3=2355
            self.attaque_max_3=301
            self.defense_max_3=196
            self.pv_max_4=3210
            self.attaque_max_4=410
            self.defense_max_4=267
            self.pv_max_5=4365
            self.attaque_max_5=557
            self.defense_max_5=363
            self.pv_max_6=5925
            self.attaque_max_6=758
            self.defense_max_6=494

            self.nb_capacites=3

            self.capacite1=Inferno.frappe
            self.capacite1_nom='Frappe'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Inferno.orage
            self.capacite2_nom='Orage d\'Eclairs'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Inferno.coup_mortel
            self.capacite3_nom='Coup Mortel'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=4
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Inferno',element[indice_element],3,1,1485,1485,175,90,94)

            self.pv_min_3=1485
            self.attaque_min_3=175
            self.defense_min_3=90
            self.pv_min_4=2145
            self.attaque_min_4=251
            self.defense_min_4=129
            self.pv_min_5=2925
            self.attaque_min_5=342
            self.defense_min_5=176
            self.pv_min_6=3975
            self.attaque_min_6=465
            self.defense_min_6=239

            self.pv_max_3=2685
            self.attaque_max_3=314
            self.defense_max_3=161
            self.pv_max_4=3660
            self.attaque_max_4=428
            self.defense_max_4=220
            self.pv_max_5=4965
            self.attaque_max_5=581
            self.defense_max_5=299
            self.pv_max_6=6750
            self.attaque_max_6=790
            self.defense_max_6=406

            self.nb_capacites=3

            self.capacite1=Inferno.frappe
            self.capacite1_nom='Frappe'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Inferno.perforation
            self.capacite2_nom='Perforation'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Inferno.jugement_divin
            self.capacite3_nom='Jugement Divin'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Inferno',element[indice_element],3,1,1230,1230,186,95,94)

            self.pv_min_3=1230
            self.attaque_min_3=186
            self.defense_min_3=95
            self.pv_min_4=1785
            self.attaque_min_4=269
            self.defense_min_4=136
            self.pv_min_5=2430
            self.attaque_min_5=366
            self.defense_min_5=185
            self.pv_min_6=3300
            self.attaque_min_6=497
            self.defense_min_6=252

            self.pv_max_3=2200
            self.attaque_max_3=335
            self.defense_max_3=170
            self.pv_max_4=3030
            self.attaque_max_4=457
            self.defense_max_4=232
            self.pv_max_5=4110
            self.attaque_max_5=622
            self.defense_max_5=315
            self.pv_max_6=5595
            self.attaque_max_6=845
            self.defense_max_6=428

            self.nb_capacites=2

            self.capacite1=Inferno.frappe
            self.capacite1_nom='Frappe'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Inferno.deflagration
            self.capacite2_nom='Déflagration'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Inferno.critique_sombre
            self.anti_leader_skill=Inferno.anti_critique_sombre

    def frappe(self,cible):
        print('\n',self.surnom,self.attribut,' frappe violemment ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.9,self.capacite1_bonus_skill,cible)
        type_coup=self.affichage_du_type_de_coup(3.9,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(type_coup=='Critique'):
            print(self.surnom,self.attribut,' voit sa jauge d\'attaque augmenter immédiatement!! \n')
            self.jauge_attaque+=max(30,Arrondir.a_l_unite(0.3*self.jauge_attaque))

    def perforation(self,cible):
        self.taux_coup_critique_actuel+=0.5
        print('\n',self.surnom,self.attribut,' perfore ',cible.surnom,cible.attribut,' avec un pieux élémentaire!!\n')
        degats=self.calcul_dommages(5.5,self.capacite2_bonus_skill,cible)
        type_coup=self.affichage_du_type_de_coup(5.5,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        self.taux_coup_critique_actuel-=0.5
        if(type_coup=='Critique'):
            print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
            cible.stun=1

    def deflagration(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' attaque toute l\'équipe ennemie avec une puissante déflagration!!\n')
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels>0):
                print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' reçoit la déflagration!!')
                degats=self.calcul_dommages(2.7,self.capacite2_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(2.7,self.capacite2_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(0.7,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        self.def_break(equipe_ennemie.membres[index],2)

    def orage(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' attaque toute l\'équipe ennemie avec un orage d\'éclairs!!\n')
        for index in range(equipe_ennemie.len):
            if (equipe_ennemie.membres[index].pv_actuels>0):
                print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' reçoit la foudre!!')
                degats=self.calcul_dommages(2.7,self.capacite2_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(2.7,self.capacite2_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(0.8,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        equipe_ennemie.membres[index].atk_break(2)

    def jugement_divin(self,cible):
        print('\n',self.surnom,self.attribut,' fait s\'abattre le jugement divin sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(7.7,self.capacite3_bonus_skill,cible)
        self.affichage_du_type_de_coup(7.7,self.capacite3_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        cible.soigner_de_tous_les_biens()

    def coup_mortel(self,cible):
        print('\n',self.surnom,self.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un coup mortel!!\n')
        degats=self.calcul_dommages(7.7,self.capacite3_bonus_skill,cible)
        self.affichage_du_type_de_coup(7.7,self.capacite3_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        print(cible.surnom,cible.attribut,' voit sa jauge d\'attaque réduite à zéro!! \n')
        cible.jauge_attaque=0

    def adrenaline(equipe_alliee):
        print('\nToute l\'équipe sent son adrénaline augmenter!!\n')
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].jauge_attaque+=max(50,Arrondir.a_l_unite(0.5*equipe_alliee.membres[index].jauge_attaque))
            print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit sa jauge d\'attaque augmenter de moitié!!')
            equipe_alliee.membres[index].espada(3)

    def critique_enflammee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Feu'):
                equipe_alliee.membres[index].taux_coup_critique_actuel+=0.23
                equipe_alliee.membres[index].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].taux_coup_critique_actuel,'\n')
                
    def critique_gelee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].taux_coup_critique_actuel+=0.23
                equipe_alliee.membres[index].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].taux_coup_critique_actuel,'\n')

    def critique_sombre(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].taux_coup_critique_actuel+=0.23
                equipe_alliee.membres[index].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].taux_coup_critique_actuel,'\n')

    def anti_critique_enflammee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Feu'):
                equipe_alliee.membres[index].taux_coup_critique_actuel-=0.23

    def anti_critique_gelee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].taux_coup_critique_actuel-=0.23

    def anti_critique_sombre(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].taux_coup_critique_actuel-=0.23


class HautElementaire(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Haut Elementaire',element[indice_element],3,1,1275,1275,172,107,101)

            self.pv_min_3=1275
            self.attaque_min_3=172
            self.defense_min_3=107
            self.pv_min_4=1830
            self.attaque_min_4=248
            self.defense_min_4=154
            self.pv_min_5=2490
            self.attaque_min_5=337
            self.defense_min_5=209
            self.pv_min_6=3390
            self.attaque_min_6=459
            self.defense_min_6=284

            self.pv_max_3=2295
            self.attaque_max_3=310
            self.defense_max_3=192
            self.pv_max_4=3120
            self.attaque_max_4=422
            self.defense_max_4=261
            self.pv_max_5=4245
            self.attaque_max_5=573
            self.defense_max_5=355
            self.pv_max_6=5760
            self.attaque_max_6=780
            self.defense_max_6=483

            self.nb_capacites=2

            self.capacite1=HautElementaire.projectiles
            self.capacite1_nom='Projectiles Elementaires'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=HautElementaire.entaille
            self.capacite2_nom='Entaille Tectonique'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=HautElementaire.critique_enflammee
            self.anti_leader_skill=HautElementaire.anti_critique_enflammee

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Haut Elementaire',element[indice_element],3,1,1230,1230,160,121,102)

            self.pv_min_3=1230
            self.attaque_min_3=160
            self.defense_min_3=121
            self.pv_min_4=1785
            self.attaque_min_4=230
            self.defense_min_4=175
            self.pv_min_5=2430
            self.attaque_min_5=314
            self.defense_min_5=238
            self.pv_min_6=3300
            self.attaque_min_6=426
            self.defense_min_6=323

            self.pv_max_3=2220
            self.attaque_max_3=288
            self.defense_max_3=218
            self.pv_max_4=3030
            self.attaque_max_4=392
            self.defense_max_4=297
            self.pv_max_5=4110
            self.attaque_max_5=533
            self.defense_max_5=404
            self.pv_max_6=5595
            self.attaque_max_6=725
            self.defense_max_6=549

            self.nb_capacites=2

            self.capacite1=HautElementaire.projectiles
            self.capacite1_nom='Projectiles Elementaires'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=HautElementaire.entaille
            self.capacite2_nom='Entaille Tectonique'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=HautElementaire.critique_gelee
            self.anti_leader_skill=HautElementaire.anti_critique_gelee

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Haut Elementaire',element[indice_element],3,1,1170,1170,184,102,104)

            self.pv_min_3=1170
            self.attaque_min_3=184
            self.defense_min_3=102
            self.pv_min_4=1680
            self.attaque_min_4=265
            self.defense_min_4=147
            self.pv_min_5=2280
            self.attaque_min_5=361
            self.defense_min_5=200
            self.pv_min_6=3105
            self.attaque_min_6=491
            self.defense_min_6=271

            self.pv_max_3=2100
            self.attaque_max_3=332
            self.defense_max_3=183
            self.pv_max_4=2850
            self.attaque_max_4=452
            self.defense_max_4=250
            self.pv_max_5=3870
            self.attaque_max_5=613
            self.defense_max_5=339
            self.pv_max_6=5265
            self.attaque_max_6=834
            self.defense_max_6=461

            self.nb_capacites=2

            self.capacite1=HautElementaire.projectiles
            self.capacite1_nom='Projectiles Elementaires'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=HautElementaire.separation
            self.capacite2_nom='Séparation du Corps et de l\'Âme'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=HautElementaire.critique_soufflee
            self.anti_leader_skill=HautElementaire.anti_critique_soufflee

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Haut Elementaire',element[indice_element],3,1,1995,1995,145,85,103)

            self.pv_min_3=1995
            self.attaque_min_3=145
            self.defense_min_3=85
            self.pv_min_4=2880
            self.attaque_min_4=209
            self.defense_min_4=122
            self.pv_min_5=3915
            self.attaque_min_5=285
            self.defense_min_5=166
            self.pv_min_6=5325
            self.attaque_min_6=387
            self.defense_min_6=226

            self.pv_max_3=3600
            self.attaque_max_3=262
            self.defense_max_3=153
            self.pv_max_4=4905
            self.attaque_max_4=356
            self.defense_max_4=208
            self.pv_max_5=6660
            self.attaque_max_5=484
            self.defense_max_5=283
            self.pv_max_6=9060
            self.attaque_max_6=659
            self.defense_max_6=384

            self.nb_capacites=2

            self.capacite1=HautElementaire.projectiles
            self.capacite1_nom='Projectiles Elementaires'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=HautElementaire.entaille
            self.capacite2_nom='Entaille Tectonique'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=HautElementaire.critique_eclairee
            self.anti_leader_skill=HautElementaire.anti_critique_eclairee

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Haut Elementaire',element[indice_element],3,1,1230,1230,177,104,103)

            self.pv_min_3=1230
            self.attaque_min_3=177
            self.defense_min_3=104
            self.pv_min_4=1785
            self.attaque_min_4=255
            self.defense_min_4=150
            self.pv_min_5=2430
            self.attaque_min_5=347
            self.defense_min_5=204
            self.pv_min_6=3300
            self.attaque_min_6=471
            self.defense_min_6=278

            self.pv_max_3=2200
            self.attaque_max_3=319
            self.defense_max_3=188
            self.pv_max_4=3030
            self.attaque_max_4=434
            self.defense_max_4=255
            self.pv_max_5=4110
            self.attaque_max_5=589
            self.defense_max_5=347
            self.pv_max_6=5595
            self.attaque_max_6=801
            self.defense_max_6=472

            self.nb_capacites=2

            self.capacite1=HautElementaire.projectiles
            self.capacite1_nom='Projectiles Elementaires'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=HautElementaire.separation
            self.capacite2_nom='Séparation du Corps et de l\'Âme'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=HautElementaire.critique_sombre
            self.anti_leader_skill=HautElementaire.anti_critique_sombre

    def projectiles(self,cible):
        print('\n',self.surnom,self.attribut,' jette deux sphères élémentaires sur ',cible.surnom,cible.attribut,'!!\n')
        for index in range(2):
            degats=self.calcul_dommages(3.8,self.capacite1_bonus_skill,cible)
            self.affichage_du_type_de_coup(3.8,self.capacite1_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.2,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    cible.degats_continus(1,3)

    def entaille(self,cible):
        print('\n',self.surnom,self.attribut,' fend ',cible.surnom,cible.attribut,'en deux avec une entaille tectonique qui ignore la défense!!\n')
        degats=self.calcul_dommages(3,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(3,self.capacite2_bonus_skill,degats,cible)
        self.procedure_attaque(degats,cible)

    def separation(self,cible):
        print('\n',self.surnom,self.attribut,' sépare le Corps et l\'Âme de ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(6.3,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(6.3,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.perturbation_recuperation(2)
        if(cible.pv_actuels<=0 and self.perturbation_recup<=0):
            print(self.surnom,self.attribut,' dévore l\'Âme de ',cible.surnom,cible.attribut,'!! \n')
            ''' Le montant est 35% des PV max de la cible ou du HE ? '''
            montant=Arrondir.a_l_unite(0.35*self.pv_max_donjons)
            self.etre_soigne(montant)

    def critique_enflammee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Feu'):
                equipe_alliee.membres[index].taux_coup_critique_actuel+=0.23
                equipe_alliee.membres[index].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].taux_coup_critique_actuel,'\n')

    def critique_gelee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].taux_coup_critique_actuel+=0.23
                equipe_alliee.membres[index].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].taux_coup_critique_actuel,'\n')

    def critique_soufflee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Vent'):
                equipe_alliee.membres[index].taux_coup_critique_actuel+=0.23
                equipe_alliee.membres[index].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].taux_coup_critique_actuel,'\n')

    def critique_eclairee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Lumière'):
                equipe_alliee.membres[index].taux_coup_critique_actuel+=0.23
                equipe_alliee.membres[index].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].taux_coup_critique_actuel,'\n')

    def critique_sombre(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].taux_coup_critique_actuel+=0.23
                equipe_alliee.membres[index].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].taux_coup_critique_actuel,'\n')

    def anti_critique_enflammee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Feu'):
                equipe_alliee.membres[index].taux_coup_critique_actuel-=0.23

    def anti_critique_gelee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].taux_coup_critique_actuel-=0.23

    def anti_critique_soufflee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Vent'):
                equipe_alliee.membres[index].taux_coup_critique_actuel-=0.23

    def anti_critique_eclairee(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Lumière'):
                equipe_alliee.membres[index].taux_coup_critique_actuel-=0.23

    def anti_critique_sombre(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].taux_coup_critique_actuel-=0.23


class OursDeCombat(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Ours de Combat',element[indice_element],3,1,2250,2250,80,133,100)

            self.pv_min_3=2250
            self.attaque_min_3=80
            self.defense_min_3=133
            self.pv_min_4=3240
            self.attaque_min_4=115
            self.defense_min_4=192
            self.pv_min_5=4425
            self.attaque_min_5=157
            self.defense_min_5=261
            self.pv_min_6=6000
            self.attaque_min_6=213
            self.defense_min_6=355

            self.pv_max_3=4065
            self.attaque_max_3=144
            self.defense_max_3=240
            self.pv_max_4=5520
            self.attaque_max_4=196
            self.defense_max_4=327
            self.pv_max_5=7500
            self.attaque_max_5=266
            self.defense_max_5=444
            self.pv_max_6=10215
            self.attaque_max_6=362
            self.defense_max_6=604

            self.nb_capacites=2

            self.capacite1=OursDeCombat.griffe
            self.capacite1_nom='Griffe de combat'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=OursDeCombat.massue
            self.capacite2_nom='Massue de combat'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=OursDeCombat.bouclier_enflamme
            self.anti_leader_skill=OursDeCombat.anti_bouclier_enflamme

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Ours de Combat',element[indice_element],3,1,2325,2325,78,131,100)

            self.pv_min_3=2325
            self.attaque_min_3=78
            self.defense_min_3=131
            self.pv_min_4=3345
            self.attaque_min_4=112
            self.defense_min_4=189
            self.pv_min_5=4560
            self.attaque_min_5=152
            self.defense_min_5=257
            self.pv_min_6=6195
            self.attaque_min_6=207
            self.defense_min_6=349

            self.pv_max_3=4185
            self.attaque_max_3=140
            self.defense_max_3=236
            self.pv_max_4=5700
            self.attaque_max_4=190
            self.defense_max_4=321
            self.pv_max_5=7755
            self.attaque_max_5=258
            self.defense_max_5=436
            self.pv_max_6=10545
            self.attaque_max_6=351
            self.defense_max_6=593

            self.nb_capacites=2

            self.capacite1=OursDeCombat.griffe
            self.capacite1_nom='Griffe de Combat'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=OursDeCombat.massue
            self.capacite2_nom='Massue de combat'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=OursDeCombat.bouclier_gele
            self.anti_leader_skill=OursDeCombat.anti_bouclier_gele

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Ours De Combat',element[indice_element],3,1,2115,2115,114,109,100)

            self.pv_min_3=2115
            self.attaque_min_3=114
            self.defense_min_3=109
            self.pv_min_4=3045
            self.attaque_min_4=164
            self.defense_min_4=157
            self.pv_min_5=4140
            self.attaque_min_5=223
            self.defense_min_5=214
            self.pv_min_6=5625
            self.attaque_min_6=304
            self.defense_min_6=291

            self.pv_max_3=3795
            self.attaque_max_3=205
            self.defense_max_3=196
            self.pv_max_4=5175
            self.attaque_max_4=279
            self.defense_max_4=267
            self.pv_max_5=7020
            self.attaque_max_5=379
            self.defense_max_5=363
            self.pv_max_6=9555
            self.attaque_max_6=516
            self.defense_max_6=494

            self.nb_capacites=2

            self.capacite1=OursDeCombat.griffe
            self.capacite1_nom='Griffe de combat'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=OursDeCombat.cri
            self.capacite2_nom='Cri de Renforcement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=OursDeCombat.bouclier_souffle
            self.anti_leader_skill=OursDeCombat.anti_bouclier_souffle

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Ours de Combat',element[indice_element],3,1,2145,2145,109,112,100)

            self.pv_min_3=2145
            self.attaque_min_3=109
            self.defense_min_3=112
            self.pv_min_4=3090
            self.attaque_min_4=157
            self.defense_min_4=161
            self.pv_min_5=4200
            self.attaque_min_5=214
            self.defense_min_5=219
            self.pv_min_6=5715
            self.attaque_min_6=291
            self.defense_min_6=297

            self.pv_max_3=3870
            self.attaque_max_3=196
            self.defense_max_3=201
            self.pv_max_4=5265
            self.attaque_max_4=267
            self.defense_max_4=273
            self.pv_max_5=7140
            self.attaque_max_5=363
            self.defense_max_5=371
            self.pv_max_6=9720
            self.attaque_max_6=494
            self.defense_max_6=505

            self.nb_capacites=2

            self.capacite1=OursDeCombat.griffe
            self.capacite1_nom='Griffe de combat'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=OursDeCombat.massue
            self.capacite2_nom='Massue de combat'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=OursDeCombat.bouclier_eclaire
            self.anti_leader_skill=OursDeCombat.anti_bouclier_eclaire

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Ours de Combat',element[indice_element],3,1,2040,2040,102,126,100)

            self.pv_min_3=2040
            self.attaque_min_3=102
            self.defense_min_3=126
            self.pv_min_4=2940
            self.attaque_min_4=147
            self.defense_min_4=182
            self.pv_min_5=3990
            self.attaque_min_5=200
            self.defense_min_5=247
            self.pv_min_6=5430
            self.attaque_min_6=271
            self.defense_min_6=336

            self.pv_max_3=3660
            self.attaque_max_3=183
            self.defense_max_3=227
            self.pv_max_4=4995
            self.attaque_max_4=250
            self.defense_max_4=309
            self.pv_max_5=6780
            self.attaque_max_5=339
            self.defense_max_5=420
            self.pv_max_6=9225
            self.attaque_max_6=461
            self.defense_max_6=571

            self.nb_capacites=2

            self.capacite1=OursDeCombat.griffe
            self.capacite1_nom='Griffe de combat'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=OursDeCombat.cri
            self.capacite2_nom='Cri de Renforcement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=OursDeCombat.bouclier_sombre
            self.anti_leader_skill=OursDeCombat.anti_bouclier_sombre

    def griffe(self,cible):
        print('\n',self.surnom,self.attribut,' griffe férocement ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.8,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.8,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                print(cible.surnom,cible.attribut,' est provoqué(e) pour un tour!! \n')
                cible.provoque=1
                cible.tours_provoque=max(2,cible.tours_provoque)
                self.provocation=1
                self.tours_provocation=2

    def massue(self,cible):
        print('\n',self.surnom,self.attribut,' abat son énorme massue sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(3,self.capacite2_bonus_skill,degats,cible)
        degats+=Arrondir.a_l_unite(0.15*self.pv_max_donjons)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)

    def cri(equipe_alliee):
        print('\nUn Cri de Renforcement retentit!! Toute l\'équipe voit ses forces augmenter!!\n')
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels>0):
                equipe_alliee.membres[index].retirer_un_malus()
                equipe_alliee.membres[index].retirer_un_malus()
                equipe_alliee.membres[index].rise(2)

    def bouclier_enflamme(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Feu'):
                equipe_alliee.membres[index].defense_actuelle+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)
                equipe_alliee.membres[index].defense_max_donjons+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)
                print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 30%!!')
                print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].defense_actuelle,'\n')

    def bouclier_gele(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].defense_actuelle+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)
                equipe_alliee.membres[index].defense_max_donjons+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)
                print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 30%!!')
                print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].defense_actuelle,'\n')

    def bouclier_souffle(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Vent'):
                equipe_alliee.membres[index].defense_actuelle+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)
                equipe_alliee.membres[index].defense_max_donjons+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)
                print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 30%!!')
                print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].defense_actuelle,'\n')

    def bouclier_eclaire(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Lumière'):
                equipe_alliee.membres[index].defense_actuelle+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)
                equipe_alliee.membres[index].defense_max_donjons+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)
                print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 30%!!')
                print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].defense_actuelle,'\n')

    def bouclier_sombre(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].defense_actuelle+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)
                equipe_alliee.membres[index].defense_max_donjons+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)
                print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 30%!!')
                print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].defense_actuelle,'\n')

    def anti_bouclier_enflamme(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Feu'):
                equipe_alliee.membres[index].defense_actuelle-=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)

    def anti_bouclier_gele(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].defense_actuelle-=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)

    def anti_bouclier_souffle(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Vent'):
                equipe_alliee.membres[index].defense_actuelle-=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)

    def anti_bouclier_eclaire(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Lumière'):
                equipe_alliee.membres[index].defense_actuelle-=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)

    def anti_bouclier_sombre(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].defense_actuelle-=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].defense_max_donjons)


class LoupGarou(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Loup Garou',element[indice_element],3,1,2370,2370,99,107,99)

            self.pv_min_3=2370
            self.attaque_min_3=99
            self.defense_min_3=107
            self.pv_min_4=3405
            self.attaque_min_4=143
            self.defense_min_4=154
            self.pv_min_5=4635
            self.attaque_min_5=195
            self.defense_min_5=209
            self.pv_min_6=6300
            self.attaque_min_6=265
            self.defense_min_6=284

            self.pv_max_3=4260
            self.attaque_max_3=179
            self.defense_max_3=192
            self.pv_max_4=5790
            self.attaque_max_4=244
            self.defense_max_4=261
            self.pv_max_5=7875
            self.attaque_max_5=331
            self.defense_max_5=355
            self.pv_max_6=10710
            self.attaque_max_6=450
            self.defense_max_6=483

            self.nb_capacites=2

            self.capacite1=LoupGarou.griffe
            self.capacite1_nom='Griffes impitoyables'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=LoupGarou.attaque_surprise
            self.capacite2_nom='Attaque surprise'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=LoupGarou.soif_de_sang

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Loup Garou',element[indice_element],3,1,2175,2175,121,97,99)

            self.pv_min_3=2175
            self.attaque_min_3=121
            self.defense_min_3=98
            self.pv_min_4=3135
            self.attaque_min_4=175
            self.defense_min_4=140
            self.pv_min_5=4275
            self.attaque_min_5=238
            self.defense_min_5=190
            self.pv_min_6=5805
            self.attaque_min_6=323
            self.defense_min_6=258

            self.pv_max_3=3930
            self.attaque_max_3=218
            self.defense_max_3=175
            self.pv_max_4=5340
            self.attaque_max_4=297
            self.defense_max_4=238
            self.pv_max_5=7260
            self.attaque_max_5=404
            self.defense_max_5=323
            self.pv_max_6=9885
            self.attaque_max_6=549
            self.defense_max_6=439

            self.nb_capacites=3

            self.capacite1=LoupGarou.griffe
            self.capacite1_nom='Griffes impitoyables'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=LoupGarou.aura
            self.capacite2_nom='Aura de Régénération'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=LoupGarou.decoupage
            self.capacite3_nom='Découpage'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=4
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Loup Garou',element[indice_element],3,1,1740,1740,116,131,99)

            self.pv_min_3=1740
            self.attaque_min_3=116
            self.defense_min_3=131
            self.pv_min_4=2520
            self.attaque_min_4=168
            self.defense_min_4=189
            self.pv_min_5=3420
            self.attaque_min_5=228
            self.defense_min_5=257
            self.pv_min_6=4650
            self.attaque_min_6=310
            self.defense_min_6=349

            self.pv_max_3=3135
            self.attaque_max_3=209
            self.defense_max_3=236
            self.pv_max_4=4275
            self.attaque_max_4=285
            self.defense_max_4=321
            self.pv_max_5=5805
            self.attaque_max_5=387
            self.defense_max_5=436
            self.pv_max_6=7905
            self.attaque_max_6=527
            self.defense_max_6=593

            self.nb_capacites=2

            self.capacite1=LoupGarou.griffe
            self.capacite1_nom='Griffes impitoyables'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=LoupGarou.attaque_surprise
            self.capacite2_nom='Attaque surprise'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=LoupGarou.predateur

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Loup Garou',element[indice_element],3,1,2430,2430,97,104,99)

            self.pv_min_3=2430
            self.attaque_min_3=97
            self.defense_min_3=104
            self.pv_min_4=3510
            self.attaque_min_4=140
            self.defense_min_4=150
            self.pv_min_5=4770
            self.attaque_min_5=190
            self.defense_min_5=204
            self.pv_min_6=6495
            self.attaque_min_6=258
            self.defense_min_6=278

            self.pv_max_3=4380
            self.attaque_max_3=175
            self.defense_max_3=188
            self.pv_max_4=5970
            self.attaque_max_4=238
            self.defense_max_4=255
            self.pv_max_5=8115
            self.attaque_max_5=323
            self.defense_max_5=347
            self.pv_max_6=11040
            self.attaque_max_6=439
            self.defense_max_6=472

            self.nb_capacites=3

            self.capacite1=LoupGarou.griffe
            self.capacite1_nom='Griffes impitoyables'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=LoupGarou.aura
            self.capacite2_nom='Aura de Régénération'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite=LoupGarou.massacre
            self.capacite3_nom='Massacre'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Loup Garou',element[indice_element],3,1,2115,2115,112,112,99)

            self.pv_min_3=2115
            self.attaque_min_3=112
            self.defense_min_3=112
            self.pv_min_4=3045
            self.attaque_min_4=161
            self.defense_min_4=161
            self.pv_min_5=4140
            self.attaque_min_5=219
            self.defense_min_5=219
            self.pv_min_6=5625
            self.attaque_min_6=297
            self.defense_min_6=297

            self.pv_max_3=3795
            self.attaque_max_3=201
            self.defense_max_3=201
            self.pv_max_4=5175
            self.attaque_max_4=273
            self.defense_max_4=273
            self.pv_max_5=7020
            self.attaque_max_5=371
            self.defense_max_5=371
            self.pv_max_6=9555
            self.attaque_max_6=505
            self.defense_max_6=505

            self.nb_capacites=2

            self.capacite1=LoupGarou.griffe
            self.capacite1_nom='Griffes impitoyables'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=LoupGarou.attaque_surprise
            self.capacite2_nom='Attaque Surprise'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=LoupGarou.retour_de_coup

    def griffe(self,cible):
        print('\n',self.surnom,self.attribut,' griffe impitoyablement ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.7,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.7,self.capacite1_bonus_skill,degats,cible)
        degats+=50
        if(self.attribut=='Vent' and self.sans_passif<=0):
            degats+=LoupGarou.predateur(self,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.perturbation_recuperation(1)
        if(self.attribut=='Ténèbres'):
            cible.def_break(1)

    def attaque_surprise(self,cible):
        print('\n',self.surnom,self.attribut,' lacère rapidement ',cible.surnom,cible.attribut,' à deux reprises!!\n')
        for index in range(2):
            degats=Arrondir.a_l_unite(0.16*self.pv_max_donjons)
            if(self.attribut=='Vent' and self.sans_passif<=0):
                degats+=LoupGarou.predateur(self,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.3,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                    cible.stun=1
            if(self.attribut=='Ténèbres'):
                self.ef_break(cible,1)

    def aura(equipe_alliee):
        print('\nLe pouvoir de l\'Aura décuple la régénénération de l\'équipe!!\n')
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels>0 and equipe_alliee.membres[index].perturbation_recup<=0):
                montant=Arrondir.a_l_unite(0.15*equipe_alliee.membres[index].pv_max_donjons)
                equipe_alliee.membres[index].etre_soigne(montant)
            self.speed_up(equipe_alliee.membres[index],2)

    def decoupage(self,cible):
        print('\n',self.surnom,self.attribut,' découpe ',cible.surnom,cible.attribut,' en morceaux!!\n')
        for index in range(3):
            degats=self.calcul_dommages(1.4,self.capacite3_bonus_skill,cible)
            self.affichage_du_type_de_coup(1.4,self.capacite3_bonus_skill,degats,cible)
            degats+=Arrondir.a_l_unite(0.1*self.pv_max_donjons)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.35,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    cible.def_break(3)
            if(self.attribut=='Ténèbres'):
                cible.def_break(1)

    def massacre(self,cible):
        print('\n',self.surnom,self.attribut,' se lance dans un véritable massacre!!\n')
        for index in range(4):
            degats=Arrondir.a_l_unite(0.12*self.pv_max_donjons)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.35,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    cible.retirer_un_bonus()
            if(self.attribut=='Ténèbres'):
                cible.def_break(1)
            if(cible.pv_actuels<=0):
                self.attente2=1

    def soif_de_sang(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='LoupGarou' and equipe_alliee.membres[index].attribut=='Feu'):
                print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit doubler le montant qu\'il recevra par les sorts de soin!!\n')

    def predateur(self,cible):
        bonus_de_dommages=0
        pourcentage_pv_actuels_cible=cible.pv_actuels/cible.pv_max_donjons
        pourcentage_pv_actuels_loup=self.pv_actuels/self.pv_max_donjons
        if(pourcentage_pv_actuels_loup>pourcentage_pv_actuels_cible):
            bonus_de_dommages=Arrondir.a_l_unite(0.15*self.pv_max_donjons)
        return bonus_de_dommages

    def retour_de_coup(self,cible):
        print('\n',self.surnom,self.attribut,' se venge!!\n')
        if(cible.pv_actuels>0):
            degats=Arrondir.a_l_unite(0.12*self.pv_max_donjons)
            degats=self.reduction_dommages(degats)
            if(cible.immortalite<=0):
                cible.recoit_degats(degats)
                print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
            else:
                print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
            if (cible.pv_actuels<=0):
                print(cible.surnom,cible.attribut,' est mort!! \n')
            else:
                print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')





class Elfe(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Elfe',element[indice_element],3,1,1860,1860,124,116,100)

            self.pv_min_3=1860
            self.attaque_min_3=124
            self.defense_min_3=116
            self.pv_min_4=2670
            self.attaque_min_4=178
            self.defense_min_4=168
            self.pv_min_5=3630
            self.attaque_min_5=242
            self.defense_min_5=228
            self.pv_min_6=4935
            self.attaque_min_6=329
            self.defense_min_6=310

            self.pv_max_3=3345
            self.attaque_max_3=223
            self.defense_max_3=209
            self.pv_max_4=4545
            self.attaque_max_4=303
            self.defense_max_4=285
            self.pv_max_5=6180
            self.attaque_max_5=412
            self.defense_max_5=387
            self.pv_max_6=8400
            self.attaque_max_6=560
            self.defense_max_6=527

            self.nb_capacites=3

            self.capacite1=Elfe.salvation
            self.capacite1_nom='Salvation'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Elfe.fleches
            self.capacite2_nom='Flèches Célestes'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Elfe.strategie
            self.capacite3_nom='Stratégie'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=6
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Elfe',element[indice_element],3,1,1710,1710,136,114,100)

            self.pv_min_3=1710
            self.attaque_min_3=136
            self.defense_min_3=114
            self.pv_min_4=2460
            self.attaque_min_4=196
            self.defense_min_4=164
            self.pv_min_5=3345
            self.attaque_min_5=266
            self.defense_min_5=223
            self.pv_min_6=4560
            self.attaque_min_6=362
            self.defense_min_6=304

            self.pv_max_3=3075
            self.attaque_max_3=244
            self.defense_max_3=205
            self.pv_max_4=4185
            self.attaque_max_4=333
            self.defense_max_4=279
            self.pv_max_5=5685
            self.attaque_max_5=452
            self.defense_max_5=379
            self.pv_max_6=7740
            self.attaque_max_6=615
            self.defense_max_6=516

            self.nb_capacites=3

            self.capacite1=Elfe.salvation
            self.capacite1_nom='Salvation'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Elfe.tir
            self.capacite2_nom='Tir Sniperial'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Elfe.pluie
            self.capacite3_nom='Pluie de Douleur'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=6
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Elfe',element[indice_element],3,1,1785,1785,131,114,100)

            self.pv_min_3=1785
            self.attaque_min_3=131
            self.defense_min_3=114
            self.pv_min_4=2565
            self.attaque_min_4=189
            self.defense_min_4=164
            self.pv_min_5=3495
            self.attaque_min_5=257
            self.defense_min_5=223
            self.pv_min_6=4740
            self.attaque_min_6=349
            self.defense_min_6=304

            self.pv_max_3=3210
            self.attaque_max_3=236
            self.defense_max_3=205
            self.pv_max_4=4365
            self.attaque_max_4=321
            self.defense_max_4=279
            self.pv_max_5=5940
            self.attaque_max_5=436
            self.defense_max_5=379
            self.pv_max_6=8070
            self.attaque_max_6=593
            self.defense_max_6=516

            self.nb_capacites=2

            self.capacite1=Elfe.salvation
            self.capacite1_nom='Salvation'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Elfe.fleches
            self.capacite2_nom='Flèches Célestes'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Elfe.mouvement_esquive
            self.passif_active=0

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Elfe',element[indice_element],3,1,1785,1785,138,107,100)

            self.pv_min_3=1785
            self.attaque_min_3=138
            self.defense_min_3=107
            self.pv_min_4=2565
            self.attaque_min_4=199
            self.defense_min_4=154
            self.pv_min_5=3495
            self.attaque_min_5=271
            self.defense_min_5=209
            self.pv_min_6=4740
            self.attaque_min_6=368
            self.defense_min_6=284

            self.pv_max_3=3210
            self.attaque_max_3=249
            self.defense_max_3=192
            self.pv_max_4=4365
            self.attaque_max_4=339
            self.defense_max_4=261
            self.pv_max_5=5940
            self.attaque_max_5=460
            self.defense_max_5=355
            self.pv_max_6=8070
            self.attaque_max_6=626
            self.defense_max_6=483

            self.nb_capacites=3

            self.capacite1=Elfe.salvation
            self.capacite1_nom='Salvation'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Elfe.tir
            self.capacite2_nom='Tir Sniperial'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Elfe.fleche_divine
            self.capacite3_nom='Flèche Divine'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Elfe',element[indice_element],4,1,2625,2625,220,182,100)

            self.pv_min_4=2625
            self.attaque_min_4=220
            self.defense_min_4=182
            self.pv_min_5=3570
            self.attaque_min_5=299
            self.defense_min_5=247
            self.pv_min_6=4845
            self.attaque_min_6=407
            self.defense_min_6=336

            self.pv_max_4=4455
            self.attaque_max_4=374
            self.defense_max_4=309
            self.pv_max_5=6060
            self.attaque_max_5=509
            self.defense_max_5=420
            self.pv_max_6=8235
            self.attaque_max_6=692
            self.defense_max_6=571

            self.nb_capacites=2

            self.capacite1=Elfe.salvation
            self.capacite1_nom='Salvation'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Elfe.fleches
            self.capacite2_nom='Flèches Célestes'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Elfe.contre_attaque

    def salvation(self,cible):
        nb_coups=2
        chance_troisieme_coup=self.taux_coup_critique_actuel
        aleatoire=random.randint(1,100)/100
        if(aleatoire<=chance_troisieme_coup):
            nb_coups+=1
        print('\n',self.surnom,self.attribut,' tire une salve de flèches sur ',cible.surnom,cible.attribut,'!!\n')
        for index in range(nb_coups):
            degats=self.calcul_dommages(1.6*nb_coups,self.capacite1_bonus_skill,cible)
            self.affichage_du_type_de_coup(1.6*nb_coups,self.capacite1_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)

    def fleches(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' attaque toute l\'équipe ennemie avec une pluie de flèches célestes aléatoires!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive()):
                indice_cible=random.randint(0,equipe_ennemie.len-1)
                while(equipe_ennemie.membres[indice_cible].pv_actuels<=0):
                    indice_cible=random.randint(0,equipe_ennemie.len-1)
                cible=equipe_ennemie.membres[indice_cible]
                degats=self.calcul_dommages(2,self.capacite2_bonus_skill,cible)
                self.affichage_du_type_de_coup(2,self.capacite2_bonus_skill,degats,cible)
                degats=cible.reduction_dommages(degats)
                self.procedure_attaque(degats,cible)
                if(cible.immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(0.75,cible.resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        cible.degats_continus(1,1)

    def pluie(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' attaque toute l\'équipe ennemie avec une pluie de flèches!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive()):
                degats=self.calcul_dommages(4.8,self.capacite3_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(4.8,self.capacite3_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].stun==0 and equipe_ennemie.membres[index].gel==0 and equipe_ennemie.membres[index].sommeil==0):
                    print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' voit sa jauge d\'attaque diminuer de moitié!! \n')
                    equipe_ennemie.membres[index].jauge_attaque-=max(50,Arrondir.a_l_unite(0.5*equipe_ennemie.membres[index].jauge_attaque))
                else:
                    print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' voit sa jauge d\'attaque réduite à zéro!! \n')
                    equipe_ennemie.membres[index].jauge_attaque=0

    def tir(self,cible):
        print('\n',self.surnom,self.attribut,' tire une flèche avec une précision extrême sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(5.2,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(5.2,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!!')
                cible.stun=1
                print(self.surnom,self.attribut,' regagne instantanément un tour supplémentaire!!\n')
                self.tour_supplementaire_tmp+=1

    def fleche_divine(self,cible):
        print('\n',self.surnom,self.attribut,' tire une divine flèche de lumière sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(7.8,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(7.8,self.capacite2_bonus_skill,degats,cible)
        if(cible.stun==1 or cible.gel==1 or cible.sommeil==1):
            degats=Arrondir.a_l_unite(1.5*degats)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)

    def strategie(equipe_alliee):
        print('\nL\'équipe échafaude un plan machiavélique en s\'inspirant du FûRinKaZan...\n')
        for index in range(equipe_alliee.len):
            self.speed_up(equipe_alliee.membres[index],3)
            equipe_alliee.membres[index].espada(3)

    def mouvement_esquive(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Elfe' and equipe_alliee.membres[index].attribut=='Vent'):
                if(equipe_alliee.membres[index].passif_active!=1):
                    print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit sa réduction de dégâts augmenter!!\n')
                    equipe_alliee.membres[index].reduction_de_degats+=0.5
                    equipe_alliee.membres[index].passif_active=1
                    self.speed_up(equipe_alliee.membres[index],1)

    def fin_mouvement_esquive(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Elfe' and equipe_alliee.membres[index].attribut=='Vent'):
                if(equipe_alliee.membres[index].passif_active==1):
                    equipe_alliee.membres[index].reduction_de_degats-=0.5
                    print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit sa réduction de dégâts diminuer!!\n')
                    equipe_alliee.membres[index].passif_active=0

    def contre_attaque(self,cible):
        print('\n',self.surnom,self.attribut,' venge son allié(e)!!\n')
        if(cible.pv_actuels>0):
            for index in range(3):
                degats=Arrondir.a_l_unite(0.65*self.attaque_actuelle)
                degats=cible.reduction_dommages(degats)
                if(cible.immortalite<=0):
                    cible.recoit_degats(degats)
                    print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
                else:
                    print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                if (cible.pv_actuels<=0):
                    print(cible.surnom,cible.attribut,' est mort!! \n')
                else:
                    print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')



class Sylphe(Monstre): # Arashi
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Sylphe',element[indice_element],4,1,3240,3240,199,161,104)

            self.pv_min_4=3240
            self.attaque_min_4=199
            self.defense_min_4=161
            self.pv_min_5=4425
            self.attaque_min_5=271
            self.defense_min_5=219
            self.pv_min_6=6000
            self.attaque_min_6=368
            self.defense_min_6=297

            self.pv_max_4=5520
            self.attaque_max_4=339
            self.defense_max_4=273
            self.pv_max_5=7500
            self.attaque_max_5=460
            self.defense_max_5=371
            self.pv_max_6=10215
            self.attaque_max_6=626
            self.defense_max_6=505

            self.nb_capacites=3

            self.capacite1=Sylphe.esprit
            self.capacite1_nom='Esprit Elémentaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Sylphe.turbulences
            self.capacite2_nom='Turbulences'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Sylphe.phenix
            self.capacite3_nom='Phénix Incandescent'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphe.vitesse
            self.anti_leader_skill=Sylphe.anti_vitesse

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Sylphe',element[indice_element],4,1,3135,3135,209,157,104)

            self.pv_min_4=3135
            self.attaque_min_4=209
            self.defense_min_4=157
            self.pv_min_5=4275
            self.attaque_min_5=285
            self.defense_min_5=214
            self.pv_min_6=5805
            self.attaque_min_6=387
            self.defense_min_6=291

            self.pv_max_4=5340
            self.attaque_max_4=356
            self.defense_max_4=267
            self.pv_max_5=7260
            self.attaque_max_5=484
            self.defense_max_5=363
            self.pv_max_6=9885
            self.attaque_max_6=659
            self.defense_max_6=494

            self.nb_capacites=3

            self.capacite1=Sylphe.esprit
            self.capacite1_nom='Esprit Elémentaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Sylphe.tourbillon
            self.capacite2_nom='Tourbillon Elémentaire'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Sylphe.blizzard
            self.capacite3_nom='Blizzard'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphe.vitesse
            self.anti_leader_skill=Sylphe.anti_vitesse

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Sylphe',element[indice_element],4,1,2985,2985,241,136,105)

            self.pv_min_4=2985
            self.attaque_min_4=241
            self.defense_min_4=136
            self.pv_min_5=4065
            self.attaque_min_5=328
            self.defense_min_5=185
            self.pv_min_6=5520
            self.attaque_min_6=446
            self.defense_min_6=252

            self.pv_max_4=5085
            self.attaque_max_4=410
            self.defense_max_4=232
            self.pv_max_5=6900
            self.attaque_max_5=557
            self.defense_max_5=315
            self.pv_max_6=9390
            self.attaque_max_6=758
            self.defense_max_6=428

            self.nb_capacites=3

            self.capacite1=Sylphe.esprit
            self.capacite1_nom='Esprit Elémentaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Sylphe.tourbillon
            self.capacite2_nom='Tourbillon Elémentaire'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Sylphe.ouragan
            self.capacite3_nom='Ouragan'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphe.vitesse_arena
            self.anti_leader_skill=Sylphe.anti_vitesse_arena

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Sylphe',element[indice_element],4,1,3240,3240,209,150,104)

            self.pv_min_4=3240
            self.attaque_min_4=209
            self.defense_min_4=150
            self.pv_min_5=4425
            self.attaque_min_5=285
            self.defense_min_5=204
            self.pv_min_6=6000
            self.attaque_min_6=387
            self.defense_min_6=278

            self.pv_max_4=5520
            self.attaque_max_4=356
            self.defense_max_4=255
            self.pv_max_5=7500
            self.attaque_max_5=484
            self.defense_max_5=347
            self.pv_max_6=10215
            self.attaque_max_6=659
            self.defense_max_6=472

            self.nb_capacites=3

            self.capacite1=Sylphe.esprit
            self.capacite1_nom='Esprit Elémentaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Sylphe.tourbillon
            self.capacite2_nom='Tourbillon Elémentaire'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Sylphe.cyclone
            self.capacite3_nom='Cyclone'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphe.vitesse_donjons
            self.anti_leader_skill=Sylphe.anti_vitesse_donjons

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Sylphe',element[indice_element],4,1,3345,3345,192,161,104)

            self.pv_min_4=3345
            self.attaque_min_4=192
            self.defense_min_4=161
            self.pv_min_5=4560
            self.attaque_min_5=261
            self.defense_min_5=219
            self.pv_min_6=6195
            self.attaque_min_6=355
            self.defense_min_6=297

            self.pv_max_4=5700
            self.attaque_max_4=327
            self.defense_max_4=273
            self.pv_max_5=7755
            self.attaque_max_5=444
            self.defense_max_5=371
            self.pv_max_6=10545
            self.attaque_max_6=604
            self.defense_max_6=505

            self.nb_capacites=3

            self.capacite1=Sylphe.esprit
            self.capacite1_nom='Esprit Elémentaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Sylphe.turbulences
            self.capacite2_nom='Turbulences'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Sylphe.nuit
            self.capacite3_nom='Tombée de la Nuit'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=7
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphe.vitesse_donjons
            self.anti_leader_skill=Sylphe.anti_vitesse_donjons

    def esprit(self,cible):
        print('\n',self.surnom,self.attribut,' projette un esprit élémentaire sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(3.8,self.capacite1_bonus_skill,cible)
        type_coup=self.affichage_du_type_de_coup(3.8,self.capacite1_bonus_skill,degats,cible)
        degats-=20
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(type_coup=='Critique'):
            self.espada(1)

    def turbulences(self,cible):
        print('\n',self.surnom,self.attribut,' cause de violentes turbulences autour de ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(6,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(6,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        print(cible.surnom,cible.attribut,'voit sa jauge d\'attaque réduite à zéro!!\n')
        cible.jauge_attaque=0

    def ouragan(self,cible):
        print('\n',self.surnom,self.attribut,' engloutit ',cible.surnom,cible.attribut,' dans un ouragan dévastateur!!\n')
        degats=self.calcul_dommages(8.4,self.capacite3_bonus_skill,cible)
        self.affichage_du_type_de_coup(8.4,self.capacite3_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        print('\n',self.surnom,self.attribut,' voit sa vitesse d\'attaque augmenter pour trois tours d\'un montant égal à la vitesse d\'attaque de ',cible.surnom,cible.attribut,'!!')
        self.vitesse_actuelle+=cible.vitesse_max_donjons
        self.tours_bonus_vitesse=max(3,self.tours_bonus_vitesse)
        print('La vitesse actuelle de ',self.surnom,self.attribut,' est désormais de ',self.vitesse_actuelle,'!!\n')

    def tourbillon(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' balaye deux fois l\'équipe ennemie avec un tourbillon élémentaire!!\n')
        for index in range(2):
            for index_bis in range(equipe_ennemie.len):
                if(equipe_ennemie.is_alive() and equipe_ennemie.membres[index_bis].pv_actuels>0):
                    degats=self.calcul_dommages(1.3,self.capacite2_bonus_skill,equipe_ennemie.membres[index_bis])
                    self.affichage_du_type_de_coup(1.3,self.capacite2_bonus_skill,degats,equipe_ennemie.membres[index_bis])
                    degats+=Arrondir.a_l_unite(0.04*equipe_ennemie.membres[index_bis].pv_max_donjons)
                    degats=equipe_ennemie.membres[index_bis].reduction_dommages(degats)
                    self.procedure_attaque(degats,equipe_ennemie.membres[index_bis])
                    if(equipe_ennemie.membres[index_bis].immunite==0):
                        effet_nefaste=random.randint(1,100)
                        limite_reussite=Calcul.taux_reussite_effet(0.4,equipe_ennemie.membres[index_bis].resistance_actuelle,self.precision_actuelle)
                        if(effet_nefaste<=100*limite_reussite):
                            equipe_ennemie.membres[index_bis].bonus_coup_superficiel(2)
            print('\n\n')

    def nuit(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' enveloppe toute l\'équipe ennemie dans une brume noire mystérieuse... La nuit tombe!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive() and equipe_ennemie.membres[index].pv_actuels>0):
                equipe_ennemie.membres[index].sommeil(2)

    def cyclone(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' balaye quatre fois l\'équipe ennemie avec un puissant cyclone!!\n')
        for index in range(4):
            for index_bis in range(equipe_ennemie.len):
                if(equipe_ennemie.is_alive() and equipe_ennemie.membres[index_bis].pv_actuels>0):
                    degats=self.calcul_dommages(1.1,self.capacite3_bonus_skill,equipe_ennemie.membres[index_bis])
                    self.affichage_du_type_de_coup(1.1,self.capacite3_bonus_skill,degats,equipe_ennemie.membres[index_bis])
                    degats=equipe_ennemie.membres[index_bis].reduction_dommages(degats)
                    self.procedure_attaque(degats,equipe_ennemie.membres[index_bis])
                    if(equipe_ennemie.membres[index_bis].immunite==0):
                        effet_nefaste=random.randint(1,100)
                        limite_reussite=Calcul.taux_reussite_effet(0.2,equipe_ennemie.membres[index_bis].resistance_actuelle,self.precision_actuelle)
                        if(effet_nefaste<=100*limite_reussite):
                            print(equipe_ennemie.membres[index_bis].surnom,equipe_ennemie.membres[index_bis].attribut,' est étourdi(e)!!')
                            print(self.surnom,self.attribut,' voit sa jauge d\'attaque augmenter d\'un cinquième de la jauge de ',equipe_ennemie.membres[index_bis].surnom,equipe_ennemie.membres[index_bis].attribut,'!!\n')
                            equipe_ennemie.membres[index_bis].stun=1
                            self.jauge_attaque+=Arrondir.a_l_unite(0.2*equipe_ennemie.membres[index_bis].jauge_attaque)
            print('\n\n')

    def blizzard(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' engloutit toute l\'équipe ennemie dans un puissant blizzard!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive() and equipe_ennemie.membres[index].pv_actuels>0):
                degats=self.calcul_dommages(3,self.capacite3_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(3,self.capacite3_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(1,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' est gelé(e)!!')
                        equipe_ennemie.membres[index].gel=1
                        self.slow_down(equipe_ennemie.membres[index],2)

    def phenix(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' invoque un Phénix incandescent!! Celui-ci engloutit toute l\'équipe ennemie dans une tempête de flammes!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive() and equipe_ennemie.membres[index].pv_actuels>0):
                degats=self.calcul_dommages(4,self.capacite3_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(4,self.capacite3_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(1,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        equipe_ennemie.membres[index].degats_continus(1,3)

    def vitesse(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].vitesse_actuelle+=Arrondir.a_l_unite(0.19*equipe_alliee.membres[index].vitesse_max_donjons)
            equipe_alliee.membres[index].vitesse_max_donjons+=Arrondir.a_l_unite(0.19*equipe_alliee.membres[index].vitesse_max_donjons)
            print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 19%!!')
            print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].vitesse_actuelle,'\n')

    def vitesse_arena(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].vitesse_actuelle+=Arrondir.a_l_unite(0.24*equipe_alliee.membres[index].vitesse_max_donjons)
            equipe_alliee.membres[index].vitesse_max_donjons+=Arrondir.a_l_unite(0.24*equipe_alliee.membres[index].vitesse_max_donjons)
            print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 24%!!')
            print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].vitesse_actuelle,'\n')

    def vitesse_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].vitesse_actuelle+=Arrondir.a_l_unite(0.24*equipe_alliee.membres[index].vitesse_max_donjons)
            equipe_alliee.membres[index].vitesse_max_donjons+=Arrondir.a_l_unite(0.24*equipe_alliee.membres[index].vitesse_max_donjons)
            print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 24%!!')
            print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].vitesse_actuelle,'\n')

    def anti_vitesse(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].vitesse_actuelle-=Arrondir.a_l_unite(0.19*equipe_alliee.membres[index].vitesse_max_donjons)

    def anti_vitesse_arena(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].vitesse_actuelle-=Arrondir.a_l_unite(0.24*equipe_alliee.membres[index].vitesse_max_donjons)

    def anti_vitesse_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].vitesse_actuelle-=Arrondir.a_l_unite(0.24*equipe_alliee.membres[index].vitesse_max_donjons)



class Sylphide(Monstre): # Hayate
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Sylphide',element[indice_element],4,1,2670,2670,223,175,102)

            self.pv_min_4=2670
            self.attaque_min_4=223
            self.defense_min_4=175
            self.pv_min_5=3630
            self.attaque_min_5=304
            self.defense_min_5=238
            self.pv_min_6=4935
            self.attaque_min_6=413
            self.defense_min_6=323

            self.pv_max_4=4545
            self.attaque_max_4=380
            self.defense_max_4=297
            self.pv_max_5=6180
            self.attaque_max_5=517
            self.defense_max_5=404
            self.pv_max_6=8400
            self.attaque_max_6=703
            self.defense_max_6=549

            self.nb_capacites=3

            self.capacite1=Sylphide.lame
            self.capacite1_nom='Lame Elémentaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Sylphide.bourrasque
            self.capacite2_nom='Bourrasque Spirituelle'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Sylphide.conjuration
            self.capacite3_nom='Conjuration'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=10
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphide.resistance_feu
            self.anti_leader_skill=Sylphide.anti_resistance_feu

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Sylphide',element[indice_element],4,1,3720,3720,133,196,102)

            self.pv_min_4=3720
            self.attaque_min_4=133
            self.defense_min_4=196
            self.pv_min_5=5055
            self.attaque_min_5=181
            self.defense_min_5=266
            self.pv_min_6=6885
            self.attaque_min_6=245
            self.defense_min_6=362

            self.pv_max_4=6330
            self.attaque_max_4=226
            self.defense_max_4=333
            self.pv_max_5=8595
            self.attaque_max_5=307
            self.defense_max_5=452
            self.pv_max_6=11700
            self.attaque_max_6=417
            self.defense_max_6=615

            self.nb_capacites=3

            self.capacite1=Sylphide.lame
            self.capacite1_nom='Lame Elémentaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Sylphide.ouragan
            self.capacite2_nom='Ouragan'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Sylphide.benediction
            self.capacite3_nom='Bénédiction de la déesse de l\'eau'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=4
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphide.resistance_eau
            self.anti_leader_skill=Sylphide.anti_resistance_eau

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Sylphide',element[indice_element],4,1,3195,3195,175,189,103)

            self.pv_min_4=3195
            self.attaque_min_4=175
            self.defense_min_4=189
            self.pv_min_5=4350
            self.attaque_min_5=238
            self.defense_min_5=257
            self.pv_min_6=5910
            self.attaque_min_6=323
            self.defense_min_6=349

            self.pv_max_4=5430
            self.attaque_max_4=297
            self.defense_max_4=321
            self.pv_max_5=7380
            self.attaque_max_5=404
            self.defense_max_5=436
            self.pv_max_6=10050
            self.attaque_max_6=549
            self.defense_max_6=593

            self.nb_capacites=3

            self.capacite1=Sylphide.lame
            self.capacite1_nom='Lame Elémentaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Sylphide.bourrasque2
            self.capacite2_nom='Bourrasque Spirituelle'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Sylphide.bouclier
            self.capacite3_nom='Bouclier Spirituel'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphide.resistance_vent
            self.anti_leader_skill=Sylphide.anti_resistance_vent

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Sylphide',element[indice_element],4,1,3510,3510,171,171,102)

            self.pv_min_4=3510
            self.attaque_min_4=171
            self.defense_min_4=171
            self.pv_min_5=4770
            self.attaque_min_5=233
            self.defense_min_5=233
            self.pv_min_6=6495
            self.attaque_min_6=316
            self.defense_min_6=316

            self.pv_max_4=5970
            self.attaque_max_4=291
            self.defense_max_4=291
            self.pv_max_5=8115
            self.attaque_max_5=396
            self.defense_max_5=396
            self.pv_max_6=11040
            self.attaque_max_6=538
            self.defense_max_6=538

            self.nb_capacites=3

            self.capacite1=Sylphide.lame
            self.capacite1_nom='Lame Elémentaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Sylphide.ouragan
            self.capacite2_nom='Ouragan'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Sylphide.benediction_lumiere
            self.capacite3_nom='Bénédiction de Lumière'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=4
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphide.resistance_lumiere
            self.anti_leader_skill=Sylphide.anti_resistance_lumiere

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Sylphide',element[indice_element],4,1,2880,2880,230,154,102)

            self.pv_min_4=2880
            self.attaque_min_4=230
            self.defense_min_4=154
            self.pv_min_5=3915
            self.attaque_min_5=314
            self.defense_min_5=209
            self.pv_min_6=5325
            self.attaque_min_6=426
            self.defense_min_6=284

            self.pv_max_4=4905
            self.attaque_max_4=392
            self.defense_max_4=261
            self.pv_max_5=6660
            self.attaque_max_5=533
            self.defense_max_5=355
            self.pv_max_6=9060
            self.attaque_max_6=725
            self.defense_max_6=483

            self.nb_capacites=3

            self.capacite1=Sylphide.lame
            self.capacite1_nom='Lame Elémentaire'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Sylphide.bourrasque2
            self.capacite2_nom='Bourrasque Spirituelle'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Sylphide.aspiration
            self.capacite3_nom='Aspiration des Ténèbres'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=6
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphide.resistance_tenebres
            self.anti_leader_skill=Sylphide.anti_resistance_tenebres

    def lame(self,cible):
        print('\n',self.surnom,self.attribut,' perce ',cible.surnom,cible.attribut,' avec une lame élémentaire!!\n')
        degats=self.calcul_dommages(3.7,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(3.7,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.3,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.degats_continus(1,3)

    def ouragan(self,cible):
        print('\n',self.surnom,self.attribut,' engloutit ',cible.surnom,cible.attribut,' dans un ouragan dévastateur!!\n')
        degats=self.calcul_dommages(5,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(5,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        print('\nToutes les capacités de ',cible.surnom,cible.attribut,' doivent désormais être rechargées au maximum!!\n')
        if(cible.nb_capacites>=2):
            cible.attente2=cible.temps_recharge2
            cible.etat_cap2='Non dispo'
        if(cible.nb_capacites>=3):
            cible.attente3=cible.temps_recharge3
            cible.etat_cap3='Non dispo'
        if(cible.nb_capacites>=4):
            cible.attente4=cible.temps_recharge4
            cible.etat_cap4='Non dispo'

    def bourrasque(self,equipe_ennemie,equipe_alliee):
        print('\n',self.surnom,self.attribut,' balaye toute l\'équipe ennemie avec une bourrasque spirituelle!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive() and equipe_ennemie.membres[index].pv_actuels>0):
                degats=self.calcul_dommages(2.6,self.capacite2_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(2.6,self.capacite2_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=self.reduction_dommages(degats,equipe_ennemie.membres[index])
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
        print('\n')
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels>0):
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit sa jauge d\'attaque augmenter d\'un cinquième!!')
                equipe_alliee.membres[index].jauge_attaque+=max(20,Arrondir.a_l_unite(0.2*equipe_alliee.membres[index].jauge_attaque))

    def bourrasque2(self,equipe_ennemie,equipe_alliee):
        print('\n',self.surnom,self.attribut,' balaye toute l\'équipe ennemie avec une bourrasque spirituelle!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive() and equipe_ennemie.membres[index].pv_actuels>0):
                degats=self.calcul_dommages(2.6,self.capacite2_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(2.6,self.capacite2_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
        print('\n')
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels>0):
                if(equipe_alliee.membres[index].perturbation_recup<=0):
                    montant=Arrondir.a_l_unite(0.2*equipe_alliee.membres[index].pv_max_donjons)
                    equipe_alliee.membres[index].etre_soigne(montant)
                else:
                    print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.attribut[index],' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces... \n')
            else:
                print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est mort(e)!!\n')

    def conjuration(equipe_alliee):
        print('\nSylphide Feu sacrifie sa vie pour soigner toute son équipe!!\n')
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom!='Sylphide' or equipe_alliee.membres[index].attribut!='Feu'):
                if(equipe_alliee.membres[index].pv_actuels>0):
                    equipe_alliee.membres[index].soigner_de_tous_les_maux()
                    print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,'est débarrassé de tous les effets négatifs qui l affectaient!!')
                    montant=equipe_alliee.membres[index].pv_max_donjons
                    equipe_alliee.membres[index].etre_soigne(montant)
                    print('Il reste ',equipe_alliee.membres[index].pv_actuels,' point(s) de vie sur',equipe_alliee.membres[index].pv_max_donjons,' à ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,'!! \n')
                else:
                    print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est mort(e)!!\n')
            else:
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' se vide de sa vie... \n')
                equipe_alliee.membres[index].pv_actuels=0

    def bouclier(equipe_alliee):
        print('\nSylphide Vent protège toute l\'équipe d\'un bouclier d\'énergie spirituelle!!\n')
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Sylphide' and equipe_alliee.membres[index].attribut=='Vent'):
                montant=equipe_alliee.membres[index].niveau*100
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels>0):
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' reçoit un bouclier d\'un montant égal à ',montant,'!!')
                equipe_alliee.membres[index].pv_actuels+=montant
            else:
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est mort(e)!!\n')

    def benediction(self,allie):
        if(allie.perturbation_recup<=0):
            print('\n',self.surnom,self.attribut,' régénère les points de vie de ',allie.surnom,allie.attribut,' à leur maximum!!\n')
            allie.pv_actuels=allie.pv_max_donjons
        else:
            print('\n',allie.surnom,allie.attribut,' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces... \n')

    def benediction_lumiere(equipe_alliee):
        print('\nToute l\'équipe reçoit la bénédiction de la déesse de la lumière!!\n')
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels>0):
                if(equipe_alliee.membres[index].perturbation_recup<=0):
                    montant=Arrondir.a_l_unite(0.2*equipe_alliee.membres[index].pv_max_donjons)
                    equipe_alliee.membres[index].etre_soigne(montant)
                else:
                    print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces... \n')
                self.tanky(equipe_alliee.membres[index],2)
            else:
                print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est mort(e)!!\n')

    def aspiration(self,cible):
        self.vol_de_vie+=100
        print('\n',self.surnom,self.attribut,' aspire la vie de ',cible.surnom,cible.attribut,' en ignorant sa défense!!\n')
        degats=0.5*self.pv_max_donjons
        self.procedure_attaque(degats,cible)
        self.vol_de_vie-=100


    def resistance_feu(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Feu'):
                equipe_alliee.membres[index].resistance_actuelle+=0.5
                equipe_alliee.membres[index].resistance_max_donjons+=0.5
                print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 50%!!')
                print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].resistance_actuelle,'\n')

    def resistance_eau(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].resistance_actuelle+=0.5
                equipe_alliee.membres[index].resistance_max_donjons+=0.5
                print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 50%!!')
                print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].resistance_actuelle,'\n')

    def resistance_vent(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Vent'):
                equipe_alliee.membres[index].resistance_actuelle+=0.5
                equipe_alliee.membres[index].resistance_max_donjons+=0.5
                print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 50%!!')
                print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].resistance_actuelle,'\n')

    def resistance_lumiere(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Lumière'):
                equipe_alliee.membres[index].resistance_actuelle+=0.5
                equipe_alliee.membres[index].resistance_max_donjons+=0.5
                print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 50%!!')
                print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].resistance_actuelle,'\n')

    def resistance_tenebres(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].resistance_actuelle+=0.5
                equipe_alliee.membres[index].resistance_max_donjons+=0.5
                print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 50%!!')
                print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].resistance_actuelle,'\n')

    def anti_resistance_feu(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Feu'):
                equipe_alliee.membres[index].resistance_actuelle-=0.5

    def anti_resistance_eau(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Eau'):
                equipe_alliee.membres[index].resistance_actuelle-=0.5

    def anti_resistance_vent(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Vent'):
                equipe_alliee.membres[index].resistance_actuelle-=0.5

    def anti_resistance_lumiere(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Lumière'):
                equipe_alliee.membres[index].resistance_actuelle-=0.5

    def anti_resistance_tenebres(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].attribut=='Ténèbres'):
                equipe_alliee.membres[index].resistance_actuelle-=0.5




class ChevalierMagique(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Chevalier Magique',element[indice_element],4,1,2730,2730,230,164,89)

            self.pv_min_4=2730
            self.attaque_min_4=230
            self.defense_min_4=164
            self.pv_min_5=3705
            self.attaque_min_5=314
            self.defense_min_5=223
            self.pv_min_6=5040
            self.attaque_min_6=426
            self.defense_min_6=304

            self.pv_max_4=4635
            self.attaque_max_4=392
            self.defense_max_4=279
            self.pv_max_5=6300
            self.attaque_max_5=533
            self.defense_max_5=379
            self.pv_max_6=8565
            self.attaque_max_6=725
            self.defense_max_6=516

            self.nb_capacites=2

            self.capacite1=ChevalierMagique.combo
            self.capacite1_nom='Combo de Trois Coups'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=ChevalierMagique.balles
            self.capacite2_nom='Balles Magiques'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=ChevalierMagique.feu_vengeur

            self.presence_leader_skill=1
            self.leader_skill=ChevalierMagique.aura_feu
            self.anti_leader_skill=ChevalierMagique.anti_aura_feu

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Chevalier Magique',element[indice_element],4,1,2985,2985,209,168,89)

            self.pv_min_4=2985
            self.attaque_min_4=209
            self.defense_min_4=168
            self.pv_min_5=4065
            self.attaque_min_5=285
            self.defense_min_5=228
            self.pv_min_6=5520
            self.attaque_min_6=387
            self.defense_min_6=310

            self.pv_max_4=5085
            self.attaque_max_4=356
            self.defense_max_4=285
            self.pv_max_5=6900
            self.attaque_max_5=484
            self.defense_max_5=387
            self.pv_max_6=9390
            self.attaque_max_6=659
            self.defense_max_6=527

            self.nb_capacites=3

            self.capacite1=ChevalierMagique.combo
            self.capacite1_nom='Combo de Trois Coups'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=ChevalierMagique.projectiles
            self.capacite2_nom='Projectiles Magiques'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=ChevalierMagique.drain
            self.capacite3_nom='Drain Magique'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=3
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=ChevalierMagique.aura_eau
            self.anti_leader_skill=ChevalierMagique.anti_aura_eau

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Chevalier Magique',element[indice_element],4,1,3195,3195,192,171,89)

            self.pv_min_4=3195
            self.attaque_min_4=192
            self.defense_min_4=171
            self.pv_min_5=4350
            self.attaque_min_5=261
            self.defense_min_5=233
            self.pv_min_6=5910
            self.attaque_min_6=355
            self.defense_min_6=316

            self.pv_max_4=5430
            self.attaque_max_4=327
            self.defense_max_4=291
            self.pv_max_5=7380
            self.attaque_max_5=444
            self.defense_max_5=396
            self.pv_max_6=10050
            self.attaque_max_6=604
            self.defense_max_6=538

            self.nb_capacites=3

            self.capacite1=ChevalierMagique.combo
            self.capacite1_nom='Combo de Trois Coups'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=ChevalierMagique.balles
            self.capacite2_nom='Balles Magiques'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=ChevalierMagique.tempete
            self.capacite3_nom='Epée des Tempêtes'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=4
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=ChevalierMagique.aura_vent
            self.anti_leader_skill=ChevalierMagique.anti_aura_vent

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Chevalier Magique',element[indice_element],4,1,3045,3045,223,150,89)

            self.pv_min_4=3045
            self.attaque_min_4=223
            self.defense_min_4=150
            self.pv_min_5=4140
            self.attaque_min_5=304
            self.defense_min_5=204
            self.pv_min_6=5625
            self.attaque_min_6=413
            self.defense_min_6=278

            self.pv_max_4=5175
            self.attaque_max_4=380
            self.defense_max_4=255
            self.pv_max_5=7020
            self.attaque_max_5=517
            self.defense_max_5=347
            self.pv_max_6=9555
            self.attaque_max_6=703
            self.defense_max_6=472

            self.nb_capacites=2

            self.capacite1=ChevalierMagique.combo
            self.capacite1_nom='Combo de Trois Coups'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=ChevalierMagique.balles
            self.capacite2_nom='Balles Magiques'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=ChevalierMagique.altruisme

            self.presence_leader_skill=1
            self.leader_skill=ChevalierMagique.aura_lumiere
            self.anti_leader_skill=ChevalierMagique.anti_aura_lumiere

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Chevalier Magique',element[indice_element],4,1,2940,2940,178,203,89)

            self.pv_min_4=2940
            self.attaque_min_4=178
            self.defense_min_4=203
            self.pv_min_5=3990
            self.attaque_min_5=242
            self.defense_min_5=276
            self.pv_min_6=5430
            self.attaque_min_6=329
            self.defense_min_6=375

            self.pv_max_4=4995
            self.attaque_max_4=303
            self.defense_max_4=345
            self.pv_max_5=6780
            self.attaque_max_5=412
            self.defense_max_5=468
            self.pv_max_6=9225
            self.attaque_max_6=590
            self.defense_max_6=637

            self.nb_capacites=3

            self.capacite1=ChevalierMagique.combo
            self.capacite1_nom='Combo de Trois Coups'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=ChevalierMagique.projectiles
            self.capacite2_nom='Projectiles Magiques'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=ChevalierMagique.vortex
            self.capacite3_nom='Vortex des Ténèbres'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=ChevalierMagique.aura_tenebres
            self.anti_leader_skill=ChevalierMagique.anti_aura_tenebres

    def combo(self,equipe_ennemie,cible):
        print('\n',self.surnom,self.attribut,' tranche deux fois ',cible.surnom,cible.attribut,'!!\n')
        for index in range(2):
            degats=self.calcul_dommages(1,self.capacite1_bonus_skill,cible)
            self.affichage_du_type_de_coup(1,self.capacite1_bonus_skill,degats,cible)
            if(self.attribut=='Feu' and cible.pv_actuels>self.pv_actuels):
                degats+=Arrondir.a_l_unite(0.5*degats)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
        print('\nLa troisième attaque touche toute l\'équipe ennemie!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive()):
                degats=self.calcul_dommages(2,self.capacite1_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(2,self.capacite1_bonus_skill,degats,equipe_ennemie.membres[index])
                if(self.attribut=='Feu' and equipe_ennemie.membres[index].pv_actuels>self.pv_actuels):
                    degats+=Arrondir.a_l_unite(0.5*degats)
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])

    def tempete(self,equipe_ennemie,cible):
        print('\n',self.surnom,self.attribut,' tranche deux fois ',cible.surnom,cible.attribut,' avec une lame de vent!!\n')
        for index in range(2):
            degats=self.calcul_dommages(1,self.capacite3_bonus_skill,cible)
            self.affichage_du_type_de_coup(1,self.capacite3_bonus_skill,degats,cible)
            degats+=Arrondir.a_l_unite(0.06*self.pv_max_donjons)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(1,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    print(cible.surnom,cible.attribut,'voit sa jauge d\'attaque diminuer de 30%!!')
                    cible.jauge_attaque-=max(30,Arrondir.a_l_unite(0.3*cible.jauge_attaque))
        print('\n',self.surnom,self.attribut,' soulève une tempête qui touche toute l\'équipe ennemie!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive()):
                degats=self.calcul_dommages(1,self.capacite3_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(1,self.capacite3_bonus_skill,degats,equipe_ennemie.membres[index])
                degats+=Arrondir.a_l_unite(0.06*self.pv_max_donjons)
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(1,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,'voit sa jauge d\'attaque diminuer de 30%!!')
                        equipe_ennemie.membres[index].jauge_attaque-=max(30,Arrondir.a_l_unite(0.3*equipe_ennemie.membres[index].jauge_attaque))

    def projectiles(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' attaque toute l\'équipe ennemie avec quatre projectiles magiques aléatoires!!\n')
        for index in range(4):
            if(equipe_ennemie.is_alive()):
                indice_cible=random.randint(0,equipe_ennemie.len-1)
                while(equipe_ennemie.membres[indice_cible].pv_actuels<=0):
                    indice_cible=random.randint(0,equipe_ennemie.len-1)
                cible=equipe_ennemie.membres[indice_cible]
                degats=self.calcul_dommages(1.9,self.capacite2_bonus_skill,cible)
                self.affichage_du_type_de_coup(1.9,self.capacite2_bonus_skill,degats,cible)
                degats=cible.reduction_dommages(degats)
                self.procedure_attaque(degats,cible)
                if(cible.immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(0.5,cible.resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        cible.def_break(2)

    def drain(self,equipe_ennemie):
        self.vol_de_vie+=50
        print('\n',self.surnom,self.attribut,' aspire les forces de toute l\'équipe ennemie avec un vortex magique!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive() and equipe_ennemie.membres[index].pv_actuels>0):
                degats=self.calcul_dommages(4.8,self.capacite3_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(4.8,self.capacite3_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(1,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,'voit sa jauge d\'attaque drainée par ',self.surnom,self.attribut,'!! \n')
                        equipe_ennemie.membres[index].jauge_attaque-=max(25,Arrondir.a_l_unite(0.25*equipe_ennemie.membres[index].jauge_attaque))
                        self.jauge_attaque+=max(25,Arrondir.a_l_unite(0.25*equipe_ennemie.membres[index].jauge_attaque))
        self.vol_de_vie-=50

    def balles(self,cible):
        print('\n',self.surnom,self.attribut,' tire des balles magiques sur ',cible.surnom,cible.attribut,'!!\n')
        for index in range(3):
            degats=self.calcul_dommages(2.1,self.capacite2_bonus_skill,cible)
            self.affichage_du_type_de_coup(2.1,self.capacite2_bonus_skill,degats,cible)
            if(self.attribut=='Feu' and cible.pv_actuels > self.pv_actuels):
                degats+=Arrondir.a_l_unite(0.5*degats)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
            if(cible.immunite==0):
                effet_nefaste=random.randint(1,100)
                limite_reussite=Calcul.taux_reussite_effet(0.75,cible.resistance_actuelle,self.precision_actuelle)
                if(effet_nefaste<=100*limite_reussite):
                    print(cible.surnom,cible.attribut,'devient silencieuse pour deux tours!! \n')
                    cible.silencieux=1
                    cible.tours_silencieux=max(2,cible.tours_silencieux)

    def vortex(self,equipe_alliee,cible):
        print('\n',self.surnom,self.attribut,' projette un vortex de ténèbres sur ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(7,self.capacite3_bonus_skill,cible)
        self.affichage_du_type_de_coup(7,self.capacite3_bonus_skill,degats,cible)
        degats+=Arrondir.a_l_unite(0.16*cible.pv_max_donjons)
        degats=cible.reduction_dommages(degats)
        montant=Arrondir.a_l_unite(0.3*degats)
        self.procedure_attaque(degats,cible)
        print('\n L\'équipe récupère les forces de ',cible.surnom,cible.attribut,'!!\n')
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].etre_soigne(montant)

    def altruisme(self,cible,equipe_alliee):
        pv_min=equipe_alliee.membres[0].pv_actuels
        indice_du_min=0
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels<pv_min):
                pv_min=equipe_alliee.membres[index].pv_actuels
                indice_du_min=index
        print('\n',equipe_alliee.membres[indice_du_min].surnom,equipe_alliee.membres[indice_du_min].attribut,' guérit grâce à l\'aura de ',self.surnom,self.attribut,'!!')
        montant=Arrondir.a_l_unite(0.15*equipe_alliee.membres[indice_du_min].pv_max_donjons)
        equipe_alliee.membres[indice_du_min].etre_soigne(montant)
        aleatoire=random.randint(1,100)
        if(aleatoire<=35):
            cible.retirer_un_bonus()

    def feu_vengeur(equipe_alliee):
        for index in range(equipe_alliee.len):
            if((equipe_alliee.membres[index].nom=='Chevalier Magique' or equipe_alliee.membres[index].nom=='ChevalierMagique') and equipe_alliee.membres[index].attribut=='Feu'):
                ratio=1-(equipe_alliee.membres[index].pv_actuels/equipe_alliee.membres[index].pv_max_donjons)
                print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' voit sa vitesse augmenter grâce à son passif!!')
                equipe_alliee.membres[index].vitesse_actuelle=equipe_alliee.membres[index].vitesse_max_donjons+Arrondir.a_l_unite(ratio*equipe_alliee.membres[index].vitesse_max_donjons)
                if(equipe_alliee.membres[index].tours_bonus_vitesse>0):
                    equipe_alliee.membres[index].vitesse_actuelle+=Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].vitesse_actuelle)
                ''' Soigne de malus_vitesse '''

    def aura_feu(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].pv_actuels+=Arrondir.a_l_unite(0.25*equipe_alliee.membres[index].pv_max_donjons)
            equipe_alliee.membres[index].pv_max_donjons+=Arrondir.a_l_unite(0.25*equipe_alliee.membres[index].pv_max_donjons)
            print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 25%!!')
            print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].pv_actuels,'\n')

    def aura_eau(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].attaque_actuelle+=Arrondir.a_l_unite(0.25*equipe_alliee.membres[index].attaque_max_donjons)
            equipe_alliee.membres[index].attaque_max_donjons+=Arrondir.a_l_unite(0.25*equipe_alliee.membres[index].attaque_max_donjons)
            print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 25%!!')
            print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].attaque_actuelle,'\n')

    def aura_vent(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].taux_coup_critique_actuel+=0.19
            equipe_alliee.membres[index].taux_coup_critique_max_donjons+=0.19
            print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 19%!!')
            print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].taux_coup_critique_actuel,'\n')

    def aura_lumiere(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].precision_actuelle+=0.3
            equipe_alliee.membres[index].precision_max_donjons+=0.3
            print('La précision actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 30%!!')
            print('La précision actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].precision_actuelle,'\n')

    def aura_tenebres(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].vitesse_actuelle+=Arrondir.a_l_unite(0.19*equipe_alliee.membres[index].vitesse_max_donjons)
            equipe_alliee.membres[index].vitesse_max_donjons+=Arrondir.a_l_unite(0.19*equipe_alliee.membres[index].vitesse_max_donjons)
            print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 19%!!')
            print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].vitesse_actuelle,'\n')

    def anti_aura_feu(equipe_alliee):
        for index in range(equipe_alliee.len):
                equipe_alliee.membres[index].pv_actuels-=Arrondir.a_l_unite(0.25*equipe_alliee.membres[index].pv_max_donjons)

    def anti_aura_eau(equipe_alliee):
        for index in range(equipe_alliee.len):
                equipe_alliee.membres[index].attaque_actuelle-=Arrondir.a_l_unite(0.25*equipe_alliee.membres[index].attaque_max_donjons)

    def anti_aura_vent(equipe_alliee):
        for index in range(equipe_alliee.len):
                equipe_alliee.membres[index].taux_coup_critique_actuel-=0.19

    def anti_aura_lumiere(equipe_alliee):
        for index in range(equipe_alliee.len):
                equipe_alliee.membres[index].precision_actuelle-=0.3

    def anti_aura_tenebres(equipe_alliee):
        for index in range(equipe_alliee.len):
                equipe_alliee.membres[index].vitesse_actuelle-=Arrondir.a_l_unite(0.19*equipe_alliee.membres[index].vitesse_max_donjons)





class Vampire(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Vampire',element[indice_element],4,1,2985,2985,220,157,98)

            self.pv_min_4=2985
            self.attaque_min_4=220
            self.defense_min_4=157
            self.pv_min_5=4065
            self.attaque_min_5=299
            self.defense_min_5=214
            self.pv_min_6=5520
            self.attaque_min_6=407
            self.defense_min_6=291

            self.pv_max_4=5085
            self.attaque_max_4=374
            self.defense_max_4=267
            self.pv_max_5=6900
            self.attaque_max_5=509
            self.defense_max_5=363
            self.pv_max_6=9390
            self.attaque_max_6=692
            self.defense_max_6=494

            self.nb_capacites=2

            self.capacite1=Vampire.drain
            self.capacite1_nom='Drain de Vie'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Vampire.destruction
            self.capacite2_nom='Destruction'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Vampire.vitesse_donjons
            self.anti_leader_skill=Vampire.anti_vitesse_donjons

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Vampire',element[indice_element],4,1,3135,3135,192,175,98)

            self.pv_min_4=3135
            self.attaque_min_4=192
            self.defense_min_4=175
            self.pv_min_5=4275
            self.attaque_min_5=261
            self.defense_min_5=238
            self.pv_min_6=5805
            self.attaque_min_6=355
            self.defense_min_6=323

            self.pv_max_4=5340
            self.attaque_max_4=327
            self.defense_max_4=297
            self.pv_max_5=7260
            self.attaque_max_5=444
            self.defense_max_5=404
            self.pv_max_6=9885
            self.attaque_max_6=604
            self.defense_max_6=549

            self.nb_capacites=2

            self.capacite1=Vampire.drain
            self.capacite1_nom='Drain de Vie'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Vampire.aneantissement
            self.capacite2_nom='Anéantissement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Vampire.pv_donjons
            self.anti_leader_skill=Vampire.anti_pv_donjons

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Vampire',element[indice_element],4,1,2730,2730,230,164,98)

            self.pv_min_4=2730
            self.attaque_min_4=230
            self.defense_min_4=164
            self.pv_min_5=3705
            self.attaque_min_5=314
            self.defense_min_5=223
            self.pv_min_6=5040
            self.attaque_min_6=426
            self.defense_min_6=304

            self.pv_max_4=4635
            self.attaque_max_4=392
            self.defense_max_4=279
            self.pv_max_5=6300
            self.attaque_max_5=533
            self.defense_max_5=379
            self.pv_max_6=8565
            self.attaque_max_6=426
            self.defense_max_6=304

            self.nb_capacites=2

            self.capacite1=Vampire.drain
            self.capacite1_nom='Drain de Vie'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Vampire.aneantissement
            self.capacite2_nom='Anéantissement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Vampire.resistance_donjons
            self.anti_leader_skill=Vampire.anti_resistance_donjons

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Vampire',element[indice_element],5,1,5205,5205,314,195,98)

            self.pv_min_5=5205
            self.attaque_min_5=314
            self.defense_min_5=195
            self.pv_min_6=7065
            self.attaque_min_6=426
            self.defense_min_6=265

            self.pv_max_5=8835
            self.attaque_max_5=533
            self.defense_max_5=331
            self.pv_max_6=12015
            self.attaque_max_6=725
            self.defense_max_6=450

            self.nb_capacites=2

            self.capacite1=Vampire.drain
            self.capacite1_nom='Drain de Vie'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Vampire.destruction
            self.capacite2_nom='Destruction'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Vampire.attaque_donjons
            self.anti_leader_skill=Vampire.anti_attaque_donjons

            self.presence_passif_1=1
            self.passif_1=Vampire.immortalite

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Vampire',element[indice_element],5,1,4200,4200,361,214,98)

            self.pv_min_5=4200
            self.attaque_min_5=361
            self.defense_min_5=214
            self.pv_min_6=5715
            self.attaque_min_6=491
            self.defense_min_6=291

            self.pv_max_5=7140
            self.attaque_max_5=613
            self.defense_max_5=363
            self.pv_max_6=9720
            self.attaque_max_6=834
            self.defense_max_6=494

            self.nb_capacites=2

            self.capacite1=Vampire.drain
            self.capacite1_nom='Drain de Vie'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Vampire.aneantissement
            self.capacite2_nom='Aneantissement'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Vampire.taux_cc_donjons
            self.anti_leader_skill=Vampire.anti_taux_cc_donjons

            self.presence_passif_1=1
            self.passif_1=Vampire.soif_de_sang

    def drain(self,cible):
        self.vol_de_vie+=30
        print('\n',self.surnom,self.attribut,' absorbe la vie de ',cible.surnom,cible.attribut,'!!\n')
        for index in range(2):
            degats=self.calcul_dommages(2,self.capacite1_bonus_skill,cible)
            self.affichage_du_type_de_coup(2,self.capacite1_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)
        self.vol_de_vie-=30

    def destruction(self,cible):
        self.taux_coup_critique_actuel+=0.3
        print('\n',self.surnom,self.attribut,' pulvérise ',cible.surnom,cible.attribut,' avec deux coups puissants!!\n')
        for index in range(2):
            degats=self.calcul_dommages(3,self.capacite2_bonus_skill,cible)
            self.affichage_du_type_de_coup(3,self.capacite2_bonus_skill,degats,cible)
            degats=cible.reduction_dommages(degats)
            self.procedure_attaque(degats,cible)

    def aneantissement(self,cible):
        print('\n',self.surnom,self.attribut,' anéantit ',cible.surnom,cible.attribut,'!!\n')
        degats=self.calcul_dommages(6.2,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(6.2,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite==0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.75,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                cible.slow_down(2)
                cible.atk_break(2)
                print(cible.surnom,cible.attribut,' ne pourra plus recevoir de bonus pour les deux prochains tours!!\n')
                cible.immunite_aux_bonus=1
                cible.tours_immunite_aux_bonus=max(cible.tours_immunite_aux_bonus,2)

    def soif_de_sang(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].jauge_attaque+=max(30,Arrondir.a_l_unite(0.3*equipe_alliee.membres[index].jauge_attaque))
        ''' Vrai effet à implémenter :
            Feast of Blood (Passive):
            Attacks leave a Branding Effect that lasts for 2 turns and
            heal all allies for 30% of the damage done.
            Also, whenever you kill an enemy, the attack bar of all allies increases by 30%.
        '''

    def immortalite(equipe_alliee):
        print('\n\nActivation du passif d\'Immortalité du Vampire Lumière \n\n')
        montant=0
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels>(0.3*equipe_alliee.membres[index].pv_max_donjons) and (equipe_alliee.membres[index].nom!='Vampire' or equipe_alliee.membres[index].attribut!='Lumiere')):
                montant+=Arrondir.a_l_unite(0.1*equipe_alliee.membres[index].pv_max_donjons)
                equipe_alliee.membres[index].pv_actuels-=Arrondir.a_l_unite(0.1*equipe_alliee.membres[index].pv_max_donjons)
                print(equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' perd un dixième de ses PV max!!')
            elif(equipe_alliee.membres[index].nom=='Vampire' and equipe_alliee.membres[index].attribut=='Lumière'):
                indice_vampire=index
        if(montant>0 and equipe_alliee.membres[indice_vampire].sans_resurrection<=0):
            print(equipe_alliee.membres[indice_vampire].surnom,equipe_alliee.membres[indice_vampire].attribut,' revient à la vie avec ',montant,' points de vie!!\n')
            equipe_alliee.membres[indice_vampire].pv_actuels=montant

    def vitesse_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].vitesse_actuelle+=Arrondir.a_l_unite(0.28*equipe_alliee.membres[index].vitesse_max_donjons)
            equipe_alliee.membres[index].vitesse_max_donjons+=Arrondir.a_l_unite(0.28*equipe_alliee.membres[index].vitesse_max_donjons)
            print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 28%!!')
            print('La vitesse actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].vitesse_actuelle,'\n')

    def pv_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].pv_actuels+=Arrondir.a_l_unite(0.38*equipe_alliee.membres[index].pv_max_donjons)
            equipe_alliee.membres[index].pv_max_donjons+=Arrondir.a_l_unite(0.38*equipe_alliee.membres[index].pv_max_donjons)
            print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 38%!!')
            print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].pv_actuels,'\n')

    def resistance_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].resistance_actuelle+=0.48
            equipe_alliee.membres[index].resistance_max_donjons+=0.48
            print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 48%!!')
            print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].resistance_actuelle,'\n')

    def attaque_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].attaque_actuelle+=Arrondir.a_l_unite(0.38*equipe_alliee.membres[index].attaque_max_donjons)
            equipe_alliee.membres[index].attaque_max_donjons+=Arrondir.a_l_unite(0.38*equipe_alliee.membres[index].attaque_max_donjons)
            print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 38%!!')
            print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].attaque_actuelle,'\n')

    def taux_cc_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].taux_coup_critique_actuel+=0.28
            equipe_alliee.membres[index].taux_coup_critique_max_donjons+=0.28
            print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 28%!!')
            print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].taux_coup_critique_actuel,'\n')

    def anti_vitesse_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].vitesse_actuelle-=Arrondir.a_l_unite(0.28*equipe_alliee.membres[index].vitesse_max_donjons)

    def anti_pv_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].pv_actuels-=Arrondir.a_l_unite(0.38*equipe_alliee.membres[index].pv_max_donjons)
        
    def anti_resistance_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].resistance_actuelle-=0.48

    def anti_attaque_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].attaque_actuelle-=Arrondir.a_l_unite(0.38*equipe_alliee.membres[index].attaque_max_donjons)

    def anti_taux_cc_donjons(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].taux_coup_critique_actuel-=0.28



class Phenix(Monstre): # Blast
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)

        if (element[indice_element]=='Feu'):
            Monstre.__init__(self,'Phénix',element[indice_element],5,1,3990,3990,361,228,93)

            self.pv_min_5=3390
            self.attaque_min_5=361
            self.defense_min_5=228
            self.pv_min_6=5430
            self.attaque_min_6=491
            self.defense_min_6=310

            self.pv_max_5=6780
            self.attaque_max_5=613
            self.defense_max_5=387
            self.pv_max_6=9225
            self.attaque_max_6=834
            self.defense_max_6=527

            self.nb_capacites=2

            self.capacite1=Phenix.geyser
            self.capacite1_nom='Geyser de Feu'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Phenix.etoile
            self.capacite2_nom='Etoile Ecarlate'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Phenix.eternite

            self.presence_passif_2=1
            self.passif_2=Phenix.resurrection
            self.passif_active=0
            self.attente_passif=0

            self.presence_leader_skill=1
            self.leader_skill=Phenix.super_power
            self.anti_leader_skill=Phenix.anti_super_power

        if (element[indice_element]=='Eau'):
            Monstre.__init__(self,'Phénix',element[indice_element],5,1,3420,3420,380,247,93)

            self.pv_min_5=3420
            self.attaque_min_5=380
            self.defense_min_5=247
            self.pv_min_6=4650
            self.attaque_min_6=517
            self.defense_min_6=336

            self.pv_max_5=5805
            self.attaque_max_5=646
            self.defense_max_5=420
            self.pv_max_6=7905
            self.attaque_max_6=878
            self.defense_max_6=571

            self.nb_capacites=3

            self.capacite1=Phenix.geyser
            self.capacite1_nom='Geyser de Glace'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Phenix.orbe
            self.capacite2_nom='Etoile des Neiges'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Phenix.blizzard
            self.capacite3_nom='Blizzard Absolu'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Phenix.super_life
            self.anti_leader_skill=Phenix.anti_super_life

        if (element[indice_element]=='Vent'):
            Monstre.__init__(self,'Phénix',element[indice_element],5,1,3285,3285,428,209,93)

            self.pv_min_5=3285
            self.attaque_min_5=428
            self.defense_min_5=209
            self.pv_min_6=4455
            self.attaque_min_6=581
            self.defense_min_6=284

            self.pv_max_5=5565
            self.attaque_max_5=727
            self.defense_max_5=355
            self.pv_max_6=7575
            self.attaque_max_6=988
            self.defense_max_6=483

            self.nb_capacites=3

            self.capacite1=Phenix.geyser
            self.capacite1_nom='Geyser de Vent'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Phenix.etoile
            self.capacite2_nom='Etoile Céleste'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Phenix.tempete
            self.capacite3_nom='Tempête Destructrice'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Phenix.super_critique
            self.anti_leader_skill=Phenix.anti_super_critique

        if (element[indice_element]=='Lumière'):
            Monstre.__init__(self,'Phénix',element[indice_element],5,1,3705,3705,333,276,93)

            self.pv_min_5=3705
            self.attaque_min_5=333
            self.defense_min_5=276
            self.pv_min_6=5040
            self.attaque_min_6=452
            self.defense_min_6=375

            self.pv_max_5=6300
            self.attaque_max_5=565
            self.defense_max_5=468
            self.pv_max_6=8565
            self.attaque_max_6=769
            self.defense_max_6=637

            self.nb_capacites=3

            self.capacite1=Phenix.geyser
            self.capacite1_nom='Geyser de Lumière'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Phenix.orbe
            self.capacite2_nom='Etoile Astrale'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=3
            self.attente2=0
            self.etat_cap2='dispo'

            self.capacite3=Phenix.purification
            self.capacite3_nom='Déflagration Purifiante'
            self.capacite3_bonus_skill=0
            self.temps_recharge3=5
            self.attente3=0
            self.etat_cap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Phenix.super_tank
            self.anti_leader_skill=Phenix.anti_super_tank

        if (element[indice_element]=='Ténèbres'):
            Monstre.__init__(self,'Phénix',element[indice_element],5,1,3570,3570,399,219,93)

            self.pv_min_5=3570
            self.attaque_min_5=399
            self.defense_min_5=219
            self.pv_min_6=4845
            self.attaque_min_6=542
            self.defense_min_6=297

            self.pv_max_5=6060
            self.attaque_max_5=678
            self.defense_max_5=371
            self.pv_max_6=8235
            self.attaque_max_6=922
            self.defense_max_6=505

            self.nb_capacites=2

            self.capacite1=Phenix.geyser
            self.capacite1_nom='Geyser de Ténèbres'
            self.capacite1_bonus_skill=0
            self.temps_recharge1=1
            self.attente1=0
            self.etat_cap1='dispo'

            self.capacite2=Phenix.etoile
            self.capacite2_nom='Etoile du Désespoir'
            self.capacite2_bonus_skill=0
            self.temps_recharge2=4
            self.attente2=0
            self.etat_cap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Phenix.enfer

            self.presence_leader_skill=1
            self.leader_skill=Phenix.super_resistance
            self.anti_leader_skill=Phenix.anti_super_resistance

    ''' Remplacer les ressusciter par renaitre de ses cendres '''
    def geyser(self,cible):
        if(self.attribut=='Feu'):
            print('\n',self.surnom,self.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un geyser de feu instantané!!\n')
        elif(self.attribut=='Eau'):
            print('\n',self.surnom,self.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un geyser de glace instantané!!\n')
        elif(self.attribut=='Vent'):
            print('\n',self.surnom,self.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un geyser de vent instantané!!\n')
        elif(self.attribut=='Lumière'):
            print('\n',self.surnom,self.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un geyser de lumière instantané!!\n')
        elif(self.attribut=='Ténèbres'):
            print('\n',self.surnom,self.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un geyser de ténèbres instantané!!\n')
        degats=self.calcul_dommages(4.2,self.capacite1_bonus_skill,cible)
        self.affichage_du_type_de_coup(4.2,self.capacite1_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(cible.immunite<=0):
            effet_nefaste=random.randint(1,100)
            limite_reussite=Calcul.taux_reussite_effet(0.18,cible.resistance_actuelle,self.precision_actuelle)
            if(effet_nefaste<=100*limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!!\n')
                cible.stun=1
        if(self.attribut=='Feu' and self.passif_active!=0):
            self.attente_passif-=1
            if(self.attente_passif<=0):
                print('\n',self.surnom,self.attribut,' peut à nouveau renaitre de ses cendres!!\n')
                self.passif_active=0
            else:
                print('\n',self.surnom,self.attribut,' voit diminuer de 1 le temps à attendre avant de pouvoir renaitre de ses cendres à nouveau!!')

    def etoile(self,cible):
        pourcentage_pv_perdus_cible=Arrondir.a_l_unite(cible.pv_actuels/cible.pv_max_donjons)
        bonus_multiplicateur=4*pourcentage_pv_perdus_cible
        if(self.attribut=='Feu'):
            print('\n',self.surnom,self.attribut,' réduit ',cible.surnom,cible.attribut,' en cendres avec une gigantesque sphère de flammes!!\n')
        elif(self.attribut=='Vent'):
            print('\n',self.surnom,self.attribut,' réduit ',cible.surnom,cible.attribut,' en poussière avec une gigantesque sphère de vent!!\n')
        elif(self.attribut=='Ténèbres'):
            print('\n',self.surnom,self.attribut,' réduit ',cible.surnom,cible.attribut,' en cendres avec une gigantesque sphère de flammes noires!!\n')
        degats=self.calcul_dommages(5+bonus_multiplicateur,self.capacite2_bonus_skill,cible)
        self.affichage_du_type_de_coup(5+bonus_multiplicateur,self.capacite2_bonus_skill,degats,cible)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(self.attribut=='Feu' and self.passif_active!=0):
            self.attente_passif-=1
            if(self.attente_passif<=0):
                print('\n',self.surnom,self.attribut,' peut à nouveau renaitre de ses cendres!!\n')
                self.passif_active=0
            else:
                print('\n',self.surnom,self.attribut,' voit diminuer de 1 le temps à attendre avant de pouvoir renaitre de ses cendres à nouveau!!')

    def orbe(self,cible):
        if(self.attribut=='Eau'):
            print('\n',self.surnom,self.attribut,' réduit ',cible.surnom,cible.attribut,' à néant avec une gigantesque sphère de glace!!\n')
        elif(self.attribut=='Lumière'):
            print('\n',self.surnom,self.attribut,' réduit ',cible.surnom,cible.attribut,' à néant avec une gigantesque sphère de lumière pure!!\n')
        degats=self.calcul_dommages(4.5,self.capacite2_bonus_skill,cible)
        type_coup=self.affichage_du_type_de_coup(4.5,self.capacite2_bonus_skill,degats,cible)
        degats+=Arrondir.a_l_unite(0.08*cible.pv_max_donjons)
        degats=cible.reduction_dommages(degats)
        self.procedure_attaque(degats,cible)
        if(type_coup=='Critique'):
            print(cible.surnom,cible.attribut,' est gelé(e)!!\n')
            cible.gel=1

    def blizzard(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' engloutit toute l\'équipe ennemie dans un puissant blizzard!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive() and equipe_ennemie.membres[index].pv_actuels>0):
                degats=self.calcul_dommages(3,self.capacite3_bonusS_skill,equipe_ennemie.membres[index])
                type_coup=self.affichage_du_type_de_coup(3,self.capacite3_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                degats+=Arrondir.a_l_unite(0.12*equipe_ennemie.membres[index].pv_max_donjons)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].immunite==0):
                    effet_nefaste=random.randint(1,100)
                    limite_reussite=Calcul.taux_reussite_effet(1,equipe_ennemie.membres[index].resistance_actuelle,self.precision_actuelle)
                    if(effet_nefaste<=100*limite_reussite):
                        equipe_ennemie.membres[index].atk_break(2)
                    if(type_coup=='Critique'):
                        print(equipe_ennemie.membres[index].surnom,equipe_ennemie.membres[index].attribut,' est gelé(e)!!\n')
                        equipe_ennemie.membres[index].gel=1

    def tempete(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' engloutit toute l\'équipe ennemie dans une violente tempête!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive() and equipe_ennemie.membres[index].pv_actuels>0):
                degats=self.calcul_dommages(4.5,self.capacite3_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(4.5,self.capacite3_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])
                if(equipe_ennemie.membres[index].pv_actuels<=0):
                    print('\n',self.surnom,self.attribut,' a tué quelqu\'un et voit donc son temps de recharge réduit à zéro!!')
                    print(self.surnom,self.attribut,' voit sa jauge d\'attaque augmenter immédiatement de 20%!!\n')
                    self.attente3=0
                    self.etat_cap3='dispo'
                    self.jauge_attaque+=max(20,Arrondir.a_l_unite(0.2*self.jauge_attaque))

    def purification(self,equipe_ennemie):
        print('\n',self.surnom,self.attribut,' éblouit toute l\'équipe ennemie d\'une lumière aveuglante!!\n')
        for index in range(equipe_ennemie.len):
            if(equipe_ennemie.is_alive() and equipe_ennemie.membres[index].pv_actuels>0):
                nb_effets_bonus=equipe_ennemie.membres[index].nb_effets_renforcement()
                equipe_ennemie.membres[index].soigner_de_tous_les_biens()
                if(nb_effets_bonus>0):
                    equipe_ennemie.membres[index].def_break(1)
                degats=self.calcul_dommages(4.5,self.capacite3_bonus_skill,equipe_ennemie.membres[index])
                self.affichage_du_type_de_coup(4.5,self.capacite3_bonus_skill,degats,equipe_ennemie.membres[index])
                degats=equipe_ennemie.membres[index].reduction_dommages(degats)
                self.procedure_attaque(degats,equipe_ennemie.membres[index])

    ''' Passif de fin de tour pour Phénix Feu'''
    def eternite(equipe_alliee):
        print('\nToute l\'équipe reçoit la bénédiction du phénix de feu!!\n')
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].pv_actuels>0 and (equipe_alliee.membres[index].nom!='Phénix' or equipe_alliee.membres[index].attribut!='Feu')):
                if(equipe_alliee.membres[index].perturbation_recup<=0):
                    montant=Arrondir.a_l_unite(0.1*equipe_alliee.membres[index].pv_max_donjons)
                    equipe_alliee.membres[index].etre_soigne(montant)
                else:
                    print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces... \n')
            elif(equipe_alliee.membres[index].pv_actuels<=0):
                print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est mort(e)!!\n')
            else:
                print('\nDans son immense générosité, le phénix de feu ne peut pas se soigner lui-même... \n')

    ''' Passif de fin de tour adverse pour Phénix Feu '''
    def resurrection(equipe_alliee):
        for index in range(equipe_alliee.len):
            if(equipe_alliee.membres[index].nom=='Phénix' and equipe_alliee.membres[index].attribut=='Feu'):
                if(equipe_alliee.membres[index].pv_actuels<=0 and equipe_alliee.membres[index].passif_active==0):
                    if(equipe_alliee.membres[index].sans_resurrection<=0):
                        print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' revient à la vie avec 100% de ses point de vie max!!')
                        print('Son passif se met maintenant en pause pour douze tours.\n')
                        equipe_alliee.membres[index].pv_actuels=equipe_alliee.membres[index].pv_max_donjons
                        equipe_alliee.membres[index].passif_active=1
                        equipe_alliee.membres[index].attente_passif=12
                    else:
                        print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' a été maudit et ne peut donc pas revenir à la vie... \n')
                elif(equipe_alliee.membres[index].pv_actuels<=0 and equipe_alliee.membres[index].passif_active!=0):
                    print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est déjà revenu à la vie et ne peut donc pas ressusciter...\n')
                else:
                    print('\n',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est toujours vivant!!\n')

    ''' Passif de fin de tour pour Phénix Ténèbres '''
    def enfer(self,cible):
        if(cible.pv_actuels<=0):
            print('\n',cible.surnom,cible.attribut,' est consumé(e) par les flammes de l\'Enfer et ne pourra donc pas revenir à la vie!!')
            print('Le temps de rechargement de Etoile du Désespoir diminue de 1!!\n')
            cible.sans_resurrection=1
            self.attente2-=1
        ''' else: Faire Branding Effects (3 tours avec 50% de chances)'''


    def super_power(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].attaque_actuelle+=Arrondir.a_l_unite(0.44*equipe_alliee.membres[index].attaque_max_donjons)
            equipe_alliee.membres[index].attaque_max_donjons+=Arrondir.a_l_unite(0.44*equipe_alliee.membres[index].attaque_max_donjons)
            print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 44%!!')
            print('L\'attaque actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].attaque_actuelle,'\n')

    def super_life(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].pv_actuels+=Arrondir.a_l_unite(0.44*equipe_alliee.membres[index].pv_max_donjons)
            equipe_alliee.membres[index].pv_max_donjons+=Arrondir.a_l_unite(0.44*equipe_alliee.membres[index].pv_max_donjons)
            print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 44%!!')
            print('Les points de vie actuels de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' sont désormais de ',equipe_alliee.membres[index].pv_actuels,'\n')

    def super_critique(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].taux_coup_critique_actuel+=0.33
            equipe_alliee.membres[index].taux_coup_critique_max_donjons+=0.33
            print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 33%!!')
            print('Le taux de coup critique actuel de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].taux_coup_critique_actuel,'\n')

    def super_tank(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].defense_actuelle+=Arrondir.a_l_unite(0.44*equipe_alliee.membres[index].defense_max_donjons)
            equipe_alliee.membres[index].defense_max_donjons+=Arrondir.a_l_unite(0.44*equipe_alliee.membres[index].defense_max_donjons)
            print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 44%!!')
            print('La défense actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].defense_actuelle,'\n')

    def super_resistance(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].resistance_actuelle+=0.55
            equipe_alliee.membres[index].resistance_max_donjons+=0.55
            print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' augmente de 55%!!')
            print('La résistance actuelle de ',equipe_alliee.membres[index].surnom,equipe_alliee.membres[index].attribut,' est désormais de ',equipe_alliee.membres[index].resistance_actuelle,'\n')

    def anti_super_power(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].attaque_actuelle-=Arrondir.a_l_unite(0.44*equipe_alliee.membres[index].attaque_max_donjons)

    def anti_super_life(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].pv_actuels-=Arrondir.a_l_unite(0.44*equipe_alliee.membres[index].pv_max_donjons)

    def anti_super_critique(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].taux_coup_critique_actuel-=0.33

    def anti_super_tank(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].defense_actuelle-=Arrondir.a_l_unite(0.44*equipe_alliee.membres[index].defense_max_donjons)

    def anti_super_resistance(equipe_alliee):
        for index in range(equipe_alliee.len):
            equipe_alliee.membres[index].resistance_actuelle-=0.55
























# POUR FAIRE LA PARTIE ENTIERE D UN NOMBRE
# nombre=math.floor(nombre)
# POUR LA FAIRE PAR EXCES PLUTOT QUE PAR DEFAUT
# nombre=math.ceil(nombre)



# On aurait pu faire sans return.
# L'utilisation massive de cette fonction me fait néanmoins conserver cette implémentation.
# Idem pour la classe Calcul (même si la conception de la classe Calcul en elle-même est absurde)
class Arrondir:
    def a_l_unite(nombre):
        reste = nombre%1
        if(reste >= 0.5):
            nombre = math.ceil(nombre)
        else:
            nombre = math.floor(nombre)
        return nombre

    def au_centieme(nombre):
        return (Arrondir.a_l_unite(100*nombre))/100


class Calcul:
    def taux_reussite_effet(self,resistance,precision):
        resistance_totale=resistance-precision
        if (resistance_totale<0.15):
            resistance_totale=0.15
        taux_reussite=1-resistance_totale
        pourcentage_reussite_effet=self*taux_reussite
        return pourcentage_reussite_effet

    # Possibilité de rajouter ici d'autres fonctions de calcul amusantes








class Security:
    def is_decimal(self):
        return str.isdecimal(self)

    def is_string(self):
        return self.isalpha()
