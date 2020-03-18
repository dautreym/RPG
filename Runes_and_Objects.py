# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:41:34 2019

@author: marin
"""

''' if need help : https://programmation360.com/programmation-orientee-objet-python/ '''

import sys
import math
from ast import literal_eval
import random

#from Teams import *


'''
from Base import *
from Dungeon import *
from Functions import *
from Functions import Arrondir
from Inventory_and_Teams import *
from Monsters import *
'''


''' Donner à tous les parchemins des taux de réussite pour toutes les étoiles avec comme valeur 0 '''
class Objets:
    def __init__(self,nom_donne):
        self.type='Objet_courant'
        self.nom=nom_donne
        if(self.nom == 'Parchemin d invocation'):
            self.taux_reussite_une_etoile=74.2
            self.taux_reussite_deux_etoiles=24.4
            self.taux_reussite_trois_etoiles=1.4
            self.prix_d_achat=3900
            self.prix_de_vente=2000
            self.prix_d_utilisation=300
        if(self.nom == 'Parchemin d invocation superieure'):
            self.taux_reussite_trois_etoiles=92.4
            self.taux_reussite_quatre_etoiles=7.3
            self.taux_reussite_cinq_etoiles=0.4
            self.prix_d_achat=115000
            self.prix_de_vente=60000
            self.prix_d_utilisation=10000
        if(self.nom == 'Parchemin d invocation ultra superieure'):
            self.taux_reussite_trois_etoiles=91.5
            self.taux_reussite_quatre_etoiles=8
            self.taux_reussite_cinq_etoiles=0.5
            self.prix_d_achat=145000
            self.prix_de_vente=75000
            self.prix_d_utilisation=10000
        if(self.nom == 'Parchemin d invocation fusion'):
            self.taux_reussite_trois_etoiles=91.5
            self.taux_reussite_quatre_etoiles=8
            self.taux_reussite_cinq_etoiles=0.5
        if(self.nom == 'Parchemin d invocation interdite'):
            self.taux_reussite_trois_etoiles=50
            self.taux_reussite_quatre_etoiles=31.25
            self.taux_reussite_cinq_etoiles=18.75
        if(self.nom == 'Parchemin d invocation legendaire'):
            self.taux_reussite_quatre_etoiles=93.9
            self.taux_reussite_cinq_etoiles=6.1
            self.prix_d_utilisation=50000
        if(self.nom == 'Parchemin d invocation divine'):
            self.prix_d_utilisation=100000

        if(self.nom == 'Parchemin d invocation Inugami d Eau'):
            self.prix_d_utilisation=3000
        if(self.nom == 'Parchemin d invocation Mastodonte de Ténèbres'):
            self.prix_d_utilisation=3000
        if(self.nom == 'Parchemin d invocation Golem de Feu'):
            self.prix_d_utilisation=3000

    def utiliser(self,game):
        reussite=random.randint(1,100)+((random.randint(1,100))/100)
        if(self.nom=='Parchemin d invocation'):
            if(reussite<=self.taux_reussite_trois_etoiles):
                creature=game.invoquer(3)
            elif(reussite>self.taux_reussite_une_etoile):
                creature=game.invoquer(1)
            else:
                creature=game.invoquer(2)
        if(self.nom=='Parchemin d invocation superieure'):
            if(reussite<=self.taux_reussite_cinq_etoiles):
                creature=game.invoquer(5)
            elif(reussite>self.taux_reussite_trois_etoiles):
                creature=game.invoquer(3)
            else:
                creature=game.invoquer(4)
        if(self.nom=='Parchemin d invocation ultra superieure'):
            if(reussite<=self.taux_reussite_cinq_etoiles):
                creature=game.invoquer(5)
            elif(reussite>self.taux_reussite_trois_etoiles):
                creature=game.invoquer(3)
            else:
                creature=game.invoquer(4)
        if(self.nom=='Parchemin d invocation fusion'):
            if(reussite<=self.taux_reussite_cinq_etoiles):
                creature=game.invoquer(5)
            elif(reussite>self.taux_reussite_trois_etoiles):
                creature=game.invoquer(3)
            else:
                creature=game.invoquer(4)
        if(self.nom=='Parchemin d invocation legendaire'):
            if(reussite<=self.taux_reussite_cinq_etoiles):
                creature=game.invoquer(5)
            else:
                creature=game.invoquer(4)
        if(self.nom=='Parchemin d invocation divine'):
            creature=game.invoquer(5)

        if(self.nom=='Parchemin d invocation Inugami d Eau'):
            creature=game.invoquer_defini('Inugami','Eau')
        if(self.nom=='Parchemin d invocation Mastodonte de Ténèbres'):
            creature=game.invoquer_defini('Mastodonte','Ténèbres')
        if(self.nom=='Parchemin d invocation Golem de Feu'):
            creature=game.invoquer_defini('Golem','Feu')

        return creature



class Runes:
    def __init__(self,nom_donne,categorie_donnee,position_donnee,qualite_donnee,rarete_donnee,bonus_donne):
        self.type='Rune'
        self.nom=nom_donne
        self.categorie=categorie_donnee
        self.niveau=0
        self.position=position_donnee
        self.qualite=qualite_donnee
        self.rarete=rarete_donnee
        if(self.rarete == 'Normale'):
            self.nb_bonus_stats_secondaires=0
        if(self.rarete == 'Magique'):
            self.nb_bonus_stats_secondaires=1
        if(self.rarete == 'Rare'):
            self.nb_bonus_stats_secondaires=2
        if(self.rarete == 'Héroïque'):
            self.nb_bonus_stats_secondaires=3
        if(self.rarete == 'Légendaire'):
            self.nb_bonus_stats_secondaires=4

        self.famille_de_bonus=bonus_donne
        self.familles_de_bonus_possibles=['HP+','HP%','ATK+','ATK%','DEF+','DEF%','VIT','TCC%','DC%','RES%','ACC%']

        self.presence_bonus_secondaires=[0,0,0,0]
        self.bonus_secondaires=[[],[],[],[]]

        if (self.qualite == 'I'):
            self.qualite_numerique=1
        if (self.qualite == 'II'):
            self.qualite_numerique=2
        if (self.qualite == 'III'):
            self.qualite_numerique=3
        if (self.qualite == 'IV'):
            self.qualite_numerique=4
        if (self.qualite == 'V'):
            self.qualite_numerique=5
        if (self.qualite == 'VI'):
            self.qualite_numerique=6

        self.gain_en_pv=0
        self.gain_en_pourcentage_de_pv=0
        self.gain_en_attaque=0
        self.gain_en_pourcentage_de_attaque=0
        self.gain_en_defense=0
        self.gain_en_pourcentage_de_defense=0
        self.gain_en_vitesse=0
        self.gain_en_taux_de_coup_critique=0
        self.gain_en_dommages_critiques=0
        self.gain_en_resistance=0
        self.gain_en_precision=0
        self.gains=[self.gain_en_pv,self.gain_en_pourcentage_de_pv,self.gain_en_attaque,self.gain_en_pourcentage_de_attaque,self.gain_en_defense,self.gain_en_pourcentage_de_defense,self.gain_en_vitesse,self.gain_en_taux_de_coup_critique,self.gain_en_dommages_critiques,self.gain_en_resistance,self.gain_en_precision]

        for index in range(len(self.familles_de_bonus_possibles)):
            if(self.famille_de_bonus == self.familles_de_bonus_possibles[index]):
                self.gains[index]=self.trouver_bonus_stat_initial(self.famille_de_bonus,self.qualite_numerique)

        self.prochain_bonus_stat_principale=self.trouver_prochain_bonus_stat_principale(self.famille_de_bonus,self.qualite_numerique)
        self.cout_prochaine_amelioration=self.trouver_cout_prochaine_amelioration(self.qualite_numerique,0)
        self.prix_d_achat=1000*self.qualite_numerique


    def initialiser(self):
        for index in range(self.nb_bonus_stats_secondaires):
            self.creer_stat_secondaire()

    # Fonction obsolète non utilisée 
    def reinitialiser(self,nom,categorie,position,qualite,rarete,bonus,niveau,bonus_secondaires,liste_des_gains):
        self=Runes(nom,categorie,position,qualite,rarete,bonus)
        self.niveau=niveau

        if(niveau != 15):
            self.prochain_bonus_stat_principale=self.trouver_prochain_bonus_stat_principale(bonus,rune.qualite_numerique)
            self.cout_prochaine_amelioration=self.trouver_cout_prochaine_amelioration(rune.qualite_numerique,rune.niveau)

        for index in range(len(self.gains)):
            self.gains[index]=liste_des_gains[index]

        self.bonus_secondaires=bonus_secondaires
        # Appliquer les bonus secondaires à gain_en_ ... ?


    def __str__(self):
        return str(self.rarete)+' '+str(self.nom)+' niveau '+str(self.niveau)+'\n Catégorie : '+str(self.categorie)+'\n Position : '+str(self.position)+'\n Gain en PV : '+str(self.gains[0])+'\n Gain en pourcentage de PV : '+str(self.gains[1])+'%\n Gain en attaque : '+str(self.gains[2])+'\n Gain en pourcentage d\'attaque : '+str(self.gains[3])+'%\n Gain en défense : '+str(self.gains[4])+'\n Gain en pourcentage de défense : '+str(self.gains[5])+'%\n Gain en vitesse : '+str(self.gains[6])+'\n Gain en taux de coup critique : '+str(self.gains[7])+'%\n Gain en dommages critiques : '+str(self.gains[8])+'%\n Gain en résistance : '+str(100*self.gains[9])+'%\n Gain en précision : '+str(100*self.gains[10])+'%\n'

    def trouver_cout_prochaine_amelioration(self,qualite,niveau):
        couts_amelioration_LV1=[100,175,250,400,550,775,1000,1300,1600,2000,2400,2925,3450,4100,4750]
        couts_amelioration_LV2=[150,300,450,700,950,1275,1600,2025,2450,3000,3550,4225,4900,5700,6500]
        couts_amelioration_LV3=[225,475,725,1075,1425,1875,2325,2850,3375,4075,4775,5600,6425,7375,8325]
        couts_amelioration_LV4=[330,680,1030,1480,1930,2455,2980,3680,4380,5205,6030,6980,7930,9130,10330]
        couts_amelioration_LV5=[500,950,1400,1925,2450,3175,3900,4750,5600,6600,7600,8850,10100,11600,13100]
        couts_amelioration_LV6=[750,1475,2200,3050,3900,4875,5850,6975,8100,9350,10600,11975,13350,14850,16350]
        couts_amelioration=[couts_amelioration_LV1,couts_amelioration_LV2,couts_amelioration_LV3,couts_amelioration_LV4,couts_amelioration_LV5,couts_amelioration_LV6]
        cout_prochaine_amelioration=couts_amelioration[qualite-1][niveau]
        return cout_prochaine_amelioration

    def trouver_bonus_stat_initial(self,famille_bonus,qualite):
        bonus_hp=[40,70,100,160,270,360]
        bonus_pourcentage_hp=[0.01,0.02,0.04,0.05,0.08,0.11]
        bonus_attaque=[3,5,7,10,15,22]
        bonus_pourcentage_attaque=[0.01,0.02,0.04,0.05,0.08,0.11]
        bonus_defense=[3,5,7,10,15,22]
        bonus_pourcentage_defense=[0.01,0.02,0.04,0.05,0.08,0.11]
        bonus_vitesse=[1,2,3,4,5,7]
        bonus_taux_coup_critique=[0.01,0.02,0.03,0.04,0.05,0.07]
        bonus_dommages_critiques=[0.02,0.03,0.04,0.06,0.08,0.11]
        bonus_resistance=[0.01,0.02,0.04,0.06,0.09,0.12]
        bonus_precision=[0.01,0.02,0.04,0.06,0.09,0.12]

        bonus_possibles=[bonus_hp,bonus_pourcentage_hp,bonus_attaque,bonus_pourcentage_attaque,bonus_defense,bonus_pourcentage_defense,bonus_vitesse,bonus_taux_coup_critique,bonus_dommages_critiques,bonus_resistance,bonus_precision]

        for index in range(len(self.familles_de_bonus_possibles)):
            if(self.famille_de_bonus == self.familles_de_bonus_possibles[index]):
                bonus_stat_initial=bonus_possibles[index][qualite-1]

        return bonus_stat_initial

    # A n'appeler que si la rune n'est pas de niveau 15
    def trouver_prochain_bonus_stat_principale(self,famille_bonus,qualite):
        bonus_hp=[45,60,75,90,105,120]
        bonus_pourcentage_hp=[0.01,0.01,0.02,0.0215,0.0245,0.03]
        bonus_attaque=[3,4,5,6,7,8]
        bonus_pourcentage_attaque=[0.01,0.01,0.02,0.0215,0.0245,0.03]
        bonus_defense=[3,4,5,6,7,8]
        bonus_pourcentage_defense=[0.01,0.01,0.02,0.0215,0.0245,0.03]
        bonus_vitesse=[1,1,1.33,1.5,2,2]
        bonus_taux_coup_critique=[0.01,0.01,0.02,0.0215,0.0245,0.03]
        bonus_dommages_critiques=[0.01,0.02,0.225,0.03,0.0333,0.04]
        bonus_resistance=[0.01,0.01,0.02,0.0215,0.0245,0.03]
        bonus_precision=[0.01,0.01,0.02,0.0215,0.0245,0.03]

        bonus_possibles=[bonus_hp,bonus_pourcentage_hp,bonus_attaque,bonus_pourcentage_attaque,bonus_defense,bonus_pourcentage_defense,bonus_vitesse,bonus_taux_coup_critique,bonus_dommages_critiques,bonus_resistance,bonus_precision]
        bonus_stat_principale=0

        for index in range(len(self.familles_de_bonus_possibles)):
            if(self.famille_de_bonus == self.familles_de_bonus_possibles[index]):
                bonus_stat_principale=bonus_possibles[index][qualite-1]

        return bonus_stat_principale

    def trouver_bonus_stat_final(self,famille_bonus,qualite):
        bonus_hp=[804,1092,1380,1704,2088,2448]
        bonus_pourcentage_hp=[0.18,0.19,0.38,0.43,0.51,0.63]
        bonus_attaque=[54,73,92,112,135,160]
        bonus_pourcentage_attaque=[0.18,0.19,0.38,0.43,0.51,0.63]
        bonus_defense=[54,73,92,112,135,160]
        bonus_pourcentage_defense=[0.18,0.19,0.38,0.43,0.51,0.63]
        bonus_vitesse=[18,19,25,30,39,42]
        bonus_taux_coup_critique=[0.18,0.19,0.37,0.42,0.47,0.58]
        bonus_dommages_critiques=[0.19,0.37,0.43,0.57,0.65,0.80]
        bonus_resistance=[0.18,0.19,0.38,0.44,0.51,0.64]
        bonus_precision=[0.18,0.19,0.38,0.44,0.51,0.64]

        bonus_possibles=[bonus_hp,bonus_pourcentage_hp,bonus_attaque,bonus_pourcentage_attaque,bonus_defense,bonus_pourcentage_defense,bonus_vitesse,bonus_taux_coup_critique,bonus_dommages_critiques,bonus_resistance,bonus_precision]

        for index in range(len(self.familles_de_bonus_possibles)):
            if(self.famille_de_bonus == self.familles_de_bonus_possibles[index]):
                bonus_stat_final=bonus_possibles[index][qualite-1]

        return bonus_stat_final


    def ameliorer(self):
        if(self.niveau!=15):
            pourcentages_reussite_amelioration=[100,100,100,85,70,60,50,40,30,25,20,15,10,8,5]
            pourcentage_reussite=pourcentages_reussite_amelioration[self.niveau]
            reussite=random.randint(1,100)
            if(reussite <= pourcentage_reussite):
                print('\nAmélioration réussie!!\n')
                self.niveau+=1
                if(self.niveau!=15):
                    for index in range(len(self.familles_de_bonus_possibles)):
                        if(self.famille_de_bonus == self.familles_de_bonus_possibles[index]):
                            self.gains[index]+=self.prochain_bonus_stat_principale
                    self.prochain_bonus_stat_principale=self.trouver_prochain_bonus_stat_principale(self.famille_de_bonus,self.qualite_numerique)

                    if((self.niveau%3)==0):
                        self.ajouter_stat_secondaire()
                else:
                    for index in range(len(self.familles_de_bonus_possibles)):
                        if(self.famille_de_bonus == self.familles_de_bonus_possibles[index]):
                            self.gains[index]=self.trouver_bonus_stat_final(self.famille_de_bonus,self.qualite_numerique)
                
                print('Rune après amélioration : \n')
                print(self)
            else:
                print('Dommage.. L\'Amélioration a échoué... \n')
        else:
            print('Cette rune a déjà été améliorée au maximum. \n')


    def creer_stat_secondaire(self):
        bornes_min_pv=[15,30,45,60,90,135]
        bornes_min_pourcentage_pv=[0.01,0.01,0.02,0.03,0.04,0.05]
        bornes_min_attaque=[1,2,3,4,8,10]
        bornes_min_pourcentage_attaque=[0.01,0.01,0.02,0.03,0.04,0.05]
        bornes_min_defense=[1,2,3,4,8,10]
        bornes_min_pourcentage_defense=[0.01,0.01,0.02,0.03,0.04,0.05]
        bornes_min_vitesse=[1,1,1,2,3,4]
        bornes_min_taux_coup_critique=[0.01,0.01,0.01,0.02,0.03,0.04]
        bornes_min_dommages_critiques=[0.01,0.01,0.02,0.02,0.03,0.04]
        bornes_min_resistance=[0.01,0.01,0.02,0.02,0.03,0.04]
        bornes_min_precision=[0.01,0.01,0.02,0.02,0.03,0.04]
        bornes_min=[bornes_min_pv,bornes_min_pourcentage_pv,bornes_min_attaque,bornes_min_pourcentage_attaque,bornes_min_defense,bornes_min_pourcentage_defense,bornes_min_vitesse,bornes_min_taux_coup_critique,bornes_min_dommages_critiques,bornes_min_resistance,bornes_min_precision]

        bornes_max_pv=[60,105,165,225,300,375]
        bornes_max_pourcentage_pv=[0.02,0.03,0.05,0.06,0.07,0.08]
        bornes_max_attaque=[4,5,8,10,15,20]
        bornes_max_pourcentage_attaque=[0.02,0.03,0.05,0.06,0.07,0.08]
        bornes_max_defense=[4,5,8,10,15,20]
        bornes_max_pourcentage_defense=[0.02,0.03,0.05,0.06,0.07,0.08]
        bornes_max_vitesse=[1,2,3,4,5,6]
        bornes_max_taux_coup_critique=[0.02,0.03,0.03,0.04,0.05,0.06]
        bornes_max_dommages_critiques=[0.02,0.03,0.04,0.05,0.05,0.06]
        bornes_max_resistance=[0.02,0.03,0.04,0.05,0.07,0.08]
        bornes_max_precision=[0.02,0.03,0.04,0.05,0.07,0.08]
        bornes_max=[bornes_max_pv,bornes_max_pourcentage_pv,bornes_max_attaque,bornes_max_pourcentage_attaque,bornes_max_defense,bornes_max_pourcentage_defense,bornes_max_vitesse,bornes_max_taux_coup_critique,bornes_max_dommages_critiques,bornes_max_resistance,bornes_max_precision]

        indice_stat_secondaire=random.randint(0,10)
        stat_secondaire=self.familles_de_bonus_possibles[indice_stat_secondaire]
        bonus_stat=random.randint(bornes_min[indice_stat_secondaire][self.qualite_numerique-1]*10000,bornes_max[indice_stat_secondaire][self.qualite_numerique-1]*10000)/10000

        for index in range(len(self.familles_de_bonus_possibles)):
            if(stat_secondaire == self.familles_de_bonus_possibles[index]):
                self.gains[index] += bonus_stat

        index=0
        while(self.presence_bonus_secondaires[index]==1):
            index+=1
        self.presence_bonus_secondaires[index]=1
        self.bonus_secondaires[index]=[stat_secondaire,bonus_stat]

    def ajouter_stat_secondaire(self):
        if((self.rarete == 'Normale') or (self.rarete=='Magique' and self.niveau == 6) or (self.rarete == 'Rare' and self.niveau == 9) or (self.rarete == 'Héroïque' and self.niveau == 12)):
            self.creer_stat_secondaire()
        else:
            bonus_a_ameliorer=self.bonus_secondaires[random.randint(1,len(self.bonus_secondaires))-1]
            gain=self.trouver_prochain_bonus_stat_principale(bonus_a_ameliorer[0],self.qualite_numerique)
            bonus_a_ameliorer[1]+=gain

            for index in range(len(self.familles_de_bonus_possibles)):
                if(bonus_a_ameliorer[0] == self.familles_de_bonus_possibles[index]):
                    self.gains[index] += gain










    def equiper(self,monstre):
        positions=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']        

        for index in range(len(positions)):
            if(self.position == positions[index] and monstre.equipement[index] == 0):
                monstre.equipement[index]=self # avec self la rune à équiper
                # Rajouter les gains des bonus secondaires 
                for index_bonus in range(len(monstre.bonus_de_runes)):
                    monstre.bonus_de_runes[index_bonus]+=self.gains[index_bonus]
            elif(self.position == positions[index]):
                print('\n',monstre.surnom,' est déjà équipé(e) d\'une rune à cette position... \n')

        monstre.afficher_equipement_monstre_complet()
        print(monstre,'\n\n')


    # Dans cette fonction on assume que la position de la rune correspond avec l'indice donné
    def equiper_sans_affichage(self,monstre,indice):
        positions=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']

        if (monstre.equipement[indice] == 0 and self != 0 and self.position == positions[indice]):
            monstre.equipement[indice]=self
            for index_bonus in range(len(monstre.bonus_de_runes)):
                monstre.bonus_de_runes[index_bonus]+=self.gains[index_bonus]


        # Runes.bonus_de_runes(monstre)

