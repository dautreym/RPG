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

    def monstres_region(donjon):
        # A COMPLETER AVEC DES ELIF CRATERE ATER...
        if(donjon.nom=='la Forêt Veur Niveau 1 - Entrée '):
            if (donjon.region==1):
                donjon.region+=2
            if (donjon.region==2):
                donjon.region+=1
            if (donjon.region==3):
                mob1=donjon.monstre1
                mob2=donjon.monstre2
                equipe_adverse=[mob1,mob2,0]
        elif(donjon.nom=='la Forêt Veur Niveau 7 - Clairière '):
            if (donjon.region==1):
                mob1=donjon.monstre1
                mob2=donjon.demiBoss1
                mob3=donjon.monstre2
                equipe_adverse=[mob1,mob2,mob3]
            if (donjon.region==2):
                mob1=donjon.monstre3
                mob2=donjon.demiBoss2
                mob3=donjon.monstre4
                equipe_adverse=[mob1,mob2,mob3]
            if (donjon.region==3):
                equipe_adverse=[donjon.Boss,0,0]
        elif(donjon.nom=='le Mont Tagne Niveau 7 - Caverne au Sommet '):
            if (donjon.region==1):
                mob1=donjon.monstre1
                mob2=donjon.demiBoss1
                mob3=donjon.monstre2
                equipe_adverse=[mob1,mob2,mob3]
            if (donjon.region==2):
                mob1=donjon.monstre3
                mob2=donjon.demiBoss2
                mob3=donjon.monstre4
                equipe_adverse=[mob1,mob2,mob3]
            if (donjon.region==3):
                equipe_adverse=[donjon.Boss]
        elif(donjon.nom=='le Cratère Ater Niveau 7 - Caverne des Profondeurs '):
            if (donjon.region==1):
                mob1=donjon.monstre1
                mob2=donjon.demiBoss1
                mob3=donjon.monstre2
                equipe_adverse=[mob1,mob2,mob3]
            if (donjon.region==2):
                mob1=donjon.monstre3
                mob2=donjon.demiBoss2
                mob3=donjon.monstre4
                equipe_adverse=[mob1,mob2,mob3]
            if (donjon.region==3):
                equipe_adverse=[donjon.Boss,0,0]
        elif(donjon.nom=='les Ruines de Senzargen Niveau 7 - Autel Sacrificiel '):
            if (donjon.region==1):
                mob1=donjon.monstre1
                mob2=donjon.demiBoss1
                mob3=donjon.monstre2
                equipe_adverse=[mob1,mob2,mob3]
            if (donjon.region==2):
                mob1=donjon.monstre3
                mob2=donjon.demiBoss2
                mob3=donjon.monstre4
                equipe_adverse=[mob1,mob2,mob3]
            if (donjon.region==3):
                equipe_adverse=[donjon.monstre6,donjon.Boss,0]
        else:
            if (donjon.region==1):
                mob1=donjon.monstre1
                mob2=donjon.demiBoss1
                mob3=donjon.monstre2
                equipe_adverse=[mob1,mob2,mob3]
            if (donjon.region==2):
                mob1=donjon.monstre3
                mob2=donjon.demiBoss2
                mob3=donjon.monstre4
                equipe_adverse=[mob1,mob2,mob3]
            if (donjon.region==3):
                mob1=donjon.monstre5
                mob2=donjon.Boss
                mob3=donjon.monstre6
                equipe_adverse=[mob1,mob2,mob3]
        return equipe_adverse

    def Position(donjon):
        print('Vous êtes actuellement dans la région ',donjon.region,'\n')

    def Rentrer(base,equipe_allies,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo):
        i=0
        while(i<len(equipe_allies)):
            if(equipe_allies[i]!=0):
                equipe_allies[i].etatCap1='dispo'
                equipe_allies[i].attente1=0
                if(equipe_allies[i].nb_capacites>=2):
                    equipe_allies[i].etatCap2='dispo'
                    equipe_allies[i].attente2=0
                if(equipe_allies[i].nb_capacites>=3):
                    equipe_allies[i].etatCap3='dispo'
                    equipe_allies[i].attente3=0
            i+=1
        Monstre.SoignerEquipe(equipe_allies)
        print('\n\n Vous êtes de retour à la base!!')
        print('Votre équipe reprend des forces... Son état est désormais : \n')
        equipe_allies=Rafraichir_equipe(base,equipe_allies)
        equipe.afficher(equipe_allies)
        Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)

    def RecevoirGold(sac,montant,nb_ennemis):
        sac.mana+=(montant*nb_ennemis)
        print('Vous recevez ',montant*nb_ennemis,' pierres de Mana!!')
        print('Vous avez désormais ',sac.mana,' pierres de Mana!! \n\n')
        str(input(' > '))
        return sac

    def CalculerXP_amelioration(monstre_a_sacrifier):
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
        if(monstre_a_sacrifier.niveau==1):
            XP_a_recevoir=XP_donnee_min[monstre_a_sacrifier.classe-1]
        elif(Donjon.Niveau_max_de_la_classe_atteint(monstre_a_sacrifier)==True):
            XP_a_recevoir=XP_donnee_max[monstre_a_sacrifier.classe-1]
        else:
            ecart=XP_donnee_max[monstre_a_sacrifier.classe-1]-XP_donnee_min[monstre_a_sacrifier.classe-1]
            nb_passages_en_niveau=9+(5*monstre_a_sacrifier.classe)
            XP_a_recevoir=XP_donnee_min[monstre_a_sacrifier.classe-1]+ecart*((monstre_a_sacrifier.niveau-1)/nb_passages_en_niveau)
        XP_a_recevoir=Arrondir(XP_a_recevoir)
        return XP_a_recevoir


    def RecevoirXP(monstre,XP_gagnee):
        print(monstre.surnom,'reçoit',XP_gagnee,'points d expérience!!')
        while(XP_gagnee>=monstre.XP_avant_prochain_niveau and (Donjon.Niveau_max_de_la_classe_atteint(monstre)==False)):
            XP_gagnee-=monstre.XP_avant_prochain_niveau
            Donjon.Monter_en_niveau(monstre)
        if(Donjon.Niveau_max_de_la_classe_atteint(monstre)==False):
            monstre.XP_avant_prochain_niveau-=XP_gagnee
            print('Il manque à',monstre.surnom,monstre.XP_avant_prochain_niveau,' points d expérience avant le prochain niveau!! \n')
        return monstre

    def Trouver_XP_avant_prochain_niveau(monstre):
        XP_requise_LV1=[460,516,579,650,728,818,918,1029,1155,1296,1455,1631,1831,2054]
        XP_requise_LV2=[552,619,695,779,875,981,1102,1235,1386,1555,1745,1958,2197,2465,2765,3103,3481,3906,4423]
        XP_requise_LV3=[662,743,834,936,1049,1178,1321,1483,1663,1866,2094,2350,2636,2957,3319,3723,4178,4687,5307,6009,6802,7703,8720,9962]
        XP_requise_LV4=[796,892,1002,1124,1261,1415,1587,1781,1998,2243,2515,2823,3167,3553,3987,4473,5019,5631,6376,7219,8172,9254,10476,11969,13673,15619,17844,20386,23495]
        XP_requise_LV5=[952,1068,1199,1344,1509,1693,1899,2131,2392,2682,3010,3378,3789,4252,4770,5352,6006,6738,7628,8638,9779,11072,12535,14321,16360,18690,21350,24392,28113,32404,37348,43048,49617,57188]
        XP_requise_LV6=[1150,1290,1447,1624,1823,2044,2294,2574,2888,3240,3635,4079,4576,5135,5762,6464,7252,8138,9214,10431,11811,13371,15140,17296,19758,22572,25786,29458,33954,39134,45107,51990,59924,69068,76085,83816,92332,101712,112046]
        XP_requise=[XP_requise_LV1,XP_requise_LV2,XP_requise_LV3,XP_requise_LV4,XP_requise_LV5,XP_requise_LV6]
        XP_avant_prochain_niveau=XP_requise[monstre.classe-1][monstre.niveau-1]
        return XP_avant_prochain_niveau

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


    def Monter_en_niveau(monstre):
        monstre.niveau+=1
        monstre=Runes.MalusDeRunes(monstre)
        print('Félicitations!! ',monstre.surnom,' est désormais niveau ',monstre.niveau,'!!')
        str(input(' > '))
        if(Donjon.Niveau_max_de_la_classe_atteint(monstre)==True):
            print(monstre.surnom,' a atteint le niveau max de sa classe et doit désormais évoluer pour pouvoir passer en niveau!!')
            monstre.XP_avant_prochain_niveau=MAX
        else:
            monstre.XP_avant_prochain_niveau=Donjon.Trouver_XP_avant_prochain_niveau(monstre)
            nb_passages_niveau=9+5*monstre.classe
            if(monstre.classe==1):
                pv_min=monstre.pv_min_1
                attaque_min=monstre.attaque_min_1
                defense_min=monstre.defense_min_1
                pv_max=monstre.pv_max_1
                attaque_max=monstre.attaque_max_1
                defense_max=monstre.defense_max_1
            if(monstre.classe==2):
                pv_min=monstre.pv_min_2
                attaque_min=monstre.attaque_min_2
                defense_min=monstre.defense_min_2
                pv_max=monstre.pv_max_2
                attaque_max=monstre.attaque_max_2
                defense_max=monstre.defense_max_2
            if(monstre.classe==3):
                pv_min=monstre.pv_min_3
                attaque_min=monstre.attaque_min_3
                defense_min=monstre.defense_min_3
                pv_max=monstre.pv_max_3
                attaque_max=monstre.attaque_max_3
                defense_max=monstre.defense_max_3
            if(monstre.classe==4):
                pv_min=monstre.pv_min_4
                attaque_min=monstre.attaque_min_4
                defense_min=monstre.defense_min_4
                pv_max=monstre.pv_max_4
                attaque_max=monstre.attaque_max_4
                defense_max=monstre.defense_max_4
            if(monstre.classe==5):
                pv_min=monstre.pv_min_5
                attaque_min=monstre.attaque_min_5
                defense_min=monstre.defense_min_5
                pv_max=monstre.pv_max_5
                attaque_max=monstre.attaque_max_5
                defense_max=monstre.defense_max_5
            if(monstre.classe==6):
                pv_min=monstre.pv_min_6
                attaque_min=monstre.attaque_min_6
                defense_min=monstre.defense_min_6
                pv_max=monstre.pv_max_6
                attaque_max=monstre.attaque_max_6
                defense_max=monstre.defense_max_6

            bonus_pv=Arrondir((pv_max-pv_min)/nb_passages_niveau)
            bonus_attaque=Arrondir((attaque_max-attaque_min)/nb_passages_niveau)
            bonus_defense=Arrondir((defense_max-defense_min)/nb_passages_niveau)

            monstre.pv+=bonus_pv
            monstre.attaque+=bonus_attaque
            monstre.defense+=bonus_defense
            if(Donjon.Niveau_max_de_la_classe_atteint(monstre)==True):
                monstre.pv=pv_max
                monstre.attaque=attaque_max
                monstre.defense=defense_max
            if(monstre.pv>0):
                monstre.pv_actuels+=bonus_pv
            monstre.attaque_actuelle+=bonus_attaque
            monstre.defense_actuelle+=bonus_defense

        monstre=Runes.BonusDeRunes(monstre)
        ''' Actualise le gain en pourcentage de pv des runes et les applique '''

        print(monstre)

    def Monter_en_niveau_sans_affichage(monstre):
        monstre.niveau+=1
        monstre=Runes.MalusDeRunes(monstre)
        if(Donjon.Niveau_max_de_la_classe_atteint(monstre)==True):
            monstre.XP_avant_prochain_niveau=MAX
        else:
            monstre.XP_avant_prochain_niveau=Donjon.Trouver_XP_avant_prochain_niveau(monstre)
            nb_passages_niveau=9+5*monstre.classe

            if(monstre.classe==1):
                pv_min=monstre.pv_min_1
                attaque_min=monstre.attaque_min_1
                defense_min=monstre.defense_min_1
                pv_max=monstre.pv_max_1
                attaque_max=monstre.attaque_max_1
                defense_max=monstre.defense_max_1
            if(monstre.classe==2):
                pv_min=monstre.pv_min_2
                attaque_min=monstre.attaque_min_2
                defense_min=monstre.defense_min_2
                pv_max=monstre.pv_max_2
                attaque_max=monstre.attaque_max_2
                defense_max=monstre.defense_max_2
            if(monstre.classe==3):
                pv_min=monstre.pv_min_3
                attaque_min=monstre.attaque_min_3
                defense_min=monstre.defense_min_3
                pv_max=monstre.pv_max_3
                attaque_max=monstre.attaque_max_3
                defense_max=monstre.defense_max_3
            if(monstre.classe==4):
                pv_min=monstre.pv_min_4
                attaque_min=monstre.attaque_min_4
                defense_min=monstre.defense_min_4
                pv_max=monstre.pv_max_4
                attaque_max=monstre.attaque_max_4
                defense_max=monstre.defense_max_4
            if(monstre.classe==5):
                pv_min=monstre.pv_min_5
                attaque_min=monstre.attaque_min_5
                defense_min=monstre.defense_min_5
                pv_max=monstre.pv_max_5
                attaque_max=monstre.attaque_max_5
                defense_max=monstre.defense_max_5
            if(monstre.classe==6):
                pv_min=monstre.pv_min_6
                attaque_min=monstre.attaque_min_6
                defense_min=monstre.defense_min_6
                pv_max=monstre.pv_max_6
                attaque_max=monstre.attaque_max_6
                defense_max=monstre.defense_max_6

            bonus_pv=Arrondir((pv_max-pv_min)/nb_passages_niveau)
            bonus_attaque=Arrondir((attaque_max-attaque_min)/nb_passages_niveau)
            bonus_defense=Arrondir((defense_max-defense_min)/nb_passages_niveau)
            monstre.pv+=bonus_pv
            monstre.attaque+=bonus_attaque
            monstre.defense+=bonus_defense
            if(monstre.pv>0):
                monstre.pv_actuels+=bonus_pv
            monstre.attaque_actuelle+=bonus_attaque
            monstre.defense_actuelle+=bonus_defense

        monstre=Runes.BonusDeRunes(monstre)
        ''' Actualise le gain en pourcentage ex. de pv des runes et les applique '''

        return monstre


    def Niveau_max_de_la_classe_atteint(monstre):
        if(monstre.niveau>=(10+5*monstre.classe)):
            summum=True
        else:
            summum=False
        return summum

    def SoignerTeamEnnemie(equipe_ennemie):
        i=0
        while(i<len(equipe_ennemie)):
            if(equipe_ennemie[i]!=0):
                equipe_ennemie[i].etatCap1='dispo'
                equipe_ennemie[i].attente1=0
                if(equipe_ennemie[i].nb_capacites>=2):
                    equipe_ennemie[i].etatCap2='dispo'
                    equipe_ennemie[i].attente2=0
                if(equipe_ennemie[i].nb_capacites>=3):
                    equipe_ennemie[i].etatCap3='dispo'
                    equipe_ennemie[i].attente3=0
            i+=1
        Monstre.SoignerEquipe(equipe_ennemie)
        return equipe_ennemie

    def CombatDonjon(base,sac,donjon,equipe_allies,choix_map,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales):
        Donjon.Position(donjon)
        allie1=equipe_allies[0]
        allie2=equipe_allies[1]
        allie3=equipe_allies[2]
        equipe_allies_tmp=[allie1]
        if(allie2!=0):
            equipe_allies_tmp.append(allie2)
        if(allie3!=0):
            equipe_allies_tmp.append(allie3)
        equipe_ennemis=Donjon.monstres_region(donjon)

        ''' On réinitialise ici toutes les stats max_donjons '''
        ''' Pas besoin de les modifier dans les Anti '''
        for a in range(len(equipe_ennemis)):
            equipe_ennemis[a]=Preparer_au_combat(equipe_ennemis[a])
        ''' Si ForetVeur Niveau 1, region = 3 mais on prépare quand même au combat '''
        if(donjon.region==1 or (donjon.nom_famille=='ForetVeur' and donjon.niveau==1)):
            for b in range(len(equipe_allies_tmp)):
                equipe_allies_tmp[b]=Preparer_au_combat(equipe_allies_tmp[b])

        survivants=Combat_xVx_avec_capacites_speciales(equipe_allies_tmp,equipe_ennemis)
        equipe_ennemis=Donjon.monstres_region(donjon)
        equipe_ennemis=Donjon.SoignerTeamEnnemie(equipe_ennemis)

        '''
        equipe_allies_tmp=[allie1]
        if(allie2!=0):
            equipe_allies_tmp.append(allie2)
        if(allie3!=0):
            equipe_allies_tmp.append(allie3)
        '''

        if(survivants=='allies'):
            for i in range(len(equipe_allies_tmp)):
                equipe_allies_tmp[i].jauge_attaque=0
            if(donjon.region<3):
                equipe_allies=Monstre.SoignerEquipeEntreDeuxVagues(equipe_allies)
                print('L état de l équipe est désormais : \n')
                equipe.afficher(equipe_allies)
                print('\n\n Vous avancez dans ',donjon.nom,'... \n')
                str(input(' > '))
            donjon.region+=1
            if (donjon.region>3):
                print('Félicitations!! Vous avez terminé ',donjon.nom,'!! \n')
                str(input(' > '))
                for j in range(len(equipe_allies_tmp)):
                    Donjon.RecevoirXP(equipe_allies_tmp[j],donjon.recompense[0])
                    equipe_allies_tmp[j].jauge_attaque=0

                sac=Donjon.RecevoirGold(sac,donjon.recompense[0],len(equipe_ennemis))
                donjon.recompense[1]=Generateur_de_recompenses(donjon.nom_famille,donjon.niveau)

                if(donjon.recompense[1][0]=='Parchemin d invocation' or donjon.recompense[1][0]=='Parchemin d invocation superieure' or donjon.recompense[1][0]=='Rune'):
                    Recompense_texte=donjon.recompense[1][0]
                    Recompense=donjon.recompense[1][1]
                    print('Vous recevez comme récompense : \n')
                    if(Recompense_texte=='Rune'):
                        Runes.Initialiser(Recompense)
                        Inventaire.ajouter_objet(sac,Recompense)
                        print(Recompense,'\n')
                    elif(Recompense_texte=='Parchemin d invocation' or Recompense_texte=='Parchemin d invocation superieure'):
                        print(Recompense,Recompense_texte,'!! \n')
                        for b in range(Recompense):
                            Inventaire.ajouter_objet(sac,Objets(Recompense_texte))
                elif(donjon.recompense[1][0]=='Mana'):
                    sac.mana+=donjon.recompense[1][1]
                    print('Vous recevez comme récompense : \n',donjon.recompense[1][1],' pierres de Mana!! \n')
                    print('Vous avez désormais ',sac.mana,' pierres de Mana!! \n\n')
                elif(donjon.recompense[1][0]=='Cristal'):
                    if (donjon.recompense[1][1]==1):
                        sac.cristaux+=donjon.recompense[1][1]
                        print('Vous recevez comme récompense : \n',donjon.recompense[1][1],' Cristal!! \n')
                        print('Vous avez désormais ',sac.cristaux,' cristaux!! \n\n')
                    else:
                        sac.cristaux+=donjon.recompense[1][1]
                        print('Vous recevez comme récompense : \n',donjon.recompense[1][1],' Cristaux!! \n')
                        print('Vous avez désormais ',sac.cristaux,' cristaux!! \n\n')
                str(input(' > '))

                modifies=Donjon.DebloquerDonjon(donjon,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,choix_map)
                Niveaux_donjons_debloques=modifies[0]
                donjons_dispo=modifies[1]
                noms_donjons_dispo=modifies[2]

                if(donjon.niveau==7):
                    '''[recompenses_donnees,recompenses_globales,types_recompenses_globales]'''
                    if(recompenses_globales_totales[0][choix_map]==0):
                        print('Vous recevez une récompense exclusive pour avoir terminé ',donjon.nom,'pour la première fois!!')
                        if(recompenses_globales_totales[2][choix_map]=='Monstre'):
                            print('Vous recevez : \n')
                            #print(recompenses_globales_totales)
                            print(recompenses_globales_totales[1][choix_map])
                            Base.ajouter_monstre(base,recompenses_globales_totales[1][choix_map])
                        elif(recompenses_globales_totales[2][choix_map]=='Monstres'):
                            print(recompenses_globales_totales)
                            for k in range(len(recompenses_globales_totales[1][choix_map])):
                                print('Vous recevez : \n')
                                str(input(' > '))
                                print(recompenses_globales_totales[1][choix_map][k])
                                Base.ajouter_monstre(base,recompenses_globales_totales[1][choix_map][k])
                        elif(recompenses_globales_totales[2][choix_map]=='Runes'):
                            for m in range(len(recompenses_globales_totales[1][choix_map])):
                                print('Vous recevez : \n')
                                str(input(' > '))
                                print(recompenses_globales_totales[1][choix_map][m])
                                Inventaire.ajouter_objet(sac,recompenses_globales_totales[1][choix_map][m])
                        str(input(' > '))
                        recompenses_globales_totales[0][choix_map]=1
                Donjon.Rentrer(base,equipe_allies,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo)
            else:
                Donjon.CombatDonjon(base,sac,donjon,equipe_allies,choix_map,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)
        else:
            ''' FAIRE UNE RECOMPENSE PARTIELLE EN XP ET EN MANA '''
            print('Vous avez perdu... \n\n\n\n')
            equipe_ennemis=Donjon.monstres_region(donjon)
            equipe_ennemis=Donjon.SoignerTeamEnnemie(equipe_ennemis)

            '''
            equipe_allies=[allie1]
            if(allie2!=0):
                equipe_allies.append(allie2)
            if(allie3!=0):
                equipe_allies.append(allie3)
            '''
            Donjon.Rentrer(base,equipe_allies,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo)

    def DebloquerDonjon(donjon,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,choix_map):
        if(Niveaux_donjons_debloques[choix_map]<7):
            if(donjon.niveau==Niveaux_donjons_debloques[choix_map]):
                Niveaux_donjons_debloques[choix_map]+=1
        else:
            if(donjons_dispo[choix_map][donjon.niveau-1][0]=='la Forêt Veur Niveau 7 - Clairière ' and 'Cratère Ater' not in noms_donjons_dispo):
                Niveaux_donjons_debloques.append(1)
                noms_donjons_dispo.append('Cratère Ater')
                print('Une nouvelle zone devient diponible : le Cratère Ater!! \n')
            if(donjons_dispo[choix_map][donjon.niveau-1][0]=='le Cratère Ater Niveau 7 - Caverne des Profondeurs ' and 'Mont Tagne' not in noms_donjons_dispo):
                Niveaux_donjons_debloques.append(1)
                noms_donjons_dispo.append('Mont Tagne')
                print('Une nouvelle zone devient diponible : le Mont Tagne!! \n')
            if(donjons_dispo[choix_map][donjon.niveau-1][0]=='le Mont Tagne Niveau 7 - Caverne au Sommet ' and 'Ruines de Senzargen' not in noms_donjons_dispo):
                Niveaux_donjons_debloques.append(1)
                noms_donjons_dispo.append('Ruines de Senzargen')
                print('Une nouvelle zone devient diponible : les Ruines de Senzargen!! \n')
            str(input(' > '))
        # DEBLOQUER LES DONJONS EN FONCTION DE LA DIFFICULTE DU PRECEDENT
        modifies=[Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo]
        return modifies











def Generateur_de_recompenses(nom_donjon,niveau_donjon):
    if(nom_donjon=='ForetVeur'):
        recompense=Recompenses_ForetVeur(niveau_donjon)
    if(nom_donjon=='CratereAter'):
        recompense=Recompenses_CratereAter(niveau_donjon)
    if(nom_donjon=='MontTagne'):
        recompense=Recompenses_MontTagne(niveau_donjon)
    if(nom_donjon=='RuinesSenzargen'):
        recompense=Recompenses_RuinesSenzargen(niveau_donjon)
    return recompense


def ForetVeur_Niveau1():
    nom='la Forêt Veur Niveau 1 - Entrée '
    nom_famille='ForetVeur'
    niveau=1
    attribut='Eau'

    monstre1=Sanglier()
    while(monstre1.attribut!='Vent'):
        monstre1=Sanglier()
    monstre1.surnom='Sanglier vert'

    monstre2=Sanglier()
    while(monstre2.attribut!='Feu'):
        monstre2=Sanglier()
    monstre2.surnom='Sanglier rouge'

    demiBoss1=Sanglier()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=Sanglier()
    demiBoss1.surnom='Gros sanglier vert'

    monstre3=Sanglier()
    while(monstre3.attribut!='Vent'):
        monstre3=Sanglier()
    monstre3.surnom='Sanglier vert'

    monstre4=Sanglier()
    while(monstre4.attribut!='Feu'):
        monstre4=Sanglier()
    monstre4.surnom='Sanglier rouge'

    demiBoss2=Sanglier()
    while(demiBoss2.attribut!='Feu'):
        demiBoss2=Sanglier()
    demiBoss2.surnom='Gros sanglier rouge'

    monstre5=Sanglier()
    while(monstre5.attribut!='Vent'):
        monstre5=Sanglier()
    monstre5.surnom='Sanglier vert'

    monstre6=Sanglier()
    while(monstre6.attribut!='Feu'):
        monstre6=Sanglier()
    monstre6.surnom='Sanglier rouge'

    Boss=Sanglier()
    while(Boss.attribut!='Vent'):
        Boss=Sanglier()
    Boss.surnom='Sanglier vert géant'

    XP_recompense=320
    Recompense_liste=Recompenses_ForetVeur(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def ForetVeur_Niveau2():
    nom='la Forêt Veur Niveau 2 - Est '
    nom_famille='ForetVeur'
    niveau=2
    attribut='Feu'

    monstre1=Champignon()
    while(monstre1.attribut!='Vent'):
        monstre1=Champignon()
    monstre1.surnom='Champignon vert'

    monstre2=Champignon()
    while(monstre2.attribut!='Feu'):
        monstre2=Champignon()
    monstre2.surnom='Champignon rouge'

    demiBoss1=Champignon()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=Champignon()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    demiBoss1.surnom='Gros champignon vert'

    monstre3=Champignon()
    while(monstre3.attribut!='Feu'):
        monstre3=Champignon()
    monstre3.surnom='Champignon rouge'

    monstre4=Champignon()
    while(monstre4.attribut!='Eau'):
        monstre4=Champignon()
    monstre4.surnom='Champignon bleu'

    demiBoss2=Champignon()
    while(demiBoss2.attribut!='Eau'):
        demiBoss2=Champignon()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    demiBoss2.surnom='Gros champignon bleu'

    monstre5=Champignon()
    while(monstre5.attribut!='Vent'):
        monstre5=Champignon()
    monstre5.surnom='Champignon vert'

    monstre6=Champignon()
    while(monstre6.attribut!='Feu'):
        monstre6=Champignon()
    monstre6.surnom='Champignon rouge'

    Boss=Sanglier()
    while(Boss.attribut!='Feu'):
        Boss=Sanglier()
    Boss=Monstre.Evoluer(Boss)
    Boss.surnom='Sanglier rouge géant'

    XP_recompense=800
    Recompense_liste=Recompenses_ForetVeur(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def ForetVeur_Niveau3():
    nom='la Forêt Veur Niveau 3 - Sud '
    nom_famille='ForetVeur'
    niveau=3
    attribut='Vent'

    monstre1=GardienForet()
    while(monstre1.attribut!='Feu'):
        monstre1=GardienForet()
    monstre1.surnom='Gardien de Feu de la Forêt'

    monstre2=GardienForet()
    while(monstre2.attribut!='Vent'):
        monstre2=GardienForet()
    monstre2.surnom='Gardien de Vent de la Forêt'

    demiBoss1=GardienForet()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=GardienForet()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grand Gardien de Vent de la Forêt'

    monstre3=GardienForet()
    while(monstre3.attribut!='Feu'):
        monstre3=GardienForet()
    monstre3.surnom='Gardien de Feu de la Forêt'

    monstre4=GardienForet()
    while(monstre4.attribut!='Eau'):
        monstre4=GardienForet()
    monstre4.surnom='Gardien d\'Eau de la Forêt'

    demiBoss2=GardienForet()
    while(demiBoss2.attribut!='Eau'):
        demiBoss2=GardienForet()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grand Gardien de l\'Eau de la Forêt'

    monstre5=GardienForet()
    while(monstre5.attribut!='Vent'):
        monstre5=GardienForet()
    monstre5.surnom='Gardien de Vent de la Forêt'

    monstre6=GardienForet()
    while(monstre6.attribut!='Vent'):
        monstre6=GardienForet()
    monstre6.surnom='Gardien de Vent de la Forêt'

    Boss=GardienForet()
    while(Boss.attribut!='Vent'):
        Boss=GardienForet()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Gardien suprême de Vent de la Forêt'

    XP_recompense=803
    Recompense_liste=Recompenses_ForetVeur(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def ForetVeur_Niveau4():
    nom='la Forêt Veur Niveau 4 - Ouest '
    nom_famille='ForetVeur'
    niveau=4
    attribut='Feu'

    monstre1=Sanglier()
    while(monstre1.attribut!='Feu'):
        monstre1=Sanglier()
    monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Sanglier rouge'

    monstre2=Sanglier()
    while(monstre2.attribut!='Vent'):
        monstre2=Sanglier()
    monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Sanglier vert'

    demiBoss1=Sanglier()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=Sanglier()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Gros sanglier vert'

    monstre3=Sanglier()
    while(monstre3.attribut!='Feu'):
        monstre3=Sanglier()
    monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Sanglier rouge'

    monstre4=Sanglier()
    while(monstre4.attribut!='Eau'):
        monstre4=Sanglier()
    monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Sanglier bleu'

    demiBoss2=Sanglier()
    while(demiBoss2.attribut!='Eau'):
        demiBoss2=Sanglier()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Gros sanglier bleu'

    monstre5=Sanglier()
    while(monstre5.attribut!='Feu'):
        monstre5=Sanglier()
    monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Sanglier rouge 1'

    monstre6=Sanglier()
    while(monstre6.attribut!='Feu'):
        monstre6=Sanglier()
    monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Sanglier rouge 2'

    Boss=Sanglier()
    while(Boss.attribut!='Feu'):
        Boss=Sanglier()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Sanglier rouge géant'

    XP_recompense=1127
    Recompense_liste=Recompenses_ForetVeur(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def ForetVeur_Niveau5():
    nom='la Forêt Veur Niveau 5 - Nord '
    nom_famille='ForetVeur'
    niveau=5
    attribut='Eau'

    monstre1=PlanteCarnivore()
    while(monstre1.attribut!='Eau'):
        monstre1=PlanteCarnivore()
    monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Plante carnivore bleue'

    monstre2=PlanteCarnivore()
    while(monstre2.attribut!='Feu'):
        monstre2=PlanteCarnivore()
    monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Plante carnivore rouge'

    demiBoss1=PlanteCarnivore()
    while(demiBoss1.attribut!='Eau'):
        demiBoss1=PlanteCarnivore()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grosse plante carnivore bleue'

    monstre3=PlanteCarnivore()
    while(monstre3.attribut!='Feu'):
        monstre3=PlanteCarnivore()
    monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Plante carnivore rouge'

    monstre4=PlanteCarnivore()
    while(monstre4.attribut!='Vent'):
        monstre4=PlanteCarnivore()
    monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Plante carnivore verte'

    demiBoss2=PlanteCarnivore()
    while(demiBoss2.attribut!='Vent'):
        demiBoss2=PlanteCarnivore()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grosse plante carnivore verte'

    monstre5=PlanteCarnivore()
    while(monstre5.attribut!='Eau'):
        monstre5=PlanteCarnivore()
    monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Plante carnivore bleue'

    monstre6=PlanteCarnivore()
    while(monstre6.attribut!='Feu'):
        monstre6=PlanteCarnivore()
    monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Plante carnivore rouge'

    Boss=PlanteCarnivore()
    while(Boss.attribut!='Eau'):
        Boss=PlanteCarnivore()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Plante carnivore bleue géante'

    XP_recompense=1130
    Recompense_liste=Recompenses_ForetVeur(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def ForetVeur_Niveau6():
    nom='la Forêt Veur Niveau 6 - Profondeurs '
    nom_famille='ForetVeur'
    niveau=6
    attribut='Eau'

    monstre1=Champignon()
    while(monstre1.attribut!='Vent'):
        monstre1=Champignon()
    monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Champignon vert'

    monstre2=Champignon()
    while(monstre2.attribut!='Feu'):
        monstre2=Champignon()
    monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Champignon rouge'

    demiBoss1=Champignon()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=Champignon()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Gros champignon vert'

    monstre3=Champignon()
    while(monstre3.attribut!='Feu'):
        monstre3=Champignon()
    monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Champignon rouge'

    monstre4=Champignon()
    while(monstre4.attribut!='Eau'):
        monstre4=Champignon()
    monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Champignon bleu'

    demiBoss2=Champignon()
    while(demiBoss2.attribut!='Eau'):
        demiBoss2=Champignon()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Gros champignon bleu'

    monstre5=Champignon()
    while(monstre5.attribut!='Vent'):
        monstre5=Champignon()
    monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Champignon vert'

    monstre6=Champignon()
    while(monstre6.attribut!='Eau'):
        monstre6=Champignon()
    monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Champignon bleu'

    Boss=Champignon()
    while(Boss.attribut!='Eau'):
        Boss=Champignon()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Champignon bleu géant'

    XP_recompense=1132
    Recompense_liste=Recompenses_ForetVeur(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def ForetVeur_Clairiere():
    nom='la Forêt Veur Niveau 7 - Clairière '
    nom_famille='ForetVeur'
    niveau=7
    attribut='Eau'

    monstre1=PlanteCarnivore()
    while(monstre1.attribut!='Eau'):
        monstre1=PlanteCarnivore()
    monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Plante carnivore bleue'

    monstre2=PlanteCarnivore()
    while(monstre2.attribut!='Vent'):
        monstre2=PlanteCarnivore()
    monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Plante carnivore verte'

    demiBoss1=PlanteCarnivore()
    while(demiBoss1.attribut!='Eau'):
        demiBoss1=PlanteCarnivore()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grosse plante carnivore bleue'

    monstre3=PlanteCarnivore()
    while(monstre3.attribut!='Eau'):
        monstre3=PlanteCarnivore()
    monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Plante carnivore bleue'

    monstre4=PlanteCarnivore()
    while(monstre4.attribut!='Vent'):
        monstre4=PlanteCarnivore()
    monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Plante carnivore verte'

    demiBoss2=PlanteCarnivore()
    while(demiBoss2.attribut!='Vent'):
        demiBoss2=PlanteCarnivore()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grosse plante carnivore verte'

    monstre5=PlanteCarnivore()
    while(monstre5.attribut!='Eau'):
        monstre5=PlanteCarnivore()
    monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Plante carnivore bleue 1'

    monstre6=PlanteCarnivore()
    while(monstre6.attribut!='Eau'):
        monstre6=PlanteCarnivore()
    monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Plante carnivore bleue 2'

    Boss=Inugami()
    while(Boss.attribut!='Eau'):
        Boss=Inugami()
    Boss=Monstre.Evoluer(Boss)
    Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Inugami bleu Royal'
    Boss.capacite2=Boss.capacite1
    Boss.capacite2Nom=Boss.capacite1Nom
    Boss.Trecharge2=1
    Boss.attente2=0
    Boss.etatCap2='dispo'
    Boss.vitesse_max_donjons=2*Boss.vitesse_max_donjons
    Boss.vitesse=2*Boss.vitesse
    Boss.vitesse_actuelle=Boss.vitesse_max_donjons
    XP_recompense=812
    Recompense_liste=Recompenses_ForetVeur(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def ForetVeur():
    caracteristiques=[ForetVeur_Niveau1(),ForetVeur_Niveau2(),ForetVeur_Niveau3(),ForetVeur_Niveau4(),ForetVeur_Niveau5(),ForetVeur_Niveau6(),ForetVeur_Clairiere()]
    return caracteristiques


def Recompenses_ForetVeur(niveau_donjon):
    ''' Rajouter le parchmin d invocation Inugami d Eau '''
    recompenses_dispo=['Mana','Parchemin d invocation','Rune','Cristal']
    chance_premiere_recompense=0.25
    chance_deuxieme_recompense=0.15
    chance_troisieme_recompense=0.55
    nombre_aleatoire=(random.randint(1,100))/100
    if(nombre_aleatoire<=chance_deuxieme_recompense):
        recompense_texte=recompenses_dispo[1]
    elif(nombre_aleatoire<=chance_troisieme_recompense):
        recompense_texte=recompenses_dispo[2]
    elif(nombre_aleatoire>(1-chance_premiere_recompense)):
        recompense_texte=recompenses_dispo[0]
    else:
        recompense_texte=recompenses_dispo[3]
    if(recompense_texte=='Mana'):
        recompense=niveau_donjon*1000
    if(recompense_texte=='Cristal'):
        recompense=niveau_donjon
    if(recompense_texte=='Parchemin d invocation'):
        recompense=niveau_donjon
    if(recompense_texte=='Rune'):
        ''' __init__(self,NOM,CATEGORIE,POSITION,QUALITE,RARETE,BONUS): '''
        categories_possibles=['HP+','HP%','ATK+','ATK%','DEF+','DEF%','VIT+','TCC%','DC%','ACC%','RES%']
        categorie_aleatoire=categories_possibles[(random.randint(0,10))]
        positions_possibles=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']
        if(niveau_donjon!=7):
            position=positions_possibles[niveau_donjon-1]
        else:
            position=positions_possibles[random.randint(0,5)]
        recompense=Runes('Rune Energie I','Energie',position,'I','Normale',categorie_aleatoire)
    return [recompense_texte,recompense]





def MontTagne_Niveau1():
    nom='le Mont Tagne Niveau 1 - Pied '
    nom_famille='MontTagne'
    niveau=1
    attribut='Vent'

    monstre1=Canniboite()
    while(monstre1.attribut!='Vent'):
        monstre1=Canniboite()
    while(monstre1.niveau!=3):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Canniboite verte'

    monstre2=Slime()
    while(monstre2.attribut!='Vent'):
        monstre2=Slime()
    while(monstre2.niveau!=3):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Slime vert'

    demiBoss1=Canniboite()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=Canniboite()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=3):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grosse canniboite verte'

    monstre3=Canniboite()
    while(monstre3.attribut!='Feu'):
        monstre3=Canniboite()
    while(monstre3.niveau!=3):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Canniboite rouge'

    monstre4=Slime()
    while(monstre4.attribut!='Feu'):
        monstre4=Slime()
    while(monstre4.niveau!=3):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Slime rouge'

    demiBoss2=Canniboite()
    while(demiBoss2.attribut!='Feu'):
        demiBoss2=Canniboite()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=3):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grosse canniboite rouge'

    monstre5=Canniboite()
    while(monstre5.attribut!='Vent'):
        monstre5=Canniboite()
    while(monstre5.niveau!=3):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Canniboite verte'

    monstre6=Slime()
    while(monstre6.attribut!='Feu'):
        monstre6=Slime()
    while(monstre6.niveau!=3):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Slime rouge'

    Boss=Canniboite()
    while(Boss.attribut!='Vent'):
        Boss=Canniboite()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=4):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Canniboite verte géante'

    XP_recompense=1144
    Recompense_liste=Recompenses_MontTagne(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def MontTagne_Niveau2():
    nom='le Mont Tagne Niveau 2 - Chemin souterrain '
    nom_famille='MontTagne'
    niveau=2
    attribut='Feu'

    monstre1=Slime()
    while(monstre1.attribut!='Vent'):
        monstre1=Slime()
    while(monstre1.niveau!=4):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Slime vert'

    monstre2=Slime()
    while(monstre2.attribut!='Eau'):
        monstre2=Slime()
    while(monstre2.niveau!=4):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Slime bleu'

    demiBoss1=Slime()
    while(demiBoss1.attribut!='Feu'):
        demiBoss1=Slime()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=4):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Gros slime rouge'

    monstre3=Slime()
    while(monstre3.attribut!='Feu'):
        monstre3=Slime()
    while(monstre3.niveau!=4):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Slime rouge'

    monstre4=Slime()
    while(monstre4.attribut!='Eau'):
        monstre4=Slime()
    while(monstre4.niveau!=4):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Slime bleu'

    demiBoss2=Slime()
    while(demiBoss2.attribut!='Vent'):
        demiBoss2=Slime()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=4):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Gros slime vert'

    monstre5=Slime()
    while(monstre5.attribut!='Eau'):
        monstre5=Slime()
    while(monstre5.niveau!=4):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Slime bleu'

    monstre6=Slime()
    while(monstre6.attribut!='Feu'):
        monstre6=Slime()
    while(monstre6.niveau!=4):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Slime rouge'

    Boss=Slime()
    while(Boss.attribut!='Feu'):
        Boss=Slime()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=4):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Slime rouge géant'

    XP_recompense=1148
    Recompense_liste=Recompenses_MontTagne(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def MontTagne_Niveau3():
    nom='le Mont Tagne Niveau 3 - Caverne intermédiaire '
    nom_famille='MontTagne'
    niveau=3
    attribut='Eau'

    monstre1=Spectre()
    while(monstre1.attribut!='Feu'):
        monstre1=Spectre()
    while(monstre1.niveau!=4):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Spectre rouge'

    monstre2=Slime()
    while(monstre2.attribut!='Feu'):
        monstre2=Slime()
    while(monstre2.niveau!=4):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Slime rouge'

    demiBoss1=Slime()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=Slime()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=4):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Gros slime vert'

    monstre3=Spectre()
    while(monstre3.attribut!='Vent'):
        monstre3=Spectre()
    while(monstre3.niveau!=4):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Spectre vert'

    monstre4=Spectre()
    while(monstre4.attribut!='Eau'):
        monstre4=Spectre()
    while(monstre4.niveau!=4):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Spectre bleu'

    demiBoss2=Spectre()
    while(demiBoss2.attribut!='Eau'):
        demiBoss2=Spectre()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=4):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.nom='Grand spectre bleu'

    monstre5=Spectre()
    while(monstre5.attribut!='Vent'):
        monstre5=Spectre()
    while(monstre5.niveau!=4):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Spectre vert'

    monstre6=Spectre()
    while(monstre6.attribut!='Eau'):
        monstre6=Spectre()
    while(monstre6.niveau!=4):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Spectre bleu'

    Boss=Slime()
    while(Boss.attribut!='Eau'):
        Boss=Slime()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=5):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Slime bleu géant'

    XP_recompense=1153
    Recompense_liste=Recompenses_MontTagne(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def MontTagne_Niveau4():
    nom='le Mont Tagne Niveau 4 - Plateau '
    nom_famille='MontTagne'
    niveau=4
    attribut='Vent'

    monstre1=Golem()
    while(monstre1.attribut!='Feu'):
        monstre1=Golem()
    while(monstre1.niveau!=5):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Golem rouge'

    monstre2=Golem()
    while(monstre2.attribut!='Eau'):
        monstre2=Golem()
    while(monstre2.niveau!=5):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Golem bleu'

    demiBoss1=Golem()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=Golem()
    while(demiBoss1.niveau!=5):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grand golem vert'

    monstre3=Golem()
    while(monstre3.attribut!='Eau'):
        monstre3=Golem()
    while(monstre3.niveau!=5):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Golem bleu'

    monstre4=Golem()
    while(monstre4.attribut!='Vent'):
        monstre4=Golem()
    while(monstre4.niveau!=5):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Golem vert'

    demiBoss2=Golem()
    while(demiBoss2.attribut!='Feu'):
        demiBoss2=Golem()
    while(demiBoss2.niveau!=5):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grand golem rouge'

    monstre5=Golem()
    while(monstre5.attribut!='Feu'):
        monstre5=Golem()
    while(monstre5.niveau!=5):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Golem rouge'

    monstre6=Golem()
    while(monstre6.attribut!='Vent'):
        monstre6=Golem()
    while(monstre6.niveau!=5):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Golem vert'

    Boss=Golem()
    while(Boss.attribut!='Vent'):
        Boss=Golem()
    while(Boss.niveau!=5):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Golem vert géant'

    XP_recompense=1159
    Recompense_liste=Recompenses_MontTagne(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def MontTagne_Niveau5():
    nom='le Mont Tagne Niveau 5 - Ascension '
    nom_famille='MontTagne'
    niveau=5
    attribut='Feu'

    monstre1=Golem()
    while(monstre1.attribut!='Feu'):
        monstre1=Golem()
    while(monstre1.niveau!=6):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Golem rouge'

    monstre2=Golem()
    while(monstre2.attribut!='Vent'):
        monstre2=Golem()
    while(monstre2.niveau!=6):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Golem vert'

    demiBoss1=Golem()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=Golem()
    while(demiBoss1.niveau!=6):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grand golem vert'

    monstre3=Golem()
    while(monstre3.attribut!='Feu'):
        monstre3=Golem()
    while(monstre3.niveau!=6):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Golem rouge'

    monstre4=Golem()
    while(monstre4.attribut!='Vent'):
        monstre4=Golem()
    while(monstre4.niveau!=6):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Golem vert'

    demiBoss2=Golem()
    while(demiBoss2.attribut!='Feu'):
        demiBoss2=Golem()
    while(demiBoss2.niveau!=6):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grand golem rouge'

    monstre5=Golem()
    while(monstre5.attribut!='Feu'):
        monstre5=Golem()
    while(monstre5.niveau!=6):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Golem rouge 1'

    monstre6=Golem()
    while(monstre6.attribut!='Feu'):
        monstre6=Golem()
    while(monstre6.niveau!=6):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Golem rouge 2'

    Boss=Golem()
    while(Boss.attribut!='Feu'):
        Boss=Golem()
    while(Boss.niveau!=6):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Golem rouge géant'

    XP_recompense=1169
    Recompense_liste=Recompenses_MontTagne(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def MontTagne_Niveau6():
    nom='le Mont Tagne Niveau 6 - Sommet '
    nom_famille='MontTagne'
    niveau=6
    attribut='Eau'

    monstre1=Golem()
    while(monstre1.attribut!='Eau'):
        monstre1=Golem()
    while(monstre1.niveau!=7):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Golem bleu'

    monstre2=Golem()
    while(monstre2.attribut!='Feu'):
        monstre2=Golem()
    while(monstre2.niveau!=7):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Golem rouge'

    demiBoss1=Golem()
    while(demiBoss1.attribut!='Eau'):
        demiBoss1=Golem()
    while(demiBoss1.niveau!=7):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grand golem bleu'

    monstre3=Golem()
    while(monstre3.attribut!='Vent'):
        monstre3=Golem()
    while(monstre3.niveau!=7):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Golem vert 1'

    monstre4=Golem()
    while(monstre4.attribut!='Vent'):
        monstre4=Golem()
    while(monstre4.niveau!=7):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Golem vert 2'

    demiBoss2=Golem()
    while(demiBoss2.attribut!='Feu'):
        demiBoss2=Golem()
    while(demiBoss2.niveau!=7):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grand golem rouge'

    monstre5=Golem()
    while(monstre5.attribut!='Feu'):
        monstre5=Golem()
    while(monstre5.niveau!=7):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Golem rouge'

    monstre6=Canniboite()
    while(monstre6.attribut!='Vent'):
        monstre6=Canniboite()
    while(monstre6.niveau!=7):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Canniboite verte'

    Boss=Golem()
    while(Boss.attribut!='Eau'):
        Boss=Golem()
    while(Boss.niveau!=8):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Golem bleu géant'

    XP_recompense=1176
    Recompense_liste=Recompenses_MontTagne(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def MontTagne_Caverne():
    nom='le Mont Tagne Niveau 7 - Caverne au Sommet '
    nom_famille='MontTagne'
    niveau=7
    attribut='Feu'

    monstre1=Golem()
    while(monstre1.attribut!='Vent'):
        monstre1=Golem()
    while(monstre1.niveau!=7):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Golem vert 1'

    monstre2=Golem()
    while(monstre2.attribut!='Vent'):
        monstre2=Golem()
    while(monstre2.niveau!=7):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Golem vert 2'

    demiBoss1=Golem()
    while(demiBoss1.attribut!='Feu'):
        demiBoss1=Golem()
    while(demiBoss1.niveau!=7):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grand golem rouge'

    monstre3=Golem()
    while(monstre3.attribut!='Feu'):
        monstre3=Golem()
    while(monstre3.niveau!=7):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Golem rouge 1'

    monstre4=Golem()
    while(monstre4.attribut!='Feu'):
        monstre4=Golem()
    while(monstre4.niveau!=7):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Golem rouge 2'

    demiBoss2=Golem()
    while(demiBoss2.attribut!='Feu'):
        demiBoss2=Golem()
    while(demiBoss2.niveau!=7):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grand golem rouge'

    monstre5=Golem()
    while(monstre5.attribut!='Feu'):
        monstre5=Golem()
    while(monstre5.niveau!=7):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Golem rouge'

    monstre6=Golem()
    while(monstre6.attribut!='Vent'):
        monstre6=Golem()
    while(monstre6.niveau!=7):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Golem vert'

    Boss=Golem()
    while(Boss.attribut!='Feu'):
        Boss=Golem()
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=8):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Golem rouge Royal'
    Boss.defense_max_donjons=2*Boss.defense_max_donjons
    Boss.defense=2*Boss.defense
    Boss.defense_actuelle=Boss.defense_max_donjons
    XP_recompense=842
    Recompense_liste=Recompenses_MontTagne(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def MontTagne():
    caracteristiques=[MontTagne_Niveau1(),MontTagne_Niveau2(),MontTagne_Niveau3(),MontTagne_Niveau4(),MontTagne_Niveau5(),MontTagne_Niveau6(),MontTagne_Caverne()]
    return caracteristiques

def Recompenses_MontTagne(niveau_donjon):
    ''' Rajouter le parchmin d invocation Golem de Feu '''
    recompenses_dispo=['Mana','Parchemin d invocation','Rune','Cristal','Parchemin d invocation superieure']
    chance_premiere_recompense=0.2
    chance_deuxieme_recompense=0.15
    chance_troisieme_recompense=0.55
    chance_cinquieme_recompense=0.05
    nombre_aleatoire=(random.randint(1,100))/100
    if(nombre_aleatoire<=chance_cinquieme_recompense):
        recompense_texte=recompenses_dispo[4]
    elif(nombre_aleatoire<=chance_deuxieme_recompense):
        recompense_texte=recompenses_dispo[1]
    elif(nombre_aleatoire<=chance_troisieme_recompense):
        recompense_texte=recompenses_dispo[2]
    elif(nombre_aleatoire>(1-chance_premiere_recompense)):
        recompense_texte=recompenses_dispo[0]
    else:
        recompense_texte=recompenses_dispo[3]
    if(recompense_texte=='Mana'):
        recompense=niveau_donjon*1000
    if(recompense_texte=='Cristal'):
        recompense=niveau_donjon
    if(recompense_texte=='Parchemin d invocation'):
        recompense=niveau_donjon
    if(recompense_texte=='Parchemin d invocation superieure'):
        recompense=1
    if(recompense_texte=='Rune'):
        ''' __init__(self,NOM,CATEGORIE,POSITION,QUALITE,RARETE,BONUS): '''
        categories_possibles=['HP+','HP%','ATK+','ATK%','DEF+','DEF%','VIT+','TCC%','DC%','ACC%','RES%']
        categorie_aleatoire=categories_possibles[(random.randint(0,10))]
        positions_possibles=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']
        if(niveau_donjon!=7):
            position=positions_possibles[niveau_donjon-1]
        else:
            position=positions_possibles[random.randint(0,5)]
        recompense=Runes('Rune Colere I','Colere',position,'I','Normale',categorie_aleatoire)
    return [recompense_texte,recompense]




''' RECOMPENSES A CHANGER!!!!!!
    Faire des parchemins exclusifs à chaque donjon pour pouvoir drop ex. Mastodonte '''

''' MONSTRES ET ATTRIBUTS A CHANGER!!!!!! '''
''' A l\'avenir faire le Cratère Rible XD '''
''' Changer Désert Tic en Désert Sébon ou Désert Des Lisses//Licieux '''






'''
Pour ForetVeur les mobs seront :
Champignon, GardienForet, Sanglier, PlanteCarnivore, Inugami

Pour CraterAter les mobs seront :
ChauveSouris (Feu, Eau, Vent seulement), SoldatSquelette (idem), Imp, éventuellement Imp Champion, Mastodonte

Pour Mont Tagne les mobs seront :
Slime, Canniboite, Spectre, Golem
'''

def CratereAter_Niveau1():
    nom='le Cratère Ater Niveau 1 - Etage -1 '
    nom_famille='CratereAter'
    niveau=1
    attribut='Vent'

    monstre1=ChauveSouris()
    while(monstre1.attribut!='Vent'):
        monstre1=ChauveSouris()
    while(monstre1.niveau!=3):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Chauve souris verte'

    monstre2=ChauveSouris()
    while(monstre2.attribut!='Feu'):
        monstre2=ChauveSouris()
    while(monstre2.niveau!=3):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Chauve souris rouge'

    demiBoss1=ChauveSouris()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=ChauveSouris()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=3):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grosse chauve souris verte'

    monstre3=ChauveSouris()
    while(monstre3.attribut!='Vent'):
        monstre3=ChauveSouris()
    while(monstre3.niveau!=3):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Chauve souris verte'

    monstre4=ChauveSouris()
    while(monstre4.attribut!='Feu'):
        monstre4=ChauveSouris()
    while(monstre4.niveau!=3):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Chauve souris rouge'

    demiBoss2=ChauveSouris()
    while(demiBoss2.attribut!='Feu'):
        demiBoss2=ChauveSouris()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=3):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grosse chauve souris rouge'

    monstre5=ChauveSouris()
    while(monstre5.attribut!='Vent'):
        monstre5=ChauveSouris()
    while(monstre5.niveau!=3):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Chauve souris verte'

    monstre6=ChauveSouris()
    while(monstre6.attribut!='Feu'):
        monstre6=ChauveSouris()
    while(monstre6.niveau!=3):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Chauve souris rouge'

    Boss=ChauveSouris()
    while(Boss.attribut!='Feu'):
        Boss=ChauveSouris()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=4):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Chauve souris rouge géante'

    XP_recompense=734
    Recompense_liste=Recompenses_CratereAter(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def CratereAter_Niveau2():
    nom='le Cratère Ater Niveau 2 - Etage -2 '
    nom_famille='CratereAter'
    niveau=2
    attribut='Eau'

    monstre1=SoldatSquelette()
    while(monstre1.attribut!='Vent'):
        monstre1=SoldatSquelette()
    while(monstre1.niveau!=4):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Soldat squelette bleu 1'

    monstre2=SoldatSquelette()
    while(monstre2.attribut!='Eau'):
        monstre2=SoldatSquelette()
    while(monstre2.niveau!=4):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Soldat squelette bleu 2'

    demiBoss1=SoldatSquelette()
    while(demiBoss1.attribut!='Eau'):
        demiBoss1=SoldatSquelette()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=4):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Chef squelette bleu'

    monstre3=SoldatSquelette()
    while(monstre3.attribut!='Eau'):
        monstre3=SoldatSquelette()
    while(monstre3.niveau!=4):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Soldat squelette bleu'

    monstre4=SoldatSquelette()
    while(monstre4.attribut!='Vent'):
        monstre4=SoldatSquelette()
    while(monstre4.niveau!=4):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Soldat squelette vert'

    demiBoss2=SoldatSquelette()
    while(demiBoss2.attribut!='Vent'):
        demiBoss2=SoldatSquelette()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=4):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Chef squelette vert'

    monstre5=SoldatSquelette()
    while(monstre5.attribut!='Eau'):
        monstre5=SoldatSquelette()
    while(monstre5.niveau!=4):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Soldat squelette bleu'

    monstre6=SoldatSquelette()
    while(monstre6.attribut!='Vent'):
        monstre6=SoldatSquelette()
    while(monstre6.niveau!=4):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Soldat squelette vert'

    Boss=SoldatSquelette()
    while(Boss.attribut!='Eau'):
        Boss=SoldatSquelette()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=4):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Capitaine squelette bleu'

    XP_recompense=974
    Recompense_liste=Recompenses_CratereAter(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def CratereAter_Niveau3():
    nom='le CraterAter Niveau 3 - Etage -3 '
    nom_famille='CratereAter'
    niveau=3
    attribut='Vent'

    monstre1=ChauveSouris()
    while(monstre1.attribut!='Eau'):
        monstre1=ChauveSouris()
    while(monstre1.niveau!=4):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Chauve souris bleue'

    monstre2=SoldatSquelette()
    while(monstre2.attribut!='Eau'):
        monstre2=SoldatSquelette()
    while(monstre2.niveau!=4):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Soldat squelette bleu'

    demiBoss1=ChauveSouris()
    while(demiBoss1.attribut!='Eau'):
        demiBoss1=ChauveSouris()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=4):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grosse chauve souris bleue'

    monstre3=SoldatSquelette()
    while(monstre3.attribut!='Vent'):
        monstre3=SoldatSquelette()
    while(monstre3.niveau!=4):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Soldat squelette vert'

    monstre4=SoldatSquelette()
    while(monstre4.attribut!='Eau'):
        monstre4=SoldatSquelette()
    while(monstre4.niveau!=4):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Soldat squelette bleu'

    demiBoss2=Imp()
    while(demiBoss2.attribut!='Vent'):
        demiBoss2=Imp()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=4):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grand imp vert'

    monstre5=ChauveSouris()
    while(monstre5.attribut!='Vent'):
        monstre5=ChauveSouris()
    while(monstre5.niveau!=4):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Chauve souris verte'

    monstre6=ChauveSouris()
    while(monstre6.attribut!='Eau'):
        monstre6=ChauveSouris()
    while(monstre6.niveau!=4):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Chauve souris bleue'

    Boss=SoldatSquelette()
    while(Boss.attribut!='Vent'):
        Boss=SoldatSquelette()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=5):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Capitaine squelette vert'

    XP_recompense=978
    Recompense_liste=Recompenses_CratereAter(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def CratereAter_Niveau4():
    nom='le Cratère Ater Niveau 4 - Première caverne '
    nom_famille='CratereAter'
    niveau=4
    attribut='Eau'

    monstre1=Imp()
    while(monstre1.attribut!='Feu'):
        monstre1=Imp()
    while(monstre1.niveau!=5):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Imp rouge'

    monstre2=Imp()
    while(monstre2.attribut!='Eau'):
        monstre2=Imp()
    while(monstre2.niveau!=5):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Imp bleu'

    demiBoss1=Imp()
    while(demiBoss1.attribut!='Feu'):
        demiBoss1=Imp()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=5):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grand Imp rouge'

    monstre3=Imp()
    while(monstre3.attribut!='Eau'):
        monstre3=Imp()
    while(monstre3.niveau!=5):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Imp bleu'

    monstre4=Imp()
    while(monstre4.attribut!='Vent'):
        monstre4=Imp()
    while(monstre4.niveau!=5):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Imp vert'

    demiBoss2=Imp()
    while(demiBoss2.attribut!='Vent'):
        demiBoss2=Imp()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=5):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grand Imp vert'

    monstre5=Imp()
    while(monstre5.attribut!='Feu'):
        monstre5=Imp()
    while(monstre5.niveau!=5):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Imp rouge'

    monstre6=Imp()
    while(monstre6.attribut!='Vent'):
        monstre6=Imp()
    while(monstre6.niveau!=5):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Imp vert'

    Boss=Imp()
    while(Boss.attribut!='Eau'):
        Boss=Imp()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=5):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Imp bleu géant'

    XP_recompense=1143
    Recompense_liste=Recompenses_CratereAter(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def CratereAter_Niveau5():
    nom='le Cratère Ater Niveau 5 - Seconde caverne '
    nom_famille='CratereAter'
    niveau=5
    attribut='Ténèbres'

    monstre1=Imp()
    while(monstre1.attribut!='Ténèbres'):
        monstre1=Imp()
    while(monstre1.niveau!=6):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Imp noir'

    monstre2=Imp()
    while(monstre2.attribut!='Lumière'):
        monstre2=Imp()
    while(monstre2.niveau!=6):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Imp blanc'

    demiBoss1=Imp()
    while(demiBoss1.attribut!='Lumière'):
        demiBoss1=Imp()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=6):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grand Imp blanc'

    monstre3=Imp()
    while(monstre3.attribut!='Lumière'):
        monstre3=Imp()
    while(monstre3.niveau!=6):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Imp blanc'

    monstre4=Imp()
    while(monstre4.attribut!='Ténèbres'):
        monstre4=Imp()
    while(monstre4.niveau!=6):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Imp noir'

    demiBoss2=Imp()
    while(demiBoss2.attribut!='Ténèbres'):
        demiBoss2=Imp()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=6):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grand Imp noir'

    monstre5=Imp()
    while(monstre5.attribut!='Ténèbres'):
        monstre5=Imp()
    while(monstre5.niveau!=6):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Imp noir'

    monstre6=Imp()
    while(monstre6.attribut!='Lumière'):
        monstre6=Imp()
    while(monstre6.niveau!=6):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Imp blanc'

    Boss=Imp()
    while(Boss.attribut!='Lumière'):
        Boss=Imp()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=6):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Imp blanc géant'

    XP_recompense=1150
    Recompense_liste=Recompenses_CratereAter(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def CratereAter_Niveau6():
    nom='le Cratère Ater Niveau 6 - Passage Obscur '
    nom_famille='CratereAter'
    niveau=6
    attribut='Ténèbres'

    monstre1=Imp()
    while(monstre1.attribut!='Eau'):
        monstre1=Imp()
    while(monstre1.niveau!=7):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Imp bleu'

    monstre2=Imp()
    while(monstre2.attribut!='Ténèbres'):
        monstre2=Imp()
    while(monstre2.niveau!=7):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Imp noir'

    demiBoss1=Imp()
    while(demiBoss1.attribut!='Eau'):
        demiBoss1=Imp()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=7):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grand Imp bleu'

    monstre3=Imp()
    while(monstre3.attribut!='Feu'):
        monstre3=Imp()
    while(monstre3.niveau!=7):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Imp rouge'

    monstre4=Imp()
    while(monstre4.attribut!='Ténèbres'):
        monstre4=Imp()
    while(monstre4.niveau!=7):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Imp noir'

    demiBoss2=Imp()
    while(demiBoss2.attribut!='Feu'):
        demiBoss2=Imp()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=7):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grand Imp rouge'

    monstre5=Imp()
    while(monstre5.attribut!='Ténèbres'):
        monstre5=Imp()
    while(monstre5.niveau!=7):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Imp noir 1'

    monstre6=Imp()
    while(monstre6.attribut!='Ténèbres'):
        monstre6=Imp()
    while(monstre6.niveau!=7):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Imp noir 2'

    Boss=Imp()
    while(Boss.attribut!='Ténèbres'):
        Boss=Imp()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=8):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Imp noir géant'

    XP_recompense=1159
    Recompense_liste=Recompenses_CratereAter(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def CratereAter_Caverne():
    nom='le Cratère Ater Niveau 7 - Caverne des Profondeurs '
    nom_famille='CratereAter'
    niveau=7
    attribut='Ténèbres'

    monstre1=Imp()
    while(monstre1.attribut!='Vent'):
        monstre1=Imp()
    while(monstre1.niveau!=7):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Imp vert'

    monstre2=Imp()
    while(monstre2.attribut!='Ténèbres'):
        monstre2=Imp()
    while(monstre2.niveau!=7):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Imp noir'

    demiBoss1=Imp()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=Imp()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=7):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grand Imp vert'

    monstre3=Imp()
    while(monstre3.attribut!='Ténèbres'):
        monstre3=Imp()
    while(monstre3.niveau!=7):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Imp noir 1'

    monstre4=Imp()
    while(monstre4.attribut!='Ténèbres'):
        monstre4=Imp()
    while(monstre4.niveau!=7):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Imp noir 2'

    demiBoss2=Imp()
    while(demiBoss2.attribut!='Ténèbres'):
        demiBoss2=Imp()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=7):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grand Imp noir'

    monstre5=Imp()
    while(monstre5.attribut!='Ténèbres'):
        monstre5=Imp()
    while(monstre5.niveau!=7):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Imp noir 1'

    monstre6=Imp()
    while(monstre6.attribut!='Ténèbres'):
        monstre6=Imp()
    while(monstre6.niveau!=7):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Imp noir 2'

    Boss=Mastodonte()
    while(Boss.attribut!='Ténèbres'):
        Boss=Mastodonte()
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=8):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Mastodonte noir Royal'
    Boss.defense_max_donjons=2*Boss.defense_max_donjons
    Boss.defense=2*Boss.defense
    Boss.defense_actuelle=Boss.defense
    XP_recompense=827
    Recompense_liste=Recompenses_CratereAter(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def CratereAter():
    caracteristiques=[CratereAter_Niveau1(),CratereAter_Niveau2(),CratereAter_Niveau3(),CratereAter_Niveau4(),CratereAter_Niveau5(),CratereAter_Niveau6(),CratereAter_Caverne()]
    return caracteristiques

def Recompenses_CratereAter(niveau_donjon):
    ''' Rajouter le parchmin d invocation Mastodonte de Ténèbres '''
    recompenses_dispo=['Mana','Parchemin d invocation','Rune','Cristal','Parchemin d invocation superieure']
    chance_premiere_recompense=0.2
    chance_deuxieme_recompense=0.35
    chance_troisieme_recompense=0.35
    chance_cinquieme_recompense=0.05
    nombre_aleatoire=(random.randint(1,100))/100
    if(nombre_aleatoire<=chance_cinquieme_recompense):
        recompense_texte=recompenses_dispo[4]
    elif(nombre_aleatoire<=chance_premiere_recompense):
        recompense_texte=recompenses_dispo[0]
    elif(nombre_aleatoire<=chance_deuxieme_recompense):
        recompense_texte=recompenses_dispo[1]
    elif(nombre_aleatoire>(1-chance_troisieme_recompense)):
        recompense_texte=recompenses_dispo[2]
    else:
        recompense_texte=recompenses_dispo[3]
    if(recompense_texte=='Mana'):
        recompense=niveau_donjon*1000
    if(recompense_texte=='Cristal'):
        recompense=niveau_donjon
    if(recompense_texte=='Parchemin d invocation'):
        recompense=niveau_donjon
    if(recompense_texte=='Parchemin d invocation superieure'):
        recompense=1
    if(recompense_texte=='Rune'):
        ''' __init__(self,NOM,CATEGORIE,POSITION,QUALITE,RARETE,BONUS): '''
        categories_possibles=['HP+','HP%','ATK+','ATK%','DEF+','DEF%','VIT+','TCC%','DC%','ACC%','RES%']
        categorie_aleatoire=categories_possibles[(random.randint(0,10))]
        positions_possibles=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']
        if(niveau_donjon!=7):
            position=positions_possibles[niveau_donjon-1]
        else:
            position=positions_possibles[random.randint(0,5)]
        recompense=Runes('Rune Tenace I','Tenace',position,'I','Normale',categorie_aleatoire)
    return [recompense_texte,recompense]





def RuinesSenzargen_Niveau1():
    nom='les Ruines de Senzargen Niveau 1 - Portes'
    nom_famille='RuinesSenzargen'
    niveau=1
    attribut='Vent'

    monstre1=DameHarpie()
    while(monstre1.attribut!='Vent'):
        monstre1=DameHarpie()
    while(monstre1.niveau!=8):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Dame Harpie du Vent'

    monstre2=DameHarpie()
    while(monstre2.attribut!='Eau'):
        monstre2=DameHarpie()
    while(monstre2.niveau!=8):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Dame Harpie de l\'Eau'

    demiBoss1=DameHarpie()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=DameHarpie()
    while(demiBoss1.niveau!=8):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grande Dame Harpie du Vent'

    monstre3=DameHarpie()
    while(monstre3.attribut!='Vent'):
        monstre3=DameHarpie()
    while(monstre3.niveau!=8):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Dame Harpie du Vent'

    monstre4=DameHarpie()
    while(monstre4.attribut!='Eau'):
        monstre4=DameHarpie()
    while(monstre4.niveau!=8):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Dame Harpie de l\'Eau'

    demiBoss2=DameHarpie()
    while(demiBoss2.attribut!='Eau'):
        demiBoss2=DameHarpie()
    while(demiBoss2.niveau!=8):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grande Dame Harpie de l\'Eau'

    monstre5=DameHarpie()
    while(monstre5.attribut!='Vent'):
        monstre5=DameHarpie()
    while(monstre5.niveau!=8):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Dame Harpie du Vent'

    monstre6=DameHarpie()
    while(monstre6.attribut!='Eau'):
        monstre6=DameHarpie()
    while(monstre6.niveau!=8):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Dame Harpie de l\'Eau'

    Boss=DameHarpie()
    while(Boss.attribut!='Vent'):
        Boss=DameHarpie()
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=8):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Reine Dame Harpie du Vent'

    XP_recompense=1530
    Recompense_liste=Recompenses_RuinesSenzargen(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def RuinesSenzargen_Niveau2():
    nom='les Ruines de Senzargen Niveau 2 - Couloir '
    nom_famille='RuinesSenzargen'
    niveau=2
    attribut='Eau'

    monstre1=DameHarpie()
    while(monstre1.attribut!='Vent'):
        monstre1=DameHarpie()
    while(monstre1.niveau!=9):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Dame Harpie du Vent 1'

    monstre2=DameHarpie()
    while(monstre2.attribut!='Vent'):
        monstre2=DameHarpie()
    while(monstre2.niveau!=9):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Dame Harpie du Vent 2'

    demiBoss1=DameHarpie()
    while(demiBoss1.attribut!='Eau'):
        demiBoss1=DameHarpie()
    while(demiBoss1.niveau!=9):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grande Dame Harpie de l\'Eau'

    monstre3=DameHarpie()
    while(monstre3.attribut!='Eau'):
        monstre3=DameHarpie()
    while(monstre3.niveau!=9):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Dame Harpie de l\'Eau'

    monstre4=DameHarpie()
    while(monstre4.attribut!='Vent'):
        monstre4=DameHarpie()
    while(monstre4.niveau!=9):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Dame Harpie du Vent'

    demiBoss2=DameHarpie()
    while(demiBoss2.attribut!='Vent'):
        demiBoss2=DameHarpie()
    while(demiBoss2.niveau!=9):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grande Dame Harpie du Vent'

    monstre5=DameHarpie()
    while(monstre5.attribut!='Vent'):
        monstre5=DameHarpie()
    while(monstre5.niveau!=9):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Dame Harpie du Vent 1'

    monstre6=DameHarpie()
    while(monstre6.attribut!='Vent'):
        monstre6=DameHarpie()
    while(monstre6.niveau!=9):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Dame Harpie du Vent 2'

    Boss=DameHarpie()
    while(Boss.attribut!='Eau'):
        Boss=DameHarpie()
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=9):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Reine Dame Harpie de l\'Eau'

    XP_recompense=1548
    Recompense_liste=Recompenses_RuinesSenzargen(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def RuinesSenzargen_Niveau3():
    nom='les Ruines de Senzargen Niveau 3 - Escaliers '
    nom_famille='RuinesSenzargen'
    niveau=3
    attribut='Vent'

    monstre1=DameHarpie()
    while(monstre1.attribut!='Vent'):
        monstre1=DameHarpie()
    while(monstre1.niveau!=10):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Dame Harpie du Vent'

    monstre2=DameHarpie()
    while(monstre2.attribut!='Eau'):
        monstre2=DameHarpie()
    while(monstre2.niveau!=10):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Dame Harpie de l\'Eau'

    demiBoss1=DameHarpie()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=DameHarpie()
    while(demiBoss1.niveau!=10):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Grande Dame Harpie du Vent'

    monstre3=DameHarpie()
    while(monstre3.attribut!='Vent'):
        monstre3=DameHarpie()
    while(monstre3.niveau!=10):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Dame Harpie du Vent'

    monstre4=DameHarpie()
    while(monstre4.attribut!='Eau'):
        monstre4=DameHarpie()
    while(monstre4.niveau!=10):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Dame Harpie de l\'Eau'

    demiBoss2=DameHarpie()
    while(demiBoss2.attribut!='Eau'):
        demiBoss2=DameHarpie()
    while(demiBoss2.niveau!=10):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Grande Dame Harpie de l\'Eau'

    monstre5=DameHarpie()
    while(monstre5.attribut!='Vent'):
        monstre5=DameHarpie()
    while(monstre5.niveau!=10):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Dame Harpie du Vent'

    monstre6=DameHarpie()
    while(monstre6.attribut!='Eau'):
        monstre6=DameHarpie()
    while(monstre6.niveau!=10):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Dame Harpie de l\'Eau'

    Boss=DameHarpie()
    while(Boss.attribut!='Vent'):
        Boss=DameHarpie()
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=10):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Reine Dame Harpie du Vent'

    XP_recompense=1566
    Recompense_liste=Recompenses_RuinesSenzargen(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def RuinesSenzargen_Niveau4():
    nom='les Ruines de Senzargen Niveau 4 - Premier Autel '
    nom_famille='RuinesSenzargen'
    niveau=4
    attribut='Vent'

    monstre1=BasElementaire()
    while(monstre1.attribut!='Vent'):
        monstre1=BasElementaire()
    monstre1=Monstre.Evoluer(monstre1)
    monstre1=Monstre.Evoluer(monstre1)
    while(monstre1.niveau!=11):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Bas Elementaire Vent 1'

    monstre2=BasElementaire()
    while(monstre2.attribut!='Vent'):
        monstre2=BasElementaire()
    monstre2=Monstre.Evoluer(monstre2)
    monstre2=Monstre.Evoluer(monstre2)
    while(monstre2.niveau!=11):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Bas Elementaire Vent 2'

    demiBoss1=BasElementaire()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=BasElementaire()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=11):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Chef Bas Elementaire Vent'

    monstre3=BasElementaire()
    while(monstre3.attribut!='Vent'):
        monstre3=BasElementaire()
    monstre3=Monstre.Evoluer(monstre3)
    monstre3=Monstre.Evoluer(monstre3)
    while(monstre3.niveau!=11):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Bas Elementaire Vent 1'

    monstre4=BasElementaire()
    while(monstre4.attribut!='Vent'):
        monstre4=BasElementaire()
    monstre4=Monstre.Evoluer(monstre4)
    monstre4=Monstre.Evoluer(monstre4)
    while(monstre4.niveau!=11):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Bas Elementaire Vent 2'

    demiBoss2=BasElementaire()
    while(demiBoss2.attribut!='Vent'):
        demiBoss2=BasElementaire()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=11):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Chef Bas Elementaire Vent'

    monstre5=BasElementaire()
    while(monstre5.attribut!='Vent'):
        monstre5=BasElementaire()
    monstre5=Monstre.Evoluer(monstre5)
    monstre5=Monstre.Evoluer(monstre5)
    while(monstre5.niveau!=11):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Bas Elementaire Vent 1'

    monstre6=BasElementaire()
    while(monstre6.attribut!='Vent'):
        monstre6=BasElementaire()
    monstre6=Monstre.Evoluer(monstre6)
    monstre6=Monstre.Evoluer(monstre6)
    while(monstre6.niveau!=11):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Bas Elementaire Vent 2'

    Boss=BasElementaire()
    while(Boss.attribut!='Vent'):
        Boss=BasElementaire()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=11):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Capitaine Bas Elementaire Vent'

    XP_recompense=1593
    Recompense_liste=Recompenses_RuinesSenzargen(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def RuinesSenzargen_Niveau5():
    nom='les Ruines de Senzargen Niveau 5 - Second Autel '
    nom_famille='RuinesSenzargen'
    niveau=5
    attribut='Vent'

    monstre1=BasElementaire()
    while(monstre1.attribut!='Vent'):
        monstre1=BasElementaire()
    monstre1=Monstre.Evoluer(monstre1)
    monstre1=Monstre.Evoluer(monstre1)
    while(monstre1.niveau!=12):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Bas Elementaire Vent 1'

    monstre2=BasElementaire()
    while(monstre2.attribut!='Vent'):
        monstre2=BasElementaire()
    monstre2=Monstre.Evoluer(monstre2)
    monstre2=Monstre.Evoluer(monstre2)
    while(monstre2.niveau!=12):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Bas Elementaire Vent 2'

    demiBoss1=Elementaire()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=Elementaire()
    demiBoss1=Monstre.Evoluer(demiBoss1)
    demiBoss1=Monstre.Evoluer(demiBoss1)
    while(demiBoss1.niveau!=12):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Chef Elementaire Vent'

    monstre3=BasElementaire()
    while(monstre3.attribut!='Vent'):
        monstre3=BasElementaire()
    monstre3=Monstre.Evoluer(monstre3)
    monstre3=Monstre.Evoluer(monstre3)
    while(monstre3.niveau!=12):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Bas Elementaire Vent 1'

    monstre4=BasElementaire()
    while(monstre4.attribut!='Vent'):
        monstre4=BasElementaire()
    monstre4=Monstre.Evoluer(monstre4)
    monstre4=Monstre.Evoluer(monstre4)
    while(monstre4.niveau!=12):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Bas Elementaire Vent 2'

    demiBoss2=Elementaire()
    while(demiBoss2.attribut!='Vent'):
        demiBoss2=Elementaire()
    demiBoss2=Monstre.Evoluer(demiBoss2)
    demiBoss2=Monstre.Evoluer(demiBoss2)
    while(demiBoss2.niveau!=12):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Chef Elementaire Vent'

    monstre5=BasElementaire()
    while(monstre5.attribut!='Vent'):
        monstre5=BasElementaire()
    monstre5=Monstre.Evoluer(monstre5)
    monstre5=Monstre.Evoluer(monstre5)
    while(monstre5.niveau!=12):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Bas Elementaire Vent 1'

    monstre6=BasElementaire()
    while(monstre6.attribut!='Vent'):
        monstre6=BasElementaire()
    monstre6=Monstre.Evoluer(monstre6)
    monstre6=Monstre.Evoluer(monstre6)
    while(monstre6.niveau!=12):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Bas Elementaire Vent 2'

    Boss=Elementaire()
    while(Boss.attribut!='Vent'):
        Boss=Elementaire()
    Boss=Monstre.Evoluer(Boss)
    Boss=Monstre.Evoluer(Boss)
    while(Boss.niveau!=12):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Capitaine Elementaire Vent'

    XP_recompense=1605
    Recompense_liste=Recompenses_RuinesSenzargen(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def RuinesSenzargen_Niveau6():
    nom='les Ruines de Senzargen Niveau 6 - Profondeurs '
    nom_famille='RuinesSenzargen'
    niveau=6
    attribut='Vent'

    monstre1=Elementaire()
    while(monstre1.attribut!='Vent'):
        monstre1=Elementaire()
    while(monstre1.niveau!=12):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Elementaire Vent 1'

    monstre2=Elementaire()
    while(monstre2.attribut!='Vent'):
        monstre2=Elementaire()
    while(monstre2.niveau!=12):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Elementaire Vent 2'

    demiBoss1=HautElementaire()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=HautElementaire()
    while(demiBoss1.niveau!=12):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Chef Haut Elementaire Vent'

    monstre3=Elementaire()
    while(monstre3.attribut!='Vent'):
        monstre3=Elementaire()
    while(monstre3.niveau!=12):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Elementaire Vent 1'

    monstre4=Elementaire()
    while(monstre4.attribut!='Vent'):
        monstre4=Elementaire()
    while(monstre4.niveau!=12):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Elementaire Vent 2'

    demiBoss2=HautElementaire()
    while(demiBoss2.attribut!='Vent'):
        demiBoss2=HautElementaire()
    while(demiBoss2.niveau!=12):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Chef Haut Elementaire Vent'

    monstre5=HautElementaire()
    while(monstre5.attribut!='Vent'):
        monstre5=HautElementaire()
    while(monstre5.niveau!=12):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Haut Elementaire Vent'

    monstre6=Elementaire()
    while(monstre6.attribut!='Vent'):
        monstre6=BasElementaire()
    while(monstre6.niveau!=12):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Elementaire Vent'

    Boss=HautElementaire()
    while(Boss.attribut!='Vent'):
        Boss=HautElementaire()
    while(Boss.niveau!=13):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Capitaine Haut Elementaire Vent'

    XP_recompense=1617
    Recompense_liste=Recompenses_RuinesSenzargen(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def RuinesSenzargen_Autel():
    nom='les Ruines de Senzargen Niveau 7 - Autel Sacrificiel '
    nom_famille='RuinesSenzargen'
    niveau=7
    attribut='Vent'

    monstre1=HautElementaire()
    while(monstre1.attribut!='Vent'):
        monstre1=HautElementaire()
    while(monstre1.niveau!=13):
        monstre1=Donjon.Monter_en_niveau_sans_affichage(monstre1)
    monstre1.surnom='Haut Elementaire Vent 1'

    monstre2=HautElementaire()
    while(monstre2.attribut!='Vent'):
        monstre2=HautElementaire()
    while(monstre2.niveau!=13):
        monstre2=Donjon.Monter_en_niveau_sans_affichage(monstre2)
    monstre2.surnom='Haut Elementaire Vent 2'

    demiBoss1=HautElementaire()
    while(demiBoss1.attribut!='Vent'):
        demiBoss1=HautElementaire()
    while(demiBoss1.niveau!=13):
        demiBoss1=Donjon.Monter_en_niveau_sans_affichage(demiBoss1)
    demiBoss1.surnom='Chef Haut Elementaire Vent'

    monstre3=HautElementaire()
    while(monstre3.attribut!='Vent'):
        monstre3=HautElementaire()
    while(monstre3.niveau!=13):
        monstre3=Donjon.Monter_en_niveau_sans_affichage(monstre3)
    monstre3.surnom='Haut Elementaire Vent 1'

    monstre4=HautElementaire()
    while(monstre4.attribut!='Vent'):
        monstre4=HautElementaire()
    while(monstre4.niveau!=13):
        monstre4=Donjon.Monter_en_niveau_sans_affichage(monstre4)
    monstre4.surnom='Haut Elementaire Vent 2'

    demiBoss2=HautElementaire()
    while(demiBoss2.attribut!='Vent'):
        demiBoss2=HautElementaire()
    while(demiBoss2.niveau!=13):
        demiBoss2=Donjon.Monter_en_niveau_sans_affichage(demiBoss2)
    demiBoss2.surnom='Chef Haut Elementaire Vent'

    monstre5=HautElementaire()
    while(monstre5.attribut!='Vent'):
        monstre5=HautElementaire()
    while(monstre5.niveau!=13):
        monstre5=Donjon.Monter_en_niveau_sans_affichage(monstre5)
    monstre5.surnom='Haut Elementaire Vent'

    monstre6=Sylphe()
    while(monstre6.attribut!='Vent'):
        monstre6=Sylphe()
    while(monstre6.niveau!=14):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Arashi la Tempête'

    Boss=Sylphide()
    while(Boss.attribut!='Vent'):
        Boss=Sylphide()
    while(Boss.niveau!=14):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Hayate le Bourrasque'

    '''
    monstre6=Hayate()
    while(monstre6.attribut!='Vent'):
        monstre6=Hayate()
    while(monstre6.niveau!=14):
        monstre6=Donjon.Monter_en_niveau_sans_affichage(monstre6)
    monstre6.surnom='Hayate la Bourrasque Spirituelle'

    Boss=Arashi()
    while(Boss.attribut!='Vent'):
        Boss=Arashi()
    while(Boss.niveau!=14):
        Boss=Donjon.Monter_en_niveau_sans_affichage(Boss)
    Boss.surnom='Arashi la Tempête Divine'
    '''

    XP_recompense=1454
    Recompense_liste=Recompenses_RuinesSenzargen(niveau)
    recompense=[XP_recompense,Recompense_liste]
    caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demiBoss1,demiBoss2,Boss,recompense,nom_famille]
    return caracteristiques


def RuinesSenzargen():
    caracteristiques=[RuinesSenzargen_Niveau1(),RuinesSenzargen_Niveau2(),RuinesSenzargen_Niveau3(),RuinesSenzargen_Niveau4(),RuinesSenzargen_Niveau5(),RuinesSenzargen_Niveau6(),RuinesSenzargen_Autel()]
    return caracteristiques

def Recompenses_RuinesSenzargen(niveau_donjon):
    ''' Boss pas encore créés... Parchemins non plus XD '''
    recompenses_dispo=['Mana','Parchemin d invocation','Rune','Cristal','Parchemin d invocation superieure']
    chance_premiere_recompense=0.2
    chance_deuxieme_recompense=0.35
    chance_troisieme_recompense=0.35
    chance_cinquieme_recompense=0.05
    nombre_aleatoire=(random.randint(1,100))/100
    if(nombre_aleatoire<=chance_cinquieme_recompense):
        recompense_texte=recompenses_dispo[4]
    elif(nombre_aleatoire<=chance_premiere_recompense):
        recompense_texte=recompenses_dispo[0]
    elif(nombre_aleatoire<=chance_deuxieme_recompense):
        recompense_texte=recompenses_dispo[1]
    elif(nombre_aleatoire>(1-chance_troisieme_recompense)):
        recompense_texte=recompenses_dispo[2]
    else:
        recompense_texte=recompenses_dispo[3]
    if(recompense_texte=='Mana'):
        recompense=niveau_donjon*1000
    if(recompense_texte=='Cristal'):
        recompense=niveau_donjon
    if(recompense_texte=='Parchemin d invocation'):
        recompense=niveau_donjon
    if(recompense_texte=='Parchemin d invocation superieure'):
        recompense=1
    if(recompense_texte=='Rune'):
        ''' __init__(self,NOM,CATEGORIE,POSITION,QUALITE,RARETE,BONUS): '''
        categories_possibles=['HP+','HP%','ATK+','ATK%','DEF+','DEF%','VIT+','TCC%','DC%','ACC%','RES%']
        categorie_aleatoire=categories_possibles[(random.randint(0,10))]
        positions_possibles=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']
        if(niveau_donjon!=7):
            position=positions_possibles[niveau_donjon-1]
        else:
            position=positions_possibles[random.randint(0,5)]
        recompense=Runes('Rune Tenace I','Tenace',position,'I','Normale',categorie_aleatoire)
    return [recompense_texte,recompense]
