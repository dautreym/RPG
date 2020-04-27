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

from Teams import *
from Game import *


'''
import Base
import Dungeon
import Functions
import Inventory_and_Teams
import Monsters
import Runes_and_Objects
'''

# Ce qu'on pourrait faire :
# Dans l'autre fichier : faire from Main import niveaux_donjons_debloques
# Cette variable peut maintenant être accédée de n'importe où en faisant Main.niveaux_donjons_debloques

''' Conventions :
Les classes commencent par des majuscules partout ex. MonsterBase
Les méthodes sont toujours en minuscules avec des underscores ex. est_full_base (même est_full car Base.est_full)
    Exception pour les instances pouvant s'apparenter à des classes comme les Niveaux ou Recompenses
Les instances de classe (objets) commencent par une minuscule et s'ensuivent par des majuscules ex. petitSlime
'''

# A CHANGER (pas ouf comme pattern)
# Fixe tous les random à venir du côté du joueur et du client 
random.seed(42)

sac=Inventaire()
partie=Game(sac)


print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print('0 : Nouvelle partie \n1 : Charger une partie\n')
entree=input('Que voulez-vous faire ? ')
while(not Security.is_decimal(entree)):
    entree=input('\nQue voulez-vous faire ? ')
choix=int(entree)
while(choix != 1 and choix != 0):
    entree=input('\nQue voulez-vous faire ? ')
    while(not Security.is_decimal(entree)):
        entree=input('\nQue voulez-vous faire ? ')
    choix=int(entree)

if(choix == 0):
    equipe_1=partie.debut()

    partie.ecrire_sauvegarde(equipe_1)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    partie.possibilites(equipe_1)


if(choix == 1):
    equipe_1=[]
    partie.lire_sauvegarde(equipe_1)
