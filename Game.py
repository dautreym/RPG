# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:41:34 2019

@author: marin
"""


import sys
import random
import math
from ast import literal_eval

import pickle

from Inventory import *
from Dungeon import *
from Teams import *
from Monsters import Security

'''
from Dungeon import *
from Functions import *
from Inventory_and_Teams import *
from Monsters import *
from Runes_and_Objects import *
'''


# Problèmes à régler :
# 1) Pour les capacités des monstres : beaucoup de choses à modifier
#       Corriger les aptitudes leader, anti_aptitudes_leader et leurs affichages
#           Bien faire les Arrondir.a_l_unite() partout
#       Tester à nouveau les capacités de tous les monstres avec un Main_test.py

# 2) Rajouter des graphismes :
#       Regarder les applications offertes par les bibliothèques suivantes :
#           Pygame, Pyglet, Cocos2d, PySFML 


class Game:
    def __init__(self,sac_donne):
        self.nom_fichier_sauvegarde="SAVE.txt"
        self.stockage=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.place_dernier_monstre=0
        self.sac=sac_donne
        self.donjons_possibles=[ForetVeur(),CratereAter(),MontTagne(),RuinesSenzargen()]
        # Variable initialisée au moment du choix du donjon et de son niveau  
        self.donjon=[] # Donjon choisi temporairement 
        self.niveau_donjon=[] # Niveau du donjon (aussi un donjon) choisi temporairement 
        self.choix_map=-1
        
        self.niveaux_donjons_debloques=[1]
        self.donjons_dispo=[ForetVeur()]
        self.noms_donjons_dispo=['Forêt Veur']
        # A COMPLETER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
        self.monstres_dispo_une_etoile_nom=['Slime','GardienForet','Champignon','Spectre','Canniboite','Crapoxique','Sacasable','BasElementaire']
        self.monstres_dispo_deux_etoiles_nom=['Sanglier','PlanteCarnivore','BoiteDePandore','SoldatSquelette','ChauveSouris','Scorpion','Imp','Lutin','Yeti','Cerbere','OursDeGuerre','Elementaire','Garuda','Harpie','Salamandre','Esprit','Viking','Chevalier']
        self.monstres_dispo_trois_etoiles_nom=['Fee','DameHarpie','Inugami','Mastodonte','Golem','Serpent','Griffon','Inferno','HautElementaire','OursDeCombat','LoupGarou','Elfe']
        self.monstres_dispo_quatre_etoiles_nom=['Vampire','Elfe','ChevalierMagique']
        self.monstres_dispo_cinq_etoiles_nom=['Vampire','Phénix']
        self.recompenses_donnees=[0,0,0,0]

        self.recompenses_globales=[Elfe(),[Fee(),Fee()],ChevalierMagique(),Vampire()]
        while(self.recompenses_globales[0].attribut != 'Lumière'):
            self.recompenses_globales[0]=Elfe()
        while(self.recompenses_globales[1][0].attribut != 'Lumière'):
            self.recompenses_globales[1][0]=Fee()
        while(self.recompenses_globales[1][1].attribut != 'Ténèbres'):
            self.recompenses_globales[1][1]=Fee()
        while(self.recompenses_globales[2].attribut != 'Eau'):
            self.recompenses_globales[2]=ChevalierMagique()
        while(self.recompenses_globales[3].attribut != 'Feu'):
            self.recompenses_globales[3]=Vampire()

        self.types_recompenses_globales=['Monstre','Monstres','Monstre','Monstre'] # A CHANGER EN monstreS
        
        self.recompenses_globales_totales=[self.recompenses_donnees,self.recompenses_globales,self.types_recompenses_globales]


    def est_full_stockage(self):
        if (self.place_dernier_monstre==99):
            fullBase=True
        else:
            fullBase=False
        return fullBase

    def ajouter_monstre(self,monstre):
        if (self.est_full_stockage()==False):
            if(monstre.indice_stockage_base==999):
                self.stockage[self.place_dernier_monstre+1]=monstre
                self.place_dernier_monstre+=1
                monstre.indice_stockage_base=self.place_dernier_monstre
            else:
                self.stockage[monstre.indice_stockage_base]=monstre
        else:
            print('Dommage!! La base est pleine... \n')

    
    '''
    def rafraichir_equipe(self,equipe):
         Enlève de l'équipe tous les monstres dont l'indice de stockage est 999 = OUT_OF_STOCKAGE 
         Réactualise les autres à partir des monstres stockés dans la base 

    def rafraichir_stockage(self,equipe):
         Enlève du stockage tous les monstres dont l'indice de stockage est OUT_OF_STOCKAGE = 999 
         Réactualise les autres à partir des monstres présents dans l'équipe 
    '''

    def renommer_monstre(self,indice):
        print('Quel nom voulez-vous donner à votre ',(self.stockage[indice]).nom,(self.stockage[indice]).attribut,' ?')
        entree=input('Nom à donner : ')
        while(not Security.is_string(entree)):
            entree=input('Nom à donner : ')
        surnom_donne=str(entree)
        (self.stockage[indice]).surnom=surnom_donne
        print('\nParfait!!')
        print((self.stockage[indice]).nom,(self.stockage[indice]).attribut,' s\'appellera désormais : ',(self.stockage[indice]).surnom,'!!\n')
        

    def afficher_monstres(self):
        print('\n')
        i=1
        while(self.stockage[i]!=0):
            print('Monstre à l emplacement ',i,' : ')
            print(self.stockage[i],'\n')
            i+=1
        print('\n\n')

    def afficher_partiellement_monstres(self):
        print('\n')
        i=1
        while(self.stockage[i]!=0):
            print('Vous avez le monstre ',self.stockage[i].surnom,'(',self.stockage[i].nom,'de',self.stockage[i].attribut,self.stockage[i].classe,' étoiles) niveau ',self.stockage[i].niveau,'à l\'emplacement ',i)
            i+=1
        print('\n\n')


    def invoquer_sans_affichage(self,classe):
        if(classe==1):
            nom_creature=self.monstres_dispo_une_etoile_nom[random.randint(0,len(self.monstres_dispo_une_etoile_nom)-1)]
        elif(classe==2):
            nom_creature=self.monstres_dispo_deux_etoiles_nom[random.randint(0,len(self.monstres_dispo_deux_etoiles_nom)-1)]
        elif(classe==3):
            nom_creature=self.monstres_dispo_trois_etoiles_nom[random.randint(0,len(self.monstres_dispo_trois_etoiles_nom)-1)]
        elif(classe==4):
            nom_creature=self.monstres_dispo_quatre_etoiles_nom[random.randint(0,len(self.monstres_dispo_quatre_etoiles_nom)-1)]
        elif(classe==5):
            nom_creature=self.monstres_dispo_cinq_etoiles_nom[random.randint(0,len(self.monstres_dispo_cinq_etoiles_nom)-1)]

        creature=Monstre.reset_monstre(nom_creature)
        while(creature.classe!=classe):
            creature=self.invoquer_sans_affichage(classe)
        return creature

    def invoquer(self,classe):
        creature=self.invoquer_sans_affichage(classe)
        print('Félicitations!! Vous avez invoqué un(e) ',creature.nom,'!! \n')
        print(creature,'\n\n')
        str(input(' > '))
        return creature

    def invoquer_defini(self,nom_monstre,attribut):
        monstre=Monstre.reset_monstre(nom_monstre)
        while(monstre.attribut!=attribut):
            monstre=Monstre.reset_monstre(nom_monstre)
        self.ajouter_monstre(monstre)
        print('Félicitations!! Vous avez invoqué un(e) ',monstre.nom,'!! \n')
        print(monstre,'\n\n')
        return monstre


    def desequiper(self):
        print('\nLa rune déséquipée retournera dans la partie équipement du sac, sauf si celui est plein, auquel cas elle sera jetée.\n')
        possibilites_monstres=[]
        possibilites_runes=[]
        index=1
        while(index <= self.place_dernier_monstre):
            print(self.stockage[index],' = ',index,'\n')
            possibilites_monstres.append(index)
            index+=1

        entree=input('De quel monstre voulez-vous modifier l\'équipement ? ')
        while(not Security.is_decimal(entree)):
            entree=input('De quel monstre voulez-vous modifier l\'équipement ? ')
        place_monstre_choisi=int(entree)
        while(place_monstre_choisi not in possibilites_monstres):
            entree=input('De quel monstre voulez-vous modifier l\'équipement ? ')
            while(not Security.is_decimal(entree)):
                entree=input('De quel monstre voulez-vous modifier l\'équipement ? ')
            place_monstre_choisi=int(entree)
        monstre_choisi=self.stockage[place_monstre_choisi]

        monstre_choisi.malus_famille_de_runes()

        print('\n\n')
        positions_a_afficher=['haut','haut à droite','bas à droite','bas','bas à gauche','haut à gauche']
        for index in range(len(monstre_choisi.equipement)):
            if(monstre_choisi.equipement[index]!=0):
                print('La rune en ',positions_a_afficher[index],' de ',monstre_choisi.surnom,' est : \n',monstre_choisi.equipement[index],'\n Pour la déséquiper, rentrez ',index,' \n')
                possibilites_runes.append(index)

        if(len(possibilites_runes)==0):
            print('Vous ne pouvez déséquiper aucune rune car aucune rune n\'est équipée.')
        else:
            entree=input('Quelle rune voulez-vous déséquiper ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Quelle rune voulez-vous déséquiper ? ')
            place_rune_choisie=int(entree)
            while(place_rune_choisie not in possibilites_runes):
                entree=input('Quelle rune voulez-vous déséquiper ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('Quelle rune voulez-vous déséquiper ? ')
                place_rune_choisie=int(entree)
            
        rune_supprimee=monstre_choisi.equipement[place_rune_choisie]
        if(rune_supprimee != 0):
            for index in range(len(rune_supprimee.gains)):
                monstre_choisi.bonus_de_runes[index] -= rune_supprimee.gains[index]
            monstre_choisi.equipement[place_rune_choisie]=0
            self.sac.ajouter_objet(rune_supprimee)

        monstre_choisi.bonus_famille_de_runes()

        for index in range(len(monstre_choisi.statistiques)):
            monstre_choisi.statistiques_actuelles[index]=monstre_choisi.statistiques[index]

        monstre_choisi.afficher_equipement_monstre_complet()
        print(monstre_choisi)


    def modifier_equipement(self):
        possibilites_monstres=[]
        possibilites_runes=[]
        index=1
        while(index <= self.place_dernier_monstre):
            print(self.stockage[index],' = ',index,'\n\n')
            possibilites_monstres.append(index)
            index+=1

        entree=input('Quel monstre voulez-vous équiper d\'une rune ? ')
        while(not Security.is_decimal(entree)):
            entree=input('Quel monstre voulez-vous équiper d\'une rune ? ')
        place_monstre_choisi=int(entree)
        while(place_monstre_choisi not in possibilites_monstres):
            entree=input('Quel monstre voulez-vous équiper d\'une rune ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Quel monstre voulez-vous équiper d\'une rune ? ')
            place_monstre_choisi=int(entree)
        monstre_choisi=self.stockage[place_monstre_choisi]

        monstre_choisi.malus_famille_de_runes()

        print('\n\n')
        monstre_choisi.afficher_equipement_monstre_complet()
        print('\n\n')

        index=1
        while(index <= self.sac.place_dernier_equipement):
            self.sac.afficher_contenu_sac_zone_unique('equipement',index)
            possibilites_runes.append(index)
            index+=1
        if(len(possibilites_runes)==0):
            print('Vous n\'avez aucune rune en votre possession pour le moment.\n\n')
        else:
            entree=input('Quelle rune voulez-vous lui équiper ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Quelle rune voulez-vous lui équiper ? ')
            place_rune_choisie=int(entree)
            while(place_rune_choisie not in possibilites_runes):
                entree=input('Quelle rune voulez-vous lui équiper ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('Quelle rune voulez-vous lui équiper ? ')
                place_rune_choisie=int(entree)
            rune_choisie=self.sac.equipement[place_rune_choisie]

            positions=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']
            for index in range(len(monstre_choisi.equipement)):
                if(monstre_choisi.equipement[index] == 0 and rune_choisie.position == positions[index]):
                    rune_choisie.equiper(monstre_choisi)
                elif(rune_choisie.position == positions[index]):
                    print(monstre_choisi.surnom,' est déjà équipé(e) de la rune : \n',monstre_choisi.equipement[index])
                    
            self.sac.supprimer_equipement_sans_affichage(place_rune_choisie)

        monstre_choisi.bonus_famille_de_runes()


        for index in range(len(monstre_choisi.statistiques)):
            monstre_choisi.statistiques_actuelles[index]=monstre_choisi.statistiques[index]

        print(monstre_choisi)









    def rentrer_de_donjon(self,equipe_allies):
        index=0
        while(index < equipe_allies.len):
            if(equipe_allies.membres[index] != 0):
                equipe_allies.membres[index].etat_cap1='dispo'
                equipe_allies.membres[index].attente1=0
                if(equipe_allies.membres[index].nb_capacites >= 2):
                    equipe_allies.membres[index].etat_cap2='dispo'
                    equipe_allies.membres[index].attente2=0
                if(equipe_allies.membres[index].nb_capacites >= 3):
                    equipe_allies.membres[index].etat_cap3='dispo'
                    equipe_allies.membres[index].attente3=0
            index+=1
        equipe_allies.soigner_equipe()
        print('\n\n Vous êtes de retour à la base!!')
        print('Votre équipe reprend des forces... Son état est désormais : \n')
        #Base.rafraichir_equipe(base,equipe_allies)
        equipe_allies.afficher()
        self.possibilites(equipe_allies)





    def debloquer_donjon(self):
        if(self.niveaux_donjons_debloques[self.choix_map] < 7):
            self.niveaux_donjons_debloques[self.choix_map]+=1
        else:
            if(self.niveau_donjon.nom == 'la Forêt Veur Niveau 7 - Clairière ' and 'Cratère Ater' not in self.noms_donjons_dispo):
                self.niveaux_donjons_debloques.append(1)
                self.donjons_dispo.append(CratereAter())
                self.noms_donjons_dispo.append('Cratère Ater')
                print('Une nouvelle zone devient diponible : le Cratère Ater!! \n')
            if(self.niveau_donjon.nom == 'le Cratère Ater Niveau 7 - Caverne des Profondeurs ' and 'Mont Tagne' not in self.noms_donjons_dispo):
                self.niveaux_donjons_debloques.append(1)
                self.donjons_dispo.append(MontTagne())
                self.noms_donjons_dispo.append('Mont Tagne')
                print('Une nouvelle zone devient diponible : le Mont Tagne!! \n')
            if(self.niveau_donjon.nom == 'le Mont Tagne Niveau 7 - Caverne au Sommet ' and 'Ruines de Senzargen' not in self.noms_donjons_dispo):
                self.niveaux_donjons_debloques.append(1)
                self.donjons_dispo.append(RuinesSenzargen())
                self.noms_donjons_dispo.append('Ruines de Senzargen')
                print('Une nouvelle zone devient diponible : les Ruines de Senzargen!! \n')
            if(self.niveau_donjon.nom == 'les Ruines de Senzargen Niveau 7 - Autel Sacrificiel '):
                print('Félicitations!! Vous avez terminé le jeu!! \n')
            str(input(' > '))
        # DEBLOQUER LES DONJONS EN FONCTION DE LA DIFFICULTE DU PRECEDENT



    def combat_donjon(self,equipe_allies):
        self.niveau_donjon.position()
        '''
        equipe_allies_tmp=[equipe_allies.leader]
        if(equipe_allies.membre_1!=0):
            equipe_allies_tmp.append(equipe_allies.membre_1)
        if(equipe_allies.membre_2!=0):
            equipe_allies_tmp.append(equipe_allies.membre_2)
        '''
        
        equipe_ennemis=self.niveau_donjon.monstres_region(self)
        equipe_ennemis.nom_niveau_donjon = self.niveau_donjon.nom
                
        # On réinitialise ici toutes les stats max_donjons 
        # Pas besoin de les modifier dans les Anti
        for index in range(equipe_ennemis.len):
            equipe_ennemis.membres[index].preparer_au_combat()

            # A ENLEVER !!!! Un jour ...
            if(equipe_ennemis.membres[index].nom == 'Sylphe'):
                equipe_ennemis.membres[index] = Sylphe()
                while(equipe_ennemis.membres[index].attribut!='Vent'):
                    equipe_ennemis.membres[index] = Sylphe()
                while(equipe_ennemis.membres[index].niveau!=14):
                    equipe_ennemis.membres[index].monter_en_niveau_sans_affichage()
                equipe_ennemis.membres[index].surnom='Arashi la Tempête'
                equipe_ennemis.membres[index].preparer_au_combat()
            


        # Si ForetVeur Niveau 1, region = 3 mais on prépare quand même au combat 
        if(self.niveau_donjon.region == 1 or (self.niveau_donjon.nom_famille == 'ForetVeur' and self.niveau_donjon.niveau == 1)):
            for index in range(equipe_allies.len):
                equipe_allies.membres[index].preparer_au_combat()


        survivants=equipe_allies.combat_xVx_avec_capacites_speciales(equipe_ennemis)
        equipe_ennemis.soigner_team_ennemie()


        if(survivants=='allies'):
            for index in range(equipe_allies.len):
                equipe_allies.membres[index].jauge_attaque=0
            
            if(self.niveau_donjon.region < 3):
                equipe_allies.soigner_equipe_entre_deux_vagues()
                print('L état de l équipe est désormais : \n')
                equipe_allies.afficher()
                print('\n\n Vous avancez dans ',self.niveau_donjon.nom,'... \n')
                str(input(' > '))
            self.niveau_donjon.region+=1

            if (self.niveau_donjon.region > 3):
                print('Félicitations!! Vous avez terminé ',self.niveau_donjon.nom,'!! \n')
                str(input(' > '))
                for index in range(equipe_allies.len):
                    equipe_allies.membres[index].recevoir_XP(self.niveau_donjon.recompense[0])

                self.sac.recevoir_gold(self.niveau_donjon.recompense[0],equipe_ennemis.len)


                if(self.niveau_donjon.recompense[1][0]=='Parchemin d invocation' or self.niveau_donjon.recompense[1][0]=='Parchemin d invocation superieure' or self.niveau_donjon.recompense[1][0]=='Rune'):
                    recompense_texte=self.niveau_donjon.recompense[1][0]
                    recompense=self.niveau_donjon.recompense[1][1]
                    print('Vous recevez comme récompense : \n')
                    if(recompense_texte=='Rune'):
                        recompense.initialiser()
                        self.sac.ajouter_objet(recompense)
                        print(recompense,'\n')
                    elif(recompense_texte=='Parchemin d invocation' or recompense_texte=='Parchemin d invocation superieure'):
                        print(recompense,recompense_texte,'!! \n')
                        for index in range(recompense):
                            self.sac.ajouter_objet(Objets(recompense_texte))

                elif(self.niveau_donjon.recompense[1][0]=='Mana'):
                    self.sac.mana+=self.niveau_donjon.recompense[1][1]
                    print('Vous recevez comme récompense : \n',self.niveau_donjon.recompense[1][1],' pierres de Mana!! \n')
                    print('Vous avez désormais ',self.sac.mana,' pierres de Mana!! \n\n')

                elif(self.niveau_donjon.recompense[1][0]=='Cristal'):
                    if (self.niveau_donjon.recompense[1][1]==1):
                        self.sac.cristaux+=self.niveau_donjon.recompense[1][1]
                        print('Vous recevez comme récompense : \n',self.niveau_donjon.recompense[1][1],' cristal!! \n')
                        if(self.sac.cristaux > 1):
                            print('Vous avez désormais ',self.sac.cristaux,' cristaux!! \n\n')
                        else:
                            print('Vous avez désormais ',self.sac.cristaux,' cristal!! \n\n')
                    else:
                        self.sac.cristaux+=self.niveau_donjon.recompense[1][1]
                        print('Vous recevez comme récompense : \n',self.niveau_donjon.recompense[1][1],' cristaux!! \n')
                        print('Vous avez désormais ',self.sac.cristaux,' cristaux!! \n\n')
                str(input(' > '))

                self.debloquer_donjon()

                if(self.niveau_donjon.niveau==7):
                    '''[recompenses_donnees,recompenses_globales,types_recompenses_globales]'''
                    if(self.recompenses_globales_totales[0][self.choix_map]==0):
                        print('Vous recevez une récompense exclusive pour avoir terminé ',self.niveau_donjon.nom,'pour la première fois!!')

                        if(self.recompenses_globales_totales[2][self.choix_map]=='Monstre'):
                            print('Vous recevez : \n')
                            #print(recompenses_globales_totales)
                            print(self.recompenses_globales_totales[1][self.choix_map])
                            self.ajouter_monstre(self.recompenses_globales_totales[1][self.choix_map])
                        
                        elif(self.recompenses_globales_totales[2][self.choix_map]=='Monstres'):
                            for index in range(len(self.recompenses_globales_totales[1][self.choix_map])):
                                print('Vous recevez : \n')
                                str(input(' > '))
                                print(self.recompenses_globales_totales[1][self.choix_map][index])
                                self.ajouter_monstre(self.recompenses_globales_totales[1][self.choix_map][index])
                        
                        elif(self.recompenses_globales_totales[2][self.choix_map]=='Runes'):
                            for index in range(len(self.recompenses_globales_totales[1][self.choix_map])):
                                print('Vous recevez : \n')
                                str(input(' > '))
                                print(self.recompenses_globales_totales[1][self.choix_map][index])
                                self.sac.ajouter_objet(self.recompenses_globales_totales[1][self.choix_map][index])
                        
                        str(input(' > '))
                        self.recompenses_globales_totales[0][self.choix_map]=1

                self.rentrer_de_donjon(equipe_allies)
            else:
                self.combat_donjon(equipe_allies)
        else:
            ''' FAIRE UNE RECOMPENSE PARTIELLE EN XP ET EN MANA '''
            print('Vous avez perdu... \n\n\n\n')
            equipe_ennemis.soigner_team_ennemie()

            '''
            equipe_allies=[allie1]
            if(allie2!=0):
                equipe_allies.append(allie2)
            if(allie3!=0):
                equipe_allies.append(allie3)
            '''
            self.rentrer_de_donjon(equipe_allies)












    def debut(self):
        print('\n\n')
        print('Bienvenu, cher invocateur!! Vous avez été appelé en ce monde pour le sauver d un grave danger qui le menace...')
        print('Pour vous défendre et nous protéger, vous seul pouvez faire appel à vos fidèles créatures pour repousser les monstres ennemis!!')
        print('Mais on dirait que vous n en n\'avez pas encore... Allons en invoquer!! \n\n')
        str(input(' > '))
        monstre2=self.invoquer_defini('Cerbere','Feu')
        str(input(' > '))
        monstre1=self.invoquer_defini('Fee','Eau')
        str(input(' > '))
        monstre3=self.invoquer_defini('Chevalier','Vent')
        str(input(' > '))
        # TEAM DE L ADMIN = A NE PAS MODIFIER!!!!!!!!!!

        #monstreX=self.invoquer_defini('ChevalierDragon','Eau')
        #monstreY=self.invoquer_defini(ChevalierDragon','Feu')
        #monstre1=self.invoquer_defini('Phenix','Feu')
        #monstre2=self.invoquer_defini('Phenix','Vent')
        #monstre3=self.invoquer_defini('Phenix','Eau')

        print('\n Bien!! Maintenant, il est temps de vous constituer une équipe!!')
        equipe_1=Equipe(self,[monstre1,monstre2,monstre3],3)
        #self.rafraichir_equipe(equipe_1)
        equipe_1.afficher_partiellement()
        print('\n Parfait!! Je vous laisse désormais remplir votre rôle de héros!! \n\n')
        str(input(' > '))
        return equipe_1
        
        
    def possibilites(self,equipe_1):
        menu=['Invoquer','Améliorer ou faire Evoluer un monstre','Partir à l\'aventure','Evaluer le mana et autres pierres transportées','Examiner ou modifier l\'équipe','Améliorer, examiner ou modifier l\'équipement','Accéder aux statistiques des créatures possédées','Ouvrir le sac','Accéder au magasin','En savoir plus sur les Relations Elémentaires','En savoir plus sur les Runes','Sauvegarder et Quitter']

        print('Vous pouvez choisir parmi les options suivantes : ')
        options_possibilites=[]
        for index in range(len(menu)):
            print(index,' : ',menu[index])
            options_possibilites.append(index)

        entree=input('\n Que voulez-vous faire ? ')
        while(not Security.is_decimal(entree)):
            entree=input('\n Que voulez-vous faire ? ')
        choix=int(entree)
        while(choix not in options_possibilites):
            entree=input('\n Que voulez-vous faire ? ')
            while(not Security.is_decimal(entree)):
                entree=input('\n Que voulez-vous faire ? ')
            choix=int(entree)

        if (choix == 0):
            if(self.sac.place_dernier_objet_courant==0):
                print('\n Vous n\'avez plus de parchemins d\'invocation... \n')
            else:
                possibilites_invocation=[0]
                print('\n Quitter = 0 \n')
                index=1
                while(index <= self.sac.place_dernier_objet_courant):
                    self.sac.afficher_contenu_sac_zone_unique('objets_courants',index)
                    possibilites_invocation.append(index)
                    index+=1

                entree=input('Quel parchemin voulez-vous utiliser pour votre invocation ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('Quel parchemin voulez-vous utiliser pour votre invocation ? ')
                choix_parchemin=int(entree)
                while(choix_parchemin not in possibilites_invocation):
                    entree=input('Quel parchemin voulez-vous utiliser pour votre invocation ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('Quel parchemin voulez-vous utiliser pour votre invocation ? ')
                    choix_parchemin=int(entree)

                if(choix_parchemin != 0):
                    parchemin_a_utiliser=self.sac.objets_courants[choix_parchemin]
                    if(self.sac.mana < parchemin_a_utiliser.prix_d_utilisation):
                        print('Vous n\'avez pas assez de pierres de mana pour réaliser l\'invocation avec ce parchemin.\n\n')
                    else:
                        self.sac.mana-=parchemin_a_utiliser.prix_d_utilisation
                        print('Invocation en cours...\n')
                        str(input(' > '))
                        creature=parchemin_a_utiliser.utiliser(self)
                        self.sac.supprimer_objet_courant_sans_affichage(choix_parchemin)
                        self.ajouter_monstre(creature)
            self.possibilites(equipe_1)

        if(choix == 1):
            print('Pour Améliorer un monste, rentrez 0')
            print('Pour faire Evoluer un monstre, rentrez 1')
            print('Tout autre choix vous renverra au menu principal.')
            entree=input('\nQue voulez-vous faire ? ')
            while(not Security.is_decimal(entree)):
                entree=input('\nQue voulez-vous faire ? ')
            choix_amelioration_ou_evolution=int(entree)

            if (choix_amelioration_ou_evolution==0):
                possibilites_amelioration=[]
                print('\nVoici les monstres que vous pouvez Améliorer : \n')
                index=1
                while(index <= self.place_dernier_monstre):
                    print('Vous avez le monstre ',self.stockage[index].surnom,'de',self.stockage[index].attribut,self.stockage[index].classe,' étoiles niveau ',self.stockage[index].niveau,'à l\'emplacement ',index,'\n')
                    possibilites_amelioration.append(index)
                    index+=1

                entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez Améliorer ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez Améliorer ? ')
                indice_monstre_a_ameliorer=int(entree)
                while(indice_monstre_a_ameliorer not in possibilites_amelioration):
                    entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez Améliorer ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez Améliorer ? ')
                    indice_monstre_a_ameliorer=int(entree)
                equipe_1.ameliorer_monstre(self.stockage[indice_monstre_a_ameliorer])
                # Base.Rafraichir_stockage(self)
                # Base.Rafraichir_equipe(self,equipe_1)
                
            if (choix_amelioration_ou_evolution == 1):
                print('\nVoici les monstres pouvant Evoluer : ')
                possibilites_evolution=[]
                index=1
                while(index <= self.place_dernier_monstre):
                    if((self.stockage[index].niveau_max_de_la_classe_atteint()) and (self.stockage[index].classe < 6)):
                        print('Le monstre ',self.stockage[index].surnom,'de',self.stockage[index].attribut,self.stockage[index].classe,' étoiles niveau ',self.stockage[index].niveau,'à l\'emplacement ',index)
                        possibilites_evolution.append(index)
                    index+=1

                if(len(possibilites_evolution) != 0):
                    entree=input('\nOui = 0 \nNon = 1 \nSouhaitez-vous faire Evoluer l\'un de ces monstre ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nOui = 0 \nNon = 1 \nSouhaitez-vous faire Evoluer l\'un de ces monstres ? ')
                    choix_evolution=int(entree)
                    while(choix_evolution != 0 and choix_evolution != 1):
                        entree=input('Oui = 0 \nNon = 1 \nSouhaitez-vous faire Evoluer l\'un de ces monstre ? ')
                        while(not Security.is_decimal(entree)):
                            entree=input('Oui = 0 \nNon = 1 \nSouhaitez-vous faire Evoluer l\'un de ces monstres ? ')
                        choix_evolution=int(entree)
                    
                    if(choix_evolution==0):
                        entree=input('Quel est l\'emplacement du monstre que vous souhaitez faire Evoluer ? ')
                        while(not Security.is_decimal(entree)):
                            entree=input('Quel est l\'emplacement du monstre que vous souhaitez faire Evoluer ? ')
                        choix_monstre_a_evoluer=int(entree)
                        while(choix_monstre_a_evoluer not in possibilites_evolution):
                            entree=input('Quel est l\'emplacement du monstre que vous souhaitez faire Evoluer ? ')
                            while(not Security.is_decimal(entree)):
                                entree=input('Quel est l\'emplacement du monstre que vous souhaitez faire Evoluer ? ')
                            choix_monstre_a_evoluer=int(entree)
                    
                        print('\n')
                        self.monter_en_classe(equipe_1,self.stockage[choix_monstre_a_evoluer])
                        # Base.Rafraichir_equipe(self,equipe_1)
                
                else:
                    print('Aucun de vos monstres ne peut évoluer pour le moment. \n')
            self.possibilites(equipe_1)

        if (choix == 2):
            possibilites_choix_map=[]
            possibilites_choix_niveau=[]           
            print('\nVoici la liste des lieux accessibles : ')
            for index in range(len(self.noms_donjons_dispo)):
                print(self.noms_donjons_dispo[index],' = ',index)
                possibilites_choix_map.append(index)
            
            entree=input('Quel lieu voulez-vous explorer ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Quel lieu voulez-vous explorer ? ')
            self.choix_map=int(entree)
            while (self.choix_map not in possibilites_choix_map):
                entree=input('Quel lieu voulez-vous explorer ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('Quel lieu voulez-vous explorer ? ')
                self.choix_map=int(entree)
            self.donjon=self.donjons_dispo[self.choix_map]
            
            print('\n\n Voici la liste des niveaux accessibles : ')
            for index in range(self.niveaux_donjons_debloques[self.choix_map]):
                # [index] pour le niveau, [0] pour le nom 
                print((self.donjon.caracteristiques)[index][0],' = ',index)
                possibilites_choix_niveau.append(index)

            entree=input('Quel niveau voulez-vous explorer ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Quel niveau voulez-vous explorer ? ')
            choix_niveau=int(entree)
            while (choix_niveau not in possibilites_choix_niveau):
                entree=input('Quel niveau voulez-vous explorer ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('Quel niveau voulez-vous explorer ? ')
                choix_niveau=int(entree)
             
            self.niveau_donjon=Donjon(self.donjon.caracteristiques[choix_niveau])
            
            print('\n\n Vous entrez dans ',self.niveau_donjon.nom,'... \n\n\n')
            self.combat_donjon(equipe_1)

        if (choix == 3):
            self.sac.afficher_argent()
            self.possibilites(equipe_1)

        if(choix == 4):
            # Base.Rafraichir_equipe(self,equipe_1)
            print('\nVous pouvez choisir parmi les options suivantes : ')
            print('Afficher un résumé de la composition actuelle de l\'équipe = 0')
            print('Afficher entièrement les statistiques de l\'équipe actuelle = 1')
            print('Remplacer un monstre de l\'équipe par un autre = 2')
            print('Ajouter un monstre à l\'équipe = 3')
            print('Modifier l\'alignement de l\'équipe actuelle = 4')
            print('Revenir au menu principal = 5')
            possibilites_choix4=[0,1,2,3,4,5]
            
            entree=input('\nQue voulez-vous choisir ? ')
            while(not Security.is_decimal(entree)):
                entree=input('\nQue voulez-vous choisir ? ')
            choix_equipe=int(entree)
            while(choix_equipe not in possibilites_choix4):
                entree=input('\nQue voulez-vous choisir ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQue voulez-vous choisir ? ')
                choix_equipe=int(entree)
            
            if(choix_equipe == 0):
                equipe_1.afficher_partiellement()
            
            if(choix_equipe == 1):
                equipe_1.afficher()

            if(choix_equipe == 2):
                equipe_1.modifier()

            if(choix_equipe == 3):
                equipe_1.ajouter()

            if(choix_equipe == 4):
                equipe_1.modifier_alignement()
                equipe_1.afficher_partiellement()
            
            print('\n')
            # Base.Rafraichir_equipe(self,equipe_1)
            self.possibilites(equipe_1)

        if(choix == 5):
            print('\nVous pouvez choisir parmi les options suivantes : ')
            print('Afficher l\'intégralité de l\'équipement d un monstre = 0')
            print('Afficher une rune particulière de l\'équipement d\'un monstre = 1')
            print('Equiper une rune à un monstre = 2')
            print('Déséquiper une rune à un monstre = 3')
            print('Améliorer une rune = 4')
            print('Revenir au menu principal = 5')
            possibilites_choix5=[0,1,2,3,4,5]

            entree=input('\nQue voulez-vous choisir ? ')
            while(not Security.is_decimal(entree)):
                entree=input('\nQue voulez-vous choisir ? ')
            choix_equipement=int(entree)
            while(choix_equipement not in possibilites_choix5):
                entree=input('\nQue voulez-vous choisir ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQue voulez-vous choisir ? ')
                choix_equipement=int(entree)

            if(choix_equipement == 0):
                self.afficher_partiellement_monstres()
                entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir l\'équipement détaillé ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir l\'équipement détaillé ? ')
                choix_monstre_equipement_a_montrer_integralement=int(entree)
                while(choix_monstre_equipement_a_montrer_integralement < 1 or choix_monstre_equipement_a_montrer_integralement > self.place_dernier_monstre):
                    entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir l\'équipement détaillé ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('Quel est l\'emplacement du monstre dont vous souhaitez voir l\'équipement détaillé ? ')
                    choix_monstre_equipement_a_montrer_integralement=int(entree)
                self.stockage[choix_monstre_equipement_a_montrer_integralement].afficher_equipement_monstre_complet()

            if(choix_equipement == 1):
                self.afficher_partiellement_monstres()
                entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir une rune particulière ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQuel est l\'emplacement du montre dont vous souhaitez voir une rune particulière ? ')
                choix_monstre_equipement_a_montrer=int(entree)
                while(choix_monstre_equipement_a_montrer < 1 or choix_monstre_equipement_a_montrer > self.place_dernier_monstre):
                    entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir une rune particulière ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir une rune particulière ? ')
                    choix_monstre_equipement_a_montrer=int(entree)

                positions=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']
                positions_a_afficher=['haut','haut à droite','bas à droite','bas','bas à gauche','haut à gauche']
                print('\n')
                for index in range(len(positions_a_afficher)):
                    print('Voir la rune en ',positions_a_afficher[index],' = ',index)
                
                entree=input('\nQue voulez-vous choisir ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQue voulez-vous choisir ? ')
                choix_position_rune_a_montrer=int(entree)
                while(choix_position_rune_a_montrer not in [0,1,2,3,4,5]):
                    entree=input('\nQue voulez-vous choisir ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQue voulez-vous choisir ? ')
                    choix_position_rune_a_montrer=int(entree)
                
                self.stockage[choix_monstre_equipement_a_montrer].afficher_equipement_monstre(positions[choix_position_rune_a_montrer])

            if(choix_equipement == 2):
                self.modifier_equipement()

            if(choix_equipement==3):
                self.desequiper()

            if(choix_equipement == 4):
                self.afficher_partiellement_monstres()

                entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez Améliorer la rune ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQuel est l\'emplacement du montre dont vous souhaitez Améliorer la rune ? ')
                choix_monstre_equipement_a_ameliorer=int(entree)
                while(choix_monstre_equipement_a_ameliorer < 1 or choix_monstre_equipement_a_ameliorer > self.place_dernier_monstre):
                    entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez Améliorer la rune ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez Améliorer la rune ? ')
                    choix_monstre_equipement_a_ameliorer=int(entree)
                
                print('\n')
                self.stockage[choix_monstre_equipement_a_ameliorer].afficher_equipement_monstre_complet()

                positions=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']
                positions_a_afficher=['haut','haut à droite','bas à droite','bas','bas à gauche','haut à gauche']
                print('\n')
                for index in range(len(positions_a_afficher)):
                    print('Améliorer la rune en ',positions_a_afficher[index],' = ',index)

                entree=input('\nQue voulez-vous choisir ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQue voulez-vous choisir ? ')
                choix_position_rune_a_ameliorer=int(entree)
                while(choix_position_rune_a_ameliorer not in [0,1,2,3,4,5]):
                    entree=input('\nQue voulez-vous choisir ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQue voulez-vous choisir ? ')
                    choix_position_rune_a_ameliorer=int(entree)
                
                self.stockage[choix_monstre_equipement_a_ameliorer].malus_famille_de_runes()
                rune_a_ameliorer=self.stockage[choix_monstre_equipement_a_ameliorer].desequiper_sans_affichage(choix_position_rune_a_ameliorer)
                
                if(rune_a_ameliorer == 0):
                    print(self.stockage[choix_monstre_equipement_a_ameliorer].surnom,'n\'est équipé d\'aucune rune à cet emplacement!!\n')
                    self.stockage[choix_monstre_equipement_a_ameliorer].bonus_famille_de_runes()
                elif(self.sac.mana < rune_a_ameliorer.cout_prochaine_amelioration):
                    print('Vous n\'avez pas assez de pierres de mana pour améliorer cette rune (',self.sac.mana,' possédées, ',rune_a_ameliorer.cout_prochaine_amelioration,'requises)\n')
                    self.stockage[choix_monstre_equipement_a_ameliorer].bonus_famille_de_runes()
                else:
                    print('Coût : ',rune_a_ameliorer.cout_prochaine_amelioration,'\n')
                    self.sac.mana -= rune_a_ameliorer.cout_prochaine_amelioration
                    rune_a_ameliorer.cout_prochaine_amelioration=rune_a_ameliorer.trouver_cout_prochaine_amelioration(rune_a_ameliorer.qualite_numerique,rune_a_ameliorer.niveau)
                    rune_a_ameliorer.ameliorer()
                    rune_a_ameliorer.equiper_sans_affichage(self.stockage[choix_monstre_equipement_a_ameliorer],choix_position_rune_a_ameliorer)
                    self.stockage[choix_monstre_equipement_a_ameliorer].bonus_famille_de_runes()

                    for index in range(len(self.stockage[choix_monstre_equipement_a_ameliorer].statistiques_actuelles)):
                        self.stockage[choix_monstre_equipement_a_ameliorer].statistiques_actuelles[index]=self.stockage[choix_monstre_equipement_a_ameliorer].statistiques[index]

                    print('Le monstre équipé devient : \n',self.stockage[choix_monstre_equipement_a_ameliorer],'\n')

            # Base.Rafraichir_equipe(self,equipe_1)
            print('\n')

            self.possibilites(equipe_1)

        if(choix == 6):
            print('\nVoici l\'ensemble des monstres que vous avez en votre possession : \n')
            self.afficher_partiellement_monstres()
            print('\n')

            entree=input('Oui = 0 \nNon = 1 \nVoulez-vous voir les caractéristiques de l\'un de ces monstres de manière plus détaillée ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Oui = 0 \nNon = 1 \nVoulez-vous voir les caractéristiques de l\'un de ces monstres de manière plus détaillée ? ')
            choix_zoom_caracteristiques=int(entree)
            while(choix_zoom_caracteristiques not in [0,1]):
                entree=input('Oui = 0 \nNon = 1 \nVoulez-vous voir les caractéristiques de l\'un de ces monstres de manière plus détaillée ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('Oui = 0 \nNon =1 \nVoulez-vous voir les caractéristiques de l\'un de ces monstres de manière plus détaillée ? ')
                choix_zoom_caracteristiques=int(entree)

            if(choix_zoom_caracteristiques == 0):
                entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez-voir les caractéristiques ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez-voir les caractéristiques ? ')
                choix_monstre_a_zoomer=int(entree)
                while(choix_monstre_a_zoomer < 1 or choix_monstre_a_zoomer > self.place_dernier_monstre):
                    entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez-voir les caractéristiques ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez-voir les caractéristiques ? ')
                    choix_monstre_a_zoomer=int(entree)
                print('\n\n',self.stockage[choix_monstre_a_zoomer],'\n')

            else:
                entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous relâcher un des monstres que vous possédez ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous relâcher un des monstres que vous possédez ? ')
                choix_relachement=int(entree)
                while(choix_relachement not in [0,1]):
                    entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous relâcher un des monstres que vous possédez ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nOui = 0 \nNon =1 \nVoulez-vous relâcher un des monstres que vous possédez ? ')
                    choix_relachement=int(entree)

                if(choix_relachement == 0):
                    entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez relâcher ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez relâcher ? ')
                    choix_monstre_a_relacher=int(entree)
                    while(choix_monstre_a_relacher < 1 or choix_monstre_a_relacher > self.place_dernier_monstre):
                        entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez relâcher ? ')
                        while(not Security.is_decimal(entree)):
                            entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez relâcher ? ')
                        choix_monstre_a_relacher=int(entree)
                    equipe_1.relacher_monstre(choix_monstre_a_relacher)
                    
                else:
                    entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous renommer un des monstres que vous possédez ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous renommer un des monstres que vous possédez ? ')
                    choix_renommement=int(entree)
                    while(choix_renommement not in [0,1]):
                        entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous renommer un des monstres que vous possédez ? ')
                        while(not Security.is_decimal(entree)):
                            entree=input('\nOui = 0 \nNon =1 \nVoulez-vous renommer un des monstres que vous possédez ? ')
                        choix_renommement=int(entree)
                    
                    if(choix_renommement == 0):
                        entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez renommer ? ')
                        while(not Security.is_decimal(entree)):
                            entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez renommer ? ')
                        choix_monstre_a_renommer=int(entree)
                        while(choix_monstre_a_renommer < 1 or choix_monstre_a_renommer > self.place_dernier_monstre):
                            entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez renommer ? ')
                            while(not Security.is_decimal(entree)):
                                entree=input('\nQuel est l\'emplacement du monstre que vous souhaitez renommer ? ')
                            choix_monstre_a_renommer=int(entree)
                        self.renommer_monstre(choix_monstre_a_renommer)
            print('\n')
            self.possibilites(equipe_1)

        if(choix == 7):
            print('\nVous pouvez choisir parmi les options suivantes : ')
            print('Regarder la place disponible pour les runes et les parchemins = 0')
            print('Afficher tous les parchemins en votre possession = 1')
            print('Afficher toutes les runes en votre possession = 2')
            print('Jeter un parchemin ou une rune = 3')
            print('Pour utiliser un parchemin, allez dans le menu Invoquer depuis le menu principal')
            print('Revenir au menu principal = 4')
            possibilites_choix7=[0,1,2,3,4]

            entree=input('\nQue voulez-vous faire ? ')
            while(not Security.is_decimal(entree)):
                entree=input('\nQue voulez-vous faire ? ')
            choix_menu=int(entree)
            while(choix_menu not in possibilites_choix7):
                entree=input('\nQue voulez-vous faire ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQue voulez-vous faire ? ')
                choix_menu=int(entree)
            
            if(choix_menu == 0):
                print('Il vous reste ',99-self.sac.place_dernier_objet_courant,'emplacements pour les parchemins.')
                print('Il vous reste ',99-self.sac.place_dernier_equipement,'emplacements pour les runes. \n')
            
            if(choix_menu == 1):
                self.sac.afficher_contenu_sac_section('objets_courants')
                print('\n')
            
            if(choix_menu == 2):
                self.sac.afficher_contenu_sac_section('equipement')
                print('\n')
            
            if(choix_menu == 3):
                print('Ne rien jeter = 0 \nJeter un parchemin = 1 \nJeter une rune = 2\n')
                
                entree=input('\nQue voulez-vous faire ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQue voulez-vous faire ? ')
                choix_suppression_a_faire=int(entree)
                while(choix_suppression_a_faire not in [0,1,2]):
                    entree=input('\nQue voulez-vous faire ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQue voulez-vous faire ? ')
                    choix_suppression_a_faire=int(entree)
                
                if(choix_suppression_a_faire == 1):
                    self.sac.supprimer_objet('objets_courants')
                
                if(choix_suppression_a_faire == 2):
                    self.sac.supprimer_objet('equipement')
            self.possibilites(equipe_1)

        if(choix == 8):
            self.sac.magasin() 
            self.possibilites(equipe_1)

        if(choix == 9):
            print('\nLe Feu est supérieur au Vent.')
            print('Le Vent est supérieur à l\'Eau.')
            print('L\'Eau est supérieure au Feu.')
            print('La Lumière est supérieure aux Ténèbres.')
            print('Les Ténèbres sont supérieures à la Lumière.\n')
            print('Lorsqu\'un monstre d\'un certain attribut attaque un monstre d\'un attribut inférieur au sien, les dommages infligés sont démultipliés!!')
            print('A l\'inverse, attaquer un monstre d\'un attribut supérieur peut réduire les dommages infligés.\n')
            print('Exploitez les Relations Elémentaires à votre avantage!! \n\n')
            self.possibilites(equipe_1)

        if(choix == 10):
            print('\nLes runes sont les équipements pour les créatures de ce monde.')
            print('Il existe différentes Catégories de runes : Energie, Colere, Tenace, Veloce,... Et bien d\'autres encore!!\n')
            print('Chaque rune renforce une caractéristique particulière dépendant de la Catégorie dans laquelle elle se trouve. \nPar exemple, les runes de la Catégorie Energie augmentent le maximum de PV de votre créature!!\n')
            print('Chaque rune a une position spécifique dans l\'équipement de la créature. \nElle peut se situer en haut, en haut à droite, en bas à droite, en bas, en bas à gauche ou en haut à gauche.')
            print('A chaque position de son équipement, une créature ne peut s\'équiper que d\'une rune. \nChaque monstre ne peut donc être équipé au maximum que de six runes.\n')
            print('Pour chaque couple de runes de la même Catégorie, la créature peut éventuellement bénéficier d\'un bonus de runes exclusif!!')
            print('Par exemple, équiper deux runes de la Catégorie Energie de positions différentes à une même créature lui octroie un bonus exclusif en points de vie... \nEt ces bonus peuvent être cumulés!!\n')
            print('Parfois, il faut plus qu\'un simple couple de runes pour bénéficier du bonus de runes... \nMais un sextuplet de runes octroie toujours un bonus incroyable!! \nA vous de découvrir lequel!! \n\n')
            self.possibilites(equipe_1)

            ''' Rajouter En savoir plus sur ce monde '''

        if(choix == 11):
            self.ecrire_sauvegarde(equipe_1)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('La sauvegarde a bien été effectuée. \n\n')

            entree=input('\nOui = 0\nNon = 1\nVoulez-vous quitter ? ')
            while(not Security.is_decimal(entree)):
                entree=input('\nOui = 0\nNon = 1\nVoulez-vous quitter ? ')
            choix_menu=int(entree)
            while(choix_menu not in [0,1]):
                entree=input('\nOui = 0\nNon = 1\nVoulez-vous quitter ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nOui = 0\nNon = 1\nVoulez-vous quitter ? ')
                choix_menu=int(entree)
            
            if(choix_menu == 0):
                print("\n\n")
                sys.exit()
            elif(choix_menu == 1):
                print("\n\n\n\n")
                self.possibilites(equipe_1)













    def ecrire_sauvegarde(self, equipe_1):
        dictionnaire_a_sauvegarder = {}
        dictionnaire_a_sauvegarder["equipe"] = equipe_1
        dictionnaire_a_sauvegarder["partie"]=self

        pickle.dump(dictionnaire_a_sauvegarder, open('fichier_de_sauvegarde.pk1','wb'),protocol=pickle.HIGHEST_PROTOCOL)


    def lire_sauvegarde(self, equipe_1):
        dictionnaire_recupere = pickle.load(open('fichier_de_sauvegarde.pk1','rb'))
        self = dictionnaire_recupere["partie"]
        equipe_1 = dictionnaire_recupere["equipe"]
        self.possibilites(equipe_1)















































class Tri:
    def tri_sans_doublons(liste):
        liste_sans_doublons=[]
        for i in range(len(liste)):
            for j in range(len(liste)):
                if ((liste[i]!=liste[j]) and (not liste[j] in liste_sans_doublons)):
                    liste_sans_doublons+=[liste[j]]
        liste_sans_doublons=Tri.tri_ordre_decroissant(liste_sans_doublons)
        return liste_sans_doublons

    def tri_ordre_decroissant(liste):
        for indice_liste in range(len(liste)):
            indice_tmp=indice_liste
            element_liste=liste[indice_tmp]
            while (indice_tmp>0 and element_liste>liste[indice_tmp-1]):
                liste[indice_tmp]=liste[indice_tmp-1]
                indice_tmp-=1
            liste[indice_tmp]=element_liste
        return liste
