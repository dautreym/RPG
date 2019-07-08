# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:41:34 2019

@author: marin
"""

''' if need help : https://programmation360.com/programmation-orientee-objet-python/ '''


import sys
import random
import math
from ast import literal_eval


class Objets:
    def __init__(self,NOM):
        self.type='Objet_courant'
        self.nom=NOM
        if(NOM=='Parchemin d invocation'):
            self.taux_reussite_une_etoile=74.2
            self.taux_reussite_deux_etoiles=24.4
            self.taux_reussite_trois_etoiles=1.4
            self.prix_d_achat=3900
            self.prix_de_vente=2000
            self.prix_d_utilisation=300
        if(NOM=='Parchemin d invocation superieure'):
            self.taux_reussite_trois_etoiles=92.4
            self.taux_reussite_quatre_etoiles=7.3
            self.taux_reussite_cinq_etoiles=0.4
            self.prix_d_achat=115000
            self.prix_de_vente=60000
            self.prix_d_utilisation=10000
        if(NOM=='Parchemin d invocation ultra superieure'):
            self.taux_reussite_trois_etoiles=91.5
            self.taux_reussite_quatre_etoiles=8
            self.taux_reussite_cinq_etoiles=0.5
            self.prix_d_achat=145000
            self.prix_de_vente=75000
            self.prix_d_utilisation=10000
        if(NOM=='Parchemin d invocation fusion'):
            self.taux_reussite_trois_etoiles=91.5
            self.taux_reussite_quatre_etoiles=8
            self.taux_reussite_cinq_etoiles=0.5
        if(NOM=='Parchemin d invocation interdite'):
            self.taux_reussite_trois_etoiles=50
            self.taux_reussite_quatre_etoiles=31.25
            self.taux_reussite_cinq_etoiles=18.75
        if(NOM=='Parchemin d invocation legendaire'):
            self.taux_reussite_quatre_etoiles=93.9
            self.taux_reussite_cinq_etoiles=6.1
            self.prix_d_utilisation=50000
        if(NOM=='Parchemin d invocation divine'):
            self.prix_d_utilisation=100000

        if(NOM=='Parchemin d invocation Inugami d Eau'):
            self.prix_d_utilisation=3000
        if(NOM=='Parchemin d invocation Mastodonte de Ténèbres'):
            self.prix_d_utilisation=3000
        if(NOM=='Parchemin d invocation Golem de Feu'):
            self.prix_d_utilisation=3000

    def utiliser(objet,base):
        reussite=random.randint(1,100)
        reussite_apres_virgule=(random.randint(1,100))/100
        reussite+=reussite_apres_virgule
        if(objet.nom=='Parchemin d invocation'):
            if(reussite<=objet.taux_reussite_trois_etoiles):
                creature=Base.invoquer(base,3)
            elif(reussite>objet.taux_reussite_une_etoile):
                creature=Base.invoquer(base,1)
            else:
                creature=Base.invoquer(base,2)
        if(objet.nom=='Parchemin d invocation superieure'):
            if(reussite<=objet.taux_reussite_cinq_etoiles):
                creature=Base.invoquer(base,5)
            elif(reussite>objet.taux_reussite_trois_etoiles):
                creature=Base.invoquer(base,3)
            else:
                creature=Base.invoquer(base,4)
        if(objet.nom=='Parchemin d invocation ultra superieure'):
            if(reussite<=objet.taux_reussite_cinq_etoiles):
                creature=Base.invoquer(base,5)
            elif(reussite>objet.taux_reussite_trois_etoiles):
                creature=Base.invoquer(base,3)
            else:
                creature=Base.invoquer(base,4)
        if(objet.nom=='Parchemin d invocation fusion'):
            if(reussite<=objet.taux_reussite_cinq_etoiles):
                creature=Base.invoquer(base,5)
            elif(reussite>objet.taux_reussite_trois_etoiles):
                creature=Base.invoquer(base,3)
            else:
                creature=Base.invoquer(base,4)
        if(objet.nom=='Parchemin d invocation legendaire'):
            if(reussite<=objet.taux_reussite_cinq_etoiles):
                creature=Base.invoquer(base,5)
            else:
                creature=Base.invoquer(base,4)
        if(objet.nom=='Parchemin d invocation divine'):
            creature=Base.invoquer(base,5)

        if(objet.nom=='Parchemin d invocation Inugami d Eau'):
            creature=Base.invoquerDefini(base,'Inugami','Eau')
        if(objet.nom=='Parchemin d invocation Mastodonte de Ténèbres'):
            creature=Base.invoquerDefini(base,'Mastodonte','Ténèbres')
        if(objet.nom=='Parchemin d invocation Golem de Feu'):
            creature=Base.invoquerDefini(base,'Golem','Feu')

        return creature



class Runes:
    def __init__(self,NOM,CATEGORIE,POSITION,QUALITE,RARETE,BONUS):
        self.type='Rune'
        self.nom=NOM
        self.categorie=CATEGORIE
        self.niveau=0
        self.position=POSITION
        self.qualite=QUALITE
        self.rarete=RARETE
        if(RARETE=='Normale'):
            self.nb_bonus_stats_secondaires=0
        if(RARETE=='Magique'):
            self.nb_bonus_stats_secondaires=1
        if(RARETE=='Rare'):
            self.nb_bonus_stats_secondaires=2
        if(RARETE=='Héroïque'):
            self.nb_bonus_stats_secondaires=3
        if(RARETE=='Légendaire'):
            self.nb_bonus_stats_secondaires=4
        self.famille_de_bonus=BONUS

        self.premier_bonus_secondaire=[]
        self.presence_premier_bonus=0
        self.deuxieme_bonus_secondaire=[]
        self.presence_deuxieme_bonus=0
        self.troisieme_bonus_secondaire=[]
        self.presence_troisieme_bonus=0
        self.quatrieme_bonus_secondaire=[]
        self.presence_quatrieme_bonus=0
        self.bonus_secondaires=[self.premier_bonus_secondaire,self.deuxieme_bonus_secondaire,self.troisieme_bonus_secondaire,self.quatrieme_bonus_secondaire]

        if (self.qualite=='I'):
            self.qualite_numerique=1
        if (self.qualite=='II'):
            self.qualite_numerique=2
        if (self.qualite=='III'):
            self.qualite_numerique=3
        if (self.qualite=='IV'):
            self.qualite_numerique=4
        if (self.qualite=='V'):
            self.qualite_numerique=5
        if (self.qualite=='VI'):
            self.qualite_numerique=6

        if(BONUS=='HP+'):
            self.gain_en_pv=Runes.Trouver_bonus_stat_initial(BONUS,self.qualite_numerique)
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
        if(BONUS=='HP%'):
            self.gain_en_pourcentage_de_pv=Runes.Trouver_bonus_stat_initial(BONUS,self.qualite_numerique)
            self.gain_en_pv=0
            self.gain_en_attaque=0
            self.gain_en_pourcentage_de_attaque=0
            self.gain_en_defense=0
            self.gain_en_pourcentage_de_defense=0
            self.gain_en_vitesse=0
            self.gain_en_taux_de_coup_critique=0
            self.gain_en_dommages_critiques=0
            self.gain_en_resistance=0
            self.gain_en_precision=0
        if(BONUS=='ATK+'):
            self.gain_en_attaque=Runes.Trouver_bonus_stat_initial(BONUS,self.qualite_numerique)
            self.gain_en_pv=0
            self.gain_en_pourcentage_de_pv=0
            self.gain_en_pourcentage_de_attaque=0
            self.gain_en_defense=0
            self.gain_en_pourcentage_de_defense=0
            self.gain_en_vitesse=0
            self.gain_en_taux_de_coup_critique=0
            self.gain_en_dommages_critiques=0
            self.gain_en_resistance=0
            self.gain_en_precision=0
        if(BONUS=='ATK%'):
            self.gain_en_pourcentage_de_attaque=Runes.Trouver_bonus_stat_initial(BONUS,self.qualite_numerique)
            self.gain_en_pv=0
            self.gain_en_pourcentage_de_pv=0
            self.gain_en_attaque=0
            self.gain_en_defense=0
            self.gain_en_pourcentage_de_defense=0
            self.gain_en_vitesse=0
            self.gain_en_taux_de_coup_critique=0
            self.gain_en_dommages_critiques=0
            self.gain_en_resistance=0
            self.gain_en_precision=0
        if(BONUS=='DEF+'):
            self.gain_en_defense=Runes.Trouver_bonus_stat_initial(BONUS,self.qualite_numerique)
            self.gain_en_pv=0
            self.gain_en_pourcentage_de_pv=0
            self.gain_en_attaque=0
            self.gain_en_pourcentage_de_attaque=0
            self.gain_en_pourcentage_de_defense=0
            self.gain_en_vitesse=0
            self.gain_en_taux_de_coup_critique=0
            self.gain_en_dommages_critiques=0
            self.gain_en_resistance=0
            self.gain_en_precision=0
        if(BONUS=='DEF%'):
            self.gain_en_pourcentage_de_defense=Runes.Trouver_bonus_stat_initial(BONUS,self.qualite_numerique)
            self.gain_en_pv=0
            self.gain_en_pourcentage_de_pv=0
            self.gain_en_attaque=0
            self.gain_en_pourcentage_de_attaque=0
            self.gain_en_defense=0
            self.gain_en_vitesse=0
            self.gain_en_taux_de_coup_critique=0
            self.gain_en_dommages_critiques=0
            self.gain_en_resistance=0
            self.gain_en_precision=0
        if(BONUS=='VIT+'):
            self.gain_en_vitesse=Runes.Trouver_bonus_stat_initial(BONUS,self.qualite_numerique)
            self.gain_en_pv=0
            self.gain_en_pourcentage_de_pv=0
            self.gain_en_attaque=0
            self.gain_en_pourcentage_de_attaque=0
            self.gain_en_defense=0
            self.gain_en_pourcentage_de_defense=0
            self.gain_en_taux_de_coup_critique=0
            self.gain_en_dommages_critiques=0
            self.gain_en_resistance=0
            self.gain_en_precision=0
        if(BONUS=='TCC%'):
            self.gain_en_taux_de_coup_critique=Runes.Trouver_bonus_stat_initial(BONUS,self.qualite_numerique)
            self.gain_en_pv=0
            self.gain_en_pourcentage_de_pv=0
            self.gain_en_attaque=0
            self.gain_en_pourcentage_de_attaque=0
            self.gain_en_defense=0
            self.gain_en_pourcentage_de_defense=0
            self.gain_en_vitesse=0
            self.gain_en_dommages_critiques=0
            self.gain_en_resistance=0
            self.gain_en_precision=0
        if(BONUS=='DC%'):
            self.gain_en_dommages_critiques=Runes.Trouver_bonus_stat_initial(BONUS,self.qualite_numerique)
            self.gain_en_pv=0
            self.gain_en_pourcentage_de_pv=0
            self.gain_en_attaque=0
            self.gain_en_pourcentage_de_attaque=0
            self.gain_en_defense=0
            self.gain_en_pourcentage_de_defense=0
            self.gain_en_vitesse=0
            self.gain_en_taux_de_coup_critique=0
            self.gain_en_resistance=0
            self.gain_en_precision=0
        if(BONUS=='RES%'):
            self.gain_en_resistance=Runes.Trouver_bonus_stat_initial(BONUS,self.qualite_numerique)
            self.gain_en_pv=0
            self.gain_en_pourcentage_de_pv=0
            self.gain_en_attaque=0
            self.gain_en_pourcentage_de_attaque=0
            self.gain_en_defense=0
            self.gain_en_pourcentage_de_defense=0
            self.gain_en_vitesse=0
            self.gain_en_taux_de_coup_critique=0
            self.gain_en_dommages_critiques=0
            self.gain_en_precision=0
        if(BONUS=='ACC%'):
            self.gain_en_precision=Runes.Trouver_bonus_stat_initial(BONUS,self.qualite_numerique)
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

        self.prochain_bonus_stat_principale=Runes.Trouver_prochain_bonus_stat_principale(BONUS,self.qualite_numerique)
        self.cout_prochaine_amelioration=Runes.Trouver_cout_prochaine_amelioration(self.qualite_numerique,0)
        self.prix_d_achat=1000*self.qualite_numerique


    def Initialiser(rune):
        for i in range(rune.nb_bonus_stats_secondaires):
            rune=Runes.Creer_stat_secondaire(rune)
        return rune

    def Reinitialiser(nom,categorie,position,qualite,rarete,bonus,niveau,bonus_secondaires,liste_des_gains):
        rune=Runes(nom,categorie,position,qualite,rarete,bonus)
        rune.niveau=niveau
        if(niveau!=15):
            rune.prochain_bonus_stat_principale=Runes.Trouver_prochain_bonus_stat_principale(bonus,rune.qualite_numerique)
            rune.cout_prochaine_amelioration=Runes.Trouver_cout_prochaine_amelioration(rune.qualite_numerique,rune.niveau)

        rune.gain_en_pv=liste_des_gains[0]
        rune.gain_en_pourcentage_de_pv=liste_des_gains[1]
        rune.gain_en_attaque=liste_des_gains[2]
        rune.gain_en_pourcentage_de_attaque=liste_des_gains[3]
        rune.gain_en_defense=liste_des_gains[4]
        rune.gain_en_pourcentage_de_defense=liste_des_gains[5]
        rune.gain_en_vitesse=liste_des_gains[6] # ici ?
        rune.gain_en_taux_de_coup_critique=liste_des_gains[7]
        rune.gain_en_dommages_critiques=liste_des_gains[8]
        rune.gain_en_resistance=liste_des_gains[9]
        rune.gain_en_precision=liste_des_gains[10]
        rune.bonus_secondaires=bonus_secondaires
        if(len(bonus_secondaires)>0 and bonus_secondaires[0]!=[]):
            rune.presence_premier_bonus=1
            rune.premier_bonus_secondaire=bonus_secondaires[0]
        if(len(bonus_secondaires)>1 and bonus_secondaires[1]!=[]):
            rune.presence_deuxieme_bonus=1
            rune.deuxieme_bonus_secondaire=bonus_secondaires[1]
        if(len(bonus_secondaires)>2 and bonus_secondaires[2]!=[]):
            rune.presence_troisieme_bonus=1
            rune.troisieme_bonus_secondaire=bonus_secondaires[2]
        if(len(bonus_secondaires)>3 and bonus_secondaires[3]!=[]):
            rune.presence_quatrieme_bonus=1
            rune.quatrieme_bonus_secondaire=bonus_secondaires[0]
        # Appliquer les bonus secondiares à gain_en_... ?
        return rune


    def __str__(self):
        return str(self.rarete)+' '+str(self.nom)+' niveau '+str(self.niveau)+'\n Catégorie : '+str(self.categorie)+'\n Position : '+str(self.position)+'\n Gain en PV : '+str(self.gain_en_pv)+'\n Gain en pourcentage de PV : '+str(self.gain_en_pourcentage_de_pv)+'%\n Gain en attaque : '+str(self.gain_en_attaque)+'\n Gain en pourcentage d\'attaque : '+str(self.gain_en_pourcentage_de_attaque)+'%\n Gain en défense : '+str(self.gain_en_defense)+'\n Gain en pourcentage de défense : '+str(self.gain_en_pourcentage_de_defense)+'%\n Gain en vitesse : '+str(self.gain_en_vitesse)+'\n Gain en taux de coup critique : '+str(self.gain_en_taux_de_coup_critique)+'%\n Gain en dommages critiques : '+str(self.gain_en_dommages_critiques)+'%\n Gain en résistance : '+str(self.gain_en_resistance)+'\n Gain en précision : '+str(self.gain_en_precision)+'\n'

    def Trouver_cout_prochaine_amelioration(qualite,niveau):
        couts_amelioration_LV1=[100,175,250,400,550,775,1000,1300,1600,2000,2400,2925,3450,4100,4750]
        couts_amelioration_LV2=[150,300,450,700,950,1275,1600,2025,2450,3000,3550,4225,4900,5700,6500]
        couts_amelioration_LV3=[225,475,725,1075,1425,1875,2325,2850,3375,4075,4775,5600,6425,7375,8325]
        couts_amelioration_LV4=[330,680,1030,1480,1930,2455,2980,3680,4380,5205,6030,6980,7930,9130,10330]
        couts_amelioration_LV5=[500,950,1400,1925,2450,3175,3900,4750,5600,6600,7600,8850,10100,11600,13100]
        couts_amelioration_LV6=[750,1475,2200,3050,3900,4875,5850,6975,8100,9350,10600,11975,13350,14850,16350]
        couts_amelioration=[couts_amelioration_LV1,couts_amelioration_LV2,couts_amelioration_LV3,couts_amelioration_LV4,couts_amelioration_LV5,couts_amelioration_LV6]
        cout_prochaine_amelioration=couts_amelioration[qualite-1][niveau]
        return cout_prochaine_amelioration

    def Trouver_bonus_stat_initial(famille_bonus,qualite):
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
        if(famille_bonus=='HP+'):
            bonus_stat_initial=bonus_hp[qualite-1]
        if(famille_bonus=='HP%'):
            bonus_stat_initial=bonus_pourcentage_hp[qualite-1]
        if(famille_bonus=='ATK+'):
            bonus_stat_initial=bonus_attaque[qualite-1]
        if(famille_bonus=='ATK%'):
            bonus_stat_initial=bonus_pourcentage_attaque[qualite-1]
        if(famille_bonus=='DEF+'):
            bonus_stat_initial=bonus_defense[qualite-1]
        if(famille_bonus=='DEF%'):
            bonus_stat_initial=bonus_pourcentage_defense[qualite-1]
        if(famille_bonus=='VIT+'):
            bonus_stat_initial=bonus_vitesse[qualite-1]
        if(famille_bonus=='TCC%'):
            bonus_stat_initial=bonus_taux_coup_critique[qualite-1]
        if(famille_bonus=='DC%'):
            bonus_stat_initial=bonus_dommages_critiques[qualite-1]
        if(famille_bonus=='RES%'):
            bonus_stat_initial=bonus_resistance[qualite-1]
        if(famille_bonus=='ACC%'):
            bonus_stat_initial=bonus_precision[qualite-1]
        return bonus_stat_initial

    ''' A n\'appeler que si la rune n\'est pas niveau 15 '''
    def Trouver_prochain_bonus_stat_principale(famille_bonus,qualite):
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
        if(famille_bonus=='HP+'):
            bonus_stat_principale=bonus_hp[qualite-1]
        if(famille_bonus=='HP%'):
            bonus_stat_principale=bonus_pourcentage_hp[qualite-1]
        if(famille_bonus=='ATK+'):
            bonus_stat_principale=bonus_attaque[qualite-1]
        if(famille_bonus=='ATK%'):
            bonus_stat_principale=bonus_pourcentage_attaque[qualite-1]
        if(famille_bonus=='DEF+'):
            bonus_stat_principale=bonus_defense[qualite-1]
        if(famille_bonus=='DEF%'):
            bonus_stat_principale=bonus_pourcentage_defense[qualite-1]
        if(famille_bonus=='VIT+'):
            bonus_stat_principale=bonus_vitesse[qualite-1]
        if(famille_bonus=='TCC%'):
            bonus_stat_principale=bonus_taux_coup_critique[qualite-1]
        if(famille_bonus=='DC%'):
            bonus_stat_principale=bonus_dommages_critiques[qualite-1]
        if(famille_bonus=='RES%'):
            bonus_stat_principale=bonus_resistance[qualite-1]
        if(famille_bonus=='ACC%'):
            bonus_stat_principale=bonus_precision[qualite-1]
        return bonus_stat_principale

    def Trouver_bonus_stat_final(famille_bonus,qualite):
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
        if(famille_bonus=='HP+'):
            bonus_stat_final=bonus_hp[qualite-1]
        if(famille_bonus=='HP%'):
            bonus_stat_final=bonus_pourcentage_hp[qualite-1]
        if(famille_bonus=='ATK+'):
            bonus_stat_final=bonus_attaque[qualite-1]
        if(famille_bonus=='ATK%'):
            bonus_stat_final=bonus_pourcentage_attaque[qualite-1]
        if(famille_bonus=='DEF+'):
            bonus_stat_final=bonus_defense[qualite-1]
        if(famille_bonus=='DEF%'):
            bonus_stat_final=bonus_pourcentage_defense[qualite-1]
        if(famille_bonus=='VIT+'):
            bonus_stat_final=bonus_vitesse[qualite-1]
        if(famille_bonus=='TCC%'):
            bonus_stat_final=bonus_taux_coup_critique[qualite-1]
        if(famille_bonus=='DC%'):
            bonus_stat_final=bonus_dommages_critiques[qualite-1]
        if(famille_bonus=='RES%'):
            bonus_stat_final=bonus_resistance[qualite-1]
        if(famille_bonus=='ACC%'):
            bonus_stat_final=bonus_precision[qualite-1]
        return bonus_stat_final


    def Ameliorer(rune):
        if(rune.niveau!=15):
            pourcentages_reussite_amelioration=[100,100,100,85,70,60,50,40,30,25,20,15,10,8,5]
            pourcentage_reussite=pourcentages_reussite_amelioration[rune.niveau]
            reussite=random.randint(1,100)
            if(reussite<=pourcentage_reussite):
                print('\nAmélioration réussie!!\n')
                rune.niveau+=1
                if(rune.niveau!=15):
                    Gain_stat_principale=rune.prochain_bonus_stat_principale
                    if(rune.famille_de_bonus=='HP+'):
                        rune.gain_en_pv+=Gain_stat_principale
                    if(rune.famille_de_bonus=='HP%'):
                        rune.gain_en_pourcentage_de_pv+=Gain_stat_principale
                    if(rune.famille_de_bonus=='ATK+'):
                        rune.gain_en_attaque+=Gain_stat_principale
                    if(rune.famille_de_bonus=='ATK%'):
                        rune.gain_en_pourcentage_de_attaque+=Gain_stat_principale
                    if(rune.famille_de_bonus=='DEF+'):
                        rune.gain_en_defense+=Gain_stat_principale
                    if(rune.famille_de_bonus=='DEF%'):
                        rune.gain_en_pourcentage_de_defense+=Gain_stat_principale
                    if(rune.famille_de_bonus=='VIT+'):
                        rune.gain_en_vitesse+=Gain_stat_principale
                    if(rune.famille_de_bonus=='TCC%'):
                        rune.gain_en_taux_de_coup_critique+=Gain_stat_principale
                    if(rune.famille_de_bonus=='DC%'):
                        rune.gain_en_dommages_critiques+=Gain_stat_principale
                    if(rune.famille_de_bonus=='RES%'):
                        rune.gain_en_resistance+=Gain_stat_principale
                    if(rune.famille_de_bonus=='ACC%'):
                        rune.gain_en_precision+=Gain_stat_principale
                    if((rune.niveau%3)==0):
                        rune=Runes.Ajouter_stat_secondaire(rune)
                else:
                    Gain_stat_principale=Runes.Trouver_bonus_stat_final(rune.famille_de_bonus,rune.qualite_numerique)
                    if(rune.famille_de_bonus=='HP+'):
                        rune.gain_en_pv=Gain_stat_principale
                    if(rune.famille_de_bonus=='HP%'):
                        rune.gain_en_pourcentage_de_pv=Gain_stat_principale
                    if(rune.famille_de_bonus=='ATK+'):
                        rune.gain_en_attaque=Gain_stat_principale
                    if(rune.famille_de_bonus=='ATK%'):
                        rune.gain_en_pourcentage_de_attaque=Gain_stat_principale
                    if(rune.famille_de_bonus=='DEF+'):
                        rune.gain_en_defense=Gain_stat_principale
                    if(rune.famille_de_bonus=='DEF%'):
                        rune.gain_en_pourcentage_de_defense=Gain_stat_principale
                    if(rune.famille_de_bonus=='VIT+'):
                        rune.gain_en_vitesse=Gain_stat_principale
                    if(rune.famille_de_bonus=='TCC%'):
                        rune.gain_en_taux_de_coup_critique=Gain_stat_principale
                    if(rune.famille_de_bonus=='DC%'):
                        rune.gain_en_dommages_critiques=Gain_stat_principale
                    if(rune.famille_de_bonus=='RES%'):
                        rune.gain_en_resistance=Gain_stat_principale
                    if(rune.famille_de_bonus=='ACC%'):
                        rune.gain_en_precision=Gain_stat_principale
                print('Rune après amélioration : \n')
                print(rune)
            else:
                print('Dommage.. L\'Amélioration a échoué... \n')
        else:
            print('Cette rune a déjà été améliorée au maximum. \n')
        return rune


    def Creer_stat_secondaire(rune):
        Bornes_min_pv=[15,30,45,60,90,135]
        Bornes_min_pourcentage_pv=[0.01,0.01,0.02,0.03,0.04,0.05]
        Bornes_min_attaque=[1,2,3,4,8,10]
        Bornes_min_pourcentage_attaque=[0.01,0.01,0.02,0.03,0.04,0.05]
        Bornes_min_defense=[1,2,3,4,8,10]
        Bornes_min_pourcentage_defense=[0.01,0.01,0.02,0.03,0.04,0.05]
        Bornes_min_vitesse=[1,1,1,2,3,4]
        Bornes_min_taux_coup_critique=[0.01,0.01,0.01,0.02,0.03,0.04]
        Bornes_min_dommages_critiques=[0.01,0.01,0.02,0.02,0.03,0.04]
        Bornes_min_resistance=[0.01,0.01,0.02,0.02,0.03,0.04]
        Bornes_min_precision=[0.01,0.01,0.02,0.02,0.03,0.04]
        Bornes_min=[Bornes_min_pv,Bornes_min_pourcentage_pv,Bornes_min_attaque,Bornes_min_pourcentage_attaque,Bornes_min_defense,Bornes_min_pourcentage_defense,Bornes_min_vitesse,Bornes_min_taux_coup_critique,Bornes_min_dommages_critiques,Bornes_min_resistance,Bornes_min_precision]

        Bornes_max_pv=[60,105,165,225,300,375]
        Bornes_max_pourcentage_pv=[0.02,0.03,0.05,0.06,0.07,0.08]
        Bornes_max_attaque=[4,5,8,10,15,20]
        Bornes_max_pourcentage_attaque=[0.02,0.03,0.05,0.06,0.07,0.08]
        Bornes_max_defense=[4,5,8,10,15,20]
        Bornes_max_pourcentage_defense=[0.02,0.03,0.05,0.06,0.07,0.08]
        Bornes_max_vitesse=[1,2,3,4,5,6]
        Bornes_max_taux_coup_critique=[0.02,0.03,0.03,0.04,0.05,0.06]
        Bornes_max_dommages_critiques=[0.02,0.03,0.04,0.05,0.05,0.06]
        Bornes_max_resistance=[0.02,0.03,0.04,0.05,0.07,0.08]
        Bornes_max_precision=[0.02,0.03,0.04,0.05,0.07,0.08]
        Bornes_max=[Bornes_max_pv,Bornes_max_pourcentage_pv,Bornes_max_attaque,Bornes_max_pourcentage_attaque,Bornes_max_defense,Bornes_max_pourcentage_defense,Bornes_max_vitesse,Bornes_max_taux_coup_critique,Bornes_max_dommages_critiques,Bornes_max_resistance,Bornes_max_precision]

        Stats=['HP+','HP%','ATK+','ATK%','DEF+','DEF%','VIT+','TCC%','DC%','RES%','ACC%']
        Indice_stat_secondaire=random.randint(0,10)
        Stat_secondaire=Stats[Indice_stat_secondaire]
        Bonus_stat=random.randint(Bornes_min[Indice_stat_secondaire][rune.qualite_numerique-1]*10000,Bornes_max[Indice_stat_secondaire][rune.qualite_numerique-1]*10000)/10000

        if(Stat_secondaire=='HP+'):
            rune.gain_en_pv+=Bonus_stat
        if(Stat_secondaire=='HP%'):
            rune.gain_en_pourcentage_de_pv+=Bonus_stat
        if(Stat_secondaire=='ATK+'):
            rune.gain_en_attaque+=Bonus_stat
        if(Stat_secondaire=='ATK%'):
            rune.gain_en_pourcentage_de_attaque+=Bonus_stat
        if(Stat_secondaire=='DEF+'):
            rune.gain_en_defense+=Bonus_stat
        if(Stat_secondaire=='DEF%'):
            rune.gain_en_pourcentage_de_defense+=Bonus_stat
        if(Stat_secondaire=='VIT+'):
            rune.gain_en_vitesse+=Bonus_stat
        if(Stat_secondaire=='TCC%'):
            rune.gain_en_taux_de_coup_critique+=Bonus_stat
        if(Stat_secondaire=='DC%'):
            rune.gain_en_dommages_critiques+=Bonus_stat
        if(Stat_secondaire=='RES%'):
            rune.gain_en_resistance+=Bonus_stat
        if(Stat_secondaire=='ACC%'):
            rune.gain_en_precision+=Bonus_stat

        if(rune.presence_premier_bonus==1):
            if(rune.presence_deuxieme_bonus==1):
                if(rune.presence_troisieme_bonus==1):
                    rune.presence_quatrieme_bonus=1
                    rune.quatrieme_bonus_secondaire=[Stat_secondaire,Bonus_stat]
                else:
                    rune.presence_troisieme_bonus=1
                    rune.troisieme_bonus_secondaire=[Stat_secondaire,Bonus_stat]
            else:
                rune.presence_deuxieme_bonus=1
                rune.deuxieme_bonus_secondaire=[Stat_secondaire,Bonus_stat]
        else:
            rune.presence_premier_bonus=1
            rune.premier_bonus_secondaire=[Stat_secondaire,Bonus_stat]

        return rune

    def Ajouter_stat_secondaire(rune):
        if((rune.rarete=='Normale') or (rune.rarete=='Magique' and rune.niveau>=6) or (rune.rarete=='Rare' and rune.niveau>=9) or (rune.rarete=='Héroïque' and rune.niveau>=12)):
            rune=Runes.Creer_stat_secondaire(rune)
        else:
            bonus_a_ameliorer=rune.bonus_secondaires[random.randint(1,len(rune.bonus_secondaires))-1]
            gain=Runes.Trouver_prochain_bonus_stat_principale(bonus_a_ameliorer[0],rune.qualite_numerique)
            bonus_a_ameliorer[1]+=gain
            if(bonus_a_ameliorer[0]=='HP+'):
                rune.gain_en_pv+=gain
            if(bonus_a_ameliorer[0]=='HP%'):
                rune.gain_en_pourcentage_de_pv+=gain
            if(bonus_a_ameliorer[0]=='ATK+'):
                rune.gain_en_attaque+=gain
            if(bonus_a_ameliorer[0]=='ATK%'):
                rune.gain_en_pourcentage_de_attaque+=gain
            if(bonus_a_ameliorer[0]=='DEF+'):
                rune.gain_en_defense+=gain
            if(bonus_a_ameliorer[0]=='DEF%'):
                rune.gain_en_pourcentage_de_defense+=gain
            if(bonus_a_ameliorer[0]=='VIT+'):
                rune.gain_en_vitesse+=gain
            if(bonus_a_ameliorer[0]=='TCC%'):
                rune.gain_en_taux_de_coup_critique+=gain
            if(bonus_a_ameliorer[0]=='DC%'):
                rune.gain_en_dommages_critiques+=gain
            if(bonus_a_ameliorer[0]=='RES%'):
                rune.gain_en_resistance+=gain
            if(bonus_a_ameliorer[0]=='ACC%'):
                rune.gain_en_precision+=gain
        return rune



    def equiper(Rune,monstre):
        # monstre=Runes.BonusDeRunes(monstre)
        if(Rune.position=='rune_haut'):
            if(monstre.equipement_rune_haut==0):
                monstre.equipement_rune_haut=Rune
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')

        if(Rune.position=='rune_haut_droite'):
            if(monstre.equipement_rune_haut_droite==0):
                monstre.equipement_rune_haut_droite=Rune
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')

        if(Rune.position=='rune_bas_droite'):
            if(monstre.equipement_rune_bas_droite==0):
                monstre.equipement_rune_bas_droite=Rune
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')

        if(Rune.position=='rune_bas'):
            if(monstre.equipement_rune_bas==0):
                monstre.equipement_rune_bas=Rune
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')

        if(Rune.position=='rune_bas_gauche'):
            if(monstre.equipement_rune_bas_gauche==0):
                monstre.equipement_rune_bas_gauche=Rune
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')

        if(Rune.position=='rune_haut_gauche'):
            if(monstre.equipement_rune_haut_gauche==0):
                monstre.equipement_rune_haut_gauche=Rune
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')
        # monstre=Runes.BonusDeRunes(monstre)
        Runes.afficher_equipement_monstre_complet(monstre)


    def Equiper_sans_affichage(monstre,Rune,indice):
        # monstre=Runes.MalusDeRunes(monstre)
        if(indice==0):
            if(monstre.equipement_rune_haut==0):
                monstre.equipement_rune_haut=Rune
                if(Rune!=0):
                    monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                    monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                    monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                    monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                    monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                    monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                    monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                    monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                    monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                    monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                    monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')

        if(indice==1):
            if(monstre.equipement_rune_haut_droite==0):
                monstre.equipement_rune_haut_droite=Rune
                if(Rune!=0):
                    monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                    monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                    monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                    monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                    monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                    monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                    monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                    monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                    monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                    monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                    monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')

        if(indice==2):
            if(monstre.equipement_rune_bas_droite==0):
                monstre.equipement_rune_bas_droite=Rune
                if(Rune!=0):
                    monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                    monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                    monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                    monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                    monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                    monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                    monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                    monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                    monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                    monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                    monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')

        if(indice==3):
            if(monstre.equipement_rune_bas==0):
                monstre.equipement_rune_bas=Rune
                if(Rune!=0):
                    monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                    monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                    monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                    monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                    monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                    monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                    monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                    monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                    monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                    monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                    monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')

        if(indice==4):
            if(monstre.equipement_rune_bas_gauche==0):
                monstre.equipement_rune_bas_gauche=Rune
                if(Rune!=0):
                    monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                    monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                    monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                    monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                    monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                    monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                    monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                    monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                    monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                    monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                    monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')

        if(indice==5):
            if(monstre.equipement_rune_haut_gauche==0):
                monstre.equipement_rune_haut_gauche=Rune
                if(Rune!=0):
                    monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                    monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                    monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                    monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                    monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                    monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                    monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                    monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                    monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                    monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                    monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision
            else:
                print('\n',monstre.surnom,' est déjà équipé(e) d une rune à cette position... \n')

        # monstre=Runes.BonusDeRunes(monstre)
        return monstre


    def Equiper_sans_affichage_special(monstre,Rune,indice):
        # monstre=Runes.MalusDeRunes(monstre)
        if(indice==0):
            monstre.equipement_rune_haut=Rune
            if(Rune!=0):
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision

        if(indice==1):
            monstre.equipement_rune_haut_droite=Rune
            if(Rune!=0):
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision

        if(indice==2):
            monstre.equipement_rune_bas_droite=Rune
            if(Rune!=0):
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision

        if(indice==3):
            monstre.equipement_rune_bas=Rune
            if(Rune!=0):
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision

        if(indice==4):
            monstre.equipement_rune_bas_gauche=Rune
            if(Rune!=0):
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision

        if(indice==5):
            monstre.equipement_rune_haut_gauche=Rune
            if(Rune!=0):
                monstre.bonus_de_runes_en_pv+=Rune.gain_en_pv
                monstre.bonus_de_runes_en_pourcentage_de_pv+=Rune.gain_en_pourcentage_de_pv
                monstre.bonus_de_runes_en_attaque+=Rune.gain_en_attaque
                monstre.bonus_de_runes_en_pourcentage_de_attaque+=Rune.gain_en_pourcentage_de_attaque
                monstre.bonus_de_runes_en_defense+=Rune.gain_en_defense
                monstre.bonus_de_runes_en_pourcentage_de_defense+=Rune.gain_en_pourcentage_de_defense
                monstre.bonus_de_runes_en_vitesse+=Rune.gain_en_vitesse
                monstre.bonus_de_runes_en_taux_de_coup_critique+=Rune.gain_en_taux_de_coup_critique
                monstre.bonus_de_runes_en_dommages_critiques+=Rune.gain_en_dommages_critiques
                monstre.bonus_de_runes_en_resistance+=Rune.gain_en_resistance
                monstre.bonus_de_runes_en_precision+=Rune.gain_en_precision

        # monstre=Runes.BonusDeRunes(monstre)
        return monstre



    def BonusDeRunes(monstre):
        types_runes_equipees=[]
        if(monstre.equipement_rune_haut!=0):
            types_runes_equipees.append(monstre.equipement_rune_haut.categorie)
        if(monstre.equipement_rune_haut_droite!=0):
            types_runes_equipees.append(monstre.equipement_rune_haut_droite.categorie)
        if(monstre.equipement_rune_bas_droite!=0):
            types_runes_equipees.append(monstre.equipement_rune_bas_droite.categorie)
        if(monstre.equipement_rune_bas!=0):
            types_runes_equipees.append(monstre.equipement_rune_bas.categorie)
        if(monstre.equipement_rune_bas_gauche!=0):
            types_runes_equipees.append(monstre.equipement_rune_bas_gauche.categorie)
        if(monstre.equipement_rune_haut_gauche!=0):
            types_runes_equipees.append(monstre.equipement_rune_haut_gauche.categorie)

        '''
        monstre.pv-=Arrondir(monstre.bonus_de_runes_en_pv+monstre.pv*monstre.bonus_de_runes_en_pourcentage_de_pv)
        monstre.attaque-=Arrondir(monstre.bonus_de_runes_en_attaque+monstre.attaque*monstre.bonus_de_runes_en_pourcentage_de_attaque)
        monstre.defense-=Arrondir(monstre.bonus_de_runes_en_defense+monstre.defense*monstre.bonus_de_runes_en_pourcentage_de_defense)
        monstre.vitesse-=Arrondir(monstre.bonus_de_runes_en_vitesse)
        monstre.taux_coup_critique-=Arrondir_au_centieme(monstre.bonus_de_runes_en_taux_de_coup_critique)
        monstre.dommages_critiques-=Arrondir_au_centieme(monstre.bonus_de_runes_en_dommages_critiques)
        monstre.resistance-=Arrondir_au_centieme(monstre.bonus_de_runes_en_resistance)
        monstre.precision-=Arrondir_au_centieme(monstre.bonus_de_runes_en_precision)
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
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Energie'):
                    compteur_Energie+=1
        if (compteur_Energie>=2):
            if(compteur_Energie>=4):
                if(compteur_Energie==6):
                    bonus_energie=0.45
                else:
                    bonus_energie=0.3
            else:
                bonus_energie=0.15
        else:
            bonus_energie=0
        monstre.bonus_de_runes_en_pourcentage_de_pv+=bonus_energie

        if ('Colere' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Colere'):
                    compteur_Colere+=1
        if (compteur_Colere>=4):
            bonus_colere=0.35
        else:
            bonus_colere=0
        monstre.bonus_de_runes_en_pourcentage_de_attaque+=bonus_colere


        if ('Tenace' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Tenace'):
                    compteur_Tenace+=1
        if (compteur_Tenace>=2):
            if(compteur_Tenace>=4):
                if(compteur_Tenace==6):
                    bonus_tenacite=0.45
                else:
                    bonus_tenacite=0.3
            else:
                bonus_tenacite=0.15
        else:
            bonus_tenacite=0
        monstre.bonus_de_runes_en_pourcentage_de_defense+=bonus_tenacite


        if ('Veloce' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Veloce'):
                    compteur_Veloce+=1
        if(compteur_Veloce>=4):
            bonus_velocite=0.25
        else:
            bonus_velocite=0
        monstre.bonus_de_runes_en_vitesse+=Arrondir(bonus_velocite*monstre.vitesse)


        if ('Lame' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Lame'):
                    compteur_Lame+=1
        if (compteur_Lame>=2):
            if(compteur_Lame>=4):
                if(compteur_Lame==6):
                    bonus_lame=0.36
                else:
                    bonus_lame=0.24
            else:
                bonus_lame=0.12
        else:
            bonus_lame=0
        monstre.bonus_de_runes_en_taux_de_coup_critique+=bonus_lame


        if ('Rage' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Rage'):
                    compteur_Rage+=1
        if(compteur_Rage>=4):
            bonus_dommages_critiques=0.4
        else:
            bonus_dommages_critiques=0
        monstre.bonus_de_runes_en_dommages_critiques+=bonus_dommages_critiques


        if ('Precision' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Precision'):
                    compteur_Sniper+=1
        if (compteur_Sniper>=2):
            if(compteur_Sniper>=4):
                if(compteur_Sniper==6):
                    bonus_precision=0.6
                else:
                    bonus_precision=0.4
            else:
                bonus_precision=0.2
        else:
            bonus_precision=0
        monstre.bonus_de_runes_en_precision+=bonus_precision


        if ('Resistance' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Resistance'):
                    compteur_Illumination+=1
        if (compteur_Illumination>=2):
            if(compteur_Illumination>=4):
                if(compteur_Illumination==6):
                    bonus_resistance=0.6
                else:
                    bonus_resistance=0.4
            else:
                bonus_resistance=0.2
        else:
            bonus_resistance=0
        monstre.bonus_de_runes_en_resistance+=bonus_resistance


        if ('Vengeance' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Vengeance'):
                    compteur_Vengeance+=1
        if (compteur_Vengeance>=2):
            if(compteur_Vengeance>=4):
                if(compteur_Vengeance==6):
                    bonus_vengeance=0.6
                else:
                    bonus_vengeance=0.4
            else:
                bonus_vengeance=0.2
        else:
            bonus_vengeance=0
        monstre.bonus_de_runes_en_taux_contre_attaque+=bonus_vengeance


        if ('Volonté' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Volonté'):
                    compteur_Volonte+=1
        if (compteur_Volonte>=2):
            if(compteur_Volonte>=4):
                if(compteur_Volonte==6):
                    bonus_immunite=4
                else:
                    bonus_immunite=3
            else:
                bonus_immunite=2
        else:
            bonus_immunite=0
        if(bonus_immunite!=0):
            monstre.bonus_de_runes_en_immunite=1
            monstre.bonus_de_runes_en_tours_immunite=max(bonus_immunite,monstre.bonus_de_runes_en_tours_immunite)


        if ('Vampirique' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Vampirique'):
                    compteur_Vampirique+=1
        if(compteur_Illumination>=4):
            bonus_vol_de_vie=35
        else:
            bonus_vol_de_vie=0
        monstre.bonus_de_runes_en_vol_de_vie+=bonus_vol_de_vie


        if ('Desespoir' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Desespoir'):
                    compteur_Desespoir+=1
        if(compteur_Desespoir>=4):
            bonus_chances_de_stun=0.25
        else:
            bonus_chances_de_stun=0
        monstre.bonus_de_runes_en_chances_de_stun+=bonus_chances_de_stun


        if ('Violence' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Violence'):
                    compteur_Violence+=1
        if(compteur_Violence>=4):
            bonus_chances_tour_supplementaire=0.22
        else:
            bonus_chances_tour_supplementaire=0
        monstre.bonus_de_runes_en_chances_tour_supplementaire+=bonus_chances_tour_supplementaire


        if ('Transcendance' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Transcendance'):
                    compteur_Transcendance+=1
        if(compteur_Transcendance==6):
            bonus_transcendance=0.15
        else:
            bonus_transcendance=0
        monstre.bonus_de_runes_en_pourcentage_de_pv+=bonus_transcendance
        monstre.bonus_de_runes_en_pourcentage_de_attaque+=bonus_transcendance
        monstre.bonus_de_runes_en_pourcentage_de_defense+=bonus_transcendance
        monstre.bonus_de_runes_en_vitesse+=Arrondir(bonus_transcendance*monstre.vitesse)
        monstre.bonus_de_runes_en_taux_de_coup_critique+=bonus_transcendance
        monstre.bonus_de_runes_en_dommages_critiques+=bonus_transcendance
        monstre.bonus_de_runes_en_precision+=bonus_transcendance
        monstre.bonus_de_runes_en_resistance+=bonus_transcendance


        if ('Extase' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Extase'):
                    compteur_Extase+=1
        if(compteur_Extase==6):
            monstre.bonus_de_runes_en_tour_supplementaire+=1


        if ('Destruction' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Destruction'):
                    compteur_Destruction+=1
        if (compteur_Destruction>=2):
            if(compteur_Destruction>=4):
                if(compteur_Destruction==6):
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
        monstre.bonus_de_runes_en_pourcentage_de_attaque+=bonus_attaque
        monstre.bonus_de_runes_en_vitesse+=Arrondir(bonus_vitesse*monstre.vitesse)


        if ('Domination' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Domination'):
                    compteur_Domination+=1
        if (compteur_Domination>=2):
            if(compteur_Domination>=4):
                if(compteur_Domination==6):
                    bonus_immortalite=4
                else:
                    bonus_immortalite=3
            else:
                bonus_immortalite=2
        else:
            bonus_immortalite=0
        if(bonus_immortalite!=0):
            monstre.bonus_de_runes_en_immortalite=1
            monstre.bonus_de_runes_en_tours_immortalite=max(bonus_immortalite,monstre.bonus_de_runes_en_tours_immortalite)


        if ('Inébranlable' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Inébranlable'):
                    compteur_Inebranlable+=1
        if(compteur_Inebranlable==6):
            monstre.bonus_de_runes_en_immunite=1


        if ('Détermination' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Détermination'):
                    compteur_Determination+=1
        if(compteur_Determination==6):
            monstre.determination=1


        if ('Incandescence' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Incandescence'):
                    compteur_Incandescence+=1
        if (compteur_Incandescence>=2):
            if(compteur_Incandescence>=4):
                if(compteur_Incandescence==6):
                    bonus_incandescence=4
                else:
                    bonus_incandescence=3
            else:
                bonus_incandescence=2
        else:
            bonus_incandescence=0
        if(bonus_incandescence>0):
            monstre.incandescence=1
            monstre.niveau_incandescence=bonus_incandescence


        if ('Sublimation' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Sublimation'):
                    compteur_Sublimation+=1
        if (compteur_Sublimation>=2):
            if(compteur_Sublimation>=4):
                if(compteur_Sublimation==6):
                    bonus_recup=0.45
                else:
                    bonus_recup=0.3
            else:
                bonus_recup=0.15
        else:
            bonus_recup=0
        monstre.bonus_de_runes_en_regeneration+=bonus_recup


        '''
        monstre.pv+=Arrondir(monstre.bonus_de_runes_en_pv+monstre.pv*monstre.bonus_de_runes_en_pourcentage_de_pv)
        monstre.attaque+=Arrondir(monstre.bonus_de_runes_en_attaque+monstre.attaque*monstre.bonus_de_runes_en_pourcentage_de_attaque)
        monstre.defense+=Arrondir(monstre.bonus_de_runes_en_defense+monstre.defense*monstre.bonus_de_runes_en_pourcentage_de_defense)
        monstre.vitesse+=Arrondir(monstre.bonus_de_runes_en_vitesse)
        monstre.taux_coup_critique+=Arrondir_au_centieme(monstre.bonus_de_runes_en_taux_de_coup_critique)
        monstre.dommages_critiques+=Arrondir_au_centieme(monstre.bonus_de_runes_en_dommages_critiques)
        monstre.resistance+=Arrondir_au_centieme(monstre.bonus_de_runes_en_resistance)
        monstre.precision+=Arrondir_au_centieme(monstre.bonus_de_runes_en_precision)
        '''

        monstre.pv_actuels=monstre.pv
        monstre.attaque_actuelle=monstre.attaque
        monstre.defense_actuelle=monstre.defense
        monstre.vitesse_actuelle=monstre.vitesse
        monstre.taux_coup_critique_actuel=monstre.taux_coup_critique
        monstre.dommages_critiques_actuels=monstre.dommages_critiques
        monstre.resistance_actuelle=monstre.resistance
        monstre.precision_actuelle=monstre.precision

        return monstre

    def MalusDeRunes(monstre):
        types_runes_equipees=[]
        if(monstre.equipement_rune_haut!=0):
            types_runes_equipees.append(monstre.equipement_rune_haut.categorie)
        if(monstre.equipement_rune_haut_droite!=0):
            types_runes_equipees.append(monstre.equipement_rune_haut_droite.categorie)
        if(monstre.equipement_rune_bas_droite!=0):
            types_runes_equipees.append(monstre.equipement_rune_bas_droite.categorie)
        if(monstre.equipement_rune_bas!=0):
            types_runes_equipees.append(monstre.equipement_rune_bas.categorie)
        if(monstre.equipement_rune_bas_gauche!=0):
            types_runes_equipees.append(monstre.equipement_rune_bas_gauche.categorie)
        if(monstre.equipement_rune_haut_gauche!=0):
            types_runes_equipees.append(monstre.equipement_rune_haut_gauche.categorie)

        '''
        monstre.pv-=Arrondir(monstre.bonus_de_runes_en_pv+monstre.pv*monstre.bonus_de_runes_en_pourcentage_de_pv)
        monstre.attaque-=Arrondir(monstre.bonus_de_runes_en_attaque+monstre.attaque*monstre.bonus_de_runes_en_pourcentage_de_attaque)
        monstre.defense-=Arrondir(monstre.bonus_de_runes_en_defense+monstre.defense*monstre.bonus_de_runes_en_pourcentage_de_defense)
        monstre.vitesse-=Arrondir(monstre.bonus_de_runes_en_vitesse)
        monstre.taux_coup_critique-=Arrondir_au_centieme(monstre.bonus_de_runes_en_taux_de_coup_critique)
        monstre.dommages_critiques-=Arrondir_au_centieme(monstre.bonus_de_runes_en_dommages_critiques)
        monstre.resistance-=Arrondir_au_centieme(monstre.bonus_de_runes_en_resistance)
        monstre.precision-=Arrondir_au_centieme(monstre.bonus_de_runes_en_precision)
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
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Energie'):
                    compteur_Energie+=1
        if (compteur_Energie>=2):
            if(compteur_Energie>=4):
                if(compteur_Energie==6):
                    bonus_energie=0.45
                else:
                    bonus_energie=0.3
            else:
                bonus_energie=0.15
        else:
            bonus_energie=0
        monstre.bonus_de_runes_en_pourcentage_de_pv-=bonus_energie


        if ('Colere' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Colere'):
                    compteur_Colere+=1
        if (compteur_Colere>=4):
            bonus_colere=0.35
        else:
            bonus_colere=0
        monstre.bonus_de_runes_en_pourcentage_de_attaque-=bonus_colere


        if ('Tenace' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Tenace'):
                    compteur_Tenace+=1
        if (compteur_Tenace>=2):
            if(compteur_Tenace>=4):
                if(compteur_Tenace==6):
                    bonus_tenacite=0.45
                else:
                    bonus_tenacite=0.3
            else:
                bonus_tenacite=0.15
        else:
            bonus_tenacite=0
        monstre.bonus_de_runes_en_pourcentage_de_defense-=bonus_tenacite


        if ('Veloce' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Veloce'):
                    compteur_Veloce+=1
        if(compteur_Veloce>=4):
            bonus_velocite=0.25
        else:
            bonus_velocite=0
        monstre.bonus_de_runes_en_vitesse-=Arrondir(bonus_velocite*monstre.vitesse)


        if ('Lame' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Lame'):
                    compteur_Lame+=1
        if (compteur_Lame>=2):
            if(compteur_Lame>=4):
                if(compteur_Lame==6):
                    bonus_lame=0.36
                else:
                    bonus_lame=0.24
            else:
                bonus_lame=0.12
        else:
            bonus_lame=0
        monstre.bonus_de_runes_en_taux_de_coup_critique-=bonus_lame


        if ('Rage' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Rage'):
                    compteur_Rage+=1
        if(compteur_Rage>=4):
            bonus_dommages_critiques=0.4
        else:
            bonus_dommages_critiques=0
        monstre.bonus_de_runes_en_dommages_critiques-=bonus_dommages_critiques


        if ('Precision' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Precision'):
                    compteur_Sniper+=1
        if (compteur_Sniper>=2):
            if(compteur_Sniper>=4):
                if(compteur_Sniper==6):
                    bonus_precision=0.6
                else:
                    bonus_precision=0.4
            else:
                bonus_precision=0.2
        else:
            bonus_precision=0
        monstre.bonus_de_runes_en_precision-=bonus_precision


        if ('Resistance' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Resistance'):
                    compteur_Illumination+=1
        if (compteur_Illumination>=2):
            if(compteur_Illumination>=4):
                if(compteur_Illumination==6):
                    bonus_resistance=0.6
                else:
                    bonus_resistance=0.4
            else:
                bonus_resistance=0.2
        else:
            bonus_resistance=0
        monstre.bonus_de_runes_en_resistance-=bonus_resistance


        if ('Vengeance' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Vengeance'):
                    compteur_Vengeance+=1
        if (compteur_Vengeance>=2):
            if(compteur_Vengeance>=4):
                if(compteur_Vengeance==6):
                    bonus_vengeance=0.6
                else:
                    bonus_vengeance=0.4
            else:
                bonus_vengeance=0.2
        else:
            bonus_vengeance=0
        monstre.bonus_de_runes_en_taux_contre_attaque-=bonus_vengeance


        if ('Volonté' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Volonté'):
                    compteur_Volonte+=1
        if (compteur_Volonte>=2):
            if(compteur_Volonte>=4):
                if(compteur_Volonte==6):
                    bonus_immunite=4
                else:
                    bonus_immunite=3
            else:
                bonus_immunite=2
        else:
            bonus_immunite=0
        if(bonus_immunite!=0):
            monstre.bonus_de_runes_en_immunite=0
            monstre.bonus_de_runes_en_tours_immunite=0


        if ('Vampirique' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Vampirique'):
                    compteur_Vampirique+=1
        if(compteur_Illumination>=4):
            bonus_vol_de_vie=35
        else:
            bonus_vol_de_vie=0
        monstre.bonus_de_runes_en_vol_de_vie-=bonus_vol_de_vie


        if ('Desespoir' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Desespoir'):
                    compteur_Desespoir+=1
        if(compteur_Desespoir>=4):
            bonus_chances_de_stun=0.25
        else:
            bonus_chances_de_stun=0
        monstre.bonus_de_runes_en_chances_de_stun-=bonus_chances_de_stun


        if ('Violence' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Violence'):
                    compteur_Violence+=1
        if(compteur_Violence>=4):
            bonus_chances_tour_supplementaire=0.22
        else:
            bonus_chances_tour_supplementaire=0
        monstre.bonus_de_runes_en_chances_tour_supplementaire-=bonus_chances_tour_supplementaire


        if ('Transcendance' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Transcendance'):
                    compteur_Transcendance+=1
        if(compteur_Transcendance==6):
            bonus_transcendance=0.15
        else:
            bonus_transcendance=0
        monstre.bonus_de_runes_en_pourcentage_de_pv-=bonus_transcendance
        monstre.bonus_de_runes_en_pourcentage_de_attaque-=bonus_transcendance
        monstre.bonus_de_runes_en_pourcentage_de_defense-=bonus_transcendance
        monstre.bonus_de_runes_en_vitesse-=Arrondir(bonus_transcendance*monstre.vitesse)
        monstre.bonus_de_runes_en_taux_de_coup_critique-=bonus_transcendance
        monstre.bonus_de_runes_en_dommages_critiques-=bonus_transcendance
        monstre.bonus_de_runes_en_precision-=bonus_transcendance
        monstre.bonus_de_runes_en_resistance-=bonus_transcendance


        if ('Extase' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Extase'):
                    compteur_Extase+=1
        if(compteur_Extase==6):
            monstre.bonus_de_runes_en_tour_supplementaire-=1


        if ('Destruction' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Destruction'):
                    compteur_Destruction+=1
        if (compteur_Destruction>=2):
            if(compteur_Destruction>=4):
                if(compteur_Destruction==6):
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
        monstre.bonus_de_runes_en_pourcentage_de_attaque-=bonus_attaque
        monstre.bonus_de_runes_en_vitesse-=Arrondir(bonus_vitesse*monstre.vitesse)


        if ('Domination' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Domination'):
                    compteur_Domination+=1
        if (compteur_Domination>=2):
            if(compteur_Domination>=4):
                if(compteur_Domination==6):
                    bonus_immortalite=4
                else:
                    bonus_immortalite=3
            else:
                bonus_immortalite=2
        else:
            bonus_immortalite=0
        if(bonus_immortalite!=0):
            monstre.bonus_de_runes_en_immortalite=0
            monstre.bonus_de_runes_en_tours_immortalite=0


        if ('Inébranlable' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Inébranlable'):
                    compteur_Inebranlable+=1
        if(compteur_Inebranlable==6):
            monstre.bonus_de_runes_en_immunite=0


        if ('Détermination' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Détermination'):
                    compteur_Determination+=1
        if(compteur_Determination==6):
            monstre.determination=0


        if ('Incandescence' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Incandescence'):
                    compteur_Incandescence+=0
        if (compteur_Incandescence>=2):
            if(compteur_Incandescence>=4):
                if(compteur_Incandescence==6):
                    bonus_incandescence=4
                else:
                    bonus_incandescence=3
            else:
                bonus_incandescence=2
        else:
            bonus_incandescence=0
        if(bonus_incandescence>0):
            monstre.incandescence=0
            monstre.niveau_incandescence=0


        if ('Sublimation' in types_runes_equipees):
            for i in range(len(types_runes_equipees)):
                if (types_runes_equipees[i]=='Sublimation'):
                    compteur_Sublimation+=1
        if (compteur_Sublimation>=2):
            if(compteur_Sublimation>=4):
                if(compteur_Sublimation==6):
                    bonus_recup=0.45
                else:
                    bonus_recup=0.3
            else:
                bonus_recup=0.15
        else:
            bonus_recup=0
        monstre.bonus_de_runes_en_regeneration-=bonus_recup


        '''
        monstre.pv+=Arrondir(monstre.bonus_de_runes_en_pv+monstre.pv*monstre.bonus_de_runes_en_pourcentage_de_pv)
        monstre.attaque+=Arrondir(monstre.bonus_de_runes_en_attaque+monstre.attaque*monstre.bonus_de_runes_en_pourcentage_de_attaque)
        monstre.defense+=Arrondir(monstre.bonus_de_runes_en_defense+monstre.defense*monstre.bonus_de_runes_en_pourcentage_de_defense)
        monstre.vitesse+=Arrondir(monstre.bonus_de_runes_en_vitesse)
        monstre.taux_coup_critique+=Arrondir_au_centieme(monstre.bonus_de_runes_en_taux_de_coup_critique)
        monstre.dommages_critiques+=Arrondir_au_centieme(monstre.bonus_de_runes_en_dommages_critiques)
        monstre.resistance+=Arrondir_au_centieme(monstre.bonus_de_runes_en_resistance)
        monstre.precision+=Arrondir_au_centieme(monstre.bonus_de_runes_en_precision)
        '''

        monstre.pv_actuels=monstre.pv
        monstre.attaque_actuelle=monstre.attaque
        monstre.defense_actuelle=monstre.defense
        monstre.vitesse_actuelle=monstre.vitesse
        monstre.taux_coup_critique_actuel=monstre.taux_coup_critique
        monstre.dommages_critiques_actuels=monstre.dommages_critiques
        monstre.resistance_actuelle=monstre.resistance
        monstre.precision_actuelle=monstre.precision

        return monstre


    def Desequiper(base,sac):
        print('\nLa rune déséquipée retournera dans la partie equipement du sac.\n')
        possibilites_monstres=[]
        possibilites_runes=[]
        i=1
        while(i<=base.place_dernier_monstre):
            print(base.stockage[i],' = ',i)
            possibilites_monstres.append(i)
            i+=1
        entree=input('De quel monstre voulez-vous modifier l\'équipement ? ')
        while(not IsSecure(entree)):
            entree=input('De quel monstre voulez-vous modifier l\'équipement ? ')
        place_monstre_choisi=int(entree)
        while(place_monstre_choisi not in possibilites_monstres):
            entree=input('De quel monstre voulez-vous modifier l\'équipement ? ')
            while(not IsSecure(entree)):
                entree=input('De quel monstre voulez-vous modifier l\'équipement ? ')
            place_monstre_choisi=int(entree)
        monstre_choisi=base.stockage[place_monstre_choisi]

        monstre_choisi=Runes.MalusDeRunes(monstre_choisi)

        '''
        monstre_choisi.pv-=Arrondir(monstre_choisi.bonus_de_runes_en_pv+monstre_choisi.pv*monstre_choisi.bonus_de_runes_en_pourcentage_de_pv)
        monstre_choisi.attaque-=Arrondir(monstre_choisi.bonus_de_runes_en_attaque+monstre_choisi.attaque*monstre_choisi.bonus_de_runes_en_pourcentage_de_attaque)
        monstre_choisi.defense-=Arrondir(monstre_choisi.bonus_de_runes_en_defense+monstre_choisi.defense*monstre_choisi.bonus_de_runes_en_pourcentage_de_defense)
        monstre_choisi.vitesse-=Arrondir(monstre_choisi.bonus_de_runes_en_vitesse)
        monstre_choisi.taux_coup_critique-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_taux_de_coup_critique)
        monstre_choisi.dommages_critiques-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_dommages_critiques)
        monstre_choisi.resistance-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_resistance)
        monstre_choisi.precision-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_precision)
        '''

        print('\n\n')
        if(monstre_choisi.equipement_rune_haut!=0):
            print('La rune du haut de ',monstre_choisi.surnom,' est : \n',monstre_choisi.equipement_rune_haut,'\n Pour la déséquiper, rentrez 0 \n')
            possibilites_runes.append(0)
        if(monstre_choisi.equipement_rune_haut_droite!=0):
            print('La rune en haut à droite de ',monstre_choisi.surnom,' est : \n',monstre_choisi.equipement_rune_haut_droite,'\n Pour la déséquiper, rentrez 1 \n')
            possibilites_runes.append(1)
        if(monstre_choisi.equipement_rune_bas_droite!=0):
            print('La rune en bas à droite de ',monstre_choisi.surnom,' est : \n',monstre_choisi.equipement_rune_bas_droite,'\n Pour la déséquiper, rentrez 2 \n')
            possibilites_runes.append(2)
        if(monstre_choisi.equipement_rune_bas!=0):
            print('La rune du bas de ',monstre_choisi.surnom,' est : \n',monstre_choisi.equipement_rune_bas,'\n Pour la déséquiper, rentrez 3 \n')
            possibilites_runes.append(3)
        if(monstre_choisi.equipement_rune_bas_gauche!=0):
            print('La rune en bas à gauche de ',monstre_choisi.surnom,' est : \n',monstre_choisi.equipement_rune_bas_gauche,'\n Pour la déséquiper, rentrez 4 \n')
            possibilites_runes.append(4)
        if(monstre_choisi.equipement_rune_haut_gauche!=0):
            print('La rune en haut à gauche de ',monstre_choisi.surnom,' est : \n',monstre_choisi.equipement_rune_haut_gauche,'\n Pour la déséquiper, rentrez 5 \n')
            possibilites_runes.append(5)

        if(len(possibilites_runes)==0):
            print('Vous ne pouvez déséquiper aucune rune car aucune rune n\'est équipée.')
        else:
            entree=input('Quelle rune voulez-vous déséquiper ? ')
            while(not IsSecure(entree)):
                entree=input('Quelle rune voulez-vous déséquiper ? ')
            place_rune_choisie=int(entree)
            while(place_rune_choisie not in possibilites_runes):
                entree=input('Quelle rune voulez-vous déséquiper ? ')
                while(not IsSecure(entree)):
                    entree=input('Quelle rune voulez-vous déséquiper ? ')
                place_rune_choisie=int(entree)
            if(place_rune_choisie==0):
                Rune_supprimee=monstre_choisi.equipement_rune_haut
            if(place_rune_choisie==1):
                Rune_supprimee=monstre_choisi.equipement_rune_haut_droite
            if(place_rune_choisie==2):
                Rune_supprimee=monstre_choisi.equipement_rune_bas_droite
            if(place_rune_choisie==3):
                Rune_supprimee=monstre_choisi.equipement_rune_bas
            if(place_rune_choisie==4):
                Rune_supprimee=monstre_choisi.equipement_rune_bas_gauche
            if(place_rune_choisie==5):
                Rune_supprimee=monstre_choisi.equipement_rune_haut_gauche

            monstre_choisi.bonus_de_runes_en_pv-=Rune_supprimee.gain_en_pv
            monstre_choisi.bonus_de_runes_en_pourcentage_de_pv-=Rune_supprimee.gain_en_pourcentage_de_pv
            monstre_choisi.bonus_de_runes_en_attaque-=Rune_supprimee.gain_en_attaque
            monstre_choisi.bonus_de_runes_en_pourcentage_de_attaque-=Rune_supprimee.gain_en_pourcentage_de_attaque
            monstre_choisi.bonus_de_runes_en_defense-=Rune_supprimee.gain_en_defense
            monstre_choisi.bonus_de_runes_en_pourcentage_de_defense-=Rune_supprimee.gain_en_pourcentage_de_defense
            monstre_choisi.bonus_de_runes_en_vitesse-=Rune_supprimee.gain_en_vitesse
            monstre_choisi.bonus_de_runes_en_taux_de_coup_critique-=Rune_supprimee.gain_en_taux_de_coup_critique
            monstre_choisi.bonus_de_runes_en_dommages_critiques-=Rune_supprimee.gain_en_dommages_critiques
            monstre_choisi.bonus_de_runes_en_resistance-=Rune_supprimee.gain_en_resistance
            monstre_choisi.bonus_de_runes_en_precision-=Rune_supprimee.gain_en_precision

            if(place_rune_choisie==0):
                monstre_choisi.equipement_rune_haut=0
            if(place_rune_choisie==1):
                monstre_choisi.equipement_rune_haut_droite=0
            if(place_rune_choisie==2):
                monstre_choisi.equipement_rune_bas_droite=0
            if(place_rune_choisie==3):
                monstre_choisi.equipement_rune_bas=0
            if(place_rune_choisie==4):
                monstre_choisi.equipement_rune_bas_gauche=0
            if(place_rune_choisie==5):
                monstre_choisi.equipement_rune_haut_gauche=0

        monstre_choisi=Runes.BonusDeRunes(monstre_choisi)

        '''
        monstre_choisi.pv+=Arrondir(monstre_choisi.bonus_de_runes_en_pv+monstre_choisi.pv*monstre_choisi.bonus_de_runes_en_pourcentage_de_pv)
        monstre_choisi.attaque+=Arrondir(monstre_choisi.bonus_de_runes_en_attaque+monstre_choisi.attaque*monstre_choisi.bonus_de_runes_en_pourcentage_de_attaque)
        monstre_choisi.defense+=Arrondir(monstre_choisi.bonus_de_runes_en_defense+monstre_choisi.defense*monstre_choisi.bonus_de_runes_en_pourcentage_de_defense)
        monstre_choisi.vitesse+=Arrondir(monstre_choisi.bonus_de_runes_en_vitesse)
        monstre_choisi.taux_coup_critique+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_taux_de_coup_critique)
        monstre_choisi.dommages_critiques+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_dommages_critiques)
        monstre_choisi.resistance+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_resistance)
        monstre_choisi.precision+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_precision)
        '''

        monstre_choisi.pv_actuels=monstre_choisi.pv
        monstre_choisi.attaque_actuelle=monstre_choisi.attaque
        monstre_choisi.defense_actuelle=monstre_choisi.defense
        monstre_choisi.vitesse_actuelle=monstre_choisi.vitesse
        monstre_choisi.taux_coup_critique_actuel=monstre_choisi.taux_coup_critique
        monstre_choisi.dommages_critiques_actuels=monstre_choisi.dommages_critiques
        monstre_choisi.resistance_actuelle=monstre_choisi.resistance
        monstre_choisi.precision_actuelle=monstre_choisi.precision

        Runes.afficher_equipement_monstre_complet(monstre_choisi)
        print(monstre_choisi)

        Inventaire.ajouter_objet(sac,Rune_supprimee)


    def Desequiper_sans_affichage(monstre_choisi,place_rune_choisie):
        monstre_choisi=Runes.MalusDeRunes(monstre_choisi)

        '''
        monstre_choisi.pv-=Arrondir(monstre_choisi.bonus_de_runes_en_pv+monstre_choisi.pv*monstre_choisi.bonus_de_runes_en_pourcentage_de_pv)
        monstre_choisi.attaque-=Arrondir(monstre_choisi.bonus_de_runes_en_attaque+monstre_choisi.attaque*monstre_choisi.bonus_de_runes_en_pourcentage_de_attaque)
        monstre_choisi.defense-=Arrondir(monstre_choisi.bonus_de_runes_en_defense+monstre_choisi.defense*monstre_choisi.bonus_de_runes_en_pourcentage_de_defense)
        monstre_choisi.vitesse-=Arrondir(monstre_choisi.bonus_de_runes_en_vitesse)
        monstre_choisi.taux_coup_critique-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_taux_de_coup_critique)
        monstre_choisi.dommages_critiques-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_dommages_critiques)
        monstre_choisi.resistance-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_resistance)
        monstre_choisi.precision-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_precision)
        '''

        if(place_rune_choisie==0):
            Rune_supprimee=monstre_choisi.equipement_rune_haut
        if(place_rune_choisie==1):
            Rune_supprimee=monstre_choisi.equipement_rune_haut_droite
        if(place_rune_choisie==2):
            Rune_supprimee=monstre_choisi.equipement_rune_bas_droite
        if(place_rune_choisie==3):
            Rune_supprimee=monstre_choisi.equipement_rune_bas
        if(place_rune_choisie==4):
            Rune_supprimee=monstre_choisi.equipement_rune_bas_gauche
        if(place_rune_choisie==5):
            Rune_supprimee=monstre_choisi.equipement_rune_haut_gauche

        if(Rune_supprimee!=0):
            monstre_choisi.bonus_de_runes_en_pv-=Rune_supprimee.gain_en_pv
            monstre_choisi.bonus_de_runes_en_pourcentage_de_pv-=Rune_supprimee.gain_en_pourcentage_de_pv
            monstre_choisi.bonus_de_runes_en_attaque-=Rune_supprimee.gain_en_attaque
            monstre_choisi.bonus_de_runes_en_pourcentage_de_attaque-=Rune_supprimee.gain_en_pourcentage_de_attaque
            monstre_choisi.bonus_de_runes_en_defense-=Rune_supprimee.gain_en_defense
            monstre_choisi.bonus_de_runes_en_pourcentage_de_defense-=Rune_supprimee.gain_en_pourcentage_de_defense
            monstre_choisi.bonus_de_runes_en_vitesse-=Rune_supprimee.gain_en_vitesse
            monstre_choisi.bonus_de_runes_en_taux_de_coup_critique-=Rune_supprimee.gain_en_taux_de_coup_critique
            monstre_choisi.bonus_de_runes_en_dommages_critiques-=Rune_supprimee.gain_en_dommages_critiques
            monstre_choisi.bonus_de_runes_en_resistance-=Rune_supprimee.gain_en_resistance
            monstre_choisi.bonus_de_runes_en_precision-=Rune_supprimee.gain_en_precision

            if(place_rune_choisie==0):
                monstre_choisi.equipement_rune_haut=0
            if(place_rune_choisie==1):
                monstre_choisi.equipement_rune_haut_droite=0
            if(place_rune_choisie==2):
                monstre_choisi.equipement_rune_bas_droite=0
            if(place_rune_choisie==3):
                monstre_choisi.equipement_rune_bas=0
            if(place_rune_choisie==4):
                monstre_choisi.equipement_rune_bas_gauche=0
            if(place_rune_choisie==5):
                monstre_choisi.equipement_rune_haut_gauche=0

        monstre_choisi=Runes.BonusDeRunes(monstre_choisi)

        '''
        monstre_choisi.pv+=Arrondir(monstre_choisi.bonus_de_runes_en_pv+monstre_choisi.pv*monstre_choisi.bonus_de_runes_en_pourcentage_de_pv)
        monstre_choisi.attaque+=Arrondir(monstre_choisi.bonus_de_runes_en_attaque+monstre_choisi.attaque*monstre_choisi.bonus_de_runes_en_pourcentage_de_attaque)
        monstre_choisi.defense+=Arrondir(monstre_choisi.bonus_de_runes_en_defense+monstre_choisi.defense*monstre_choisi.bonus_de_runes_en_pourcentage_de_defense)
        monstre_choisi.vitesse+=Arrondir(monstre_choisi.bonus_de_runes_en_vitesse)
        monstre_choisi.taux_coup_critique+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_taux_de_coup_critique)
        monstre_choisi.dommages_critiques+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_dommages_critiques)
        monstre_choisi.resistance+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_resistance)
        monstre_choisi.precision+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_precision)
        '''

        monstre_choisi.pv_actuels=monstre_choisi.pv
        monstre_choisi.attaque_actuelle=monstre_choisi.attaque
        monstre_choisi.defense_actuelle=monstre_choisi.defense
        monstre_choisi.vitesse_actuelle=monstre_choisi.vitesse
        monstre_choisi.taux_coup_critique_actuel=monstre_choisi.taux_coup_critique
        monstre_choisi.dommages_critiques_actuels=monstre_choisi.dommages_critiques
        monstre_choisi.resistance_actuelle=monstre_choisi.resistance
        monstre_choisi.precision_actuelle=monstre_choisi.precision

        return Rune_supprimee


    def Modifier_equipement(base,sac):
        # Creer une rune vide
        # Remplir uniquement la catégorie pour bénéficier du BonusdeRunes en %
        # Tout faire avec ça
        # Remplacer la rune vide par la vraie une fois terminée pour bénéficier du +

        # REFAIRE EN PLUS SIMPLE SANS LA RUNE VIDE!!!!

        possibilites_monstres=[]
        possibilites_runes=[]
        i=1
        while(i<=base.place_dernier_monstre):
            print(base.stockage[i],' = ',i,'\n\n')
            possibilites_monstres.append(i)
            i+=1
        entree=input('Quel monstre voulez-vous équiper d\'une rune ? ')
        while(not IsSecure(entree)):
            entree=input('Quel monstre voulez-vous équiper d\'une rune ? ')
        place_monstre_choisi=int(entree)
        while(place_monstre_choisi not in possibilites_monstres):
            entree=input('Quel monstre voulez-vous équiper d\'une rune ? ')
            while(not IsSecure(entree)):
                entree=input('Quel monstre voulez-vous équiper d\'une rune ? ')
            place_monstre_choisi=int(entree)
        monstre_choisi=base.stockage[place_monstre_choisi]

        monstre_choisi=Runes.MalusDeRunes(monstre_choisi)

        '''
        monstre_choisi.pv-=Arrondir(monstre_choisi.bonus_de_runes_en_pv+monstre_choisi.pv*monstre_choisi.bonus_de_runes_en_pourcentage_de_pv)
        monstre_choisi.attaque-=Arrondir(monstre_choisi.bonus_de_runes_en_attaque+monstre_choisi.attaque*monstre_choisi.bonus_de_runes_en_pourcentage_de_attaque)
        monstre_choisi.defense-=Arrondir(monstre_choisi.bonus_de_runes_en_defense+monstre_choisi.defense*monstre_choisi.bonus_de_runes_en_pourcentage_de_defense)
        monstre_choisi.vitesse-=Arrondir(monstre_choisi.bonus_de_runes_en_vitesse)
        monstre_choisi.taux_coup_critique-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_taux_de_coup_critique)
        monstre_choisi.dommages_critiques-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_dommages_critiques)
        monstre_choisi.resistance-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_resistance)
        monstre_choisi.precision-=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_precision)
        '''

        print('\n\n')
        Runes.afficher_equipement_monstre_complet(monstre_choisi)
        print('\n\n')

        j=1
        while(j<=sac.place_dernier_equipement):
            Inventaire.Afficher_contenu_sac_zone_unique(sac,'equipement',j)
            possibilites_runes.append(j)
            j+=1
        if(len(possibilites_runes)==0):
            print('Vous n avez aucune rune en votre possession pour le moment.\n\n')
        else:
            entree=input('Quelle rune voulez-vous lui équiper ? ')
            while(not IsSecure(entree)):
                entree=input('Quelle rune voulez-vous lui équiper ? ')
            place_rune_choisie=int(entree)
            while(place_rune_choisie not in possibilites_runes):
                entree=input('Quelle rune voulez-vous lui équiper ? ')
                while(not IsSecure(entree)):
                    entree=input('Quelle rune voulez-vous lui équiper ? ')
                place_rune_choisie=int(entree)
            rune_choisie=sac.equipement[place_rune_choisie]
            position_rune_a_modifier=rune_choisie.position

            ''' Définition de rune vide : '''
            '''
            rune_vide=Runes('Rune vide',rune_choisie.categorie,rune_choisie.position,'I','Normale',rune_choisie.famille_de_bonus)
            rune_vide.gain_en_pv=0
            rune_vide.gain_en_pourcentage_de_pv=0
            rune_vide.gain_en_attaque=0
            rune_vide.gain_en_pourcentage_de_attaque=0
            rune_vide.gain_en_defense=0
            rune_vide.gain_en_pourcentage_de_defense=0
            rune_vide.gain_en_vitesse=0
            rune_vide.gain_en_taux_de_coup_critique=0
            rune_vide.gain_en_dommages_critiques=0
            rune_vide.gain_en_resistance=0
            rune_vide.gain_en_precision=0
            '''

            if(position_rune_a_modifier=='rune_haut'):
                if(monstre_choisi.equipement_rune_haut==0):
                    Runes.equiper(rune_choisie,monstre_choisi)
                else:
                    print(monstre_choisi.surnom,' est déjà équipe(e) de la rune : \n',monstre_choisi.equipement_rune_haut)
                    entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    while(not IsSecure(entree)):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    choix=int(entree)
                    while(choix!=0 and choix!=1):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        while(not IsSecure(entree)):
                            entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        choix=int(entree)
                    if(choix==0):
                        Runes.Desequiper_sans_affichage(monstre_choisi,0)
                        Runes.equiper(rune_choisie,monstre_choisi)
                #indice=0

            if(position_rune_a_modifier=='rune_haut_droite'):
                if(monstre_choisi.equipement_rune_haut_droite==0):
                    Runes.equiper(rune_choisie,monstre_choisi)
                else:
                    print(monstre_choisi.surnom,' est déjà équipe(e) de la rune : \n',monstre_choisi.equipement_rune_haut_droite)
                    entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    while(not IsSecure(entree)):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    choix=int(entree)
                    while(choix!=0 and choix!=1):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        while(not IsSecure(entree)):
                            entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        choix=int(entree)
                    if(choix==0):
                        Runes.Desequiper_sans_affichage(monstre_choisi,1)
                        Runes.equiper(rune_choisie,monstre_choisi)
                #indice=1

            if(position_rune_a_modifier=='rune_bas_droite'):
                if(monstre_choisi.equipement_rune_bas_droite==0):
                    Runes.equiper(rune_choisie,monstre_choisi)
                else:
                    print(monstre_choisi.surnom,' est déjà équipe(e) de la rune : \n',monstre_choisi.equipement_rune_bas_droite)
                    entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    while(not IsSecure(entree)):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    choix=int(entree)
                    while(choix!=0 and choix!=1):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        while(not IsSecure(entree)):
                            entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        choix=int(entree)
                    if(choix==0):
                        Runes.Desequiper_sans_affichage(monstre_choisi,2)
                        Runes.equiper(rune_choisie,monstre_choisi)
                #indice=2

            if(position_rune_a_modifier=='rune_bas'):
                if(monstre_choisi.equipement_rune_bas==0):
                    Runes.equiper(rune_choisie,monstre_choisi)
                else:
                    print(monstre_choisi.surnom,' est déjà équipe(e) de la rune : \n',monstre_choisi.equipement_rune_bas)
                    entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    while(not IsSecure(entree)):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    choix=int(entree)
                    while(choix!=0 and choix!=1):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        while(not IsSecure(entree)):
                            entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        choix=int(entree)
                    if(choix==0):
                        Runes.Desequiper_sans_affichage(monstre_choisi,3)
                        Runes.equiper(rune_choisie,monstre_choisi)
                #indice=3

            if(position_rune_a_modifier=='rune_bas_gauche'):
                if(monstre_choisi.equipement_rune_bas_gauche==0):
                    Runes.equiper(rune_choisie,monstre_choisi)
                else:
                    print(monstre_choisi.surnom,' est déjà équipe(e) de la rune : \n',monstre_choisi.equipement_rune_bas_gauche)
                    entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    while(not IsSecure(entree)):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    choix=int(entree)
                    while(choix!=0 and choix!=1):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        while(not IsSecure(entree)):
                            entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        choix=int(entree)
                    if(choix==0):
                        Runes.Desequiper_sans_affichage(monstre_choisi,4)
                        Runes.equiper(rune_choisie,monstre_choisi)
                #indice=4

            if(position_rune_a_modifier=='rune_haut_gauche'):
                if(monstre_choisi.equipement_rune_haut_gauche==0):
                    Runes.equiper(rune_choisie,monstre_choisi)
                else:
                    print(monstre_choisi.surnom,' est déjà équipe(e) de la rune : \n',monstre_choisi.equipement_rune_haut_gauche)
                    entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    while(not IsSecure(entree)):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                    choix=int(entree)
                    while(choix!=0 and choix!=1):
                        entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        while(not IsSecure(entree)):
                            entree=input('Cette rune précédemment équipée sera détruite. Pour ne pas la détruire, vous devriez la déséquiper avant de continuer. \nOui = 0 \nNon = 1 \nContinuer ? ')
                        choix=int(entree)
                    if(choix==0):
                        Runes.Desequiper_sans_affichage(monstre_choisi,5)
                        Runes.equiper(rune_choisie,monstre_choisi)
                #indice=5

            sac=Inventaire.supprimer_equipement_sans_affichage(sac,place_rune_choisie)

        monstre_choisi=Runes.BonusDeRunes(monstre_choisi)

        # Si au dessus on remplaçais toutes les rune_choisie par rune_vide, faire :
        # Runes.Equiper_sans_affichage_special(monstre_choisi,rune_choisie,indice)

        '''
        monstre_choisi.pv+=Arrondir(monstre_choisi.bonus_de_runes_en_pv+monstre_choisi.pv*monstre_choisi.bonus_de_runes_en_pourcentage_de_pv)
        monstre_choisi.attaque+=Arrondir(monstre_choisi.bonus_de_runes_en_attaque+monstre_choisi.attaque*monstre_choisi.bonus_de_runes_en_pourcentage_de_attaque)
        monstre_choisi.defense+=Arrondir(monstre_choisi.bonus_de_runes_en_defense+monstre_choisi.defense*monstre_choisi.bonus_de_runes_en_pourcentage_de_defense)
        monstre_choisi.vitesse+=Arrondir(monstre_choisi.bonus_de_runes_en_vitesse)
        monstre_choisi.taux_coup_critique+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_taux_de_coup_critique)
        monstre_choisi.dommages_critiques+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_dommages_critiques)
        monstre_choisi.resistance+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_resistance)
        monstre_choisi.precision+=Arrondir_au_centieme(monstre_choisi.bonus_de_runes_en_precision)
        '''

        monstre_choisi.pv_actuels=monstre_choisi.pv
        monstre_choisi.attaque_actuelle=monstre_choisi.attaque
        monstre_choisi.defense_actuelle=monstre_choisi.defense
        monstre_choisi.vitesse_actuelle=monstre_choisi.vitesse
        monstre_choisi.taux_coup_critique_actuel=monstre_choisi.taux_coup_critique
        monstre_choisi.dommages_critiques_actuels=monstre_choisi.dommages_critiques
        monstre_choisi.resistance_actuelle=monstre_choisi.resistance
        monstre_choisi.precision_actuelle=monstre_choisi.precision

        print(monstre_choisi)


    def afficher_equipement_monstre(monstre,position):
        print('\n')
        if (position=='rune_haut'):
            if (monstre.equipement_rune_haut!=0):
                print('La rune du haut de ',monstre.surnom,'est :',monstre.equipement_rune_haut,'\n')
            else:
                print('Vous n avez aucune rune d équipée en haut pour le moment.\n')
        if (position=='rune_haut_droite'):
            if (monstre.equipement_rune_haut_droite!=0):
                print('La rune en haut à droite de ',monstre.surnom,'est :',monstre.equipement_rune_haut_droite,'\n')
            else:
                print('Vous n avez aucune rune d équipée en haut à droite pour le moment.\n')
        if (position=='rune_bas_droite'):
            if (monstre.equipement_rune_bas_droite!=0):
                print('La rune en bas à droite de ',monstre.surnom,'est :',monstre.equipement_rune_bas_droite,'\n')
            else:
                print('Vous n avez aucune rune d équipée en bas à droite pour le moment.\n')
        if (position=='rune_bas'):
            if (monstre.equipement_rune_bas!=0):
                print('La rune du bas de ',monstre.surnom,'est :',monstre.equipement_rune_bas,'\n')
            else:
                print('Vous n avez aucune rune d équipée en bas pour le moment.\n')
        if (position=='rune_bas_gauche'):
            if (monstre.equipement_rune_bas_gauche!=0):
                print('La rune en bas à gauche de ',monstre.surnom,'est :',monstre.equipement_rune_bas_gauche,'\n')
            else:
                print('Vous n avez aucune rune d équipée en bas à gauche pour le moment.\n')
        if (position=='rune_haut_gauche'):
            if (monstre.equipement_rune_haut_gauche!=0):
                print('La rune en haut à gauche de ',monstre.surnom,'est :',monstre.equipement_rune_haut_gauche,'\n')
            else:
                print('Vous n avez aucune rune d équipée en haut à gauche pour le moment.\n')
        print('\n')

    def afficher_equipement_monstre_complet(monstre):
        print('\n')
        if (monstre.equipement_rune_haut!=0):
            print('La rune du haut de ',monstre.surnom,' est : \n',monstre.equipement_rune_haut,'\n')
        else:
            print('Vous n avez aucune rune d équipée en haut pour le moment.\n')
        if (monstre.equipement_rune_haut_droite!=0):
            print('La rune en haut à droite de ',monstre.surnom,' est : \n',monstre.equipement_rune_haut_droite,'\n')
        else:
            print('Vous n avez aucune rune d équipée en haut à droite pour le moment.\n')
        if (monstre.equipement_rune_bas_droite!=0):
            print('La rune en bas à droite de ',monstre.surnom,' est : \n',monstre.equipement_rune_bas_droite,'\n')
        else:
            print('Vous n avez aucune rune d équipée en bas à droite pour le moment.\n')
        if (monstre.equipement_rune_bas!=0):
            print('La rune du bas de ',monstre.surnom,' est : \n',monstre.equipement_rune_bas,'\n')
        else:
            print('Vous n avez aucune rune d équipée en bas pour le moment.\n')
        if (monstre.equipement_rune_bas_gauche!=0):
            print('La rune en bas à gauche de ',monstre.surnom,' est : \n',monstre.equipement_rune_bas_gauche,'\n')
        else:
            print('Vous n avez aucune rune d équipée en bas à gauche pour le moment.\n')
        if (monstre.equipement_rune_haut_gauche!=0):
            print('La rune en haut à gauche de ',monstre.surnom,' est : \n',monstre.equipement_rune_haut_gauche,'\n')
        else:
            print('Vous n avez aucune rune d équipée en haut à gauche pour le moment.\n')
        print('\n')
