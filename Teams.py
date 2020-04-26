# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:41:34 2019

@author: marin
"""


# doctest à chercher!!!!!

'''
import sys
import math
from ast import literal_eval
import random
'''

from Monsters import *
from Inventory import *
from Server import *
# from Client import *


class Equipe:
    # IMPORTANT POUR TOUTES LES FONCTIONS : UNE EQUIPE COMPORTE AU MINIMUM UN LEADER != 0 !!!!
    def __init__(self,game,liste_de_monstres,taille):
        self.taille_petite_equipe=3
        self.taille_moyenne_equipe=5
        self.taille_grande_equipe=10
        self.taille_equipe_geante=20

        self.membres=liste_de_monstres
        self.len=taille # paramètre indépendant de self.membres
        self.base=game
        self.nom_niveau_donjon='' # utilisé pour les graphismes 
        # On aurait pu faire Game.__init__(self) pour pouvoir utiliser self.stockage
        # Mais le stockage appartient à une base de référence pour une équipe (plus clair je trouve)

        # Toutes les équipes seront initialisées avec la même game
        # Elles auront ainsi toute la même base de référence, laquelle aura
        # un stockage et un index communs pour toutes les équipes la remplissant 



    def afficher(self):
        print('\n Leader : ')
        print(self.membres[0],'\n\n')
        index=1
        while(self.len > index and self.membres[index] != 0):
            print(' Membre ',index,' : ')
            print(self.membres[index],'\n\n')
            index+=1

    def afficher_partiellement(self):
        print('Taille de l\'équipe : ',self.len,' membres. \n')
        print('\nLeader : ',self.membres[0].surnom,'(',self.membres[0].nom,' de ',self.membres[0].attribut,self.membres[0].classe,' étoiles)\n\n')
        index=1
        while (self.len > index and self.membres[index] != 0):
            print('Membre ',index,' : ',self.membres[index].surnom,'(',self.membres[index].nom,' de ',self.membres[index].attribut,self.membres[index].classe,' étoiles)\n\n')
            index+=1
        while (index < self.taille_petite_equipe):
            print('Emplacement ',index,' de l\'équipe : libre\n\n')
            index+=1


    def afficher_position_stockage(self):
        print(self.membres[0].surnom,'(',self.membres[0].nom,' de ',self.membres[0].attribut,self.membres[0].classe,' étoiles) se situe à l\'emplacement ',self.membres[0].indice_stockage_base,' du stockage.\n')
        index=1
        while(self.len > index and self.membres[index]!=0):
            print(self.membres[index].surnom,'(',self.membres[index].nom,' de ',self.membres[index].attribut,self.membres[index].classe,' étoiles) se situe à l\'emplacement ',self.membres[index].indice_stockage_base,' du stockage.\n')
            index+=1









    def modifier(self):
        print('L équipe actuelle  est : ')
        self.afficher_partiellement()
        print('\n\n')

        # Affichage des monstres à remplacer possibles 
        possibilites_modifier=[]
        for index in range(self.taille_petite_equipe):
            if(self.membres[index] != 0):
                print('\n',self.membres[index],' = ',index,'\n')
            else:
                print('\n Emplacement ',index,' : libre \n')
            possibilites_modifier.append(index)

        # Choix du monstre à remplacer
        entree=input('Quel monstre voulez-vous remplacer ? ')
        while(not Security.is_decimal(entree)):
            entree=input('Quel monstre voulez-vous remplacer ? ')
        place_monstre_a_retirer=int(entree)
        while(place_monstre_a_retirer not in possibilites_modifier):
            entree=input('Quel monstre voulez-vous remplacer ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Quel monstre voulez-vous remplacer ? ')
            place_monstre_a_retirer=int(entree)        
        print('\n\n')

        # Affichage des monstres remplaçants possibles 
        print('Ne remplacer ce monstre par personne = ',0,'\n')
        possibilites=[0]
        index=1
        while(index <= self.base.place_dernier_monstre):
            # Si le monstre dans le stockage n'est pas déjà dans l'équipe
            if(self.base.stockage[index] not in self.membres):
                print(self.base.stockage[index],' = ',index,'\n')
                possibilites.append(index)
            index+=1
        
        # Choix du monstre remplaçant 
        entree=input('Par quel monstre voulez-vous le remplacer ? ')
        while(not Security.is_decimal(entree)):
            entree=input('Par quel monstre voulez-vous le remplacer ? ')
        place_monstre_remplacant=int(entree)
        while(place_monstre_remplacant not in possibilites):
            entree=input('Par quel monstre voulez-vous le remplacer ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Par quel monstre voulez-vous le remplacer ? ')
            place_monstre_remplacant=int(entree)
        
        # Remplacement 
        if(place_monstre_remplacant != 0):
            if(self.membres[place_monstre_a_retirer] == 0):
                self.len+=1
            self.membres[place_monstre_a_retirer]=self.base.stockage[place_monstre_remplacant]
        else:
            self.supprimer_monstre_equipe(place_monstre_a_retirer)
        print('\nL\'équipe est désormais : \n')
        self.afficher_partiellement()
        

    def ajouter(self):
        if(self.membres[0] != 0 and self.membres[1] != 0 and self.membres[2] != 0):
            print('L\'équipe est déjà au complet!! \n\n')
        else:
            print('L équipe actuelle  est : ')
            self.afficher_partiellement()
            print('\n\n')

            # Affichage des emplacements d'ajout possibles
            possibilites_emplacement=[]
            index=1
            while(self.membres[index] != 0):
                index+=1
            while(index < self.taille_petite_equipe):
                print('\n Ajouter un monstre à l\'emplacement ',index,' de l\'équipe = ',index,' \n')
                possibilites_emplacement.append(index)
                index+=1

            
            print('\n\n',possibilites_emplacement,'\n\n')
            '''
            for index in range(self.taille_petite_equipe):
                if(self.membres[index] == 0):
                    print('\n',self.membres[index],' = ',index,'\n')
                    possibilites_modifier.append(index)
            '''

            # Sélection de l'emplacement d'ajout 
            entree=input('A quel emplacement voulez-vous ajouter un monstre ? ')
            while(not Security.is_decimal(entree)):
                entree=input('A quel emplacement voulez-vous ajouter un monstre ? ')
            place_monstre_a_ajouter=int(entree)
            while(place_monstre_a_ajouter not in possibilites_emplacement):
                entree=input('A quel emplacement voulez-vous ajouter un monstre ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('A quel emplacement voulez-vous ajouter un monstre ? ')
                place_monstre_a_ajouter=int(entree)
            print('\n\n')
                
            # Affichage des monstres à ajouter possibles 
            print('Annuler et ne pas ajouter de monstre = ',0,'\n')
            possibilites=[0]
            index=1
            while(index <= self.base.place_dernier_monstre):
                # Si le monstre dans le stockage n'est pas déjà dans l'équipe
                if(self.base.stockage[index] not in self.membres):
                    print(self.base.stockage[index],' = ',index,'\n')
                    possibilites.append(index)
                index+=1

            # Choix du monstre à ajouter 
            entree=input('Quel monstre voulez-vous y ajouter ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Quel monstre voulez-vous y ajouter ? ')
            place_monstre_remplacant=int(entree)
            while(place_monstre_remplacant not in possibilites):
                entree=input('Quel monstre voulez-vous y ajouter ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('Quel monstre voulez-vous y ajouter ? ')
                place_monstre_remplacant=int(entree)

            # Ajout du monstre à l'équipe 
            if(place_monstre_remplacant != 0):
                self.membres[place_monstre_a_ajouter]=self.base.stockage[place_monstre_remplacant]
                self.len+=1
        print('\nL\'équipe est désormais : \n')
        self.afficher_partiellement()



    def supprimer_monstre_base(self,indice):
        if (indice > 0 and indice <= self.base.place_dernier_monstre):
            # Suppression du monstre dans l'équipe 
            if(indice == self.membres[0].indice_stockage_base):
                self.supprimer_monstre_equipe(0)
            if(self.membres[1] != 0 and indice == self.membres[1].indice_stockage_base):
                self.supprimer_monstre_equipe(1)
            if(self.membres[2] != 0 and indice == self.membres[2].indice_stockage_base):
                self.supprimer_monstre_equipe(2)
            
            # Suppression du monstre dans le stockage de la base
            for index in range(indice,self.base.place_dernier_monstre):
                self.base.stockage[index]=self.base.stockage[index+1]
                self.base.stockage[index].indice_stockage_base-=1
            self.base.stockage[self.base.place_dernier_monstre]=0 
            self.base.place_dernier_monstre-=1
        else:
            print('Vous n\'avez aucun monstre à cet emplacement de la base.')

    def relacher_monstre(self,indice):
        if (indice > 0 and indice <= self.base.place_dernier_monstre):
            if((self.len == 1) and (self.membres[0] == self.stockage[indice])):
                print('Vous ne pouvez pas relâcher ce montre. \n\n')
            else:
                print('Êtes vous sûr(e) de vouloir relâcher le monstre ',self.stockage[indice].nom,self.stockage[indice].attribut,' ? \n')
                entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                choix=int(entree)
                while(choix!=0 and choix!=1):
                    entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    choix=int(entree)
                if (choix == 0):
                    print('Le monstre ',self.stockage[indice].surnom,'(',self.stockage[indice].nom,') a bien été relâché. \n')
                    self.supprimer_monstre_base(indice)
        else:
            print('Vous n avez aucun monstre à cet emplacement de la base.')

    def supprimer_monstre_equipe(self,indice):
        if(indice == 0):
            # Si il y a au moins un autre membre dans l'équipe
            if(self.membres[1] != 0 or self.membres[2] != 0):
                self.membres.pop(0)
                self.len-=1
            else:
                print('\nImpossible de retirer de votre équipe l\'unique monstre qui la compose... \n')
                
        else:
            self.membres.pop(indice)
            self.len-=1
        if(self.len < 3):
            self.membres.append(0)


    def modifier_alignement(self):
        print('Leader : ',self.membres[0].surnom,' de ',self.membres[0].attribut,self.membres[0].classe,' étoiles  = 0')
        if(self.len > 1):
            print('Membre 1 : ',self.membres[1].surnom,' de ',self.membres[1].attribut,self.membres[1].classe,' étoiles  = 1')
        if(self.len > 2):
            print('Membre 2 : ',self.membres[2].surnom,' de ',self.membres[2].attribut,self.membres[2].classe,' étoiles  = 2 \n\n')

        if(self.len==1):
            print('Votre équipe ne comporte qu un seul monstre. Impossible de changer son alignement!!')
        else:
            if(self.len==2):
                indice_stockage_base_tmp=self.membres[0].indice_stockage_base
                self.membres[0]=self.base.stockage[self.membre_1.indice_stockage_base]
                self.membres[1]=self.base.stockage[indice_stockage_base_tmp]
            else:
                entree=input('\nQuel est le premier monstre que vous voulez permuter ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQuel est le premier monstre que vous voulez permuter ? ')
                choix1=int(entree)
                while(choix1 not in [0,1,2]):
                    entree=input('\nQuel est le premier monstre que vous voulez permuter ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQuel est le premier monstre que vous voulez permuter ? ')
                    choix1=int(entree)

                entree=input('\nAvec quel monstre voulez-vous le permuter ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nAvec quel monstre voulez-vous le permuter ? ')
                choix2=int(entree)
                while(choix2 not in [0,1,2]):
                    entree=input('\nAvec quel monstre voulez-vous le permuter ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nAvec quel monstre voulez-vous le permuter ? ')
                    choix2=int(entree)
                    
                indice_stockage_base_tmp=self.membres[choix1].indice_stockage_base
                self.membres[choix1]=self.base.stockage[self.membres[choix2].indice_stockage_base]
                self.membres[choix2]=self.base.stockage[indice_stockage_base_tmp]









    def ameliorer_monstre(self,monstre_a_ameliorer):
        print('\n\nPour faire une Amélioration, vous devez choisir un monstre à sacrifier qui sera converti en expérience.')
        print('Affichage des monstres pouvant être sacrifiés : \n')
        print('Impossible d\'utiliser le monstre à l\'indice : ',monstre_a_ameliorer.indice_stockage_base,'\n')
        print('Annuler = 0\n')
        possibilites_monstres_a_sacrifier=[0]
        for index in range(1,self.base.place_dernier_monstre+1):
            if(index != monstre_a_ameliorer.indice_stockage_base):
                print(self.base.stockage[index],' = ',index,'\n')
                possibilites_monstres_a_sacrifier.append(index)

        entree=input('Quel monstre voulez-vous sacrifier ? ')
        while(not Security.is_decimal(entree)):
            entree=input('\nQuel monstre voulez-vous sacrifier ? ')
        choix_monstre_a_sacrifier=int(entree)
        while(choix_monstre_a_sacrifier not in possibilites_monstres_a_sacrifier):
            entree=input('\nQuel monstre voulez-vous sacrifier ? ')
            while(not Security.is_decimal(entree)):
                entree=input('\nQuel monstre voulez-vous sacrifier ? ')
            choix_monstre_a_sacrifier=int(entree)
        
        if((self.len==1) and (self.membres[0] == self.base.stockage[choix_monstre_a_sacrifier])):
            print('Vous ne pouvez pas sacrifier l\'unique monstre de votre équipe... \n\n')
        else:
            if(choix_monstre_a_sacrifier != 0):
                print('\n')
                XP_a_gagner=self.base.stockage[choix_monstre_a_sacrifier].calculer_XP_amelioration()
                monstre_a_ameliorer.recevoir_XP(XP_a_gagner)
                self.supprimer_monstre_base(choix_monstre_a_sacrifier)
                # Le supprime aussi de l'équipe (fonction inclue dans supprimer_monstre_base)
                self.base.stockage[monstre_a_ameliorer.indice_stockage_base]=monstre_a_ameliorer
                for index in range(self.len):
                    self.membres[index]=self.base.stockage[self.membres[index].indice_stockage_base]
                

    def monter_en_classe(self,monstre_a_evoluer):
        print('\n\nPour faire une telle Evolution, vous devez sacrifiez ',monstre_a_evoluer.classe,'monstres de ',monstre_a_evoluer.classe,'étoiles.')
        print('Pour ne pas sacrifier de monstre, annuler l\'Evolution et revenir au menu principal, rentrez 0 pour l\'un des choix à faire. \n')
        print('Affichage des monstres pouvant être sacrifiés : \n')
        possibilites_monstres_a_sacrifier=[]
        choix_monstres_materiels=[]
        for index in range(1,1+self.base.place_dernier_monstre):
            if((self.base.stockage[index].classe == monstre_a_evoluer.classe) and (index != monstre_a_evoluer.indice_stockage_base)):
                print(self.base.stockage[index],' = ',index,'\n')
            possibilites_monstres_a_sacrifier.append(index)
        print('\n\n')
        
        if(len(possibilites_monstres_a_sacrifier) < monstre_a_evoluer.classe):
            print('Pas assez de monstres matériels pour réaliser l\'Evolution \n(',len(possibilites_monstres_a_sacrifier),'disponibles, ',monstre_a_evoluer.classe,'requis)\n')
        else:
            for index in range(monstre_a_evoluer.classe):
                entree=input('\nQuel monstre voulez-vous sacrifier ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQuel monstre voulez-vous sacrifier ? ')
                choix_monstre_a_sacrifier=int(entree)
                while(choix_monstre_a_sacrifier not in possibilites_monstres_a_sacrifier):
                    entree=input('\nQuel monstre voulez-vous sacrifier ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQuel monstre voulez-vous sacrifier ? ')
                    choix_monstre_a_sacrifier=int(entree)
                choix_monstres_materiels.append(choix_monstre_a_sacrifier)                

            if(0 in choix_monstres_materiels):
                print('Annulation de l\'Evolution réussie. Retour au menu principal... \n\n')
            else:
                choix_monstres_materiels=Tri.tri_ordre_decroissant(choix_monstres_materiels)
                if(choix_monstres_materiels == Tri.tri_sans_doublons(choix_monstres_materiels)):
                    for index in range(len(choix_monstres_materiels)):
                        self.supprimer_monstre_base(choix_monstres_materiels[l])

                    monstre_a_evoluer.evoluer()
                    self.stockage[monstre_a_evoluer.indice_stockage_base]=monstre_a_evoluer
                    for index in range(self.len):
                        self.membres[index]=self.base.stockage[self.membres[index].indice_stockage_base]
                    print(monstre_a_evoluer.surnom,'évolue!!\n')
                    print(monstre_a_evoluer)
                else:
                    print('Pas assez de monstres matériels pour réaliser l\'Evolution \n(',len(Tri.tri_sans_doublons(choix_monstres_materiels)),'donnés, ',monstre_a_evoluer.classe,'requis)\n')



# Fonctions de combat 

# Fonctions qui modifient les statistiques des monstres de l'équipe lors d'un combat
# à l'échelle de l'équipe 

    def is_alive(self):
        alive=False
        if(self.membres[0].pv_actuels > 0 or (self.len > 1 and self.membres[1].pv_actuels > 0) or (self.len > 2 and self.membres[2].pv_actuels > 0)):
            alive=True
        return alive

    def is_ennemi_provocateur_in(self):
        presence=False
        if(self.membres[0].provocation > 0 or self.membres[1].provocation > 0 or self.membres[2].provocation > 0):
            presence=True
        return presence
    
    def soigner_equipe_entre_deux_vagues(self):
        for index in range(self.len):
            if(self.membres[index] != 0):
                self.membres[index].soigner_monstre_entre_deux_vagues()

    def soigner_equipe(self):
        for index in range(self.len):
            if(self.membres[index] != 0):
                self.membres[index].soigner_monstre()
            
    def soigner_team_ennemie(self):
        for index in range(self.len):
            if(self.membres[index] != 0):
                self.membres[index].etat_cap1='dispo'
                self.membres[index].attente1=0
                if(self.membres[index].nb_capacites >= 2):
                    self.membres[index].etat_cap2='dispo'
                    self.membres[index].attente2=0
                if(self.membres[index].nb_capacites >= 3):
                    self.membres[index].etat_cap3='dispo'
                    self.membres[index].attente3=0
        self.soigner_equipe()

    def un_perso_doit_jouer(self):
        doit_jouer=False
        if((self.membres[0].jauge_attaque >= 100) or (self.len > 1 and self.membres[1].jauge_attaque >= 100) or (self.len > 2 and self.membres[2].jauge_attaque >= 100)):
            doit_jouer=True
        return doit_jouer

    def tick(self):
        for index in range(self.len):
            self.membres[index].jauge_attaque+=Arrondir.a_l_unite(7*self.membres[index].vitesse_actuelle/100)
    
    def fin_du_combat(self,ennemis):
        fin=False
        if(self.is_alive() and not ennemis.is_alive()):
            fin=True
        elif(not self.is_alive()):
            fin=True
        return fin
        



    ''' IDEE : RETENIR LES INDICES DE STOCKAGE DAND LA BASE DE L EQUIPE AVANT COMBAT '''
    ''' APRES FIN DU COMBAT, RECONSTITUER EQUIPE => PAS BESOIN DE FAIRE GAFFE AUX .pop '''
    def combat_xVx_avec_capacites_speciales(self,ennemis):
        ''' Créer tous les Anti Passifs... '''
        passifs_debut_de_partie=[Chevalier.chevalerie,Serpent.coupe_feu,Griffon.bouclier_lumiere,Griffon.bouclier_tenebres,LoupGarou.soif_de_sang]
        passifs_fin_de_partie=[Griffon.anti_bouclier_tenebres,Griffon.anti_bouclier_lumiere]
        
        if(self.membres[0].presence_leader_skill == 1):
            self.membres[0].leader_skill(self)
        if(ennemis.membres[0].presence_leader_skill == 1):
            ennemis.membres[0].leader_skill(ennemis)
        
        ''' Pour l'instant, aucun passif_2 dans les passifs de début de partie '''
        for index in range(self.len):
            if(self.membres[index].presence_passif_1 == 1):
                if(self.membres[index].passif_1 in passifs_debut_de_partie):
                    self.membres[index].passif_1()

        for index in range(ennemis.len):
            if(ennemis.membres[index].presence_passif_1==1):
               if(ennemis.membres[index].passif_1 in passifs_debut_de_partie):
                    ennemis.membres[index].passif_1()

        persos=self.membres + ennemis.membres
        index=0
        while(index < len(persos)):
            # len(persos) peut être modifié par les .pop
            if(index < len(persos) and persos[index] == 0):
                persos.pop(index)
                index-=1
            index+=1


        while(not self.fin_du_combat(ennemis)):
            while(not self.un_perso_doit_jouer() and not ennemis.un_perso_doit_jouer()):
                self.tick()
                ennemis.tick()
            while((self.un_perso_doit_jouer() or ennemis.un_perso_doit_jouer()) and not self.fin_du_combat(ennemis)):
                for index_persos in range(len(persos)):
                    if(persos[index_persos].jauge_attaque >= 100 and not self.fin_du_combat(ennemis)):
                        print('***** Recapitulatif *****')
                        for index in range(self.len):
                            print(persos[index].surnom,persos[index].attribut,' : ',persos[index].pv_actuels,'PV sur',persos[index].pv_max_donjons)
                            print('Jauge d\'attaque : ',persos[index].jauge_attaque)
                        print('*************************')
                        print('\n')
                        print('*************************')
                        for index_ennemis in range(ennemis.len):
                            print(persos[index+index_ennemis+1].surnom,persos[index+index_ennemis+1].attribut,' : ',persos[index+index_ennemis+1].pv_actuels,'PV sur',persos[index+index_ennemis+1].pv_max_donjons)
                            print('Jauge d\'attaque : ',persos[index+index_ennemis+1].jauge_attaque)
                        print('*************************')
                        print('\n')
                        
                        '''
                        if(allies.membre_2.pv_actuels<=0 and (allies.membre_2 not in allies_morts)):
                            allies_morts.append(allies.membre_2)
                        if(allies.membre_1.pv_actuels<=0 and (allies.membre_1 not in allies_morts)):
                            allies_morts.append(allies.membre_1)
                        if(allies.leader.pv_actuels<=0 and (allies.leader not in allies_morts)):
                            allies_morts.append(allies.leader)
                            
                        if(ennemis.membre_2.pv_actuels<=0 and (ennemis.membre_2 not in ennemis_morts)):
                            ennemis_morts.append(ennemis.membre_2)
                        if(ennemis.membre_1.pv_actuels<=0 and (ennemis.membre_1 not in ennemis_morts)):
                            ennemis_morts.append(ennemis.membre_1)
                        if(ennemis.leader.pv_actuels<=0 and (ennemis.leader not in ennemis_morts)):
                            ennemis_morts.append(ennemis.leader)
                        '''

                        # PAS DE COMPARAISON DES STATS DE VITESSSE POUR DECIDER WTF 
                        
                        jauge_max=persos[0].jauge_attaque
                        vitesse_actuelle_max = persos[0].vitesse_actuelle
                        indice_du_max=0
                        for index in range(len(persos)):
                            if(persos[index].jauge_attaque > jauge_max or (persos[index].jauge_attaque == jauge_max and persos[index].vitesse_actuelle > vitesse_actuelle_max)):
                                jauge_max=persos[index].jauge_attaque
                                vitesse_actuelle_max = persos[index].vitesse_actuelle
                                indice_du_max=index
                        if(indice_du_max <= self.len-1):
                            # retour_action=Monstre.action_allies(persos[indice_du_max],allies,ennemis,allies_morts,ennemis_morts)
                            persos[indice_du_max].action_allies(self,ennemis)
                        else:
                            # retour_action=Monstre.action_ennemis(persos[indice_du_max],allies,ennemis,allies_morts,ennemis_morts)
                            persos[indice_du_max].action_ennemis(self,ennemis)
                        '''
                        allies_morts=retour_action[0]
                        ennemis_morts=retour_action[1]
                        '''
                        persos[indice_du_max].tour_supplementaire_tmp=0
                        self.tick()
                        ennemis.tick()
                        
                        # str(input(' > '))

            if(self.fin_du_combat(ennemis)):
                dimensions_fenetre = [2*617,480]
                fenetre = pygame.display.set_mode((dimensions_fenetre[0], dimensions_fenetre[1]))
                pygame.display.flip()
                pygame.quit()
                # FERMER LA FENETRE car sinon rien ne le fait pour nous !!!
                print('Le combat est terminé. \n\n')
        if(self.is_alive()):
            vainqueur='allies'
        else:
            vainqueur='ennemis'

        if(self.membres[0].presence_leader_skill == 1):
            self.membres[0].anti_leader_skill(self)
        if(ennemis.membres[0].presence_leader_skill == 1):
            ennemis.membres[0].anti_leader_skill(ennemis)

        ''' Pour l'instant, aucun passif_2 dans les passifs de fin de partie '''
        for index in range(self.len):
            if(self.membres[index].presence_passif_1 == 1):
                if(self.membres[index].passif_1 in passifs_fin_de_partie):
                    self.membres[index].passif_1()
        
        for index in range(ennemis.len):
            if(ennemis.membres[index].presence_passif_1 == 1):
                if(ennemis.membres[index].passif_1 in passifs_fin_de_partie):
                    ennemis.membres[index].passif_1()

        print('Le vainqueur est : ',vainqueur,'!! \n\n')
        str(input(' > '))
        return vainqueur





























    # Sert à reset un monstre dans server.py
    # On ne peut pas importer Monsters dans Server...
    # Sinon les import bouclent et ça casse tout
    def reset_equipe(self, nom_monstre_a_reset):
        return Monstre.reset_monstre(nom_monstre_a_reset)
            







    '''
                Ce qu'on veut faire :
        
        0)  Le serveur se met en attente d'une connexion client

        1)  Le client initie la connexion en envoyant son premier monstre
            Le serveur lui répond en lui envoyant son premmier monstre 
            On recommence jusqu'à ce que le client et le serveur aient envoyé leurs trois monstres
            Puis on ferme la connexion
        
        2)  On rouvre les deux connexions et on écoute
            Le joueur au monstre le plus rapide va commencer à jouer
            Il va envoyer un message à l'autre joueur pour lui indiquer 
                le choix de sa capacité et de sa cible si besoin
            Cela va réveiller l'autre joueur, le faire se synchroniser dans le jeu
            Puis on remet les deux joueurs en attente et on recommence
    '''

    #                       PROBLEME HYPER IMPORTANT
    
    #               Si un coup critique survient chez l'un des joueurs et pas chez l'autre ???
    
    # Si statut == client, c'est à nous d'initialiser la communication vers le serveur 
    # Sinon si statut == serveur, on n'a qu'à attendre la connexion du client :)
    def combat_multijoueurs(self, game, statut):
        # print("Statut dans Teams : " + statut)
        partie_tmp = game
        resultat = init_team_ennemie(self,statut)
        # print("FIN DE L INITIALISATION !!!! \n")
        # print(resultat)
        adresse_joueur = resultat[0]
        ennemis = Equipe(partie_tmp, resultat[1], len(resultat[1]))

        for index in range(ennemis.len):
            ennemis.membres[index].preparer_au_combat()
        for index in range(self.len):
            self.membres[index].preparer_au_combat()

        passifs_debut_de_partie=[Chevalier.chevalerie,Serpent.coupe_feu,Griffon.bouclier_lumiere,Griffon.bouclier_tenebres,LoupGarou.soif_de_sang]
        passifs_fin_de_partie=[Griffon.anti_bouclier_tenebres,Griffon.anti_bouclier_lumiere]
        
        if(self.membres[0].presence_leader_skill == 1):
            self.membres[0].leader_skill(self)
        if(ennemis.membres[0].presence_leader_skill == 1):
            ennemis.membres[0].leader_skill(ennemis)
        
        ''' Pour l'instant, aucun passif_2 dans les passifs de début de partie '''
        for index in range(self.len):
            if(self.membres[index].presence_passif_1 == 1):
                if(self.membres[index].passif_1 in passifs_debut_de_partie):
                    self.membres[index].passif_1()

        for index in range(ennemis.len):
            if(ennemis.membres[index].presence_passif_1==1):
               if(ennemis.membres[index].passif_1 in passifs_debut_de_partie):
                    ennemis.membres[index].passif_1()

        persos=self.membres + ennemis.membres
        index=0
        while(index < len(persos)):
            # len(persos) peut être modifié par les .pop
            if(index < len(persos) and persos[index] == 0):
                persos.pop(index)
                index-=1
            index+=1


        while(not self.fin_du_combat(ennemis)):
            while(not self.un_perso_doit_jouer() and not ennemis.un_perso_doit_jouer()):
                self.tick()
                ennemis.tick()
            while((self.un_perso_doit_jouer() or ennemis.un_perso_doit_jouer()) and not self.fin_du_combat(ennemis)):
                for index_persos in range(len(persos)):
                    if(persos[index_persos].jauge_attaque >= 100 and not self.fin_du_combat(ennemis)):
                        print('***** Recapitulatif *****')
                        for index in range(self.len):
                            print(persos[index].surnom,persos[index].attribut,' : ',persos[index].pv_actuels,'PV sur',persos[index].pv_max_donjons)
                            print('Jauge d\'attaque : ',persos[index].jauge_attaque)
                        print('*************************')
                        print('\n')
                        print('*************************')
                        for index_ennemis in range(ennemis.len):
                            print(persos[index+index_ennemis+1].surnom,persos[index+index_ennemis+1].attribut,' : ',persos[index+index_ennemis+1].pv_actuels,'PV sur',persos[index+index_ennemis+1].pv_max_donjons)
                            print('Jauge d\'attaque : ',persos[index+index_ennemis+1].jauge_attaque)
                        print('*************************')
                        print('\n')

                        # PAS DE COMPARAISON DES STATS DE VITESSSE POUR DECIDER WTF 
                        
                        vitesse_actuelle_max = persos[0].vitesse_actuelle
                        jauge_max = persos[0].jauge_attaque
                        indice_du_max = 0
                        for index in range(len(persos)):
                            if(persos[index].jauge_attaque > jauge_max or (persos[index].jauge_attaque == jauge_max and persos[index].vitesse_actuelle > vitesse_actuelle_max) or (persos[index].jauge_attaque == jauge_max and persos[index].vitesse_actuelle == vitesse_actuelle_max and index > self.len-1 and statut == 'client') or (persos[index].jauge_attaque == jauge_max and persos[index].vitesse_actuelle == vitesse_actuelle_max and index <= self.len-1 and statut == 'serveur')):
                                # print("\n A l'index " + str(index) + " : " + persos[index].nom + " a une jauge d'attaque de " + str(persos[index].jauge_attaque) + " ce qui est > " + str(jauge_max) + " (jauge max).")
                                jauge_max = persos[index].jauge_attaque
                                vitesse_actuelle_max = persos[index].vitesse_actuelle
                                indice_du_max = index
                        
                        # persos = self.membres + ennemis.membres
                        # Pour le serveur : serveur.equipe + client.equipe    délimité par serveur.equipe.len-1
                        # Pour le client : client.equipe + serveur.equipe     délimité par client.equipe.len-1
                        # print("Persos : ")
                        # print(persos)
                        # print("\n\n Indice du max : " + str(indice_du_max) + "\n\n")
                        

                        if (statut == 'client'):
                            if (indice_du_max <= self.len-1):
                                persos[indice_du_max].action_allies_multijoueur(self, ennemis, statut, 'client',adresse_joueur)
                            else:
                                persos[indice_du_max].action_allies_multijoueur(ennemis, self, statut, 'serveur',adresse_joueur)
                        elif (statut == 'serveur'):
                            if (indice_du_max <= self.len-1):
                                persos[indice_du_max].action_allies_multijoueur(self, ennemis, statut, 'client',adresse_joueur)
                            else:
                                persos[indice_du_max].action_allies_multijoueur(ennemis, self, statut, 'serveur',adresse_joueur)

                        '''
                        if(indice_du_max <= self.len-1):
                            if (statut == 'serveur'):
                                persos[indice_du_max].action_allies_multijoueur(self, ennemis, statut, 'client',adresse_joueur)
                            elif (statut == 'client'):
                                persos[indice_du_max].action_allies_multijoueur(ennemis, self, statut, 'serveur',adresse_joueur)
                                # persos[indice_du_max].action_allies_multijoueur(self, ennemis, statut, 'serveur',adresse_joueur)
                        else:
                            # A ré inverser si ça marche pas 
                            if (statut == 'serveur'):
                                persos[indice_du_max].action_allies_multijoueur(ennemis, self, statut, 'serveur',adresse_joueur)
                                # persos[indice_du_max].action_allies_multijoueur(self, ennemis, statut, 'serveur',adresse_joueur)
                            elif (statut == 'client'):
                        '''     
    
                        persos[indice_du_max].tour_supplementaire_tmp=0
                        self.tick()
                        ennemis.tick()
                        
                        # str(input(' > '))

            if(self.fin_du_combat(ennemis)):
                print('Le combat est terminé. \n\n')
        if(self.is_alive()):
            vainqueur='allies'
        else:
            vainqueur='ennemis'

        if(self.membres[0].presence_leader_skill == 1):
            self.membres[0].anti_leader_skill(self)
        if(ennemis.membres[0].presence_leader_skill == 1):
            ennemis.membres[0].anti_leader_skill(ennemis)

        ''' Pour l'instant, aucun passif_2 dans les passifs de fin de partie '''
        for index in range(self.len):
            if(self.membres[index].presence_passif_1 == 1):
                if(self.membres[index].passif_1 in passifs_fin_de_partie):
                    self.membres[index].passif_1()
        
        for index in range(ennemis.len):
            if(ennemis.membres[index].presence_passif_1 == 1):
                if(ennemis.membres[index].passif_1 in passifs_fin_de_partie):
                    ennemis.membres[index].passif_1()


        print('Le vainqueur est : ',vainqueur,'!! \n\n')
        str(input(' > '))
        return vainqueur







# base=Base()

''' Les attributs possibles pour les Slime sont Feu, Eau et Vent '''
'''
fireSlime=Slime()
while(fireSlime.attribut!='Feu'):
    fireSlime=Slime()
fireSlime.indice_stockage_base=1
    
iceSlime=Slime()
while(iceSlime.attribut!='Eau'):
    iceSlime=Slime()
iceSlime.indice_stockage_base=2
    
windSlime=Slime()
while(windSlime.attribut!='Vent'):
    windSlime=Slime()
windSlime.indice_stockage_base=3

redSlime=Slime()
while(redSlime.attribut!='Feu'):
    redSlime=Slime()
redSlime.indice_stockage_base=4
redSlime.niveau=2
redSlime.XP_avant_prochain_niveau=200

base.stockage[1]=fireSlime
base.stockage[2]=iceSlime
base.stockage[3]=windSlime
base.stockage[4]=redSlime
base.place_dernier_monstre=4

equipe=Equipe(fireSlime,iceSlime,windSlime)
Equipe.afficher_partiellement(equipe)
print('\n\n')

Equipe.supprimer_monstre(base,equipe,0)
Equipe.afficher_partiellement(equipe)
print('\n\n')

Equipe.ajouter(base,equipe)
print('\n\n')
Equipe.modifier_alignement(base,equipe)
Equipe.afficher(equipe)
print('\n\n')

Equipe.modifier(base,equipe)
print('\n\n\n\n')

Equipe.supprimer_monstre(base,equipe,1)
Equipe.ajouter(base,equipe)
print('\n\n')

Equipe.supprimer_monstre(base,equipe,2)
Equipe.ajouter(base,equipe)
print('\n\n\n\n')
Equipe.afficher(equipe)
print('\n\n\n\n Fin Algo \n\n')
'''
