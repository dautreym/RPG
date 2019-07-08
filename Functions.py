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

# POUR FAIRE LA PARTIE ENTIERE D UN NOMBRE
# nombre=math.floor(nombre)
# POUR LA FAIRE PAR EXCES PLUTOT QUE PAR DEFAUT
# nombre=math.ceil(nombre)


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
