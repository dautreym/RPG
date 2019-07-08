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

# POUR FAIRE LA PARTIE ENTIERE D UN NOMBRE 
# nombre=math.floor(nombre)
# POUR LA FAIRE PAR EXCES PLUTOT QUE PAR DEFAUT
# nombre=math.ceil(nombre)


''' A COMPLETER '''
Monstres_dispo_une_etoile_nom=['Slime','GardienForet','Champignon','Spectre','Canniboite','Crapoxique','Sacasable','BasElementaire']
Monstres_dispo_deux_etoiles_nom=['Sanglier','PlanteCarnivore','BoiteDePandore','SoldatSquelette','ChauveSouris','Scorpion','Imp','Lutin','Yeti','Cerbere','OursDeGuerre','Elementaire','Garuda','Harpie','Salamandre','Esprit','Viking','Chevalier']
Monstres_dispo_trois_etoiles_nom=['Fee','DameHarpie','Inugami','Mastodonte','Golem','Serpent','Griffon','Inferno','HautElementaire','OursDeCombat','LoupGarou','Elfe']
Monstres_dispo_quatre_etoiles_nom=['Vampire','Elfe','ChevalierMagique']
Monstres_dispo_cinq_etoiles_nom=['Vampire','Phénix']


'''
ATTENTION

PAS URGENT :
Faire la marque (passif du Vampire ténèbres) 

Après combat réappliquer les améliorations passives comme la réflexion // réduction de dégâts
Faire au cas par cas 

Faire Viking.Encouragement à l'occasion... 

Rajouter la Détermination : octroie du vdv en fonction des PV manquants // nombre de coups subis
Faire aussi chances_de_stun et chances_tour_supplementaire
Rajouter l'incandescence pour infliger des dégâts continus 

Vérifier tous les effets de toutes les compétences au cas par cas

Si besoin : Corriger le juste après Avancer pour soigner un peu toute l'équipe alliée 
    
    
    URGENT :
        IsOkay for now :
            Dans algo SoignerMonstre :
                Réinitialiser les valeurs dans les cas particuliers

        REACTUALISER LA LISTE DES CAPACITES ANORMALES!!!!!!!!!
        
        Tester l'Evolution 
        Regarder si les monstres matériels d'évolution peuvent être le monstre à évoluer 
'''


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

    def recoitDegats(victime,degats):
        victime.pv_actuels=victime.pv_actuels-degats
        if (victime.pv_actuels<=0):
            victime.pv_actuels=0
            victime.etat='mort'
        return victime
        
    def etreSoigne(monstre,montant):
        montant=Arrondir(montant)
        if(monstre.nom=='LoupGarou' and monstre.attribut=='Feu'):
            montant=2*montant
        if(montant>0 and monstre.perturbation_recup<=0):
            pv_actuels_tmp=monstre.pv_actuels
            if (montant+monstre.pv_actuels>=monstre.pv_max_donjons):
                monstre.pv_actuels=monstre.pv_max_donjons
                print(monstre.surnom,monstre.attribut,' récupère ',monstre.pv_max_donjons-pv_actuels_tmp,'points de vie!! \n')
            else:
                monstre.pv_actuels+=montant
                print(monstre.surnom,monstre.attribut,' récupère ',montant,'points de vie!! \n')
        return monstre
    
    
    def SoignerMonstreEntreDeuxVagues(monstre):
        monstre.etat='vivant'
        monstre.jauge_attaque=0
        monstre.tour_supplementaire_tmp=0
        monstre.nb_coups_subis=0
        monstre.reduction_de_degats=0
        monstre.taux_coup_superficiel=0

        monstre.immunite=monstre.immunite_max_donjons
        monstre.tours_immunite=monstre.tours_immunite_max_donjons
        monstre.vol_de_vie=monstre.vol_de_vie_max_donjons
        monstre.regeneration=monstre.regeneration_max_donjons
        monstre.taux_contre_attaque=monstre.taux_contre_attaque_max_donjons
        monstre.chances_de_stun=monstre.chances_de_stun_max_donjons
        monstre.tour_supplementaire=monstre.tour_supplementaire_max_donjons
        monstre.chances_tour_supplementaire=monstre.chances_tour_supplementaire_max_donjons
        monstre.immortalite=monstre.immortalite_max_donjons
        monstre.tours_immortalite=monstre.tours_immortalite_max_donjons

        monstre.tours_bonus_attaque=0
        monstre.tours_bonus_defense=0
        monstre.tours_bonus_vitesse=0
        monstre.tours_bonus_taux_coup_critique=0        
        monstre.tours_regeneration=0
        monstre.contre_attaque=0
        monstre.tours_contre_attaque=0
        monstre.immunite=0
        monstre.tours_immunite=0
        monstre.invincibilite=0
        monstre.tours_invincibilite=0   
        monstre.immortalite=0
        monstre.tours_immortalite=0 
        
        if(not (monstre.nom=='Golem' and monstre.attribut=='Ténèbres')):
            monstre.pourcentage_reflexion_dommages=0
            monstre.tours_reflexion_dommages=0
            monstre.reflexion_dommages=0
        else:
            monstre.pourcentage_reflexion_dommages=0.15
            monstre.tours_reflexion_dommages=0
            monstre.reflexion_dommages=1 
        if((monstre.nom=='Golem' and (monstre.attribut=='Feu' or monstre.attribut=='Eau')) or monstre.nom=='Mastodonte'):
            monstre.passif_active=0
        if(monstre.nom=='Serpent' and monstre.attribut=='Lumière'):
            monstre.nb_effets_renforcement=0
            
        monstre.endurance=0
        monstre.tours_endurance=0
        monstre.provocation=0
        monstre.tours_provocation=0
        
        monstre.tours_malus_attaque=0
        monstre.tours_malus_defense=0        
        monstre.tours_malus_vitesse=0       
        monstre.bonus_taux_coup_superficiel=0
        monstre.tours_bonus_taux_coup_superficiel=0
        monstre.immunite_aux_bonus=0
        monstre.tours_immunite_aux_bonus=0
        monstre.bombe=0
        monstre.tours_avant_explosion=0
        monstre.degats_des_bombes=0
        monstre.provoque=0
        monstre.tours_provoque=0
        monstre.Peut_jouer=1
        monstre.stun=0
        monstre.gel=0
        monstre.sommeil=0
        monstre.tours_sommeil=0
        monstre.marques_degats_continus=0
        monstre.intensite_degats_continus=0
        monstre.perturbation_recup=0
        monstre.tours_perturbation_recup=0
        monstre.silencieux=0
        monstre.tours_silencieux=0
        monstre.marque=0
        monstre.tours_marque=0
        monstre.sans_passif=0
        monstre.tours_sans_passif=0
        monstre.sans_resurrection=0
        monstre.tours_sans_resurrection=0
        
        return monstre
        
    def SoignerEquipeEntreDeuxVagues(equipe_allies):
        i=0
        while(i<len(equipe_allies)):
            if(equipe_allies[i]!=0):
                equipe_allies[i]=Monstre.SoignerMonstreEntreDeuxVagues(equipe_allies[i])
            i+=1
        return equipe_allies
        
    
    # A CHANGER POUR CONSERVER PASSIFS 
    def SoignerMonstre(monstre):
        monstre.pv_actuels=monstre.pv
        monstre.attaque_actuelle=monstre.attaque
        monstre.defense_actuelle=monstre.defense
        monstre.vitesse_actuelle=monstre.vitesse
        monstre.etat='vivant'
        
        monstre.taux_coup_critique_actuel=monstre.taux_coup_critique
        monstre.dommages_critiques_actuels=monstre.dommages_critiques
        monstre.taux_coup_superficiel=0
        monstre.resistance_actuelle=monstre.resistance
        monstre.precision_actuelle=monstre.precision
        monstre.jauge_attaque=0
        monstre.tour_supplementaire_tmp=0
        monstre.nb_coups_subis=0
        monstre.reduction_de_degats=0

        monstre.immunite=0
        monstre.tours_immunite=0
        monstre.vol_de_vie=0
        monstre.regeneration=0
        monstre.taux_contre_attaque=0
        monstre.chances_de_stun=0
        monstre.tour_supplementaire=0
        monstre.chances_tour_supplementaire=0
        monstre.immortalite=0
        monstre.tours_immortalite=0

        monstre.tours_bonus_attaque=0
        monstre.tours_bonus_defense=0
        monstre.tours_bonus_vitesse=0
        monstre.tours_bonus_taux_coup_critique=0        
        monstre.tours_regeneration=0
        monstre.contre_attaque=0
        monstre.tours_contre_attaque=0
        monstre.immunite=0
        monstre.tours_immunite=0
        monstre.invincibilite=0
        monstre.tours_invincibilite=0   
        monstre.immortalite=0
        monstre.tours_immortalite=0 
        
        if(not (monstre.nom=='Golem' and monstre.attribut=='Ténèbres')):
            monstre.pourcentage_reflexion_dommages=0
            monstre.tours_reflexion_dommages=0
            monstre.reflexion_dommages=0
        else:
            monstre.pourcentage_reflexion_dommages=0.15
            monstre.tours_reflexion_dommages=0
            monstre.reflexion_dommages=1 
        if((monstre.nom=='Golem' and (monstre.attribut=='Feu' or monstre.attribut=='Eau')) or monstre.nom=='Mastodonte'):
            monstre.passif_active=0
        if(monstre.nom=='Serpent' and monstre.attribut=='Lumière'):
            monstre.nb_effets_renforcement=0
            
        monstre.endurance=0
        monstre.tours_endurance=0
        monstre.provocation=0
        monstre.tours_provocation=0
        
        monstre.tours_malus_attaque=0
        monstre.tours_malus_defense=0        
        monstre.tours_malus_vitesse=0       
        monstre.bonus_taux_coup_superficiel=0
        monstre.tours_bonus_taux_coup_superficiel=0
        monstre.immunite_aux_bonus=0
        monstre.tours_immunite_aux_bonus=0
        monstre.bombe=0
        monstre.tours_avant_explosion=0
        monstre.degats_des_bombes=0
        monstre.provoque=0
        monstre.tours_provoque=0
        monstre.Peut_jouer=1
        monstre.stun=0
        monstre.gel=0
        monstre.sommeil=0
        monstre.tours_sommeil=0
        monstre.marques_degats_continus=0
        monstre.intensite_degats_continus=0
        monstre.perturbation_recup=0
        monstre.tours_perturbation_recup=0
        monstre.silencieux=0
        monstre.tours_silencieux=0
        monstre.marque=0
        monstre.tours_marque=0
        monstre.sans_passif=0
        monstre.tours_sans_passif=0
        monstre.sans_resurrection=0
        monstre.tours_sans_resurrection=0
        
        return monstre


    def SoignerEquipe(equipe_allies):
        i=0
        while(i<len(equipe_allies)):
            if(equipe_allies[i]!=0):
                equipe_allies[i]=Monstre.SoignerMonstre(equipe_allies[i])
            i+=1
        return equipe_allies
        
        
    def Evoluer(monstre):
        Equipement=[]
        for i in range(6):
            Equipement.append(Runes.Desequiper_sans_affichage(monstre,i))            
        Attribut=monstre.attribut

        while(monstre.attribut!=Attribut):
            monstre=Base.reset_monstre(monstre.nom)
        if(monstre.classe==1):
            pv_min=monstre.pv_min_2
            attaque_min=monstre.attaque_min_2
            defense_min=monstre.defense_min_2
        if(monstre.classe==2):
            pv_min=monstre.pv_min_3
            attaque_min=monstre.attaque_min_3
            defense_min=monstre.defense_min_3
        if(monstre.classe==3):
            pv_min=monstre.pv_min_4
            attaque_min=monstre.attaque_min_4
            defense_min=monstre.defense_min_4
        if(monstre.classe==4):
            pv_min=monstre.pv_min_5
            attaque_min=monstre.attaque_min_5
            defense_min=monstre.defense_min_5
        if(monstre.classe==5):
            pv_min=monstre.pv_min_6
            attaque_min=monstre.attaque_min_6
            defense_min=monstre.defense_min_6
        monstre.pv=pv_min
        monstre.attaque=attaque_min
        monstre.defense=defense_min

        monstre.niveau=1
        monstre.classe+=1
        monstre.XP_avant_prochain_niveau=Donjon.Trouver_XP_initiale(monstre.classe,monstre.niveau)
                
        for j in range(6):
            monstre=Runes.Equiper_sans_affichage(monstre,Equipement[j],j)
        
        monstre=Runes.BonusDeRunes(monstre)
        
        monstre.bonus_de_runes_en_pv+=Arrondir(monstre.pv*monstre.bonus_de_runes_en_pourcentage_de_pv)
        monstre.bonus_de_runes_en_attaque+=Arrondir(monstre.attaque*monstre.bonus_de_runes_en_pourcentage_de_attaque)
        monstre.bonus_de_runes_en_defense+=Arrondir(monstre.defense*monstre.bonus_de_runes_en_pourcentage_de_defense)
        
        monstre.pv_actuels=monstre.pv
        monstre.attaque_actuelle=monstre.attaque
        monstre.defense_actuelle=monstre.defense
        monstre.vitesse_actuelle=monstre.vitesse
        monstre.taux_coup_critique_actuel=monstre.taux_coup_critique
        monstre.dommages_critiques_actuels=monstre.dommages_critiques
        monstre.resistance_actuelle=monstre.resistance
        monstre.precision_actuelle=monstre.precision
        
        return monstre
        
    def __str__(self):
        return ' Nom : '+str(self.nom)+'\n Surnom : '+str(self.surnom)+'\n Attribut : '+str(self.attribut)+'\n Classe : '+str(self.classe)+' étoile(s) \n Niveau : '+str(self.niveau)+'\n PV : '+str(self.pv_actuels)+' sur '+str(self.pv)+' ( + '+str(self.bonus_de_runes_en_pv+self.pv*self.bonus_de_runes_en_pourcentage_de_pv)+')\n Attaque : '+str(self.attaque_actuelle)+' sur '+str(self.attaque)+' ( +'+str(self.bonus_de_runes_en_attaque+self.attaque*self.bonus_de_runes_en_pourcentage_de_attaque)+')\n Défense : '+str(self.defense_actuelle)+' sur '+str(self.defense)+' ( +'+str(self.bonus_de_runes_en_defense+self.defense*self.bonus_de_runes_en_pourcentage_de_defense)+')\n Vitesse : '+str(self.vitesse_actuelle)+' sur '+str(self.vitesse)+' ( +'+str(self.bonus_de_runes_en_vitesse)+')\n Taux de coup critique : '+str(self.taux_coup_critique_actuel)+' sur '+str(self.taux_coup_critique)+' ( +'+str(self.bonus_de_runes_en_taux_de_coup_critique)+')\n Dommages critiques : '+str(self.dommages_critiques_actuels)+' sur '+str(self.dommages_critiques)+' ( +'+str(self.bonus_de_runes_en_dommages_critiques)+')\n Résistance : '+str(self.resistance_actuelle)+' sur '+str(self.resistance)+' ( +'+str(self.bonus_de_runes_en_resistance)+')\n Précision : '+str(self.precision_actuelle)+' sur '+str(self.precision)+' ( +'+str(self.bonus_de_runes_en_precision)+')\n Etat = '+str(self.etat)+'\n Expérience requise avant le prochain niveau : '+str(self.XP_avant_prochain_niveau)+'\n'


def IsSecure(entree):
    return str.isdecimal(entree)
    
def IsSecureString(entree):
    return entree.isalpha()
    

def Afficher_position_stockage(base,team):
    for i in range(len(team)):
        if(team[i]!=0):
            print(team[i],'\n se situe à l\'emplacement ',team[i].indice_stockage_base,' du stockage.\n')

def Rafraichir_equipe(base,team):
    for i in range(len(team)):
        if(team[i]!=0):
            if(team[i].indice_stockage_base!=OUT_OF_STOCKAGE):
                team[i]=base.stockage[team[i].indice_stockage_base]
            else:
                team=equipe.Supprimer_monstre_equipe(team,i)
    return team
    
def Rafraichir_stockage(base):
    for i in range(len(base.stockage)):
        if((base.stockage[i]!=0) and ((base.stockage[i]).indice_stockage_base==OUT_OF_STOCKAGE)):
            Base.supprimer_monstre(base,i)
    
def Arrondir(nombre):
    reste=nombre%1
    if(reste>=0.5):
        nombre=math.ceil(nombre)
    else:
        nombre=math.floor(nombre)
    return nombre
    
def Arrondir_au_centieme(nombre):
    return Arrondir(100*nombre)/100
    
    
def CalculDommage(attaquant,Multiplicateur,BonusSkill,cible):
    degats_infliges=attaquant.attaque_actuelle*Multiplicateur*(1+BonusSkill)
    intensite_coup=random.randint(1,100)
    if(PrioriteElementaire(attaquant,cible)==True):
        if(intensite_coup>=100-(15+100*attaquant.taux_coup_critique_actuel)):
            degats_infliges+=Arrondir(attaquant.attaque_actuelle*Multiplicateur*attaquant.dommages_critiques_actuels)
        else:
            degats_infliges+=Arrondir(0.3*degats_infliges)
    elif(PrioriteElementaire(cible,attaquant)==True):
        if(intensite_coup<=50+100*attaquant.taux_coup_superficiel):
            degats_infliges-=Arrondir(0.3*degats_infliges)
    cible.nb_coups_subis+=1
    return degats_infliges


def ReductionDommage(degats_infliges,cible):
    facteur_reduction_de_degats=1000/(1140+3.5*cible.defense_actuelle)
    degats_infliges=Arrondir(degats_infliges*facteur_reduction_de_degats)
    degats_infliges-=cible.reduction_de_degats*degats_infliges
    return degats_infliges


def AffichageTypeDeCoup(attaquant,Multiplicateur,BonusSkill,degats,cible):
    type_de_coup='Normal'
    degats_infliges=attaquant.attaque_actuelle*Multiplicateur*(1+BonusSkill)
    if((degats_infliges-Arrondir(0.3*degats_infliges))==degats):
        type_de_coup='Superficiel'
        print('Coup superficiel!!')
    elif((degats_infliges+Arrondir(attaquant.attaque_actuelle*Multiplicateur*attaquant.dommages_critiques_actuels))==degats):
        type_de_coup='Critique'
        print('Coup critique!!')
    elif((degats_infliges+Arrondir(0.3*degats_infliges))==degats):
        type_de_coup='Dévastateur'
        print('Coup dévastateur!!')
    return type_de_coup


def Debut_de_tour(perso):
    if(perso.tours_regeneration>0):
        if(perso.perturbation_recup>0):
            perso.tours_perturbation_recup-=1
        else:
            montant=Arrondir(perso.regeneration*perso.pv_max_donjons)
            pv_actuels_tmp=perso.pv_actuels
            if(montant+perso.pv_actuels>=perso.pv_max_donjons):
                perso.pv_actuels=perso.pv_max_donjons
                print(perso.surnom,perso.attribut,'récupère',perso.pv_max_donjons-pv_actuels_tmp,'points de vie grâce à sa régénération!!\n')
            else:
                perso.pv_actuels+=montant
                print(perso.surnom,perso.attribut,'récupère',montant,'points de vie grâce à sa régénération!!\n')
    elif(perso.regeneration>0):
        if(perso.perturbation_recup<=0):
            montant=Arrondir(perso.regeneration*perso.pv_max_donjons)
            pv_actuels_tmp=perso.pv_actuels
            if(montant+perso.pv_actuels>=perso.pv_max_donjons):
                perso.pv_actuels=perso.pv_max_donjons
                print(perso.surnom,perso.attribut,'récupère',perso.pv_max_donjons-pv_actuels_tmp,'points de vie grâce à sa régénération!!\n')
            else:
                perso.pv_actuels+=montant
                print(perso.surnom,perso.attribut,'récupère',montant,'points de vie grâce à sa régénération!!\n')
    if(perso.bombe>0):
        if(perso.tours_avant_explosion==0):
            perso.pv_actuels-=perso.degats_des_bombes
            perso.bombe=0
            perso.stun=1
    if(perso.stun>0):
        perso.Peut_jouer=0
        perso.stun=0
    if(perso.gel>0):
        perso.Peut_jouer=0
        perso.gel=0
    if(perso.sommeil>0):
        perso.Peut_jouer=0
        perso.tours_sommeil-=1
        if(perso.tours_sommeil<=0):
            perso.sommeil=0
    if(perso.intensite_degats_continus>0):
        if(perso.pv_actuels>0):
            perso.pv_actuels-=math.floor(perso.marques_degats_continus*(0.05*perso.pv_max_donjons))
            print(perso.surnom,' perd ',math.floor(perso.marques_degats_continus*(0.05*perso.pv_max_donjons)),' PV à cause des dégâts continus!! \n')
        perso.intensite_degats_continus-=1
    if(perso.intensite_degats_continus==0):
        perso.marques_degats_continus=0
        
    if(perso.tours_bonus_attaque>0):
        perso.tours_bonus_attaque-=1
        if(perso.tours_bonus_attaque==0):
            if(perso.tours_malus_attaque<=0):
                perso.attaque_actuelle=perso.attaque_max_donjons
            else:
                perso.attaque_actuelle=perso.attaque_max_donjons-(0.5*perso.attaque_actuelle)
    if(perso.tours_bonus_defense>0):
        perso.tours_bonus_defense-=1
        if(perso.tours_bonus_defense==0):
            if(perso.tours_malus_defense<=0):
                perso.defense_actuelle=perso.defense_max_donjons
            else:
                perso.defense_actuelle=perso.defense_max_donjons-(0.7*perso.defense_actuelle)
    if(perso.tours_bonus_vitesse>0):
        perso.tours_bonus_vitesse-=1
        if(perso.tours_bonus_vitesse==0):
            if(perso.tours_malus_vitesse<=0):
                perso.vitesse_actuelle=perso.vitesse_max_donjons
            else:
                perso.vitesse_actuelle=perso.vitesse_max_donjons-(0.3*perso.vitesse_actuelle)
    if(perso.tours_bonus_taux_coup_critique>0):
        perso.tours_bonus_taux_coup_critique-=1
        if(perso.tours_bonus_taux_coup_critique==0):
            perso.taux_coup_critique_actuel=perso.taux_coup_critique_max_donjons
    if(perso.tours_regeneration>0):
        perso.tours_regeneration-=1
        if(perso.tours_regeneration==0):
            perso.regeneration=0
    if(perso.tours_contre_attaque>0):
        perso.tours_contre_attaque-=1
        if(perso.tours_contre_attaque==0):
            perso.contre_attaque=0
    if(perso.taux_contre_attaque>0):
        reussite_effet=(random.randint(1,100))/100
        if(reussite_effet<=perso.taux_contre_attaque):
            perso.contre_attaque=1
            perso.tours_contre_attaque=max(1,perso.tours_contre_attaque)
    if(perso.tours_immunite>0):
        perso.tours_immunite-=1
        if(perso.tours_immunite==0):
            perso.immunite=0
    if(perso.tours_invincibilite>0):
        perso.tours_invincibilite-=1
        if(perso.tours_invincibilite==0):
            perso.invincibilite=0
    if(perso.tours_immortalite>0):
        perso.tours_immortalite-=1
        if(perso.tours_immortalite==0):
            perso.immortalite=0
    if(perso.tours_reflexion_dommages>0):
        perso.tours_reflexion_dommages-=1
        if(perso.tours_reflexion_dommages==0):
            perso.reflexion_dommages=0
    if(perso.tours_endurance>0):
        perso.tours_endurance-=1
        if(perso.tours_endurance==0):
            perso.endurance=0
    if(perso.tours_provocation>0):
        perso.tours_provocation-=1
        if(perso.tours_provocation==0):
            perso.provocation=0
            
    if(perso.tours_malus_attaque>0):
        perso.tours_malus_attaque-=1
        if(perso.tours_malus_attaque==0):
            if(perso.tours_bonus_attaque<=0):
                perso.attaque_actuelle=perso.attaque_max_donjons
            else:
                perso.attaque_actuelle=perso.attaque_max_donjons+(0.5*perso.attaque_actuelle)
    if(perso.tours_malus_defense>0):
        perso.tours_malus_defense-=1
        if(perso.tours_malus_defense==0):
            if(perso.tours_bonus_defense<=0):
                perso.defense_actuelle=perso.defense_max_donjons
            else:
                perso.defense_actuelle=perso.defense_max_donjons+(0.7*perso.defense_actuelle)
    if(perso.tours_malus_vitesse>0):
        perso.tours_malus_vitesse-=1
        if(perso.tours_malus_vitesse==0):
            if(perso.tours_bonus_vitesse<=0):
                perso.vitesse_actuelle=perso.vitesse_max_donjons
            else:
                perso.vitesse_actuelle=perso.vitesse_max_donjons+(0.3*perso.vitesse_actuelle)
    if(perso.tours_bonus_taux_coup_superficiel>0):
        perso.tours_bonus_taux_coup_superficiel-=1
        if(perso.tours_bonus_taux_coup_superficiel==0):
            perso.bonus_taux_coup_superficiel=0
    if(perso.tours_immunite_aux_bonus>0):
        perso.tours_immunite_aux_bonus-=1
        if(perso.tours_immunite_aux_bonus==0):
            perso.immunite_aux_bonus=0
    if(perso.tours_provoque>0):
        perso.tours_provoque-=1
        if(perso.tours_provoque==0):
            perso.provoque=0
    if(perso.tours_perturbation_recup>0):
        perso.tours_perturbation_recup-=1
        if(perso.tours_perturbation_recup==0):
            perso.perturbation_recup=0
    if(perso.tours_silencieux>0):
        perso.tours_silencieux-=1
        if(perso.tours_silencieux==0):
            perso.silencieux=0
    if(perso.tours_marque>0):
        perso.tours_marque-=1
        if(perso.tours_marque==0):
            perso.marque=0
    if(perso.tours_sans_passif>0):
        perso.tours_sans_passif-=1
        if(perso.tours_sans_passif==0):
            perso.sans_passif=0
    if(perso.tours_sans_resurrection>0):
        perso.tours_sans_resurrection-=1
        if(perso.tours_sans_resurrection==0):
            perso.sans_resurrection=0
    
    return perso
    

def isAlive(team):
    Alive=False
    for i in range(len(team)):
        if(team[i].pv_actuels>0):
            Alive=True
    return Alive
    

def UnPersoDoitJouer(persos):
    DoitJouer=False    
    for k in range(len(persos)):
        if(persos[k].jauge_attaque>=100):
            DoitJouer=True
    return DoitJouer


def EnnemiProvocateur(team):
    Presence=False
    for i in range(len(team)):
        if(team[i].provocation>0):
            Presence=True
    return Presence
    
def AppliquerPassifsFinDeTour(attaquant,cible,team_attaquant,team_cible):
    if(cible.pv_actuels>0):
        for w in range(len(team_cible)):
            if(team_cible[w].nom=='Elfe' and team_cible[w].attribut=='Ténèbres' and team_cible[w].sans_passif<=0):
                attaquant=Elfe.ContreAttaque(team_cible[w],attaquant)
        if((cible.nom=='LoupGarou' or cible.nom=='Loup Garou') and cible.attribut=='Ténèbres' and cible.sans_passif<=0):
            attaquant=LoupGarou.RetourDeCoup(cible,attaquant)
        if(cible.nom=='Elfe' and cible.attribut=='Vent' and cible.sans_passif<=0):
            team_cible=Elfe.FinMouvementEsquive(team_cible)
    else:
        if(cible.nom=='Vampire' and cible.attribut=='Lumière' and cible.sans_passif<=0 and cible.pv_actuels<=0):
            team_cible=Vampire.Immortalite(team_cible)
    if(((attaquant.nom=='ChevalierMagique') or (attaquant.nom=='Chevalier Magique')) and attaquant.attribut=='Lumière' and attaquant.sans_passif<=0):
        team_attaquant=ChevalierMagique.Altruisme(attaquant,cible,team_attaquant)
    if(attaquant.nom=='Phénix' and attaquant.attribut=='Ténèbres'):
        Phenix.Enfer(attaquant,cible)
    if(attaquant.nom=='Phénix' and attaquant.attribut=='Feu'):
        team_attaquant=Phenix.Eternite(team_attaquant)
    if(cible.nom=='Phénix' and cible.attribut=='Feu'):
        team_cible=Phenix.Resurrection(team_cible)
        
    ''' TESTER SI MARCHE BIEN SANS RETURN, SINON EN FAIRE UN '''
    

def FinDuCombat(allies,ennemis):
    Fin=False
    if(isAlive(allies) and (isAlive(ennemis)==False)):
        Fin=True
    if(isAlive(ennemis) and (isAlive(allies)==False)):
        Fin=True
    return Fin


def Tick(persos):
    for k in range(len(persos)):
        persos[k].jauge_attaque+=Arrondir(7*persos[k].vitesse_actuelle/100)
    return persos


def Combat_xVx_avec_capacites_speciales(allies,ennemis):

    ''' Créer tous les Anti Passifs... '''
    Passifs_debut_de_partie=[Chevalier.Chevalerie,Serpent.CoupeFeu,Griffon.BouclierLumiere,Griffon.BouclierTenebres,LoupGarou.SoifDeSang]
    Passifs_fin_de_partie=[Griffon.AntiBouclierTenebres,Griffon.AntiBouclierLumiere]
    
    if(allies[2]==0):
        allies.pop(2)
    if(allies[1]==0):
        allies.pop(1)
    if(ennemis[2]==0):
        ennemis.pop(2)
    if(ennemis[1]==0):
        ennemis.pop(1)
    
    if(allies[0].presence_leader_skill==1):
        allies=allies[0].leader_skill(allies)
    if(ennemis[0].presence_leader_skill==1):
        ennemis=ennemis[0].leader_skill(ennemis)

    ''' Pour l'instant, aucun passif_2 dans les passifs de début de partie '''
    for z in range(len(allies)):
        if(allies[z].presence_passif_1==1):
            if(allies[z].passif_1 in Passifs_debut_de_partie):
                allies=allies[z].passif_1(allies)

    for z in range(len(ennemis)):
        if(ennemis[z].presence_passif_1==1):
            if(ennemis[z].passif_1 in Passifs_debut_de_partie):
                ennemis=ennemis[z].passif_1(ennemis)
        
    persos=[]
    allies_morts=[]
    ennemis_morts=[]
    
    for i in range(len(allies)):
        if(allies[i]!=0):
            persos.append(allies[i])
    for j in range(len(ennemis)):
        if(ennemis[j]!=0):
            persos.append(ennemis[j])
            
    while(FinDuCombat(allies,ennemis)==False):
        while(UnPersoDoitJouer(persos)==False):
            persos=Tick(persos)
        while(UnPersoDoitJouer(persos)==True and not FinDuCombat(allies,ennemis)):
            for l in range(len(persos)):
                if(persos[l].jauge_attaque>=100 and not FinDuCombat(allies,ennemis)):
                    print('***** Recapitulatif *****')
                    for m in range(len(persos)):
                        print(persos[m].surnom,persos[m].attribut,' : ',persos[m].pv_actuels,'PV sur',persos[m].pv_max_donjons)
                        print('Jauge d\'attaque : ',persos[m].jauge_attaque)
                    print('*************************')
                    print('\n')
                    for n in range(len(allies)):
                        if(allies[n].pv_actuels<=0 and (allies[n] not in allies_morts)):
                            allies_morts.append(allies[n])
                    for n in range(len(ennemis)):
                        if(ennemis[n].pv_actuels<=0 and (ennemis[n] not in ennemis_morts)):
                            ennemis_morts.append(ennemis[n])

                    jauge_max=persos[0].jauge_attaque
                    indice_du_max=0
                    for o in range(len(persos)):
                        if(persos[o].jauge_attaque>jauge_max):
                            jauge_max=persos[o].jauge_attaque
                            indice_du_max=o                            
                    retourAction=Action(persos[indice_du_max],allies,ennemis,allies_morts,ennemis_morts)
                    allies_morts=retourAction[0]
                    ennemis_morts=retourAction[1]
                    persos[indice_du_max].tour_supplementaire_tmp=0
                    persos=Tick(persos)
                    str(input(' > '))
                    
                    '''                    
                    if((persos[l] in allies) and isAlive(ennemis)):
                        Action(persos[l],allies,ennemis)
                        persos[l].tour_supplementaire_tmp=0
                    elif((persos[l] in ennemis) and isAlive(allies)):
                        Action(persos[l],allies,ennemis)
                        persos[l].tour_supplementaire_tmp=0
                    else:
                        break
                    '''
        if(FinDuCombat(allies,ennemis)):
            print('Le combat est terminé. \n\n')
    if(isAlive(allies)):
        vainqueur='allies'
    else:
        vainqueur='ennemis'
        
    if(allies[0].presence_leader_skill==1):
        allies=allies[0].Anti_leader_skill(allies)
    if(ennemis[0].presence_leader_skill==1):
        ennemis=ennemis[0].Anti_leader_skill(ennemis)

    ''' Pour l'instant, aucun passif_2 dans les passifs de fin de partie '''
    for z in range(len(allies)):
        if(allies[z].presence_passif_1==1):
            if(allies[z].passif_1 in Passifs_fin_de_partie):
                allies=allies[z].passif_1(allies)
    for z in range(len(ennemis)):
        if(ennemis[z].presence_passif_1==1):
            if(ennemis[z].passif_1 in Passifs_fin_de_partie):
                ennemis=ennemis[z].passif_1(ennemis)
            
    print('Le vainqueur est : ',vainqueur,'!! \n\n')
    str(input(' > '))
    
    return vainqueur
    
    
def Action(attaquant,team_allies,team_ennemis,allies_morts,ennemis_morts):
    ''' ACTUALISER TOUTES LES CAPACITES ANORMALES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! '''
    ''' FONCTION A OPTIMISER... Faire beaucoup plus de fonctions auxiliaires!!!! '''
    
    CapacitesAnormales=[SoldatSquelette.Slash,ChauveSouris.Ultrason,Lutin.Deceleration,OursDeGuerre.Rugissement,Salamandre.Tremblement,Chevalier.Abnegation,OursDeGuerre.Abnegation,Elementaire.Renforcement,Garuda.Resurgir,Garuda.Lumiere,Esprit.Guerison,Esprit.SphereSpirituelle,Fee.Soin,Fee.DoubleFleche,Fee.PluieDouleur,Fee.Benediction,DameHarpie.Plumes,DameHarpie.Danse,Inugami.Coop,Inugami.Hurlement,Golem.CorpsLave,Golem.CorpsGlace,Golem.MurDeFer,Mastodonte.PluieGravats,Mastodonte.ArmureGlace,Serpent.Tsunami,Serpent.Orage,Griffon.Tornade,Inferno.Deflagration,Inferno.Orage,Elfe.Fleches,Elfe.Pluie,ChevalierMagique.Projectiles,ChevalierMagique.Drain,Griffon.Acceleration,Inferno.Adrenaline,OursDeCombat.Cri,Elfe.Strategie,ChevalierMagique.Combo,ChevalierMagique.Tempete,ChevalierMagique.Vortex,Phenix.Blizzard,Phenix.Tempete,Phenix.Purification,Sylphe.Tourbillon,Sylphe.Nuit,Sylphe.Cyclone,Sylphe.Blizzard,Sylphe.Phenix,Sylphide.Bourrasque,Sylphide.Bourrasque2,Sylphide.Conjuration,Sylphide.Bouclier,Sylphide.Benediction,Sylphide.BenedictionLumiere]
    CapacitesMulticibles=[SoldatSquelette.Slash,ChauveSouris.Ultrason,Lutin.Deceleration,OursDeGuerre.Rugissement,Salamandre.Tremblement,Chevalier.Abnegation,Fee.DoubleFleche,Fee.PluieDouleur,DameHarpie.Plumes,Golem.CorpsLave,Golem.CorpsGlace,Mastodonte.PluieGravats,Serpent.Tsunami,Serpent.Orage,Griffon.Tornade,Inferno.Deflagration,Inferno.Orage,Elfe.Fleches,Elfe.Pluie,ChevalierMagique.Projectiles,ChevalierMagique.Drain,Phenix.Blizzard,Phenix.Tempete,Phenix.Purification,Sylphe.Tourbillon,Sylphe.Nuit,Sylphe.Cyclone,Sylphe.Blizzard,Sylphe.Phenix]
    CapacitesMulticiblesMultiequipes=[Sylphide.Bourrasque,Sylphide.Bourrasque2] # (sylphe,equipe_ennemie,equipe_alliee)
    CapacitesHitMulticibles=[ChevalierMagique.Combo,ChevalierMagique.Tempete]

    CapacitesSoinAllie=[Esprit.Guerison,Fee.Soin,Sylphide.Benediction]
    CapacitesSoinAllieAvecHit=[Esprit.SphereSpirituelle,ChevalierMagique.Vortex] # (esprit,Team_allies,cible)
    CapacitesProtectionAllie=[]
    CapacitesRenforcementAllie=[Garuda.Resurgir]
    CapacitesResurrectionAllie=[Garuda.Lumiere] # Prend Team_allies comme argument
    
    CapacitesRenforcementPerso=[OursDeGuerre.Abnegation,Elementaire.Renforcement,Golem.MurDeFer,Mastodonte.ArmureGlace]
    CapacitesRenforcementEquipe=[Fee.Benediction,DameHarpie.Danse,Inugami.Hurlement,Griffon.Acceleration,Inferno.Adrenaline,OursDeCombat.Cri,Elfe.Strategie,Sylphide.BenedictionLumiere,Sylphide.Bouclier,Sylphide.Conjuration] # Same
    CapacitesAttaqueEnGroupe=[Inugami.Coop] # (inugami,Team_allies,cible)
    
    Passifs_debut_de_tour=[Serpent.Renforcement,Elfe.MouvementEsquive,ChevalierMagique.FeuVengeur]
    Passifs_fin_de_tour=[Chevalier.Urgence,Golem.Barriere,Mastodonte.PeauDure,Elfe.FinMouvementEsquive,Vampire.SoifDeSang]
    
    attaquant.tour_supplementaire_tmp+=attaquant.tour_supplementaire
    if(attaquant.chances_tour_supplementaire>0):
        reussite_effet=(random.randint(1,100))/100
        if(reussite_effet<=attaquant.chances_tour_supplementaire):
            attaquant.tour_supplementaire_tmp+=1
    
    print("C'est au tour de ", attaquant.surnom, attaquant.attribut, " : ", "\n")
    while(attaquant.tour_supplementaire_tmp>=0):
        attaquant=Debut_de_tour(attaquant)
        if(attaquant.pv_actuels>0):
            if(attaquant.Peut_jouer==1):
                if(attaquant in team_allies):
                    if(isAlive(team_ennemis)):
                        if((attaquant.presence_passif_1==1) and (attaquant.sans_passif<=0)  and (attaquant.passif_1 in Passifs_debut_de_tour)):
                            team_allies=attaquant.passif_1(team_allies)
                        if((attaquant.presence_passif_2==1) and (attaquant.sans_passif<=0)  and (attaquant.passif_2 in Passifs_debut_de_tour)):
                            team_allies=attaquant.passif_2(team_allies)
                        if(attaquant.provoque<=0):
                            positions_ennemis=['de gauche','du centre','de droite']
                            k=0
                            while(k<len(team_ennemis)):
                                if (team_ennemis[k].pv_actuels<=0):
                                    ennemis_morts.append(team_ennemis[k])
                                    team_ennemis.pop(k)
                                    positions_ennemis.pop(k)
                                    k-=1
                                k+=1
                            possibilites_cible=[]
                            print('Vos ennemis sont : ')
                            for k in range(len(team_ennemis)):
                                print(team_ennemis[k].surnom,positions_ennemis[k],' = ',k,'(',team_ennemis[k].pv_actuels,'PV restants)')
                                possibilites_cible.append(k)
                            
                            capacite_choisie=Choisir_capacite_speciale(attaquant)
                            if((capacite_choisie not in CapacitesAnormales) or (capacite_choisie in CapacitesSoinAllieAvecHit) or (capacite_choisie in CapacitesAttaqueEnGroupe) or (capacite_choisie in CapacitesHitMulticibles)):
                                entree=input('Quelle cible voulez-vous attaquer ? ')
                                while(not IsSecure(entree)):
                                    entree=input('Quelle cible voulez-vous attaquer ? ')
                                indice_cible=int(entree)
                                while(indice_cible not in possibilites_cible):
                                    entree=input('Quelle cible voulez-vous attaquer ? ')
                                    while(not IsSecure(entree)):
                                        entree=input('Quelle cible voulez-vous attaquer ? ')
                                    indice_cible=int(entree)
                                cible=team_ennemis[indice_cible]
                                pv_avant_degats=cible.pv_actuels
                                if ((capacite_choisie not in CapacitesSoinAllieAvecHit) and (capacite_choisie not in CapacitesAttaqueEnGroupe) and (capacite_choisie not in CapacitesHitMulticibles)):
                                    capacite_choisie(attaquant,cible)
                                elif(capacite_choisie in CapacitesHitMulticibles):
                                    capacite_choisie(attaquant,team_ennemis,cible)
                                else:
                                    capacite_choisie(attaquant,team_allies,cible)
                                if(cible.reflexion_dommages>0):
                                    degats_subis=pv_avant_degats-cible.pv_actuels
                                    degats_renvoyes=Arrondir(cible.pourcentage_reflexion_dommages*degats_subis)
                                    cible.pv_actuels+=degats_renvoyes # oui c'est bien un + 
                                    if(attaquant.immortalite<=0):
                                        print(attaquant.surnom,attaquant.attribut,' reçoit la réflexion des dégâts!!')
                                        print(attaquant.surnom,attaquant.attribut,' subit ',degats_renvoyes,' points de dégâts!!')            
                                        attaquant.pv_actuels-=degats_renvoyes
                                    else:
                                        print(attaquant.surnom,attaquant.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                                    if(attaquant.pv_actuels<=0):
                                        print(attaquant.surnom,attaquant.attribut,' est mort!! \n')
                                    else:
                                        print('Il reste ',attaquant.pv_actuels,' point(s) de vie sur',attaquant.pv_max_donjons,' à ',attaquant.surnom,attaquant.attribut,'!! \n')
                                if(cible.contre_attaque>0 and cible.pv_actuels>0):
                                    if (degats_subis<=0):
                                        degats_subis=1
                                    print(cible.surnom,cible.attribut,' effectue une contre-attaque sur ',attaquant.surnom,attaquant.attribut,'!!')
                                    if(attaquant.immortalite<=0):
                                        pv_attaquant_avant_dommages=attaquant.pv_actuels
                                        attaquant=cible.capacite1(cible,attaquant)
                                        ecart=attaquant.pv_actuels-pv_attaquant_avant_dommages
                                        attaquant.pv_actuels+=Arrondir(0.25*ecart) # seulement 75% des dégâts sont subis
                                    else:
                                        print(attaquant.surnom,attaquant.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                                    if(attaquant.pv_actuels<=0):
                                        print(attaquant.surnom,attaquant.attribut,' est mort!! \n')
                                    else:
                                        print('Il reste ',attaquant.pv_actuels,' point(s) de vie sur',attaquant.pv_max_donjons,' à ',attaquant.surnom,attaquant.attribut,'!! \n')
                                AppliquerPassifsFinDeTour(attaquant,cible,team_allies,team_ennemis)
                                        
                            else:
                                if((capacite_choisie in CapacitesSoinAllie) or (capacite_choisie in CapacitesProtectionAllie) or (capacite_choisie in CapacitesRenforcementAllie)):
                                    possibilites_choix_allie=[]
                                    for n in range(len(team_allies)):
                                        if(team_allies[n].pv_actuels>0):
                                            print('Il reste ',team_allies[n].pv_actuels,' PV à l allié ',n,':',team_allies[n].surnom,team_allies[n].attribut,' sur ',team_allies[n].pv_max_donjons)
                                            possibilites_choix_allie.append(n)
                                    if(capacite_choisie in CapacitesSoinAllie):
                                        entree=input('Quel allié voulez-vous soigner ? ')
                                        while(not IsSecure(entree)):
                                            entree=input('Quel allié voulez-vous soigner ? ')
                                        choix=int(entree)                                        
                                        while(choix not in possibilites_choix_allie):
                                            entree=input('Quel allié voulez-vous soigner ? ')
                                            while(not IsSecure(entree)):
                                                entree=input('Quel allié voulez-vous soigner ? ')
                                            choix=int(entree)
                                        team_allies[choix]=capacite_choisie(attaquant,team_allies[choix])
                                    elif(capacite_choisie in CapacitesProtectionAllie):
                                        entree=input('Quel allié voulez-vous protéger ? ')
                                        while(not IsSecure(entree)):
                                            entree=input('Quel allié voulez-vous protéger ? ')
                                        choix=int(entree)          
                                        while(choix not in possibilites_choix_allie):
                                            entree=input('Quel allié voulez-vous protéger ? ')
                                            while(not IsSecure(entree)):
                                                entree=input('Quel allié voulez-vous protéger ? ')
                                            choix=int(entree)
                                        team_allies[choix]=capacite_choisie(attaquant,team_allies[choix])
                                    else:
                                        entree=input('Quel allié voulez-vous renforcer ? ')
                                        while(not IsSecure(entree)):
                                            entree=input('Quel allié voulez-vous renforcer ? ')
                                        choix=int(entree)
                                        while(choix not in possibilites_choix_allie):
                                            entree=input('Quel allié voulez-vous renforcer ? ')
                                            while(not IsSecure(entree)):
                                                entree=input('Quel allié voulez-vous renforcer ? ')
                                            choix=int(entree)
                                        team_allies[choix]=capacite_choisie(team_allies[choix])

                                if(capacite_choisie in CapacitesRenforcementPerso):
                                    attaquant=capacite_choisie(attaquant)
                            
                                if((capacite_choisie in CapacitesResurrectionAllie) or (capacite_choisie in CapacitesRenforcementEquipe)):
                                    for x in range(len(allies_morts)):
                                        if(allies_morts[x] not in team_allies):
                                            team_allies.append(allies_morts[x])
                                    team_allies=capacite_choisie(team_allies)
                                    x=0
                                    while(x<len(team_allies)):
                                        if(team_allies[x].pv_actuels<=0):
                                            team_allies.pop(x)
                                            x-=1
                                        x+=1
                                    x=0
                                    while(x<len(allies_morts)):
                                        if(allies_morts[x].pv_actuels>0):
                                            allies_morts.pop(x)
                                            x-=1
                                        x+=1
                                        
                                if(capacite_choisie in CapacitesMulticibles):
                                    team_ennemis=capacite_choisie(attaquant,team_ennemis)
                                    
                                if(capacite_choisie in CapacitesMulticiblesMultiequipes):
                                    team_ennemis=capacite_choisie(attaquant,team_ennemis,team_allies)

                        else:
                            indice_provocation=0
                            while(team_ennemis[indice_provocation].provocation<=0):
                                if(indice_provocation<len(team_ennemis)):
                                    indice_provocation+=1
                                if(indice_provocation==len(team_ennemis)):
                                    break
                            if(indice_provocation==len(team_ennemis)):
                                indice_provocation=random.randint(0,len(team_ennemis)-1)
                                while(team_ennemis[indice_provocation].pv_actuels<=0):
                                    indice_provocation=random.randint(0,len(team_ennemis)-1)
                            cible=team_ennemis[indice_provocation]
                            print(attaquant.surnom,attaquant.attribut,' attaque ',cible.surnom,cible.attribut,' avec sa capacité : ',attaquant.capacite1Nom,' à cause de sa provocation!!\n')
                            capacite_choisie=attaquant.capacite1
                            
                            if((capacite_choisie not in CapacitesMulticibles) and (capacite_choisie not in CapacitesSoinAllieAvecHit) and (capacite_choisie not in CapacitesHitMulticibles)):
                                capacite_choisie(attaquant,cible)
                                AppliquerPassifsFinDeTour(attaquant,cible,team_allies,team_ennemis)
                                        
                            elif(capacite_choisie in CapacitesSoinAllieAvecHit):
                                capacite_choisie(attaquant,team_allies,cible)
                                AppliquerPassifsFinDeTour(attaquant,cible,team_allies,team_ennemis)
                                
                            elif(capacite_choisie in CapacitesHitMulticibles):
                                capacite_choisie(attaquant,team_ennemis,cible)
                                AppliquerPassifsFinDeTour(attaquant,cible,team_allies,team_ennemis)
                            else:
                                capacite_choisie(attaquant,team_ennemis)
                                
                else:
                    if(isAlive(team_allies)):
                        if((attaquant.presence_passif_1==1) and (attaquant.sans_passif<=0) and (attaquant.passif_1 in Passifs_debut_de_tour)):
                            team_ennemis=attaquant.passif_1(team_ennemis)
                        if((attaquant.presence_passif_2==1) and (attaquant.sans_passif<=0)  and (attaquant.passif_2 in Passifs_debut_de_tour)):
                            team_ennemis=attaquant.passif_2(team_ennemis)
                        if(attaquant.provoque<=0):
                            capacite_choisie=Choisir_capacite_speciale_sans_affichage(attaquant)
                            if((capacite_choisie not in CapacitesAnormales) or (capacite_choisie in CapacitesSoinAllieAvecHit) or (capacite_choisie in CapacitesAttaqueEnGroupe) or (capacite_choisie in CapacitesHitMulticibles)):
                                k=0
                                while(k<len(team_allies)):
                                    if (team_allies[k].pv_actuels<=0):
                                        if(team_allies[k] not in allies_morts):
                                            allies_morts.append(team_allies[k])
                                        team_allies.pop(k)
                                        k-=1
                                    k+=1
                                indice_cible=random.randint(0,len(team_allies)-1)
                                cible_allie=team_allies[indice_cible]
                                pv_avant_degats=cible_allie.pv_actuels
                                if ((capacite_choisie not in CapacitesSoinAllieAvecHit) and (capacite_choisie not in CapacitesAttaqueEnGroupe) and (capacite_choisie not in CapacitesHitMulticibles)):
                                    capacite_choisie(attaquant,cible_allie)
                                elif(capacite_choisie in CapacitesHitMulticibles):
                                    capacite_choisie(attaquant,team_allies,cible_allie)
                                else:
                                    capacite_choisie(attaquant,team_ennemis,cible_allie)
                                if(cible_allie.reflexion_dommages>0):
                                    degats_subis=pv_avant_degats-cible_allie.pv_actuels
                                    degats_renvoyes=Arrondir(cible_allie.pourcentage_reflexion_dommages*degats_subis)
                                    cible_allie.pv_actuels+=degats_renvoyes
                                    if(attaquant.immortalite<=0):
                                        print(attaquant.surnom,attaquant.attribut,' reçoit la réflexion des dégâts!!')
                                        print(attaquant.surnom,attaquant.attribut,' subit ',degats_renvoyes,' points de dégâts!!')
                                        attaquant.pv_actuels-=degats_renvoyes
                                    else:
                                        print(attaquant.surnom,attaquant.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                                    if(attaquant.pv_actuels<=0):
                                        print(attaquant.surnom,attaquant.attribut,' est mort!! \n')
                                    else:
                                        print('Il reste ',attaquant.pv_actuels,' point(s) de vie sur',attaquant.pv_max_donjons,' à ',attaquant.surnom,attaquant.attribut,'!! \n')
                                if(cible_allie.contre_attaque>0 and cible_allie.pv_actuels>0):
                                    degats_subis=pv_avant_degats-cible_allie.pv_actuels
                                    if (degats_subis<=0):
                                        degats_subis=1
                                    print(cible_allie.surnom,cible_allie.attribut,' effectue une contre-attaque sur ',attaquant.surnom,attaquant.attribut,'!!')
                                    if(attaquant.immortalite<=0):
                                        attaquant=Monstre.recoitDegats(attaquant,0.75*degats_subis)
                                        print(attaquant.surnom,attaquant.attribut,' reçoit ',0.75*degats_subis,' points de dégâts!! \n')
                                        if (cible_allie.perturbation_recup<=0):
                                            cible_allie=Monstre.etreSoigne(cible_allie,math.floor(cible_allie.vol_de_vie*0.75*degats_subis/100))
                                    else:
                                        print(attaquant.surnom,attaquant.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                                    if(attaquant.pv_actuels<=0):
                                        print(attaquant.surnom,attaquant.attribut,' est mort!! \n')
                                    else:
                                        print('Il reste ',attaquant.pv_actuels,' point(s) de vie sur',attaquant.pv_max_donjons,' à ',attaquant.surnom,attaquant.attribut,'!! \n')
                                AppliquerPassifsFinDeTour(attaquant,cible_allie,team_ennemis,team_allies)
                                        
                            else:
                                if((capacite_choisie in CapacitesSoinAllie) or (capacite_choisie in CapacitesProtectionAllie) or (capacite_choisie in CapacitesRenforcementAllie)):                                    
                                    possibilites_choix_allie=[]
                                    for n in range(len(team_ennemis)):
                                        if(team_ennemis[n].pv_actuels>0):
                                            possibilites_choix_allie.append(n)
                                    choix=random.randint(0,len(team_ennemis)-1)
                                    while(choix not in possibilites_choix_allie):
                                        choix=random.randint(0,len(team_ennemis)-1)
                                    if((capacite_choisie in CapacitesSoinAllie) or (capacite_choisie in CapacitesProtectionAllie)):
                                        team_ennemis[choix]=capacite_choisie(attaquant,team_ennemis[choix])
                                    else:
                                        team_ennemis[choix]=capacite_choisie(team_ennemis[choix])

                                if(capacite_choisie in CapacitesRenforcementPerso):
                                    attaquant=capacite_choisie(attaquant)
                            
                                if((capacite_choisie in CapacitesResurrectionAllie) or (capacite_choisie in CapacitesRenforcementEquipe)):
                                    for x in range(len(ennemis_morts)):
                                        if(ennemis_morts[x] not in team_ennemis):
                                            team_ennemis.append(ennemis_morts[x])
                                    team_ennemis=capacite_choisie(team_ennemis)
                                    x=0
                                    while(x<len(team_ennemis)):
                                        if(team_ennemis[x].pv_actuels<=0):
                                            team_ennemis.pop(x)
                                            x-=1
                                        x+=1
                                    x=0
                                    while(x<len(ennemis_morts)):
                                        if(ennemis_morts[x].pv_actuels>0):
                                            ennemis_morts.pop(x)
                                            x-=1
                                        x+=1
                                        
                                if(capacite_choisie in CapacitesMulticibles):
                                    team_allies=capacite_choisie(attaquant,team_allies)
                                    
                                if(capacite_choisie in CapacitesMulticiblesMultiequipes):
                                    team_allies=capacite_choisie(attaquant,team_allies,team_ennemis)
                                    
                        else:
                            indice_provocation=0
                            while(team_allies[indice_provocation].provocation<=0):
                                if(indice_provocation<len(team_allies)):
                                    indice_provocation+=1
                                if(indice_provocation==len(team_allies)):
                                    break
                            if(indice_provocation==len(team_allies)):
                                indice_provocation=random.randint(0,len(team_allies)-1)
                                while(team_allies[indice_provocation].pv_actuels<=0):
                                    indice_provocation=random.randint(0,len(team_allies)-1)
                            cible_allie=team_allies[indice_provocation]
                            print(attaquant.surnom,attaquant.attribut,' attaque ',cible_allie.surnom,cible_allie.attribut,' avec sa capacité : ',attaquant.capacite1Nom,' à cause de sa provocation!!\n')
                            capacite_choisie=attaquant.capacite1
                            
                            if((capacite_choisie not in CapacitesMulticibles) and (capacite_choisie not in CapacitesSoinAllieAvecHit) and (capacite_choisie not in CapacitesHitMulticibles)):
                                capacite_choisie(attaquant,cible_allie)
                                AppliquerPassifsFinDeTour(attaquant,cible_allie,team_ennemis,team_allies)
                                        
                            elif(capacite_choisie in CapacitesSoinAllieAvecHit):
                                capacite_choisie(attaquant,team_ennemis,cible_allie)
                                AppliquerPassifsFinDeTour(attaquant,cible_allie,team_ennemis,team_allies)
                                        
                            elif(capacite_choisie in CapacitesHitMulticibles):
                                capacite_choisie(attaquant,team_allies,cible_allie)
                                AppliquerPassifsFinDeTour(attaquant,cible_allie,team_ennemis,team_allies)
                            else:
                                capacite_choisie(attaquant,team_allies)
                    
            else:
                if(attaquant.tours_sommeil>0):
                    print(attaquant.surnom,attaquant.attribut,' est endormi(e)!!\n')
                else:
                    print(attaquant.surnom,attaquant.attribut,' se reprend. \n')
                attaquant.Peut_jouer=1
        else:
            print('\n ',attaquant.surnom,attaquant.attribut,'est mort!! \n')
        attaquant.tour_supplementaire_tmp-=1
        
        for z in range(len(team_allies)):
            if(team_allies[z].presence_passif_1==1):
                if((team_allies[z].passif_1 in Passifs_fin_de_tour) and (team_allies[z].sans_passif<=0)):
                    team_allies=team_allies[z].passif_1(team_allies)
            if(team_allies[z].presence_passif_2==1):
                if((team_allies[z].passif_2 in Passifs_fin_de_tour) and (team_allies[z].sans_passif<=0)):
                    team_allies=team_allies[z].passif_2(team_allies)
                
        for z in range(len(team_ennemis)):
            if(team_ennemis[z].presence_passif_1==1):
                if((team_ennemis[z].passif_1 in Passifs_fin_de_tour) and (team_ennemis[z].sans_passif<=0)):
                    team_ennemis=team_ennemis[z].passif_1(team_ennemis)
            if(team_ennemis[z].presence_passif_2==1):
                if((team_ennemis[z].passif_2 in Passifs_fin_de_tour) and (team_ennemis[z].sans_passif<=0)):
                    team_ennemis=team_ennemis[z].passif_2(team_ennemis)
        
        FinDeTour(attaquant)
        if (attaquant.perturbation_recup<=0):
            attaquant=Monstre.etreSoigne(attaquant,math.floor((attaquant.regeneration*attaquant.pv_max_donjons)/100))                         
        if(attaquant.tour_supplementaire_tmp>=0):
            print("C'est encore au tour de ", attaquant.surnom,attaquant.attribut, " : ", "\n")            
            attaquant.jauge_attaque+=100
    return [allies_morts,ennemis_morts]

'''     
#  Algorithmes Ordre des Actions :
#V 1) Debut de tour =
#V      Regeneration bonus
#V      Bombe (stun pendant 1 tour)
#V      Evaluer le stun, le sommeil et le gel
#V      Degats continus
#V      Application des bonus/malus (se fait lors de l'application des capacites)
#V      Diminuer de 1 les tours bonus/malus
#V      Si < 0, faire = 0

#V 2) Action
#V      Choisir une capacite
#V      Si aucune provocation adverse
#V      Ou si attaquant pas provoque
#V         Choisir une cible
#V      Appliquer la compétence à la cible
#V      Infliger la réflexion de dommage
#V      Activer la régénération passive si dispo et pas bloquée
#V      Evaluer contre-attaque, l'appliquer si besoin
#V          Counter COMPETENCE 1 * 75%
#V      Evaluer le tour supplémentaire
#V      Eventuellement tout recommencer
'''


def CalculTauxReussiteEffet(pourcentage,resistance,precision):
    resistance_totale=resistance-precision
    if (resistance_totale<0.15):
        resistance_totale=0.15
    taux_reussite=1-resistance_totale
    pourcentage_reussite_effet=pourcentage*taux_reussite
    return pourcentage_reussite_effet



def Procedure_attaque(attaquant,degats,cible):
    if (degats<=0):
        degats=1
    if(cible.immortalite<=0):
        if(cible.nom=='Serpent' and cible.attribut=='Vent' and attaquant.attribut=='Feu' and cible.sans_passif<=0):
            degats=Arrondir(degats/2)
        if(cible.nom=='Griffon' and cible.sans_passif<=0):
            if(cible.attribut=='Lumière' and attaquant.attribut=='Ténèbres'):
                degats=Arrondir(degats/2)
            if(cible.attribut=='Ténèbres' and attaquant.attribut=='Lumière'):
                degats=Arrondir(degats/2)
        cible=(Monstre.recoitDegats(cible,degats))
        print(cible.surnom,cible.attribut,' reçoit ',degats,' points de dégâts!! \n')
        if(cible.tours_sommeil>0):
            print(cible.surnom,cible.attribut,' se réveille!!\n')
            cible.tours_sommeil=0
            cible.sommeil=0
            cible.Peut_jouer=1
        if (attaquant.perturbation_recup<=0):
            attaquant=Monstre.etreSoigne(attaquant,math.floor(attaquant.vol_de_vie*degats/100))
    else:
        print(cible.surnom,cible.attribut,'ne subit pas de dégâts grâce à son état d Immortalité!!')
    if (cible.pv_actuels<=0):
        print(cible.surnom,cible.attribut,' est mort!! \n')
    else:
        print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv_max_donjons,' à ',cible.surnom,cible.attribut,'!! \n')


''' +1 pour certains effets pour pouvoir bénéficier des bonus/malus s'ils ne durent qu'un tour '''

def Slow_down(cible,nb_tours):
    if(cible.immunite<=0):
        print(cible.surnom,cible.attribut,' voit sa vitesse diminuer pour ',nb_tours,' tour(s)!! \n')
        cible.vitesse_actuelle-=Arrondir(0.3*cible.vitesse_actuelle)
        cible.tours_malus_vitesse=max(cible.tours_malus_vitesse,nb_tours)
    
def Speed_up(cible,nb_tours):
    if(cible.immunite_aux_bonus<=0):
        print(cible.surnom,cible.attribut,' voit sa vitesse augmenter pour ',nb_tours,' tour(s)!! \n')
        cible.vitesse_actuelle+=Arrondir(0.3*cible.vitesse_actuelle)
        cible.tours_bonus_vitesse=max(cible.tours_bonus_vitesse,nb_tours)
        
def Def_break(cible,nb_tours):
    if(cible.immunite<=0):
        print(cible.surnom,cible.attribut,' voit sa défense diminuer pour ',nb_tours,' tour(s)!! \n')
        cible.defense_actuelle-=Arrondir(0.7*cible.defense_actuelle)
        cible.tours_malus_defense=max(cible.tours_malus_defense,nb_tours)
    
def Tanky(cible,nb_tours):
    if(cible.immunite_aux_bonus<=0):
        print(cible.surnom,cible.attribut,' voit sa défense augmenter pour ',nb_tours,' tour(s)!! \n')
        cible.defense_actuelle+=Arrondir(0.7*cible.defense_actuelle)
        cible.tours_bonus_defense=max(cible.tours_bonus_defense,nb_tours)
    
def Atk_break(cible,nb_tours):
    if(cible.immunite<=0):
        print(cible.surnom,cible.attribut,' voit son attaque diminuer pour ',nb_tours,' tour(s)!! \n')
        cible.attaque_actuelle-=Arrondir(0.5*cible.attaque_actuelle)
        cible.tours_malus_attaque=max(cible.tours_malus_attaque,nb_tours+1)

def Rise(cible,nb_tours):
    if(cible.immunite_aux_bonus<=0):
        print(cible.surnom,cible.attribut,' voit son attaque augmenter pour ',nb_tours,' tour(s)!! \n')
        cible.attaque_actuelle+=Arrondir(0.5*cible.attaque_actuelle)
        cible.tours_bonus_attaque=max(cible.tours_bonus_attaque,nb_tours+1)

def Espada(cible,nb_tours):
    if(cible.immunite_aux_bonus<=0):
        print(cible.surnom,cible.attribut,' voit ses chances d\'infliger un coup critique augmenter pour ',nb_tours,' tour(s)!! \n')
        cible.taux_coup_critique_actuel+=0.3
        cible.tours_bonus_taux_coup_critique=max(cible.tours_bonus_taux_coup_critique,nb_tours+1)

def Bonus_coup_superficiel(cible,nb_tours):
    if(cible.immunite<=0):
        print(cible.surnom,cible.attribut,' voit ses chances d\'infliger un coup superficiel augmenter pour ',nb_tours,' tour(s)!! \n')
        cible.bonus_taux_coup_superficiel+=0.5
        cible.tours_bonus_taux_coup_superficiel=max(cible.tours_bonus_taux_coup_superficiel,nb_tours+1)
    
def Degats_continus(cible,nb_marques,nb_tours):
    if(cible.immunite<=0):
        if(nb_marques==1):
            print(cible.surnom,cible.attribut,' reçoit une marque de dégats continus pour ',nb_tours,' tour(s)!! \n')
        elif(nb_marques==2):
            print(cible.surnom,cible.attribut,' reçoit deux marques de dégats continus pour ',nb_tours,' tour(s)!! \n')
        elif(nb_marques==3):
            print(cible.surnom,cible.attribut,' reçoit trois marques de dégâts continus pour ',nb_tours,' tour(s)!! \n')
        cible.marques_degats_continus+=nb_marques
        cible.intensite_degats_continus=max(nb_tours,cible.intensite_degats_continus)
    
def Immunity(cible,nb_tours):
    if(cible.immunite_aux_bonus<=0):
        print(cible.surnom,cible.attribut,' reçoit l\'immunité aux effets négatifs pour ',nb_tours,' tour(s)!! \n')
        cible.immunite=1
        cible.tours_immunite=max(cible.tours_immunite,nb_tours)

def Sommeil(cible,nb_tours):
    if(cible.immunite<=0):
        print(cible.surnom,cible.attribut,' s\'endort pour ',nb_tours,' tour(s)!! \n')
        cible.sommeil=1
        cible.tours_sommeil=max(cible.tours_sommeil,nb_tours)

def Perturbation_recup(cible,nb_tours):
    if(cible.immunite<=0):
        print(cible.surnom,cible.attribut,' voit sa récupération de points de vie perturbée pour ',nb_tours,' tour(s)!! \n')
        cible.perturbation_recup=1
        cible.tours_perturbation_recup=max(cible.tours_perturbation_recup,nb_tours)

def Retirer_un_bonus(cible):
    if(NbEffetsRenforcement(cible)>0):
        print(cible.surnom,cible.attribut,'perd l\'un de ses bonus!! \n')
        if(cible.tours_bonus_attaque>0):
            cible.tours_bonus_attaque=0
            if(cible.tours_malus_attaque<=0):
                cible.attaque_actuelle=cible.attaque_max_donjons
            else:
                cible.attaque_actuelle=cible.attaque_max_donjons-(0.5*cible.attaque_actuelle)
        elif(cible.tours_bonus_defense>0):
            cible.tours_bonus_defense=0
            if(cible.tours_malus_defense<=0):
                cible.defense_actuelle=cible.defense_max_donjons
            else:
                cible.defense_actuelle=cible.defense_max_donjons-(0.5*cible.defense_actuelle)
        elif(cible.tours_bonus_vitesse>0):
            cible.tours_bonus_vitesse=0
            if(cible.tours_malus_vitesse<=0):
                cible.vitesse_actuelle=cible.vitesse_max_donjons
            else:
                cible.vitesse_actuelle=cible.vitesse_max_donjons-(0.5*cible.vitesse_actuelle)
        elif(cible.tours_bonus_taux_coup_critique>0):
            cible.tours_bonus_taux_coup_critique=0
            cible.taux_coup_critique_actuel=cible.taux_coup_critique
        elif(cible.tours_regeneration>0):
            cible.tours_regeneration=0
        elif(cible.tours_contre_attaque>0):
            cible.tours_contre_attaque=0
        elif(cible.tours_immunite>0):
            cible.tours_immunite=0
            cible.immunite=0
        elif(cible.tours_invincibilite>0):
            cible.tours_invincibilite=0
            cible.invincibilite=0
        elif(cible.tours_immortalite>0):
            cible.tours_immortalite=0
            cible.immortalite=0        
        elif(cible.tours_reflexion_dommages>0):
            cible.tours_reflexion_dommages=0
        elif(cible.tours_endurance>0):
            cible.tours_endurance=0
            cible.endurance=0
        elif(cible.tours_provocation>0):
            cible.tours_provocation=0
            cible.provocation=0
            
def NbEffetsRenforcement(cible):
    nb_effets_renforcements=0
    if(cible.tours_bonus_attaque>0):
        nb_effets_renforcements+=1
    elif(cible.tours_bonus_defense>0):
        nb_effets_renforcements+=1
    elif(cible.tours_bonus_vitesse>0):
        nb_effets_renforcements+=1
    elif(cible.tours_bonus_taux_coup_critique>0):
        nb_effets_renforcements+=1
    elif(cible.tours_regeneration>0):
        nb_effets_renforcements+=1
    elif(cible.tours_contre_attaque>0):
        nb_effets_renforcements+=1
    elif(cible.tours_immunite>0):
        nb_effets_renforcements+=1
    elif(cible.tours_invincibilite>0):
        nb_effets_renforcements+=1
    elif(cible.tours_immortalite>0):
        nb_effets_renforcements+=1   
    elif(cible.tours_reflexion_dommages>0):
        nb_effets_renforcements+=1
    elif(cible.tours_endurance>0):
        nb_effets_renforcements+=1
    elif(cible.tours_provocation>0):
        nb_effets_renforcements+=1
    return nb_effets_renforcements

def Retirer_un_malus(perso):
    if(NbEffetsNocifs(perso)>0):
        print(perso.surnom,perso.attribut,'perd l\'un de ses bonus!! \n')
        if(perso.tours_malus_attaque>0):
            perso.tours_malus_attaque=0
            if(perso.tours_bonus_attaque<=0):
                perso.attaque_actuelle=perso.attaque_max_donjons
            else:
                perso.attaque_actuelle=perso.attaque_max_donjons+(0.5*perso.attaque_actuelle)
        elif(perso.tours_malus_defense>0):
            perso.tours_malus_defense=0
            if(perso.tours_bonus_defense<=0):
                perso.defense_actuelle=perso.defense_max_donjons
            else:
                perso.defense_actuelle=perso.defense_max_donjons+(0.7*perso.defense_actuelle)
        elif(perso.tours_malus_vitesse>0):
            perso.tours_malus_vitesse=0
            if(perso.tours_bonus_vitesse<=0):
                perso.vitesse_actuelle=perso.vitesse_max_donjons
            else:
                perso.vitesse_actuelle=perso.vitesse_max_donjons+(0.3*perso.vitesse_actuelle)
        elif(perso.tours_bonus_taux_coup_superficiel>0):
            perso.bonus_taux_coup_superficiel=0
            perso.tours_bonus_taux_coup_superficiel=0
        elif(perso.tours_immunite_aux_bonus>0):
            perso.immunite_aux_bonus=0
            perso.tours_immunite_aux_bonus=0
        elif(perso.tours_avant_explosion>0):
            perso.bombe=0
            perso.tours_avant_explosion=0
        elif(perso.tours_provoque>0):
            perso.provoque=0
            perso.tours_provoque=0
        elif(perso.stun>0):
            perso.stun=0
            perso.Peut_jouer=1
        elif(perso.gel>0):
            perso.gel=0
            perso.Peut_jouer=1
        elif(perso.tours_sommeil>0):
            perso.sommeil=0
            perso.tours_sommeil=0
            perso.Peut_jouer=1
        elif(perso.intensite_degats_continus>0):
            perso.marques_degats_continus=0
            perso.intensite_degats_continus=0
        elif(perso.tours_perturbation_recup>0):
            perso.perturbation_recup=0
            perso.tours_perturbation_recup=0
        elif(perso.tours_silencieux>0):
            perso.silencieux=0
            perso.tours_silencieux=0
        elif(perso.tours_marque>0 or perso.marque>0):
            perso.marque=0
            perso.tours_marque=0
        elif(perso.tours_sans_passif>0):
            perso.sans_passif=0
            perso.tours_sans_passif=0
    return perso

def NbEffetsNocifs(perso):
    nb_effets_nocifs=0
    if(perso.tours_malus_attaque>0):
        nb_effets_nocifs+=1
    if(perso.tours_malus_defense>0):
        nb_effets_nocifs+=1
    if(perso.tours_malus_vitesse>0):
        nb_effets_nocifs+=1
    if(perso.tours_bonus_taux_coup_superficiel>0):
        nb_effets_nocifs+=1
    if(perso.tours_immunite_aux_bonus>0):
        nb_effets_nocifs+=1
    if(perso.tours_avant_explosion>0):
        nb_effets_nocifs+=1
    if(perso.tours_provoque>0):
        nb_effets_nocifs+=1
    if(perso.stun>0):
        nb_effets_nocifs+=1
    if(perso.gel>0):
        nb_effets_nocifs+=1
    if(perso.sommeil>0):
        nb_effets_nocifs+=1
    if(perso.marques_degats_continus>0):
        nb_effets_nocifs+=1
    if(perso.perturbation_recup>0):
        nb_effets_nocifs+=1
    if(perso.silencieux>0):
        nb_effets_nocifs+=1
    if(perso.marque>0):
        nb_effets_nocifs+=1
    if(perso.sans_passif>0):
        nb_effets_nocifs+=1
    return nb_effets_nocifs
    

def SoignerDeTousLesMaux(perso):
    perso.tours_malus_attaque=0
    if(perso.tours_bonus_attaque<=0):
        perso.attaque_actuelle=perso.attaque_max_donjons
    else:
        perso.attaque_actuelle=perso.attaque_max_donjons+(0.5*perso.attaque_actuelle)
    perso.tours_malus_defense=0
    if(perso.tours_bonus_defense<=0):
        perso.defense_actuelle=perso.defense_max_donjons
    else:
        perso.defense_actuelle=perso.defense_max_donjons+(0.7*perso.defense_actuelle)
    perso.tours_malus_vitesse=0
    if(perso.tours_bonus_vitesse<=0):
        perso.vitesse_actuelle=perso.vitesse_max_donjons
    else:
        perso.vitesse_actuelle=perso.vitesse_max_donjons+(0.3*perso.vitesse_actuelle)
    perso.bonus_taux_coup_superficiel=0
    perso.tours_bonus_taux_coup_superficiel=0
    perso.immunite_aux_bonus=0
    perso.tours_immunite_aux_bonus=0
    perso.bombe=0
    perso.tours_avant_explosion=0
    perso.provoque=0
    perso.tours_provoque=0
    perso.stun=0
    perso.Peut_jouer=1
    perso.gel=0
    perso.sommeil=0
    perso.tours_sommeil=0
    perso.marques_degats_continus=0
    perso.intensite_degats_continus=0
    perso.perturbation_recup=0
    perso.tours_perturbation_recup=0
    perso.silencieux=0
    perso.tours_silencieux=0
    perso.marque=0
    perso.tours_marque=0
    perso.sans_passif=0
    perso.tours_sans_passif=0
    return perso
    
def SoignerDeTousLesBiens(perso):
    perso.tours_bonus_attaque=0
    if(perso.tours_malus_attaque<=0):
        perso.attaque_actuelle=perso.attaque_max_donjons
    else:
        perso.attaque_actuelle=perso.attaque_max_donjons-(0.5*perso.attaque_actuelle)
    perso.tours_bonus_defense=0
    if(perso.tours_malus_defense<=0):
        perso.defense_actuelle=perso.defense_max_donjons
    else:
        perso.defense_actuelle=perso.defense_max_donjons-(0.7*perso.defense_actuelle)
    perso.tours_bonus_vitesse=0
    if(perso.tours_malus_vitesse<=0):
        perso.vitesse_actuelle=perso.vitesse_max_donjons
    else:
        perso.vitesse_actuelle=perso.vitesse_max_donjons-(0.3*perso.vitesse_actuelle)
    perso.tours_bonus_taux_coup_critique=0
    perso.taux_coup_critique_actuel=perso.taux_coup_critique_max_donjons
    if(perso.tours_regeneration>0):
        perso.tours_regeneration=0
        perso.regeneration=0
    if(perso.tours_contre_attaque>0):
        perso.tours_contre_attaque=0
        perso.contre_attaque=0
    if(perso.tours_immunite>0):
        perso.tours_immunite=0
        perso.immunite=0
    if(perso.tours_invincibilite>0):
        perso.tours_invincibilite=0
        perso.invincibilite=0
    if(perso.tours_immortalite>0):
        perso.tours_immortalite=0
        perso.immortalite=0        
    if(perso.tours_reflexion_dommages>0):
        perso.tours_reflexion_dommages=0
        perso.reflexion_dommages=0
    if(perso.tours_endurance>0):
        perso.tours_endurance=0
        perso.endurance=0
    if(perso.tours_provocation>0):
        perso.tours_provocation=0
        perso.provocation=0
    return perso


def Initialiser_stats_max_donjons(monstre):
    monstre.pv_max_donjons=monstre.pv
    monstre.attaque_max_donjons=monstre.attaque
    monstre.defense_max_donjons=monstre.defense
    monstre.vitesse_max_donjons=monstre.vitesse
    monstre.taux_coup_critique_max_donjons=monstre.taux_coup_critique
    monstre.dommages_critiques_max_donjons=monstre.dommages_critiques
    monstre.resistance_max_donjons=monstre.resistance
    monstre.precision_max_donjons=monstre.precision
    
    monstre.immunite_max_donjons=monstre.immunite
    monstre.tours_immunite_max_donjons=monstre.tours_immunite
    monstre.vol_de_vie_max_donjons=monstre.vol_de_vie
    monstre.regeneration_max_donjons=monstre.regeneration
    monstre.taux_contre_attaque_max_donjons=monstre.taux_contre_attaque
    monstre.chances_de_stun_max_donjons=monstre.chances_de_stun
    monstre.tour_supplementaire_max_donjons=monstre.tour_supplementaire
    monstre.chances_tour_supplementaire_max_donjons=monstre.chances_tour_supplementaire
    monstre.immortalite_max_donjons=monstre.immortalite
    monstre.tours_immortalite_max_donjons=monstre.tours_immortalite
        
def Preparer_au_combat(monstre):
    if(monstre!=0):
        Initialiser_stats_max_donjons(monstre) # Réinitialise les stats max donjons = pas de cumulation
    
        monstre.pv_max_donjons+=monstre.bonus_de_runes_en_pv
        monstre.pv_max_donjons+=Arrondir(monstre.pv*monstre.bonus_de_runes_en_pourcentage_de_pv)
        monstre.attaque_max_donjons+=monstre.bonus_de_runes_en_attaque
        monstre.attaque_max_donjons+=Arrondir(monstre.attaque*monstre.bonus_de_runes_en_pourcentage_de_attaque)
        monstre.defense_max_donjons+=monstre.bonus_de_runes_en_defense
        monstre.defense_max_donjons+=Arrondir(monstre.defense*monstre.bonus_de_runes_en_pourcentage_de_defense)
        monstre.vitesse_max_donjons+=monstre.bonus_de_runes_en_vitesse            
        monstre.taux_coup_critique_max_donjons+=monstre.bonus_de_runes_en_taux_de_coup_critique
        monstre.dommages_critiques_max_donjons+=monstre.bonus_de_runes_en_dommages_critiques
        monstre.resistance_max_donjons+=monstre.bonus_de_runes_en_resistance
        monstre.precision_max_donjons+=monstre.bonus_de_runes_en_precision
        monstre.immunite_max_donjons+=monstre.bonus_de_runes_en_immunite
        monstre.tours_immunite_max_donjons+=monstre.bonus_de_runes_en_tours_immunite
        monstre.vol_de_vie_max_donjons+=monstre.bonus_de_runes_en_vol_de_vie
        monstre.regeneration_max_donjons+=monstre.bonus_de_runes_en_regeneration
        monstre.taux_contre_attaque_max_donjons+=monstre.bonus_de_runes_en_taux_contre_attaque
        monstre.chances_de_stun_max_donjons+=monstre.bonus_de_runes_en_chances_de_stun
        monstre.tour_supplementaire_max_donjons+=monstre.bonus_de_runes_en_tour_supplementaire
        monstre.chances_tour_supplementaire_max_donjons+=monstre.bonus_de_runes_en_chances_tour_supplementaire
        monstre.immortalite_max_donjons+=monstre.bonus_de_runes_en_immortalite
        monstre.tours_immortalite_max_donjons+=monstre.bonus_de_runes_en_tours_immortalite
    
        monstre.pv_actuels=monstre.pv_max_donjons
        monstre.attaque_actuelle=monstre.attaque_max_donjons
        monstre.defense_actuelle=monstre.defense_max_donjons
        monstre.vitesse_actuelle=monstre.vitesse_max_donjons
        monstre.taux_coup_critique_actuel=monstre.taux_coup_critique_max_donjons
        monstre.dommages_critiques_actuels=monstre.dommages_critiques_max_donjons
        monstre.resistance_actuelle=monstre.resistance_max_donjons
        monstre.precision_actuelle=monstre.precision_max_donjons
        monstre.immunite=monstre.immunite_max_donjons
        monstre.tours_immunite=monstre.tours_immunite_max_donjons
        monstre.vol_de_vie=monstre.vol_de_vie_max_donjons
        monstre.regeneration=monstre.regeneration_max_donjons
        monstre.taux_contre_attaque=monstre.taux_contre_attaque_max_donjons
        monstre.chances_de_stun=monstre.chances_de_stun_max_donjons
        monstre.tour_supplementaire=monstre.tour_supplementaire_max_donjons
        monstre.chances_tour_supplementaire=monstre.chances_tour_supplementaire_max_donjons
        monstre.immortalite=monstre.immortalite_max_donjons
        monstre.tours_immortalite=monstre.tours_immortalite_max_donjons
    
    return monstre
    
    

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





# Total : 117 monstres (non éveillés)
# Actuellement 40 de faits  
#   77 RESTANTS 



        
'''     
class Samourai(Monstre):
    def __init__(self):
        # acier, multilame, diamant, puis avec éveil platine
        self.capacite1=Samourai.LameAcier
        self.capacite2=Samourai.Multilame
        self.capacite1Nom='Lame Acier'
        self.capacite2Nom='Multilame'
        self.nb_capacites=2
        self.Trecharge1=1
        self.Trecharge2=3
        self.attente1=0
        self.attente2=0
        self.etatCap1='dispo'
        self.etatCap2='dispo'
        element=['Feu','Eau','Vent']
        indice_element=random.randint(0,2)
        Monstre.__init__(self,'Samourai',element[indice_element],3,1,160,160,70,0,20)
        self.taux_coup_critique=10
        self.vol_de_vie=15
        
    def LameAcier(samourai,cible):
        print(samourai.nom,' attaque ',cible.nom,'!!')
        if (PrioriteElementaire(samourai,cible)==True):
            degats=samourai.attaque_actuelle
            print('Dégâts augmentés par avantage élémentaire!!')
        else:
            degats=samourai.attaque_actuelle-cible.defense_actuelle
        if (degats<=0):
            degats=1
        coup_critique=random.randint(1,100)
        if(coup_critique<=samourai.taux_coup_critique):
            print('Coup critique!!')
            degats*=2
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.nom,' reçoit ',degats,' points de dégâts!! \n')
        else:
            print(cible.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if(cible.pv_actuels<=0):
            print(cible.nom,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv,' à ',cible.nom,'!! \n')
        samourai=Monstre.etreSoigne(samourai,math.floor(samourai.vol_de_vie*degats/100))
        return cible
        
    def Multilame(samourai,equipe_ennemie):
        print(samourai.nom,'attaque toute l équipe ennemie!!')
        nb_cibles=len(equipe_ennemie)-1
        i=0
        while(i<3):
            if((equipe_ennemie[0].pv_actuels>0) or (equipe_ennemie[1].pv_actuels>0) or (equipe_ennemie[2].pv_actuels>0)):
                indice_cible=random.randint(0,nb_cibles)
                if (PrioriteElementaire(samourai,equipe_ennemie[indice_cible])==True):
                    degats=samourai.attaque_actuelle
                    print('Dégâts augmentés par avantage élémentaire!!')
                else:
                    degats=samourai.attaque_actuelle-equipe_ennemie[indice_cible].defense_actuelle
                while(equipe_ennemie[indice_cible].pv_actuels<=0):
                    indice_cible=random.randint(0,nb_cibles)
                    if (PrioriteElementaire(samourai,equipe_ennemie[indice_cible])==True):
                        degats=samourai.attaque_actuelle
                        print('Dégâts augmentés par avantage élémentaire!!')
                    else:
                        degats=samourai.attaque_actuelle-equipe_ennemie[indice_cible].defense_actuelle
                if (degats<=0):
                    degats=1
                coup_critique=random.randint(1,100)
                if(coup_critique<=samourai.taux_coup_critique):
                    print('Coup critique!!')
                    degats*=2
                print(samourai.nom,' attaque ',equipe_ennemie[indice_cible].nom,'!!')
                if(equipe_ennemie[indice_cible].immortalite<=0):
                    equipe_ennemie[indice_cible]=(Monstre.recoitDegats(equipe_ennemie[indice_cible],degats))
                    print(equipe_ennemie[indice_cible].nom,' reçoit ',degats,' points de dégâts!! \n')
                else:
                    print(equipe_ennemie[indice_cible].nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                if(equipe_ennemie[indice_cible].pv_actuels<=0):
                    print(equipe_ennemie[indice_cible].nom,' est mort!! \n')
                else:
                    print('Il reste ',equipe_ennemie[indice_cible].pv_actuels,' point(s) de vie sur ', equipe_ennemie[indice_cible].pv,' à ',equipe_ennemie[indice_cible].nom,'!! \n')
                samourai=Monstre.etreSoigne(samourai,math.floor(samourai.vol_de_vie*degats/100))
            i+=1
        return equipe_ennemie
    
    def Multilame_cible_unique(samourai,ennemi):
        i=0
        while(i<3):
            if (PrioriteElementaire(samourai,ennemi)==True):
                degats=samourai.attaque_actuelle
                print('Dégâts augmentés par avantage élémentaire!!')
            else:
                degats=samourai.attaque_actuelle-ennemi.defense_actuelle
            if(degats<=0):
                degats=1
            coup_critique=random.randint(1,100)
            if(coup_critique<=samourai.taux_coup_critique):
                print('Coup critique!!')
                degats*=2
            print(samourai.nom,' attaque ',ennemi.nom,'!!')
            if(ennemi.immortalite<=0):
                ennemi=(Monstre.recoitDegats(ennemi,degats))
                print(ennemi.nom,' reçoit ',degats,' points de dégâts!! \n')
            else:
                print(ennemi.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
            if(ennemi.pv_actuels<=0):
                print(ennemi.nom,' est mort!! \n')
            else:
                print('Il reste ',ennemi.pv_actuels,' point(s) de vie sur',ennemi.pv,' à ',ennemi.nom,'!! \n')
            samourai=Monstre.etreSoigne(samourai,math.floor(samourai.vol_de_vie*degats/100))
            i+=1
        return ennemi


class Paladin(Monstre):
    def __init__(self):
        self.capacite1=Paladin.Marteau
        self.capacite2=Paladin.Bouclier
        self.capacite1Nom='Coup de Marteau'
        self.capacite2Nom='Bouclier'
        self.nb_capacites=2
        self.Trecharge1=1
        self.Trecharge2=4
        self.attente1=0
        self.attente2=0
        self.etatCap1='dispo'
        self.etatCap2='dispo'      
        element=['Feu','Eau','Vent']
        indice_element=random.randint(0,2)
        Monstre.__init__(self,'Paladin',element[indice_element],3,1,200,200,15,30,5)
        self.vol_de_vie=15
        self.regeneration=15
        
    def Marteau(paladin,cible):
        chance=random.randint(1,4)
        if (PrioriteElementaire(paladin,cible)==True):
            degats=paladin.attaque_actuelle
            print('Dégâts augmentés par avantage élémentaire!!')
        else:
            degats=paladin.attaque_actuelle-cible.defense_actuelle
        if (degats<=0):
            degats=1
        if(chance==1):
            degats+=paladin.defense_actuelle
        coup_critique=random.randint(1,100)
        if(coup_critique<=paladin.taux_coup_critique):
            print('Coup critique!!')
            degats*=2
        print(paladin.nom,' attaque ',cible.nom,'!!')
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.nom,' reçoit ',degats,' points de dégâts!! \n')
        else:
            print(cible.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if(cible.pv_actuels<=0):
            print(cible.nom,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv,' à ',cible.nom,'!! \n')
        paladin=Monstre.etreSoigne(paladin,math.floor(paladin.vol_de_vie*degats/100))
        return cible
        
    def Bouclier(paladin,allie):
        montant=paladin.defense
        allie.pv_actuels+=montant
        print(allie.nom,'reçoit un bouclier pouvant bloquer jusqu à ',montant,'points de dégâts!! \n')
        return allie


class Demon(Monstre):
    def __init__(self):
        self.capacite1=Demon.LameOmbre
        self.capacite2=Demon.TrouNoir
        self.capacite3=Demon.Apocalypse
        self.capacite1Nom='Lame d Ombre'
        self.capacite2Nom='Trou Noir'
        self.capacite3Nom='Apocalypse'
        self.nb_capacites=3
        self.Trecharge1=1
        self.Trecharge2=3
        self.Trecharge3=5
        self.attente1=0
        self.attente2=0
        self.attente3=0
        self.etatCap1='dispo'
        self.etatCap2='dispo'
        self.etatCap3='dispo'
        Monstre.__init__(self,'Démon','Ténèbres',5,1,160,160,120,50,20)
        self.vol_de_vie=20
        
    def LameOmbre(demon,cible):
        print(demon.nom,' attaque ',cible.nom,'!!')
        if (PrioriteElementaire(demon,cible)==True):
            degats=demon.attaque_actuelle
            print('Dégâts augmentés par avantage élémentaire!!')
        else:
            degats=demon.attaque_actuelle-cible.defense_actuelle
        if (degats<=0):
            degats=1
        coup_critique=random.randint(1,100)
        if(coup_critique<=demon.taux_coup_critique):
            print('Coup critique!!')
            degats*=2
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.nom,' reçoit ',degats,' points de dégâts!! \n')
        else:
            print(cible.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if(cible.pv_actuels<=0):
            print(cible.nom,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv,' à ',cible.nom,'!! \n')
        demon=Monstre.etreSoigne(demon,math.floor(demon.vol_de_vie*degats/100))
        return cible
        
    def TrouNoir(demon,equipe_ennemie):
        print(demon.nom,'engloutit toute l équipe ennemie dans un Trou Noir!!')
        i=0
        while(i<3):
            if(equipe_ennemie[i].pv_actuels>0):
                if (PrioriteElementaire(demon,equipe_ennemie[i])==True):
                    degats=demon.attaque_actuelle+math.floor((equipe_ennemie[i].pv)/4)
                    print('Dégâts augmentés par avantage élémentaire!!')
                else:
                    degats=demon.attaque_actuelle+math.floor((equipe_ennemie[i].pv)/4)-equipe_ennemie[i].defense_actuelle
                if (demon.attaque_actuelle<=equipe_ennemie[i].defense_actuelle):
                    degats=math.floor((equipe_ennemie[i].pv)/4)
                coup_critique=random.randint(1,100)
                if(coup_critique<=demon.taux_coup_critique):
                    print('Coup critique!!')
                    degats+=demon.attaque_actuelle
                if(equipe_ennemie[i].immortalite<=0):
                    equipe_ennemie[i]=(Monstre.recoitDegats(equipe_ennemie[i],degats))
                    print(equipe_ennemie[i].nom,' reçoit ',degats,' points de dégâts!! \n')
                else:
                    print(equipe_ennemie[i].nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                if(equipe_ennemie[i].pv_actuels<=0):
                    print(equipe_ennemie[i].nom,' est mort!! \n')
                else:
                    print('Il reste ',equipe_ennemie[i].pv_actuels,' point(s) de vie sur ', equipe_ennemie[i].pv,' à ',equipe_ennemie[i].nom,'!! \n')
                demon=Monstre.etreSoigne(demon,math.floor(demon.vol_de_vie*degats/100))
            i+=1
        return equipe_ennemie
        
    def TrouNoir_cible_unique(demon,cible_unique):
        print(demon.nom,'engloutit',cible_unique.nom,'dans un Trou Noir!!')
        if(cible_unique.pv_actuels>0):
            if (PrioriteElementaire(demon,cible_unique)==True):
                degats=demon.attaque_actuelle+math.floor((cible_unique.pv)/4)
                print('Dégâts augmentés par avantage élémentaire!!')
            else:
                degats=demon.attaque_actuelle+math.floor((cible_unique.pv)/4)-cible_unique.defense_actuelle
            if (demon.attaque_actuelle<=cible_unique.defense_actuelle):
                degats=math.floor((cible_unique.pv)/4)
            coup_critique=random.randint(1,100)
            if(coup_critique<=demon.taux_coup_critique):
                print('Coup critique!!')
                degats+=demon.attaque_actuelle
            if(cible_unique.immortalite<=0):
                cible_unique=(Monstre.recoitDegats(cible_unique,degats))
                print(cible_unique.nom,' reçoit ',degats,' points de dégâts!! \n')
            else:
                print(cible_unique.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
            if(cible_unique.pv_actuels<=0):
                print(cible_unique.nom,' est mort!! \n')
            else:
                print('Il reste ',cible_unique.pv_actuels,' point(s) de vie sur ', cible_unique.pv,' à ',cible_unique.nom,'!! \n')
            demon=Monstre.etreSoigne(demon,math.floor(demon.vol_de_vie*degats/100))
        return cible_unique
        
    def Apocalypse(demon,equipe_ennemie):
        print(demon.nom,'provoque la fin du monde!!')
        i=0
        while(i<3):
            if(equipe_ennemie[i].pv_actuels>0):
                if (PrioriteElementaire(demon,equipe_ennemie[i])==True):
                    degats=demon.attaque_actuelle+math.floor((equipe_ennemie[i].pv)/2)
                    print('Dégâts augmentés par avantage élémentaire!!')
                else:
                    degats=math.floor((equipe_ennemie[i].pv)/2)
                coup_critique=random.randint(1,100)
                if(coup_critique<=demon.taux_coup_critique):
                    print('Coup critique!!')
                    degats+=demon.attaque_actuelle
                if(equipe_ennemie[i].immortalite<=0):
                    equipe_ennemie[i]=(Monstre.recoitDegats(equipe_ennemie[i],degats))
                    print(equipe_ennemie[i].nom,' reçoit ',degats,' points de dégâts!! \n')
                else:
                    print(equipe_ennemie[i].nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                if(equipe_ennemie[i].pv_actuels<=0):
                    print(equipe_ennemie[i].nom,' est mort!! \n')
                else:
                    print('Il reste ',equipe_ennemie[i].pv_actuels,' point(s) de vie sur ', equipe_ennemie[i].pv,' à ',equipe_ennemie[i].nom,'!! \n')
                demon=Monstre.etreSoigne(demon,math.floor(demon.vol_de_vie*degats/100))
            i+=1
        return equipe_ennemie
        
    def Apocalypse_cible_unique(demon,cible_unique):
        print(demon.nom,'provoque la fin du monde!!')
        if(cible_unique.pv_actuels>0):
            if (PrioriteElementaire(demon,cible_unique)==True):
                degats=demon.attaque_actuelle+math.floor((cible_unique.pv)/2)
                print('Dégâts augmentés par avantage élémentaire!!')
            else:
                degats=math.floor((cible_unique.pv)/2)
            coup_critique=random.randint(1,100)
            if(coup_critique<=demon.taux_coup_critique):
                print('Coup critique!!')
                degats+=demon.attaque_actuelle
            if(cible_unique.immortalite<=0):
                cible_unique=(Monstre.recoitDegats(cible_unique,degats))
                print(cible_unique.nom,' reçoit ',degats,' points de dégâts!! \n')
            else:
                print(cible_unique.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
            if(cible_unique.pv_actuels<=0):
                print(cible_unique.nom,' est mort!! \n')
            else:
                print('Il reste ',cible_unique.pv_actuels,' point(s) de vie sur ', cible_unique.pv,' à ',cible_unique.nom,'!! \n')
            demon=Monstre.etreSoigne(demon,math.floor(demon.vol_de_vie*degats/100))
        return cible_unique
        


class Pretresse_celeste(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent','Lumière','Ténèbres']
        indice_element=random.randint(0,4)
        attribut=element[indice_element]
        if (attribut=='Feu'):
            self.capacite1=Pretresse_celeste.ManaDrain
            self.capacite1Nom='Drain de Mana'
            self.capacite2=Pretresse_celeste.Invincibilite
            self.capacite2Nom='Invincibilité'
            self.capacite3=Pretresse_celeste.GuerisonCeleste
            self.capacite3Nom='Guérison Céleste'
            self.capacite4=Pretresse_celeste.BenedictionFeu
            self.capacite4Nom='Bénédiction de la Déesse des Flammes'
        if (attribut=='Eau'):
            self.capacite1=Pretresse_celeste.ManaDrain
            self.capacite1Nom='Drain de Mana'
            self.capacite2=Pretresse_celeste.Indestructibilite
            self.capacite2Nom='Indestructibilité'
            self.capacite3=Pretresse_celeste.GuerisonCeleste
            self.capacite3Nom='Guérison Céleste'
            self.capacite4=Pretresse_celeste.BenedictionEau
            self.capacite4Nom='Bénédiction de la Déesse des Eaux'
        if (attribut=='Vent'):
            self.capacite1=Pretresse_celeste.ManaDrain
            self.capacite1Nom='Drain de Mana'
            self.capacite2=Pretresse_celeste.Insensibilite
            self.capacite2Nom='Insensibilité'
            self.capacite3=Pretresse_celeste.GuerisonCeleste
            self.capacite3Nom='Guérison Céleste'
            self.capacite4=Pretresse_celeste.BenedictionVent
            self.capacite4Nom='Bénédiction de la Déesse des Vents'
        if (attribut=='Lumière'):
            self.capacite1=Pretresse_celeste.ManaDrain
            self.capacite1Nom='Drain de Mana'
            self.capacite2=Pretresse_celeste.Immortalite
            self.capacite2Nom='Immortalité'
            self.capacite3=Pretresse_celeste.GuerisonCeleste
            self.capacite3Nom='Guérison Céleste'
            self.capacite4=Pretresse_celeste.BenedictionLumiere
            self.capacite4Nom='Bénédiction de la Déesse des Cieux'
        if (attribut=='Ténèbres'):
            self.capacite1=Pretresse_celeste.ManaDrain
            self.capacite1Nom='Drain de Mana'
            self.capacite2=Pretresse_celeste.Impunite
            self.capacite2Nom='Impunité'
            self.capacite3=Pretresse_celeste.GuerisonCeleste
            self.capacite3Nom='Guérison Céleste'
            self.capacite4=Pretresse_celeste.BenedictionTenebres
            self.capacite4Nom='Bénédiction de la Déesse des Ombres'
        self.nb_capacites=4
        self.Trecharge1=1
        self.Trecharge2=4
        self.Trecharge3=2
        self.Trecharge4=3
        self.attente1=0
        self.attente2=0
        self.attente3=0
        self.attente4=0
        self.etatCap1='dispo'
        self.etatCap2='dispo'
        self.etatCap3='dispo'
        self.etatCap4='dispo'
        if (attribut=='Feu'):
            Monstre.__init__(self,'Prêtresse Céleste du Feu',element[indice_element],6,1,330,330,30,20,20)
            self.regeneration=20
        if (attribut=='Eau'):
            Monstre.__init__(self,'Prêtresse Céleste de l Eau',element[indice_element],6,1,340,340,20,20,20)
            self.regeneration=20
        if (attribut=='Vent'):
            Monstre.__init__(self,'Prêtresse Céleste du Vent',element[indice_element],6,1,330,330,20,20,30)
            self.regeneration=20
        if (attribut=='Lumière'):
            Monstre.__init__(self,'Prêtresse Céleste de la Lumière',element[indice_element],6,1,330,330,20,20,20)
            self.regeneration=30
        if (attribut=='Ténèbres'):
            Monstre.__init__(self,'Prêtresse Céleste de l Ombre',element[indice_element],6,1,330,330,20,30,20)
            self.regeneration=20
        self.taux_coup_critique=10
        self.vol_de_vie=50
    
    def ManaDrain(pretresse,cible):
        if (PrioriteElementaire(pretresse,cible)==True):
            degats=pretresse.attaque_actuelle+math.floor(pretresse.pv/5)
            print('Dégâts augmentés par avantage élémentaire!!')
        else:
            degats=(pretresse.attaque_actuelle-cible.defense_actuelle)+math.floor(pretresse.pv/5)
        if (pretresse.attaque_actuelle<=cible.defense_actuelle):
            degats=math.floor(pretresse.pv/5)
        coup_critique=random.randint(1,100)
        if(coup_critique<=pretresse.taux_coup_critique):
            print('Coup critique!!')
            degats*=2
        print(pretresse.nom,' attaque ',cible.nom,'!!')
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.nom,' reçoit ',degats,' points de dégâts!! \n')
        else:
            print(cible.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if(cible.pv_actuels<=0):
            print(cible.nom,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv,' à ',cible.nom,'!! \n')
        pretresse=Monstre.etreSoigne(pretresse,math.floor(pretresse.vol_de_vie*degats/100))
        return cible        
            
    def Invincibilite(pretresse,equipe):
        for i in range(len(equipe)):
            equipe[i].invincibilite=1
        return equipe
        
    def Indestructibilite(pretresse,allie):
        montant=2*pretresse.pv
        allie.pv_actuels+=montant
        print(allie.nom,'reçoit un bouclier pouvant bloquer jusqu à ',montant,'points de dégâts!! \n')
        return allie
        
    def Insensibilite(pretresse,equipe):
        for i in range(len(equipe)):
            equipe[i].marques_degats_continus=0
            equipe[i].intensite_degats_continus=0
            if(equipe[i].attaque_actuelle<equipe[i].attaque):
                equipe[i].attaque_actuelle=equipe[i].attaque
            if(equipe[i].defense_actuelle<equipe[i].defense):
                equipe[i].defense_actuelle=equipe[i].defense
            if(equipe[i].vitesse_actuelle<equipe[i].vitesse):
                equipe[i].vitesse_actuelle=equipe[i].vitesse
            if(equipe[i].invincibilite>0):
                equipe[i].invincibilite+=1
            if(equipe[i].immortalite>0):
                equipe[i].immortalite+=1
            if(equipe[i].impunite>0):
                equipe[i].impunite+=1
        return equipe
    
    def Immortalite(pretresse,equipe):
        for i in range(len(equipe)):
            equipe[i].regeneration+=30
            equipe[i].immortalite=3
        return equipe
        
    def Impunite(pretresse,equipe):
        for i in range(len(equipe)):
            equipe[i].vol_de_vie+=50
            equipe[i].impunite=3
        return equipe
    
    def Guerison_Celeste(pretresse,allie):
        if(pretresse.attribut=='Feu'):
            allie=Monstre.etreSoigne(allie,pretresse.attaque+math.floor(pretresse.pv/4))
            if (allie.attribut=='Feu'):
                allie.attaque_actuelle+=pretresse.attaque
                allie.taux_coup_critique+=10
                allie.tours_bonus_attaque=max(allie.tours_bonus_attaque,3)
        
        if(pretresse.attribut=='Eau'):
            allie=Monstre.etreSoigne(allie,pretresse.pv+(math.floor(pretresse.pv/4)))
            if (allie.attribut=='Eau'):
                allie.pv_actuels+=pretresse.pv

        if(pretresse.attribut=='Vent'):
            allie=Monstre.etreSoigne(allie,pretresse.vitesse+math.floor(pretresse.pv/4))
            if (allie.attribut=='Vent'):
                allie.vitesse_actuelle+=pretresse.vitesse
                allie.tour_supplementaire+=1
                allie.tours_bonus_vitesse=3

        if(pretresse.attribut=='Lumière'):
            allie=Monstre.etreSoigne(allie,pretresse.pv+pretresse.regeneration+math.floor(pretresse.pv/4))
            if (allie.attribut=='Lumière'):
                allie.regeneration+=30
                allie.immortalite=3
        
        if(pretresse.attribut=='Ténèbres'):
            allie=Monstre.etreSoigne(allie,pretresse.defense+math.floor(pretresse.pv/4))
            if (allie.attribut=='Ténèbres'):
                allie.defense_actuelle+=pretresse.defense
                allie.vol_de_vie+=50
                allie.impunite=3

        return allie

        
    def BenedictionFeu(pretresse,equipe):
        for i in range(len(equipe)):
            equipe[i].attaque_actuelle+=2*pretresse.attaque
            equipe[i].taux_coup_critique+=10
            equipe[i].tours_bonus_attaque=3
        return equipe
    
    def BenedictionEau(pretresse,equipe):
        for i in range(len(equipe)):
            equipe[i].pv_actuels+=2*pretresse.pv
        return equipe
        
    def BenedictionVent(pretresse,equipe):
        for i in range(len(equipe)):
            equipe[i].vitesse_actuelle+=2*pretresse.vitesse
            equipe[i].tour_supplementaire+=1
            equipe[i].tours_bonus_vitesse=3
        return equipe

    def BenedictionLumiere(pretresse,equipe):
        for i in range(len(equipe)):
            equipe[i].regeneration+=30
            equipe[i].immortalite=3
        return equipe
    
    def BenedictionTenebres(pretresse,equipe):
        for i in range(len(equipe)):
            equipe[i].defense_actuelle+=pretresse.defense
            equipe[i].tours_bonus_defense=3
            equipe[i].vol_de_vie+=50
            equipe[i].impunite=3
        return equipe
        




class Phenix(Monstre):
    def __init__(self):
        element=['Feu','Eau','Vent']
        indice_element=random.randint(0,2)
        attribut=element[indice_element]
        if (attribut=='Feu'):
            self.capacite1=Phenix.GeyserDeFeu
            self.capacite1Nom='Geyser de Feu'
            self.capacite2=Phenix.EtoileEcarlate
            self.capacite2Nom='Etoile Ecarlate'
            self.capacite3=Phenix.BrasierInfernal
            self.capacite3Nom='Brasier Infernal'
        if (attribut=='Eau'):
            self.capacite1=Phenix.GeyserDeGlace
            self.capacite1Nom='Geyser de Glace'
            self.capacite2=Phenix.EtoileDesNeiges
            self.capacite2Nom='Etoile des Neiges'
            self.capacite3=Phenix.BlizzardAbsolu
            self.capacite3Nom='Blizzard Absolu'
        if (attribut=='Vent'):
            self.capacite1=Phenix.GeyserDeVent
            self.capacite1Nom='Geyser de Vent'
            self.capacite2=Phenix.EtoileCeleste
            self.capacite2Nom='Etoile Céleste'
            self.capacite3=Phenix.TempeteDeDestruction
            self.capacite3Nom='Tempête de Destruction'
        self.nb_capacites=3
        self.Trecharge1=1
        self.Trecharge2=2
        self.Trecharge3=3
        self.attente1=0
        self.attente2=0
        self.attente3=0
        self.etatCap1='dispo'
        self.etatCap2='dispo'
        self.etatCap3='dispo'
        if (attribut=='Feu'):
            Monstre.__init__(self,'Phénix du Feu',element[indice_element],7,1,300,300,70,60,20)
        if (attribut=='Eau'):
            Monstre.__init__(self,'Phénix de Glace',element[indice_element],7,1,310,310,60,60,20)
        if (attribut=='Vent'):
            Monstre.__init__(self,'Phénix du Vent',element[indice_element],7,1,300,300,60,60,30)
        self.regeneration=20

    def GeyserDeFeu(Phenix,cible):
        if (cible.attribut=='Vent'):
            degats=3*Phenix.attaque_actuelle
            print('Dégâts augmentés par avantage élémentaire!!')
        else:
            degats=3*(Phenix.attaque_actuelle-cible.defense_actuelle)
        if (degats<=0):
            degats=3
        coup_critique=random.randint(1,100)
        if(coup_critique<=Phenix.taux_coup_critique):
            print('Coup critique!!')
            degats*=2
        print(Phenix.nom,' attaque ',cible.nom,'!!')
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.nom,' reçoit ',degats,' points de dégâts!! \n')
        else:
            print(cible.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if(cible.pv_actuels<=0):
            print(cible.nom,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv,' à ',cible.nom,'!! \n')
        Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
        return cible
    
    def GeyserDeGlace(Phenix,cible):
        if (cible.attribut=='Feu'):
            degats=3*Phenix.attaque_actuelle
            print('Dégâts augmentés par avantage élémentaire!!')
        else:
            degats=3*(Phenix.attaque_actuelle-cible.defense_actuelle)
        if (degats<=0):
            degats=3
        coup_critique=random.randint(1,100)
        if(coup_critique<=Phenix.taux_coup_critique):
            print('Coup critique!!')
            degats*=2
        print(Phenix.nom,' attaque ',cible.nom,'!!')
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.nom,' reçoit ',degats,' points de dégâts!! \n')
        else:
            print(cible.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if(cible.pv_actuels<=0):
            print(cible.nom,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv,' à ',cible.nom,'!! \n')
        Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
        return cible
    
    def GeyserDeVent(Phenix,cible):
        if (cible.attribut=='Eau'):
            degats=3*Phenix.attaque_actuelle
            print('Dégâts augmentés par avantage élémentaire!!')
        else:
            degats=3*(Phenix.attaque_actuelle-cible.defense_actuelle)
        if (degats<=0):
            degats=3
        coup_critique=random.randint(1,100)
        if(coup_critique<=Phenix.taux_coup_critique):
            print('Coup critique!!')
            degats*=2
        print(Phenix.nom,' attaque ',cible.nom,'!!')
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.nom,' reçoit ',degats,' points de dégâts!! \n')
        else:
            print(cible.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if(cible.pv_actuels<=0):
            print(cible.nom,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv,' à ',cible.nom,'!! \n')
        Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
        return cible
        
    def EtoileEcarlate(Phenix,cible):
        print(Phenix.nom,'engloutit',cible.nom,'dans une gigantesque sphère de flammes!!')
        if (cible.attribut=='Vent'):
            degats=3*Phenix.attaque_actuelle
            print('Dégâts augmentés par avantage élémentaire!!')
        else:
            degats=3*(Phenix.attaque_actuelle-cible.defense_actuelle)
        if (degats<=0):
            degats=3
        degats+=math.floor((cible.pv/5))
        coup_critique=random.randint(1,100)
        if(coup_critique<=Phenix.taux_coup_critique):
            print('Coup critique!!')
            degats*=2
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.nom,' reçoit ',degats,' points de dégâts!! \n')
        else:
            print(cible.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if(cible.pv_actuels<=0):
            print(cible.nom,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv,' à ',cible.nom,'!! \n')
        Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
        return cible
    
    def EtoileDesNeiges(Phenix,cible):
        print(Phenix.nom,'engloutit',cible.nom,'dans une gigantesque sphère de glace!!')
        if (cible.attribut=='Feu'):
            degats=3*Phenix.attaque_actuelle
            print('Dégâts augmentés par avantage élémentaire!!')
        else:
            degats=3*(Phenix.attaque_actuelle-cible.defense_actuelle)
        if (degats<=0):
            degats=3
        degats+=math.floor((cible.pv/5))
        coup_critique=random.randint(1,100)
        if(coup_critique<=Phenix.taux_coup_critique):
            print('Coup critique!!')
            degats*=2
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.nom,' reçoit ',degats,' points de dégâts!! \n')
        else:
            print(cible.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if(cible.pv_actuels<=0):
            print(cible.nom,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv,' à ',cible.nom,'!! \n')
        Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
        return cible
    
    def EtoileCeleste(Phenix,cible):
        print(Phenix.nom,'engloutit',cible.nom,'dans une gigantesque tornade!!')
        if (cible.attribut=='Eau'):
            degats=3*Phenix.attaque_actuelle
            print('Dégâts augmentés par avantage élémentaire!!')
        else:
            degats=3*(Phenix.attaque_actuelle-cible.defense_actuelle)
        if (degats<=0):
            degats=3
        degats+=math.floor((cible.pv/5))
        coup_critique=random.randint(1,100)
        if(coup_critique<=Phenix.taux_coup_critique):
            print('Coup critique!!')
            degats*=2
        if(cible.immortalite<=0):
            cible=(Monstre.recoitDegats(cible,degats))
            print(cible.nom,' reçoit ',degats,' points de dégâts!! \n')
        else:
            print(cible.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
        if(cible.pv_actuels<=0):
            print(cible.nom,' est mort!! \n')
        else:
            print('Il reste ',cible.pv_actuels,' point(s) de vie sur',cible.pv,' à ',cible.nom,'!! \n')
        Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
        return cible
        
    def BrasierInfernal(Phenix,equipe_ennemie):
        print(Phenix.nom,'engloutit toute l équipe ennemie dans un brasier infernal!!')
        i=0
        while(i<3):
            if(equipe_ennemie[i].pv_actuels>0):
                if (PrioriteElementaire(Phenix,equipe_ennemie[i])==True):
                    degats=Phenix.attaque_actuelle+math.floor((equipe_ennemie[i].pv)/4)
                    print('Dégâts augmentés par avantage élémentaire!!')
                else:
                    degats=Phenix.attaque_actuelle+math.floor((equipe_ennemie[i].pv)/4)-equipe_ennemie[i].defense_actuelle
                if (Phenix.attaque_actuelle<=equipe_ennemie[i].defense_actuelle):
                    degats=math.floor((equipe_ennemie[i].pv)/4)
                coup_critique=random.randint(1,100)
                if(coup_critique<=Phenix.taux_coup_critique):
                    print('Coup critique!!')
                    degats+=Phenix.attaque_actuelle
                if(equipe_ennemie[i].immortalite<=0):
                    equipe_ennemie[i]=(Monstre.recoitDegats(equipe_ennemie[i],degats))
                    print(equipe_ennemie[i].nom,' reçoit ',degats,' points de dégâts!! \n')
                else:
                    print(equipe_ennemie[i].nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                if(equipe_ennemie[i].pv_actuels<=0):
                    print(equipe_ennemie[i].nom,' est mort!! \n')
                else:
                    print('Il reste ',equipe_ennemie[i].pv_actuels,' point(s) de vie sur ', equipe_ennemie[i].pv,' à ',equipe_ennemie[i].nom,'!! \n')
                Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
            i+=1
        return equipe_ennemie
        
    def BrasierInfernal_cible_unique(Phenix,cible_unique):
        print(Phenix.nom,'engloutit',cible_unique.nom,'dans un brasier infernal!!')
        if(cible_unique.pv_actuels>0):
            if (PrioriteElementaire(Phenix,cible_unique)==True):
                degats=Phenix.attaque_actuelle+math.floor((cible_unique.pv)/4)
                print('Dégâts augmentés par avantage élémentaire!!')
            else:
                degats=Phenix.attaque_actuelle+math.floor((cible_unique.pv)/4)-cible_unique.defense_actuelle
            if (Phenix.attaque_actuelle<=cible_unique.defense_actuelle):
                degats=math.floor((cible_unique.pv)/4)
            coup_critique=random.randint(1,100)
            if(coup_critique<=Phenix.taux_coup_critique):
                print('Coup critique!!')
                degats+=Phenix.attaque_actuelle
            if(cible_unique.immortalite<=0):
                cible_unique=(Monstre.recoitDegats(cible_unique,degats))
                print(cible_unique.nom,' reçoit ',degats,' points de dégâts!! \n')
            else:
                print(cible_unique.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
            if(cible_unique.pv_actuels<=0):
                print(cible_unique.nom,' est mort!! \n')
            else:
                print('Il reste ',cible_unique.pv_actuels,' point(s) de vie sur ', cible_unique.pv,' à ',cible_unique.nom,'!! \n')
            Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
        return cible_unique
    
    def BlizzardAbsolu(Phenix,equipe_ennemie):
        print(Phenix.nom,'engloutit toute l équipe ennemie dans un blizzard absolu!!')
        i=0
        while(i<3):
            if(equipe_ennemie[i].pv_actuels>0):
                if (PrioriteElementaire(Phenix,equipe_ennemie[i])==True):
                    degats=Phenix.attaque_actuelle+math.floor((equipe_ennemie[i].pv)/4)
                    print('Dégâts augmentés par avantage élémentaire!!')
                else:
                    degats=Phenix.attaque_actuelle+math.floor((equipe_ennemie[i].pv)/4)-equipe_ennemie[i].defense_actuelle
                if (Phenix.attaque_actuelle<=equipe_ennemie[i].defense_actuelle):
                    degats=math.floor((equipe_ennemie[i].pv)/4)
                coup_critique=random.randint(1,100)
                if(coup_critique<=Phenix.taux_coup_critique):
                    print('Coup critique!!')
                    degats+=Phenix.attaque_actuelle
                if(equipe_ennemie[i].immortalite<=0):
                    equipe_ennemie[i]=(Monstre.recoitDegats(equipe_ennemie[i],degats))
                    print(equipe_ennemie[i].nom,' reçoit ',degats,' points de dégâts!! \n')
                else:
                    print(equipe_ennemie[i].nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                if(equipe_ennemie[i].pv_actuels<=0):
                    print(equipe_ennemie[i].nom,' est mort!! \n')
                else:
                    print('Il reste ',equipe_ennemie[i].pv_actuels,' point(s) de vie sur ', equipe_ennemie[i].pv,' à ',equipe_ennemie[i].nom,'!! \n')
                Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
            i+=1
        return equipe_ennemie
        
    def BlizzardAbsolu_cible_unique(Phenix,cible_unique):
        print(Phenix.nom,'engloutit',cible_unique.nom,'dans un blizzard absolu!!')
        if(cible_unique.pv_actuels>0):
            if (PrioriteElementaire(Phenix,cible_unique)==True):
                degats=Phenix.attaque_actuelle+math.floor((cible_unique.pv)/4)
                print('Dégâts augmentés par avantage élémentaire!!')
            else:
                degats=Phenix.attaque_actuelle+math.floor((cible_unique.pv)/4)-cible_unique.defense_actuelle
            if (Phenix.attaque_actuelle<=cible_unique.defense_actuelle):
                degats=math.floor((cible_unique.pv)/4)
            coup_critique=random.randint(1,100)
            if(coup_critique<=Phenix.taux_coup_critique):
                print('Coup critique!!')
                degats+=Phenix.attaque_actuelle
            if(cible_unique.immortalite<=0):
                cible_unique=(Monstre.recoitDegats(cible_unique,degats))
                print(cible_unique.nom,' reçoit ',degats,' points de dégâts!! \n')
            else:
                print(cible_unique.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
            if(cible_unique.pv_actuels<=0):
                print(cible_unique.nom,' est mort!! \n')
            else:
                print('Il reste ',cible_unique.pv_actuels,' point(s) de vie sur ', cible_unique.pv,' à ',cible_unique.nom,'!! \n')
            Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
        return cible_unique
    
    def TempeteDeDestruction(Phenix,equipe_ennemie):
        print(Phenix.nom,'engloutit toute l équipe ennemie dans une tempête destructrice!!')
        i=0
        while(i<3):
            if(equipe_ennemie[i].pv_actuels>0):
                if (PrioriteElementaire(Phenix,equipe_ennemie[i])==True):
                    degats=Phenix.attaque_actuelle+math.floor((equipe_ennemie[i].pv)/4)
                    print('Dégâts augmentés par avantage élémentaire!!')
                else:
                    degats=Phenix.attaque_actuelle+math.floor((equipe_ennemie[i].pv)/4)-equipe_ennemie[i].defense_actuelle
                if (Phenix.attaque_actuelle<=equipe_ennemie[i].defense_actuelle):
                    degats=math.floor((equipe_ennemie[i].pv)/4)
                coup_critique=random.randint(1,100)
                if(coup_critique<=Phenix.taux_coup_critique):
                    print('Coup critique!!')
                    degats+=Phenix.attaque_actuelle
                if(equipe_ennemie[i].immortalite<=0):
                    equipe_ennemie[i]=(Monstre.recoitDegats(equipe_ennemie[i],degats))
                    print(equipe_ennemie[i].nom,' reçoit ',degats,' points de dégâts!! \n')
                else:
                    print(equipe_ennemie[i].nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
                if(equipe_ennemie[i].pv_actuels<=0):
                    print(equipe_ennemie[i].nom,' est mort!! \n')
                else:
                    print('Il reste ',equipe_ennemie[i].pv_actuels,' point(s) de vie sur ', equipe_ennemie[i].pv,' à ',equipe_ennemie[i].nom,'!! \n')
                Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
            i+=1
        return equipe_ennemie
        
    def TempeteDeDestruction_cible_unique(Phenix,cible_unique):
        print(Phenix.nom,'engloutit',cible_unique.nom,'dans une tempête destructrice!!')
        if(cible_unique.pv_actuels>0):
            if (PrioriteElementaire(Phenix,cible_unique)==True):
                degats=Phenix.attaque_actuelle+math.floor((cible_unique.pv)/4)
                print('Dégâts augmentés par avantage élémentaire!!')
            else:
                degats=Phenix.attaque_actuelle+math.floor((cible_unique.pv)/4)-cible_unique.defense_actuelle
            if (Phenix.attaque_actuelle<=cible_unique.defense_actuelle):
                degats=math.floor((cible_unique.pv)/4)
            coup_critique=random.randint(1,100)
            if(coup_critique<=Phenix.taux_coup_critique):
                print('Coup critique!!')
                degats+=Phenix.attaque_actuelle
            if(cible_unique.immortalite<=0):
                cible_unique=(Monstre.recoitDegats(cible_unique,degats))
                print(cible_unique.nom,' reçoit ',degats,' points de dégâts!! \n')
            else:
                print(cible_unique.nom,'ne subit pas de dégâts grâce à son état d Immortalité!!')
            if(cible_unique.pv_actuels<=0):
                print(cible_unique.nom,' est mort!! \n')
            else:
                print('Il reste ',cible_unique.pv_actuels,' point(s) de vie sur ', cible_unique.pv,' à ',cible_unique.nom,'!! \n')
            Phenix=Monstre.etreSoigne(Phenix,math.floor(Phenix.vol_de_vie*degats/100))
        return cible_unique
'''




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



class Base:
    def __init__(self):
        self.stockage=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.place_dernier_monstre=0
        
    def estFullBase(base):
        if (base.place_dernier_monstre==99):
            fullBase=True
        else:
            fullBase=False
        return fullBase
    
    def ajouter_monstre(base,monstre):
        if (Base.estFullBase(base)==False):
            if(monstre.indice_stockage_base==OUT_OF_STOCKAGE):
                base.stockage[base.place_dernier_monstre+1]=monstre
                base.place_dernier_monstre+=1
                monstre.indice_stockage_base=base.place_dernier_monstre
            else:
                base.stockage[monstre.indice_stockage_base]=monstre
        else:
            print('Dommage!! La base est pleine... \n')
    
    def renommer_monstre(base,indice):
        print('Quel nom voulez-vous donner à votre ',(base.stockage[indice]).nom,(base.stockage[indice]).attribut,' ?')
        entree=input('Nom à donner : ')
        while(not IsSecureString(entree)):
            entree=input('Nom à donner : ')
        Surnom=str(entree)
        (base.stockage[indice]).surnom=Surnom
        print('\nParfait!!')
        print((base.stockage[indice]).nom,(base.stockage[indice]).attribut,' s\'appellera désormais : ',(base.stockage[indice]).surnom,'!!\n')
    
    def relacher_monstre(base,Team,indice):
        if (indice>0 and indice<=base.place_dernier_monstre):
            if((len(Team)==1) and (Team[0]==base.stockage[indice])):
                print('Vous ne pouvez pas relâcher ce montre. \n\n')
            else:
                print('Êtes vous sûr(e) de vouloir relâcher le monstre ',base.stockage[indice].nom,' ? \n')
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
                    print('Le monstre ',base.stockage[indice].nom,' a bien été relâché. \n')
                    j=0
                    while(j<len(Team)):
                        if(Team[j]==base.stockage[indice]):
                            Team=equipe.Supprimer_monstre_equipe(Team,j)
                        j+=1
                    Base.supprimer_monstre(base,indice)
        else:
            print('Vous n avez aucun monstre à cet emplacement de la base.')
        return Team
    
    def supprimer_monstre_mieux(base,Team,indice):
        if (indice>0 and indice<=base.place_dernier_monstre):
            j=0
            while(j<len(Team)):
                if(Team[j]==base.stockage[indice]):
                    Team=equipe.Supprimer_monstre_equipe(Team,j)
                    j-=1
                j+=1
            Base.supprimer_monstre(base,indice)
        else:
            print('Vous n avez aucun monstre à cet emplacement de la base.')
        return Team
    
    def supprimer_monstre(base,indice):
        if (indice>0 and indice<=base.place_dernier_monstre):
            base.stockage[indice]=0
            for i in range(indice,base.place_dernier_monstre):
                base.stockage[i]=base.stockage[i+1]
                (base.stockage[i]).indice_stockage_base-=1
            base.stockage[base.place_dernier_monstre]=0
            base.place_dernier_monstre-=1
                
    def afficher_monstres(base):
        i=1
        while(base.stockage[i]!=0):
            print('Monstre à l emplacement ',i,' : ')
            print(base.stockage[i],'\n')
            i+=1
            
    def afficher_partiellement_monstres(base):
        i=1
        while(base.stockage[i]!=0):
            print('Vous avez le monstre ',base.stockage[i].surnom,'(',base.stockage[i].nom,'de',base.stockage[i].attribut,base.stockage[i].classe,' étoiles) niveau ',base.stockage[i].niveau,'à l emplacement ',i)
            i+=1
    
    def reset_monstre(nom_creature):
        # Faire un or pour les noms séparés 
        if(nom_creature=='Slime'):
            creature=Slime()
        if(nom_creature=='GardienForet' or nom_creature=='Gardien de la Forêt'):
            creature=GardienForet()
        if(nom_creature=='Champignon'):
            creature=Champignon()
        if(nom_creature=='Spectre'):
            creature=Spectre()
        if(nom_creature=='Canniboite'):
            creature=Canniboite()
        if(nom_creature=='Crapoxique'):
            creature=Crapoxique()
        if(nom_creature=='Sacasable'):
            creature=Sacasable()
        if(nom_creature=='BasElementaire' or nom_creature=='Bas Elementaire'):
            creature=BasElementaire()
        if(nom_creature=='Sanglier'):
            creature=Sanglier()
        if(nom_creature=='PlanteCarnivore' or nom_creature=='Plante Carnivore'):
            creature=PlanteCarnivore()
        if(nom_creature=='BoiteDePandore' or nom_creature=='Boite de Pandore'):
            creature=BoiteDePandore()
        if(nom_creature=='SoldatSquelette' or nom_creature=='Soldat Squelette'):
            creature=SoldatSquelette()
        if(nom_creature=='ChauveSouris' or nom_creature=='Chauve Souris'):
            creature=ChauveSouris()
        if(nom_creature=='Scorpion'):
            creature=Scorpion()
        if(nom_creature=='Imp'):
            creature=Imp()
        if(nom_creature=='Lutin'):
            creature=Lutin()
        if(nom_creature=='Yeti'):
            creature=Yeti()
        if(nom_creature=='Cerbere'):
            creature=Cerbere()
        if(nom_creature=='OursDeGuerre' or nom_creature=='Ours de Guerre'):
            creature=OursDeGuerre()
        if(nom_creature=='Elementaire'):
            creature=Elementaire()
        if(nom_creature=='Garuda'):
            creature=Garuda()
        if(nom_creature=='Harpie'):
            creature=Harpie()
        if(nom_creature=='Salamandre'):
            creature=Salamandre()
        if(nom_creature=='Esprit'):
            creature=Esprit()
        if(nom_creature=='Viking'):
            creature=Viking()
        if(nom_creature=='Chevalier'):
            creature=Chevalier()
        if(nom_creature=='Fee'):
            creature=Fee()
        if(nom_creature=='DameHarpie' or nom_creature=='Dame Harpie'):
            creature=DameHarpie()
        if(nom_creature=='Inugami'):
            creature=Inugami()
        if(nom_creature=='Golem'):
            creature=Golem()
        if(nom_creature=='Mastodonte'):
            creature=Mastodonte()
        if(nom_creature=='Serpent'):
            creature=Serpent()
        if(nom_creature=='Griffon'):
            creature=Griffon()
        if(nom_creature=='Inferno'):
            creature=Inferno()
        if(nom_creature=='HautElementaire' or nom_creature=='Haut Elementaire'):
            creature=HautElementaire()
        if(nom_creature=='OursDeCombat' or nom_creature=='Ours de Combat'):
            creature=OursDeCombat()
        if(nom_creature=='LoupGarou' or nom_creature=='Loup Garou'):
            creature=LoupGarou()
        if(nom_creature=='Elfe'):
            creature=Elfe()
        if(nom_creature=='ChevalierMagique' or nom_creature=='Chevalier Magique'):
            creature=ChevalierMagique()
        if(nom_creature=='Vampire'):
            creature=Vampire()
        if(nom_creature=='Sylphe'):
            creature=Sylphe()
        if(nom_creature=='Sylphide'):
            creature=Sylphide()
        if(nom_creature=='Phénix'):
            creature=Phenix()
        return creature
        
        
    def invoquer_sans_affichage(base,Classe):
        if(Classe==1):
            nom_creature=Monstres_dispo_une_etoile_nom[random.randint(0,len(Monstres_dispo_une_etoile_nom)-1)]
        elif(Classe==2):
            nom_creature=Monstres_dispo_deux_etoiles_nom[random.randint(0,len(Monstres_dispo_deux_etoiles_nom)-1)]
        elif(Classe==3):
            nom_creature=Monstres_dispo_trois_etoiles_nom[random.randint(0,len(Monstres_dispo_trois_etoiles_nom)-1)]
        elif(Classe==4):
            nom_creature=Monstres_dispo_quatre_etoiles_nom[random.randint(0,len(Monstres_dispo_quatre_etoiles_nom)-1)]
        elif(Classe==5):
            nom_creature=Monstres_dispo_cinq_etoiles_nom[random.randint(0,len(Monstres_dispo_cinq_etoiles_nom)-1)]
        
        creature=Base.reset_monstre(nom_creature)        
        while(creature.classe!=Classe):
            creature=Base.invoquer_sans_affichage(base,Classe)
        return creature
            
    def invoquer(base,Classe):
        creature=Base.invoquer_sans_affichage(base,Classe)
        print('Félicitations!! Vous avez invoqué un(e) ',creature.nom,'!! \n')
        print(creature,'\n\n')
        str(input(' > '))
        return creature
        
    def invoquerDefini(base,nom_monstre,Attribut):
        monstre=Base.reset_monstre(nom_monstre)
        while(monstre.attribut!=Attribut):
            monstre=Base.reset_monstre(nom_monstre)
        Base.ajouter_monstre(base,monstre)
        print('Félicitations!! Vous avez invoqué un(e) ',monstre.nom,'!! \n')
        print(monstre,'\n\n')
        return monstre

     
    def possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales):
        menu=['Invoquer','Améliorer ou faire Evoluer un monstre','Partir à l aventure','Evaluer le mana et autres pierres transportées','Examiner ou modifier l équipe','Améliorer, examiner ou modifier l équipement','Accéder aux statistiques des créatures possédées','Ouvrir le sac','Accéder au magasin','En savoir plus sur les Relations Elementaires','En savoir plus sur les Runes','Sauvegarder et Quitter']
        # RAJOUTER OUVRIR L'INVENTAIRE + OPTIONS INVENTAIRE
        # REORGANISER L ORDRE
        print('Vous pouvez choisir parmi les options suivantes : ')
        options_possibilites=[]
        for a in range(len(menu)):
            print(a,' : ',menu[a])
            options_possibilites.append(a)
        entree=input('\n Que voulez-vous faire ? ')
        while(not IsSecure(entree)):
            entree=input('\n Que voulez-vous faire ? ')
        choix=int(entree)
        while(choix not in options_possibilites):
            entree=input('\n Que voulez-vous faire ? ')
            while(not IsSecure(entree)):
                entree=input('\n Que voulez-vous faire ? ')
            choix=int(entree)
            
        if (choix==0):
            nb_parchemins=sac.place_dernier_objet_courant
            if(nb_parchemins==0):
                print('\n Vous n avez plus de parchemins d invocation... \n')
            else:
                possibilites_invocation=[0]
                print('\n Quitter = 0 \n')
                b=1
                while(b<=sac.place_dernier_objet_courant):
                    Inventaire.Afficher_contenu_sac_zone_unique(sac,'objets_courants',b)
                    possibilites_invocation.append(b)
                    b+=1
                entree=input('Quel parchemin voulez-vous utiliser pour votre invocation ? ')
                while(not IsSecure(entree)):
                    entree=input('Quel parchemin voulez-vous utiliser pour votre invocation ? ')
                choix_parchemin=int(entree)
                while(choix_parchemin not in possibilites_invocation):
                    entree=input('Quel parchemin voulez-vous utiliser pour votre invocation ? ')
                    while(not IsSecure(entree)):
                        entree=input('Quel parchemin voulez-vous utiliser pour votre invocation ? ')
                    choix_parchemin=int(entree)
                if(choix_parchemin!=0):
                    parchemin_a_utiliser=sac.objets_courants[choix_parchemin]
                    if(sac.mana<parchemin_a_utiliser.prix_d_utilisation):
                        print('Vous n avez pas assez de pierres de mana pour réaliser l invocation avec ce parchemin.')
                    else:
                        sac.mana-=parchemin_a_utiliser.prix_d_utilisation
                        print('Invocation en cours...')
                        str(input(' > '))
                        creature=Objets.utiliser(parchemin_a_utiliser,base)
                        sac=Inventaire.supprimer_objet_courant_sans_affichage(sac,choix_parchemin)
                        Base.ajouter_monstre(base,creature)
            Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)
            
        if(choix==1):
            print('Pour Améliorer un monste, rentrez 0')
            print('Pour faire Evoluer un monstre, rentrez 1')
            print('Tout autre choix vous renverra au menu principal.')
            entree=input('\nQue voulez-vous faire ? ')
            while(not IsSecure(entree)):
                entree=input('\nQue voulez-vous faire ? ')
            choix_amelioration_ou_evolution=int(entree)
            if (choix_amelioration_ou_evolution==0):
                possibilites_amelioration=[]
                print('\nVoici les monstres que vous pouvez Améliorer : \n')
                i=1
                while(i<=base.place_dernier_monstre):
                    print('Vous avez le monstre ',base.stockage[i].surnom,'de',base.stockage[i].attribut,base.stockage[i].classe,' étoiles niveau ',base.stockage[i].niveau,'à l emplacement ',i)
                    possibilites_amelioration.append(i)                    
                    i+=1
                entree=input('Quel est l\'emplacement du monstre que vous souhaitez Améliorer ? ')
                while(not IsSecure(entree)):
                    entree=input('Quel est l\'emplacement du monstre que vous souhaitez Améliorer ? ')
                indice_monstre_a_ameliorer=int(entree)
                while(indice_monstre_a_ameliorer not in possibilites_amelioration):
                    entree=input('Quel est l\'emplacement du monstre que vous souhaitez Améliorer ? ')
                    while(not IsSecure(entree)):
                        entree=input('Quel est l\'emplacement du monstre que vous souhaitez Améliorer ? ')
                    indice_monstre_a_ameliorer=int(entree)
                monstre_a_ameliorer=base.stockage[indice_monstre_a_ameliorer]
                FirstTeam=Base.ameliorer_monstre(base,FirstTeam,monstre_a_ameliorer,indice_monstre_a_ameliorer) 
                Rafraichir_stockage(base)                
                FirstTeam=Rafraichir_equipe(base,FirstTeam)
            if (choix_amelioration_ou_evolution==1):
                print('\nVoici les monstres pouvant Evoluer : ')
                possibilites_evolution=[]
                e=1
                while(e<=base.place_dernier_monstre):
                    if(Donjon.Niveau_max_de_la_classe_atteint(base.stockage[e])==True and (base.stockage[e]).classe<6):
                        print('Le monstre ',base.stockage[e].surnom,'de',base.stockage[e].attribut,base.stockage[e].classe,' étoiles niveau ',base.stockage[e].niveau,'à l emplacement ',e)
                        possibilites_evolution.append(e)
                    e+=1
                if(len(possibilites_evolution)!=0):
                    entree=input('\nOui = 0 \nNon = 1 \nSouhaitez-vous faire Evoluer l\'un de ces monstre ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nOui = 0 \nNon = 1 \nSouhaitez-vous faire Evoluer l\'un de ces monstres ? ')
                    choix_evolution=int(entree)
                    while(choix_evolution!=0 and choix_evolution!=1):
                        entree=input('Oui = 0 \nNon = 1 \nSouhaitez-vous faire Evoluer l\'un de ces monstre ? ')
                        while(not IsSecure(entree)):
                            entree=input('Oui = 0 \nNon = 1 \nSouhaitez-vous faire Evoluer l\'un de ces monstres ? ')
                        choix_evolution=int(entree)
                    if(choix_evolution==0):
                        entree=input('Quel est l\'emplacement du monstre que vous souhaitez faire Evoluer ? ')
                        while(not IsSecure(entree)):
                            entree=input('Quel est l\'emplacement du monstre que vous souhaitez faire Evoluer ? ')
                        choix_monstre_a_evoluer=int(entree)
                        while(choix_monstre_a_evoluer not in possibilites_evolution):
                            entree=input('Quel est l\'emplacement du monstre que vous souhaitez faire Evoluer ? ')
                            while(not IsSecure(entree)):
                                entree=input('Quel est l\'emplacement du monstre que vous souhaitez faire Evoluer ? ')
                            choix_monstre_a_evoluer=int(entree)
                        print('\n')
                        FirstTeam=Base.Monter_en_classe(base,FirstTeam,base.stockage[choix_monstre_a_evoluer])
                        FirstTeam=Rafraichir_equipe(base,FirstTeam)
                else:
                    print('Aucun de vos monstres ne peut évoluer pour le moment. \n')
            Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)
            
        if (choix==2):
            possibilites_choix_map=[]
            possibilites_choix_niveau=[]
            print('\nVoici la liste des lieux accessibles : ')
            for c in range(len(noms_donjons_dispo)):
                print(noms_donjons_dispo[c],' = ',c)
                possibilites_choix_map.append(c)
            entree=input('Quel lieu voulez-vous explorer ? ')
            while(not IsSecure(entree)):
                entree=input('Quel lieu voulez-vous explorer ? ')
            choix_map=int(entree)
            while (choix_map not in possibilites_choix_map):
                entree=input('Quel lieu voulez-vous explorer ? ')
                while(not IsSecure(entree)):
                    entree=input('Quel lieu voulez-vous explorer ? ')
                choix_map=int(entree)
            Map=donjons_dispo[choix_map]
            nb_niveaux_accessibles=Niveaux_donjons_debloques[choix_map]
            print('\n\n Voici la liste des niveaux accessibles : ')
            for d in range(nb_niveaux_accessibles):
                print(Map[d][0],' = ',d)
                possibilites_choix_niveau.append(d)
            entree=input('Quel niveau voulez-vous explorer ? ')
            while(not IsSecure(entree)):
                entree=input('Quel niveau voulez-vous explorer ? ')
            choix_niveau=int(entree)
            while (choix_niveau not in possibilites_choix_niveau):
                entree=input('Quel niveau voulez-vous explorer ? ')
                while(not IsSecure(entree)):
                    entree=input('Quel niveau voulez-vous explorer ? ')
                choix_niveau=int(entree)
            donjon=Donjon(Map[choix_niveau])
            print('\n\n Vous entrez dans ',donjon.nom,'... \n\n\n')
            Donjon.CombatDonjon(base,sac,donjon,FirstTeam,choix_map,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)
       
        if (choix==3):
            Inventaire.AfficherArgent(sac)
            Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)        
        
        if(choix==4):
            FirstTeam=Rafraichir_equipe(base,FirstTeam)
            print('\nVous pouvez choisir parmi les options suivantes : ')
            print('Afficher un résumé de la composition actuelle de l équipe = 0')
            print('Afficher entièrement les statistiques de l équipe actuelle = 1')
            print('Remplacer un monstre de l équipe par un autre = 2')
            print('Ajouter un monstre à l\'équipe = 3')
            print('Modifier l alignement de l équipe actuelle = 4')
            print('Revenir au menu principal = 5')
            possibilites_choix4=[0,1,2,3,4,5]
            entree=input('\nQue voulez-vous choisir ? ')
            while(not IsSecure(entree)):
                entree=input('\nQue voulez-vous choisir ? ')
            choix_equipe=int(entree)
            while(choix_equipe not in possibilites_choix4):
                entree=input('\nQue voulez-vous choisir ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQue voulez-vous choisir ? ')
                choix_equipe=int(entree)
            if(choix_equipe==0):
                equipe.afficherPartiellement(FirstTeam)
            if(choix_equipe==1):
                equipe.afficher(FirstTeam)
            if(choix_equipe==2):
                FirstTeam=equipe.Modifier(base,FirstTeam)
            if(choix_equipe==3):
                FirstTeam=equipe.Ajouter(base,FirstTeam)
            if(choix_equipe==4):
                FirstTeam=equipe.Modifier_alignement_equipe(FirstTeam)
                equipe.afficherPartiellement(FirstTeam)
            print('\n')
            FirstTeam=Rafraichir_equipe(base,FirstTeam)
            Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)
            
        if(choix==5):
            print('\nVous pouvez choisir parmi les options suivantes : ')
            print('Afficher l intégralité de l équipement d un monstre = 0')
            print('Afficher une rune particulière de l équipement d un monstre = 1')
            print('Equiper une rune à un monstre = 2')
            print('Déséquiper une rune à un monstre = 3')
            print('Améliorer une rune = 4')
            print('Revenir au menu principal = 5')
            possibilites_choix5=[0,1,2,3,4,5]
            entree=input('\nQue voulez-vous choisir ? ')
            while(not IsSecure(entree)):
                entree=input('\nQue voulez-vous choisir ? ')
            choix_equipement=int(entree)
            while(choix_equipement not in possibilites_choix5):
                entree=input('\nQue voulez-vous choisir ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQue voulez-vous choisir ? ')
                choix_equipement=int(entree)
            if(choix_equipement==0):
                Base.afficher_partiellement_monstres(base)
                entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir l\'équipement détaillé ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir l\'équipement détaillé ? ')
                choix_monstre_equipement_a_montrer_integralement=int(entree)
                while(choix_monstre_equipement_a_montrer_integralement<1 and choix_monstre_equipement_a_montrer_integralement>base.place_dernier_monstre):
                    entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir l\'équipement détaillé ? ')
                    while(not IsSecure(entree)):
                        entree=input('Quel est l\'emplacement du monstre dont vous souhaitez voir l\'équipement détaillé ? ')
                    choix_monstre_equipement_a_montrer_integralement=int(entree)
                Runes.afficher_equipement_monstre_complet(base.stockage[choix_monstre_equipement_a_montrer_integralement])

            if(choix_equipement==1):
                Base.afficher_partiellement_monstres(base)
                entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir la rune ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQuel est l\'emplacement du montre dont vous souhaitez voir la rune ? ')
                choix_monstre_equipement_a_montrer=int(entree)
                while(choix_monstre_equipement_a_montrer<1 and choix_monstre_equipement_a_montrer>base.place_dernier_monstre):
                    entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir la rune ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez voir la rune ? ')
                    choix_monstre_equipement_a_montrer=int(entree)
                print('\n')
                print('Voir la rune du haut = 0')
                print('Voir la rune en haut à droite =1')
                print('Voir la rune en bas à droite = 2')
                print('Voir la rune du bas = 3')
                print('Voir la rune en bas à gauche = 4')
                print('Voir la rune en haut à gauche = 5')
                entree=input('\nQue voulez-vous choisir ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQue voulez-vous choisir ? ')
                choix_position_rune_a_montrer=int(entree)
                while(choix_position_rune_a_montrer not in [0,1,2,3,4,5]):
                    entree=input('\nQue voulez-vous choisir ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nQue voulez-vous choisir ? ')
                    choix_position_rune_a_montrer=int(entree)
                if(choix_position_rune_a_montrer==0):
                    Runes.afficher_equipement_monstre(base.stockage[choix_monstre_equipement_a_montrer],'rune_haut')
                if(choix_position_rune_a_montrer==1):
                    Runes.afficher_equipement_monstre(base.stockage[choix_monstre_equipement_a_montrer],'rune_haut_droite')
                if(choix_position_rune_a_montrer==2):
                    Runes.afficher_equipement_monstre(base.stockage[choix_monstre_equipement_a_montrer],'rune_bas_droite')
                if(choix_position_rune_a_montrer==3):
                    Runes.afficher_equipement_monstre(base.stockage[choix_monstre_equipement_a_montrer],'rune_bas')
                if(choix_position_rune_a_montrer==4):
                    Runes.afficher_equipement_monstre(base.stockage[choix_monstre_equipement_a_montrer],'rune_bas_gauche')
                if(choix_position_rune_a_montrer==5):
                    Runes.afficher_equipement_monstre(base.stockage[choix_monstre_equipement_a_montrer],'rune_haut_gauche')

            if(choix_equipement==2):
                Runes.Modifier_equipement(base,sac)
                
            if(choix_equipement==3):
                Runes.Desequiper(base,sac)
                
            if(choix_equipement==4):
                Base.afficher_partiellement_monstres(base)
                entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez Améliorer la rune ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQuel est l\'emplacement du montre dont vous souhaitez Améliorer la rune ? ')
                choix_monstre_equipement_a_ameliorer=int(entree)
                while(choix_monstre_equipement_a_ameliorer<1 and choix_monstre_equipement_a_ameliorer>base.place_dernier_monstre):
                    entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez Améliorer la rune ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nQuel est l\'emplacement du monstre dont vous souhaitez Améliorer la rune ? ')
                    choix_monstre_equipement_a_ameliorer=int(entree)
                print('\n')
                Runes.afficher_equipement_monstre_complet(base.stockage[choix_monstre_equipement_a_ameliorer])
                print('\n')
                print('Améliorer la rune du haut = 0')
                print('Améliorer la rune en haut à droite =1')
                print('Améliorer la rune en bas à droite = 2')
                print('Améliorer la rune du bas = 3')
                print('Améliorer la rune en bas à gauche = 4')
                print('Améliorer la rune en haut à gauche = 5')
                entree=input('\nQue voulez-vous choisir ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQue voulez-vous choisir ? ')
                choix_position_rune_a_ameliorer=int(entree)
                while(choix_position_rune_a_ameliorer not in [0,1,2,3,4,5]):
                    entree=input('\nQue voulez-vous choisir ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nQue voulez-vous choisir ? ')
                    choix_position_rune_a_ameliorer=int(entree)
                rune_a_ameliorer=Runes.Desequiper_sans_affichage(base.stockage[choix_monstre_equipement_a_ameliorer],choix_position_rune_a_ameliorer)
                if(rune_a_ameliorer==0):
                    print(base.stockage[choix_monstre_equipement_a_ameliorer].surnom,'n\'est équipé d\'aucune rune à cet emplacement!!\n')
                else:
                    rune_a_ameliorer=Runes.Ameliorer(rune_a_ameliorer)
                    base.stockage[choix_monstre_equipement_a_ameliorer]=Runes.MalusDeRunes(base.stockage[choix_monstre_equipement_a_ameliorer])
                    Runes.Equiper_sans_affichage(base.stockage[choix_monstre_equipement_a_ameliorer],rune_a_ameliorer,choix_position_rune_a_ameliorer)
                    base.stockage[choix_monstre_equipement_a_ameliorer]=Runes.BonusDeRunes(base.stockage[choix_monstre_equipement_a_ameliorer])

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
                    
                    base.stockage[choix_monstre_equipement_a_ameliorer].pv_actuels=base.stockage[choix_monstre_equipement_a_ameliorer].pv
                    base.stockage[choix_monstre_equipement_a_ameliorer].attaque_actuelle=base.stockage[choix_monstre_equipement_a_ameliorer].attaque
                    base.stockage[choix_monstre_equipement_a_ameliorer].defense_actuelle=base.stockage[choix_monstre_equipement_a_ameliorer].defense
                    base.stockage[choix_monstre_equipement_a_ameliorer].vitesse_actuelle=base.stockage[choix_monstre_equipement_a_ameliorer].vitesse
                    base.stockage[choix_monstre_equipement_a_ameliorer].taux_coup_critique_actuel=base.stockage[choix_monstre_equipement_a_ameliorer].taux_coup_critique
                    base.stockage[choix_monstre_equipement_a_ameliorer].dommages_critiques_actuels=base.stockage[choix_monstre_equipement_a_ameliorer].dommages_critiques
                    base.stockage[choix_monstre_equipement_a_ameliorer].resistance_actuelle=base.stockage[choix_monstre_equipement_a_ameliorer].resistance
                    base.stockage[choix_monstre_equipement_a_ameliorer].precision_actuelle=base.stockage[choix_monstre_equipement_a_ameliorer].precision

                    print('Le monstre équipé devient : \n',base.stockage[choix_monstre_equipement_a_ameliorer],'\n')

                FirstTeam=Rafraichir_equipe(base,FirstTeam)
            print('\n')

            Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)
            
        if(choix==6):
            print('\nVoici l ensemble des monstres que vous avez en votre possession : \n')
            Base.afficher_partiellement_monstres(base)
            print('\n')
            entree=input('Oui = 0 \nNon = 1 \nVoulez-vous voir les caractéristiques de l\'un de ces monstres de manière plus détaillée ? ')
            while(not IsSecure(entree)):
                entree=input('Oui = 0 \nNon = 1 \nVoulez-vous voir les caractéristiques de l\'un de ces monstres de manière plus détaillée ? ')
            choix_zoom_caracteristiques=int(entree)
            while(choix_zoom_caracteristiques!=0 and choix_zoom_caracteristiques!=1):
                entree=input('Oui = 0 \nNon = 1 \nVoulez-vous voir les caractéristiques de l\'un de ces monstres de manière plus détaillée ? ')
                while(not IsSecure(entree)):
                    entree=input('Oui = 0 \nNon =1 \nVoulez-vous voir les caractéristiques de l\'un de ces monstres de manière plus détaillée ? ')
                choix_zoom_caracteristiques=int(entree)
            if(choix_zoom_caracteristiques==0):
                entree=input('Quel est l\'emplacement du monstre dont vous souhaitez-voir les caractéristiques ? ')
                while(not IsSecure(entree)):
                    entree=input('Quel est l\'emplacement du monstre dont vous souhaitez-voir les caractéristiques ? ')
                choix_monstre_a_zoomer=int(entree)
                while(choix_monstre_a_zoomer<1 and choix_monstre_a_zoomer>base.place_dernier_monstre):
                    entree=input('Quel est l\'emplacement du monstre dont vous souhaitez-voir les caractéristiques ? ')
                    while(not IsSecure(entree)):
                        entree=input('Quel est l\'emplacement du monstre dont vous souhaitez-voir les caractéristiques ? ')
                    choix_monstre_a_zoomer=int(entree)
                print(base.stockage[choix_monstre_a_zoomer])
            else:
                entree=input('Oui = 0 \nNon = 1 \nVoulez-vous relâcher un des monstres que vous possédez ? ')
                while(not IsSecure(entree)):
                    entree=input('Oui = 0 \nNon = 1 \nVoulez-vous relâcher un des monstres que vous possédez ? ')
                choix_relachement=int(entree)
                while(choix_relachement!=0 and choix_relachement!=1):
                    entree=input('Oui = 0 \nNon = 1 \nVoulez-vous relâcher un des monstres que vous possédez ? ')
                    while(not IsSecure(entree)):
                        entree=input('Oui = 0 \nNon =1 \nVoulez-vous relâcher un des monstres que vous possédez ? ')
                    choix_relachement=int(entree)
                if(choix_relachement==0):
                    entree=input('Quel est l\'emplacement du monstre que vous souhaitez relâcher ? ')
                    while(not IsSecure(entree)):
                        entree=input('Quel est l\'emplacement du monstre que vous souhaitez relâcher ? ')
                    choix_monstre_a_relacher=int(entree)
                    while(choix_monstre_a_relacher<1 and choix_monstre_a_relacher>base.place_dernier_monstre):
                        entree=input('Quel est l\'emplacement du monstre que vous souhaitez relâcher ? ')
                        while(not IsSecure(entree)):
                            entree=input('Quel est l\'emplacement du monstre que vous souhaitez relâcher ? ')
                        choix_monstre_a_relacher=int(entree)
                    FirstTeam=Base.relacher_monstre(base,FirstTeam,choix_monstre_a_relacher)
                else:
                    entree=input('Oui = 0 \nNon = 1 \nVoulez-vous renommer un des monstres que vous possédez ? ')
                    while(not IsSecure(entree)):
                        entree=input('Oui = 0 \nNon = 1 \nVoulez-vous renommer un des monstres que vous possédez ? ')
                    choix_renommement=int(entree)
                    while(choix_renommement!=0 and choix_renommement!=1):
                        entree=input('Oui = 0 \nNon = 1 \nVoulez-vous renommer un des monstres que vous possédez ? ')
                        while(not IsSecure(entree)):
                            entree=input('Oui = 0 \nNon =1 \nVoulez-vous renommer un des monstres que vous possédez ? ')
                        choix_renommement=int(entree)
                    if(choix_renommement==0):
                        entree=input('Quel est l\'emplacement du monstre que vous souhaitez renommer ? ')
                        while(not IsSecure(entree)):
                            entree=input('Quel est l\'emplacement du monstre que vous souhaitez renommer ? ')
                        choix_monstre_a_renommer=int(entree)
                        while(choix_monstre_a_renommer<1 and choix_monstre_a_renommer>base.place_dernier_monstre):
                            entree=input('Quel est l\'emplacement du monstre que vous souhaitez renommer ? ')
                            while(not IsSecure(entree)):
                                entree=input('Quel est l\'emplacement du monstre que vous souhaitez renommer ? ')
                            choix_monstre_a_renommer=int(entree)
                        Base.renommer_monstre(base,choix_monstre_a_renommer)
            print('\n')
            Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)
            
        if(choix==7):
            print('\nVous pouvez choisir parmi les options suivantes : ')
            print('Regarder la place disponible pour les runes et les parchemins = 0')
            print('Afficher tous les parchemins en votre possession = 1')
            print('Afficher toutes les runes en votre possession = 2')
            print('Jeter un parchemin ou une rune = 3')
            print('Pour utiliser un parchemin, allez dans le menu Invoquer depuis le menu principal')
            print('Revenir au menu principal = 4')
            possibilites_choix7=[0,1,2,3,4]
            entree=input('\nQue voulez-vous faire ? ')
            while(not IsSecure(entree)):
                entree=input('\nQue voulez-vous faire ? ')
            choix_menu=int(entree)
            while(choix_menu not in possibilites_choix7):
                entree=input('\nQue voulez-vous faire ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQue voulez-vous faire ? ')
                choix_menu=int(entree)
            if(choix_menu==0):
                print('Il vous reste ',99-sac.place_dernier_objet_courant,'emplacements pour les parchemins.')
                print('Il vous reste ',99-sac.place_dernier_equipement,'emplacements pour les runes. \n')
            if(choix_menu==1):
                Inventaire.Afficher_contenu_sac_section(sac,'objets_courants')
                print('\n')
            if(choix_menu==2):
                Inventaire.Afficher_contenu_sac_section(sac,'equipement')
                print('\n')
            if(choix_menu==3):
                print('Ne rien jeter = 0 \nJeter un parchemin = 1 \nJeter une rune = 2\n')
                entree=input('\nQue voulez-vous faire ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQue voulez-vous faire ? ')
                choix_suppression_a_faire=int(entree)
                while(choix_suppression_a_faire!=0 and choix_suppression_a_faire!=1 and choix_suppression_a_faire!=2):
                    entree=input('\nQue voulez-vous faire ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nQue voulez-vous faire ? ')
                    choix_suppression_a_faire=int(entree)
                if(choix_suppression_a_faire==1):
                    Inventaire.supprimer_objet(sac,'objets_courants')
                if(choix_suppression_a_faire==2):
                    Inventaire.supprimer_objet(sac,'equipement')
            Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)
            
        if(choix==8):
            Inventaire.magasin(base,sac)
            Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)
        
        if(choix==9):
            print('\nLe Feu est supérieur au Vent.')
            print('Le Vent est supérieur à l\'Eau.')
            print('L\'Eau est supérieure au Feu.')
            print('La Lumière est supérieure aux Ténèbres.')
            print('Les Ténèbres sont supérieures à la Lumière.')
            print('Lorsqu\'un monstre d\'un certain attribut attaque un monstre d\'un attribut inférieur au sien, les dommages infligés sont démultipliés!!')
            print('A l\'inverse, attaquer un monstre d\'un attribut supérieur peut réduire les dommages infligés.')
            print('Exploitez les Relations Elémentaires à votre avantage!! \n\n')
            Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)
            
        if(choix==10):
            ''' EXPLICATIONS A REFAIRE '''
            print('\nLes runes sont les équipements pour les créatures de ce monde.')
            print('Il existe différentes Catégories de runes : Energie, Colere, Tenace, Veloce,... Et bien d\'autres encore!!\n')
            print('Chaque rune renforce une caractéristique particulière dépendant de la Catégorie dans laquelle elle se trouve. Par exemple, les runes de la Catégorie Energie augmentent le maximum de PV de votre créature!!\n')
            print('Chaque rune a une position spécifique dans l\'équipement de la créature. Elle peut se situer en haut, en haut à droite, en bas à droite, en bas, en bas à gauche ou en haut à gauche.')
            print('A chaque position de son équipement, une créature ne peut s\'équiper que d\'une rune. Chaque monstre ne peut donc être équipé au maximum que de six runes.\n')
            print('Pour chaque couple de runes de la même Catégorie, la créature peut éventuellement bénéficier d\'un bonus de runes exclusif!!')
            print('Par exemple, équiper deux runes de la Catégorie Energie de positions différentes à une même créature lui octroie un bonus exclusif en points de vie égal à 15% de ses PV max... Et ces bonus peuvent être cumulés!!')
            print('Parfois, il faut plus qu\'un simple couple de runes pour bénéficier du bonus de runes... Mais un sextuplet de runes octroie toujours un bonus incroyable!! A vous de découvrir lequel!! \n\n') 
            Base.possibilites(base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo,recompenses_globales_totales)

            ''' Rajouter En savoir plus sur ce monde '''
            
        if(choix==11):
            ecrire_sauvegarde("SAVE",base,sac,FirstTeam,Niveaux_donjons_debloques,donjons_dispo,noms_donjons_dispo)
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('La sauvegarde a bien été effectuée. \n\n')
            sys.exit()

    def ameliorer_monstre(base,equipe,monstre_a_ameliorer,indice_monstre_a_ameliorer):
        print('\n\nPour faire une Amélioration, vous devez choisir un monstre à sacrifier qui sera converti en expérience.')
        print('Affichage des monstres pouvant être sacrifiés : \n')
        print('Impossible d\'utiliser le monstre à l\'indice : ',indice_monstre_a_ameliorer,'\n')
        print('Annuler = 0\n')
        possibilites_monstres_a_sacrifier=[0]
        for j in range(1,base.place_dernier_monstre+1):
            if(j!=indice_monstre_a_ameliorer):
                print(base.stockage[j],' = ',j,'\n')
                possibilites_monstres_a_sacrifier.append(j)
        entree=input('Quel monstre voulez-vous sacrifier ? ')
        while(not IsSecure(entree)):
            entree=input('\nQuel monstre voulez-vous sacrifier ? ')
        choix_monstre_a_sacrifier=int(entree)
        while(choix_monstre_a_sacrifier not in possibilites_monstres_a_sacrifier):            
            entree=input('\nQuel monstre voulez-vous sacrifier ? ')
            while(not IsSecure(entree)):
                entree=input('\nQuel monstre voulez-vous sacrifier ? ')
            choix_monstre_a_sacrifier=int(entree)
            
        monstre_a_sacrifier=base.stockage[choix_monstre_a_sacrifier]
        if((len(equipe)==1) and (equipe[0]==monstre_a_sacrifier)):
            print('Vous ne pouvez pas sacrifier ce monstre. \n\n')
        else:
            if(choix_monstre_a_sacrifier!=0):
                print('\n')
                XP_a_gagner=Donjon.CalculerXP_amelioration(monstre_a_sacrifier)
                monstre_a_ameliorer=Donjon.RecevoirXP(monstre_a_ameliorer,XP_a_gagner)
                equipe=Base.supprimer_monstre_mieux(base,equipe,choix_monstre_a_sacrifier)
                equipe=Rafraichir_equipe(base,equipe)
                # La fonction supprimer_monstre_mieux enlève le monstre sacrifié de l'équipe
        return equipe

    def Monter_en_classe(base,equipe,monstre_a_evoluer):
        print('\n\nPour faire une telle Evolution, vous devez sacrifiez ',monstre_a_evoluer.classe,'monstres de ',monstre_a_evoluer.classe,'étoiles.')
        print('Affichage des monstres pouvant être sacrifiés : \n')
        possibilites_monstres_a_sacrifier=[]
        choix_monstres_materiels=[]
        for j in range(1,1+base.place_dernier_monstre):
            if((base.stockage[j].classe==monstre_a_evoluer.classe) and (base.stockage[j]!=monstre_a_evoluer)):
                print(base.stockage[j],' = ',j,'\n')
            possibilites_monstres_a_sacrifier.append(j)
        if(len(possibilites_monstres_a_sacrifier)<monstre_a_evoluer.classe):
            print('Pas assez de monstres matériels pour réaliser l Evolution \n(',len(possibilites_monstres_a_sacrifier),'disponibles, ',monstre_a_evoluer.classe,'requis)\n')
        else:
            for k in range(monstre_a_evoluer.classe):
                entree=input('\nQuel monstre voulez-vous sacrifier ? ')
                while(not IsSecure(entree)):
                    entree=input('\nQuel monstre voulez-vous sacrifier ? ')
                choix_monstre_a_sacrifier=int(entree)
                while(choix_monstre_a_sacrifier not in possibilites_monstres_a_sacrifier):            
                    entree=input('\nQuel monstre voulez-vous sacrifier ? ')
                    while(not IsSecure(entree)):
                        entree=input('\nQuel monstre voulez-vous sacrifier ? ')
                    choix_monstre_a_sacrifier=int(entree)
                if(choix_monstre_a_sacrifier!=0):
                    choix_monstres_materiels.append(choix_monstre_a_sacrifier)
            choix_monstres_materiels=tri_ordre_decroissant(choix_monstres_materiels)
            if(choix_monstres_materiels==tri_sans_doublons(choix_monstres_materiels)):
                for l in range(len(choix_monstres_materiels)):
                    equipe=Base.supprimer_monstre_mieux(base,equipe,choix_monstres_materiels[l])
                Doit_modifier_equipe=False
                for m in range(len(equipe)):
                    if(equipe[m]==monstre_a_evoluer):
                        indice_a_remplacer=m
                        Doit_modifier_equipe=True
                Monstre.Evoluer(monstre_a_evoluer)
                if(Doit_modifier_equipe):
                    equipe[indice_a_remplacer]=monstre_a_evoluer    
                    equipe=Rafraichir_equipe(base,equipe)
                print(monstre_a_evoluer.surnom,'évolue!!')
                print(monstre_a_evoluer)
            else:
                print('Pas assez de monstres matériels pour réaliser l Evolution \n(',len(tri_sans_doublons(choix_monstres_materiels)),'donnés, ',monstre_a_evoluer.classe,'requis)\n')
        return equipe
            
            
    def debut(base):
        print('\n\n')
        print('Bienvenu, cher invocateur!! Vous avez été appelé en ce monde pour le sauver d un grave danger qui le menace...')
        print('Pour vous défendre et nous protéger, vous seul pouvez faire appel à vos fidèles créatures pour repousser les monstres ennemis!!')
        print('Mais on dirait que vous n en n\'avez pas encore... Allons en invoquer!! \n\n')
        str(input(' > '))
        monstre1=Base.invoquerDefini(base,'Cerbere','Feu')
        str(input(' > '))
        monstre2=Base.invoquerDefini(base,'Fee','Eau')
        str(input(' > '))
        monstre3=Base.invoquerDefini(base,'Chevalier','Vent')
        str(input(' > '))
        # TEAM DE L ADMIN = A NE PAS MODIFIER!!!!!!!!!!

        #monstreX=Base.invoquerDefini(base,'ChevalierDragon','Eau')
        #monstreY=Base.invoquerDefini(base,ChevalierDragon','Feu')
        #monstre1=Base.invoquerDefini(base,'Phenix','Feu')
        #monstre2=Base.invoquerDefini(base,'Phenix','Vent')
        #monstre3=Base.invoquerDefini(base,'Phenix','Eau')

        print('\n Bien!! Maintenant, il est temps de vous constituer une équipe!!')
        Equipe1=equipe.__init__(monstre1,monstre2,monstre3)
        Equipe1=Rafraichir_equipe(base,Equipe1)
        equipe.afficherPartiellement(Equipe1)
        print('\n Parfait!! Je vous laisse désormais remplir votre rôle de héros!! \n\n')
        str(input(' > '))
        return Equipe1

    


def tri_sans_doublons(liste):
    liste_sans_doublons=[]
    for i in range(len(liste)):
        for j in range(len(liste)):
            if ((liste[i]!=liste[j]) and (not liste[j] in liste_sans_doublons)):
                liste_sans_doublons+=[liste[j]]
    liste_sans_doublons=tri_ordre_decroissant(liste_sans_doublons)
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
    
def PrioriteElementaire(attaquant,cible):
    Avantage=False    
    if(attaquant.attribut=='Feu' and cible.attribut=='Vent'):
        Avantage=True
    if(attaquant.attribut=='Vent' and cible.attribut=='Eau'):
        Avantage=True
    if(attaquant.attribut=='Eau' and cible.attribut=='Feu'):
        Avantage=True
    if(attaquant.attribut=='Lumière' and cible.attribut=='Ténèbres'):
        Avantage=True
    if(attaquant.attribut=='Ténèbres' and cible.attribut=='Lumière'):
        Avantage=True
    return Avantage
    
def Choisir_capacite_speciale(creature):
    print('\n Vous pouvez utiliser l une des capacités suivantes : ')
    possibilites_capacite_speciale=[]
    if (creature.etatCap1=='dispo'):
        print(creature.capacite1Nom,' = 1')
        possibilites_capacite_speciale.append(1)
    if(creature.silencieux<=0):
        if(creature.nb_capacites>=2):
            if (creature.etatCap2=='dispo'):
                print(creature.capacite2Nom,' = 2')
                possibilites_capacite_speciale.append(2)
        if(creature.nb_capacites>=3):
            if (creature.etatCap3=='dispo'):
                print(creature.capacite3Nom,' = 3')
                possibilites_capacite_speciale.append(3)
        if(creature.nb_capacites>=4):
            if (creature.etatCap4=='dispo'):
                print(creature.capacite4Nom,' = 4')
                possibilites_capacite_speciale.append(4)
    entree=input('Quelle capacité voulez-vous utiliser ? ')
    while(not IsSecure(entree)):
        entree=input('\nQuelle capacité voulez-vous utiliser ? ')
    choix=int(entree)
    while(choix not in possibilites_capacite_speciale):
        entree=input('\nQuelle capacité voulez-vous utiliser ? ')
        while(not IsSecure(entree)):
            entree=input('\nQuelle capacité voulez-vous utiliser ? ')
        choix=int(entree)
    if (choix==1):
        capacite_choisie=creature.capacite1
        creature.attente1=creature.Trecharge1
        creature.etatCap1='Non dispo'
    elif (choix==2):
        capacite_choisie=creature.capacite2
        creature.attente2=creature.Trecharge2
        creature.etatCap2='Non dispo'
    elif (choix==3):
        capacite_choisie=creature.capacite3
        creature.attente3=creature.Trecharge3
        creature.etatCap3='Non dispo'
    elif (choix==4):
        capacite_choisie=creature.capacite4
        creature.attente4=creature.Trecharge4
        creature.etatCap4='Non dispo'
    return capacite_choisie
    
def Choisir_capacite_speciale_sans_affichage(creature):
    possibilites_capacite_speciale=[]
    if (creature.etatCap1=='dispo'):
        possibilites_capacite_speciale.append(1)
    if(creature.silencieux<=0):
        if(creature.nb_capacites>=2):
            if (creature.etatCap2=='dispo'):
                possibilites_capacite_speciale.append(2)
        if(creature.nb_capacites>=3):
            if (creature.etatCap3=='dispo'):
                possibilites_capacite_speciale.append(3)
        if(creature.nb_capacites>=4):
            if(creature.etatCap4=='dispo'):
                possibilites_capacite_speciale.append(4)
    indice_aleatoire=random.randint(0,len(possibilites_capacite_speciale)-1)
    while(possibilites_capacite_speciale[indice_aleatoire] not in possibilites_capacite_speciale):
        indice_aleatoire=random.randint(0,len(possibilites_capacite_speciale)-1)
    choix=possibilites_capacite_speciale[indice_aleatoire]
    if (choix==1):
        capacite_choisie=creature.capacite1
        creature.attente1=creature.Trecharge1
        creature.etatCap1='Non dispo'
    elif (choix==2):
        capacite_choisie=creature.capacite2
        creature.attente2=creature.Trecharge2
        creature.etatCap2='Non dispo'
    elif (choix==3):
        capacite_choisie=creature.capacite3
        creature.attente3=creature.Trecharge3
        creature.etatCap3='Non dispo'
    elif (choix==4):
        capacite_choisie=creature.capacite4
        creature.attente4=creature.Trecharge4
        creature.etatCap4='Non dispo'
    return capacite_choisie


def FinDeTour(attaquant):
    attaquant.attente1-=1
    if (attaquant.attente1<=0):
        attaquant.etatCap1='dispo'
        attaquant.attente1=0
        
    if(attaquant.nb_capacites>=2):
        attaquant.attente2-=1
        if (attaquant.attente2<=0):
            attaquant.etatCap2='dispo'
            attaquant.attente2=0

    if(attaquant.nb_capacites>=3):
        attaquant.attente3-=1
        if (attaquant.attente3<=0):
            attaquant.etatCap3='dispo'
            attaquant.attente3=0

    if(attaquant.nb_capacites>=4):
        attaquant.attente4-=1
        if (attaquant.attente4<=0):
            attaquant.etatCap4='dispo'
            attaquant.attente4=0
    
    attaquant.jauge_attaque-=100
    return attaquant



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

 


'''
def Recompenses_ForetVeur(niveau_donjon):
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
        __init__(self,NOM,CATEGORIE,POSITION,QUALITE,RARETE,BONUS)
        categories_possibles=['HP+','HP%','ATK+','ATK%','DEF+','DEF%','VIT+','TCC%','DC%','ACC%','RES%']
        categorie_aleatoire=categories_possibles[(random.randint(0,10))]
        positions_possibles=['rune_haut','rune_haut_droite','rune_bas_droite','rune_bas','rune_bas_gauche','rune_haut_gauche']
        if(niveau_donjon!=7):
            position=positions_possibles[niveau_donjon-1]
        else:
            position=positions_possibles[random.randint(0,5)]
        recompense=Runes('Rune Energie I','Energie',position,'I','Normale',categorie_aleatoire)
    return [recompense_texte,recompense]
'''

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







''' Runes.__init__(self,NOM,CATEGORIE,POSITION,QUALITE,RARETE,BONUS) '''
''' Suffisant pour recréer la même rune ? '''
''' NON. Préférer : '''
''' Runes.Reinitialiser(nom,categorie,position,qualite,rarete,bonus,niveau,bonus_secondaires,liste_des_gains) '''

def ecrire_sauvegarde(nom_fichier, base, sac, FirstTeam, Niveaux_donjons_debloques, donjons_dispo, noms_donjons_dispo):
    try:
        save_file = open(nom_fichier + ".txt", "w")
    except IOError:
        print("Erreur d'écriture")
    save_file.write(str(lire_stockage_base(base.stockage)) + "\n")
    save_file.write(str(sac.mana) + "\n")
    save_file.write(str(sac.cristaux) + "\n")
    save_file.write(str(sac.pierres_de_fusion) + "\n")
    for i in range(1,len(sac.equipement)):
        print('sac.equipement',i,' = ',sac.equipement[i],'\n')
        if(sac.equipement[i]!=0):
            save_file.write(str([(sac.equipement[i]).nom,(sac.equipement[i]).categorie,(sac.equipement[i]).position,(sac.equipement[i]).qualite,(sac.equipement[i]).rarete,(sac.equipement[i]).famille_de_bonus,(sac.equipement[i]).niveau,(sac.equipement[i]).bonus_secondaires,[(sac.equipement[i]).gain_en_pv,(sac.equipement[i]).gain_en_pourcentage_de_pv,(sac.equipement[i]).gain_en_attaque,(sac.equipement[i]).gain_en_pourcentage_de_attaque,(sac.equipement[i]).gain_en_defense,(sac.equipement[i]).gain_en_pourcentage_de_defense,(sac.equipement[i]).gain_en_vitesse,(sac.equipement[i]).gain_en_taux_de_coup_critique,(sac.equipement[i]).gain_en_dommages_critiques,(sac.equipement[i]).gain_en_resistance,(sac.equipement[i]).gain_en_precision]]) + "\n")
        else:
            save_file.write(str(0) + '\n')
    for j in range(1,len(sac.objets_courants)):
        if(sac.objets_courants[j]!=0):
            print('sac.objets_courants',j,' = ',sac.objets_courants[j].nom,'\n')
            save_file.write("'" + str(sac.objets_courants[j].nom) + "'" + "\n")
        else:
            print('sac.objets_courants',j,' = ',sac.objets_courants[j],'\n')
            save_file.write(str(0) + '\n')
    '''
    save_file.write(str(FirstTeam[0]))
    if(len(FirstTeam)>0):
        save_file.write(str(FirstTeam[1]))
    if(len(FirstTeam)>1):
        save_file.write(str(FirstTeam[2]))
    '''
    save_file.write(str(lire_stockage_base(FirstTeam)) + "\n")
    save_file.write(str(Niveaux_donjons_debloques) + "\n")
    save_file.write(str(noms_donjons_dispo) + "\n")
    save_file.write(str(recompenses_globales_totales[0]) + "\n")
    
    ''' A MODIFIER LORS DE MODIFICATION DES RECOMPENSES GLOBALES!!!!!! '''
    recompenses_globales_totales[1][0].indice_stockage=OUT_OF_STOCKAGE
    save_file.write(str(lire_stockage_base([recompenses_globales_totales[1][0]])) + "\n")
    for k in range(len(recompenses_globales_totales[1][1])):
        recompenses_globales_totales[1][1][k].indice_stockage=OUT_OF_STOCKAGE
        save_file.write(str(lire_stockage_base([recompenses_globales_totales[1][1][k]])) + "\n")
    recompenses_globales_totales[1][2].indice_stockage=OUT_OF_STOCKAGE
    save_file.write(str(lire_stockage_base([recompenses_globales_totales[1][2]])) + "\n")
    save_file.write(str(recompenses_globales_totales[2]) + "\n")

    '''
    Les objets courants sont uniquement caractérisés par leur nom
    '''
    save_file.close()

def lire_sauvegarde(nom_fichier):
    try:
        save_file = open(nom_fichier, "r")
    except IOError:
        print("Erreur : fichier inexistant")
        return []
    data_list = save_file.readlines()
    return data_list
     
 
def lire_stockage_base(data_list):
    return_list=[]
    for objects in data_list:
        object_stats=[]
        print(objects,'\n')
        if(objects==0):
            return_list.append(0)
        else:
            object_stats.append(objects.nom)
            object_stats.append(objects.attribut)
            object_stats.append(objects.classe)
            object_stats.append(objects.niveau)
            object_stats.append(objects.XP_avant_prochain_niveau)
            if(objects.equipement_rune_haut!=0):
                object_stats.append([(objects.equipement_rune_haut).nom,(objects.equipement_rune_haut).categorie,(objects.equipement_rune_haut).position,(objects.equipement_rune_haut).qualite,(objects.equipement_rune_haut).rarete,(objects.equipement_rune_haut).famille_de_bonus,(objects.equipement_rune_haut).niveau,(objects.equipement_rune_haut).bonus_secondaires,[(objects.equipement_rune_haut).gain_en_pv,(objects.equipement_rune_haut).gain_en_pourcentage_de_pv,(objects.equipement_rune_haut).gain_en_attaque,(objects.equipement_rune_haut).gain_en_pourcentage_de_attaque,(objects.equipement_rune_haut).gain_en_defense,(objects.equipement_rune_haut).gain_en_pourcentage_de_defense,(objects.equipement_rune_haut).gain_en_vitesse,(objects.equipement_rune_haut).gain_en_taux_de_coup_critique,(objects.equipement_rune_haut).gain_en_dommages_critiques,(objects.equipement_rune_haut).gain_en_resistance,(objects.equipement_rune_haut).gain_en_precision]])
            else:
                object_stats.append(0)
            if(objects.equipement_rune_haut_droite!=0):
                object_stats.append([(objects.equipement_rune_haut_droite).nom,(objects.equipement_rune_haut_droite).categorie,(objects.equipement_rune_haut_droite).position,(objects.equipement_rune_haut_droite).qualite,(objects.equipement_rune_haut_droite).rarete,(objects.equipement_rune_haut_droite).famille_de_bonus,(objects.equipement_rune_haut_droite).niveau,(objects.equipement_rune_haut_droite).bonus_secondaires,[(objects.equipement_rune_haut_droite).gain_en_pv,(objects.equipement_rune_haut_droite).gain_en_pourcentage_de_pv,(objects.equipement_rune_haut_droite).gain_en_attaque,(objects.equipement_rune_haut_droite).gain_en_pourcentage_de_attaque,(objects.equipement_rune_haut_droite).gain_en_defense,(objects.equipement_rune_haut_droite).gain_en_pourcentage_de_defense,(objects.equipement_rune_haut_droite).gain_en_vitesse,(objects.equipement_rune_haut_droite).gain_en_taux_de_coup_critique,(objects.equipement_rune_haut_droite).gain_en_dommages_critiques,(objects.equipement_rune_haut_droite).gain_en_resistance,(objects.equipement_rune_haut_droite).gain_en_precision]])
            else:
                object_stats.append(0)
            if(objects.equipement_rune_bas_droite!=0):
                object_stats.append([(objects.equipement_rune_bas_droite).nom,(objects.equipement_rune_bas_droite).categorie,(objects.equipement_rune_bas_droite).position,(objects.equipement_rune_bas_droite).qualite,(objects.equipement_rune_bas_droite).rarete,(objects.equipement_rune_bas_droite).famille_de_bonus,(objects.equipement_rune_bas_droite).niveau,(objects.equipement_rune_bas_droite).bonus_secondaires,[(objects.equipement_rune_bas_droite).gain_en_pv,(objects.equipement_rune_bas_droite).gain_en_pourcentage_de_pv,(objects.equipement_rune_bas_droite).gain_en_attaque,(objects.equipement_rune_bas_droite).gain_en_pourcentage_de_attaque,(objects.equipement_rune_bas_droite).gain_en_defense,(objects.equipement_rune_bas_droite).gain_en_pourcentage_de_defense,(objects.equipement_rune_bas_droite).gain_en_vitesse,(objects.equipement_rune_bas_droite).gain_en_taux_de_coup_critique,(objects.equipement_rune_bas_droite).gain_en_dommages_critiques,(objects.equipement_rune_bas_droite).gain_en_resistance,(objects.equipement_rune_bas_droite).gain_en_precision]])
            else:
                object_stats.append(0)
            if(objects.equipement_rune_bas!=0):
                object_stats.append([(objects.equipement_rune_bas).nom,(objects.equipement_rune_bas).categorie,(objects.equipement_rune_bas).position,(objects.equipement_rune_bas).qualite,(objects.equipement_rune_bas).rarete,(objects.equipement_rune_bas).famille_de_bonus,(objects.equipement_rune_bas).niveau,(objects.equipement_rune_bas).bonus_secondaires,[(objects.equipement_rune_bas).gain_en_pv,(objects.equipement_rune_bas).gain_en_pourcentage_de_pv,(objects.equipement_rune_bas).gain_en_attaque,(objects.equipement_rune_bas).gain_en_pourcentage_de_attaque,(objects.equipement_rune_bas).gain_en_defense,(objects.equipement_rune_bas).gain_en_pourcentage_de_defense,(objects.equipement_rune_bas).gain_en_vitesse,(objects.equipement_rune_bas).gain_en_taux_de_coup_critique,(objects.equipement_rune_bas).gain_en_dommages_critiques,(objects.equipement_rune_bas).gain_en_resistance,(objects.equipement_rune_bas).gain_en_precision]])
            else:
                object_stats.append(0)
            if(objects.equipement_rune_bas_gauche!=0):
                object_stats.append([(objects.equipement_rune_bas_gauche).nom,(objects.equipement_rune_bas_gauche).categorie,(objects.equipement_rune_bas_gauche).position,(objects.equipement_rune_bas_gauche).qualite,(objects.equipement_rune_bas_gauche).rarete,(objects.equipement_rune_bas_gauche).famille_de_bonus,(objects.equipement_rune_bas_gauche).niveau,(objects.equipement_rune_bas_gauche).bonus_secondaires,[(objects.equipement_rune_bas_gauche).gain_en_pv,(objects.equipement_rune_bas_gauche).gain_en_pourcentage_de_pv,(objects.equipement_rune_bas_gauche).gain_en_attaque,(objects.equipement_rune_bas_gauche).gain_en_pourcentage_de_attaque,(objects.equipement_rune_bas_gauche).gain_en_defense,(objects.equipement_rune_bas_gauche).gain_en_pourcentage_de_defense,(objects.equipement_rune_bas_gauche).gain_en_vitesse,(objects.equipement_rune_bas_gauche).gain_en_taux_de_coup_critique,(objects.equipement_rune_bas_gauche).gain_en_dommages_critiques,(objects.equipement_rune_bas_gauche).gain_en_resistance,(objects.equipement_rune_bas_gauche).gain_en_precision]])
            else:
                object_stats.append(0)
            if(objects.equipement_rune_haut_gauche!=0):
                object_stats.append([(objects.equipement_rune_haut_gauche).nom,(objects.equipement_rune_haut_gauche).categorie,(objects.equipement_rune_haut_gauche).position,(objects.equipement_rune_haut_gauche).qualite,(objects.equipement_rune_haut_gauche).rarete,(objects.equipement_rune_haut_gauche).famille_de_bonus,(objects.equipement_rune_haut_gauche).niveau,(objects.equipement_rune_haut_gauche).bonus_secondaires,[(objects.equipement_rune_haut_gauche).gain_en_pv,(objects.equipement_rune_haut_gauche).gain_en_pourcentage_de_pv,(objects.equipement_rune_haut_gauche).gain_en_attaque,(objects.equipement_rune_haut_gauche).gain_en_pourcentage_de_attaque,(objects.equipement_rune_haut_gauche).gain_en_defense,(objects.equipement_rune_haut_gauche).gain_en_pourcentage_de_defense,(objects.equipement_rune_haut_gauche).gain_en_vitesse,(objects.equipement_rune_haut_gauche).gain_en_taux_de_coup_critique,(objects.equipement_rune_haut_gauche).gain_en_dommages_critiques,(objects.equipement_rune_haut_gauche).gain_en_resistance,(objects.equipement_rune_haut_gauche).gain_en_precision]])
            else:
                object_stats.append(0)
            object_stats.append(objects.indice_stockage_base)
            object_stats.append(objects.surnom)
            return_list.append(object_stats)
    return return_list


def remplir_stockage_base(new_list,data_list):
    for objects in data_list:
        if(objects==0):
            new_list.append(0)
        else:
            Nom=objects[0]
            Attribut=objects[1]
            Classe=objects[2]
            Niveau=objects[3]
            XP_restante=objects[4]
            '''
            A partir de objects[i], reconstituer la rune avant de mettre dans equipement
            '''
            if(objects[5]!=0):
                equipement_rune_haut=Runes.Reinitialiser(objects[5][0],objects[5][1],objects[5][2],objects[5][3],objects[5][4],objects[5][5],objects[5][6],objects[5][7],objects[5][8]) 
            else:
                equipement_rune_haut=0
            if(objects[6]!=0):
                equipement_rune_haut_droite=Runes.Reinitialiser(objects[6][0],objects[6][1],objects[6][2],objects[6][3],objects[6][4],objects[6][5],objects[6][6],objects[6][7],objects[6][8])
            else:
                equipement_rune_haut_droite=0
            if(objects[7]!=0):
                equipement_rune_bas_droite=Runes.Reinitialiser(objects[7][0],objects[7][1],objects[7][2],objects[7][3],objects[7][4],objects[7][5],objects[7][6],objects[7][7],objects[7][8]) 
            else:
                equipement_rune_bas_droite=0
            if(objects[8]!=0):
                equipement_rune_bas=Runes.Reinitialiser(objects[8][0],objects[8][1],objects[8][2],objects[8][3],objects[8][4],objects[8][5],objects[8][6],objects[8][7],objects[8][8]) 
            else:
                equipement_rune_bas=0
            if(objects[9]!=0):
                equipement_rune_bas_gauche=Runes.Reinitialiser(objects[9][0],objects[9][1],objects[9][2],objects[9][3],objects[9][4],objects[9][5],objects[9][6],objects[9][7],objects[9][8]) 
            else:
                equipement_rune_bas_gauche=0
            if(objects[10]!=0):
                equipement_rune_haut_gauche=Runes.Reinitialiser(objects[10][0],objects[10][1],objects[10][2],objects[10][3],objects[10][4],objects[10][5],objects[10][6],objects[10][7],objects[10][8])
            else:
                equipement_rune_haut_gauche=0
            Equipement=[equipement_rune_haut,equipement_rune_haut_droite,equipement_rune_bas_droite,equipement_rune_bas,equipement_rune_bas_gauche,equipement_rune_haut_gauche]
            
            Place_dans_base=objects[11]
            Surnom=objects[12]
           
            monstre=Base.reset_monstre(Nom)
            while(monstre.attribut!=Attribut):
                monstre=Base.reset_monstre(Nom)
            
            if(Classe==2):
                monstre.pv=monstre.pv_min_2
                monstre.attaque=monstre.attaque_min_2
                monstre.defense=monstre.defense_min_2
            if(Classe==3):
                monstre.pv=monstre.pv_min_3
                monstre.attaque=monstre.attaque_min_3
                monstre.defense=monstre.defense_min_3
            if(Classe==4):
                monstre.pv=monstre.pv_min_4
                monstre.attaque=monstre.attaque_min_4
                monstre.defense=monstre.defense_min_4
            if(Classe==5):
                monstre.pv=monstre.pv_min_5
                monstre.attaque=monstre.attaque_min_5
                monstre.defense=monstre.defense_min_5
            if(Classe==6):
                monstre.pv=monstre.pv_min_6
                monstre.attaque=monstre.attaque_min_6
                monstre.defense=monstre.defense_min_6

            monstre.classe=Classe
            while(monstre.niveau!=Niveau):
                monstre=Donjon.Monter_en_niveau_sans_affichage(monstre)
            monstre.XP_avant_prochain_niveau=XP_restante

                
            for j in range(6):
                monstre=Runes.Equiper_sans_affichage(monstre,Equipement[j],j)
            Runes.BonusDeRunes(monstre)

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
            
            monstre.indice_dans_base=Place_dans_base
            monstre.surnom=Surnom
            Base.ajouter_monstre(base,monstre)
    
    return new_list
 

def remplir_team(equipe,data_list):
   # print('Data liste : ',data_list)
    for objects in data_list:
        #print('Object : ',objects)
        if(objects==0):
            equipe.append(0)
        elif(objects[11]!=OUT_OF_STOCKAGE):
            equipe.append(base.stockage[objects[11]])
        else:
            Nom=objects[0]
            Attribut=objects[1]
            Classe=objects[2]
            Niveau=objects[3]
            XP_restante=objects[4]
            Surnom=objects[12]
            '''
            A partir de object[i], reconstituer la rune avant de mettre dans equipement
            '''
            if(objects[5]!=0):
                equipement_rune_haut=Runes.Reinitialiser(objects[5][0],objects[5][1],objects[5][2],objects[5][3],objects[5][4],objects[5][5],objects[5][6],objects[5][7],objects[5][8]) 
            else:
                equipement_rune_haut=0
            if(objects[6]!=0):
                equipement_rune_haut_droite=Runes.Reinitialiser(objects[6][0],objects[6][1],objects[6][2],objects[6][3],objects[6][4],objects[6][5],objects[6][6],objects[6][7],objects[6][8])
            else:
                equipement_rune_haut_droite=0
            if(objects[7]!=0):
                equipement_rune_bas_droite=Runes.Reinitialiser(objects[7][0],objects[7][1],objects[7][2],objects[7][3],objects[7][4],objects[7][5],objects[7][6],objects[7][7],objects[7][8]) 
            else:
                equipement_rune_bas_droite=0
            if(objects[8]!=0):
                equipement_rune_bas=Runes.Reinitialiser(objects[8][0],objects[8][1],objects[8][2],objects[8][3],objects[8][4],objects[8][5],objects[8][6],objects[8][7],objects[8][8]) 
            else:
                equipement_rune_bas=0
            if(objects[9]!=0):
                equipement_rune_bas_gauche=Runes.Reinitialiser(objects[9][0],objects[9][1],objects[9][2],objects[9][3],objects[9][4],objects[9][5],objects[9][6],objects[9][7],objects[9][8]) 
            else:
                equipement_rune_bas_gauche=0
            if(objects[10]!=0):
                equipement_rune_haut_gauche=Runes(objects[10][0],objects[10][1],objects[10][2],objects[10][3],objects[10][4],objects[10][5],objects[10][6],objects[10][7],objects[10][8])
            else:
                equipement_rune_haut_gauche=0
            Equipement=[equipement_rune_haut,equipement_rune_haut_droite,equipement_rune_bas_droite,equipement_rune_bas,equipement_rune_bas_gauche,equipement_rune_haut_gauche]

            monstre=Base.reset_monstre(Nom)
            while(monstre.attribut!=Attribut):
                monstre=Base.reset_monstre(Nom)
            
            if(Classe==2):
                monstre.pv=monstre.pv_min_2
                monstre.attaque=monstre.attaque_min_2
                monstre.defense=monstre.defense_min_2
            if(Classe==3):
                monstre.pv=monstre.pv_min_3
                monstre.attaque=monstre.attaque_min_3
                monstre.defense=monstre.defense_min_3
            if(Classe==4):
                monstre.pv=monstre.pv_min_4
                monstre.attaque=monstre.attaque_min_4
                monstre.defense=monstre.defense_min_4
            if(Classe==5):
                monstre.pv=monstre.pv_min_5
                monstre.attaque=monstre.attaque_min_5
                monstre.defense=monstre.defense_min_5
            if(Classe==6):
                monstre.pv=monstre.pv_min_6
                monstre.attaque=monstre.attaque_min_6
                monstre.defense=monstre.defense_min_6

            monstre.classe=Classe
            while(monstre.niveau!=Niveau):
                monstre=Donjon.Monter_en_niveau_sans_affichage(monstre)
            monstre.XP_avant_prochain_niveau=XP_restante
            

            for j in range(6):
                monstre=Runes.Equiper_sans_affichage(monstre,Equipement[j],j)
            Runes.BonusDeRunes(monstre)
            
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
            
            monstre.surnom=Surnom
            equipe.append(monstre)
    return equipe



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

