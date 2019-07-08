# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:41:34 2019

@author: marin
"""

''' if need help : https://programmation360.com/programmation-orientee-objet-python/ '''
# SUBLIME TEXT VACHEMENT TROP BIEN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Sauf pour la tabulation de m****...
# doctest à chercher!!!!!

import sys
import random
import math
from ast import literal_eval



class equipe(Monstre):
    def __init__(MONSTRE1,MONSTRE2,MONSTRE3):
        team=[MONSTRE1,MONSTRE2,MONSTRE3]
        return team

    def afficher(Team):
        print(' Leader : ')
        print(Monstre.__str__(Team[0]))
        if((len(Team)>1) and (Team[1]!=0)):
            print(' Membre 1 : ')
            print(Monstre.__str__(Team[1]))
        if((len(Team)>2) and (Team[2]!=0)):
            print(' Membre 2 : ')
            print(Monstre.__str__(Team[2]))

    def afficherPartiellement(Team):
        print('Leader : ',Team[0].surnom,'(',Team[0].nom,' de ',Team[0].attribut,Team[0].classe,' étoiles)')
        if((len(Team)>1) and (Team[1]!=0)):
            print('Membre 1 : ',Team[1].surnom,'(',Team[1].nom,' de ',Team[1].attribut,Team[1].classe,' étoiles)')
        else:
            print('Emplacement 1 de l\'équipe : libre')
        if((len(Team)>2) and (Team[2]!=0)):
            print('Membre 2 : ',Team[2].surnom,'(',Team[2].nom,' de ',Team[2].attribut,Team[2].classe,' étoiles)\n')
        else:
            print('Emplacement 2 de l\'équipe : libre\n')

    def Modifier(base,Team):
        print('L équipe actuelle  est : ')
        equipe.afficherPartiellement(Team)
        possibilites_modifier=[0]
        print('\n\n',Team[0],' = 0')
        if((len(Team)>1) and (Team[1]!=0)):
            print('\n',Team[1],' = 1 \n')
            possibilites_modifier.append(1)
        else:
            Team.append(0)
            print('\nEmplacement 1 = 1 \n')
            possibilites_modifier.append(1)
        if((len(Team)>2) and (Team[2]!=0)):
            print('\n',Team[2],' = 2 \n')
            possibilites_modifier.append(2)
        else:
            Team.append(0)
            print('\nEmplacement 2 = 2 \n')
            possibilites_modifier.append(2)
        entree=input('Quel monstre voulez-vous remplacer ? ')
        while(not IsSecure(entree)):
            entree=input('Quel monstre voulez-vous remplacer ? ')
        place_monstre_a_retirer=int(entree)
        while(place_monstre_a_retirer not in possibilites_modifier):
            entree=input('Oui = 0 \nNon = 1 \nQuel monstre voulez-vous remplacer ? ')
            while(not IsSecure(entree)):
                entree=input('Oui = 0 \nNon = 1 \nQuel monstre voulez-vous remplacer ? ')
            place_monstre_a_retirer=int(entree)
        print('\n\n')
        print('Ne remplacer ce monstre par personne = ',0,'\n')
        possibilites=[0]
        i=1
        while(i<=base.place_dernier_monstre):
            if(base.stockage[i]!=Team[0]):
                if((len(Team)>1) and (base.stockage[i]!=Team[1])):
                    if((len(Team)>2) and (base.stockage[i]!=Team[2])):
                        print(base.stockage[i],' = ',i,'\n')
                        possibilites.append(i)
            i+=1
        entree=input('Par quel monstre voulez-vous le remplacer ? ')
        while(not IsSecure(entree)):
            entree=input('Par quel monstre voulez-vous le remplacer ? ')
        place_monstre_remplacant=int(entree)
        while(place_monstre_remplacant not in possibilites):
            entree=input('Par quel monstre voulez-vous le remplacer ? ')
            while(not IsSecure(entree)):
                entree=input('Par quel monstre voulez-vous le remplacer ? ')
            place_monstre_remplacant=int(entree)
        if(place_monstre_remplacant!=0):
            Team[place_monstre_a_retirer]=base.stockage[place_monstre_remplacant]
        else:
            Team=equipe.Supprimer_monstre_equipe(Team,place_monstre_a_retirer)
        print('\nL\'équipe est désormais : \n')
        equipe.afficherPartiellement(Team)
        return Team

    def Ajouter(base,Team):
        if(not (0 in Team)):
            print('L\'équipe est déjà au complet!! \n\n')
        else:
            print('L équipe actuelle  est : ')
            equipe.afficherPartiellement(Team)
            entree=input('Oui = 0 \nNon = 1 \nVoulez-vous y ajouter un monstre ? ')
            while(not IsSecure(entree)):
                entree=input('Oui = 0 \nNon = 1 \nVoulez-vous y ajouter un monstre ? ')
            choix=int(entree)
            while(choix!=0 and choix!=1):
                entree=input('Oui = 0 \nNon = 1 \nVoulez-vous y ajouter un monstre ? ')
                while(not IsSecure(entree)):
                    entree=input('Oui = 0 \nNon = 1 \nVoulez-vous y ajouter un monstre ? ')
                choix=int(entree)
            if(choix==0):
                possibilites_emplacement=[]
                if((len(Team)>1) and (Team[1])==0):
                    print('\n Emplacement 1 = 1 \n')
                    possibilites_emplacement.append(1)
                if((len(Team)>2) and (Team[2]==0)):
                    print('\n Emplacement 2 = 2 \n')
                    possibilites_emplacement.append(2)
                entree=input('A quel emplacement voulez-vous ajouter un monstre ? ')
                while(not IsSecure(entree)):
                    entree=input('A quel emplacement voulez-vous ajouter un monstre ? ')
                place_monstre_a_ajouter=int(entree)
                while(place_monstre_a_ajouter not in possibilites_emplacement):
                    entree=input('A quel emplacement voulez-vous ajouter un monstre ? ')
                    while(not IsSecure(entree)):
                        entree=input('A quel emplacement voulez-vous ajouter un monstre ? ')
                    place_monstre_a_ajouter=int(entree)
                print('\n\n')
                print('Annuler et ne pas remplacer de monstre = ',0)
                possibilites=[0]
                i=1
                while(i<=base.place_dernier_monstre):
                    if(base.stockage[i]!=Team[0]):
                        if((len(Team)>1) and (base.stockage[i]!=Team[1])):
                            if((len(Team)>2) and (base.stockage[i]!=Team[2])):
                                print(base.stockage[i],' = ',i,'\n')
                                possibilites.append(i)
                    i+=1
                entree=input('Par quel monstre voulez-vous le remplacer ? ')
                while(not IsSecure(entree)):
                    entree=input('Par quel monstre voulez-vous le remplacer ? ')
                place_monstre_remplacant=int(entree)
                while(place_monstre_remplacant not in possibilites):
                    entree=input('Par quel monstre voulez-vous le remplacer ? ')
                    while(not IsSecure(entree)):
                        entree=input('Par quel monstre voulez-vous le remplacer ? ')
                    place_monstre_remplacant=int(entree)
                if(place_monstre_remplacant!=0):
                    Team[place_monstre_a_ajouter]=base.stockage[place_monstre_remplacant]
        print('\nL\'équipe est désormais : \n')
        equipe.afficherPartiellement(Team)
        return Team

    def Supprimer_monstre_equipe(Team,indice):
        if(len(Team)==3):
            if(indice==0):
                Team_tmp=[Team[1],Team[2],0]
            elif(indice==1):
                Team_tmp=[Team[0],Team[2],0]
            else:
                Team_tmp=[Team[0],Team[1],0]
        elif(len(Team)==2):
            if(indice==0):
                Team_tmp=[Team[1],0,0]
            elif(indice==1):
                Team_tmp=[Team[0],0,0]
        else:
            if(indice==0):
                Team_tmp=Team
        Team=Team_tmp
        return Team

    def Modifier_alignement_equipe(Team):
        print('Leader : ',Team[0].surnom,' de ',Team[0].attribut,Team[0].classe,' étoiles  = 0')
        if((len(Team)>1) and (Team[1]!=0)):
            print('Membre 1 : ',Team[1].surnom,' de ',Team[1].attribut,Team[1].classe,' étoiles  = 1')
        if((len(Team)>2) and (Team[2]!=0)):
            print('Membre 2 : ',Team[2].surnom,' de ',Team[2].attribut,Team[2].classe,' étoiles  = 2 \n\n')

        if(len(Team)==0):
            print('L equipe est vide!!')
        if(len(Team)==1):
            print('Votre équipe ne comporte qu un seul monstre. Impossible de changer son alignement!!')
        else:
            if(len(Team)==2):
                Team_tmp=[Team[1],Team[0]]
                Team=Team_tmp
            else:
                entree=input('\nQuel est le premier monstre que vous voulez permuter ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQuel est le premier monstre que vous voulez permuter ? ')
                choix1=int(entree)
                while(choix1!=0 and choix1!=1 and choix1!=2):
                    entree=input('\nQuel est le premier monstre que vous voulez permuter ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nQuel est le premier monstre que vous voulez permuter ? ')
                    choix1=int(entree)
                entree=input('\nAvec quel monstre voulez-vous le permuter ? ')
                while(not IsSecure(entree)):
                    entree=input('\nAvec quel monstre voulez-vous le permuter ? ')
                choix2=int(entree)
                while(choix2!=0 and choix2!=1 and choix2!=2):
                    entree=input('\nAvec quel monstre voulez-vous le permuter ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nAvec quel monstre voulez-vous le permuter ? ')
                    choix2=int(entree)
                if(choix1==0):
                    if(choix2==1):
                        Team_tmp=[Team[1],Team[0],Team[2]]
                    elif(choix2==2):
                        Team_tmp=[Team[2],Team[1],Team[0]]
                    else:
                        Team_tmp=Team
                elif(choix1==1):
                    if(choix2==0):
                        Team_tmp=[Team[1],Team[0],Team[2]]
                    elif(choix2==2):
                        Team_tmp=[Team[0],Team[2],Team[1]]
                    else:
                        Team_tmp=Team
                elif(choix1==2):
                    if(choix2==0):
                        Team_tmp=[Team[2],Team[1],Team[0]]
                    elif(choix2==1):
                        Team_tmp=[Team[0],Team[1],Team[2]]
                    else:
                        Team_tmp=Team
                Team=Team_tmp
        return Team





class Inventaire:
    def __init__(self):
        self.equipement=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.equipement[0]='Quitter'
        self.place_dernier_equipement=0
        self.objets_courants=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.objets_courants[0]='Quitter'
        self.place_dernier_objet_courant=0
        self.mana=0
        self.cristaux=0
        self.pierres_de_fusion=0

    def estFull(sac,zone):
        if(zone=='equipement'):
            if(sac.place_dernier_equipement==99):
                full=True
            else:
                full=False
        else:
            if(zone=='objets_courants'):
                if(sac.place_dernier_objet_courant==99):
                    full=True
                else:
                    full=False
        return full

    def ajouter_objet(sac,objet):
        if(objet.type=='Rune'):
            if (Inventaire.estFull(sac,'equipement')==False):
                sac.equipement[sac.place_dernier_equipement+1]=objet
                sac.place_dernier_equipement+=1
            else:
                print('Dommage!! La partie runes du sac est pleine... \n')

        elif(objet.type=='Objet_courant'):
            if (Inventaire.estFull(sac,'objets_courants')==False):
                sac.objets_courants[sac.place_dernier_objet_courant+1]=objet
                sac.place_dernier_objet_courant+=1
            else:
                print('Dommage!! La partie objets courants du sac est pleine... \n')
        else:
            print('\n Vous ne devriez pas toucher à cet objet... \n ')


    def AfficherArgent(sac):
        print('\n Vous avez actuellement ',sac.mana,'pierres de mana.')
        print('Vous avez actuellement ',sac.cristaux,'cristaux.')
        print('Vous avez actuellement ',sac.pierres_de_fusion,'pierres de fusion. \n')

    # Jamais utilisee, plutot regarder section
    def Afficher_contenu_sac_entier(sac):
        print('0 = afficher les runes ')
        print('1 = afficher les objets courants \n')
        entree=input('Que voulez-vous afficher ? ')
        while(not IsSecure(entree)):
            entree=input('Que voulez-vous afficher ? ')
        choix=int(entree)
        while(choix!=0 and choix!=1):
            entree=input('Que voulez-vous afficher ? ')
            while(not IsSecure(entree)):
                entree=input('Que voulez-vous afficher ? ')
            choix=int(entree)
        end_equipement=sac.place_dernier_equipement
        end_objets_courants=sac.place_dernier_objet_courant
        if (choix==0):
            for i in range(end_equipement):
                print('Vous avez la rune : ',sac.equipement[i+1],' à l emplacement ',i+1,'\n')
        if (choix==1):
            for i in range(end_objets_courants):
                print('Vous avez l objet : ',sac.objets_courants[i+1],' à l emplacement',i+1,'\n')
        print('\n')

    def Afficher_contenu_sac_section(sac,section):
        if (section=='equipement'):
            for i in range(1,sac.place_dernier_equipement+1):
                print('Vous avez la rune : ',sac.equipement[i],' à l emplacement ',i)
            if(sac.place_dernier_equipement==0):
                print('Vous ne transportez aucune rune pour le moment.')
        if (section=='objets_courants'):
            for i in range(1,sac.place_dernier_objet_courant+1):
                print('Vous avez l objet : ',(sac.objets_courants[i]).nom,' à l emplacement',i,'\n')
            if(sac.place_dernier_objet_courant==0):
                print('Vous ne transportez aucun parchemin pour le moment.')
        print('\n')


    def Afficher_contenu_sac_zone_unique(sac,zone,indice):
        if (zone=='equipement'):
            if (indice>0 and indice<=sac.place_dernier_equipement):
                print('Vous avez la rune : ',sac.equipement[indice],'à l emplacement ',indice)
            else:
                print('Vous n avez aucune rune à cet emplacement du sac.')
        else:
            if(zone=='objets_courants'):
                if (indice>0 and indice<=sac.place_dernier_objet_courant):
                    print('Vous avez l objet : ',sac.objets_courants[indice].nom,'à l emplacement ',indice)
                    print('Il vous coûterait ',sac.objets_courants[indice].prix_d_utilisation,'pierres de mana pour l utiliser.')
                else:
                    print('Vous n avez aucun objet à cet emplacement du sac.')
        print('\n')


    ''' Traiter le cas où la rune est équipée à un monstre!!! '''
    def supprimer_objet(sac,zone):
        possibilites_suppression_parchemin=[]
        possibilites_suppression_rune=[]
        if (zone=='equipement'):
            m=1
            while(m<=sac.place_dernier_equipement):
                Inventaire.Afficher_contenu_sac_zone_unique(sac,zone,m)
                possibilites_suppression_rune.append(m)
                m+=1
            if(len(possibilites_suppression_rune)==0):
                print('Vous n avez aucune rune à jeter.')
            else:
                entree=input('\nQuelle rune voulez-vous jeter ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQuelle rune voulez-vous jeter ? ')
                indice=int(entree)
                while(indice not in possibilites_suppression_rune):
                    indice=input('\nQuelle rune voulez-vous jeter ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nQuelle rune voulez-vous jeter ? ')
                    indice=int(entree)
                if (indice>0 and indice<=sac.place_dernier_equipement):
                    print('Êtes vous sûr(e) de vouloir jeter la rune ',sac.equipement[indice].nom,' ? \n')
                    entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    while(not IsSecure(entree)):
                        entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    choix=int(entree)
                    while(choix!=0 and choix!=1):
                        entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                        while(not IsSecure(entree)):
                            entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                        choix=int(entree)
                    if (choix==0):
                        print('La rune ',sac.equipement[indice].nom,' a bien été jetée. \n')
                        sac.equipement[indice]=0
                        for i in range(indice,sac.place_dernier_equipement-1):
                            sac.equipement[i]=sac.equipement[i+1]
                        sac.equipement[sac.place_dernier_equipement]=0
                        sac.place_dernier_equipement-=1
                else:
                    print('Vous n avez aucune rune à cet emplacement du sac.')
        else:
            if(zone=='objets_courants'):
                n=1
                while(n<=sac.place_dernier_objet_courant):
                    Inventaire.Afficher_contenu_sac_zone_unique(sac,zone,n)
                    possibilites_suppression_parchemin.append(n)
                    n+=1
                if(len(possibilites_suppression_parchemin)==0):
                    print('Vous n avez aucun parchemin à jeter.')
                else:
                    entree=input('\nQuel parchemin voulez-vous jeter ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nQuel parchemin voulez-vous jeter ? ')
                    indice=int(entree)
                    while(indice not in possibilites_suppression_parchemin):
                        entree=input('\nQuel parchemin voulez-vous jeter ? ')
                        while(not IsSecure(entree)):
                            entree=input('\nQuel parchemin voulez-vous jeter ? ')
                        indice=int(entree)
                    if (indice>0 and indice<=sac.place_dernier_objet_courant):
                        print('Êtes vous sûr(e) de vouloir jeter l objet ',sac.objets_courants[indice].nom,' ? \n')
                        entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                        while(not IsSecure(entree)):
                            entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                        choix=int(entree)
                        while(choix!=0 and choix!=1):
                            entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                            while(not IsSecure(entree)):
                                entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                            choix=int(entree)
                        if (choix==0):
                            print('L objet ',sac.objets_courants[indice].nom,' a bien été jeté. \n')
                            sac.objets_courants[indice]=0
                            for i in range(indice,sac.place_dernier_objet_courant-1):
                                sac.objets_courants[i]=sac.objets_courants[i+1]
                            sac.objets_courants[sac.place_dernier_objet_courant]=0
                            sac.place_dernier_objet_courant-=1
                    else:
                        print('Vous n avez aucun objet à cet emplacement du sac.')
        print('\n')


    def supprimer_objet_courant_sans_affichage(sac,indice):
        if (indice>0 and indice<=sac.place_dernier_objet_courant):
            for i in range(indice,sac.place_dernier_objet_courant):
                sac.objets_courants[i]=sac.objets_courants[i+1]
            sac.objets_courants[sac.place_dernier_objet_courant]=0
            sac.place_dernier_objet_courant-=1
        else:
            print('Vous n avez aucun objet à cet emplacement du sac.')
        print('\n\n')
        return sac

    def supprimer_equipement_sans_affichage(sac,indice):
        if (indice>0 and indice<=sac.place_dernier_equipement):
            for i in range(indice,sac.place_dernier_equipement):
                sac.equipement[i]=sac.equipement[i+1]
            sac.equipement[sac.place_dernier_equipement]=0
            sac.place_dernier_equipement-=1
        else:
            print('Vous n avez aucun objet à cet emplacement du sac.')
        print('\n\n')
        return sac


    ''' Produits à refaire '''
    def magasin(base,sac):
        print('\nBienvenu au magasin Chirino!!')
        print('Vous pouvez choisir parmi les options suivantes : ')
        print('Acheter des parchemins = 0')
        print('Acheter des runes = 1')
        print('Vendre un objet = 2')
        print('Revenir au menu principal = 3')
        entree=input('\n Que voulez-vous faire ? ')
        while(not IsSecure(entree)):
            entree=input('\n Que voulez-vous faire ? ')
        choix_magasin=int(entree)
        while(choix_magasin!=0 and choix_magasin!=1 and choix_magasin!=2 and choix_magasin!=3):
            entree=input('\n Que voulez-vous faire ? ')
            while(not IsSecure(entree)):
                entree=input('\n Que voulez-vous faire ? ')
            choix_magasin=int(entree)

        if(choix_magasin==0):
            print('Voici la liste des parchemins disponibles : ')
            Parchemin_d_invocation=Objets('Parchemin d invocation')
            Parchemin_d_invocation_superieure=Objets('Parchemin d invocation superieure')
            Parchemin_d_invocation_ultra_superieure=Objets('Parchemin d invocation ultra superieure')
            print('Ne rien acheter = 0')
            print('Parchemin d invocation (1 à 3 étoiles)  :  Prix d achat : ',Parchemin_d_invocation.prix_d_achat,'  = 1')
            print('Parchemin d invocation superieure (3 à 5 étoiles)  :  Prix d achat : ',Parchemin_d_invocation_superieure.prix_d_achat,'  = 2')
            print('Parchemin d invocation ultra superieure (3 à 5 étoiles) : Prix d achat : ',Parchemin_d_invocation_ultra_superieure.prix_d_achat,'  = 3')
            entree=input('\nQue voulez-vous acheter ? ')
            while(not IsSecure(entree)):
                entree=input('\nQue voulez-vous acheter ? ')
            parchemin_a_acheter=int(entree)
            while(parchemin_a_acheter!=0 and parchemin_a_acheter!=1 and parchemin_a_acheter!=2 and parchemin_a_acheter!=3):
                entree=input('\nQue voulez-vous acheter ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQue voulez-vous acheter ? ')
                parchemin_a_acheter=int(entree)
            if(parchemin_a_acheter==0):
                Inventaire.magasin(base,sac)
            if(parchemin_a_acheter==1):
                Inventaire.acheter_objet(base,sac,Parchemin_d_invocation)
            if(parchemin_a_acheter==2):
                Inventaire.acheter_objet(base,sac,Parchemin_d_invocation_superieure)
            if(parchemin_a_acheter==3):
                Inventaire.acheter_objet(base,sac,Parchemin_d_invocation_ultra_superieure)

        if(choix_magasin==1):
            print('Voici la liste des catégories runes disponibles : ')
            print('Ne rien acheter = 0')
            print('Energie (catégorie Energie) = 1')
            print('Altruisme (catégorie Energie) = 2')
            print('Colère (Catégorie Colere) = 3')
            print('Haine (Catégorie Colere) = 4')
            print('Tenace (Catégorie Tenace) = 5')
            print('Gardien (Catégorie Tenace) = 6')
            print('Véloce (Catégorie Veloce) = 7')
            print('Lame (Catégorie Lame) = 8')
            print('Rage (Catégorie Rage) = 9')
            print('Sniper (Catégorie Precision) = 10')
            print('Illumination (Catégorie Résistance) = 11')
            possibilites_categorie_rune_a_acheter=[0,1,2,3,4,5,6,7,8,9,10,11]
            entree=input('\nQuelle est la catégorie de la rune que vous voulez acheter ? ')
            while(not IsSecure(entree)):
                entree=input('\nQuelle est la catégorie de la rune que vous voulez acheter ? ')
            choix_categorie_rune_a_acheter=int(entree)
            while(choix_categorie_rune_a_acheter not in possibilites_categorie_rune_a_acheter):
                entree=input('\nQuelle est la catégorie de la rune que vous voulez acheter ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQuelle est la catégorie de la rune que vous voulez acheter ? ')
                choix_categorie_rune_a_acheter=int(entree)

            ''' Runes.__init__(self,NOM,CATEGORIE,POSITION,QUALITE,RARETE,BONUS) '''
            ''' MODIFIER LES PRIX D ACHATS!!!!!! '''
            Rune_Energie_I_haut=Runes('Rune Energie I','Energie','rune_haut','I','Normale','HP+')
            Rune_Energie_I_haut_droite=Runes('Rune Energie I','Energie','rune_haut_droite','I','Normale','HP+')
            Rune_Energie_I_bas_droite=Runes('Rune Energie I','Energie','rune_bas_droite','I','Normale','HP+')
            Rune_Energie_I_bas=Runes('Rune Energie I','Energie','rune_bas','I','Normale','HP+')
            Rune_Energie_I_bas_gauche=Runes('Rune Energie I','Energie','rune_bas_gauche','I','Normale','HP+')
            Rune_Energie_I_haut_gauche=Runes('Rune Energie I','Energie','rune_haut_gauche','I','Normale','HP+')
            Rune_Energie_I=[Rune_Energie_I_haut,Rune_Energie_I_haut_droite,Rune_Energie_I_bas_droite,Rune_Energie_I_bas,Rune_Energie_I_bas_gauche,Rune_Energie_I_haut_gauche]

            Rune_Altruisme_I_haut=Runes('Rune Altruisme I','Energie','rune_haut','I','Normale','HP%')
            Rune_Altruisme_I_haut_droite=Runes('Rune Altruisme I','Energie','rune_haut_droite','I','Normale','HP%')
            Rune_Altruisme_I_bas_droite=Runes('Rune Altruisme I','Energie','rune_bas_droite','I','Normale','HP%')
            Rune_Altruisme_I_bas=Runes('Rune Altruisme I','Energie','rune_bas','I','Normale','HP%')
            Rune_Altruisme_I_bas_gauche=Runes('Rune Altruisme I','Energie','rune_bas_gauche','I','Normale','HP%')
            Rune_Altruisme_I_haut_gauche=Runes('Rune Altruisme I','Energie','rune_haut_gauche','I','Normale','HP%')
            Rune_Altruisme_I=[Rune_Altruisme_I_haut,Rune_Altruisme_I_haut_droite,Rune_Altruisme_I_bas_droite,Rune_Altruisme_I_bas,Rune_Altruisme_I_bas_gauche,Rune_Altruisme_I_haut_gauche]

            Rune_Colere_I_haut=Runes('Rune Colere I','Colere','rune_haut','I','Normale','ATK+')
            Rune_Colere_I_haut_droite=Runes('Rune Colere I','Colere','rune_haut_droite','I','Normale','ATK+')
            Rune_Colere_I_bas_droite=Runes('Rune Colere I','Colere','rune_bas_droite','I','Normale','ATK+')
            Rune_Colere_I_bas=Runes('Rune Colere I','Colere','rune_bas','I','Normale','ATK+')
            Rune_Colere_I_bas_gauche=Runes('Rune Colere I','Colere','rune_bas_gauche','I','Normale','ATK+')
            Rune_Colere_I_haut_gauche=Runes('Rune Colere I','Colere','rune_haut_gauche','I','Normale','ATK+')
            Rune_Colere_I=[Rune_Colere_I_haut,Rune_Colere_I_haut_droite,Rune_Colere_I_bas_droite,Rune_Colere_I_bas,Rune_Colere_I_bas_gauche,Rune_Colere_I_haut_gauche]

            Rune_Haine_I_haut=Runes('Rune Haine I','Colere','rune_haut','I','Normale','ATK%')
            Rune_Haine_I_haut_droite=Runes('Rune Haine I','Colere','rune_haut_droite','I','Normale','ATK%')
            Rune_Haine_I_bas_droite=Runes('Rune Haine I','Colere','rune_bas_droite','I','Normale','ATK%')
            Rune_Haine_I_bas=Runes('Rune Haine I','Colere','rune_bas','I','Normale','ATK%')
            Rune_Haine_I_bas_gauche=Runes('Rune Haine I','Colere','rune_bas_gauche','I','Normale','ATK%')
            Rune_Haine_I_haut_gauche=Runes('Rune Haine I','Colere','rune_haut_gauche','I','Normale','ATK%')
            Rune_Haine_I=[Rune_Haine_I_haut,Rune_Haine_I_haut_droite,Rune_Haine_I_bas_droite,Rune_Haine_I_bas,Rune_Haine_I_bas_gauche,Rune_Haine_I_haut_gauche]

            Rune_Tenace_I_haut=Runes('Rune Tenace I','Tenace','rune_haut','I','Normale','DEF+')
            Rune_Tenace_I_haut_droite=Runes('Rune Tenace I','Tenace','rune_haut_droite','I','Normale','DEF+')
            Rune_Tenace_I_bas_droite=Runes('Rune Tenace I','Tenace','rune_bas_droite','I','Normale','DEF+')
            Rune_Tenace_I_bas=Runes('Rune Tenace I','Tenace','rune_bas','I','Normale','DEF+')
            Rune_Tenace_I_bas_gauche=Runes('Rune Tenace I','Tenace','rune_bas_gauche','I','Normale','DEF+')
            Rune_Tenace_I_haut_gauche=Runes('Rune Tenace I','Tenace','rune_haut_gauche','I','Normale','DEF+')
            Rune_Tenace_I=[Rune_Tenace_I_haut,Rune_Tenace_I_haut_droite,Rune_Tenace_I_bas_droite,Rune_Tenace_I_bas,Rune_Tenace_I_bas_gauche,Rune_Tenace_I_haut_gauche]

            Rune_Gardien_I_haut=Runes('Rune Gardien I','Tenace','rune_haut','I','Normale','DEF%')
            Rune_Gardien_I_haut_droite=Runes('Rune Gardien I','Tenace','rune_haut_droite','I','Normale','DEF%')
            Rune_Gardien_I_bas_droite=Runes('Rune Gardien I','Tenace','rune_bas_droite','I','Normale','DEF%')
            Rune_Gardien_I_bas=Runes('Rune Tenace I','Gardien','rune_bas','I','Normale','DEF%')
            Rune_Gardien_I_bas_gauche=Runes('Rune Gardien I','Tenace','rune_bas_gauche','I','Normale','DEF%')
            Rune_Gardien_I_haut_gauche=Runes('Rune Gardien I','Tenace','rune_haut_gauche','I','Normale','DEF%')
            Rune_Gardien_I=[Rune_Gardien_I_haut,Rune_Gardien_I_haut_droite,Rune_Gardien_I_bas_droite,Rune_Gardien_I_bas,Rune_Gardien_I_bas_gauche,Rune_Gardien_I_haut_gauche]

            Rune_Veloce_I_haut=Runes('Rune Veloce I','Veloce','rune_haut','I','Normale','VIT+')
            Rune_Veloce_I_haut_droite=Runes('Rune Veloce I','Veloce','rune_haut_droite','I','Normale','VIT+')
            Rune_Veloce_I_bas_droite=Runes('Rune Veloce I','Veloce','rune_bas_droite','I','Normale','VIT+')
            Rune_Veloce_I_bas=Runes('Rune Veloce I','Veloce','rune_bas','I','Normale','VIT+')
            Rune_Veloce_I_bas_gauche=Runes('Rune Veloce I','Veloce','rune_bas_gauche','I','Normale','VIT+')
            Rune_Veloce_I_haut_gauche=Runes('Rune Veloce I','Veloce','rune_haut_gauche','I','Normale','VIT+')
            Rune_Veloce_I=[Rune_Veloce_I_haut,Rune_Veloce_I_haut_droite,Rune_Veloce_I_bas_droite,Rune_Veloce_I_bas,Rune_Veloce_I_bas_gauche,Rune_Veloce_I_haut_gauche]
            '''
            Cheatée
            Rune_Transcendance_I_haut=Runes('Rune Transcendance I','Transcendance','rune_haut','I','Normale','TCC%')
            Rune_Transcendance_I_haut_droite=Runes('Rune Transcendance I','Transcendance','rune_haut_droite','I','Normale','TCC%')
            Rune_Transcendance_I_bas_droite=Runes('Rune Transcendance I','Transcendance','rune_bas_droite','I','Normale','HP%')
            Rune_Transcendance_I_bas=Runes('Rune Transcendance I','Transcendance','rune_bas','I','Normale','HP%')
            Rune_Transcendance_I_bas_gauche=Runes('Rune Transcendance I','Transcendance','rune_bas_gauche','I','Normale','HP%')
            Rune_Transcendance_I_haut_gauche=Runes('Rune Transcendance I','Transcendance','rune_haut_gauche','I','Normale','HP%')
            Rune_Transcendance_I=[Rune_Transcendance_I_haut,Rune_Transcendance_I_haut_droite,Rune_Transcendance_I_bas_droite,Rune_Transcendance_I_bas,Rune_Transcendance_I_bas_gauche,Rune_Transcendance_I_haut_gauche]

            Cheatée
            Rune_Extase_I_haut=Runes('Rune Extase I','Extase','rune_haut','I','Normale','HP%')
            Rune_Extase_I_haut_droite=Runes('Rune Extase I','Extase','rune_haut_droite','I','Normale','HP%')
            Rune_Extase_I_bas_droite=Runes('Rune Extase I','Extase','rune_bas_droite','I','Normale','HP%')
            Rune_Extase_I_bas=Runes('Rune Extase I','Extase','rune_bas','I','Normale','HP%')
            Rune_Extase_I_bas_gauche=Runes('Rune Extase I','Extase','rune_bas_gauche','I','Normale','HP%')
            Rune_Extase_I_haut_gauche=Runes('Rune Extase I','Extase','rune_haut_gauche','I','Normale','HP%')
            Rune_Extase_I=[Rune_Extase_I_haut,Rune_Extase_I_haut_droite,Rune_Extase_I_bas_droite,Rune_Extase_I_bas,Rune_Extase_I_bas_gauche,Rune_Extase_I_haut_gauche]

            Cheatée
            Rune_Destruction_I_haut=Runes('Rune Destruction I','Destruction','rune_haut','I','Normale','TCC%')
            Rune_Destruction_I_haut_droite=Runes('Rune Destruction I','Destruction','rune_haut_droite','I','Normale','TCC%')
            Rune_Destruction_I_bas_droite=Runes('Rune Destruction I','Destruction','rune_bas_droite','I','Normale','DC%')
            Rune_Destruction_I_bas=Runes('Rune Destruction I','Destruction','rune_bas','I','Normale','DC%')
            Rune_Destruction_I_bas_gauche=Runes('Rune Destruction I','Destruction','rune_bas_gauche','I','Normale','DC%')
            Rune_Destruction_I_haut_gauche=Runes('Rune Destruction I','Destruction','rune_haut_gauche','I','Normale','DC%')
            Rune_Destruction_I=[Rune_Destruction_I_haut,Rune_Destruction_I_haut_droite,Rune_Destruction_I_bas_droite,Rune_Destruction_I_bas,Rune_Destruction_I_bas_gauche,Rune_Destruction_I_haut_gauche]

            Cheatée
            Rune_Domination_I_haut=Runes('Rune Domination I','Domination','rune_haut','I','Normale','TCC%')
            Rune_Domination_I_haut_droite=Runes('Rune Domination I','Domination','rune_haut_droite','I','Normale','TCC%')
            Rune_Domination_I_bas_droite=Runes('Rune Domination I','Domination','rune_bas_droite','I','Normale','DC%')
            Rune_Domination_I_bas=Runes('Rune Domination I','Domination','rune_bas','I','Normale','DC%')
            Rune_Domination_I_bas_gauche=Runes('Rune Domination I','Domination','rune_bas_gauche','I','Normale','DC%')
            Rune_Domination_I_haut_gauche=Runes('Rune Domination I','Domination','rune_haut_gauche','I','Normale','DC%')
            Rune_Domination_I=[Rune_Domination_I_haut,Rune_Domination_I_haut_droite,Rune_Domination_I_bas_droite,Rune_Domination_I_bas,Rune_Domination_I_bas_gauche,Rune_Domination_I_haut_gauche]

            Cheatée
            Rune_Inébranlable_I_haut=Runes('Rune Inébranlable I','Inébranlable','rune_haut','I','Normale','HP%')
            Rune_Inébranlable_I_haut_droite=Runes('Rune Inébranlable I','Inébranlable','rune_haut_droite','I','Normale','HP%')
            Rune_Inébranlable_I_bas_droite=Runes('Rune Inébranlable I','Inébranlable','rune_bas_droite','I','Normale','HP%')
            Rune_Inébranlable_I_bas=Runes('Rune Inébranlable I','Inébranlable','rune_bas','I','Normale','HP%')
            Rune_Inébranlable_I_bas_gauche=Runes('Rune Inébranlable I','Inébranlable','rune_bas_gauche','I','Normale','HP%')
            Rune_Inébranlable_I_haut_gauche=Runes('Rune Inébranlable I','Inébranlable','rune_haut_gauche','I','Normale','HP%')
            Rune_Inébranlable_I=[Rune_Inébranlable_I_haut,Rune_Inébranlable_I_haut_droite,Rune_Inébranlable_I_bas_droite,Rune_Inébranlable_I_bas,Rune_Inébranlable_I_bas_gauche,Rune_Inébranlable_I_haut_gauche]

            Pas cheatée
            Rune_Volonté_I_haut=Runes('Rune Volonté I','Volonté','rune_haut','I','Normale','HP%')
            Rune_Volonté_I_haut_droite=Runes('Rune Volonté I','Volonté','rune_haut_droite','I','Normale','HP%')
            Rune_Volonté_I_bas_droite=Runes('Rune Volonté I','Volonté','rune_bas_droite','I','Normale','HP%')
            Rune_Volonté_I_bas=Runes('Rune Volonté I','Volonté','rune_bas','I','Normale','HP%')
            Rune_Volonté_I_bas_gauche=Runes('Rune Volonté I','Volonté','rune_bas_gauche','I','Normale','HP%')
            Rune_Volonté_I_haut_gauche=Runes('Rune Volonté I','Volonté','rune_haut_gauche','I','Normale','HP%')
            Rune_Volonté_I=[Rune_Volonté_I_haut,Rune_Volonté_I_haut_droite,Rune_Volonté_I_bas_droite,Rune_Volonté_I_bas,Rune_Volonté_I_bas_gauche,Rune_Volonté_I_haut_gauche]

            Plus que cheatée
            Rune_Sublimation_I_haut=Runes('Rune Sublimation I','Sublimation','rune_haut','I','Normale','HP%')
            Rune_Sublimation_I_haut_droite=Runes('Rune Sublimation I','Sublimation','rune_haut_droite','I','Normale','HP%')
            Rune_Sublimation_I_bas_droite=Runes('Rune Sublimation I','Sublimation','rune_bas_droite','I','Normale','HP%')
            Rune_Sublimation_I_bas=Runes('Rune Sublimation I','Sublimation','rune_bas','I','Normale','HP%')
            Rune_Sublimation_I_bas_gauche=Runes('Rune Sublimation I','Sublimation','rune_bas_gauche','I','Normale','HP%')
            Rune_Sublimation_I_haut_gauche=Runes('Rune Sublimation I','Sublimation','rune_haut_gauche','I','Normale','HP%')
            Rune_Sublimation_I=[Rune_Sublimation_I_haut,Rune_Sublimation_I_haut_droite,Rune_Sublimation_I_bas_droite,Rune_Sublimation_I_bas,Rune_Sublimation_I_bas_gauche,Rune_Sublimation_I_haut_gauche]

            Pas cheatée
            Rune_Vampirique_I_haut=Runes('Rune Vampirique I','Vampirique','rune_haut','I','Normale','TCC%')
            Rune_Vampirique_I_haut_droite=Runes('Rune Vampirique I','Vampirique','rune_haut_droite','I','Normale','TCC%')
            Rune_Vampirique_I_bas_droite=Runes('Rune Vampirique I','Vampirique','rune_bas_droite','I','Normale','DC%')
            Rune_Vampirique_I_bas=Runes('Rune Vampirique I','Vampirique','rune_bas','I','Normale','DC%')
            Rune_Vampirique_I_bas_gauche=Runes('Rune Vampirique I','Vampirique','rune_bas_gauche','I','Normale','DC%')
            Rune_Vampirique_I_haut_gauche=Runes('Rune Vampirique I','Vampirique','rune_haut_gauche','I','Normale','DC%')
            Rune_Vampirique_I=[Rune_Vampirique_I_haut,Rune_Vampirique_I_haut_droite,Rune_Vampirique_I_bas_droite,Rune_Vampirique_I_bas,Rune_Vampirique_I_bas_gauche,Rune_Vampirique_I_haut_gauche]

            Plus que cheatée
            Rune_Incandescence_I_haut=Runes('Rune Incandescence I','Incandescence','rune_haut','I','Normale','TCC%')
            Rune_Incandescence_I_haut_droite=Runes('Rune Incandescence I','Incandescence','rune_haut_droite','I','Normale','TCC%')
            Rune_Incandescence_I_bas_droite=Runes('Rune Incandescence I','Incandescence','rune_bas_droite','I','Normale','DC%')
            Rune_Incandescence_I_bas=Runes('Rune Incandescence I','Incandescence','rune_bas','I','Normale','DC%')
            Rune_Incandescence_I_bas_gauche=Runes('Rune Incandescence I','Incandescence','rune_bas_gauche','I','Normale','DC%')
            Rune_Incandescence_I_haut_gauche=Runes('Rune Incandescence I','Incandescence','rune_haut_gauche','I','Normale','DC%')
            Rune_Vampirique_I=[Rune_Incandescence_I_haut,Rune_Incandescence_I_haut_droite,Rune_Incandescence_I_bas_droite,Rune_Incandescence_I_bas,Rune_Incandescence_I_bas_gauche,Rune_Incandescence_I_haut_gauche]

            Pas cheatée
            Rune_Desespoir_I_haut=Runes('Rune Desespoir I','Desespoir','rune_haut','I','Normale','TCC%')
            Rune_Desespoir_I_haut_droite=Runes('Rune Desespoir I','Desespoir','rune_haut_droite','I','Normale','TCC%')
            Rune_Desespoir_I_bas_droite=Runes('Rune Desespoir I','Desespoir','rune_bas_droite','I','Normale','DC%')
            Rune_Desespoir_I_bas=Runes('Rune Desespoir I','Desespoir','rune_bas','I','Normale','DC%')
            Rune_Desespoir_I_bas_gauche=Runes('Rune Desespoir I','Desespoir','rune_bas_gauche','I','Normale','DC%')
            Rune_Desespoir_I_haut_gauche=Runes('Rune Desespoir I','Desespoir','rune_haut_gauche','I','Normale','DC%')
            Rune_Desespoir_I=[Rune_Desespoir_I_haut,Rune_Desespoir_I_haut_droite,Rune_Desespoir_I_bas_droite,Rune_Desespoir_I_bas,Rune_Desespoir_I_bas_gauche,Rune_Desespoir_I_haut_gauche]

            Faire Destruction (STR AGI), Domination (donne un tour d'invincibilite), Immunité (Inébranlable) (Volonté en moins puissant = pas cheaté), Régénération (Sublimation), Vengeance, Vampirique et Incandescence (vampirique améliorée)
            '''
            Rune_Lame_I_haut=Runes('Rune Lame I','Lame','rune_haut','I','Normale','TCC%')
            Rune_Lame_I_haut_droite=Runes('Rune Lame I','Lame','rune_haut_droite','I','Normale','TCC%')
            Rune_Lame_I_bas_droite=Runes('Rune Lame I','Lame','rune_bas_droite','I','Normale','TCC%')
            Rune_Lame_I_bas=Runes('Rune Lame I','Lame','rune_bas','I','Normale','TCC%')
            Rune_Lame_I_bas_gauche=Runes('Rune Lame I','Lame','rune_bas_gauche','I','Normale','TCC%')
            Rune_Lame_I_haut_gauche=Runes('Rune Lame I','Lame','rune_haut_gauche','I','Normale','TCC%')
            Rune_Lame_I=[Rune_Lame_I_haut,Rune_Lame_I_haut_droite,Rune_Lame_I_bas_droite,Rune_Lame_I_bas,Rune_Lame_I_bas_gauche,Rune_Lame_I_haut_gauche]

            Rune_Rage_I_haut=Runes('Rune Rage I','Rage','rune_haut','I','Normale','DC%')
            Rune_Rage_I_haut_droite=Runes('Rune Rage I','Rage','rune_haut_droite','I','Normale','DC%')
            Rune_Rage_I_bas_droite=Runes('Rune Rage I','Rage','rune_bas_droite','I','Normale','DC%')
            Rune_Rage_I_bas=Runes('Rune Rage I','Rage','rune_bas','I','Normale','DC%')
            Rune_Rage_I_bas_gauche=Runes('Rune Rage I','Rage','rune_bas_gauche','I','Normale','DC%')
            Rune_Rage_I_haut_gauche=Runes('Rune Rage I','Rage','rune_haut_gauche','I','Normale','DC%')
            Rune_Rage_I=[Rune_Rage_I_haut,Rune_Rage_I_haut_droite,Rune_Rage_I_bas_droite,Rune_Rage_I_bas,Rune_Rage_I_bas_gauche,Rune_Rage_I_haut_gauche]

            Rune_Sniper_I_haut=Runes('Rune Sniper I','Precision','rune_haut','I','Normale','ACC%')
            Rune_Sniper_I_haut_droite=Runes('Rune Sniper I','Precision','rune_haut_droite','I','Normale','ACC%')
            Rune_Sniper_I_bas_droite=Runes('Rune Sniper I','Precision','rune_bas_droite','I','Normale','ACC%')
            Rune_Sniper_I_bas=Runes('Rune Sniper I','Precision','rune_bas','I','Normale','ACC%')
            Rune_Sniper_I_bas_gauche=Runes('Rune Sniper I','Precision','rune_bas_gauche','I','Normale','ACC%')
            Rune_Sniper_I_haut_gauche=Runes('Rune Sniper I','Precision','rune_haut_gauche','I','Normale','ACC%')
            Rune_Sniper_I=[Rune_Sniper_I_haut,Rune_Sniper_I_haut_droite,Rune_Sniper_I_bas_droite,Rune_Sniper_I_bas,Rune_Sniper_I_bas_gauche,Rune_Sniper_I_haut_gauche]

            Rune_Illumination_I_haut=Runes('Rune Illumination I','Resistance','rune_haut','I','Normale','RES%')
            Rune_Illumination_I_haut_droite=Runes('Rune Illumination I','Resistance','rune_haut_droite','I','Normale','RES%')
            Rune_Illumination_I_bas_droite=Runes('Rune Illumination I','Resistance','rune_bas_droite','I','Normale','RES%')
            Rune_Illumination_I_bas=Runes('Rune Illumination I','Energie','Resistance','I','Normale','RES%')
            Rune_Illumination_I_bas_gauche=Runes('Rune Illumination I','Resistance','rune_bas_gauche','I','Normale','RES%')
            Rune_Illumination_I_haut_gauche=Runes('Rune Illumination I','Resistance','rune_haut_gauche','I','Normale','RES%')
            Rune_Illumination_I=[Rune_Illumination_I_haut,Rune_Illumination_I_haut_droite,Rune_Illumination_I_bas_droite,Rune_Illumination_I_bas,Rune_Illumination_I_bas_gauche,Rune_Illumination_I_haut_gauche]

            Rune_toutes_categories_I=[Rune_Energie_I,Rune_Altruisme_I,Rune_Colere_I,Rune_Haine_I,Rune_Tenace_I,Rune_Gardien_I,Rune_Veloce_I,Rune_Lame_I,Rune_Rage_I,Rune_Sniper_I,Rune_Illumination_I]

            if(choix_categorie_rune_a_acheter==0):
                Inventaire.magasin(base,sac)
            else:
                print('Ne rien acheter = 0 \n')
                possibilites_runes_a_acheter=[0]
                for i in range(len(Rune_toutes_categories_I[choix_categorie_rune_a_acheter-1])):
                    print(Rune_toutes_categories_I[choix_categorie_rune_a_acheter-1][i])
                    print('Prix d achat :',Rune_toutes_categories_I[choix_categorie_rune_a_acheter-1][i].prix_d_achat,' : rentrez ',i+1,'\n')
                    str(input(' > '))
                    possibilites_runes_a_acheter.append(i+1)
                entree=input('\nQue voulez-vous acheter ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQue voulez-vous acheter ? ')
                indice_rune_a_acheter=int(entree)
                while(indice_rune_a_acheter not in possibilites_runes_a_acheter):
                    entree=input('\nQue voulez-vous acheter ? ')
                    while(not IsSecure(entree)):
                        entree=input('Que voulez-vous acheter ? ')
                    indice_rune_a_acheter=int(entree)
                if(indice_rune_a_acheter==0):
                    Inventaire.magasin(base,sac)
                else:
                    Rune_a_acheter=Rune_toutes_categories_I[choix_categorie_rune_a_acheter-1][indice_rune_a_acheter-1]
                    Inventaire.acheter_objet(base,sac,Rune_a_acheter)

        if(choix_magasin==2):
            entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre un parchemin ? ')
            while(not IsSecure(entree)):
                entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre un parchemin ? ')
            choix_objet_a_vendre=int(entree)
            while(choix_objet_a_vendre!=0 and choix_objet_a_vendre!=1):
                entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre un parchemin ? ')
                while(not IsSecure(entree)):
                    entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre un parchemin ? ')
                choix_objet_a_vendre=int(entree)
            if(choix_objet_a_vendre==1):
                entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre une rune ? ')
                while(not IsSecure(entree)):
                    entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre une rune ? ')
                choix_objet_a_vendre_2=int(entree)
                while(choix_objet_a_vendre_2!=0 and choix_objet_a_vendre_2!=1):
                    entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre une rune ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre une rune ? ')
                    choix_objet_a_vendre_2=int(entree)
                if(choix_objet_a_vendre_2==1):
                    print('Je vois, vous avez changé d avis!! \n')
                    Inventaire.magasin(base,sac)
                else:
                    possibilites_runes_a_vendre=[]
                    j=1
                    while(j<=sac.place_dernier_equipement):
                        Inventaire.Afficher_contenu_sac_zone_unique(sac,'equipement',j)
                        possibilites_runes_a_vendre.append(j)
                        j+=1
                    if(len(possibilites_runes_a_vendre)==0):
                        print('Vous n avez aucune rune à vendre pour le moment.')
                        Inventaire.magasin(base,sac)
                    else:
                        entree=input('Quelle rune voulez-vous vendre ? ')
                        while(not IsSecure(entree)):
                            entree=input('Quelle rune voulez-vous vendre ? ')
                        place_rune_a_vendre=int(entree)
                        while(place_rune_a_vendre not in possibilites_runes_a_vendre):
                            entree=input('Quelle rune voulez-vous vendre ? ')
                            while(not IsSecure(entree)):
                                entree=input('Quelle rune voulez-vous vendre ? ')
                            place_rune_a_vendre=int(entree)
                        Inventaire.vendre_objet(base,sac,'equipement',place_rune_a_vendre)
            else:
                possibilites_parchemins_a_vendre=[]
                i=1
                while(i<=sac.place_dernier_objet_courant):
                    Inventaire.Afficher_contenu_sac_zone_unique(sac,'objets_courants',i)
                    possibilites_parchemins_a_vendre.append(i)
                    i+=1
                if(len(possibilites_parchemins_a_vendre)==0):
                    print('Vous n avez aucun parchemin à vendre pour le moment.')
                    Inventaire.magasin(base,sac)
                else:
                    entree=input('Quel parchemin voulez-vous vendre ? ')
                    while(not IsSecure(entree)):
                        entree=input('Quel parchemin voulez-vous vendre ? ')
                    place_parchemin_a_vendre=int(entree)
                    while(place_parchemin_a_vendre not in possibilites_parchemins_a_vendre):
                        entree=input('Quel parchemin voulez-vous vendre ? ')
                        while(not IsSecure(entree)):
                            entree=input('Quel parchemin voulez-vous vendre ? ')
                        place_parchemin_a_vendre=int(entree)
                    Inventaire.vendre_objet(base,sac,'objets_courants',place_parchemin_a_vendre)


    def acheter_objet(base,sac,objet_achete):
        if(objet_achete.prix_d_achat>sac.mana):
            print('Vous n avez pas assez de pierres de mana pour acheter ceci. \n')
        else:
            sac.mana-=objet_achete.prix_d_achat
            print('Vous avez acheté ',objet_achete.nom,'!!')
            if(objet_achete.type=='Rune'):
                print(objet_achete,'\n')
            Inventaire.ajouter_objet(sac,objet_achete)
        Inventaire.magasin(base,sac)


    def vendre_objet(base,sac,zone,indice):
        if (zone=='equipement'):
            if (indice>0 and indice<=sac.place_dernier_equipement):
                valeur=sac.equipement[indice].prix_d_achat/2
                print('La valeur de la rune que vous voulez vendre est de ',valeur,' pierres de mana.')
                print('Êtes vous sûr(e) de vouloir vendre la rune ',sac.equipement[indice].nom,' ? \n')
                entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                while(not IsSecure(entree)):
                    entree=input('Oui = 0 \nNon = 1 \nQuel est ovtre choix ? ')
                choix=int(entree)
                while(choix!=0 and choix!=1):
                    entree=input('\n\nOui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    while(not IsSecure(entree)):
                        entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    choix=int(entree)
                if (choix==0):
                    print('La rune ',sac.equipement[indice].nom,' a bien été vendue. \n')
                    sac.equipement[indice]=0
                    for i in range(indice,sac.place_dernier_equipement-1):
                        sac.equipement[i]=sac.equipement[i+1]
                    sac.equipement[sac.place_dernier_equipement]=0
                    sac.place_dernier_equipement-=1
                    sac.mana+=valeur
            else:
                print('Vous n avez aucune rune à cet emplacement du sac.')
        else:
            if(zone=='objets_courants'):
                if (indice>0 and indice<=sac.place_dernier_objet_courant):
                    valeur=sac.objets_courants[indice].prix_de_vente
                    print('La valeur de l objet que vous voulez vendre est de ',valeur,' pierres de mana.')
                    print('Êtes vous sûr(e) de vouloir vendre l objet ',sac.objets_courants[indice].nom,' ? \n')
                    entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    while(not IsSecure(entree)):
                        entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    choix=int(entree)
                    while(choix!=0 and choix!=1):
                        entree=input('\n\nOui = 0 \nNon = 1 \nQuel est votre choix ? ')
                        while(not IsSecure(entree)):
                            entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                        choix=int(entree)
                    if (choix==0):
                        print('L objet ',sac.objets_courants[indice].nom,' a bien été vendu.')
                        print('Vous recevez ',valeur,'pierres de mana!! \n')
                        sac.objets_courants[indice]=0
                        for i in range(indice,sac.place_dernier_objet_courant-1):
                            sac.equipement[i]=sac.objets_courants[i+1]
                        sac.objets_courants[sac.place_dernier_objet_courant]=0
                        sac.place_dernier_objet_courant-=1
                        sac.mana+=valeur
                else:
                    print('Vous n avez aucun objet à cet emplacement du sac.')
        print('\n')
        Inventaire.magasin(base,sac)
