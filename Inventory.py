
from Monsters import Security
from Runes_and_Objects import *

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

    def recevoir_gold(self,montant,nb_ennemis):
        self.mana += (montant*nb_ennemis)
        print('Vous recevez ',montant*nb_ennemis,' pierres de Mana!!')
        print('Vous avez désormais ',self.mana,' pierres de Mana!! \n\n')
        str(input(' > '))
        
    def est_full(self,zone):
        if(zone=='equipement'):
            if(self.place_dernier_equipement==99):
                full=True
            else:
                full=False

        elif(zone=='objets_courants'):
            if(self.place_dernier_objet_courant==99):
                full=True
            else:
                full=False
        return full

    def ajouter_objet(self,objet):
        if(objet.type=='Rune'):
            if (not self.est_full('equipement')):
                self.equipement[self.place_dernier_equipement+1] = objet
                self.place_dernier_equipement+=1
            else:
                print('Dommage!! La partie runes du sac est pleine... \n')

        elif(objet.type=='Objet_courant'):
            if (not self.est_full('objets_courants')):
                self.objets_courants[self.place_dernier_objet_courant+1] = objet
                self.place_dernier_objet_courant+=1
            else:
                print('Dommage!! La partie objets courants du sac est pleine... \n')
        else:
            print('\n Vous ne devriez pas toucher à cet objet... \n ')


    def afficher_argent(self):
        print('\n Vous avez actuellement ',self.mana,'pierres de mana.')
        print('Vous avez actuellement ',self.cristaux,'cristaux.')
        print('Vous avez actuellement ',self.pierres_de_fusion,'pierres de fusion. \n')

    # Jamais utilisee, plutot regarder section
    def afficher_contenu_sac_entier(self):
        print('0 = afficher les runes ')
        print('1 = afficher les objets courants \n')
        entree=input('Que voulez-vous afficher ? ')

        while(not Security.is_decimal(entree)):
            entree=input('Que voulez-vous afficher ? ')
        choix=int(entree)
        while(choix != 0 and choix != 1):
            entree=input('Que voulez-vous afficher ? ')
            while(not Security.is_decimal(entree)):
                entree=input('Que voulez-vous afficher ? ')
            choix=int(entree)
        
        if (choix == 0):
            for index in range(self.place_dernier_equipement):
                print('Vous avez la rune : ',self.equipement[index+1],' à l\'emplacement ',index+1,'\n')
        if (choix == 1):
            for index in range(self.place_dernier_objet_courant):
                print('Vous avez l\'objet : ',self.objets_courants[index+1],' à l\'emplacement',index+1,'\n')
        print('\n')

    def afficher_contenu_sac_section(self,section):
        if (section == 'equipement'):
            for index in range(self.place_dernier_equipement):
                print('Vous avez la rune : ',self.equipement[index+1],' à l\'emplacement ',index+1)
            if(self.place_dernier_equipement == 0):
                print('Vous ne transportez aucune rune pour le moment.')
        if (section == 'objets_courants'):
            for index in range(self.place_dernier_objet_courant):
                print('Vous avez l\'objet : ',(self.objets_courants[index]).nom,' à l\'emplacement',index,'\n')
            if(self.place_dernier_objet_courant == 0):
                print('Vous ne transportez aucun parchemin pour le moment.')
        print('\n')


    def afficher_contenu_sac_zone_unique(self,zone,indice):
        if (zone == 'equipement'):
            if (indice > 0 and indice <= self.place_dernier_equipement):
                print('Vous avez la rune : ',self.equipement[indice],'à l\'emplacement ',indice)
            else:
                print('Vous n\'avez aucune rune à cet emplacement du sac.')
        else:
            if(zone == 'objets_courants'):
                if (indice > 0 and indice <= self.place_dernier_objet_courant):
                    print('Vous avez l\'objet : ',self.objets_courants[indice].nom,'à l\'emplacement ',indice)
                    print('Il vous coûterait ',self.objets_courants[indice].prix_d_utilisation,'pierres de mana pour l\'utiliser.')
                else:
                    print('Vous n\'avez aucun objet à cet emplacement du sac.')
        print('\n')


    # Pas besoin de traiter le cas où la rune est équipée à un monstre 
    # car lors de l'équipement de la rune, cette dernière disparait de l'inventaire
    # (réapparait lorsque déséquipée) 
    def supprimer_objet(self,zone):
        possibilites_suppression_parchemin=[]
        possibilites_suppression_rune=[]
        if (zone == 'equipement'):
            index=1
            while(index <= self.place_dernier_equipement):
                self.afficher_contenu_sac_zone_unique(zone,index)
                possibilites_suppression_rune.append(index)
                index+=1
            if(len(possibilites_suppression_rune) == 0):
                print('Vous n\'avez aucune rune à jeter.')
            
            else:
                entree=input('\nQuelle rune voulez-vous jeter ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQuelle rune voulez-vous jeter ? ')
                indice=int(entree)
                while(indice not in possibilites_suppression_rune):
                    indice=input('\nQuelle rune voulez-vous jeter ? ')
                    indice=int(indice)
                    # print(possibilites_suppression_rune,' (affichage 1) ',indice,indice in possibilites_suppression_rune,'\n\n')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQuelle rune voulez-vous jeter ? ')
                        indice=int(entree)

                    # print(possibilites_suppression_rune,'Indice après conversion : ',indice,int(indice),indice in possibilites_suppression_rune,int(indice) in possibilites_suppression_rune,'\n\n')
                    # claqué au sol 

                if (indice > 0 and indice <= self.place_dernier_equipement):
                    print('Êtes vous sûr(e) de vouloir jeter la rune ',self.equipement[indice].nom,' ? \n')
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
                        print('La rune ',self.equipement[indice].nom,' a bien été jetée. \n')
                        self.equipement[indice]=0
                        for index in range(indice,self.place_dernier_equipement-1):
                            self.equipement[index]=self.equipement[index+1]
                        self.equipement[self.place_dernier_equipement]=0
                        self.place_dernier_equipement-=1
                else:
                    print('Vous n\'avez aucune rune à cet emplacement du sac.')
        else:
            if(zone=='objets_courants'):
                index=1
                while(index <= self.place_dernier_objet_courant):
                    self.afficher_contenu_sac_zone_unique(zone,index)
                    possibilites_suppression_parchemin.append(index)
                    index+=1
                if(len(possibilites_suppression_parchemin) == 0):
                    print('Vous n\'avez aucun parchemin à jeter.')

                else:
                    entree=input('\nQuel parchemin voulez-vous jeter ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nQuel parchemin voulez-vous jeter ? ')
                    indice=int(entree)
                    while(indice not in possibilites_suppression_parchemin):
                        entree=input('\nQuel parchemin voulez-vous jeter ? ')
                        while(not Security.is_decimal(entree)):
                            entree=input('\nQuel parchemin voulez-vous jeter ? ')
                        indice=int(entree)

                    if (indice > 0 and indice <= self.place_dernier_objet_courant):
                        print('Êtes vous sûr(e) de vouloir jeter l\'objet ',self.objets_courants[indice].nom,' ? \n')
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
                            print('L\'objet ',self.objets_courants[indice].nom,' a bien été jeté. \n')
                            self.objets_courants[indice]=0
                            for index in range(indice,self.place_dernier_objet_courant-1):
                                self.objets_courants[index]=self.objets_courants[index+1]
                            self.objets_courants[self.place_dernier_objet_courant]=0
                            self.place_dernier_objet_courant-=1
                    else:
                        print('Vous n\'avez aucun objet à cet emplacement du sac.')
        print('\n')


    def supprimer_objet_courant_sans_affichage(self,indice):
        if (indice > 0 and indice <= self.place_dernier_objet_courant):
            for index in range(indice,self.place_dernier_objet_courant):
                self.objets_courants[index]=self.objets_courants[index+1]
            self.objets_courants[self.place_dernier_objet_courant]=0
            self.place_dernier_objet_courant-=1
        else:
            print('Vous n\'avez aucun objet à cet emplacement du sac.')
        print('\n\n')

    def supprimer_equipement_sans_affichage(self,indice):
        if (indice > 0 and indice <= self.place_dernier_equipement):
            for index in range(indice,self.place_dernier_equipement):
                self.equipement[index]=self.equipement[index+1]
            self.equipement[self.place_dernier_equipement]=0
            self.place_dernier_equipement-=1
        else:
            print('Vous n\'avez aucune rune à cet emplacement du sac.')
        print('\n\n')


    # Magasin à refaire 
    # Prendre en paramètre le nombre de niveaux débloqués 
    # Proposer une liste d'items en conséquence 
    # Ne proposer qu'une rune par catégorie PUIS au moment de l'achat faire choisir la position
    def magasin(self):
        print('\nBienvenu au magasin Chirino!!')
        print('Vous pouvez choisir parmi les options suivantes : ')
        print('Acheter des parchemins = 0')
        print('Acheter des runes = 1')
        print('Vendre un objet = 2')
        print('Revenir au menu principal = 3')
        # Le game.possibilites se fait après le retour de cette fonction. Ce n'est pas un oubli !

        entree=input('\n Que voulez-vous faire ? ')
        while(not Security.is_decimal(entree)):
            entree=input('\n Que voulez-vous faire ? ')
        choix_magasin=int(entree)
        while(choix_magasin!=0 and choix_magasin!=1 and choix_magasin!=2 and choix_magasin!=3):
            entree=input('\n Que voulez-vous faire ? ')
            while(not Security.is_decimal(entree)):
                entree=input('\n Que voulez-vous faire ? ')
            choix_magasin=int(entree)

        if(choix_magasin == 0):
            print('Voici la liste des parchemins disponibles : ')
            Parchemin_d_invocation=Objets('Parchemin d invocation')
            Parchemin_d_invocation_superieure=Objets('Parchemin d invocation superieure')
            Parchemin_d_invocation_ultra_superieure=Objets('Parchemin d invocation ultra superieure')
            print('Ne rien acheter = 0')
            print('Parchemin d invocation (1 à 3 étoiles)  :  Prix d achat : ',Parchemin_d_invocation.prix_d_achat,'  = 1')
            print('Parchemin d invocation superieure (3 à 5 étoiles)  :  Prix d achat : ',Parchemin_d_invocation_superieure.prix_d_achat,'  = 2')
            print('Parchemin d invocation ultra superieure (3 à 5 étoiles) : Prix d achat : ',Parchemin_d_invocation_ultra_superieure.prix_d_achat,'  = 3')
            
            entree=input('\nQue voulez-vous acheter ? ')
            while(not Security.is_decimal(entree)):
                entree=input('\nQue voulez-vous acheter ? ')
            parchemin_a_acheter=int(entree)
            while(parchemin_a_acheter!=0 and parchemin_a_acheter!=1 and parchemin_a_acheter!=2 and parchemin_a_acheter!=3):
                entree=input('\nQue voulez-vous acheter ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQue voulez-vous acheter ? ')
                parchemin_a_acheter=int(entree)
            
            if(parchemin_a_acheter == 0):
                self.magasin()
            if(parchemin_a_acheter == 1):
                self.acheter_objet(Parchemin_d_invocation)
            if(parchemin_a_acheter == 2):
                self.acheter_objet(Parchemin_d_invocation_superieure)
            if(parchemin_a_acheter == 3):
                self.acheter_objet(Parchemin_d_invocation_ultra_superieure)

        if(choix_magasin == 1):
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
            while(not Security.is_decimal(entree)):
                entree=input('\nQuelle est la catégorie de la rune que vous voulez acheter ? ')
            choix_categorie_rune_a_acheter=int(entree)
            while(choix_categorie_rune_a_acheter not in possibilites_categorie_rune_a_acheter):
                entree=input('\nQuelle est la catégorie de la rune que vous voulez acheter ? ')
                while(not Security.is_decimal(entree)):
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

            if(choix_categorie_rune_a_acheter == 0):
                self.magasin()
            else:
                print('Ne rien acheter = 0 \n')
                possibilites_runes_a_acheter=[0]
                for index in range(len(Rune_toutes_categories_I[choix_categorie_rune_a_acheter-1])):
                    print(Rune_toutes_categories_I[choix_categorie_rune_a_acheter-1][index])
                    print('Prix d achat :',Rune_toutes_categories_I[choix_categorie_rune_a_acheter-1][index].prix_d_achat,' : rentrez ',index+1,' au moment du choix \n')
                    str(input(' > '))
                    possibilites_runes_a_acheter.append(index+1)

                entree=input('\nQue voulez-vous acheter ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nQue voulez-vous acheter ? ')
                indice_rune_a_acheter=int(entree)
                while(indice_rune_a_acheter not in possibilites_runes_a_acheter):
                    entree=input('\nQue voulez-vous acheter ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('Que voulez-vous acheter ? ')
                    indice_rune_a_acheter=int(entree)
                if(indice_rune_a_acheter == 0):
                    self.magasin()
                else:
                    rune_a_acheter=Rune_toutes_categories_I[choix_categorie_rune_a_acheter-1][indice_rune_a_acheter-1]
                    self.acheter_objet(rune_a_acheter)

        if(choix_magasin == 2):
            entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre un parchemin ? ')
            while(not Security.is_decimal(entree)):
                entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre un parchemin ? ')
            choix_objet_a_vendre=int(entree)
            while(choix_objet_a_vendre!=0 and choix_objet_a_vendre!=1):
                entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre un parchemin ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre un parchemin ? ')
                choix_objet_a_vendre=int(entree)

            if(choix_objet_a_vendre == 1):
                entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre une rune ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre une rune ? ')
                choix_objet_a_vendre_2=int(entree)
                while(choix_objet_a_vendre_2!=0 and choix_objet_a_vendre_2!=1):
                    entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre une rune ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('\nOui = 0 \nNon = 1 \nVoulez-vous vendre une rune ? ')
                    choix_objet_a_vendre_2=int(entree)

                if(choix_objet_a_vendre_2==1):
                    print('Je vois, vous avez changé d\'avis!!  \n')
                    self.magasin()
                else:
                    possibilites_runes_a_vendre=[]
                    index=1
                    while(index <= self.place_dernier_equipement):
                        self.afficher_contenu_sac_zone_unique('equipement',index)
                        possibilites_runes_a_vendre.append(index)
                        index+=1
                    if(len(possibilites_runes_a_vendre) == 0):
                        print('Vous n\'avez aucune rune à vendre pour le moment.')
                        self.magasin()
                    else:
                        entree=input('Quelle rune voulez-vous vendre ? ')
                        while(not Security.is_decimal(entree)):
                            entree=input('Quelle rune voulez-vous vendre ? ')
                        place_rune_a_vendre=int(entree)
                        while(place_rune_a_vendre not in possibilites_runes_a_vendre):
                            entree=input('Quelle rune voulez-vous vendre ? ')
                            while(not Security.is_decimal(entree)):
                                entree=input('Quelle rune voulez-vous vendre ? ')
                            place_rune_a_vendre=int(entree)

                        self.vendre_objet('equipement',place_rune_a_vendre)
            else:
                possibilites_parchemins_a_vendre=[]
                index=1
                while(index <= self.place_dernier_objet_courant):
                    self.afficher_contenu_sac_zone_unique('objets_courants',index)
                    possibilites_parchemins_a_vendre.append(index)
                    index+=1
                if(len(possibilites_parchemins_a_vendre)==0):
                    print('Vous n\'avez aucun parchemin à vendre pour le moment.')
                    self.magasin()
                else:
                    entree=input('Quel parchemin voulez-vous vendre ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('Quel parchemin voulez-vous vendre ? ')
                    place_parchemin_a_vendre=int(entree)
                    while(place_parchemin_a_vendre not in possibilites_parchemins_a_vendre):
                        entree=input('Quel parchemin voulez-vous vendre ? ')
                        while(not Security.is_decimal(entree)):
                            entree=input('Quel parchemin voulez-vous vendre ? ')
                        place_parchemin_a_vendre=int(entree)
                    self.vendre_objet('objets_courants',place_parchemin_a_vendre)


    def acheter_objet(self,objet_achete):
        if(objet_achete.prix_d_achat > self.mana):
            print('Vous n\'avez pas assez de pierres de mana pour acheter ceci. \n')
        else:
            self.mana-=objet_achete.prix_d_achat
            print('Vous avez acheté ',objet_achete.nom,'!!')
            if(objet_achete.type == 'Rune'):
                print(objet_achete,'\n')
            self.ajouter_objet(objet_achete)
        self.magasin()


    def vendre_objet(self,zone,indice):
        if (zone == 'equipement'):
            if (indice > 0 and indice <= self.place_dernier_equipement):
                valeur=self.equipement[indice].prix_d_achat/2
                print('La valeur de la rune que vous voulez vendre est de ',valeur,' pierres de mana.')
                print('Êtes vous sûr(e) de vouloir vendre la rune ',self.equipement[indice].nom,' ? \n')
                entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                while(not Security.is_decimal(entree)):
                    entree=input('Oui = 0 \nNon = 1 \nQuel est ovtre choix ? ')
                choix=int(entree)
                while(choix!=0 and choix!=1):
                    entree=input('\n\nOui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    choix=int(entree)
                if (choix == 0):
                    print('La rune ',self.equipement[indice].nom,' a bien été vendue. \n')
                    self.equipement[indice]=0
                    for index in range(indice,self.place_dernier_equipement-1):
                        sac.equipement[index]=self.equipement[index+1]
                    self.equipement[self.place_dernier_equipement]=0
                    self.place_dernier_equipement-=1
                    self.mana+=valeur
            else:
                print('Vous n\'avez aucune rune à cet emplacement du sac.')
        else:
            if(zone == 'objets_courants'):
                if (indice > 0 and indice <= self.place_dernier_objet_courant):
                    valeur=self.objets_courants[indice].prix_de_vente
                    print('La valeur de l\'objet que vous voulez vendre est de ',valeur,' pierres de mana.')
                    print('Êtes vous sûr(e) de vouloir vendre l\'objet ',self.objets_courants[indice].nom,' ? \n')
                    entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    while(not Security.is_decimal(entree)):
                        entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                    choix=int(entree)
                    while(choix!=0 and choix!=1):
                        entree=input('\n\nOui = 0 \nNon = 1 \nQuel est votre choix ? ')
                        while(not Security.is_decimal(entree)):
                            entree=input('Oui = 0 \nNon = 1 \nQuel est votre choix ? ')
                        choix=int(entree)
                    if (choix == 0):
                        print('L\'objet ',self.objets_courants[indice].nom,' a bien été vendu.')
                        print('Vous recevez ',valeur,'pierres de mana!! \n')
                        self.objets_courants[indice]=0
                        for index in range(indice,self.place_dernier_objet_courant-1):
                            self.equipement[index]=sac.objets_courants[index+1]
                        self.objets_courants[self.place_dernier_objet_courant]=0
                        self.place_dernier_objet_courant-=1
                        self.mana+=valeur
                else:
                    print('Vous n\'avez aucun objet à cet emplacement du sac.')
        print('\n')
        self.magasin()

