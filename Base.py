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
