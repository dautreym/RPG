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


''' A COMPLETER '''
Monstres_dispo_une_etoile_nom=['Slime','GardienForet','Champignon','Spectre','Canniboite','Crapoxique','Sacasable','BasElementaire']
Monstres_dispo_deux_etoiles_nom=['Sanglier','PlanteCarnivore','BoiteDePandore','SoldatSquelette','ChauveSouris','Scorpion','Imp','Lutin','Yeti','Cerbere','OursDeGuerre','Elementaire','Garuda','Harpie','Salamandre','Esprit','Viking','Chevalier']
Monstres_dispo_trois_etoiles_nom=['Fee','DameHarpie','Inugami','Mastodonte','Golem','Serpent','Griffon','Inferno','HautElementaire','OursDeCombat','LoupGarou','Elfe']
Monstres_dispo_quatre_etoiles_nom=['Vampire','Elfe','ChevalierMagique']
Monstres_dispo_cinq_etoiles_nom=['Vampire','Phénix']


base=Base()
sac=Inventaire()
MAX=999999999
OUT_OF_STOCKAGE=999
Niveaux_donjons_debloques=[1]
all_donjons=[ForetVeur(),CratereAter(),MontTagne(),RuinesSenzargen()]
''' A COMPLETER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! '''
donjons_dispo=[ForetVeur()]
noms_donjons_dispo=['Forêt Veur']


recompenses_donnees=[0,0,0]
recompense_globale_0=Elfe()
while(recompense_globale_0.attribut!='Lumière'):
    recompense_globale_0=Elfe()
recompense_globale_1_1=Fee()
while(recompense_globale_1_1.attribut!='Lumière'):
    recompense_globale_1_1=Fee()
recompense_globale_1_2=Fee()
while(recompense_globale_1_2.attribut!='Ténèbres'):
    recompense_globale_1_2=Fee()
recompense_globale_1=[recompense_globale_1_1,recompense_globale_1_2]
recompense_globale_2=ChevalierMagique()
while(recompense_globale_2.attribut!='Eau'):
    recompense_globale_2=ChevalierMagique()
''' (PRESQUE) TOTALEMENT A CHANGER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! '''
recompenses_globales=[recompense_globale_0,recompense_globale_1,recompense_globale_2]
types_recompenses_globales=['Monstre','Monstres','Monstre'] # A CHANGER EN monstreS

'''
recompense_globale_1=Elfe()
while(recompense_globale_1.attribut!='Lumière'):
    recompense_globale_1=Elfe()
recompense_globale_2_1=Fee()
while(recompense_globale_2_1.attribut!='Lumière'):
    recompense_globale_2_1=Fee()
recompense_globale_2_2=CowGirl()
while(recompense_globale_2_2.attribut!='Ténèbres'):
    recompense_globale_2_2=CowGirl()
recompense_globale_3=ChevalierMagique()
while(recompense_globale_3.attribut!='Eau'):
    recompense_globale_3=ChevalierMagique()

recompenses_globales=[recompense_globale_1,[recompense_globale_2_1,recompense_globale_2_2],recompense_globale_3]
'''
recompenses_globales_totales=[recompenses_donnees,recompenses_globales,types_recompenses_globales]










print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print('0 : Nouvelle partie \n1 : Charger une partie\n')
entree=input('Que voulez-vous faire ? ')
while(not IsSecure(entree)):
    entree=input('\nQue voulez-vous faire ? ')
choix=int(entree)
while(choix != 1 and choix != 0):
    choix=input('\nQue voulez-vous faire ? ')
    while(not IsSecure(entree)):
        entree=input('\nQue voulez-vous faire ? ')
    choix=int(entree)

if(choix==0):
    sac.mana=0
    Niveaux_donjons_debloques=[1]
    donjons_dispo=[ForetVeur()]
    noms_donjons_dispo=['Forêt Veur']
    FirstTeam=Base.debut(base)
    '''
    allie1=Base.invoquerDefini(base,'Sylphide','Feu')
    allie2=Base.invoquerDefini(base,'Sylphide','Eau')
    allie3=Base.invoquerDefini(base,'Sylphide','Vent')
    allie1.surnom='Itachi'
    allie2.surnom='Kisame'
    allie3.surnom='Gaara'
    ennemi1=Base.invoquerDefini(base,'Sylphide','Feu')
    ennemi2=Base.invoquerDefini(base,'Sylphide','Eau')
    ennemi3=Base.invoquerDefini(base,'Sylphide','Vent')
    ennemi1.surnom='Naruto'
    ennemi2.surnom='Sakura'
    ennemi3.surnom='Sasuke'
    FirstTeam=equipe.__init__(allie1,allie2,allie3)
    Ennemis=equipe.__init__(ennemi1,ennemi2,ennemi3)
    for a in range(len(FirstTeam)):
        FirstTeam[a]=Preparer_au_combat(FirstTeam[a])
    for a in range(len(Ennemis)):
        Ennemis[a]=Preparer_au_combat(Ennemis[a])
    Combat_xVx_avec_capacites_speciales(FirstTeam,Ennemis)
    '''

    ecrire_sauvegarde("SAVE",base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)


if(choix==1):
    print("Entrez le nom du fichier (extension comprise)(par défaut SAVE.txt) : ")
    nom_sauvegarde=str(input("> "))
    liste_donnees=lire_sauvegarde(nom_sauvegarde)
    if(liste_donnees==[]):
        print("Fichier de sauvegarde non trouvée")
        sys.exit()
    else:
        donnees_stockage=literal_eval(liste_donnees[0])
        base.stockage=remplir_stockage_base(base.stockage,donnees_stockage)
        sac.mana=literal_eval(liste_donnees[1])
        sac.cristaux=literal_eval(liste_donnees[2])
        sac.pierres_de_fusion=literal_eval(liste_donnees[3])

        sac.equipement[0]='Quitter'
        sac.place_dernier_equipement=0
        for i in range(1,100):
            ''' 100 = len(sac.equipement) = len(sac.objets_courants) '''
            if(literal_eval(liste_donnees[3+i])!=0):
                sac.equipement[i]=Runes.Reinitialiser(literal_eval(liste_donnees[3+i])[0],literal_eval(liste_donnees[3+i])[1],literal_eval(liste_donnees[3+i])[2],literal_eval(liste_donnees[3+i])[3],literal_eval(liste_donnees[3+i])[4],literal_eval(liste_donnees[3+i])[5],literal_eval(liste_donnees[3+i])[6],literal_eval(liste_donnees[3+i])[7],literal_eval(liste_donnees[3+i])[8])
                sac.place_dernier_equipement+=1
            else:
                sac.equipement[i]=0

        sac.objets_courants[0]='Quitter'
        sac.place_dernier_objet_courant=0
        for j in range(i+1,i+99):
            if(literal_eval(liste_donnees[3+j])!=0):
                sac.objets_courants[j-i]=Objets(literal_eval(liste_donnees[3+j]))
                sac.place_dernier_objet_courant+=1
            else:
                sac.objets_courants[j-i]=0

        '''
        FirstTeam=[]
        FirstTeam.append(literal_eval(liste_donnees[j+1]))
        k=j+2
        Prochain indice de literal_eval
        if(len(FirstTeam)>0):
            FirstTeam.append(literal_eval(liste_donnees[j+2]))
            k+=1
        if(len(FirstTeam)>1):
            FirstTeam.append(literal_eval(liste_donnees[j+3]))
            k+=1
        '''
        while(literal_eval(liste_donnees[j+1])==0):
            j+=1
        FirstTeam=[]
        FirstTeam=remplir_team(FirstTeam,literal_eval(liste_donnees[j+1]))
        FirstTeam=Rafraichir_equipe(base,FirstTeam)
        Niveaux_donjons_debloques=literal_eval(liste_donnees[j+2])
        '''
        IMPOSSIBLE DE SAUVGARDER UN DONJON !!!!
        donjons_dispos=literal_eval(liste_donnees[j+3])
        '''
        noms_donjons_dispo=literal_eval(liste_donnees[j+3])
        donjons_dispo=[]
        k=0
        while(k<len(noms_donjons_dispo)):
            donjons_dispo.append(all_donjons[k])
            k+=1
        recompenses_globales_totales=[]
        recompenses_globales_totales.append(literal_eval(liste_donnees[j+4]))
        recompenses_globales_1_tmp=[]
        recompenses_globales_1_1_tmp=[]
        '''
        save_file.write(str(lire_stockage_base([recompenses_globales_totales[1][0]])) + "\n")
        print(recompenses_globales_totales[1][1],'\n\n')
        for k in range(len(recompenses_globales_totales[1][1])):
            save_file.write(str(lire_stockage_base([recompenses_globales_totales[1][1][k]])) + "\n")
        save_file.write(str(lire_stockage_base([recompenses_globales_totales[1][2]])) + "\n")
        save_file.write(str(recompenses_globales_totales[2]) + "\n")
        '''
        #print(liste_donnees[j+5])
        #print(literal_eval(liste_donnees[j+5])[0])
        #print(liste_donnees[j+5][2])
        recompenses_globales_1_tmp=remplir_team(recompenses_globales_1_tmp,literal_eval(liste_donnees[j+5]))
        #print(recompenses_globales_1_tmp,'\n')
        recompenses_globales_1_1_tmp=remplir_team(recompenses_globales_1_1_tmp,literal_eval(liste_donnees[j+6]))
        recompenses_globales_1_1_tmp=remplir_team(recompenses_globales_1_1_tmp,literal_eval(liste_donnees[j+7]))
        recompenses_globales_1_tmp.append(recompenses_globales_1_1_tmp)
        recompenses_globales_1_tmp=remplir_team(recompenses_globales_1_tmp,literal_eval(liste_donnees[j+8]))
        recompenses_globales_totales.append(recompenses_globales_1_tmp)
        recompenses_globales_totales.append(literal_eval(liste_donnees[j+9]))
        #print('Récompenses : \n',recompenses_globales_totales,'\n\n')
        print('\n\n\n\n')
        Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)
