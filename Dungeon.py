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


from Monsters import *
from Runes_and_Objects import *
from Teams import *

'''
from Base import *
from Functions import *
from Inventory_and_Teams import *
from Monsters import *
from Runes_and_Objects import *
'''


class Donjon:
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
        self.demi_boss1=caracteristiques_donjon[9]
        self.demi_boss2=caracteristiques_donjon[10]
        self.boss=caracteristiques_donjon[11]
        self.recompense=caracteristiques_donjon[12]
        self.nom_famille=caracteristiques_donjon[13]
        self.region=1

    def monstres_region(self,game):
        # A COMPLETER AVEC DES ELIF CRATERE ATER...
        if(self.nom=='la Forêt Veur Niveau 1 - Entrée '):
            if (self.region==1):
                self.region+=2
            if (self.region==2):
                self.region+=1
            if (self.region==3):
                equipe_adverse=Equipe(game,[self.monstre1,self.monstre2],2)
        elif(self.nom=='la Forêt Veur Niveau 7 - Clairière '):
            if (self.region==1):
                equipe_adverse=Equipe(game,[self.monstre1,self.demi_boss1,self.monstre2],3)
            if (self.region==2):
                equipe_adverse=Equipe(game,[self.monstre3,self.demi_boss2,self.monstre4],3)
            if (self.region==3):
                equipe_adverse=Equipe(game,[self.boss],1)
        elif(self.nom=='le Mont Tagne Niveau 7 - Caverne au Sommet '):
            if (self.region==1):
                equipe_adverse=Equipe(game,[self.monstre1,self.demi_boss1,self.monstre2],3)
            if (self.region==2):
                equipe_adverse=Equipe(game,[self.monstre3,self.demi_boss2,self.monstre4],3)
            if (self.region==3):
                equipe_adverse=Equipe(game,[self.boss],1)
        elif(self.nom=='le Cratère Ater Niveau 7 - Caverne des Profondeurs '):
            if (self.region==1):
                equipe_adverse=Equipe(game,[self.monstre1,self.demi_boss1,self.monstre2],3)
            if (self.region==2):
                equipe_adverse=Equipe(game,[self.monstre3,self.demi_boss2,self.monstre4],3)
            if (self.region==3):
                equipe_adverse=Equipe(game,[self.boss],1)
        elif(self.nom=='les Ruines de Senzargen Niveau 7 - Autel Sacrificiel '):
            if (self.region==1):
                equipe_adverse=Equipe(game,[self.monstre1,self.demi_boss1,self.monstre2],3)
            if (self.region==2):
                equipe_adverse=Equipe(game,[self.monstre3,self.demi_boss2,self.monstre4],3)
            if (self.region==3):
                equipe_adverse=Equipe(game,[self.monstre6,self.boss],2)
        else:
            if (self.region==1):
                equipe_adverse=Equipe(game,[self.monstre1,self.demi_boss1,self.monstre2],3)
            if (self.region==2):
                equipe_adverse=Equipe(game,[self.monstre3,self.demi_boss2,self.monstre4],3)
            if (self.region==3):
                equipe_adverse=Equipe(game,[self.monstre5,self.boss,self.monstre6],3)
        return equipe_adverse

    def position(self):
        print('Vous êtes actuellement dans la région ',self.region,'\n')















''' Faire des classes, mais retourner une liste de caractéristiques quand-même '''
class ForetVeur:
    def __init__(self):
        self.caracteristiques=[ForetVeur.Niveau1(),ForetVeur.Niveau2(),ForetVeur.Niveau3(),ForetVeur.Niveau4(),ForetVeur.Niveau5(),ForetVeur.Niveau6(),ForetVeur.Clairiere()]

    def Niveau1():
        nom='la Forêt Veur Niveau 1 - Entrée '
        nom_famille='ForetVeur'
        niveau=1
        attribut='Eau'

        monstre1=Sanglier()
        while(monstre1.attribut!='Vent'):
            monstre1=Sanglier()
        monstre1.surnom='Orc de gauche'

        monstre2=Sanglier()
        while(monstre2.attribut!='Feu'):
            monstre2=Sanglier()
        monstre2.surnom='Orc de droite'

        demi_boss1=Sanglier()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=Sanglier()
        demi_boss1.surnom='Gros sanglier vert'

        monstre3=Sanglier()
        while(monstre3.attribut!='Vent'):
            monstre3=Sanglier()
        monstre3.surnom='Sanglier vert'

        monstre4=Sanglier()
        while(monstre4.attribut!='Feu'):
            monstre4=Sanglier()
        monstre4.surnom='Sanglier rouge'

        demi_boss2=Sanglier()
        while(demi_boss2.attribut!='Feu'):
            demi_boss2=Sanglier()
        demi_boss2.surnom='Gros sanglier rouge'

        monstre5=Sanglier()
        while(monstre5.attribut!='Vent'):
            monstre5=Sanglier()
        monstre5.surnom='Sanglier vert'

        monstre6=Sanglier()
        while(monstre6.attribut!='Feu'):
            monstre6=Sanglier()
        monstre6.surnom='Sanglier rouge'

        boss=Sanglier()
        while(boss.attribut!='Vent'):
            boss=Sanglier()
        boss.surnom='Sanglier vert géant'

        XP_recompense=320
        recompense=[XP_recompense,ForetVeur.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def Niveau2():
        nom='la Forêt Veur Niveau 2 - Est '
        nom_famille='ForetVeur'
        niveau=2
        attribut='Feu'

        monstre1=Champignon()
        while(monstre1.attribut!='Vent'):
            monstre1=Champignon()
        monstre1.surnom='Abeille de gauche'

        monstre2=Champignon()
        while(monstre2.attribut!='Feu'):
            monstre2=Champignon()
        monstre2.surnom='Abeille de droite'

        demi_boss1=Champignon()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=Champignon()
        Monstre.evoluer(demi_boss1)
        demi_boss1.surnom='Abeille du centre'

        monstre3=Champignon()
        while(monstre3.attribut!='Feu'):
            monstre3=Champignon()
        monstre3.surnom='Abeille de gauche'

        monstre4=Champignon()
        while(monstre4.attribut!='Eau'):
            monstre4=Champignon()
        monstre4.surnom='Abeille de droite'

        demi_boss2=Champignon()
        while(demi_boss2.attribut!='Eau'):
            demi_boss2=Champignon()
        Monstre.evoluer(demi_boss2)
        demi_boss2.surnom='Abeille du centre'

        monstre5=Champignon()
        while(monstre5.attribut!='Vent'):
            monstre5=Champignon()
        monstre5.surnom='Abeille de gauche'

        monstre6=Champignon()
        while(monstre6.attribut!='Feu'):
            monstre6=Champignon()
        monstre6.surnom='Abeille de droite'

        boss=Sanglier()
        while(boss.attribut!='Feu'):
            boss=Sanglier()
        Monstre.evoluer(boss)
        boss.surnom='Orc du centre'

        XP_recompense=800
        recompense=[XP_recompense,ForetVeur.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques

    ''' CORRIGER LES GARDIENS DE VENT EN JUSTE GARDIENS (attribut précisé derrière le nom) '''
    def Niveau3():
        nom='la Forêt Veur Niveau 3 - Sud '
        nom_famille='ForetVeur'
        niveau=3
        attribut='Vent'

        monstre1=GardienForet()
        while(monstre1.attribut!='Feu'):
            monstre1=GardienForet()
        monstre1.surnom='Gardien de la Forêt'

        monstre2=GardienForet()
        while(monstre2.attribut!='Vent'):
            monstre2=GardienForet()
        monstre2.surnom='Gardien de la Forêt'

        demi_boss1=GardienForet()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=GardienForet()
        Monstre.evoluer(demi_boss1)
        Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grand Gardien de la Forêt'

        monstre3=GardienForet()
        while(monstre3.attribut!='Feu'):
            monstre3=GardienForet()
        monstre3.surnom='Gardien de la Forêt'

        monstre4=GardienForet()
        while(monstre4.attribut!='Eau'):
            monstre4=GardienForet()
        monstre4.surnom='Gardien de la Forêt'

        demi_boss2=GardienForet()
        while(demi_boss2.attribut!='Eau'):
            demi_boss2=GardienForet()
        Monstre.evoluer(demi_boss2)
        Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grand Gardien de la Forêt'

        monstre5=GardienForet()
        while(monstre5.attribut!='Vent'):
            monstre5=GardienForet()
        monstre5.surnom='Gardien de la Forêt'

        monstre6=GardienForet()
        while(monstre6.attribut!='Vent'):
            monstre6=GardienForet()
        monstre6.surnom='Gardien de la Forêt'

        boss=GardienForet()
        while(boss.attribut!='Vent'):
            boss=GardienForet()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Gardien Suprême de la Forêt'

        XP_recompense=803
        recompense=[XP_recompense,ForetVeur.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def Niveau4():
        nom='la Forêt Veur Niveau 4 - Ouest '
        nom_famille='ForetVeur'
        niveau=4
        attribut='Feu'

        monstre1=Sanglier()
        while(monstre1.attribut!='Feu'):
            monstre1=Sanglier()
        Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Sanglier rouge'

        monstre2=Sanglier()
        while(monstre2.attribut!='Vent'):
            monstre2=Sanglier()
        Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Sanglier vert'

        demi_boss1=Sanglier()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=Sanglier()
        Monstre.evoluer(demi_boss1)
        Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Gros sanglier vert'

        monstre3=Sanglier()
        while(monstre3.attribut!='Feu'):
            monstre3=Sanglier()
        Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Sanglier rouge'

        monstre4=Sanglier()
        while(monstre4.attribut!='Eau'):
            monstre4=Sanglier()
        Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Sanglier bleu'

        demi_boss2=Sanglier()
        while(demi_boss2.attribut!='Eau'):
            demi_boss2=Sanglier()
        Monstre.evoluer(demi_boss2)
        Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Gros sanglier bleu'

        monstre5=Sanglier()
        while(monstre5.attribut!='Feu'):
            monstre5=Sanglier()
        Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Sanglier rouge 1'

        monstre6=Sanglier()
        while(monstre6.attribut!='Feu'):
            monstre6=Sanglier()
        Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Sanglier rouge 2'

        boss=Sanglier()
        while(boss.attribut!='Feu'):
            boss=Sanglier()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Sanglier rouge géant'

        XP_recompense=1127
        recompense=[XP_recompense,ForetVeur.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def Niveau5():
        nom='la Forêt Veur Niveau 5 - Nord '
        nom_famille='ForetVeur'
        niveau=5
        attribut='Eau'

        monstre1=PlanteCarnivore()
        while(monstre1.attribut!='Eau'):
            monstre1=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Plante carnivore bleue'

        monstre2=PlanteCarnivore()
        while(monstre2.attribut!='Feu'):
            monstre2=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Plante carnivore rouge'

        demi_boss1=PlanteCarnivore()
        while(demi_boss1.attribut!='Eau'):
            demi_boss1=PlanteCarnivore()
        Monstre.evoluer(demi_boss1)
        Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grosse plante carnivore bleue'

        monstre3=PlanteCarnivore()
        while(monstre3.attribut!='Feu'):
            monstre3=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Plante carnivore rouge'

        monstre4=PlanteCarnivore()
        while(monstre4.attribut!='Vent'):
            monstre4=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Plante carnivore verte'

        demi_boss2=PlanteCarnivore()
        while(demi_boss2.attribut!='Vent'):
            demi_boss2=PlanteCarnivore()
        Monstre.evoluer(demi_boss2)
        Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grosse plante carnivore verte'

        monstre5=PlanteCarnivore()
        while(monstre5.attribut!='Eau'):
            monstre5=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Plante carnivore bleue'

        monstre6=PlanteCarnivore()
        while(monstre6.attribut!='Feu'):
            monstre6=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Plante carnivore rouge'

        boss=PlanteCarnivore()
        while(boss.attribut!='Eau'):
            boss=PlanteCarnivore()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        Monstre.monter_en_niveau_sans_affichage(boss)
        Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Plante carnivore bleue géante'

        XP_recompense=1130
        recompense=[XP_recompense,ForetVeur.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def Niveau6():
        nom='la Forêt Veur Niveau 6 - Profondeurs '
        nom_famille='ForetVeur'
        niveau=6
        attribut='Eau'

        monstre1=Champignon()
        while(monstre1.attribut!='Vent'):
            monstre1=Champignon()
        Monstre.monter_en_niveau_sans_affichage(monstre1)
        Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Champignon vert'

        monstre2=Champignon()
        while(monstre2.attribut!='Feu'):
            monstre2=Champignon()
        Monstre.monter_en_niveau_sans_affichage(monstre2)
        Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Champignon rouge'

        demi_boss1=Champignon()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=Champignon()
        Monstre.evoluer(demi_boss1)
        Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Gros champignon vert'

        monstre3=Champignon()
        while(monstre3.attribut!='Feu'):
            monstre3=Champignon()
        Monstre.monter_en_niveau_sans_affichage(monstre3)
        Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Champignon rouge'

        monstre4=Champignon()
        while(monstre4.attribut!='Eau'):
            monstre4=Champignon()
        Monstre.monter_en_niveau_sans_affichage(monstre4)
        Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Champignon bleu'

        demi_boss2=Champignon()
        while(demi_boss2.attribut!='Eau'):
            demi_boss2=Champignon()
        Monstre.evoluer(demi_boss2)
        Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Gros champignon bleu'

        monstre5=Champignon()
        while(monstre5.attribut!='Vent'):
            monstre5=Champignon()
        Monstre.monter_en_niveau_sans_affichage(monstre5)
        Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Champignon vert'

        monstre6=Champignon()
        while(monstre6.attribut!='Eau'):
            monstre6=Champignon()
        Monstre.monter_en_niveau_sans_affichage(monstre6)
        Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Champignon bleu'

        boss=Champignon()
        while(boss.attribut!='Eau'):
            boss=Champignon()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        Monstre.monter_en_niveau_sans_affichage(boss)
        Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Champignon bleu géant'

        XP_recompense=1132
        recompense=[XP_recompense,ForetVeur.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def Clairiere():
        nom='la Forêt Veur Niveau 7 - Clairière '
        nom_famille='ForetVeur'
        niveau=7
        attribut='Eau'

        monstre1=PlanteCarnivore()
        while(monstre1.attribut!='Eau'):
            monstre1=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre1)
        Monstre.monter_en_niveau_sans_affichage(monstre1)
        Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Plante carnivore bleue'

        monstre2=PlanteCarnivore()
        while(monstre2.attribut!='Vent'):
            monstre2=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre2)
        Monstre.monter_en_niveau_sans_affichage(monstre2)
        Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Plante carnivore verte'

        demi_boss1=PlanteCarnivore()
        while(demi_boss1.attribut!='Eau'):
            demi_boss1=PlanteCarnivore()
        Monstre.evoluer(demi_boss1)
        Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grosse plante carnivore bleue'
        
        monstre3=PlanteCarnivore()
        while(monstre3.attribut!='Eau'):
            monstre3=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre3)
        Monstre.monter_en_niveau_sans_affichage(monstre3)
        Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Plante carnivore bleue'
        
        monstre4=PlanteCarnivore()
        while(monstre4.attribut!='Vent'):
            monstre4=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre4)
        Monstre.monter_en_niveau_sans_affichage(monstre4)
        Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Plante carnivore verte'

        demi_boss2=PlanteCarnivore()
        while(demi_boss2.attribut!='Vent'):
            demi_boss2=PlanteCarnivore()
        Monstre.evoluer(demi_boss2)
        Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grosse plante carnivore verte'
        
        monstre5=PlanteCarnivore()
        while(monstre5.attribut!='Eau'):
            monstre5=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre5)
        Monstre.monter_en_niveau_sans_affichage(monstre5)
        Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Plante carnivore bleue 1'

        monstre6=PlanteCarnivore()
        while(monstre6.attribut!='Eau'):
            monstre6=PlanteCarnivore()
        Monstre.monter_en_niveau_sans_affichage(monstre6)
        Monstre.monter_en_niveau_sans_affichage(monstre6)
        Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Plante carnivore bleue 2'

        boss=Inugami()
        while(boss.attribut!='Eau'):
            boss=Inugami()
        Monstre.evoluer(boss)
        Monstre.monter_en_niveau_sans_affichage(boss)
        Monstre.monter_en_niveau_sans_affichage(boss)
        Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Inugami bleu Royal'
        boss.capacite2=boss.capacite1
        boss.capacite2_nom=boss.capacite1_nom
        boss.temps_recharge2=1
        boss.attente2=0
        boss.etat_cap2='dispo'
        boss.vitesse_max_donjons=2*boss.vitesse_max_donjons
        boss.vitesse=2*boss.vitesse
        boss.vitesse_actuelle=boss.vitesse # mieux pour l'affichage
        XP_recompense=812
        recompense=[XP_recompense,ForetVeur.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def recompenses(niveau_donjon):
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











class MontTagne:
    def __init__(self):
        self.caracteristiques=[MontTagne.Niveau1(),MontTagne.Niveau2(),MontTagne.Niveau3(),MontTagne.Niveau4(),MontTagne.Niveau5(),MontTagne.Niveau6(),MontTagne.Caverne()]
        
    def Niveau1():
        nom='le Mont Tagne Niveau 1 - Pied '
        nom_famille='MontTagne'
        niveau=1
        attribut='Vent'

        monstre1=Canniboite()
        while(monstre1.attribut!='Vent'):
            monstre1=Canniboite()
        while(monstre1.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Canniboite verte'

        monstre2=Slime()
        while(monstre2.attribut!='Vent'):
            monstre2=Slime()
        while(monstre2.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Slime vert'
    
        demi_boss1=Canniboite()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=Canniboite()
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grosse canniboite verte'
    
        monstre3=Canniboite()
        while(monstre3.attribut!='Feu'):
            monstre3=Canniboite()
        while(monstre3.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Canniboite rouge'
    
        monstre4=Slime()
        while(monstre4.attribut!='Feu'):
            monstre4=Slime()
        while(monstre4.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Slime rouge'
    
        demi_boss2=Canniboite()
        while(demi_boss2.attribut!='Feu'):
            demi_boss2=Canniboite()
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grosse canniboite rouge'
    
        monstre5=Canniboite()
        while(monstre5.attribut!='Vent'):
            monstre5=Canniboite()
        while(monstre5.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Canniboite verte'
    
        monstre6=Slime()
        while(monstre6.attribut!='Feu'):
            monstre6=Slime()
        while(monstre6.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Slime rouge'
    
        boss=Canniboite()
        while(boss.attribut!='Vent'):
            boss=Canniboite()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        while(boss.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Canniboite verte géante'
    
        XP_recompense=1144
        recompense=[XP_recompense,MontTagne.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Niveau2():
        nom='le Mont Tagne Niveau 2 - Chemin souterrain '
        nom_famille='MontTagne'
        niveau=2
        attribut='Feu'
    
        monstre1=Slime()
        while(monstre1.attribut!='Vent'):
            monstre1=Slime()
        while(monstre1.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Slime vert'
    
        monstre2=Slime()
        while(monstre2.attribut!='Eau'):
            monstre2=Slime()
        while(monstre2.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Slime bleu'
    
        demi_boss1=Slime()
        while(demi_boss1.attribut!='Feu'):
            demi_boss1=Slime()
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Gros slime rouge'
    
        monstre3=Slime()
        while(monstre3.attribut!='Feu'):
            monstre3=Slime()
        while(monstre3.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Slime rouge'
    
        monstre4=Slime()
        while(monstre4.attribut!='Eau'):
            monstre4=Slime()
        while(monstre4.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Slime bleu'
    
        demi_boss2=Slime()
        while(demi_boss2.attribut!='Vent'):
            demi_boss2=Slime()
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Gros slime vert'
    
        monstre5=Slime()
        while(monstre5.attribut!='Eau'):
            monstre5=Slime()
        while(monstre5.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Slime bleu'
    
        monstre6=Slime()
        while(monstre6.attribut!='Feu'):
            monstre6=Slime()
        while(monstre6.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Slime rouge'
    
        boss=Slime()
        while(boss.attribut!='Feu'):
            boss=Slime()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        while(boss.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Slime rouge géant'
    
        XP_recompense=1148
        recompense=[XP_recompense,MontTagne.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Niveau3():
        nom='le Mont Tagne Niveau 3 - Caverne intermédiaire '
        nom_famille='MontTagne'
        niveau=3
        attribut='Eau'
    
        monstre1=Spectre()
        while(monstre1.attribut!='Feu'):
            monstre1=Spectre()
        while(monstre1.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Spectre rouge'
    
        monstre2=Slime()
        while(monstre2.attribut!='Feu'):
            monstre2=Slime()
        while(monstre2.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Slime rouge'
    
        demi_boss1=Slime()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=Slime()
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Gros slime vert'
    
        monstre3=Spectre()
        while(monstre3.attribut!='Vent'):
            monstre3=Spectre()
        while(monstre3.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Spectre vert'
    
        monstre4=Spectre()
        while(monstre4.attribut!='Eau'):
            monstre4=Spectre()
        while(monstre4.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Spectre bleu'
    
        demi_boss2=Spectre()
        while(demi_boss2.attribut!='Eau'):
            demi_boss2=Spectre()
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grand spectre bleu'
    
        monstre5=Spectre()
        while(monstre5.attribut!='Vent'):
            monstre5=Spectre()
        while(monstre5.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Spectre vert'
    
        monstre6=Spectre()
        while(monstre6.attribut!='Eau'):
            monstre6=Spectre()
        while(monstre6.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Spectre bleu'
    
        boss=Slime()
        while(boss.attribut!='Eau'):
            boss=Slime()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        while(boss.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Slime bleu géant'
    
        XP_recompense=1153
        recompense=[XP_recompense,MontTagne.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Niveau4():
        nom='le Mont Tagne Niveau 4 - Plateau '
        nom_famille='MontTagne'
        niveau=4
        attribut='Vent'
    
        monstre1=Golem()
        while(monstre1.attribut!='Feu'):
            monstre1=Golem()
        while(monstre1.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Golem rouge'
    
        monstre2=Golem()
        while(monstre2.attribut!='Eau'):
            monstre2=Golem()
        while(monstre2.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Golem bleu'
    
        demi_boss1=Golem()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=Golem()
        while(demi_boss1.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grand golem vert'
    
        monstre3=Golem()
        while(monstre3.attribut!='Eau'):
            monstre3=Golem()
        while(monstre3.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Golem bleu'
    
        monstre4=Golem()
        while(monstre4.attribut!='Vent'):
            monstre4=Golem()
        while(monstre4.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Golem vert'
    
        demi_boss2=Golem()
        while(demi_boss2.attribut!='Feu'):
            demi_boss2=Golem()
        while(demi_boss2.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grand golem rouge'
    
        monstre5=Golem()
        while(monstre5.attribut!='Feu'):
            monstre5=Golem()
        while(monstre5.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Golem rouge'
    
        monstre6=Golem()
        while(monstre6.attribut!='Vent'):
            monstre6=Golem()
        while(monstre6.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Golem vert'
    
        boss=Golem()
        while(boss.attribut!='Vent'):
            boss=Golem()
        while(boss.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Golem vert géant'
    
        XP_recompense=1159
        recompense=[XP_recompense,MontTagne.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Niveau5():
        nom='le Mont Tagne Niveau 5 - Ascension '
        nom_famille='MontTagne'
        niveau=5
        attribut='Feu'
    
        monstre1=Golem()
        while(monstre1.attribut!='Feu'):
            monstre1=Golem()
        while(monstre1.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Golem rouge'
    
        monstre2=Golem()
        while(monstre2.attribut!='Vent'):
            monstre2=Golem()
        while(monstre2.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Golem vert'
    
        demi_boss1=Golem()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=Golem()
        while(demi_boss1.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grand golem vert'
    
        monstre3=Golem()
        while(monstre3.attribut!='Feu'):
            monstre3=Golem()
        while(monstre3.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Golem rouge'
    
        monstre4=Golem()
        while(monstre4.attribut!='Vent'):
            monstre4=Golem()
        while(monstre4.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Golem vert'
    
        demi_boss2=Golem()
        while(demi_boss2.attribut!='Feu'):
            demi_boss2=Golem()
        while(demi_boss2.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grand golem rouge'
    
        monstre5=Golem()
        while(monstre5.attribut!='Feu'):
            monstre5=Golem()
        while(monstre5.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Golem rouge 1'
    
        monstre6=Golem()
        while(monstre6.attribut!='Feu'):
            monstre6=Golem()
        while(monstre6.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Golem rouge 2'
    
        boss=Golem()
        while(boss.attribut!='Feu'):
            boss=Golem()
        while(boss.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Golem rouge géant'
    
        XP_recompense=1169
        recompense=[XP_recompense,MontTagne.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def Niveau6():
        nom='le Mont Tagne Niveau 6 - Sommet '
        nom_famille='MontTagne'
        niveau=6
        attribut='Eau'
    
        monstre1=Golem()
        while(monstre1.attribut!='Eau'):
            monstre1=Golem()
        while(monstre1.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Golem bleu'
    
        monstre2=Golem()
        while(monstre2.attribut!='Feu'):
            monstre2=Golem()
        while(monstre2.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Golem rouge'
    
        demi_boss1=Golem()
        while(demi_boss1.attribut!='Eau'):
            demi_boss1=Golem()
        while(demi_boss1.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grand golem bleu'
    
        monstre3=Golem()
        while(monstre3.attribut!='Vent'):
            monstre3=Golem()
        while(monstre3.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Golem vert 1'
    
        monstre4=Golem()
        while(monstre4.attribut!='Vent'):
            monstre4=Golem()
        while(monstre4.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Golem vert 2'

        demi_boss2=Golem()
        while(demi_boss2.attribut!='Feu'):
            demi_boss2=Golem()
        while(demi_boss2.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grand golem rouge'

        monstre5=Golem()
        while(monstre5.attribut!='Feu'):
            monstre5=Golem()
        while(monstre5.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Golem rouge'

        monstre6=Canniboite()
        while(monstre6.attribut!='Vent'):
            monstre6=Canniboite()
        while(monstre6.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Canniboite verte'
    
        boss=Golem()
        while(boss.attribut!='Eau'):
            boss=Golem()
        while(boss.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Golem bleu géant'
    
        XP_recompense=1176
        recompense=[XP_recompense,MontTagne.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def Caverne():
        nom='le Mont Tagne Niveau 7 - Caverne au Sommet '
        nom_famille='MontTagne'
        niveau=7
        attribut='Feu'

        monstre1=Golem()
        while(monstre1.attribut!='Vent'):
            monstre1=Golem()
        while(monstre1.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Golem vert 1'
    
        monstre2=Golem()
        while(monstre2.attribut!='Vent'):
            monstre2=Golem()
        while(monstre2.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Golem vert 2'
    
        demi_boss1=Golem()
        while(demi_boss1.attribut!='Feu'):
            demi_boss1=Golem()
        while(demi_boss1.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grand golem rouge'
    
        monstre3=Golem()
        while(monstre3.attribut!='Feu'):
            monstre3=Golem()
        while(monstre3.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Golem rouge 1'
    
        monstre4=Golem()
        while(monstre4.attribut!='Feu'):
            monstre4=Golem()
        while(monstre4.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Golem rouge 2'
    
        demi_boss2=Golem()
        while(demi_boss2.attribut!='Feu'):
            demi_boss2=Golem()
        while(demi_boss2.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grand golem rouge'

        monstre5=Golem()
        while(monstre5.attribut!='Feu'):
            monstre5=Golem()
        while(monstre5.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Golem rouge'

        monstre6=Golem()
        while(monstre6.attribut!='Vent'):
            monstre6=Golem()
        while(monstre6.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Golem vert'

        boss=Golem()
        while(boss.attribut!='Feu'):
            boss=Golem()
        Monstre.evoluer(boss)
        while(boss.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Golem rouge Royal'
        boss.defense_max_donjons=2*boss.defense_max_donjons
        boss.defense=2*boss.defense
        boss.defense_actuelle=boss.defense
        boss.pv_max_donjons=2*boss.pv_max_donjons
        boss.pv=2*boss.pv
        boss.pv_actuels=2*boss.pv_actuels
        XP_recompense=842
        recompense=[XP_recompense,MontTagne.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def recompenses(niveau_donjon):
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


class CratereAter():
    def __init__(self):  
        self.caracteristiques=[CratereAter.Niveau1(),CratereAter.Niveau2(),CratereAter.Niveau3(),CratereAter.Niveau4(),CratereAter.Niveau5(),CratereAter.Niveau6(),CratereAter.Caverne()]
        
    def Niveau1():
        nom='le Cratère Ater Niveau 1 - Etage -1 '
        nom_famille='CratereAter'
        niveau=1
        attribut='Vent'
    
        monstre1=ChauveSouris()
        while(monstre1.attribut!='Vent'):
            monstre1=ChauveSouris()
        while(monstre1.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Chauve souris verte'
    
        monstre2=ChauveSouris()
        while(monstre2.attribut!='Feu'):
            monstre2=ChauveSouris()
        while(monstre2.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Chauve souris rouge'
    
        demi_boss1=ChauveSouris()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=ChauveSouris()
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grosse chauve souris verte'
    
        monstre3=ChauveSouris()
        while(monstre3.attribut!='Vent'):
            monstre3=ChauveSouris()
        while(monstre3.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Chauve souris verte'
    
        monstre4=ChauveSouris()
        while(monstre4.attribut!='Feu'):
            monstre4=ChauveSouris()
        while(monstre4.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Chauve souris rouge'
    
        demi_boss2=ChauveSouris()
        while(demi_boss2.attribut!='Feu'):
            demi_boss2=ChauveSouris()
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grosse chauve souris rouge'
    
        monstre5=ChauveSouris()
        while(monstre5.attribut!='Vent'):
            monstre5=ChauveSouris()
        while(monstre5.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Chauve souris verte'

        monstre6=ChauveSouris()
        while(monstre6.attribut!='Feu'):
            monstre6=ChauveSouris()
        while(monstre6.niveau!=3):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Chauve souris rouge'
    
        boss=ChauveSouris()
        while(boss.attribut!='Feu'):
            boss=ChauveSouris()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        while(boss.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Chauve souris rouge géante'
    
        XP_recompense=734
        recompense=[XP_recompense,CratereAter.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def Niveau2():
        nom='le Cratère Ater Niveau 2 - Etage -2 '
        nom_famille='CratereAter'
        niveau=2
        attribut='Eau'
    
        monstre1=SoldatSquelette()
        while(monstre1.attribut!='Vent'):
            monstre1=SoldatSquelette()
        while(monstre1.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Soldat squelette vert'
    
        monstre2=SoldatSquelette()
        while(monstre2.attribut!='Eau'):
            monstre2=SoldatSquelette()
        while(monstre2.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Soldat squelette bleu'
    
        demi_boss1=SoldatSquelette()
        while(demi_boss1.attribut!='Eau'):
            demi_boss1=SoldatSquelette()
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Chef squelette bleu'
    
        monstre3=SoldatSquelette()
        while(monstre3.attribut!='Eau'):
            monstre3=SoldatSquelette()
        while(monstre3.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Soldat squelette bleu'
    
        monstre4=SoldatSquelette()
        while(monstre4.attribut!='Vent'):
            monstre4=SoldatSquelette()
        while(monstre4.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Soldat squelette vert'
    
        demi_boss2=SoldatSquelette()
        while(demi_boss2.attribut!='Vent'):
            demi_boss2=SoldatSquelette()
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Chef squelette vert'

        monstre5=SoldatSquelette()
        while(monstre5.attribut!='Eau'):
            monstre5=SoldatSquelette()
        while(monstre5.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Soldat squelette bleu'
    
        monstre6=SoldatSquelette()
        while(monstre6.attribut!='Vent'):
            monstre6=SoldatSquelette()
        while(monstre6.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Soldat squelette vert'
    
        boss=SoldatSquelette()
        while(boss.attribut!='Eau'):
            boss=SoldatSquelette()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        while(boss.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Capitaine squelette bleu'
    
        XP_recompense=974
        recompense=[XP_recompense,CratereAter.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def Niveau3():
        nom='le Cratère Ater Niveau 3 - Etage -3 '
        nom_famille='CratereAter'
        niveau=3
        attribut='Vent'

        monstre1=ChauveSouris()
        while(monstre1.attribut!='Eau'):
            monstre1=ChauveSouris()
        while(monstre1.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Chauve souris bleue'
    
        monstre2=SoldatSquelette()
        while(monstre2.attribut!='Eau'):
            monstre2=SoldatSquelette()
        while(monstre2.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Soldat squelette bleu'

        demi_boss1=ChauveSouris()
        while(demi_boss1.attribut!='Eau'):
            demi_boss1=ChauveSouris()
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grosse chauve souris bleue'
    
        monstre3=SoldatSquelette()
        while(monstre3.attribut!='Vent'):
            monstre3=SoldatSquelette()
        while(monstre3.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Soldat squelette vert'
    
        monstre4=SoldatSquelette()
        while(monstre4.attribut!='Eau'):
            monstre4=SoldatSquelette()
        while(monstre4.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Soldat squelette bleu'
    
        demi_boss2=Imp()
        while(demi_boss2.attribut!='Vent'):
            demi_boss2=Imp()
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grand imp vert'
    
        monstre5=ChauveSouris()
        while(monstre5.attribut!='Vent'):
            monstre5=ChauveSouris()
        while(monstre5.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Chauve souris verte'
    
        monstre6=ChauveSouris()
        while(monstre6.attribut!='Eau'):
            monstre6=ChauveSouris()
        while(monstre6.niveau!=4):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Chauve souris bleue'
    
        boss=SoldatSquelette()
        while(boss.attribut!='Vent'):
            boss=SoldatSquelette()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        while(boss.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Capitaine squelette vert'
    
        XP_recompense=978
        recompense=[XP_recompense,CratereAter.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Niveau4():
        nom='le Cratère Ater Niveau 4 - Première caverne '
        nom_famille='CratereAter'
        niveau=4
        attribut='Eau'
    
        monstre1=Imp()
        while(monstre1.attribut!='Feu'):
            monstre1=Imp()
        while(monstre1.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Imp rouge'
    
        monstre2=Imp()
        while(monstre2.attribut!='Eau'):
            monstre2=Imp()
        while(monstre2.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Imp bleu'
    
        demi_boss1=Imp()
        while(demi_boss1.attribut!='Feu'):
            demi_boss1=Imp()
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grand Imp rouge'
    
        monstre3=Imp()
        while(monstre3.attribut!='Eau'):
            monstre3=Imp()
        while(monstre3.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Imp bleu'
    
        monstre4=Imp()
        while(monstre4.attribut!='Vent'):
            monstre4=Imp()
        while(monstre4.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Imp vert'
    
        demi_boss2=Imp()
        while(demi_boss2.attribut!='Vent'):
            demi_boss2=Imp()
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grand Imp vert'
    
        monstre5=Imp()
        while(monstre5.attribut!='Feu'):
            monstre5=Imp()
        while(monstre5.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Imp rouge'
    
        monstre6=Imp()
        while(monstre6.attribut!='Vent'):
            monstre6=Imp()
        while(monstre6.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Imp vert'
    
        boss=Imp()
        while(boss.attribut!='Eau'):
            boss=Imp()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        while(boss.niveau!=5):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Imp bleu géant'
    
        XP_recompense=1143
        recompense=[XP_recompense,CratereAter.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Niveau5():
        nom='le Cratère Ater Niveau 5 - Seconde caverne '
        nom_famille='CratereAter'
        niveau=5
        attribut='Ténèbres'
    
        monstre1=Imp()
        while(monstre1.attribut!='Ténèbres'):
            monstre1=Imp()
        while(monstre1.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Imp noir'

        monstre2=Imp()
        while(monstre2.attribut!='Lumière'):
            monstre2=Imp()
        while(monstre2.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Imp blanc'
    
        demi_boss1=Imp()
        while(demi_boss1.attribut!='Lumière'):
            demi_boss1=Imp()
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grand Imp blanc'
    
        monstre3=Imp()
        while(monstre3.attribut!='Lumière'):
            monstre3=Imp()
        while(monstre3.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Imp blanc'
    
        monstre4=Imp()
        while(monstre4.attribut!='Ténèbres'):
            monstre4=Imp()
        while(monstre4.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Imp noir'
    
        demi_boss2=Imp()
        while(demi_boss2.attribut!='Ténèbres'):
            demi_boss2=Imp()
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grand Imp noir'
    
        monstre5=Imp()
        while(monstre5.attribut!='Ténèbres'):
            monstre5=Imp()
        while(monstre5.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Imp noir'
    
        monstre6=Imp()
        while(monstre6.attribut!='Lumière'):
            monstre6=Imp()
        while(monstre6.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Imp blanc'
    
        boss=Imp()
        while(boss.attribut!='Lumière'):
            boss=Imp()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        while(boss.niveau!=6):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Imp blanc géant'
    
        XP_recompense=1150
        recompense=[XP_recompense,CratereAter.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Niveau6():
        nom='le Cratère Ater Niveau 6 - Passage Obscur '
        nom_famille='CratereAter'
        niveau=6
        attribut='Ténèbres'
    
        monstre1=Imp()
        while(monstre1.attribut!='Eau'):
            monstre1=Imp()
        while(monstre1.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Imp bleu'
    
        monstre2=Imp()
        while(monstre2.attribut!='Ténèbres'):
            monstre2=Imp()
        while(monstre2.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Imp noir'
    
        demi_boss1=Imp()
        while(demi_boss1.attribut!='Eau'):
            demi_boss1=Imp()
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grand Imp bleu'
    
        monstre3=Imp()
        while(monstre3.attribut!='Feu'):
            monstre3=Imp()
        while(monstre3.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Imp rouge'
    
        monstre4=Imp()
        while(monstre4.attribut!='Ténèbres'):
            monstre4=Imp()
        while(monstre4.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Imp noir'
    
        demi_boss2=Imp()
        while(demi_boss2.attribut!='Feu'):
            demi_boss2=Imp()
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grand Imp rouge'
    
        monstre5=Imp()
        while(monstre5.attribut!='Ténèbres'):
            monstre5=Imp()
        while(monstre5.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Imp noir 1'
    
        monstre6=Imp()
        while(monstre6.attribut!='Ténèbres'):
            monstre6=Imp()
        while(monstre6.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Imp noir 2'
    
        boss=Imp()
        while(boss.attribut!='Ténèbres'):
            boss=Imp()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        while(boss.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Imp noir géant'
    
        XP_recompense=1159
        recompense=[XP_recompense,CratereAter.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Caverne():
        nom='le Cratère Ater Niveau 7 - Caverne des Profondeurs '
        nom_famille='CratereAter'
        niveau=7
        attribut='Ténèbres'
    
        monstre1=Imp()
        while(monstre1.attribut!='Vent'):
            monstre1=Imp()
        while(monstre1.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Imp vert'
    
        monstre2=Imp()
        while(monstre2.attribut!='Ténèbres'):
            monstre2=Imp()
        while(monstre2.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Imp noir'
    
        demi_boss1=Imp()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=Imp()
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grand Imp vert'
    
        monstre3=Imp()
        while(monstre3.attribut!='Ténèbres'):
            monstre3=Imp()
        while(monstre3.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Imp noir 1'
    
        monstre4=Imp()
        while(monstre4.attribut!='Ténèbres'):
            monstre4=Imp()
        while(monstre4.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Imp noir 2'
    
        demi_boss2=Imp()
        while(demi_boss2.attribut!='Ténèbres'):
            demi_boss2=Imp()
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grand Imp noir'
    
        monstre5=Imp()
        while(monstre5.attribut!='Ténèbres'):
            monstre5=Imp()
        while(monstre5.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Imp noir 1'
    
        monstre6=Imp()
        while(monstre6.attribut!='Ténèbres'):
            monstre6=Imp()
        while(monstre6.niveau!=7):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Imp noir 2'
    
        boss=Mastodonte()
        while(boss.attribut!='Ténèbres'):
            boss=Mastodonte()
        Monstre.evoluer(boss)
        while(boss.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Mastodonte noir Royal'
        boss.defense_max_donjons=2*boss.defense_max_donjons
        boss.defense=2*boss.defense
        boss.defense_actuelle=boss.defense
        boss.pv_max_donjons=2*boss.pv_max_donjons
        boss.pv=2*boss.pv
        boss.pv_actuels=2*boss.pv_actuels
        XP_recompense=827
        recompense=[XP_recompense,CratereAter.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def recompenses(niveau_donjon):
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







class RuinesSenzargen:
    def __init__(self):
        self.caracteristiques=[RuinesSenzargen.Niveau1(),RuinesSenzargen.Niveau2(),RuinesSenzargen.Niveau3(),RuinesSenzargen.Niveau4(),RuinesSenzargen.Niveau5(),RuinesSenzargen.Niveau6(),RuinesSenzargen.Autel()]

    def Niveau1():
        nom='les Ruines de Senzargen Niveau 1 - Portes'
        nom_famille='RuinesSenzargen'
        niveau=1
        attribut='Vent'
    
        monstre1=DameHarpie()
        while(monstre1.attribut!='Vent'):
            monstre1=DameHarpie()
        while(monstre1.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Dame Harpie du Vent'

        monstre2=DameHarpie()
        while(monstre2.attribut!='Eau'):
            monstre2=DameHarpie()
        while(monstre2.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Dame Harpie de l\'Eau'
    
        demi_boss1=DameHarpie()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=DameHarpie()
        while(demi_boss1.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grande Dame Harpie du Vent'
    
        monstre3=DameHarpie()
        while(monstre3.attribut!='Vent'):
            monstre3=DameHarpie()
        while(monstre3.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Dame Harpie du Vent'
    
        monstre4=DameHarpie()
        while(monstre4.attribut!='Eau'):
            monstre4=DameHarpie()
        while(monstre4.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Dame Harpie de l\'Eau'
    
        demi_boss2=DameHarpie()
        while(demi_boss2.attribut!='Eau'):
            demi_boss2=DameHarpie()
        while(demi_boss2.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grande Dame Harpie de l\'Eau'
    
        monstre5=DameHarpie()
        while(monstre5.attribut!='Vent'):
            monstre5=DameHarpie()
        while(monstre5.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Dame Harpie du Vent'
    
        monstre6=DameHarpie()
        while(monstre6.attribut!='Eau'):
            monstre6=DameHarpie()
        while(monstre6.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Dame Harpie de l\'Eau'
    
        boss=DameHarpie()
        while(boss.attribut!='Vent'):
            boss=DameHarpie()
        Monstre.evoluer(boss)
        while(boss.niveau!=8):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Reine Dame Harpie du Vent'
    
        XP_recompense=1530
        recompense=[XP_recompense,RuinesSenzargen.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Niveau2():
        nom='les Ruines de Senzargen Niveau 2 - Couloir '
        nom_famille='RuinesSenzargen'
        niveau=2
        attribut='Eau'
    
        monstre1=DameHarpie()
        while(monstre1.attribut!='Vent'):
            monstre1=DameHarpie()
        while(monstre1.niveau!=9):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Dame Harpie du Vent 1'
    
        monstre2=DameHarpie()
        while(monstre2.attribut!='Vent'):
            monstre2=DameHarpie()
        while(monstre2.niveau!=9):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Dame Harpie du Vent 2'
    
        demi_boss1=DameHarpie()
        while(demi_boss1.attribut!='Eau'):
            demi_boss1=DameHarpie()
        while(demi_boss1.niveau!=9):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grande Dame Harpie de l\'Eau'
    
        monstre3=DameHarpie()
        while(monstre3.attribut!='Eau'):
            monstre3=DameHarpie()
        while(monstre3.niveau!=9):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Dame Harpie de l\'Eau'

        monstre4=DameHarpie()
        while(monstre4.attribut!='Vent'):
            monstre4=DameHarpie()
        while(monstre4.niveau!=9):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Dame Harpie du Vent'
    
        demi_boss2=DameHarpie()
        while(demi_boss2.attribut!='Vent'):
            demi_boss2=DameHarpie()
        while(demi_boss2.niveau!=9):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grande Dame Harpie du Vent'
    
        monstre5=DameHarpie()
        while(monstre5.attribut!='Vent'):
            monstre5=DameHarpie()
        while(monstre5.niveau!=9):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Dame Harpie du Vent 1'
    
        monstre6=DameHarpie()
        while(monstre6.attribut!='Vent'):
            monstre6=DameHarpie()
        while(monstre6.niveau!=9):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Dame Harpie du Vent 2'
    
        boss=DameHarpie()
        while(boss.attribut!='Eau'):
            boss=DameHarpie()
        Monstre.evoluer(boss)
        while(boss.niveau!=9):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Reine Dame Harpie de l\'Eau'
    
        XP_recompense=1548
        recompense=[XP_recompense,RuinesSenzargen.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Niveau3():
        nom='les Ruines de Senzargen Niveau 3 - Escaliers '
        nom_famille='RuinesSenzargen'
        niveau=3
        attribut='Vent'
    
        monstre1=DameHarpie()
        while(monstre1.attribut!='Vent'):
            monstre1=DameHarpie()
        while(monstre1.niveau!=10):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Dame Harpie du Vent'

        monstre2=DameHarpie()
        while(monstre2.attribut!='Eau'):
            monstre2=DameHarpie()
        while(monstre2.niveau!=10):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Dame Harpie de l\'Eau'
    
        demi_boss1=DameHarpie()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=DameHarpie()
        while(demi_boss1.niveau!=10):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Grande Dame Harpie du Vent'
    
        monstre3=DameHarpie()
        while(monstre3.attribut!='Vent'):
            monstre3=DameHarpie()
        while(monstre3.niveau!=10):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Dame Harpie du Vent'
    
        monstre4=DameHarpie()
        while(monstre4.attribut!='Eau'):
            monstre4=DameHarpie()
        while(monstre4.niveau!=10):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Dame Harpie de l\'Eau'
    
        demi_boss2=DameHarpie()
        while(demi_boss2.attribut!='Eau'):
            demi_boss2=DameHarpie()
        while(demi_boss2.niveau!=10):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Grande Dame Harpie de l\'Eau'
    
        monstre5=DameHarpie()
        while(monstre5.attribut!='Vent'):
            monstre5=DameHarpie()
        while(monstre5.niveau!=10):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Dame Harpie du Vent'
    
        monstre6=DameHarpie()
        while(monstre6.attribut!='Eau'):
            monstre6=DameHarpie()
        while(monstre6.niveau!=10):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Dame Harpie de l\'Eau'
    
        boss=DameHarpie()
        while(boss.attribut!='Vent'):
            boss=DameHarpie()
        Monstre.evoluer(boss)
        while(boss.niveau!=10):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Reine Dame Harpie du Vent'
    
        XP_recompense=1566
        recompense=[XP_recompense,RuinesSenzargen.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Niveau4():
        nom='les Ruines de Senzargen Niveau 4 - Premier Autel '
        nom_famille='RuinesSenzargen'
        niveau=4
        attribut='Vent'
    
        monstre1=BasElementaire()
        while(monstre1.attribut!='Vent'):
            monstre1=BasElementaire()
        Monstre.evoluer(monstre1)
        Monstre.evoluer(monstre1)
        while(monstre1.niveau!=11):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Bas Elementaire Vent 1'
    
        monstre2=BasElementaire()
        while(monstre2.attribut!='Vent'):
            monstre2=BasElementaire()
        Monstre.evoluer(monstre2)
        Monstre.evoluer(monstre2)
        while(monstre2.niveau!=11):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Bas Elementaire Vent 2'
    
        demi_boss1=BasElementaire()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=BasElementaire()
        Monstre.evoluer(demi_boss1)
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=11):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Chef Bas Elementaire Vent'
    
        monstre3=BasElementaire()
        while(monstre3.attribut!='Vent'):
            monstre3=BasElementaire()
        Monstre.evoluer(monstre3)
        Monstre.evoluer(monstre3)
        while(monstre3.niveau!=11):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Bas Elementaire Vent 1'
    
        monstre4=BasElementaire()
        while(monstre4.attribut!='Vent'):
            monstre4=BasElementaire()
        Monstre.evoluer(monstre4)
        Monstre.evoluer(monstre4)
        while(monstre4.niveau!=11):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Bas Elementaire Vent 2'
    
        demi_boss2=BasElementaire()
        while(demi_boss2.attribut!='Vent'):
            demi_boss2=BasElementaire()
        Monstre.evoluer(demi_boss2)
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=11):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Chef Bas Elementaire Vent'
    
        monstre5=BasElementaire()
        while(monstre5.attribut!='Vent'):
            monstre5=BasElementaire()
        Monstre.evoluer(monstre5)
        Monstre.evoluer(monstre5)
        while(monstre5.niveau!=11):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Bas Elementaire Vent 1'
    
        monstre6=BasElementaire()
        while(monstre6.attribut!='Vent'):
            monstre6=BasElementaire()
        Monstre.evoluer(monstre6)
        Monstre.evoluer(monstre6)
        while(monstre6.niveau!=11):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Bas Elementaire Vent 2'
    
        boss=BasElementaire()
        while(boss.attribut!='Vent'):
            boss=BasElementaire()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        while(boss.niveau!=11):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Capitaine Bas Elementaire Vent'
    
        XP_recompense=1593
        recompense=[XP_recompense,RuinesSenzargen.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def Niveau5():
        nom='les Ruines de Senzargen Niveau 5 - Second Autel '
        nom_famille='RuinesSenzargen'
        niveau=5
        attribut='Vent'
    
        monstre1=BasElementaire()
        while(monstre1.attribut!='Vent'):
            monstre1=BasElementaire()
        Monstre.evoluer(monstre1)
        Monstre.evoluer(monstre1)
        while(monstre1.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Bas Elementaire Vent 1'
    
        monstre2=BasElementaire()
        while(monstre2.attribut!='Vent'):
            monstre2=BasElementaire()
        Monstre.evoluer(monstre2)
        Monstre.evoluer(monstre2)
        while(monstre2.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Bas Elementaire Vent 2'
    
        demi_boss1=Elementaire()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=Elementaire()
        Monstre.evoluer(demi_boss1)
        Monstre.evoluer(demi_boss1)
        while(demi_boss1.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Chef Elementaire Vent'
    
        monstre3=BasElementaire()
        while(monstre3.attribut!='Vent'):
            monstre3=BasElementaire()
        Monstre.evoluer(monstre3)
        Monstre.evoluer(monstre3)
        while(monstre3.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Bas Elementaire Vent 1'
    
        monstre4=BasElementaire()
        while(monstre4.attribut!='Vent'):
            monstre4=BasElementaire()
        Monstre.evoluer(monstre4)
        Monstre.evoluer(monstre4)
        while(monstre4.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Bas Elementaire Vent 2'
    
        demi_boss2=Elementaire()
        while(demi_boss2.attribut!='Vent'):
            demi_boss2=Elementaire()
        Monstre.evoluer(demi_boss2)
        Monstre.evoluer(demi_boss2)
        while(demi_boss2.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Chef Elementaire Vent'
    
        monstre5=BasElementaire()
        while(monstre5.attribut!='Vent'):
            monstre5=BasElementaire()
        Monstre.evoluer(monstre5)
        Monstre.evoluer(monstre5)
        while(monstre5.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Bas Elementaire Vent 1'
    
        monstre6=BasElementaire()
        while(monstre6.attribut!='Vent'):
            monstre6=BasElementaire()
        Monstre.evoluer(monstre6)
        Monstre.evoluer(monstre6)
        while(monstre6.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Bas Elementaire Vent 2'
    
        boss=Elementaire()
        while(boss.attribut!='Vent'):
            boss=Elementaire()
        Monstre.evoluer(boss)
        Monstre.evoluer(boss)
        while(boss.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Capitaine Elementaire Vent'
    
        XP_recompense=1605
        recompense=[XP_recompense,RuinesSenzargen.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def Niveau6():
        nom='les Ruines de Senzargen Niveau 6 - Profondeurs '
        nom_famille='RuinesSenzargen'
        niveau=6
        attribut='Vent'
    
        monstre1=Elementaire()
        while(monstre1.attribut!='Vent'):
            monstre1=Elementaire()
        while(monstre1.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Elementaire Vent 1'
    
        monstre2=Elementaire()
        while(monstre2.attribut!='Vent'):
            monstre2=Elementaire()
        while(monstre2.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Elementaire Vent 2'
    
        demi_boss1=HautElementaire()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=HautElementaire()
        while(demi_boss1.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Chef Haut Elementaire Vent'
    
        monstre3=Elementaire()
        while(monstre3.attribut!='Vent'):
            monstre3=Elementaire()
        while(monstre3.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Elementaire Vent 1'
    
        monstre4=Elementaire()
        while(monstre4.attribut!='Vent'):
            monstre4=Elementaire()
        while(monstre4.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Elementaire Vent 2'
    
        demi_boss2=HautElementaire()
        while(demi_boss2.attribut!='Vent'):
            demi_boss2=HautElementaire()
        while(demi_boss2.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Chef Haut Elementaire Vent'
    
        monstre5=HautElementaire()
        while(monstre5.attribut!='Vent'):
            monstre5=HautElementaire()
        while(monstre5.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Haut Elementaire Vent'
    
        monstre6=Elementaire()
        while(monstre6.attribut!='Vent'):
            monstre6=Elementaire()
        while(monstre6.niveau!=12):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Elementaire Vent'
    
        boss=HautElementaire()
        while(boss.attribut!='Vent'):
            boss=HautElementaire()
        while(boss.niveau!=13):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Capitaine Haut Elementaire Vent'
    
        XP_recompense=1617
        recompense=[XP_recompense,RuinesSenzargen.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques


    def Autel():
        nom='les Ruines de Senzargen Niveau 7 - Autel Sacrificiel '
        nom_famille='RuinesSenzargen'
        niveau=7
        attribut='Vent'
    
        monstre1=HautElementaire()
        while(monstre1.attribut!='Vent'):
            monstre1=HautElementaire()
        while(monstre1.niveau!=13):
            Monstre.monter_en_niveau_sans_affichage(monstre1)
        monstre1.surnom='Haut Elementaire Vent 1'
    
        monstre2=HautElementaire()
        while(monstre2.attribut!='Vent'):
            monstre2=HautElementaire()
        while(monstre2.niveau!=13):
            Monstre.monter_en_niveau_sans_affichage(monstre2)
        monstre2.surnom='Haut Elementaire Vent 2'
    
        demi_boss1=HautElementaire()
        while(demi_boss1.attribut!='Vent'):
            demi_boss1=HautElementaire()
        while(demi_boss1.niveau!=13):
            Monstre.monter_en_niveau_sans_affichage(demi_boss1)
        demi_boss1.surnom='Chef Haut Elementaire Vent'
    
        monstre3=HautElementaire()
        while(monstre3.attribut!='Vent'):
            monstre3=HautElementaire()
        while(monstre3.niveau!=13):
            Monstre.monter_en_niveau_sans_affichage(monstre3)
        monstre3.surnom='Haut Elementaire Vent 1'
    
        monstre4=HautElementaire()
        while(monstre4.attribut!='Vent'):
            monstre4=HautElementaire()
        while(monstre4.niveau!=13):
            Monstre.monter_en_niveau_sans_affichage(monstre4)
        monstre4.surnom='Haut Elementaire Vent 2'
    
        demi_boss2=HautElementaire()
        while(demi_boss2.attribut!='Vent'):
            demi_boss2=HautElementaire()
        while(demi_boss2.niveau!=13):
            Monstre.monter_en_niveau_sans_affichage(demi_boss2)
        demi_boss2.surnom='Chef Haut Elementaire Vent'

        monstre5=HautElementaire()
        while(monstre5.attribut!='Vent'):
            monstre5=HautElementaire()
        while(monstre5.niveau!=13):
            Monstre.monter_en_niveau_sans_affichage(monstre5)
        monstre5.surnom='Haut Elementaire Vent'
    
        monstre6=Sylphe()
        while(monstre6.attribut!='Vent'):
            monstre6=Sylphe()
        while(monstre6.niveau!=14):
            Monstre.monter_en_niveau_sans_affichage(monstre6)
        monstre6.surnom='Arashi la Tempête'
    
        boss=Sylphide()
        while(boss.attribut!='Vent'):
            boss=Sylphide()
        while(boss.niveau!=14):
            Monstre.monter_en_niveau_sans_affichage(boss)
        boss.surnom='Hayate la Bourrasque'
    
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
        recompense=[XP_recompense,RuinesSenzargen.recompenses(niveau)]
        caracteristiques=[nom,niveau,attribut,monstre1,monstre2,monstre3,monstre4,monstre5,monstre6,demi_boss1,demi_boss2,boss,recompense,nom_famille]
        return caracteristiques
    
    
    def recompenses(niveau_donjon):
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

