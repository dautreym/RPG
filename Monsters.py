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


class Monstre:
    def __init__(self, NOM, ATTRIBUT, CLASSE, NIVEAU, PV, PV_ACTUELS, ATK, DEF, VIT):
        self.nom=NOM
        self.surnom=NOM
        self.type='Monstre'
        self.attribut=ATTRIBUT
        self.classe=CLASSE
        self.niveau=NIVEAU
        self.pv=PV
        self.pv_actuels=PV_ACTUELS
        self.attaque=ATK
        self.attaque_actuelle=ATK
        self.defense=DEF
        self.defense_actuelle=DEF
        self.vitesse=VIT
        self.vitesse_actuelle=VIT
        self.eveil=0
        self.etat='vivant'
        self.indice_stockage_base=OUT_OF_STOCKAGE
        self.equipement_rune_haut=0
        self.equipement_rune_haut_droite=0
        self.equipement_rune_bas_droite=0
        self.equipement_rune_bas=0
        self.equipement_rune_bas_gauche=0
        self.equipement_rune_haut_gauche=0
        self.XP_avant_prochain_niveau=Donjon.Trouver_XP_initiale(CLASSE,NIVEAU)

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

        self.pv_max_donjons=0
        self.attaque_max_donjons=0
        self.defense_max_donjons=0
        self.vitesse_max_donjons=0
        self.taux_coup_critique_max_donjons=0
        self.dommages_critiques_max_donjons=0
        self.resistance_max_donjons=0
        self.precision_max_donjons=0

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


        self.resistance=0.15
        self.resistance_actuelle=self.resistance
        self.precision=0
        self.precision_actuelle=self.precision
        self.presence_leader_skill=0
        self.presence_passif_1=0
        self.presence_passif_2=0
        self.reduction_de_degats=0
        self.nb_coups_subis=0
        self.vol_de_vie=0
        self.determination=0
        self.taux_coup_critique=0.15
        self.taux_coup_critique_actuel=self.taux_coup_critique
        self.dommages_critiques=0.5
        self.dommages_critiques_actuels=self.dommages_critiques
        self.taux_coup_superficiel=0
        self.jauge_attaque=0
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
        self.Peut_jouer=1
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

        self.capacite1=Slime.Ecrasement
        self.capacite1Nom='Ecrasement'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

    def Ecrasement(slime,cible):
        print('\n',slime.surnom,slime.attribut,'saute en l air et retombe de tout son poids sur ',cible.surnom,cible.attribut,'!!\n')
        degats=35+CalculDommage(slime,3.3,slime.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(slime,3.3,slime.capacite1BonusSkill,degats-35,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(slime,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.3,cible.resistance_actuelle,slime.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Slow_down(cible,1)
        return cible


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

        self.capacite1=GardienForet.Branche
        self.capacite1Nom='Coup de branche'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

    def Branche(arbre,cible):
        print('\n',arbre.surnom,arbre.attribut,' frappe ',cible.surnom,cible.attribut,' avec une branche!!\n')
        degats=CalculDommage(arbre,3.6,arbre.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(arbre,3.6,arbre.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(arbre,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.15,cible.resistance_actuelle,arbre.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1
        return cible


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

        self.capacite1=Champignon.Spore
        self.capacite1Nom='Spore Toxique'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

    def Spore(champi,cible):
        print('\n',champi.surnom,champi.attribut,' projette des spores toxiques sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(champi,3.0,champi.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(champi,3.0,champi.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(champi,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,champi.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Degats_continus(cible,1,1)
        return cible


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

        self.capacite1=Spectre.Persecution
        self.capacite1Nom='Persécution'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

    def Persecution(spectre,cible):
        print('\n',spectre.surnom,spectre.attribut,' frappe ',cible.surnom,cible.attribut,' avec sa lanterne!!\n')
        degats=CalculDommage(spectre,3.4,spectre.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(spectre,3.4,spectre.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(spectre,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,spectre.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Bonus_coup_superficiel(cible,1)
        return cible


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

        self.capacite1=Canniboite.Morsure
        self.capacite1Nom='Morsure'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

    def Morsure(boite,cible):
        print('\n',boite.surnom,boite.attribut,' mord ',cible.surnom,cible.attribut,'de toutes ses forces!!\n')
        degats=CalculDommage(boite,3.6,boite.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(boite,3.6,boite.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(boite,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,boite.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Def_break(cible,1)
        return cible


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

        self.capacite1=Crapoxique.Bave
        self.capacite1Nom='Jet de bave'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

    def Bave(croa,cible):
        print('\n',croa.surnom,croa.attribut,' jette sa bave toxique sur ',cible.surnom,cible.attribut,'!!\n')
        degats=30+CalculDommage(croa,3.4,croa.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(croa,3.4,croa.capacite1BonusSkill,degats-30,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(croa,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,croa.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' perd 15% de sa jauge d\'attaque!!\n')
                cible.jauge_attaque-=max(15,Arrondir(0.15*cible.jauge_attaque))
        return cible


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

        self.capacite1=Sacasable.Sable
        self.capacite1Nom='Jet de Sable'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

    def Sable(sable,cible):
        print('\n',sable.surnom,sable.attribut,' jette du sable sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(sable,3.5,sable.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(sable,3.5,sable.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(sable,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.3,cible.resistance_actuelle,sable.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Sommeil(cible,1)
        return cible


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

        self.capacite1=BasElementaire.Sphere
        self.capacite1Nom='Sphères élémentaires'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

        self.capacite2=BasElementaire.Frappes
        self.capacite2Nom='Frappes élémentaires'
        self.capacite2BonusSkill=0
        self.Trecharge2=3
        self.attente2=0
        self.etatCap2='dispo'

    def Sphere(elem,cible):
        print('\n',elem.surnom,elem.attribut,' jette deux orbes élémentaires sur ',cible.surnom,cible.attribut,'!!\n')
        for i in range(2):
            degats=CalculDommage(elem,1.9,elem.capacite1BonusSkill,cible)
            AffichageTypeDeCoup(elem,1.9,elem.capacite1BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(elem,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.2,cible.resistance_actuelle,elem.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Atk_break(cible,2)
        return cible

    def Frappes(elem,cible):
        print('\n',elem.surnom,elem.attribut,' frappe quatre fois ',cible.surnom,cible.attribut,'!!\n')
        for j in range(4):
            degats=CalculDommage(elem,1.3,elem.capacite2BonusSkill,cible)
            AffichageTypeDeCoup(elem,1.3,elem.capacite2BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(elem,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.3,cible.resistance_actuelle,elem.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Def_break(cible,2)
        return cible

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
        self.capacite1Nom='Ingrédient de qualité'

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
        XP_recue=Arrondir(XP_recue)
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
        self.capacite1Nom='Ingrédient de qualité'

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
        self.capacite1Nom='Ingrédient de qualité'

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
        XP_recue=Arrondir(2*XP_recue)
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

        self.capacite1=Sanglier.Charge
        self.capacite1Nom='Charge'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

    def Charge(sangli,cible):
        print('\n',sangli.surnom,sangli.attribut,' charge sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(sangli,3.5,sangli.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(sangli,3.5,sangli.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(sangli,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.15,cible.resistance_actuelle,sangli.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1
        return cible


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

        self.capacite1=PlanteCarnivore.Fouet
        self.capacite1Nom='Fouet Liane'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

    def Fouet(plante,cible):
        plante.vol_de_vie+=30
        print('\n',plante.surnom,plante.attribut,' fouette ',cible.surnom,cible.attribut,' avec une liane!!\n')
        degats=CalculDommage(plante,3.5,plante.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(plante,3.5,plante.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(plante,degats,cible)
        plante.vol_de_vie-=30
        return cible


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

        self.capacite1=BoiteDePandore.Morsure
        self.capacite1Nom='Morsure'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

    def Morsure(boite,cible):
        print('\n',boite.surnom,boite.attribut,' mord ',cible.surnom,cible.attribut,'de toutes ses forces!!\n')
        degats=CalculDommage(boite,3.8,boite.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(boite,3.8,boite.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(boite,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,boite.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Retirer_un_bonus(cible)
        return cible


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

        self.capacite1=SoldatSquelette.Entaille
        self.capacite1Nom='Entaille'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

        self.capacite2=SoldatSquelette.Slash
        self.capacite2Nom='Slash Circulaire'
        self.capacite2BonusSkill=0
        self.Trecharge2=4
        self.attente2=0
        self.etatCap2='dispo'

    def Entaille(skelet,cible):
        print('\n',skelet.surnom,skelet.attribut,' tranche ',cible.surnom,cible.attribut,' avec son épée!!\n')
        degats=CalculDommage(skelet,3.8,skelet.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(skelet,3.8,skelet.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(skelet,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,skelet.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Atk_break(cible,2)
        return cible

    def Slash(skelet,equipe_ennemie):
        for i in range(len(equipe_ennemie)):
            print('\n',skelet.surnom,skelet.attribut,' tranche toute l\'équipe ennemie avec une attaque circulaire!!\n')
            if (equipe_ennemie[i].pv_actuels>0):
                print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' reçoit l\'attaque circulaire!!')
                degats=CalculDommage(skelet,2.4,skelet.capacite2BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(skelet,2.4,skelet.capacite2BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(skelet,degats,equipe_ennemie[i])
                if(PrioriteElementaire(skelet,equipe_ennemie[i])==True):
                    Perturbation_recup(equipe_ennemie[i],2)
        return equipe_ennemie


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

        self.capacite1=ChauveSouris.Morsure
        self.capacite1Nom='Morsure'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

        self.capacite2=ChauveSouris.Ultrason
        self.capacite2Nom='Ultrason'
        self.capacite2BonusSkill=0
        self.Trecharge2=4
        self.attente2=0
        self.etatCap2='dispo'

    def Morsure(cs,cible):
        print('\n',cs.surnom,cs.attribut,' mord ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(cs,3.6,cs.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(cs,3.6,cs.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(cs,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,cs.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Def_break(cible,2)
        return cible

    def Ultrason(cs,equipe_ennemie):
        print('\n',cs.surnom,cs.attribut,'projette des ultrason sur l équipe ennemie!!\n')
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,'reçoit les ultrasons!!')
                degats=CalculDommage(cs,3.2,cs.capacite2BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(cs,3.2,cs.capacite2BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(cs,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(0.75,equipe_ennemie[i].resistance_actuelle,cs.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' perd 30% de sa jauge d\'attaque!!\n')
                        equipe_ennemie[i].jauge_attaque-=max(30,Arrondir(0.3*equipe_ennemie[i].jauge_attaque))
        return equipe_ennemie


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

        self.capacite1=Scorpion.Griffe
        self.capacite1Nom='Double Griffes'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

    def Griffe(scorpi,cible):
        print('\n',scorpi.surnom,scorpi.attribut,' griffe deux fois ',cible.surnom,cible.attribut,'!!\n')
        for i in range(2):
            degats=CalculDommage(scorpi,1.8,scorpi.capacite1BonusSkill,cible)
            AffichageTypeDeCoup(scorpi,1.8,scorpi.capacite1BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(scorpi,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,scorpi.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Degats_continus(cible,1,1)
        return cible


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

            self.capacite1=Imp.Lance
            self.capacite1Nom='Coup de Lance'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Imp.Perforation
            self.capacite2Nom='Perforation'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Imp.Lance
            self.capacite1Nom='Coup de Lance'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Imp.SphereInfernale
            self.capacite2Nom='Sphère Infernale'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Imp.Lance
            self.capacite1Nom='Coup de Lance'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Imp.Perforation
            self.capacite2Nom='Perforation'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Imp.Lance
            self.capacite1Nom='Coup de Lance'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Imp.SphereInfernale
            self.capacite2Nom='Sphère Infernale'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Imp.Lance
            self.capacite1Nom='Coup de Lance'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Imp.Perforation
            self.capacite2Nom='Perforation'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'


    def Lance(imp,cible):
        print('\n',imp.surnom,imp.attribut,' plante sa lance dans ',cible.surnom,cible.attribut,'!!\n')
        degats=-20+CalculDommage(imp,3.7,imp.capacite1BonusSkill,cible)
        Type_coup=AffichageTypeDeCoup(imp,3.7,imp.capacite1BonusSkill,degats+20,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(imp,degats,cible)
        if(Type_coup=='Critique'):
            Speed_up(imp,2)
        return cible

    def SphereInfernale(imp,cible):
        print('\n',imp.surnom,imp.attribut,' projette une sphère infernale sur ',cible.surnom,cible.attribut,'!!\n')
        degats=50+CalculDommage(imp,4.8,imp.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(imp,4.8,imp.capacite2BonusSkill,degats-50,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(imp,degats,cible)
        if(cible.pv_actuels>0):
            if(imp.attribut=='Lumière'):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1
            elif(imp.attribut=='Eau'):
                print(cible.surnom,cible.attribut,' est gelé(e)!! \n')
                cible.gel=1
        return cible

    def Perforation(imp,cible):
        print('\n',imp.surnom,imp.attribut,' plante profondément sa lance dans le coeur de ',cible.surnom,cible.attribut,'!!\n')
        imp.taux_coup_critique_actuel+=50
        degats=50+CalculDommage(imp,5.2,imp.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(imp,5.2,imp.capacite2BonusSkill,degats-50,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(imp,degats,cible)
        imp.taux_coup_critique_actuel-=50
        return cible


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

            self.capacite1=Lutin.SphereSacree
            self.capacite1Nom='Sphère Sacrée'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Lutin.Ignition
            self.capacite2Nom='Ignition'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Lutin.SphereSacree
            self.capacite1Nom='Sphère Sacrée'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Lutin.Deceleration
            self.capacite2Nom='Décélération'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Lutin.SphereSacree
            self.capacite1Nom='Sphère Sacrée'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Lutin.Deceleration
            self.capacite2Nom='Décélération'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Lutin.SphereSacree
            self.capacite1Nom='Sphère Sacrée'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Lutin.Ignition
            self.capacite2Nom='Ignition'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Lutin.SphereSacree
            self.capacite1Nom='Sphère Sacrée'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Lutin.Deceleration
            self.capacite2Nom='Décélération'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

    def SphereSacree(lutin,cible):
        print('\n',lutin.surnom,lutin.attribut,' projette une sphère sacrée sur ',cible.surnom,cible.attribut,'!!\n')
        degats=20+CalculDommage(lutin,3.6,lutin.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(lutin,3.6,lutin.capacite1BonusSkill,degats-20,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(lutin,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,lutin.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Slow_down(cible,2)
        return cible

    def Deceleration(lutin,equipe_ennemie):
        print('\n',lutin.surnom,lutin.attribut,'lance un sort de décélération sur l équipe ennemie!!\n')
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,'reçoit le sort de décélération!!')
                degats=CalculDommage(lutin,2.1,lutin.capacite2BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(lutin,2.1,lutin.capacite2BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(lutin,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(0.8,equipe_ennemie[i].resistance_actuelle,lutin.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        Slow_down(equipe_ennemie[i],2)
        return equipe_ennemie

    def Ignition(lutin,cible):
        print('\n',lutin.surnom,lutin.attribut,' réduit ',cible.surnom,cible.attribut,' en cendres avec un sort de feu!!\n')
        degats=90+CalculDommage(lutin,4.6,lutin.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(lutin,4.6,lutin.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(lutin,degats,cible)
        Degats_continus(cible,1,3)
        return cible


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

            self.capacite1=Yeti.Poing
            self.capacite1Nom='Poing d Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Yeti.Ecrasement
            self.capacite2Nom='Ecrasement'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Yeti.Poing
            self.capacite1Nom='Poing d Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Yeti.Smash
            self.capacite2Nom='Smash Lourd'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Yeti.Poing
            self.capacite1Nom='Poing d Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Yeti.Smash
            self.capacite2Nom='Smash Lourd'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Yeti.Poing
            self.capacite1Nom='Poing d Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Yeti.Smash
            self.capacite2Nom='Smash Lourd'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Yeti.Poing
            self.capacite1Nom='Poing d Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Yeti.Ecrasement
            self.capacite2Nom='Ecrasement'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

    def Poing(yeti,cible):
        print('\n',yeti.surnom,yeti.attribut,' écrase son poing monstrueux sur ',cible.surnom,cible.attribut,'!!\n')
        for i in range(2):
            degats=20+CalculDommage(yeti,1.9,yeti.capacite1BonusSkill,cible)
            AffichageTypeDeCoup(yeti,1.9,yeti.capacite1BonusSkill,degats-20,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(yeti,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,yeti.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Slow_down(cible,1)
        return cible

    def Smash(yeti,cible):
        print('\n',yeti.surnom,yeti.attribut,' frappe violemment ',cible.surnom,cible.attribut,'!!\n')
        for i in range(2):
            degats=(Arrondir(1.5*yeti.defense))+CalculDommage(yeti,1.5,yeti.capacite2BonusSkill,cible)
            AffichageTypeDeCoup(yeti,1.5,yeti.capacite2BonusSkill,degats-(Arrondir(1.5*yeti.defense)),cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(yeti,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.3,cible.resistance_actuelle,yeti.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                    cible.stun=1
        return cible

    def Ecrasement(yeti,cible):
        print('\n',yeti.surnom,yeti.attribut,' écrase ',cible.surnom,cible.attribut,' de tout son poids!!\n')
        for i in range(2):
            degats=(Arrondir(0.28*yeti.pv_max_donjons))+CalculDommage(yeti,2.0,yeti.capacite2BonusSkill,cible)
            AffichageTypeDeCoup(yeti,2.0,yeti.capacite2BonusSkill,degats-(Arrondir(0.28*yeti.pv_max_donjons)),cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(yeti,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,yeti.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Slow_down(cible,2)
        return cible


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

            self.capacite1=Cerbere.Morsure
            self.capacite1Nom='Morsure'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Cerbere.DoubleMorsure
            self.capacite2Nom='Double Morsure'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Cerbere.Morsure
            self.capacite1Nom='Morsure'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Cerbere.Embuscade
            self.capacite2Nom='Embuscade'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Cerbere.Morsure
            self.capacite1Nom='Morsure'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Cerbere.DoubleMorsure
            self.capacite2Nom='Double Morsure'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Cerbere.Morsure
            self.capacite1Nom='Morsure'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Cerbere.DoubleMorsure
            self.capacite2Nom='Double Morsure'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Cerbere.Morsure
            self.capacite1Nom='Morsure'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Cerbere.Embuscade
            self.capacite2Nom='Embuscade'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

    def Morsure(cerbere,cible):
        cerbere.vol_de_vie+=30
        print('\n',cerbere.surnom,cerbere.attribut,' mord ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(cerbere,3.6,cerbere.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(cerbere,3.6,cerbere.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(cerbere,degats,cible)
        cerbere.vol_de_vie-=30
        return cible

    def DoubleMorsure(cerbere,cible):
        print('\n',cerbere.surnom,cerbere.attribut,' mords deux fois ',cible.surnom,cible.attribut,'!!\n')
        for i in range(2):
            degats=CalculDommage(cerbere,3.7,cerbere.capacite2BonusSkill,cible)
            AffichageTypeDeCoup(cerbere,3.7,cerbere.capacite2BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(cerbere,degats,cible)
        return cible

    def Embuscade(cerbere,cible):
        print('\n',cerbere.surnom,cerbere.attribut,' lacère ',cible.surnom,cible.attribut,' à une vitesse incroyable!!\n')
        degats=2*(140+cerbere.vitesse_actuelle+cerbere.capacite2BonusSkill)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(cerbere,degats,cible)
        Speed_up(cerbere,2)
        return cible


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

            self.capacite1=OursDeGuerre.Griffe
            self.capacite1Nom='Griffe Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=OursDeGuerre.Rugissement
            self.capacite2Nom='Rugissement'
            self.capacite2BonusSkill=0
            self.Trecharge2=5
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=OursDeGuerre.Griffe
            self.capacite1Nom='Griffe Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=OursDeGuerre.Abnegation
            self.capacite2Nom='Abnégation'
            self.capacite2BonusSkill=0
            self.Trecharge2=5
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=OursDeGuerre.Griffe
            self.capacite1Nom='Griffe Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=OursDeGuerre.Abnegation
            self.capacite2Nom='Abnégation'
            self.capacite2BonusSkill=0
            self.Trecharge2=5
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=OursDeGuerre.Griffe
            self.capacite1Nom='Griffe Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=OursDeGuerre.Abnegation
            self.capacite2Nom='Abnégation'
            self.capacite2BonusSkill=0
            self.Trecharge2=5
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=OursDeGuerre.Griffe
            self.capacite1Nom='Griffe Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=OursDeGuerre.Rugissement
            self.capacite2Nom='Rugissement'
            self.capacite2BonusSkill=0
            self.Trecharge2=5
            self.attente2=0
            self.etatCap2='dispo'

    def Griffe(ours,cible):
        print('\n',ours.surnom,ours.attribut,' griffe violemment ',cible.surnom,cible.attribut,'!!\n')
        degats=(Arrondir(0.15*ours.pv_max_donjons))+CalculDommage(ours,1.7,ours.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(ours,1.7,ours.capacite1BonusSkill,degats-(Arrondir(0.15*ours.pv_max_donjons)),cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(ours,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,ours.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' perd un quart de sa jauge d\'attaque!!\n')
                cible.jauge_attaque-=max(25,Arrondir(0.25*cible.jauge_attaque))
        return cible

    def Rugissement(ours,equipe_ennemie):
        print('\n',ours.surnom,ours.attribut,' rugit sur l équipe ennemie!!\n')
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,'reçoit le rugissement!!')
                degats=Arrondir(0.2*ours.pv_max_donjons)
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(ours,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(1,equipe_ennemie[i].resistance_actuelle,ours.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        Atk_break(equipe_ennemie[i],2)
        return equipe_ennemie

    def Abnegation(ours):
        if(ours.pv_actuels>0):
            print('\n',ours.surnom,ours.attribut,' érige une barrière spirituelle!!\n')
            if (ours.perturbation_recup<=0):
                montant=Arrondir(0.3*ours.pv_max_donjons)
                ours=Monstre.etreSoigne(ours,montant)
            else:
                print('La récupération de points de vie de ',ours.surnom,ours.attribut,' est actuellement entravée!! \n')
            print('Il reste ',ours.pv_actuels,' point(s) de vie sur',ours.pv_max_donjons,' à ',ours.surnom,ours.attribut,'!! \n')
            Tanky(ours,2)
        return ours


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

            self.capacite1=Elementaire.Griffe
            self.capacite1Nom='Griffe Elementaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Elementaire.Explosion
            self.capacite2Nom='Explosion Elementaire'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Elementaire.Griffe
            self.capacite1Nom='Griffe Elementaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Elementaire.Explosion
            self.capacite2Nom='Explosion Elementaire'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Elementaire.Griffe
            self.capacite1Nom='Griffe Elementaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Elementaire.Renforcement
            self.capacite2Nom='Renforcement Elementaire'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Elementaire.Griffe
            self.capacite1Nom='Griffe Elementaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Elementaire.Explosion
            self.capacite2Nom='Explosion Elementaire'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Elementaire.Griffe
            self.capacite1Nom='Griffe Elementaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Elementaire.Renforcement
            self.capacite2Nom='Renforcement Elementaire'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

    def Griffe(elem,cible):
        print('\n',elem.surnom,elem.attribut,' tranche ',cible.surnom,cible.attribut,' avec ses griffes acérées!!\n')
        degats=CalculDommage(elem,3.5,elem.capacite1BonusSkill,cible)
        Type_coup=AffichageTypeDeCoup(elem,3.5,elem.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(elem,degats,cible)
        if(Type_coup=='Critique'):
            Degats_continus(cible,1,2)
        return cible

    def Explosion(elem,cible):
        print('\n',elem.surnom,elem.attribut,' désintègre ',cible.surnom,cible.attribut,'dans une explosion élémentaire!!\n')
        degats=(Arrondir(0.1*elem.pv_max_donjons))+CalculDommage(elem,4.1,elem.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(elem,4.1,elem.capacite2BonusSkill,degats-(Arrondir(0.1*elem.pv_max_donjons)),cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(elem,degats,cible)
        return cible

    def Renforcement(elem):
        print('\n',elem.surnom,elem.attribut,' se renforce avec de l énergie naturelle!!\n')
        Rise(elem,3)
        Espada(elem,3)
        return elem


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

            self.capacite1=Garuda.Assaut
            self.capacite1Nom='Assaut Aérien'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Garuda.FireBall
            self.capacite2Nom='Boule de Feu'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Garuda.Assaut
            self.capacite1Nom='Assaut Aérien'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Garuda.Resurgir
            self.capacite2Nom='Resurgir'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Garuda.Assaut
            self.capacite1Nom='Assaut Aérien'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Garuda.ThunderBall
            self.capacite2Nom='Boule de Foudre'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Garuda.Assaut
            self.capacite1Nom='Assaut Aérien'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Garuda.Resurgir
            self.capacite2Nom='Resurgir'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Garuda.Lumiere
            self.capacite3Nom='Lumière de Résurrection'
            self.capacite3BonusSkill=0
            self.Trecharge3=7
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Garuda.Assaut
            self.capacite1Nom='Assaut Aérien'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Garuda.ShadowBall
            self.capacite2Nom='Balle Ombre'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

    def Assaut(garuda,cible):
        print('\n',garuda.surnom,garuda.attribut,' plonge en piquée sur ',cible.surnom,cible.attribut,'!!\n')
        degats=(-15)+CalculDommage(garuda,3.7,garuda.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(garuda,3.7,garuda.capacite1BonusSkill,degats+15,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(garuda,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.24,cible.resistance_actuelle,garuda.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1
        return cible

    def FireBall(garuda,cible):
        print('\n',garuda.surnom,garuda.attribut,' projette une boule de feu sur ',cible.surnom,cible.attribut,'!!\n')
        degats=50+CalculDommage(garuda,4.8,garuda.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(garuda,4.8,garuda.capacite2BonusSkill,degats-50,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(garuda,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,garuda.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Degats_continus(cible,1,3)
        return cible

    def ThunderBall(garuda,cible):
        print('\n',garuda.surnom,garuda.attribut,' projette une boule de foudre sur ',cible.surnom,cible.attribut,'!!\n')
        degats=50+CalculDommage(garuda,4.8,garuda.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(garuda,4.8,garuda.capacite2BonusSkill,degats-50,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(garuda,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,garuda.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1
        return cible

    def ShadowBall(garuda,cible):
        print('\n',garuda.surnom,garuda.attribut,' projette une boule de ténèbres sur ',cible.surnom,cible.attribut,'!!\n')
        degats=50+CalculDommage(garuda,4.8,garuda.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(garuda,4.8,garuda.capacite2BonusSkill,degats-50,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(garuda,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,garuda.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Degats_continus(cible,1,3)
        return cible

    def Resurgir(allie):
        print('\n',allie.surnom,allie.attribut,'reçoit un tour supplémentaire!!')
        Rise(allie,1)
        Espada(allie,1)
        allie.jauge_attaque+=100
        return allie

    def Lumiere(equipe_alliee):
        print('\nGaruda Lumière enveloppe toute l\'équipe dans une lumière de résurrection!! \n')
        possibilites_resurrection=[]
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels<=0):
                if(equipe_alliee[i].sans_resurrection<=0):
                    possibilites_resurrection.append(i)
                    print('L\'allié ',i,' : ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' peut revenir à la vie!!')
                else:
                    print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' a été maudit et ne peut donc pas revenir à la vie...\n')
            else:
                if (equipe_alliee[i].perturbation_recup<=0):
                    equipe_alliee[i]=Monstre.etreSoigne(equipe_alliee[i],0.2*equipe_alliee[i].pv_max_donjons)
                else:
                    print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces!!\n')
        if(len(possibilites_resurrection)!=0):
            ''' OUI, QUAND UN ENNEMI UTILISE CETTE CAPACITE, ON PEUT CHOISIR POUR LUI, NORMAL!! '''
            entree=input('Qui voulez-vous ramener à la vie ? ')
            while(not IsSecure(entree)):
                entree=input('Qui voulez-vous ramener à la vie ? ')
            choix_resurrection=int(entree)
            while(choix_resurrection not in possibilites_resurrection):
                entree=input('Qui voulez-vous ramener à la vie ? ')
                while(not IsSecure(entree)):
                    entree=input('Qui voulez-vous ramener à la vie ? ')
                choix_resurrection=int(entree)
            print(equipe_alliee[choix_resurrection].surnom,equipe_alliee[choix_resurrection].attribut,' revient à la vie!! \n')
            equipe_alliee[choix_resurrection].pv_actuels=Arrondir(0.2*equipe_alliee[i].pv_max_donjons)
            equipe_alliee[choix_resurrection]=SoignerDeTousLesMaux(equipe_alliee[choix_resurrection])
            equipe_alliee[choix_resurrection].etat='vivant'
        return equipe_alliee


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

            self.capacite1=Harpie.Kick
            self.capacite1Nom='Double Kick'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Harpie.Plumes
            self.capacite2Nom='Plumes Tranchantes'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Harpie.Kick
            self.capacite1Nom='Double Kick'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Harpie.Plumes
            self.capacite2Nom='Plumes Tranchantes'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Harpie.Kick
            self.capacite1Nom='Double Kick'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Harpie.Hurlement
            self.capacite2Nom='Hurlement'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Harpie.Kick
            self.capacite1Nom='Double Kick'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Harpie.Hurlement
            self.capacite2Nom='Hurlement'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Harpie.Kick
            self.capacite1Nom='Double Kick'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Harpie.Plumes
            self.capacite2Nom='Plumes Tranchantes'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Harpie.DanseCeleste
            self.capacite3Nom='Danse Céleste'
            self.capacite3BonusSkill=0
            self.Trecharge3=4
            self.attente3=0
            self.etatCap3='dispo'

    def Kick(harpie,cible):
        print('\n',harpie.surnom,harpie.attribut,' frappe deux fois ',cible.surnom,cible.attribut,'!!\n')
        for i in range(2):
            degats=CalculDommage(harpie,1.9,harpie.capacite1BonusSkill,cible)
            AffichageTypeDeCoup(harpie,1.9,harpie.capacite1BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(harpie,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,harpie.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Atk_break(cible,2)
        return cible

    def Hurlement(harpie,cible):
        print('\n',harpie.surnom,harpie.attribut,'pousse un hurlement strident!!\n')
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,harpie.precision_actuelle+0.5)
            if(EffetNefaste<=100*Limite_reussite):
                cible.stun=1
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                Degats_continus(cible,1,3)
            else:
                print(cible.surnom,cible.attribut,' résiste au hurlement!! \n')
        else:
            print(cible.surnom,cible.attribut,' est immunisé(e) contre les effets néfastes!!\n')
        return cible

    def Plumes(harpie,cible):
        print('\n',harpie.surnom,harpie.attribut,' projette une nuée de plumes tranchantes sur ',cible.surnom,cible.attribut,'!!\n')
        for i in range(3):
            degats=CalculDommage(harpie,1.9,harpie.capacite2BonusSkill,cible)
            AffichageTypeDeCoup(harpie,1.9,harpie.capacite2BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(harpie,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,harpie.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Perturbation_recup(cible,2)
        return cible

    def DanseCeleste(harpie,cible):
        print('\n',harpie.surnom,harpie.attribut,' entame une dance céleste et lacère plusieurs fois ',cible.surnom,cible.attribut,'!!\n')
        for i in range(4):
            degats=CalculDommage(harpie,2,harpie.capacite3BonusSkill,cible)
            AffichageTypeDeCoup(harpie,2,harpie.capacite3BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(harpie,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.3,cible.resistance_actuelle,harpie.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Def_break(cible,2)
        return cible


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

            self.capacite1=Salamandre.Tourbillon
            self.capacite1Nom='Tourbillon'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Salamandre.Ecrasement
            self.capacite2Nom='Ecrasement'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Salamandre.Tremblement
            self.capacite3Nom='Tremblement de Terre'
            self.capacite3BonusSkill=0
            self.Trecharge3=6
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Salamandre.Tourbillon
            self.capacite1Nom='Tourbillon'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Salamandre.Ecrasement
            self.capacite2Nom='Ecrasement'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Salamandre.Tourbillon
            self.capacite1Nom='Tourbillon'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Salamandre.Tempete
            self.capacite2Nom='Tempête de Sable'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Salamandre.Tourbillon
            self.capacite1Nom='Tourbillon'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Salamandre.Ecrasement
            self.capacite2Nom='Ecrasement'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Salamandre.Tourbillon
            self.capacite1Nom='Tourbillon'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Salamandre.Tempete
            self.capacite2Nom='Tempête de Sable'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

    def Tourbillon(salam,cible):
        print('\n',salam.surnom,salam.attribut,' engloutit ',cible.surnom,cible.attribut,'dans un tourbillon magique!!\n')
        degats=15+CalculDommage(salam,3.5,salam.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(salam,3.5,salam.capacite1BonusSkill,degats-15,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(salam,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,salam.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Atk_break(cible,2)
        return cible

    def Ecrasement(salam,cible):
        print('\n',salam.surnom,salam.attribut,' écrase violemment ',cible.surnom,cible.attribut,'!!\n')
        degats=(Arrondir(3*salam.defense_actuelle))+CalculDommage(salam,2.4,salam.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(salam,2.4,salam.capacite2BonusSkill,degats-(Arrondir(3*salam.defense_actuelle)),cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(salam,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,salam.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Slow_down(cible,2)
        return cible

    def Tempete(salam,cible):
        print('\n',salam.surnom,salam.attribut,' engloutit ',cible.surnom,cible.attribut,'dans une violente tempête!!\n')
        degats=(Arrondir(2.8*salam.defense_actuelle))+CalculDommage(salam,2.5,salam.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(salam,2.5,salam.capacite2BonusSkill,degats-(Arrondir(2.8*salam.defense_actuelle)),cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(salam,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,salam.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Degats_continus(cible,1,3)
        return cible

    def Tremblement(salam,equipe_ennemie):
        print('\n',salam.surnom,salam.attribut,' secoue toute l équipe ennemie avec un puissant séisme!!\n')
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,'reçoit le tremblement de terre!!')
                degats=(Arrondir(2.1*salam.defense_actuelle))+CalculDommage(salam,2,salam.capacite3BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(salam,2,salam.capacite3BonusSkill,degats-(Arrondir(2.1*salam.defense_actuelle)),equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(salam,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(1,equipe_ennemie[i].resistance_actuelle,salam.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' voit sa jauge d\'attaque diminuer de moitié!! \n')
                        equipe_ennemie[i].jauge_attaque-=max(50,Arrondir(0.5*equipe_ennemie[i].jauge_attaque))
        return equipe_ennemie


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

        self.capacite1=Esprit.SphereSpirituelle
        self.capacite1Nom='Sphère Spirituelle'
        self.capacite1BonusSkill=0
        self.Trecharge1=1
        self.attente1=0
        self.etatCap1='dispo'

        self.capacite2=Esprit.Guerison
        self.capacite2Nom='Guérison'
        self.capacite2BonusSkill=0
        self.Trecharge2=3
        self.attente2=0
        self.etatCap2='dispo'

    def SphereSpirituelle(esprit,equipe_alliee,cible):
        print('\n',esprit.surnom,esprit.attribut,' projette une sphère spirituelle sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(esprit,3.5,esprit.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(esprit,3.5,esprit.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(esprit,degats,cible)
        nb_allies=len(equipe_alliee)
        if(nb_allies>0):
            pv_min=equipe_alliee[0].pv_actuels
            indice_allie_a_soigner=0
            i=0
            while(i<=nb_allies-1):
                if(equipe_alliee[i].pv_actuels<pv_min):
                    pv_min=equipe_alliee[i].pv_actuels
                    indice_allie_a_soigner=i
                i+=1
            montant=Arrondir(0.15*equipe_alliee[indice_allie_a_soigner].pv_max_donjons)
            equipe_alliee[indice_allie_a_soigner]=Monstre.etreSoigne(equipe_alliee[indice_allie_a_soigner],montant)
        return cible
        ''' Verifier que la jauge d'attaque ne réaugmente pas immédiatement ex. de 15 '''
        ''' Askip non '''

    def Guerison(esprit,allie):
        print('\n',esprit.surnom,esprit.attribut,' soigne ',allie.surnom,allie.attribut,'et lui-même!!\n')
        if (allie.pv_actuels>0):
            allie=SoignerDeTousLesMaux(allie)
            print(allie.surnom,allie.attribut,'est débarrassé de tous les effets négatifs qui l affectaient!!')
            montant=allie.pv_max_donjons*((1/5)+esprit.capacite2BonusSkill)
            allie=Monstre.etreSoigne(allie,montant)
        elif (allie.pv_actuels<=0):
            print(allie.surnom,allie.attribut,' est mort!! \n')
        print('Il reste ',allie.pv_actuels,' point(s) de vie sur',allie.pv_max_donjons,' à ',allie.surnom,allie.attribut,'!! \n')
        esprit=SoignerDeTousLesMaux(esprit)
        print(esprit.surnom,esprit.attribut,'est débarrassé de tous les effets négatifs qui l affectaient!!')
        montant=esprit.pv_max_donjons*((1/5)+esprit.capacite2BonusSkill)
        esprit=Monstre.etreSoigne(esprit,montant)
        print('Il reste ',esprit.pv_actuels,' point(s) de vie sur',esprit.pv_max_donjons,' à ',esprit.surnom,esprit.attribut,'!! \n')
        return allie


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

            self.capacite1=Viking.Hache
            self.capacite1Nom='Lancer de Hache'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Viking.Meurtre
            self.capacite2Nom='Folie Meurtrière'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Viking.Encouragement
            self.Anti_leader_skill=Viking.AntiEncouragement

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

            self.capacite1=Viking.Hache
            self.capacite1Nom='Lancer de Hache'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Viking.MultipleHache
            self.capacite2Nom='Multiples Lancers de Haches'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Viking.Hache
            self.capacite1Nom='Lancer de Hache'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Viking.Meurtre
            self.capacite2Nom='Folie Meurtrière'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Viking.Hache
            self.capacite1Nom='Lancer de Hache'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Viking.MultipleHache
            self.capacite2Nom='Multiples Lancers de Haches'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Viking.Hache
            self.capacite1Nom='Lancer de Hache'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Viking.Meurtre
            self.capacite2Nom='Folie Meurtrière'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

    def Hache(vik,cible):
        print('\n',vik.surnom,vik.attribut,' lance une hache sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(vik,3.7,vik.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(vik,3.7,vik.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(vik,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.3,cible.resistance_actuelle,vik.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Degats_continus(cible,1,3)
        return cible

    def Meurtre(vik,cible):
        print('\n',vik.surnom,vik.attribut,' entre dans une folie meurtrière et pourfend ',cible.surnom,cible.attribut,' de sa hache!!\n')
        rage=4+3.5*(1-(vik.pv_actuels/vik.pv_max_donjons))
        degats=CalculDommage(vik,rage,vik.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(vik,rage,vik.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(vik,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,vik.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Def_break(cible,2)
        return cible

    def MultipleHache(vik,cible):
        print('\n',vik.surnom,vik.attribut,' lance trois haches sur ',cible.surnom,cible.attribut,'!!\n')
        for i in range(3):
            degats=CalculDommage(vik,2.1,vik.capacite2BonusSkill,cible)
            Type_coup=AffichageTypeDeCoup(vik,2.1,vik.capacite2BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(vik,degats,cible)
            if(Type_coup=='Critique'):
                print(vik.surnom,vik.attribut,' voit sa jauge d\'attaque augmenter de 15%!!\n')
                vik.jauge_attaque+=max(15,Arrondir(0.15*vik.jauge_attaque))
        return cible

    def Encouragement(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].attaque_actuelle+=Arrondir(0.15*equipe_alliee[i].attaque_max_donjons)
            equipe_alliee[i].attaque_max_donjons+=Arrondir(0.15*equipe_alliee[i].attaque_max_donjons)
            print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 15%!!')
            print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].attaque_actuelle,'\n')
        return equipe_alliee

    def AntiEncouragement(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].attaque_actuelle-=Arrondir(0.15*equipe_alliee[i].attaque_max_donjons)
        return equipe_alliee


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

            self.capacite1=Chevalier.ClivageTerrestre
            self.capacite1Nom='Clivage Terrestre'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Chevalier.ClivageMarin
            self.capacite2Nom='Clivage Marin'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Chevalier.Abnegation
            self.capacite3Nom='Abnégation'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Chevalier.ClivageTerrestre
            self.capacite1Nom='Clivage Terrestre'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Chevalier.Provocation
            self.capacite2Nom='Provocation'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Chevalier.ClivageTerrestre
            self.capacite1Nom='Clivage Terrestre'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Chevalier.ClivageMarin
            self.capacite2Nom='Clivage Marin'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Chevalier.ClivageTerrestre
            self.capacite1Nom='Clivage Terrestre'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Chevalier.ClivageMarin
            self.capacite2Nom='Clivage Marin'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Chevalier.Chevalerie

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

            self.capacite1=Chevalier.ClivageTerrestre
            self.capacite1Nom='Clivage Terrestre'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Chevalier.Provocation
            self.capacite2Nom='Provocation'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Chevalier.Urgence

    def ClivageTerrestre(chev,cible):
        print('\n',chev.surnom,chev.attribut,' fend ',cible.surnom,cible.attribut,' avec son épée!!\n')
        degats=Arrondir(0.18*chev.pv_max_donjons)+CalculDommage(chev,1,chev.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(chev,1,chev.capacite1BonusSkill,degats-Arrondir(0.18*chev.pv_max_donjons),cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(chev,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.4,cible.resistance_actuelle,chev.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Def_break(cible,2)
        return cible

    def ClivageMarin(chev,cible):
        print('\n',chev.surnom,chev.attribut,' fend deux fois ',cible.surnom,cible.attribut,' de son épée!!\n')
        for i in range(2):
            degats=(Arrondir(0.12*chev.pv_max_donjons))+CalculDommage(chev,1,chev.capacite2BonusSkill,cible)
            AffichageTypeDeCoup(chev,1,chev.capacite1BonusSkill,degats-(Arrondir(0.12*chev.pv_max_donjons)),cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(chev,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,chev.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Atk_break(cible,2)
        return cible

    def Provocation(chev,cible):
        print('\n',chev.surnom,chev.attribut,' provoque ',cible.surnom,cible.attribut,'!!\n')
        degats=(Arrondir(0.26*chev.pv_max_donjons))+CalculDommage(chev,1.9,chev.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(chev,1.9,chev.capacite2BonusSkill,degats-(Arrondir(0.26*chev.pv_max_donjons)),cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(chev,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.8,cible.resistance_actuelle,chev.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,'est provoquée!! \n')
                cible.provoque=1
                cible.tours_provoque=max(2,cible.tours_provoque)
                chev.provocation=1
                chev.tours_provocation=2
        return cible

    def Abnegation(chev,equipe_ennemie):
        print('\n',chev.surnom,chev.attribut,' provoque toute l équipe ennemie!!\n')
        for j in range(len(equipe_ennemie)):
            if(equipe_ennemie[j].pv_actuels>0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.8,equipe_ennemie[j].resistance_actuelle,chev.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    print(equipe_ennemie[j].surnom,equipe_ennemie[j].attribut,'devient provoqué!!')
                    equipe_ennemie[j].provoque=1
                    equipe_ennemie[j].tours_provoque=max(2,equipe_ennemie[j].tours_provoque)
        chev.provocation=1
        chev.tours_provocation=2
        Tanky(chev,3)
        return equipe_ennemie

    def Chevalerie(equipe_alliee):
        for k in range(len(equipe_alliee)):
            equipe_alliee[k].reduction_de_degats+=0.2
            print(equipe_alliee[k].surnom,equipe_alliee[k].attribut,' voit sa réduction de dégâts augmenter de 20%!!')
            print('La réduction de dégâts de ',equipe_alliee[k].surnom,equipe_alliee[k].attribut,' est désormais de ',equipe_alliee[k].reduction_de_degats,'!!\n')
        return equipe_alliee

    def AntiChevalerie(equipe_alliee):
        for k in range(len(equipe_alliee)):
            equipe_alliee[k].reduction_de_degats-=0.2

    def Urgence(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='Chevalier' and equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].attente1-=equipe_alliee[i].nb_coups_subis
                if(equipe_alliee[i].attente1<0):
                    equipe_alliee[i].attente1=0
                equipe_alliee[i].attente2-=equipe_alliee[i].nb_coups_subis
                if(equipe_alliee[i].attente2<0):
                    equipe_alliee[i].attente2=0
                equipe_alliee[i].nb_coups_subis=0
        return equipe_alliee


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

            self.capacite1=Fee.Tourbillon
            self.capacite1Nom='Tourbillon'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Fee.DoubleFleche
            self.capacite2Nom='Double Flèche'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Fee.PluieDouleur
            self.capacite3Nom='Pluie de Douleur'
            self.capacite3BonusSkill=0
            self.Trecharge3=6
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Fee.Tourbillon
            self.capacite1Nom='Tourbillon'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Fee.Soin
            self.capacite2Nom='Soin'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Fee.Support
            self.Anti_leader_skill=Fee.AntiSupport

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

            self.capacite1=Fee.Tourbillon
            self.capacite1Nom='Tourbillon'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Fee.Soin
            self.capacite2Nom='Soin'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Fee.Tourbillon
            self.capacite1Nom='Tourbillon'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Fee.Soin
            self.capacite2Nom='Soin'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Fee.Benediction
            self.capacite3Nom='Bénédiction de lumière'
            self.capacite3BonusSkill=0
            self.Trecharge3=4
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Fee.Support
            self.Anti_leader_skill=Fee.AntiSupport

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

            self.capacite1=Fee.Tourbillon
            self.capacite1Nom='Tourbillon'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Fee.DoubleFleche
            self.capacite2Nom='Double Flèche'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

    def Tourbillon(fee,cible):
        print('\n',fee.surnom,fee.attribut,' balaye trois fois ',cible.surnom,cible.attribut,' avec un tourbillon magique!!\n')
        for i in range(3):
            degats=CalculDommage(fee,1.2,fee.capacite1BonusSkill,cible)
            AffichageTypeDeCoup(fee,1.2,fee.capacite1BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(fee,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.2,cible.resistance_actuelle,fee.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    if(fee.attribut=='Eau'):
                        print(cible.surnom,cible.attribut,' est gelé(e)!! \n')
                        cible.gel=1
                    else:
                        print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                        cible.stun=1
        return cible

    def Soin(fee,allie):
        print('\n',fee.surnom,fee.attribut,' soigne ',allie.surnom,allie.attribut,'!!\n')
        if (allie.pv_actuels>0):
            allie=SoignerDeTousLesMaux(allie)
            print(allie.surnom,allie.attribut,'est débarrassé de tous les effets négatifs qui l affectaient!!')
            montant=fee.attaque*(4+fee.capacite2BonusSkill)
            allie=Monstre.etreSoigne(allie,montant)
        elif (allie.pv_actuels<=0):
            print(allie.surnom,allie.attribut,' est mort!! \n')
        print('Il reste ',allie.pv_actuels,' point(s) de vie sur',allie.pv_max_donjons,' à ',allie.surnom,allie.attribut,'!! \n')
        return allie

    # ignore la contre-attaque et la réflexion de dommages
    def DoubleFleche(fee,equipe_ennemie):
        ''' ON PEUT CHOISIR POUR L ENNEMI !!! :( '''
        positions_ennemis=['de gauche','du centre','de droite']
        k=0
        while(k<len(equipe_ennemie)):
            if (equipe_ennemie[k].pv_actuels<=0):
                equipe_ennemie.pop(k)
                positions_ennemis.pop(k)
                k-=1
            k+=1
        possibilites_cible=[]
        print('Vos ennemis sont : ')
        for k in range(len(equipe_ennemie)):
            print(equipe_ennemie[k].surnom,equipe_ennemie[k].attribut,positions_ennemis[k],' = ',k,'(',equipe_ennemie[k].pv_actuels,'PV restants)')
            possibilites_cible.append(k)
        entree=input('Quelle cible voulez-vous attaquer ? ')
        while(not IsSecure(entree)):
            entree=input('Quelle cible voulez-vous attaquer ? ')
        indice_cible=int(entree)
        while(indice_cible not in possibilites_cible):
            entree=input('Quelle cible voulez-vous attaquer ? ')
            while(not IsSecure(entree)):
                entree=input('Quelle cible voulez-vous attaquer ? ')
            indice_cible=int(entree)
        cible=equipe_ennemie[indice_cible]
        print('\n',fee.surnom,fee.attribut,' tire une première flèche magique sur ',cible.surnom,cible.attribut,'!! \n')
        degats=CalculDommage(fee,3.4,fee.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(fee,3.4,fee.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(fee,degats,cible)

        if isAlive(equipe_ennemie):
            print('\n',fee.surnom,fee.attribut,' tire une deuxième flèche magique aléatoire sur l équipe ennemie!!\n')
            indice_cible_random=random.randint(0,len(equipe_ennemie)-1)
            while(equipe_ennemie[indice_cible_random].pv_actuels<=0):
                indice_cible_random=random.randint(0,len(equipe_ennemie)-1)
            cible_2=equipe_ennemie[indice_cible_random]
            degats=CalculDommage(fee,3.4,fee.capacite2BonusSkill,cible_2)
            AffichageTypeDeCoup(fee,3.4,fee.capacite2BonusSkill,degats,cible_2)
            degats=ReductionDommage(degats,cible_2)
            Procedure_attaque(fee,degats,cible_2)
            ''' La comparaison s'effectue bien, même si les PV actuels ne sont plus les mêmes '''
            if(cible==cible_2):
                print(cible_2.surnom,cible_2.attribut,' est étourdi(e)!! \n')
                cible_2.stun=1
        return equipe_ennemie

    def PluieDouleur(fee,equipe_ennemie):
        nb_attaques=random.randint(4,6)
        print('\n',fee.surnom,fee.attribut,' attaque toute l\'équipe ennemie avec une pluie de flèches magiques aléatoires!!\n')
        for i in range(nb_attaques):
            if(isAlive(equipe_ennemie)):
                indice_cible=random.randint(0,len(equipe_ennemie)-1)
                while(equipe_ennemie[indice_cible].pv_actuels<=0):
                    indice_cible=random.randint(0,len(equipe_ennemie)-1)
                cible=equipe_ennemie[indice_cible]
                degats=CalculDommage(fee,0.85*len(equipe_ennemie),fee.capacite3BonusSkill,cible)
                AffichageTypeDeCoup(fee,0.85,fee.capacite3BonusSkill,0.85*len(equipe_ennemie),cible)
                degats=ReductionDommage(degats,cible)
                Procedure_attaque(fee,degats,cible)
                if(cible.immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(0.2,cible.resistance_actuelle,fee.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        Slow_down(cible,2)
        return equipe_ennemie

    def Benediction(equipe_alliee):
        print('\nToute l\'équipe est bénie par la Déesse de la Lumière!!\n')
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels>0):
                if(equipe_alliee[i].perturbation_recup>0):
                    print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces!!\n')
                else:
                    montant=Arrondir(0.2*equipe_alliee[i].pv_max_donjons)
                    equipe_alliee[i]=Monstre.etreSoigne(equipe_alliee[i],montant)
                equipe_alliee[i].jauge_attaque+=max(20,Arrondir(0.2*equipe_alliee[i].jauge_attaque))
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit sa jauge d\'attaque augmenter de 20%!!')
            else:
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est mort!! \n')
            print('\n')
        return equipe_alliee

    def Support(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].resistance_max_donjons+=0.2
            equipe_alliee[i].resistance_actuelle+=0.2
            print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 20%!!')
            print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].resistance_actuelle,'\n')
        return equipe_alliee

    def AntiSupport(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].resistance_actuelle-=0.2
        return equipe_alliee


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

            self.capacite1=DameHarpie.Griffe
            self.capacite1Nom='Griffe Céleste'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=DameHarpie.Plumes
            self.capacite2Nom='Pluie de Plumes'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=DameHarpie.AuraFlamboyante
            self.Anti_leader_skill=DameHarpie.AntiAuraFlamboyante

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

            self.capacite1=DameHarpie.Griffe
            self.capacite1Nom='Griffe Céleste'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=DameHarpie.Serres
            self.capacite2Nom='Serres Céleste'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=DameHarpie.Laceration
            self.capacite3Nom='Lacération Céleste'
            self.capacite3BonusSkill=0
            self.Trecharge3=4
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=DameHarpie.Griffe
            self.capacite1Nom='Griffe Céleste'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=DameHarpie.Plumes
            self.capacite2Nom='Pluie de Plumes'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=DameHarpie.Laceration2
            self.capacite3Nom='Lacération Céleste'
            self.capacite3BonusSkill=0
            self.Trecharge3=4
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=DameHarpie.Griffe
            self.capacite1Nom='Griffe Céleste'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=DameHarpie.Plumes
            self.capacite2Nom='Pluie de Plumes'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=DameHarpie.Danse
            self.capacite3Nom='Danse Divine'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=DameHarpie.Griffe
            self.capacite1Nom='Griffe Céleste'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=DameHarpie.Serres
            self.capacite2Nom='Serres Céleste'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=DameHarpie.AuraDemoniaque
            self.Anti_leader_skill=DameHarpie.AntiAuraDemoniaque

    def Griffe(dh,cible):
        print('\n',dh.surnom,dh.attribut,' griffe sauvagement ',cible.surnom,cible.attribut,'!!\n')
        degats=(-20)+CalculDommage(dh,3.7,dh.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(dh,3.7,dh.capacite1BonusSkill,degats+20,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(dh,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,dh.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Def_break(cible,2)
        return cible

    def Serres(dh,cible):
        print('\n',dh.surnom,dh.attribut,' lacère sauvagement ',cible.surnom,cible.attribut,' avec ses serres!!\n')
        for i in range(2):
            degats=CalculDommage(dh,2.7,dh.capacite2BonusSkill,cible)
            Type_coup=AffichageTypeDeCoup(dh,2.7,dh.capacite2BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(dh,degats,cible)
            if(Type_coup=='Critique'):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1
        return cible

    def Plumes(dh,equipe_ennemie):
        print('\n',dh.surnom,dh.attribut,' attaque toute l\'équipe ennemie avec une pluie de plumes tranchantes aléatoires!!\n')
        nb_ennemis_vivants=0
        for j in range(len(equipe_ennemie)):
            if(equipe_ennemie[j].pv_actuels>0):
                nb_ennemis_vivants+=1
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie)):
                indice_cible=random.randint(0,len(equipe_ennemie)-1)
                while(equipe_ennemie[indice_cible].pv_actuels<=0):
                    indice_cible=random.randint(0,len(equipe_ennemie)-1)
                cible=equipe_ennemie[indice_cible]
                ''' Peut monter jusqu'à 7.8 dans les donjons OMG '''
                degats=CalculDommage(dh,2.6*nb_ennemis_vivants,dh.capacite2BonusSkill,cible)
                AffichageTypeDeCoup(dh,2.6*nb_ennemis_vivants,dh.capacite2BonusSkill,degats,cible)
                degats=ReductionDommage(degats,cible)
                Procedure_attaque(dh,degats,cible)
        return equipe_ennemie

    def Danse(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].jauge_attaque+=max(30,Arrondir(0.3*equipe_alliee[i].jauge_attaque))
            print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,'voit sa jauge d\'attaque augmenter de 30!!')
            Espada(equipe_alliee[i],3)
        return equipe_alliee

    def Laceration(dh,cible):
        print('\n',dh.surnom,dh.attribut,' fend les cieux pour lacérer mortellement ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(dh,7,dh.capacite3BonusSkill,cible)
        AffichageTypeDeCoup(dh,7,dh.capacite3BonusSkill,degats,cible)
        degats+=Arrondir(dh.attaque_actuelle*7*dh.dommages_critiques_actuels)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(dh,degats,cible)
        return cible

    def Laceration2(dh,cible):
        print('\n',dh.surnom,dh.attribut,' fend les cieux pour lacérer mortellement ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(dh,7,dh.capacite3BonusSkill,cible)
        AffichageTypeDeCoup(dh,7,dh.capacite3BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(dh,degats,cible)
        print(cible.surnom,cible.attribut,' est étourdi(e)!!\n')
        cible.stun=1
        Def_break(cible,2)
        return cible

    def AuraFlamboyante(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Feu'):
                equipe_alliee[i].attaque_actuelle+=Arrondir(0.3*equipe_alliee[i].attaque_max_donjons)
                equipe_alliee[i].attaque_max_donjons+=Arrondir(0.3*equipe_alliee[i].attaque_max_donjons)
                print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 30%!!')
                print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].attaque_actuelle,'\n')
        return equipe_alliee

    def AuraDemoniaque(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].attaque_actuelle+=Arrondir(0.3*equipe_alliee[i].attaque_max_donjons)
                equipe_alliee[i].attaque_max_donjons+=Arrondir(0.3*equipe_alliee[i].attaque_max_donjons)
                print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 30%!!')
                print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].attaque_actuelle,'\n')
        return equipe_alliee

    def AntiAuraFlamboyante(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Feu'):
                equipe_alliee[i].attaque_actuelle-=Arrondir(0.3*equipe_alliee[i].attaque_max_donjons)
        return equipe_alliee

    def AntiAuraDemoniaque(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].attaque_actuelle-=Arrondir(0.3*equipe_alliee[i].attaque_max_donjons)
        return equipe_alliee


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

            self.capacite1=Inugami.Griffe
            self.capacite1Nom='Griffe Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Inugami.Coop
            self.capacite2Nom='Attaque en groupe'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

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

            self.capacite1=Inugami.Griffe
            self.capacite1Nom='Griffe Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Inugami.Coop
            self.capacite2Nom='Attaque en groupe'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Inugami.ChefDeMeuteEau
            self.Anti_leader_skill=Inugami.AntiChefDeMeuteEau

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

            self.capacite1=Inugami.Griffe
            self.capacite1Nom='Griffe Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Inugami.Entaille
            self.capacite2Nom='Entaille Vicieuse'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Inugami.ChefDeMeuteVent
            self.Anti_leader_skill=Inugami.AntiChefDeMeuteVent

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

            self.capacite1=Inugami.Griffe
            self.capacite1Nom='Griffe Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Inugami.Entaille
            self.capacite2Nom='Entaille Vicieuse'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Inugami.Hurlement
            self.capacite3Nom='Hurlement'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Inugami.Griffe
            self.capacite1Nom='Griffe Acier'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Inugami.Coop
            self.capacite2Nom='Attaque en groupe'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Inugami.Laceration
            self.capacite3Nom='Lacération Profonde'
            self.capacite3BonusSkill=0
            self.Trecharge3=4
            self.attente3=0
            self.etatCap3='dispo'

    ''' Pour toutes les compétences suivantes '''
    ''' La condition marche car on ne peut pas renommer son montre 'Inugami bleu Royal' '''
    ''' Les espaces n'étant pas autorisés dans les surnoms, il est impossible de tricher '''

    def Griffe(inu,cible):
        print('\n',inu.surnom,inu.attribut,' griffe sauvagement ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(inu,3.7,inu.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(inu,3.7,inu.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        # On n'utilise pas Procedure_attaque ici car passif Aneantissement
        # tour_supplementaire_tmp augmente de 1 si la cible est tuée
        if (degats<=0):
            degats=1
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
            if (inu.perturbation_recup<=0):
                inu=Monstre.etreSoigne(inu,math.floor(inu.vol_de_vie*degats/100))
        else:
            print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if (cible.pv_actuels<=0 and (inu.attribut=='Feu' or inu.surnom=='Inugami bleu Royal')):
            inu.tour_supplementaire_tmp+=1
        elif(cible.pv_actuels<=0):
            print(cible.surnom,cible.attribut,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,inu.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Def_break(cible,2)
        return cible

    def Entaille(inu,cible):
        print('\n',inu.surnom,inu.attribut,' lacère profondément ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(inu,5.5,inu.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(inu,5.5,inu.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        if (degats<=0):
            degats=1
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
            if (inu.perturbation_recup<=0):
                inu=Monstre.etreSoigne(inu,math.floor(inu.vol_de_vie*degats/100))
        else:
            print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if (cible.pv_actuels<=0 and (inu.attribut=='Feu' or inu.surnom=='Inugami bleu Royal')):
            inu.tour_supplementaire_tmp+=1
        elif(cible.pv_actuels<=0):
            print(cible.surnom,cible.attribut,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')
        cible=SoignerDeTousLesBiens(cible)
        print(cible.surnom,cible.attribut,' perd tous les bonus qu\'il avait!! \n')
        return cible

    def Coop(inu,equipe_alliee,cible):
        possibilites_coop=[]
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels>0 and (equipe_alliee[i]!=inu)):
                possibilites_coop.append(i)
        if(len(possibilites_coop)>0):
            indice_random=random.randint(0,len(possibilites_coop)-1)
            indice=possibilites_coop[indice_random]
            allie=equipe_alliee[indice]
            print('\n',inu.surnom,inu.attribut,' et ',allie.surnom,allie.attribut,' lancent une attaque combinée sur ',cible.surnom,cible.attribut,'!!\n')
            degats=CalculDommage(inu,3.7,inu.capacite2BonusSkill,cible)
            AffichageTypeDeCoup(inu,3.7,inu.capacite2BonusSkill,degats,cible)
            degats2=CalculDommage(allie,3.7,allie.capacite1BonusSkill,cible)
            AffichageTypeDeCoup(allie,3.7,allie.capacite1BonusSkill,degats2,cible)
            degats+=degats2
            degats=ReductionDommage(degats,cible)
            if (degats<=0):
                degats=1
            if(cible.immortalite<=0):
                cible=(Monstre.recoitDegats(cible,degats))
                print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
                if (inu.perturbation_recup<=0):
                    inu=Monstre.etreSoigne(inu,math.floor(inu.vol_de_vie*degats/100))
            else:
                print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
            if (cible.pv_actuels<=0 and (inu.attribut=='Feu' or inu.surnom=='Inugami bleu Royal')):
                inu.tour_supplementaire_tmp+=1
            elif(cible.pv_actuels<=0):
                print(cible.surnom,cible.attribut,' est mort!! \n')
            else:
                print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')
        return cible

    def Hurlement(equipe_alliee):
        print('\nToute l\'équipe est galvanisée par un hurlement sauvage!!\n')
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels>0):
                if(equipe_alliee[i].perturbation_recup<=0):
                    montant=Arrondir(0.3*equipe_alliee[i].pv_max_donjons)
                    equipe_alliee[i]=Monstre.etreSoigne(equipe_alliee[i],montant)
                equipe_alliee[i].jauge_attaque+=max(30,Arrondir(0.3*equipe_alliee[i].jauge_attaque))
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,'voit sa jauge d\'attaque augmenter de 30!!')
        return equipe_alliee

    def Laceration(inu,cible):
        print('\n',inu.surnom,inu.attribut,' lacère profondément ',cible.surnom,cible.attribut,' en rouvrant ses cicatrices!!\n')
        degats=CalculDommage(inu,5.7,inu.capacite3BonusSkill,cible)
        AffichageTypeDeCoup(inu,5.7,inu.capacite3BonusSkill,degats,cible)
        nb_effets_nocifs_cible=NbEffetsNocifs(cible)
        for k in range(nb_effets_nocifs_cible):
            degats+=Arrondir(0.5*degats)
        degats=ReductionDommage(degats,cible)
        if (degats<=0):
            degats=1
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
            if (inu.perturbation_recup<=0):
                inu=Monstre.etreSoigne(inu,math.floor(inu.vol_de_vie*degats/100))
        else:
            print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if (cible.pv_actuels<=0 and (inu.attribut=='Feu' or inu.surnom=='Inugami bleu Royal')):
            inu.tour_supplementaire_tmp+=1
        elif(cible.pv_actuels<=0):
            print(cible.surnom,cible.attribut,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')
        return cible

    def ChefDeMeuteEau(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].vitesse_actuelle+=Arrondir(0.23*equipe_alliee[i].vitesse_max_donjons)
                equipe_alliee[i].vitesse_max_donjons+=Arrondir(0.23*equipe_alliee[i].vitesse_max_donjons)
                print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 23%!!')
                print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].vitesse_actuelle,'\n')
        return equipe_alliee

    def ChefDeMeuteVent(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Vent'):
                equipe_alliee[i].vitesse_actuelle+=Arrondir(0.23*equipe_alliee[i].vitesse_max_donjons)
                equipe_alliee[i].vitesse_max_donjons+=Arrondir(0.23*equipe_alliee[i].vitesse_max_donjons)
                print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 23%!!')
                print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].vitesse_actuelle,'\n')
        return equipe_alliee

    def AntiChefDeMeuteEau(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].vitesse_actuelle-=Arrondir(0.23*equipe_alliee[i].vitesse_max_donjons)
        return equipe_alliee

    def AntiChefDeMeuteVent(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Vent'):
                equipe_alliee[i].vitesse_actuelle-=Arrondir(0.23*equipe_alliee[i].vitesse_max_donjons)
        return equipe_alliee


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

            self.capacite1=Golem.Impact
            self.capacite1Nom='Impact'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Golem.CorpsLave
            self.capacite2Nom='Corps de Lave'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Golem.Barriere
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

            self.capacite1=Golem.Impact
            self.capacite1Nom='Impact'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Golem.CorpsGlace
            self.capacite2Nom='Corps de Glace'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Golem.Barriere
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

            self.capacite1=Golem.Impact
            self.capacite1Nom='Impact'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Golem.MurDeFer
            self.capacite2Nom='Mur de Fer'
            self.capacite2BonusSkill=0
            self.Trecharge2=5
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Golem.TankDeVent
            self.Anti_leader_skill=Golem.AntiTankDeVent

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

            self.capacite1=Golem.Impact
            self.capacite1Nom='Impact'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Golem.MurDeFer
            self.capacite2Nom='Mur de Fer'
            self.capacite2BonusSkill=0
            self.Trecharge2=5
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Golem.TankDeLumiere
            self.Anti_leader_skill=Golem.AntiTankDeLumiere

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

            self.capacite1=Golem.Impact
            self.capacite1Nom='Impact'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Golem.CorpsLave
            self.capacite2Nom='Corps de Ténèbres'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.pourcentage_reflexion_dommages=0.15
            self.reflexion_dommages=1


    def Impact(golem,cible):
        print('\n',golem.surnom,golem.attribut,' projette une onde de choc dévastatrice sur ',cible.surnom,cible.attribut,'!!\n')
        degats=(Arrondir(2.5*golem.defense_actuelle))+CalculDommage(golem,1.8,golem.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(golem,1.8,golem.capacite1BonusSkill,degats-(Arrondir(2.5*(golem.defense_actuelle))),cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(golem,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.25,cible.resistance_actuelle,golem.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1
            Limite_reussite_2=CalculTauxReussiteEffet(0.1,cible.resistance_actuelle,golem.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite_2):
                print(cible.surnom,cible.attribut,' est provoqué par ',golem.surnom,golem.attribut,' pour un tour!! \n')
                cible.provoque=1
                cible.tours_provoque=max(2,cible.tours_provoque)
                golem.provocation=1
                golem.tours_provocation=2
        return cible

    def CorpsLave(golem,equipe_ennemie):
        if(golem.attribut=='Feu'):
            print('\n',golem.surnom,golem.attribut,' écrase toute l\'équipe ennemie avec son corps de lave!!\n')
        elif(golem.attribut=='Ténèbres'):
            print('\n',golem.surnom,golem.attribut,' écrase toute l\'équipe ennemie avec son corps de ténèbres!!\n')
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                degats=(Arrondir(2.5*golem.defense_actuelle))+CalculDommage(golem,1.8,golem.capacite2BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(golem,1.8,golem.capacite2BonusSkill,degats-(Arrondir(2.5*golem.defense_actuelle)),equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(golem,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    Degats_continus(equipe_ennemie[i],1,3)
        return equipe_ennemie

    def CorpsGlace(golem,equipe_ennemie):
        print('\n',golem.surnom,golem.attribut,' écrase toute l\'équipe ennemie avec son corps de glace!!\n')
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                degats=(Arrondir(2.5*golem.defense_actuelle))+CalculDommage(golem,2.5,golem.capacite2BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(golem,2.5,golem.capacite2BonusSkill,degats-(Arrondir(2.5*golem.defense_actuelle)),equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(golem,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(0.5,equipe_ennemie[i].resistance_actuelle,golem.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' est gelé(e)!! \n')
                        equipe_ennemie[i].gel=1
        return equipe_ennemie

    def MurDeFer(golem):
        print('\n',golem.surnom,golem.attribut,' se transforme en mur de fer!!\n')
        Tanky(golem,3)
        Immunity(golem,3)
        print('Sa jauge d\'attaque augmente à nouveau immédiatement!! \n')
        golem.jauge_attaque+=max(50,Arrondir(0.5*golem.jauge_attaque))
        return golem


    def Barriere(equipe_alliee):
        liste_noms_alternatifs=['Golem rouge','Grand golem rouge','Golem rouge géant','Golem rouge Royal','Golem bleu','Grand golem bleu','Golem bleu géant']
        for i in range(len(equipe_alliee)):
            if((equipe_alliee[i].nom=='Golem' and (equipe_alliee[i].attribut=='Feu' or equipe_alliee[i].attribut=='Eau')) or (equipe_alliee[i].nom in liste_noms_alternatifs)):
                if(equipe_alliee[i].passif_active!=1 and equipe_alliee[i].pv_actuels<=0.5*equipe_alliee[i].pv_max_donjons):
                    print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit sa réduction de dégâts augmenter!!\n')
                    equipe_alliee[i].reduction_de_degats+=0.5
                    equipe_alliee[i].passif_active=1
        return equipe_alliee


    def TankDeVent(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Vent'):
                equipe_alliee[i].pv_actuels+=Arrondir(0.3*equipe_alliee[i].pv_max_donjons)
                equipe_alliee[i].pv_max_donjons+=Arrondir(0.3*equipe_alliee[i].pv_max_donjons)
                print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 30%!!')
                print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].pv_actuels,'\n')
        return equipe_alliee

    def TankDeLumiere(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Lumière'):
                equipe_alliee[i].pv_actuels+=Arrondir(0.3*equipe_alliee[i].pv_max_donjons)
                equipe_alliee[i].pv_max_donjons+=Arrondir(0.3*equipe_alliee[i].pv_max_donjons)
                print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 30%!!')
                print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].pv_actuels,'\n')
        return equipe_alliee

    def AntiTankDeVent(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Vent'):
                equipe_alliee[i].pv_actuels-=Arrondir(0.3*equipe_alliee[i].pv_max_donjons)
        return equipe_alliee

    def AntiTankDeLumiere(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Lumière'):
                equipe_alliee[i].pv_actuels-=Arrondir(0.3*equipe_alliee[i].pv_max_donjons)
        return equipe_alliee



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

            self.capacite1=Mastodonte.Corne
            self.capacite1Nom='Coup de Corne'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Mastodonte.PluieGravats
            self.capacite2Nom='Pluie de Gravats'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Mastodonte.PeauDure
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

            self.capacite1=Mastodonte.Corne
            self.capacite1Nom='Coup de Corne'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Mastodonte.ArmureGlace
            self.capacite2Nom='Armure de Glace'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Mastodonte.PeauDure
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

            self.capacite1=Mastodonte.Corne
            self.capacite1Nom='Coup de Corne'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Mastodonte.Charge
            self.capacite2Nom='Charge Dévastatrice'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Mastodonte.PeauDure
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

            self.capacite1=Mastodonte.Corne
            self.capacite1Nom='Coup de Corne'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Mastodonte.Charge
            self.capacite2Nom='Charge Dévastatrice'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Mastodonte.PeauDure
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

            self.capacite1=Mastodonte.Corne
            self.capacite1Nom='Coup de Corne'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Mastodonte.PluieGravats
            self.capacite2Nom='Pluie de Gravats'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Mastodonte.PeauDure
            self.passif_active=0


    def Corne(mastoc,cible):
        print('\n',mastoc.surnom,mastoc.attribut,' envoie valdinguer ',cible.surnom,cible.attribut,' d\'un puissant coup de corne!!\n')
        degats=CalculDommage(mastoc,4,mastoc.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(mastoc,4,mastoc.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(mastoc,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,mastoc.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1
        return cible

    def PluieGravats(mastoc,equipe_ennemie):
        print('\n',mastoc.surnom,mastoc.attribut,' déclenche une pluie de gravats!!\n')
        nb_ennemis_vivants=0
        for j in range(len(equipe_ennemie)):
            if(equipe_ennemie[j].pv_actuels>0):
                nb_ennemis_vivants+=1
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' reçoit la pluie de gravats!!')
                degats=CalculDommage(mastoc,2.4*nb_ennemis_vivants,mastoc.capacite2BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(mastoc,2.4*nb_ennemis_vivants,mastoc.capacite2BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(mastoc,degats,equipe_ennemie[i])
        return equipe_ennemie

    def Charge(mastoc,cible):
        print('\n',mastoc.surnom,mastoc.attribut,' charge sur ',cible.surnom,cible.attribut,' à pleine vitesse!!\n')
        degats=4*mastoc.vitesse_actuelle+CalculDommage(mastoc,1.6,mastoc.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(mastoc,1.6,mastoc.capacite2BonusSkill,degats-4*mastoc.vitesse_actuelle,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(mastoc,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.8,cible.resistance_actuelle,mastoc.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                cible.stun=1
        return cible

    def ArmureGlace(mastoc):
        print('\n',mastoc.surnom,mastoc.attribut,' se renforce d\'une armure de glace!!\n')
        Tanky(mastoc,3)
        Immunity(mastoc,3)
        print('Il renverra une partie des dégâts subis pour trois tours!! \n')
        mastoc.reflexion_dommages=1
        mastoc.pourcentage_reflexion_dommages+=0.15
        mastoc.tours_reflexion_dommages=max(mastoc.tours_reflexion_dommages,3)
        return mastoc

    def PeauDure(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='Mastodonte' or equipe_alliee[i].nom=='Mastodonte noir Royal'):
                if(equipe_alliee[i].passif_active!=1 and equipe_alliee[i].pv_actuels<=0.5*equipe_alliee[i].pv_max_donjons):
                    print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit sa défense augmenter!!\n')
                    equipe_alliee[i].defense_actuelle+=equipe_alliee[i].defense_max_donjons
                    equipe_alliee[i].passif_active=1
        return equipe_alliee


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

            self.capacite1=Serpent.Morsure
            self.capacite1Nom='Morsure'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Serpent.Deflagration
            self.capacite2Nom='Déflagration'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Serpent.TankArena
            self.Anti_leader_skill=Serpent.AntiTankArena

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

            self.capacite1=Serpent.Morsure
            self.capacite1Nom='Morsure'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Serpent.Deflagration
            self.capacite2Nom='Déflagration'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Serpent.Tsunami
            self.capacite3Nom='Raz de Marée'
            self.capacite3BonusSkill=0
            self.Trecharge3=4
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Serpent.Morsure
            self.capacite1Nom='Morsure'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Serpent.Orage
            self.capacite2Nom='Orage d\'Eclairs'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Serpent.CoupeFeu

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

            self.capacite1=Serpent.Morsure
            self.capacite1Nom='Morsure'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Serpent.Deflagration
            self.capacite2Nom='Déflagration'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Serpent.Renforcement
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

            self.capacite1=Serpent.Morsure
            self.capacite1Nom='Morsure'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Serpent.Orage
            self.capacite2Nom='Orage d\'Eclairs'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Serpent.TankArena
            self.Anti_leader_skill=Serpent.AntiTankArena

    def Morsure(snake,cible):
        print('\n',snake.surnom,snake.attribut,' mord profondément ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(snake,4,snake.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(snake,4,snake.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(snake,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.75,cible.resistance_actuelle,snake.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Retirer_un_bonus(cible)
        return cible

    def Deflagration(snake,cible):
        print('\n',snake.surnom,snake.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'une puissante déflagration!!\n')
        for i in range(3):
            degats=CalculDommage(snake,0.8,snake.capacite2BonusSkill,cible)
            AffichageTypeDeCoup(snake,0.8,snake.capacite2BonusSkill,degats,cible)
            degats+=Arrondir(0.08*snake.pv_max_donjons)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(snake,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.3,cible.resistance_actuelle,snake.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    print(cible.surnom,cible.attribut,' voit sa jauge d\'attaque diminuer de 30%!!\n')
                    cible.jauge_attaque-=max(30,Arrondir(0.3*cible.jauge_attaque))
        return cible

    def Tsunami(snake,equipe_ennemie):
        print('\n',snake.surnom,snake.attribut,' attaque toute l\'équipe ennemie avec un terrifiant raz de marée!!\n')
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' reçoit le tsunami!!')
                degats=Arrondir(0.28*snake.pv_max_donjons)
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(snake,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' voit sa jauge d\'attaque diminuer de 30%!!\n')
                    equipe_ennemie[i].jauge_attaque-=max(30,Arrondir(0.3*equipe_ennemie[i].jauge_attaque))
        return equipe_ennemie

    def Orage(snake,equipe_ennemie):
        print('\n',snake.surnom,snake.attribut,' attaque toute l\'équipe ennemie avec un orage d\'éclairs!!\n')
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' reçoit la foudre!!')
                degats=CalculDommage(snake,1,snake.capacite2BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(snake,1,snake.capacite2BonusSkill,degats,equipe_ennemie[i])
                degats+=Arrondir(0.16*snake.pv_max_donjons)
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(snake,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(1,equipe_ennemie[i].resistance_actuelle,snake.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        Slow_down(equipe_ennemie[i],2)
        return equipe_ennemie

    def TankArena(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].pv_actuels+=Arrondir(0.21*equipe_alliee[i].pv_max_donjons)
            equipe_alliee[i].pv_max_donjons+=Arrondir(0.21*equipe_alliee[i].pv_max_donjons)
            print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 21%!!')
            print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].pv_actuels,'\n')
        return equipe_alliee

    def AntiTankArena(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].pv_actuels-=Arrondir(0.21*equipe_alliee[i].pv_max_donjons)
        return equipe_alliee

    def CoupeFeu(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='Serpent' and equipe_alliee[i].attribut=='Vent'):
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,'subira deux fois moins de dégâts face à l\'Attribut Feu!!')
        return equipe_alliee

    def Renforcement(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='Serpent' and equipe_alliee[i].attribut=='Lumière'):
                print('\n(Ré)actualisation du passif... ')
                equipe_alliee[i].defense_actuelle-=Arrondir(0.2*equipe_alliee[i].defense_max_donjons*equipe_alliee[i].nb_effets_renforcement)
                equipe_alliee[i].attaque_actuelle-=Arrondir(0.2*equipe_alliee[i].attaque_max_donjons*equipe_alliee[i].nb_effets_renforcement)
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' perd ',20*equipe_alliee[i].nb_effets_renforcement,'% d\'attaque et de défense grâce à son passif!! \n')
                equipe_alliee[i].nb_effets_renforcement=min(equipe_alliee[i].nb_coups_subis,10)
                equipe_alliee[i].defense_actuelle+=Arrondir(0.2*equipe_alliee[i].defense_max_donjons*equipe_alliee[i].nb_effets_renforcement)
                equipe_alliee[i].attaque_actuelle+=Arrondir(0.2*equipe_alliee[i].attaque_max_donjons*equipe_alliee[i].nb_effets_renforcement)
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' gagne ',20*equipe_alliee[i].nb_effets_renforcement,'% d\'attaque et de défense grâce à son passif car il a désormais subis ',equipe_alliee[i].nb_effets_renforcement,' coups!! \n')
        return equipe_alliee


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

            self.capacite1=Griffon.Griffes
            self.capacite1Nom='Griffes'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Griffon.Ecrasement
            self.capacite2Nom='Ecrasement'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Griffon.Tornade
            self.capacite3Nom='Tornade'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Griffon.Griffes
            self.capacite1Nom='Griffes'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Griffon.Laceration
            self.capacite2Nom='Lacération'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Griffon.WaterPower
            self.Anti_leader_skill=Griffon.AntiWaterPower

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

            self.capacite1=Griffon.Griffes
            self.capacite1Nom='Griffes'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Griffon.Laceration
            self.capacite2Nom='Lacération'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Griffon.Acceleration
            self.capacite3Nom='Accélération'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Griffon.Griffes
            self.capacite1Nom='Griffes'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Griffon.Ecrasement
            self.capacite2Nom='Ecrasement'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Griffon.BouclierLumiere

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

            self.capacite1=Griffon.Griffes
            self.capacite1Nom='Griffes'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Griffon.Laceration
            self.capacite2Nom='Lacération'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Griffon.BouclierTenebres

    def Griffes(gri,cible):
        print('\n',gri.surnom,gri.attribut,' griffe profondément ',cible.surnom,cible.attribut,'!!\n')
        degats=Arrondir((90+gri.vitesse_actuelle)/0.55)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(gri,degats,cible)
        return cible

    def Laceration(gri,cible):
        print('\n',gri.surnom,gri.attribut,' découpe ',cible.surnom,cible.attribut,' en morceaux!!\n')
        degats=CalculDommage(gri,5.1,gri.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(gri,5.1,gri.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(gri,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,gri.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Def_break(cible,2)
                Atk_break(cible,2)
        return cible

    def Ecrasement(gri,cible):
        print('\n',gri.surnom,gri.attribut,' s\'écrase de tout son poids sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(gri,3.5,gri.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(gri,3.5,gri.capacite2BonusSkill,degats,cible)
        degats+=Arrondir(0.18*cible.pv_max_donjons)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(gri,degats,cible)
        print(gri.surnom,gri.attribut,' est heurté par le contrecoup!!')
        print(gri.surnom,gri.attribut,' subit ',Arrondir(0.1*gri.pv_max_donjons),' points de dégâts!!')
        gri.pv_actuels-=Arrondir(0.1*gri.pv_max_donjons)
        if(gri.pv_actuels<=0):
            print(gri.surnom,gri.attribut,' est mort!!')
        print('\n')
        return cible

    def Tornade(gri,equipe_ennemie):
        print('\n',gri.surnom,gri.attribut,' balaye toute l\'équipe ennemie avec une violente tornade!!\n')
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' reçoit la tornade!!')
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(1,equipe_ennemie[i].resistance_actuelle,gri.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Slow_down(equipe_ennemie[i],2)
                Limite_reussite_2=CalculTauxReussiteEffet(0.5,equipe_ennemie[i].resistance_actuelle,gri.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite_2):
                    print('\n',equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' voit sa jauge d\'attaque diminuer de 30%!!')
                    equipe_ennemie[i].jauge_attaque-=max(30,Arrondir(0.3*equipe_ennemie.jauge_attaque))
        return equipe_ennemie

    def Acceleration(equipe_alliee):
        print('\nUn vent bénéfique vient accélérer toute l\'équipe!!\n')
        for i in range(len(equipe_alliee)):
            if (equipe_alliee[i].pv_actuels>0):
                Speed_up(equipe_alliee[i],2)
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit sa jauge d\'attaque augmenter de 30%!!\n')
                equipe_alliee[i].jauge_attaque+=max(30,Arrondir(0.3*equipe_alliee[i].jauge_attaque))
        return equipe_alliee

    def BouclierLumiere(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='Griffon' and equipe_alliee[i].attribut=='Lumière'):
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit sa résistance augmenter!!\n')
                equipe_alliee[i].resistance_actuelle+=0.2
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' subira deux fois moins de dégâts face à l\'Attribut Ténèbres!!')
        return equipe_alliee

    def AntiBouclierLumiere(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='Griffon' and equipe_alliee[i].attribut=='Lumière'):
                equipe_alliee[i].resistance_actuelle-=0.2
        return equipe_alliee

    def BouclierTenebres(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='Griffon' and equipe_alliee[i].attribut=='Ténèbres'):
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit son vol de vie augmenter!!\n')
                equipe_alliee[i].vol_de_vie+=20
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' subira deux fois moins de dégâts face à l\'Attribut Lumière!!')
        return equipe_alliee

    def AntiBouclierTenebres(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='Griffon' and equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].vol_de_vie-=20

    def WaterPower(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].attaque_actuelle+=Arrondir(0.3*equipe_alliee[i].attaque_max_donjons)
                equipe_alliee[i].attaque_max_donjons+=Arrondir(0.3*equipe_alliee[i].attaque_max_donjons)
                print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 30%!!')
                print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].attaque_actuelle,'\n')
        return equipe_alliee

    def AntiWaterPower(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].attaque_actuelle-=Arrondir(0.3*equipe_alliee[i].attaque_max_donjons)
        return equipe_alliee


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

            self.capacite1=Inferno.Frappe
            self.capacite1Nom='Frappe'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Inferno.Deflagration
            self.capacite2Nom='Déflagration'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Inferno.CritiqueEnflammee
            self.Anti_leader_skill=Inferno.AntiCritiqueEnflammee

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

            self.capacite1=Inferno.Frappe
            self.capacite1Nom='Frappe'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Inferno.Perforation
            self.capacite2Nom='Perforation'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Inferno.Adrenaline
            self.capacite3Nom='Adrénaline'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Inferno.CritiqueGelee
            self.Anti_leader_skill=Inferno.AntiCritiqueGelee

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

            self.capacite1=Inferno.Frappe
            self.capacite1Nom='Frappe'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Inferno.Orage
            self.capacite2Nom='Orage d\'Eclairs'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Inferno.CoupMortel
            self.capacite3Nom='Coup Mortel'
            self.capacite3BonusSkill=0
            self.Trecharge3=4
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Inferno.Frappe
            self.capacite1Nom='Frappe'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Inferno.Perforation
            self.capacite2Nom='Perforation'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Inferno.JugementDivin
            self.capacite3Nom='Jugement Divin'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Inferno.Frappe
            self.capacite1Nom='Frappe'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Inferno.Deflagration
            self.capacite2Nom='Déflagration'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Inferno.CritiqueSombre
            self.Anti_leader_skill=Inferno.AntiCritiqueSombre

    def Frappe(hell,cible):
        print('\n',hell.surnom,hell.attribut,' frappe violemment ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(hell,3.9,hell.capacite1BonusSkill,cible)
        Type_coup=AffichageTypeDeCoup(hell,3.9,hell.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(hell,degats,cible)
        if(Type_coup=='Critique'):
            print(hell.surnom,hell.attribut,' voit sa jauge d\'attaque augmenter immédiatement!! \n')
            hell.jauge_attaque+=max(30,Arrondir(0.3*hell.jauge_attaque))
        return cible

    def Perforation(hell,cible):
        hell.taux_coup_critique_actuel+=0.5
        print('\n',hell.surnom,hell.attribut,' perfore ',cible.surnom,cible.attribut,' avec un pieux élémentaire!!\n')
        degats=CalculDommage(hell,5.5,hell.capacite2BonusSkill,cible)
        Type_coup=AffichageTypeDeCoup(hell,5.5,hell.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(hell,degats,cible)
        hell.taux_coup_critique_actuel-=0.5
        if(Type_coup=='Critique'):
            print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
            cible.stun=1
        return cible

    def Deflagration(hell,equipe_ennemie):
        print('\n',hell.surnom,hell.attribut,' attaque toute l\'équipe ennemie avec une puissante déflagration!!\n')
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' reçoit la déflagration!!')
                degats=CalculDommage(hell,2.7,hell.capacite2BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(hell,2.7,hell.capacite2BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(hell,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(0.7,equipe_ennemie[i].resistance_actuelle,hell.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        Def_break(equipe_ennemie[i],2)
        return equipe_ennemie

    def Orage(hell,equipe_ennemie):
        print('\n',hell.surnom,hell.attribut,' attaque toute l\'équipe ennemie avec un orage d\'éclairs!!\n')
        for i in range(len(equipe_ennemie)):
            if (equipe_ennemie[i].pv_actuels>0):
                print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' reçoit la foudre!!')
                degats=CalculDommage(hell,2.7,hell.capacite2BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(hell,2.7,hell.capacite2BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(hell,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(0.8,equipe_ennemie[i].resistance_actuelle,hell.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        Atk_break(equipe_ennemie[i],2)
        return equipe_ennemie

    def JugementDivin(hell,cible):
        print('\n',hell.surnom,hell.attribut,' fait s\'abattre le jugement divin sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(hell,7.7,hell.capacite3BonusSkill,cible)
        AffichageTypeDeCoup(hell,7.7,hell.capacite3BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(hell,degats,cible)
        SoignerDeTousLesBiens(cible)
        return cible

    def CoupMortel(hell,cible):
        print('\n',hell.surnom,hell.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un coup mortel!!\n')
        degats=CalculDommage(hell,7.7,hell.capacite3BonusSkill,cible)
        AffichageTypeDeCoup(hell,7.7,hell.capacite3BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(hell,degats,cible)
        print(cible.surnom,cible.attribut,' voit sa jauge d\'attaque réduite à zéro!! \n')
        cible.jauge_attaque=0
        return cible

    def Adrenaline(equipe_alliee):
        print('\nToute l\'équipe sent son adrénaline augmenter!!\n')
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].jauge_attaque+=max(50,Arrondir(0.5*equipe_alliee[i].jauge_attaque))
            print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit sa jauge d\'attaque augmenter de moitié!!')
            Espada(equipe_alliee[i],3)
        return equipe_alliee

    def CritiqueEnflammee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Feu'):
                equipe_alliee[i].taux_coup_critique_actuel+=0.23
                equipe_alliee[i].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].taux_coup_critique_actuel,'\n')
        return equipe_alliee

    def CritiqueGelee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].taux_coup_critique_actuel+=0.23
                equipe_alliee[i].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].taux_coup_critique_actuel,'\n')
        return equipe_alliee

    def CritiqueSombre(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].taux_coup_critique_actuel+=0.23
                equipe_alliee[i].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].taux_coup_critique_actuel,'\n')
        return equipe_alliee

    def AntiCritiqueEnflammee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Feu'):
                equipe_alliee[i].taux_coup_critique_actuel-=0.23
        return equipe_alliee

    def AntiCritiqueGelee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].taux_coup_critique_actuel-=0.23
        return equipe_alliee

    def AntiCritiqueSombre(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].taux_coup_critique_actuel-=0.23
        return equipe_alliee


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

            self.capacite1=HautElementaire.Projectiles
            self.capacite1Nom='Projectiles Elementaires'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=HautElementaire.Entaille
            self.capacite2Nom='Entaille Tectonique'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=HautElementaire.CritiqueEnflammee
            self.Anti_leader_skill=HautElementaire.AntiCritiqueEnflammee

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

            self.capacite1=HautElementaire.Projectiles
            self.capacite1Nom='Projectiles Elementaires'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=HautElementaire.Entaille
            self.capacite2Nom='Entaille Tectonique'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=HautElementaire.CritiqueGelee
            self.Anti_leader_skill=HautElementaire.AntiCritiqueGelee

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

            self.capacite1=HautElementaire.Projectiles
            self.capacite1Nom='Projectiles Elementaires'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=HautElementaire.Separation
            self.capacite2Nom='Séparation du Corps et de l\'Âme'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=HautElementaire.CritiqueSoufflee
            self.Anti_leader_skill=HautElementaire.AntiCritiqueSoufflee

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

            self.capacite1=HautElementaire.Projectiles
            self.capacite1Nom='Projectiles Elementaires'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=HautElementaire.Entaille
            self.capacite2Nom='Entaille Tectonique'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=HautElementaire.CritiqueEclairee
            self.Anti_leader_skill=HautElementaire.AntiCritiqueEclairee

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

            self.capacite1=HautElementaire.Projectiles
            self.capacite1Nom='Projectiles Elementaires'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=HautElementaire.Separation
            self.capacite2Nom='Séparation du Corps et de l\'Âme'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=HautElementaire.CritiqueSombre
            self.Anti_leader_skill=HautElementaire.AntiCritiqueSombre

    def Projectiles(elem,cible):
        print('\n',elem.surnom,elem.attribut,' jette deux sphères élémentaires sur ',cible.surnom,cible.attribut,'!!\n')
        for i in range(2):
            degats=CalculDommage(elem,3.8,elem.capacite1BonusSkill,cible)
            AffichageTypeDeCoup(elem,3.8,elem.capacite1BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(elem,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.2,cible.resistance_actuelle,elem.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Degats_continus(cible,1,3)
        return cible

    def Entaille(elem,cible):
        print('\n',elem.surnom,elem.attribut,' fend ',cible.surnom,cible.attribut,'en deux avec une entaille tectonique qui ignore la défense!!\n')
        degats=CalculDommage(elem,3,elem.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(elem,3,elem.capacite2BonusSkill,degats,cible)
        Procedure_attaque(elem,degats,cible)
        return cible

    def Separation(elem,cible):
        print('\n',elem.surnom,elem.attribut,' sépare le Corps et l\'Âme de ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(elem,6.3,elem.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(elem,6.3,elem.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(elem,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,elem.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Perturbation_recup(cible,2)
        if(cible.pv_actuels<=0 and elem.perturbation_recup<=0):
            print(elem.surnom,elem.attribut,' dévore l\'Âme de ',cible.surnom,cible.attribut,'!! \n')
            montant=Arrondir(0.35*elem.pv_max_donjons)
            elem=Monstre.etreSoigne(elem,montant)
        return cible

    def CritiqueEnflammee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Feu'):
                equipe_alliee[i].taux_coup_critique_actuel+=0.23
                equipe_alliee[i].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].taux_coup_critique_actuel,'\n')
        return equipe_alliee

    def CritiqueGelee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].taux_coup_critique_actuel+=0.23
                equipe_alliee[i].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].taux_coup_critique_actuel,'\n')
        return equipe_alliee

    def CritiqueSoufflee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Vent'):
                equipe_alliee[i].taux_coup_critique_actuel+=0.23
                equipe_alliee[i].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].taux_coup_critique_actuel,'\n')
        return equipe_alliee

    def CritiqueEclairee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Lumière'):
                equipe_alliee[i].taux_coup_critique_actuel+=0.23
                equipe_alliee[i].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].taux_coup_critique_actuel,'\n')
        return equipe_alliee

    def CritiqueSombre(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].taux_coup_critique_actuel+=0.23
                equipe_alliee[i].taux_coup_critique_max_donjons+=0.23
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 23%!!')
                print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].taux_coup_critique_actuel,'\n')
        return equipe_alliee

    def AntiCritiqueEnflammee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Feu'):
                equipe_alliee[i].taux_coup_critique_actuel-=0.23
        return equipe_alliee

    def AntiCritiqueGelee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].taux_coup_critique_actuel-=0.23
        return equipe_alliee

    def AntiCritiqueSoufflee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Vent'):
                equipe_alliee[i].taux_coup_critique_actuel-=0.23
        return equipe_alliee

    def AntiCritiqueEclairee(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Lumière'):
                equipe_alliee[i].taux_coup_critique_actuel-=0.23
        return equipe_alliee

    def AntiCritiqueSombre(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].taux_coup_critique_actuel-=0.23
        return equipe_alliee


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

            self.capacite1=OursDeCombat.Griffe
            self.capacite1Nom='Griffe de combat'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=OursDeCombat.Massue
            self.capacite2Nom='Massue de combat'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=OursDeCombat.BouclierEnflamme
            self.Anti_leader_skill=OursDeCombat.AntiBouclierEnflamme

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

            self.capacite1=OursDeCombat.Griffe
            self.capacite1Nom='Griffe de Combat'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=OursDeCombat.Massue
            self.capacite2Nom='Massue de combat'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=OursDeCombat.BouclierGele
            self.Anti_leader_skill=OursDeCombat.AntiBouclierGele

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

            self.capacite1=OursDeCombat.Griffe
            self.capacite1Nom='Griffe de combat'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=OursDeCombat.Cri
            self.capacite2Nom='Cri de Renforcement'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=OursDeCombat.BouclierSouffle
            self.Anti_leader_skill=OursDeCombat.AntiBouclierSouffle

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

            self.capacite1=OursDeCombat.Griffe
            self.capacite1Nom='Griffe de combat'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=OursDeCombat.Massue
            self.capacite2Nom='Massue de combat'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=OursDeCombat.BouclierEclaire
            self.Anti_leader_skill=OursDeCombat.AntiBouclierEclaire

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

            self.capacite1=OursDeCombat.Griffe
            self.capacite1Nom='Griffe de combat'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=OursDeCombat.Cri
            self.capacite2Nom='Cri de Renforcement'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=OursDeCombat.BouclierSombre
            self.Anti_leader_skill=OursDeCombat.AntiBouclierSombre

    def Griffe(ours,cible):
        print('\n',ours.surnom,ours.attribut,' griffe férocement ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(ours,3.8,ours.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(ours,3.8,ours.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(ours,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,ours.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' est provoqué(e) pour un tour!! \n')
                cible.provoque=1
                cible.tours_provoque=max(2,cible.tours_provoque)
                ours.provocation=1
                ours.tours_provocation=2
        return cible

    def Massue(ours,cible):
        print('\n',ours.surnom,ours.attribut,' abat son énorme massue sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(ours,3,ours.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(ours,3,ours.capacite2BonusSkill,degats,cible)
        degats+=Arrondir(0.15*ours.pv_max_donjons)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(ours,degats,cible)
        return cible

    def Cri(equipe_alliee):
        print('\nUn Cri de Renforcement retentit!! Toute l\'équipe voit ses forces augmenter!!\n')
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels>0):
                equipe_alliee[i]=Retirer_un_malus(equipe_alliee[i])
                equipe_alliee[i]=Retirer_un_malus(equipe_alliee[i])
                Rise(equipe_alliee[i],2)
        return equipe_alliee

    def BouclierEnflamme(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Feu'):
                equipe_alliee[i].defense_actuelle+=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
                equipe_alliee[i].defense_max_donjons+=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
                print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 30%!!')
                print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].defense_actuelle,'\n')
        return equipe_alliee

    def BouclierGele(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].defense_actuelle+=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
                equipe_alliee[i].defense_max_donjons+=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
                print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 30%!!')
                print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].defense_actuelle,'\n')
        return equipe_alliee

    def BouclierSouffle(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Vent'):
                equipe_alliee[i].defense_actuelle+=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
                equipe_alliee[i].defense_max_donjons+=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
                print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 30%!!')
                print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].defense_actuelle,'\n')
        return equipe_alliee

    def BouclierEclaire(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Lumière'):
                equipe_alliee[i].defense_actuelle+=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
                equipe_alliee[i].defense_max_donjons+=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
                print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 30%!!')
                print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].defense_actuelle,'\n')
        return equipe_alliee

    def BouclierSombre(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].defense_actuelle+=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
                equipe_alliee[i].defense_max_donjons+=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
                print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 30%!!')
                print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].defense_actuelle,'\n')
        return equipe_alliee

    def AntiBouclierEnflamme(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Feu'):
                equipe_alliee[i].defense_actuelle-=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
        return equipe_alliee

    def AntiBouclierGele(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].defense_actuelle-=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
        return equipe_alliee

    def AntiBouclierSouffle(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Vent'):
                equipe_alliee[i].defense_actuelle-=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
        return equipe_alliee

    def AntiBouclierEclaire(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Lumière'):
                equipe_alliee[i].defense_actuelle-=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
        return equipe_alliee

    def AntiBouclierSombre(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].defense_actuelle-=Arrondir(0.3*equipe_alliee[i].defense_max_donjons)
        return equipe_alliee


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

            self.capacite1=LoupGarou.Griffe
            self.capacite1Nom='Griffes impitoyables'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=LoupGarou.AttaqueSurprise
            self.capacite2Nom='Attaque surprise'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=LoupGarou.SoifDeSang

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

            self.capacite1=LoupGarou.Griffe
            self.capacite1Nom='Griffes impitoyables'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=LoupGarou.Aura
            self.capacite2Nom='Aura de Régénération'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=LoupGarou.Decoupage
            self.capacite3Nom='Découpage'
            self.capacite3BonusSkill=0
            self.Trecharge3=4
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=LoupGarou.Griffe
            self.capacite1Nom='Griffes impitoyables'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=LoupGarou.AttaqueSurprise
            self.capacite2Nom='Attaque surprise'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=LoupGarou.Predateur

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

            self.capacite1=LoupGarou.Griffe
            self.capacite1Nom='Griffes impitoyables'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=LoupGarou.Aura
            self.capacite2Nom='Aura de Régénération'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite=LoupGarou.Massacre
            self.capacite3Nom='Massacre'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=LoupGarou.Griffe
            self.capacite1Nom='Griffes impitoyables'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=LoupGarou.AttaqueSurprise
            self.capacite2Nom='Attaque Surprise'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=LoupGarou.RetourDeCoup

    def Griffe(loup,cible):
        print('\n',loup.surnom,loup.attribut,' griffe impitoyablement ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(loup,3.7,loup.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(loup,3.7,loup.capacite1BonusSkill,degats,cible)
        degats+=50
        if(loup.attribut=='Vent' and loup.sans_passif<=0):
            degats+=LoupGarou.Predateur(loup,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(loup,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,loup.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Perturbation_recup(cible,1)
        if(loup.attribut=='Ténèbres'):
            Def_break(cible,1)
        return cible

    def AttaqueSurprise(loup,cible):
        print('\n',loup.surnom,loup.attribut,' lacère rapidement ',cible.surnom,cible.attribut,' à deux reprises!!\n')
        for i in range(2):
            degats=Arrondir(0.16*loup.pv_max_donjons)
            if(loup.attribut=='Vent' and loup.sans_passif<=0):
                degats+=LoupGarou.Predateur(loup,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(loup,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.3,cible.resistance_actuelle,loup.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    print(cible.surnom,cible.attribut,' est étourdi(e)!! \n')
                    cible.stun=1
            if(loup.attribut=='Ténèbres'):
                Def_break(cible,1)
        return cible

    def Aura(equipe_alliee):
        print('\nLe pouvoir de l\'Aura décuple la régénénération de l\'équipe!!\n')
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels>0 and equipe_alliee[i].perturbation_recup<=0):
                montant=Arrondir(0.15*equipe_alliee[i].pv_max_donjons)
                equipe_alliee[i]=Monstre.etreSoigne(equipe_alliee[i],montant)
            Speed_up(equipe_alliee[i],2)
        return equipe_alliee

    def Decoupage(loup,cible):
        print('\n',loup.surnom,loup.attribut,' découpe ',cible.surnom,cible.attribut,' en morceaux!!\n')
        for i in range(3):
            degats=CalculDommage(loup,1.4,loup.capacite3BonusSkill,cible)
            AffichageTypeDeCoup(loup,1.4,loup.capacite3BonusSkill,degats,cible)
            degats+=Arrondir(0.1*loup.pv_max_donjons)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(loup,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.35,cible.resistance_actuelle,loup.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Def_break(cible,3)
            if(loup.attribut=='Ténèbres'):
                Def_break(cible,1)
        return cible

    def Massacre(loup,cible):
        print('\n',loup.surnom,loup.attribut,' se lance dans un véritable massacre!!\n')
        for i in range(4):
            degats=Arrondir(0.12*loup.pv_max_donjons)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(loup,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.35,cible.resistance_actuelle,loup.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    Retirer_un_bonus(cible)
            if(loup.attribut=='Ténèbres'):
                Def_break(cible,1)
            if(cible.pv_actuels<=0):
                loup.attente2=1
        return cible

    def SoifDeSang(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='LoupGarou' and equipe_alliee[i].attribut=='Feu'):
                print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit doubler le montant qu\'il recevra par les sorts de soin!!\n')
        return equipe_alliee

    def Predateur(loup,cible):
        bonus_de_dommages=0
        pourcentage_pv_actuels_cible=cible.pv_actuels/cible.pv_max_donjons
        pourcentage_pv_actuels_loup=loup.pv_actuels/loup.pv_max_donjons
        if(pourcentage_pv_actuels_loup>pourcentage_pv_actuels_cible):
            bonus_de_dommages=Arrondir(0.15*loup.pv_max_donjons)
        return bonus_de_dommages

    def RetourDeCoup(loup,cible):
        print('\n',loup.surnom,loup.attribut,' se venge!!\n')
        if(cible.pv_actuels>0):
            degats=Arrondir(0.12*loup.pv_max_donjons)
            degats=ReductionDommage(degats)
            if(cible.immortalite<=0):
                cible=(Monstre.recoitDegats(cible,degats))
                print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
            else:
                print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
            if (cible.pv_actuels<=0):
                print(cible.surnom,cible.attribut,' est mort!! \n')
            else:
                print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')
        return cible





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

            self.capacite1=Elfe.Salvation
            self.capacite1Nom='Salvation'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Elfe.Fleches
            self.capacite2Nom='Flèches Célestes'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Elfe.Strategie
            self.capacite3Nom='Stratégie'
            self.capacite3BonusSkill=0
            self.Trecharge3=6
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Elfe.Salvation
            self.capacite1Nom='Salvation'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Elfe.Tir
            self.capacite2Nom='Tir Sniperial'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Elfe.Pluie
            self.capacite3Nom='Pluie de Douleur'
            self.capacite3BonusSkill=0
            self.Trecharge3=6
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Elfe.Salvation
            self.capacite1Nom='Salvation'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Elfe.Fleches
            self.capacite2Nom='Flèches Célestes'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Elfe.MouvementEsquive
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

            self.capacite1=Elfe.Salvation
            self.capacite1Nom='Salvation'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Elfe.Tir
            self.capacite2Nom='Tir Sniperial'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Elfe.FlecheDivine
            self.capacite3Nom='Flèche Divine'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

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

            self.capacite1=Elfe.Salvation
            self.capacite1Nom='Salvation'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Elfe.Fleches
            self.capacite2Nom='Flèches Célestes'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Elfe.ContreAttaque

    def Salvation(elfe,cible):
        nb_coups=2
        chance_troisieme_coup=elfe.taux_coup_critique_actuel
        aleatoire=random.randint(1,100)/100
        if(aleatoire<=chance_troisieme_coup):
            nb_coups+=1
        print('\n',elfe.surnom,elfe.attribut,' tire une salve de flèches sur ',cible.surnom,cible.attribut,'!!\n')
        for i in range(nb_coups):
            degats=CalculDommage(elfe,1.6*nb_coups,elfe.capacite1BonusSkill,cible)
            AffichageTypeDeCoup(elfe,1.6*nb_coups,elfe.capacite1BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(elfe,degats,cible)
        return cible

    def Fleches(elfe,equipe_ennemie):
        print('\n',elfe.surnom,elfe.attribut,' attaque toute l\'équipe ennemie avec une pluie de flèches célestes aléatoires!!\n')
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie)):
                indice_cible=random.randint(0,len(equipe_ennemie)-1)
                while(equipe_ennemie[indice_cible].pv_actuels<=0):
                    indice_cible=random.randint(0,len(equipe_ennemie)-1)
                cible=equipe_ennemie[indice_cible]
                degats=CalculDommage(elfe,2,elfe.capacite2BonusSkill,cible)
                AffichageTypeDeCoup(elfe,2,elfe.capacite2BonusSkill,degats,cible)
                degats=ReductionDommage(degats,cible)
                Procedure_attaque(elfe,degats,cible)
                if(cible.immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(0.75,cible.resistance_actuelle,elfe.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        Degats_continus(cible,1,1)
        return equipe_ennemie

    def Pluie(elfe,equipe_ennemie):
        print('\n',elfe.surnom,elfe.attribut,' attaque toute l\'équipe ennemie avec une pluie de flèches!!\n')
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie)):
                degats=CalculDommage(elfe,4.8,elfe.capacite3BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(elfe,4.8,elfe.capacite3BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(elfe,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].stun==0 and equipe_ennemie[i].gel==0 and equipe_ennemie[i].sommeil==0):
                    print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' voit sa jauge d\'attaque diminuer de moitié!! \n')
                    equipe_ennemie[i].jauge_attaque-=max(50,Arrondir(0.5*equipe_ennemie[i].jauge_attaque))
                else:
                    print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' voit sa jauge d\'attaque réduite à zéro!! \n')
                    equipe_ennemie[i].jauge_attaque=0
        return equipe_ennemie

    def Tir(elfe,cible):
        print('\n',elfe.surnom,elfe.attribut,' tire une flèche avec une précision extrême sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(elfe,5.2,elfe.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(elfe,5.2,elfe.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(elfe,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,elfe.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!!')
                cible.stun=1
                print(elfe.surnom,elfe.attribut,' regagne instantanément un tour supplémentaire!!\n')
                elfe.tour_supplementaire_tmp+=1
        return cible

    def FlecheDivine(elfe,cible):
        print('\n',elfe.surnom,elfe.attribut,' tire une divine flèche de lumière sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(elfe,7.8,elfe.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(elfe,7.8,elfe.capacite2BonusSkill,degats,cible)
        if(cible.stun==1 or cible.gel==1 or cible.sommeil==1):
            degats=Arrondir(1.5*degats)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(elfe,degats,cible)
        return cible

    def Strategie(equipe_alliee):
        print('\nL\'équipe échafaude un plan machiavélique en s\'inspirant du FûRinKaZan...\n')
        for i in range(len(equipe_alliee)):
            Speed_up(equipe_alliee[i],3)
            Espada(equipe_alliee[i],3)
        return equipe_alliee

    def MouvementEsquive(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='Elfe' and equipe_alliee[i].attribut=='Vent'):
                if(equipe_alliee[i].passif_active!=1):
                    print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit sa réduction de dégâts augmenter!!\n')
                    equipe_alliee[i].reduction_de_degats+=0.5
                    equipe_alliee[i].passif_active=1
                    Speed_up(equipe_alliee[i],1)
        return equipe_alliee

    def FinMouvementEsquive(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='Elfe' and equipe_alliee[i].attribut=='Vent'):
                if(equipe_alliee[i].passif_active==1):
                    equipe_alliee[i].reduction_de_degats-=0.5
                    print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit sa réduction de dégâts diminuer!!\n')
                    equipe_alliee[i].passif_active=0
        return equipe_alliee

    def ContreAttaque(elfe,cible):
        print('\n',elfe.surnom,elfe.attribut,' venge son allié(e)!!\n')
        if(cible.pv_actuels>0):
            for i in range(3):
                degats=Arrondir(0.65*elfe.attaque_actuelle)
                degats=ReductionDommage(degats,cible)
                if(cible.immortalite<=0):
                    cible=(Monstre.recoitDegats(cible,degats))
                    print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
                else:
                    print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                if (cible.pv_actuels<=0):
                    print(cible.surnom,cible.attribut,' est mort!! \n')
                else:
                    print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')
        return cible



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

            self.capacite1=Sylphe.Esprit
            self.capacite1Nom='Esprit Elémentaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Sylphe.Turbulences
            self.capacite2Nom='Turbulences'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Sylphe.Phenix
            self.capacite3Nom='Phénix Incandescent'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphe.Vitesse
            self.Anti_leader_skill=Sylphe.AntiVitesse

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

            self.capacite1=Sylphe.Esprit
            self.capacite1Nom='Esprit Elémentaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Sylphe.Tourbillon
            self.capacite2Nom='Tourbillon Elémentaire'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Sylphe.Blizzard
            self.capacite3Nom='Blizzard'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphe.Vitesse
            self.Anti_leader_skill=Sylphe.AntiVitesse

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

            self.capacite1=Sylphe.Esprit
            self.capacite1Nom='Esprit Elémentaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Sylphe.Tourbillon
            self.capacite2Nom='Tourbillon Elémentaire'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Sylphe.Ouragan
            self.capacite3Nom='Ouragan'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphe.VitesseArena
            self.Anti_leader_skill=Sylphe.AntiVitesseArena

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

            self.capacite1=Sylphe.Esprit
            self.capacite1Nom='Esprit Elémentaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Sylphe.Tourbillon
            self.capacite2Nom='Tourbillon Elémentaire'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Sylphe.Cyclone
            self.capacite3Nom='Cyclone'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphe.VitesseDonjons
            self.Anti_leader_skill=Sylphe.AntiVitesseDonjons

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

            self.capacite1=Sylphe.Esprit
            self.capacite1Nom='Esprit Elémentaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Sylphe.Turbulences
            self.capacite2Nom='Turbulences'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Sylphe.Nuit
            self.capacite3Nom='Tombée de la Nuit'
            self.capacite3BonusSkill=0
            self.Trecharge3=7
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphe.VitesseDonjons
            self.Anti_leader_skill=Sylphe.AntiVitesseDonjons

    def Esprit(sylphe,cible):
        print('\n',sylphe.surnom,sylphe.attribut,' projette un esprit élémentaire sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(sylphe,3.8,sylphe.capacite1BonusSkill,cible)
        Type_coup=AffichageTypeDeCoup(sylphe,3.8,sylphe.capacite1BonusSkill,degats,cible)
        degats-=20
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(sylphe,degats,cible)
        if(Type_coup=='Critique'):
            Espada(sylphe,1)
        return cible

    def Turbulences(sylphe,cible):
        print('\n',sylphe.surnom,sylphe.attribut,' cause de violentes turbulences autour de ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(sylphe,6,sylphe.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(sylphe,6,sylphe.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(sylphe,degats,cible)
        print(cible.surnom,cible.attribut,'voit sa jauge d\'attaque réduite à zéro!!\n')
        cible.jauge_attaque=0
        return cible

    def Ouragan(sylphe,cible):
        print('\n',sylphe.surnom,sylphe.attribut,' engloutit ',cible.surnom,cible.attribut,' dans un ouragan dévastateur!!\n')
        degats=CalculDommage(sylphe,8.4,sylphe.capacite3BonusSkill,cible)
        AffichageTypeDeCoup(sylphe,8.4,sylphe.capacite3BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(sylphe,degats,cible)
        print('\n',sylphe.surnom,sylphe.attribut,' voit sa vitesse d\'attaque augmenter pour trois tours d\'un montant égal à la vitesse d\'attaque de ',cible.surnom,cible.attribut,'!!')
        sylphe.vitesse_actuelle+=cible.vitesse_max_donjons
        sylphe.tours_bonus_vitesse=max(3,sylphe.tours_bonus_vitesse)
        print('La vitesse actuelle de ',sylphe.surnom,sylphe.attribut,' est désormais de ',sylphe.vitesse_actuelle,'!!\n')
        return cible

    def Tourbillon(sylphe,equipe_ennemie):
        print('\n',sylphe.surnom,sylphe.attribut,' balaye deux fois l\'équipe ennemie avec un tourbillon élémentaire!!\n')
        for i in range(2):
            for j in range(len(equipe_ennemie)):
                if(isAlive(equipe_ennemie) and equipe_ennemie[j].pv_actuels>0):
                    degats=CalculDommage(sylphe,1.3,sylphe.capacite2BonusSkill,equipe_ennemie[j])
                    AffichageTypeDeCoup(sylphe,1.3,sylphe.capacite2BonusSkill,degats,equipe_ennemie[j])
                    degats+=Arrondir(0.04*equipe_ennemie[j].pv_max_donjons)
                    degats=ReductionDommage(degats,equipe_ennemie[j])
                    Procedure_attaque(sylphe,degats,equipe_ennemie[j])
                    if(equipe_ennemie[j].immunite==0):
                        EffetNefaste=random.randint(1,100)
                        Limite_reussite=CalculTauxReussiteEffet(0.4,equipe_ennemie[j].resistance_actuelle,sylphe.precision_actuelle)
                        if(EffetNefaste<=100*Limite_reussite):
                            Bonus_coup_superficiel(equipe_ennemie[j],2)
            print('\n\n')
        return equipe_ennemie

    def Nuit(sylphe,equipe_ennemie):
        print('\n',sylphe.surnom,sylphe.attribut,' enveloppe toute l\'équipe ennemie dans une brume noire mystérieuse... La nuit tombe!!\n')
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie) and equipe_ennemie[i].pv_actuels>0):
                Sommeil(equipe_ennemie[i],2)
        return equipe_ennemie

    def Cyclone(sylphe,equipe_ennemie):
        print('\n',sylphe.surnom,sylphe.attribut,' balaye quatre fois l\'équipe ennemie avec un puissant cyclone!!\n')
        for i in range(4):
            for j in range(len(equipe_ennemie)):
                if(isAlive(equipe_ennemie) and equipe_ennemie[j].pv_actuels>0):
                    degats=CalculDommage(sylphe,1.1,sylphe.capacite3BonusSkill,equipe_ennemie[j])
                    AffichageTypeDeCoup(sylphe,1.1,sylphe.capacite3BonusSkill,degats,equipe_ennemie[j])
                    degats=ReductionDommage(degats,equipe_ennemie[j])
                    Procedure_attaque(sylphe,degats,equipe_ennemie[j])
                    if(equipe_ennemie[j].immunite==0):
                        EffetNefaste=random.randint(1,100)
                        Limite_reussite=CalculTauxReussiteEffet(0.2,equipe_ennemie[j].resistance_actuelle,sylphe.precision_actuelle)
                        if(EffetNefaste<=100*Limite_reussite):
                            print(equipe_ennemie[j].surnom,equipe_ennemie[j].attribut,' est étourdi(e)!!')
                            print(sylphe.surnom,sylphe.attribut,' voit sa jauge d\'attaque augmenter d\'un cinquième de la jauge de ',equipe_ennemie[j].surnom,equipe_ennemie[j].attribut,'!!\n')
                            equipe_ennemie[j].stun=1
                            sylphe.jauge_attaque+=Arrondir(0.2*equipe_ennemie[j].jauge_attaque)
            print('\n\n')
        return equipe_ennemie

    def Blizzard(sylphe,equipe_ennemie):
        print('\n',sylphe.surnom,sylphe.attribut,' engloutit toute l\'équipe ennemie dans un puissant blizzard!!\n')
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie) and equipe_ennemie[i].pv_actuels>0):
                degats=CalculDommage(sylphe,3,sylphe.capacite3BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(sylphe,3,sylphe.capacite3BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(sylphe,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(1,equipe_ennemie[i].resistance_actuelle,sylphe.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' est gelé(e)!!')
                        equipe_ennemie[i].gel=1
                        Slow_down(equipe_ennemie[i],2)
        return equipe_ennemie

    def Phenix(sylphe,equipe_ennemie):
        print('\n',sylphe.surnom,sylphe.attribut,' invoque un Phénix incandescent!! Celui-ci engloutit toute l\'équipe ennemie dans une tempête de flammes!!\n')
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie) and equipe_ennemie[i].pv_actuels>0):
                degats=CalculDommage(sylphe,4,sylphe.capacite3BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(sylphe,4,sylphe.capacite3BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(sylphe,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(1,equipe_ennemie[i].resistance_actuelle,sylphe.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        Degats_continus(equipe_ennemie[i],1,3)
        return equipe_ennemie

    def Vitesse(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].vitesse_actuelle+=Arrondir(0.19*equipe_alliee[i].vitesse_max_donjons)
            equipe_alliee[i].vitesse_max_donjons+=Arrondir(0.19*equipe_alliee[i].vitesse_max_donjons)
            print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 19%!!')
            print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].vitesse_actuelle,'\n')
        return equipe_alliee

    def VitesseArena(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].vitesse_actuelle+=Arrondir(0.24*equipe_alliee[i].vitesse_max_donjons)
            equipe_alliee[i].vitesse_max_donjons+=Arrondir(0.24*equipe_alliee[i].vitesse_max_donjons)
            print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 24%!!')
            print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].vitesse_actuelle,'\n')
        return equipe_alliee

    def VitesseDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].vitesse_actuelle+=Arrondir(0.24*equipe_alliee[i].vitesse_max_donjons)
            equipe_alliee[i].vitesse_max_donjons+=Arrondir(0.24*equipe_alliee[i].vitesse_max_donjons)
            print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 24%!!')
            print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].vitesse_actuelle,'\n')
        return equipe_alliee

    def AntiVitesse(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].vitesse_actuelle-=Arrondir(0.19*equipe_alliee[i].vitesse_max_donjons)
        return equipe_alliee

    def AntiVitesseArena(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].vitesse_actuelle-=Arrondir(0.24*equipe_alliee[i].vitesse_max_donjons)
        return equipe_alliee

    def AntiVitesseDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].vitesse_actuelle-=Arrondir(0.24*equipe_alliee[i].vitesse_max_donjons)
        return equipe_alliee



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

            self.capacite1=Sylphide.Lame
            self.capacite1Nom='Lame Elémentaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Sylphide.Bourrasque
            self.capacite2Nom='Bourrasque Spirituelle'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Sylphide.Conjuration
            self.capacite3Nom='Conjuration'
            self.capacite3BonusSkill=0
            self.Trecharge3=10
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphide.ResistanceFeu
            self.Anti_leader_skill=Sylphide.AntiResistanceFeu

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

            self.capacite1=Sylphide.Lame
            self.capacite1Nom='Lame Elémentaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Sylphide.Ouragan
            self.capacite2Nom='Ouragan'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Sylphide.Benediction
            self.capacite3Nom='Bénédiction de la déesse de l\'eau'
            self.capacite3BonusSkill=0
            self.Trecharge3=4
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphide.ResistanceEau
            self.Anti_leader_skill=Sylphide.AntiResistanceEau

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

            self.capacite1=Sylphide.Lame
            self.capacite1Nom='Lame Elémentaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Sylphide.Bourrasque2
            self.capacite2Nom='Bourrasque Spirituelle'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Sylphide.Bouclier
            self.capacite3Nom='Bouclier Spirituel'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphide.ResistanceVent
            self.Anti_leader_skill=Sylphide.AntiResistanceVent

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

            self.capacite1=Sylphide.Lame
            self.capacite1Nom='Lame Elémentaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Sylphide.Ouragan
            self.capacite2Nom='Ouragan'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Sylphide.BenedictionLumiere
            self.capacite3Nom='Bénédiction de Lumière'
            self.capacite3BonusSkill=0
            self.Trecharge3=4
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphide.ResistanceLumiere
            self.Anti_leader_skill=Sylphide.AntiResistanceLumiere

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

            self.capacite1=Sylphide.Lame
            self.capacite1Nom='Lame Elémentaire'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Sylphide.Bourrasque2
            self.capacite2Nom='Bourrasque Spirituelle'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Sylphide.Aspiration
            self.capacite3Nom='Aspiration des Ténèbres'
            self.capacite3BonusSkill=0
            self.Trecharge3=6
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Sylphide.ResistanceTenebres
            self.Anti_leader_skill=Sylphide.AntiResistanceTenebres

    def Lame(sylphe,cible):
        print('\n',sylphe.surnom,sylphe.attribut,' perce ',cible.surnom,cible.attribut,' avec une lame élémentaire!!\n')
        degats=CalculDommage(sylphe,3.7,sylphe.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(sylphe,3.7,sylphe.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(sylphe,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.3,cible.resistance_actuelle,sylphe.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Degats_continus(cible,1,3)
        return cible

    def Ouragan(sylphe,cible):
        print('\n',sylphe.surnom,sylphe.attribut,' engloutit ',cible.surnom,cible.attribut,' dans un ouragan dévastateur!!\n')
        degats=CalculDommage(sylphe,5,sylphe.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(sylphe,5,sylphe.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(sylphe,degats,cible)
        print('\nToutes les capacités de ',cible.surnom,cible.attribut,' doivent désormais être rechargées au maximum!!\n')
        if(cible.nb_capacites>=2):
            cible.attente2=cible.Trecharge2
            cible.etatCap2='Non dispo'
        if(cible.nb_capacites>=3):
            cible.attente3=cible.Trecharge3
            cible.etatCap3='Non dispo'
        if(cible.nb_capacites>=4):
            cible.attente4=cible.Trecharge4
            cible.etatCap4='Non dispo'
        return cible

    def Bourrasque(sylphe,equipe_ennemie,equipe_alliee):
        print('\n',sylphe.surnom,sylphe.attribut,' balaye toute l\'équipe ennemie avec une bourrasque spirituelle!!\n')
        for j in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie) and equipe_ennemie[j].pv_actuels>0):
                degats=CalculDommage(sylphe,2.6,sylphe.capacite2BonusSkill,equipe_ennemie[j])
                AffichageTypeDeCoup(sylphe,2.6,sylphe.capacite2BonusSkill,degats,equipe_ennemie[j])
                degats=ReductionDommage(degats,equipe_ennemie[j])
                Procedure_attaque(sylphe,degats,equipe_ennemie[j])
        print('\n')
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels>0):
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit sa jauge d\'attaque augmenter d\'un cinquième!!')
                equipe_alliee[i].jauge_attaque+=max(20,Arrondir(0.2*equipe_alliee[i].jauge_attaque))
        return equipe_ennemie

    def Bourrasque2(sylphe,equipe_ennemie,equipe_alliee):
        print('\n',sylphe.surnom,sylphe.attribut,' balaye toute l\'équipe ennemie avec une bourrasque spirituelle!!\n')
        for j in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie) and equipe_ennemie[j].pv_actuels>0):
                degats=CalculDommage(sylphe,2.6,sylphe.capacite2BonusSkill,equipe_ennemie[j])
                AffichageTypeDeCoup(sylphe,2.6,sylphe.capacite2BonusSkill,degats,equipe_ennemie[j])
                degats=ReductionDommage(degats,equipe_ennemie[j])
                Procedure_attaque(sylphe,degats,equipe_ennemie[j])
        print('\n')
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels>0):
                if(equipe_alliee[i].perturbation_recup<=0):
                    montant=Arrondir(0.2*equipe_alliee[i].pv_max_donjons)
                    equipe_alliee[i]=Monstre.etreSoigne(equipe_alliee[i],montant)
                else:
                    print('\n',equipe_alliee[i].surnom,equipe_alliee.attribut[i],' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces... \n')
            else:
                print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est mort(e)!!\n')
        return equipe_ennemie

    ''' CORRIGER TOUS LES AND EN OR POUR LES != '''
    def Conjuration(equipe_alliee):
        print('\nSylphide Feu sacrifie sa vie pour soigner toute son équipe!!\n')
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom!='Sylphide' or equipe_alliee[i].attribut!='Feu'):
                if(equipe_alliee[i].pv_actuels>0):
                    equipe_alliee[i]=SoignerDeTousLesMaux(equipe_alliee[i])
                    print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,'est débarrassé de tous les effets négatifs qui l affectaient!!')
                    montant=equipe_alliee[i].pv_max_donjons
                    equipe_alliee[i]=Monstre.etreSoigne(equipe_alliee[i],montant)
                    print('Il reste ',equipe_alliee[i].pv_actuels,' point(s) de vie sur',equipe_alliee[i].pv_max_donjons,' à ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,'!! \n')
                else:
                    print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est mort(e)!!\n')
            else:
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' se vide de sa vie... \n')
                equipe_alliee[i].pv_actuels=0
        return equipe_alliee

    def Bouclier(equipe_alliee):
        print('\nSylphide Vent protège toute l\'équipe d\'un bouclier d\'énergie spirituelle!!\n')
        for j in range(len(equipe_alliee)):
            if(equipe_alliee[j].nom=='Sylphide' and equipe_alliee[j].attribut=='Vent'):
                montant=equipe_alliee[j].niveau*100
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels>0):
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' reçoit un bouclier d\'un montant égal à ',montant,'!!')
                equipe_alliee[i].pv_actuels+=montant
            else:
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est mort(e)!!\n')
        return equipe_alliee

    def Benediction(sylphe,allie):
        if(allie.perturbation_recup<=0):
            print('\n',sylphe.surnom,sylphe.attribut,' régénère les points de vie de ',allie.surnom,allie.attribut,' à leur maximum!!\n')
            allie.pv_actuels=allie.pv_max_donjons
        else:
            print('\n',allie.surnom,allie.attribut,' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces... \n')
        return allie

    def BenedictionLumiere(equipe_alliee):
        print('\nToute l\'équipe reçoit la bénédiction de la déesse de la lumière!!\n')
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels>0):
                if(equipe_alliee[i].perturbation_recup<=0):
                    montant=Arrondir(0.2*equipe_alliee[i].pv_max_donjons)
                    equipe_alliee[i]=Monstre.etreSoigne(equipe_alliee[i],montant)
                else:
                    print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces... \n')
                Tanky(equipe_alliee[i],2)
            else:
                print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est mort(e)!!\n')
        return equipe_alliee

    def Aspiration(sylphe,cible):
        sylphe.vol_de_vie+=100
        print('\n',sylphe.surnom,sylphe.attribut,' aspire la vie de ',cible.surnom,cible.attribut,' en ignorant sa défense!!\n')
        degats=0.5*sylphe.pv_max_donjons
        Procedure_attaque(sylphe,degats,cible)
        sylphe.vol_de_vie-=100
        return cible


    def ResistanceFeu(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Feu'):
                equipe_alliee[i].resistance_actuelle+=0.5
                equipe_alliee[i].resistance_max_donjons+=0.5
                print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 50%!!')
                print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].resistance_actuelle,'\n')
        return equipe_alliee

    def ResistanceEau(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].resistance_actuelle+=0.5
                equipe_alliee[i].resistance_max_donjons+=0.5
                print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 50%!!')
                print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].resistance_actuelle,'\n')
        return equipe_alliee

    def ResistanceVent(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Vent'):
                equipe_alliee[i].resistance_actuelle+=0.5
                equipe_alliee[i].resistance_max_donjons+=0.5
                print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 50%!!')
                print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].resistance_actuelle,'\n')
        return equipe_alliee

    def ResistanceLumiere(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Lumière'):
                equipe_alliee[i].resistance_actuelle+=0.5
                equipe_alliee[i].resistance_max_donjons+=0.5
                print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 50%!!')
                print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].resistance_actuelle,'\n')
        return equipe_alliee

    def ResistanceTenebres(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].resistance_actuelle+=0.5
                equipe_alliee[i].resistance_max_donjons+=0.5
                print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 50%!!')
                print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].resistance_actuelle,'\n')
        return equipe_alliee

    def AntiResistanceFeu(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Feu'):
                equipe_alliee[i].resistance_actuelle-=0.5
        return equipe_alliee

    def AntiResistanceEau(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Eau'):
                equipe_alliee[i].resistance_actuelle-=0.5
        return equipe_alliee

    def AntiResistanceVent(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Vent'):
                equipe_alliee[i].resistance_actuelle-=0.5
        return equipe_alliee

    def AntiResistanceLumiere(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Lumière'):
                equipe_alliee[i].resistance_actuelle-=0.5
        return equipe_alliee

    def AntiResistanceTenebres(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].attribut=='Ténèbres'):
                equipe_alliee[i].resistance_actuelle-=0.5
        return equipe_alliee



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

            self.capacite1=ChevalierMagique.Combo
            self.capacite1Nom='Combo de Trois Coups'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=ChevalierMagique.Balles
            self.capacite2Nom='Balles Magiques'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=ChevalierMagique.FeuVengeur

            self.presence_leader_skill=1
            self.leader_skill=ChevalierMagique.AuraFeu
            self.Anti_leader_skill=ChevalierMagique.AntiAuraFeu

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

            self.capacite1=ChevalierMagique.Combo
            self.capacite1Nom='Combo de Trois Coups'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=ChevalierMagique.Projectiles
            self.capacite2Nom='Projectiles Magiques'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=ChevalierMagique.Drain
            self.capacite3Nom='Drain Magique'
            self.capacite3BonusSkill=0
            self.Trecharge3=3
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=ChevalierMagique.AuraEau
            self.Anti_leader_skill=ChevalierMagique.AntiAuraEau

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

            self.capacite1=ChevalierMagique.Combo
            self.capacite1Nom='Combo de Trois Coups'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=ChevalierMagique.Balles
            self.capacite2Nom='Balles Magiques'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=ChevalierMagique.Tempete
            self.capacite3Nom='Epée des Tempêtes'
            self.capacite3BonusSkill=0
            self.Trecharge3=4
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=ChevalierMagique.AuraVent
            self.Anti_leader_skill=ChevalierMagique.AntiAuraVent

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

            self.capacite1=ChevalierMagique.Combo
            self.capacite1Nom='Combo de Trois Coups'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=ChevalierMagique.Balles
            self.capacite2Nom='Balles Magiques'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=ChevalierMagique.Altruisme

            self.presence_leader_skill=1
            self.leader_skill=ChevalierMagique.AuraLumiere
            self.Anti_leader_skill=ChevalierMagique.AntiAuraLumiere

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

            self.capacite1=ChevalierMagique.Combo
            self.capacite1Nom='Combo de Trois Coups'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=ChevalierMagique.Projectiles
            self.capacite2Nom='Projectiles Magiques'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=ChevalierMagique.Vortex
            self.capacite3Nom='Vortex des Ténèbres'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=ChevalierMagique.AuraTenebres
            self.Anti_leader_skill=ChevalierMagique.AntiAuraTenebres

    def Combo(cm,equipe_ennemie,cible):
        print('\n',cm.surnom,cm.attribut,' tranche deux fois ',cible.surnom,cible.attribut,'!!\n')
        for i in range(2):
            degats=CalculDommage(cm,1,cm.capacite1BonusSkill,cible)
            AffichageTypeDeCoup(cm,1,cm.capacite1BonusSkill,degats,cible)
            if(cm.attribut=='Feu' and cible.pv_actuels>cm.pv_actuels):
                degats+=Arrondir(0.5*degats)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(cm,degats,cible)
        print('\nLa troisième attaque touche toute l\'équipe ennemie!!\n')
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie)):
                degats=CalculDommage(cm,2,cm.capacite1BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(cm,2,cm.capacite1BonusSkill,degats,equipe_ennemie[i])
                if(cm.attribut=='Feu' and equipe_ennemie[i].pv_actuels>cm.pv_actuels):
                    degats+=Arrondir(0.5*degats)
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(cm,degats,equipe_ennemie[i])
        return cible

    def Tempete(cm,equipe_ennemie,cible):
        print('\n',cm.surnom,cm.attribut,' tranche deux fois ',cible.surnom,cible.attribut,' avec une lame de vent!!\n')
        for i in range(2):
            degats=CalculDommage(cm,1,cm.capacite3BonusSkill,cible)
            AffichageTypeDeCoup(cm,1,cm.capacite3BonusSkill,degats,cible)
            degats+=Arrondir(0.06*cm.pv_max_donjons)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(cm,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(1,cible.resistance_actuelle,cm.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    print(cible.surnom,cible.attribut,'voit sa jauge d\'attaque diminuer de 30%!!')
                    cible.jauge_attaque-=max(30,Arrondir(0.3*cible.jauge_attaque))
        print('\n',cm.surnom,cm.attribut,' soulève une tempête qui touche toute l\'équipe ennemie!!\n')
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie)):
                degats=CalculDommage(cm,1,cm.capacite3BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(cm,1,cm.capacite3BonusSkill,degats,equipe_ennemie[i])
                degats+=Arrondir(0.06*cm.pv_max_donjons)
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(cm,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(1,equipe_ennemie[i].resistance_actuelle,cm.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,'voit sa jauge d\'attaque diminuer de 30%!!')
                        equipe_ennemie[i].jauge_attaque-=max(30,Arrondir(0.3*equipe_ennemie[i].jauge_attaque))
        return cible

    def Projectiles(cm,equipe_ennemie):
        print('\n',cm.surnom,cm.attribut,' attaque toute l\'équipe ennemie avec quatre projectiles magiques aléatoires!!\n')
        for i in range(4):
            if(isAlive(equipe_ennemie)):
                indice_cible=random.randint(0,len(equipe_ennemie)-1)
                while(equipe_ennemie[indice_cible].pv_actuels<=0):
                    indice_cible=random.randint(0,len(equipe_ennemie)-1)
                cible=equipe_ennemie[indice_cible]
                degats=CalculDommage(cm,1.9,cm.capacite2BonusSkill,cible)
                AffichageTypeDeCoup(cm,1.9,cm.capacite2BonusSkill,degats,cible)
                degats=ReductionDommage(degats,cible)
                Procedure_attaque(cm,degats,cible)
                if(cible.immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(0.5,cible.resistance_actuelle,cm.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        Def_break(cible,2)
        return equipe_ennemie

    def Drain(cm,equipe_ennemie):
        cm.vol_de_vie+=50
        print('\n',cm.surnom,cm.attribut,' aspire les forces de toute l\'équipe ennemie avec un vortex magique!!\n')
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie) and equipe_ennemie[i].pv_actuels>0):
                degats=CalculDommage(cm,4.8,cm.capacite3BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(cm,4.8,cm.capacite3BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(cm,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(1,equipe_ennemie[i].resistance_actuelle,cm.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,'voit sa jauge d\'attaque drainée par ',cm.surnom,cm.attribut,'!! \n')
                        equipe_ennemie[i].jauge_attaque-=max(25,Arrondir(0.25*equipe_ennemie[i].jauge_attaque))
                        cm.jauge_attaque+=max(25,Arrondir(0.25*equipe_ennemie[i].jauge_attaque))
        cm.vol_de_vie-=50
        return equipe_ennemie

    def Balles(cm,cible):
        print('\n',cm.surnom,cm.attribut,' tire des balles magiques sur ',cible.surnom,cible.attribut,'!!\n')
        for i in range(3):
            degats=CalculDommage(cm,2.1,cm.capacite2BonusSkill,cible)
            AffichageTypeDeCoup(cm,2.1,cm.capacite2BonusSkill,degats,cible)
            if(cm.attribut=='Feu' and cible.pv_actuels>cm.pv_actuels):
                degats+=Arrondir(0.5*degats)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(cm,degats,cible)
            if(cible.immunite==0):
                EffetNefaste=random.randint(1,100)
                Limite_reussite=CalculTauxReussiteEffet(0.75,cible.resistance_actuelle,cm.precision_actuelle)
                if(EffetNefaste<=100*Limite_reussite):
                    print(cible.surnom,cible.attribut,'devient silencieuse pour deux tours!! \n')
                    cible.silencieux=1
                    cible.tours_silencieux=max(2,cible.tours_silencieux)
        return cible

    def Vortex(cm,equipe_alliee,cible):
        print('\n',cm.surnom,cm.attribut,' projette un vortex de ténèbres sur ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(cm,7,cm.capacite3BonusSkill,cible)
        AffichageTypeDeCoup(cm,7,cm.capacite3BonusSkill,degats,cible)
        degats+=Arrondir(0.16*cible.pv_max_donjons)
        degats=ReductionDommage(degats,cible)
        montant=Arrondir(0.3*degats)
        Procedure_attaque(cm,degats,cible)
        print('\n L\'équipe récupère les forces de ',cible.surnom,cible.attribut,'!!\n')
        for i in range(len(equipe_alliee)):
            equipe_alliee[i]=Monstre.etreSoigne(equipe_alliee[i],montant)
        return cible

    def Altruisme(cm,cible,equipe_alliee):
        pv_min=equipe_alliee[0].pv_actuels
        indice_du_min=0
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels<pv_min):
                pv_min=equipe_alliee[i].pv_actuels
                indice_du_min=i
        print('\n',equipe_alliee[indice_du_min].surnom,equipe_alliee[indice_du_min].attribut,' guérit grâce à l\'aura de ',cm.surnom,cm.attribut,'!!')
        montant=Arrondir(0.15*equipe_alliee[indice_du_min].pv_max_donjons)
        equipe_alliee[indice_du_min]=Monstre.etreSoigne(equipe_alliee[indice_du_min],montant)
        Aleatoire=random.randint(1,100)
        if(Aleatoire<=35):
            Retirer_un_bonus(cible)

    def FeuVengeur(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if((equipe_alliee[i].nom=='Chevalier Magique' or equipe_alliee[i].nom=='ChevalierMagique') and equipe_alliee[i].attribut=='Feu'):
                ratio=equipe_alliee[i].pv_actuels/equipe_alliee[i].pv_max_donjons
                ratio=1-ratio
                print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' voit sa vitesse augmenter grâce à son passif!!')
                equipe_alliee[i].vitesse_actuelle=equipe_alliee[i].vitesse_max_donjons+Arrondir(ratio*equipe_alliee[i].vitesse_max_donjons)
                if(equipe_alliee[i].tours_bonus_vitesse>0):
                    equipe_alliee[i].vitesse_actuelle+=Arrondir(0.3*equipe_alliee[i].vitesse_actuelle)
                ''' Soigne de malus_vitesse '''
        return equipe_alliee

    def AuraFeu(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].pv_actuels+=Arrondir(0.25*equipe_alliee[i].pv_max_donjons)
            equipe_alliee[i].pv_max_donjons+=Arrondir(0.25*equipe_alliee[i].pv_max_donjons)
            print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 25%!!')
            print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].pv_actuels,'\n')
        return equipe_alliee

    def AuraEau(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].attaque_actuelle+=Arrondir(0.25*equipe_alliee[i].attaque_max_donjons)
            equipe_alliee[i].attaque_max_donjons+=Arrondir(0.25*equipe_alliee[i].attaque_max_donjons)
            print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 25%!!')
            print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].attaque_actuelle,'\n')
        return equipe_alliee

    def AuraVent(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].taux_coup_critique_actuel+=0.19
            equipe_alliee[i].taux_coup_critique_max_donjons+=0.19
            print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 19%!!')
            print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].taux_coup_critique_actuel,'\n')
        return equipe_alliee

    def AuraLumiere(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].precision_actuelle+=0.3
            equipe_alliee[i].precision_max_donjons+=0.3
            print('La précision actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 30%!!')
            print('La précision actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].precision_actuelle,'\n')
        return equipe_alliee

    def AuraTenebres(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].vitesse_actuelle+=Arrondir(0.19*equipe_alliee[i].vitesse_max_donjons)
            equipe_alliee[i].vitesse_max_donjons+=Arrondir(0.19*equipe_alliee[i].vitesse_max_donjons)
            print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 19%!!')
            print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].vitesse_actuelle,'\n')
        return equipe_alliee

    def AntiAuraFeu(equipe_alliee):
        for i in range(len(equipe_alliee)):
                equipe_alliee[i].pv_actuels-=Arrondir(0.25*equipe_alliee[i].pv_max_donjons)
        return equipe_alliee

    def AntiAuraEau(equipe_alliee):
        for i in range(len(equipe_alliee)):
                equipe_alliee[i].attaque_actuelle-=Arrondir(0.25*equipe_alliee[i].attaque_max_donjons)
        return equipe_alliee

    def AntiAuraVent(equipe_alliee):
        for i in range(len(equipe_alliee)):
                equipe_alliee[i].taux_coup_critique_actuel-=0.19
        return equipe_alliee

    def AntiAuraLumiere(equipe_alliee):
        for i in range(len(equipe_alliee)):
                equipe_alliee[i].precision_actuelle-=0.3
        return equipe_alliee

    def AntiAuraTenebres(equipe_alliee):
        for i in range(len(equipe_alliee)):
                equipe_alliee[i].vitesse_actuelle-=Arrondir(0.19*equipe_alliee[i].vitesse_max_donjons)
        return equipe_alliee





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

            self.capacite1=Vampire.Drain
            self.capacite1Nom='Drain de Vie'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Vampire.Destruction
            self.capacite2Nom='Destruction'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Vampire.VitesseDonjons
            self.Anti_leader_skill=Vampire.AntiVitesseDonjons

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

            self.capacite1=Vampire.Drain
            self.capacite1Nom='Drain de Vie'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Vampire.Aneantissement
            self.capacite2Nom='Anéantissement'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Vampire.PVDonjons
            self.Anti_leader_skill=Vampire.AntiPVDonjons

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

            self.capacite1=Vampire.Drain
            self.capacite1Nom='Drain de Vie'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Vampire.Aneantissement
            self.capacite2Nom='Anéantissement'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Vampire.ResistanceDonjons
            self.Anti_leader_skill=Vampire.AntiResistanceDonjons

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

            self.capacite1=Vampire.Drain
            self.capacite1Nom='Drain de Vie'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Vampire.Destruction
            self.capacite2Nom='Destruction'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Vampire.AttaqueDonjons
            self.Anti_leader_skill=Vampire.AntiAttaqueDonjons

            self.presence_passif_1=1
            self.passif_1=Vampire.Immortalite

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

            self.capacite1=Vampire.Drain
            self.capacite1Nom='Drain de Vie'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Vampire.Aneantissement
            self.capacite2Nom='Aneantissement'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Vampire.TCCDonjons
            self.Anti_leader_skill=Vampire.AntiTCCDonjons

            self.presence_passif_1=1
            self.passif_1=Vampire.SoifDeSang

    def Drain(vampire,cible):
        vampire.vol_de_vie+=30
        print('\n',vampire.surnom,vampire.attribut,' absorbe la vie de ',cible.surnom,cible.attribut,'!!\n')
        for i in range(2):
            degats=CalculDommage(vampire,2,vampire.capacite1BonusSkill,cible)
            AffichageTypeDeCoup(vampire,2,vampire.capacite1BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(vampire,degats,cible)
        vampire.vol_de_vie-=30
        return cible

    def Destruction(vampire,cible):
        vampire.taux_coup_critique_actuel+=0.3
        print('\n',vampire.surnom,vampire.attribut,' pulvérise ',cible.surnom,cible.attribut,' avec deux coups puissants!!\n')
        for i in range(2):
            degats=CalculDommage(vampire,3,vampire.capacite2BonusSkill,cible)
            AffichageTypeDeCoup(vampire,3,vampire.capacite2BonusSkill,degats,cible)
            degats=ReductionDommage(degats,cible)
            Procedure_attaque(vampire,degats,cible)
        return cible

    def Aneantissement(vampire,cible):
        print('\n',vampire.surnom,vampire.attribut,' anéantit ',cible.surnom,cible.attribut,'!!\n')
        degats=CalculDommage(vampire,6.2,vampire.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(vampire,6.2,vampire.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(vampire,degats,cible)
        if(cible.immunite==0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.75,cible.resistance_actuelle,vampire.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                Slow_down(cible,2)
                Atk_break(cible,2)
                print(cible.surnom,cible.attribut,' ne pourra plus recevoir de bonus pour les deux prochains tours!!\n')
                cible.immunite_aux_bonus=1
                cible.tours_immunite_aux_bonus=max(cible.tours_immunite_aux_bonus,2)
        return cible

    def SoifDeSang(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].jauge_attaque+=max(30,Arrondir(0.3*equipe_alliee[i].jauge_attaque))
        return equipe_alliee
        ''' Vrai effet à implémenter :
            Feast of Blood (Passive):
            Attacks leave a Branding Effect that lasts for 2 turns and
            heal all allies for 30% of the damage done.
            Also, whenever you kill an enemy, the attack bar of all allies increases by 30%.
        '''

    def Immortalite(equipe_alliee):
        print('\n\nActivation du passif d\'Immortalité du Vampire Lumière \n\n')
        montant=0
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels>(0.3*equipe_alliee[i].pv_max_donjons) and (equipe_alliee[i].nom!='Vampire' or equipe_alliee[i].attribut!='Lumiere')):
                montant+=Arrondir(0.1*equipe_alliee[i].pv_max_donjons)
                equipe_alliee[i].pv_actuels-=Arrondir(0.1*equipe_alliee[i].pv_max_donjons)
                print(equipe_alliee[i].surnom,equipe_alliee[i].attribut,' perd un dixième de ses PV max!!')
            elif(equipe_alliee[i].nom=='Vampire' and equipe_alliee[i].attribut=='Lumière'):
                indice_vampire=i
        if(montant>0 and equipe_alliee[indice_vampire].sans_resurrection<=0):
            print(equipe_alliee[indice_vampire].surnom,equipe_alliee[indice_vampire].attribut,' revient à la vie avec ',montant,' points de vie!!\n')
            equipe_alliee[indice_vampire].pv_actuels=montant
        return equipe_alliee

    def VitesseDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].vitesse_actuelle+=Arrondir(0.28*equipe_alliee[i].vitesse_max_donjons)
            equipe_alliee[i].vitesse_max_donjons+=Arrondir(0.28*equipe_alliee[i].vitesse_max_donjons)
            print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 28%!!')
            print('La vitesse actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].vitesse_actuelle,'\n')
        return equipe_alliee

    def PVDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].pv_actuels+=Arrondir(0.38*equipe_alliee[i].pv_max_donjons)
            equipe_alliee[i].pv_max_donjons+=Arrondir(0.38*equipe_alliee[i].pv_max_donjons)
            print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 38%!!')
            print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].pv_actuels,'\n')
        return equipe_alliee

    def ResistanceDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].resistance_actuelle+=0.48
            equipe_alliee[i].resistance_max_donjons+=0.48
            print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 48%!!')
            print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].resistance_actuelle,'\n')
        return equipe_alliee

    def AttaqueDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].attaque_actuelle+=Arrondir(0.38*equipe_alliee[i].attaque_max_donjons)
            equipe_alliee[i].attaque_max_donjons+=Arrondir(0.38*equipe_alliee[i].attaque_max_donjons)
            print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 38%!!')
            print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].attaque_actuelle,'\n')
        return equipe_alliee

    def TCCDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].taux_coup_critique_actuel+=0.28
            equipe_alliee[i].taux_coup_critique_max_donjons+=0.28
            print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 28%!!')
            print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].taux_coup_critique_actuel,'\n')
        return equipe_alliee

    def AntiVitesseDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].vitesse_actuelle-=Arrondir(0.28*equipe_alliee[i].vitesse_max_donjons)
        return equipe_alliee

    def AntiPVDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].pv_actuels-=Arrondir(0.38*equipe_alliee[i].pv_max_donjons)
        return equipe_alliee

    def AntiResistanceDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].resistance_actuelle-=0.48
        return equipe_alliee

    def AntiAttaqueDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].attaque_actuelle-=Arrondir(0.38*equipe_alliee[i].attaque_max_donjons)
        return equipe_alliee

    def AntiTCCDonjons(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].taux_coup_critique_actuel-=0.28
        return equipe_alliee



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

            self.capacite1=Phenix.Geyser
            self.capacite1Nom='Geyser de Feu'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Phenix.Etoile
            self.capacite2Nom='Etoile Ecarlate'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Phenix.Eternite

            self.presence_passif_2=1
            self.passif_2=Phenix.Resurrection
            self.passif_active=0
            self.attentePassif=0

            self.presence_leader_skill=1
            self.leader_skill=Phenix.SuperPower
            self.Anti_leader_skill=Phenix.AntiSuperPower

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

            self.capacite1=Phenix.Geyser
            self.capacite1Nom='Geyser de Glace'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Phenix.Orbe
            self.capacite2Nom='Etoile des Neiges'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Phenix.Blizzard
            self.capacite3Nom='Blizzard Absolu'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Phenix.SuperLife
            self.Anti_leader_skill=Phenix.AntiSuperLife

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

            self.capacite1=Phenix.Geyser
            self.capacite1Nom='Geyser de Vent'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Phenix.Etoile
            self.capacite2Nom='Etoile Céleste'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Phenix.Tempete
            self.capacite3Nom='Tempête Destructrice'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Phenix.SuperCritique
            self.Anti_leader_skill=Phenix.AntiSuperCritique

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

            self.capacite1=Phenix.Geyser
            self.capacite1Nom='Geyser de Lumière'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Phenix.Orbe
            self.capacite2Nom='Etoile Astrale'
            self.capacite2BonusSkill=0
            self.Trecharge2=3
            self.attente2=0
            self.etatCap2='dispo'

            self.capacite3=Phenix.Purification
            self.capacite3Nom='Déflagration Purifiante'
            self.capacite3BonusSkill=0
            self.Trecharge3=5
            self.attente3=0
            self.etatCap3='dispo'

            self.presence_leader_skill=1
            self.leader_skill=Phenix.SuperTank
            self.Anti_leader_skill=Phenix.AntiSuperTank

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

            self.capacite1=Phenix.Geyser
            self.capacite1Nom='Geyser de Ténèbres'
            self.capacite1BonusSkill=0
            self.Trecharge1=1
            self.attente1=0
            self.etatCap1='dispo'

            self.capacite2=Phenix.Etoile
            self.capacite2Nom='Etoile du Désespoir'
            self.capacite2BonusSkill=0
            self.Trecharge2=4
            self.attente2=0
            self.etatCap2='dispo'

            self.presence_passif_1=1
            self.passif_1=Phenix.Enfer

            self.presence_leader_skill=1
            self.leader_skill=Phenix.SuperResistance
            self.Anti_leader_skill=Phenix.AntiSuperResistance

    ''' Remplacer les ressusciter par renaitre de ses cendres '''
    def Geyser(phenix,cible):
        if(phenix.attribut=='Feu'):
            print('\n',phenix.surnom,phenix.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un geyser de feu instantané!!\n')
        elif(phenix.attribut=='Eau'):
            print('\n',phenix.surnom,phenix.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un geyser de glace instantané!!\n')
        elif(phenix.attribut=='Vent'):
            print('\n',phenix.surnom,phenix.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un geyser de vent instantané!!\n')
        elif(phenix.attribut=='Lumière'):
            print('\n',phenix.surnom,phenix.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un geyser de lumière instantané!!\n')
        elif(phenix.attribut=='Ténèbres'):
            print('\n',phenix.surnom,phenix.attribut,' pulvérise ',cible.surnom,cible.attribut,' d\'un geyser de ténèbres instantané!!\n')
        degats=CalculDommage(phenix,4.2,phenix.capacite1BonusSkill,cible)
        AffichageTypeDeCoup(phenix,4.2,phenix.capacite1BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(phenix,degats,cible)
        if(cible.immunite<=0):
            EffetNefaste=random.randint(1,100)
            Limite_reussite=CalculTauxReussiteEffet(0.18,cible.resistance_actuelle,phenix.precision_actuelle)
            if(EffetNefaste<=100*Limite_reussite):
                print(cible.surnom,cible.attribut,' est étourdi(e)!!\n')
                cible.stun=1
        if(phenix.attribut=='Feu' and phenix.passif_active!=0):
            phenix.attentePassif-=1
            if(phenix.attentePassif<=0):
                print('\n',phenix.surnom,phenix.attribut,' peut à nouveau renaitre de ses cendres!!\n')
                phenix.passif_active=0
            else:
                print('\n',phenix.surnom,phenix.attribut,' voit diminuer de 1 le temps à attendre avant de pouvoir renaitre de ses cendres à nouveau!!')
        return cible

    def Etoile(phenix,cible):
        pourcentage_pv_perdus_cible=Arrondir(cible.pv_actuels/cible.pv_max_donjons)
        bonus_multiplicateur=4*pourcentage_pv_perdus_cible
        if(phenix.attribut=='Feu'):
            print('\n',phenix.surnom,phenix.attribut,' réduit ',cible.surnom,cible.attribut,' en cendres avec une gigantesque sphère de flammes!!\n')
        elif(phenix.attribut=='Vent'):
            print('\n',phenix.surnom,phenix.attribut,' réduit ',cible.surnom,cible.attribut,' en poussière avec une gigantesque sphère de vent!!\n')
        elif(phenix.attribut=='Ténèbres'):
            print('\n',phenix.surnom,phenix.attribut,' réduit ',cible.surnom,cible.attribut,' en cendres avec une gigantesque sphère de flammes noires!!\n')
        degats=CalculDommage(phenix,5+bonus_multiplicateur,phenix.capacite2BonusSkill,cible)
        AffichageTypeDeCoup(phenix,5+bonus_multiplicateur,phenix.capacite2BonusSkill,degats,cible)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(phenix,degats,cible)
        if(phenix.attribut=='Feu' and phenix.passif_active!=0):
            phenix.attentePassif-=1
            if(phenix.attentePassif<=0):
                print('\n',phenix.surnom,phenix.attribut,' peut à nouveau renaitre de ses cendres!!\n')
                phenix.passif_active=0
            else:
                print('\n',phenix.surnom,phenix.attribut,' voit diminuer de 1 le temps à attendre avant de pouvoir renaitre de ses cendres à nouveau!!')
        return cible

    def Orbe(phenix,cible):
        if(phenix.attribut=='Eau'):
            print('\n',phenix.surnom,phenix.attribut,' réduit ',cible.surnom,cible.attribut,' à néant avec une gigantesque sphère de glace!!\n')
        elif(phenix.attribut=='Lumière'):
            print('\n',phenix.surnom,phenix.attribut,' réduit ',cible.surnom,cible.attribut,' à néant avec une gigantesque sphère de lumière pure!!\n')
        degats=CalculDommage(phenix,4.5,phenix.capacite2BonusSkill,cible)
        Type_coup=AffichageTypeDeCoup(phenix,4.5,phenix.capacite2BonusSkill,degats,cible)
        degats+=Arrondir(0.08*cible.pv_max_donjons)
        degats=ReductionDommage(degats,cible)
        Procedure_attaque(phenix,degats,cible)
        if(Type_coup=='Critique'):
            print(cible.surnom,cible.attribut,' est gelé(e)!!\n')
            cible.gel=1
        return cible

    def Blizzard(phenix,equipe_ennemie):
        print('\n',phenix.surnom,phenix.attribut,' engloutit toute l\'équipe ennemie dans un puissant blizzard!!\n')
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie) and equipe_ennemie[i].pv_actuels>0):
                degats=CalculDommage(phenix,3,phenix.capacite3BonusSkill,equipe_ennemie[i])
                Type_coup=AffichageTypeDeCoup(phenix,3,phenix.capacite3BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                degats+=Arrondir(0.12*equipe_ennemie[i].pv_max_donjons)
                Procedure_attaque(phenix,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].immunite==0):
                    EffetNefaste=random.randint(1,100)
                    Limite_reussite=CalculTauxReussiteEffet(1,equipe_ennemie[i].resistance_actuelle,phenix.precision_actuelle)
                    if(EffetNefaste<=100*Limite_reussite):
                        Atk_break(equipe_ennemie[i],2)
                    if(Type_coup=='Critique'):
                        print(equipe_ennemie[i].surnom,equipe_ennemie[i].attribut,' est gelé(e)!!\n')
                        equipe_ennemie[i].gel=1
        return equipe_ennemie

    def Tempete(phenix,equipe_ennemie):
        print('\n',phenix.surnom,phenix.attribut,' engloutit toute l\'équipe ennemie dans une violente tempête!!\n')
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie) and equipe_ennemie[i].pv_actuels>0):
                degats=CalculDommage(phenix,4.5,phenix.capacite3BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(phenix,4.5,phenix.capacite3BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(phenix,degats,equipe_ennemie[i])
                if(equipe_ennemie[i].pv_actuels<=0):
                    print('\n',phenix.surnom,phenix.attribut,' a tué quelqu\'un et voit donc son temps de recharge réduit à zéro!!')
                    print(phenix.surnom,phenix.attribut,' voit sa jauge d\'attaque augmenter immédiatement de 20%!!\n')
                    phenix.attente3=0
                    phenix.etatCap3='dispo'
                    phenix.jauge_attaque+=max(20,Arrondir(0.2*phenix.jauge_attaque))
        return equipe_ennemie

    def Purification(phenix,equipe_ennemie):
        print('\n',phenix.surnom,phenix.attribut,' éblouit toute l\'équipe ennemie d\'une lumière aveuglante!!\n')
        for i in range(len(equipe_ennemie)):
            if(isAlive(equipe_ennemie) and equipe_ennemie[i].pv_actuels>0):
                nb_effets_renforcement=NbEffetsRenforcement(equipe_ennemie[i])
                equipe_ennemie[i]=SoignerDeTousLesBiens(equipe_ennemie[i])
                if(nb_effets_renforcement>0):
                    Def_break(equipe_ennemie[i],1)
                degats=CalculDommage(phenix,4.5,phenix.capacite3BonusSkill,equipe_ennemie[i])
                AffichageTypeDeCoup(phenix,4.5,phenix.capacite3BonusSkill,degats,equipe_ennemie[i])
                degats=ReductionDommage(degats,equipe_ennemie[i])
                Procedure_attaque(phenix,degats,equipe_ennemie[i])
        return equipe_ennemie

    ''' Passif de fin de tour pour Phénix Feu'''
    def Eternite(equipe_alliee):
        print('\nToute l\'équipe reçoit la bénédiction du phénix de feu!!\n')
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].pv_actuels>0 and (equipe_alliee[i].nom!='Phénix' or equipe_alliee[i].attribut!='Feu')):
                if(equipe_alliee[i].perturbation_recup<=0):
                    montant=Arrondir(0.1*equipe_alliee[i].pv_max_donjons)
                    equipe_alliee[i]=Monstre.etreSoigne(equipe_alliee[i],montant)
                else:
                    print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' a sa récupération de points de vie perturbée et ne recouvre donc pas ses forces... \n')
            elif(equipe_alliee[i].pv_actuels<=0):
                print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est mort(e)!!\n')
            else:
                print('\nDans son immense générosité, le phénix de feu ne peut pas se soigner lui-même... \n')
        return equipe_alliee

    ''' Passif de fin de tour adverse pour Phénix Feu '''
    def Resurrection(equipe_alliee):
        for i in range(len(equipe_alliee)):
            if(equipe_alliee[i].nom=='Phénix' and equipe_alliee[i].attribut=='Feu'):
                if(equipe_alliee[i].pv_actuels<=0 and equipe_alliee[i].passif_active==0):
                    if(equipe_alliee[i].sans_resurrection<=0):
                        print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' revient à la vie avec 100% de ses point de vie max!!')
                        print('Son passif se met maintenant en pause pour douze tours.\n')
                        equipe_alliee[i].pv_actuels=equipe_alliee[i].pv_max_donjons
                        equipe_alliee[i].passif_active=1
                        equipe_alliee[i].attentePassif=12
                    else:
                        print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' a été maudit et ne peut donc pas revenir à la vie... \n')
                elif(equipe_alliee[i].pv_actuels<=0 and equipe_alliee[i].passif_active!=0):
                    print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est déjà revenu à la vie et ne peut donc pas ressusciter...\n')
                else:
                    print('\n',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est toujours vivant!!\n')
        return equipe_alliee

    ''' Passif de fin de tour pour Phénix Ténèbres '''
    def Enfer(phenix,cible):
        if(cible.pv_actuels<=0):
            print('\n',cible.surnom,cible.attribut,' est consumé(e) par les flammes de l\'Enfer et ne pourra donc pas revenir à la vie!!')
            print('Le temps de rechargement de Etoile du Désespoir diminue de 1!!\n')
            cible.sans_resurrection=1
            phenix.attente2-=1
        ''' else: Faire Branding Effetcs (3 tours avec 50% de chances)'''
    # Pas de return (principalement de l'affichage)
    # Retourner cible quand le else aura été fait


    def SuperPower(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].attaque_actuelle+=Arrondir(0.44*equipe_alliee[i].attaque_max_donjons)
            equipe_alliee[i].attaque_max_donjons+=Arrondir(0.44*equipe_alliee[i].attaque_max_donjons)
            print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 44%!!')
            print('L\'attaque actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].attaque_actuelle,'\n')
        return equipe_alliee

    def SuperLife(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].pv_actuels+=Arrondir(0.44*equipe_alliee[i].pv_max_donjons)
            equipe_alliee[i].pv_max_donjons+=Arrondir(0.44*equipe_alliee[i].pv_max_donjons)
            print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 44%!!')
            print('Les points de vie actuels de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' sont désormais de ',equipe_alliee[i].pv_actuels,'\n')
        return equipe_alliee

    def SuperCritique(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].taux_coup_critique_actuel+=0.33
            equipe_alliee[i].taux_coup_critique_max_donjons+=0.33
            print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 33%!!')
            print('Le taux de coup critique actuel de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].taux_coup_critique_actuel,'\n')
        return equipe_alliee

    def SuperTank(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].defense_actuelle+=Arrondir(0.44*equipe_alliee[i].defense_max_donjons)
            equipe_alliee[i].defense_max_donjons+=Arrondir(0.44*equipe_alliee[i].defense_max_donjons)
            print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 44%!!')
            print('La défense actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].defense_actuelle,'\n')
        return equipe_alliee

    def SuperResistance(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].resistance_actuelle+=0.55
            equipe_alliee[i].resistance_max_donjons+=0.55
            print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' augmente de 55%!!')
            print('La résistance actuelle de ',equipe_alliee[i].surnom,equipe_alliee[i].attribut,' est désormais de ',equipe_alliee[i].resistance_actuelle,'\n')
        return equipe_alliee

    def AntiSuperPower(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].attaque_actuelle-=Arrondir(0.44*equipe_alliee[i].attaque_max_donjons)
        return equipe_alliee

    def AntiSuperLife(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].pv_actuels-=Arrondir(0.44*equipe_alliee[i].pv_max_donjons)
        return equipe_alliee

    def AntiSuperCritique(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].taux_coup_critique_actuel-=0.33
        return equipe_alliee

    def AntiSuperTank(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].defense_actuelle-=Arrondir(0.44*equipe_alliee[i].defense_max_donjons)
        return equipe_alliee

    def AntiSuperResistance(equipe_alliee):
        for i in range(len(equipe_alliee)):
            equipe_alliee[i].resistance_actuelle-=0.55
        return equipe_alliee


class Donjon(equipe):
    def __init__(self,caracteristiques_donjon):
        self.nom=caracteristiques_donjon[0]
        self.niveau=caracteristiques_donjon[1]
        self.attribut=caracteristiques_donjon[2]
        self.monstre1=caracteristiques_donjon[3]
        self.monstre2=caracteristiques_donjon[4]
        self.monstre3=caracteristiques_donjon[5]
        self.monstre4=caracteristiques_donjon[6]
        self.monstre5=caracteristiques_donjon[7]
        self.monstre6=caracteristiques_donjon[8]
        self.demiBoss1=caracteristiques_donjon[9]
        self.demiBoss2=caracteristiques_donjon[10]
        self.Boss=caracteristiques_donjon[11]
        self.recompense=caracteristiques_donjon[12]
        self.nom_famille=caracteristiques_donjon[13]
        self.region=1


    def Trouver_XP_initiale(classe,niveau):
        XP_requise_LV1=[460,516,579,650,728,818,918,1029,1155,1296,1455,1631,1831,2054]
        XP_requise_LV2=[552,619,695,779,875,981,1102,1235,1386,1555,1745,1958,2197,2465,2765,3103,3481,3906,4423]
        XP_requise_LV3=[662,743,834,936,1049,1178,1321,1483,1663,1866,2094,2350,2636,2957,3319,3723,4178,4687,5307,6009,6802,7703,8720,9962]
        XP_requise_LV4=[796,892,1002,1124,1261,1415,1587,1781,1998,2243,2515,2823,3167,3553,3987,4473,5019,5631,6376,7219,8172,9254,10476,11969,13673,15619,17844,20386,23495]
        XP_requise_LV5=[952,1068,1199,1344,1509,1693,1899,2131,2392,2682,3010,3378,3789,4252,4770,5352,6006,6738,7628,8638,9779,11072,12535,14321,16360,18690,21350,24392,28113,32404,37348,43048,49617,57188]
        XP_requise_LV6=[1150,1290,1447,1624,1823,2044,2294,2574,2888,3240,3635,4079,4576,5135,5762,6464,7252,8138,9214,10431,11811,13371,15140,17296,19758,22572,25786,29458,33954,39134,45107,51990,59924,69068,76085,83816,92332,101712,112046]
        XP_requise=[XP_requise_LV1,XP_requise_LV2,XP_requise_LV3,XP_requise_LV4,XP_requise_LV5,XP_requise_LV6]
        XP_avant_prochain_niveau=XP_requise[classe-1][niveau-1]
        return XP_avant_prochain_niveau



OUT_OF_STOCKAGE=999
