


import socket

# from Client import *

serveur = "109.210.159.20"
# client = "82.252.134.200"
client = "88.120.157.226"
port = 17777
port_client = 17777*3

# socket.AF_INET : la famille d'adresses, ici ce sont des adresses Internet ;
# socket.SOCK_STREAM : le type du socket, SOCK_STREAM pour le protocole TCP

# Pour comprendre pourquoi il faut shutdown avant chaque close :
# https://stackoverflow.com/questions/409783/socket-shutdown-vs-socket-close


def init_team_ennemie(equipe, statut):
    # print("Statut : " + statut + "\n\n")
    if (statut == 'serveur'):
        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        connexion.bind(('', port))
        nb_max_connections_autorisées = 1
        connexion.listen(nb_max_connections_autorisées)
        client, address = connexion.accept()

        liste_de_monstres = []
        continuer = True
        index_monster = 0

        while continuer:
            response = client.recv(128)
            response = response.decode("utf-8")
            message = str(response)

            message_to_send = equipe.membres[index_monster].nom + ',' + equipe.membres[index_monster].attribut + ',' + str(equipe.membres[index_monster].classe) + ',' + str(equipe.membres[index_monster].niveau)

            if (response != ""):
                indice_virgule_1 = 0
                caractere_tmp = message[indice_virgule_1:indice_virgule_1+1]

                while(indice_virgule_1 < len(message) and caractere_tmp != ','):
                    indice_virgule_1 += 1
                    caractere_tmp = message[indice_virgule_1:indice_virgule_1+1]
        
                indice_virgule_2 = indice_virgule_1 + 1
                caractere_tmp = message[indice_virgule_2:indice_virgule_2+1]

                while(indice_virgule_2 < len(message) and caractere_tmp != ','):
                    indice_virgule_2 += 1
                    caractere_tmp = message[indice_virgule_2:indice_virgule_2+1]

                indice_virgule_3 = indice_virgule_2 + 1
                caractere_tmp = message[indice_virgule_3:indice_virgule_3+1]
        
                while(indice_virgule_3 < len(message) and caractere_tmp != ','):
                    indice_virgule_3 += 1
                    caractere_tmp = message[indice_virgule_3:indice_virgule_3+1]


                nom_monstre = message[0:indice_virgule_1]
                attribut_monstre = message[indice_virgule_1+1:indice_virgule_2]
                classe_monstre = message[indice_virgule_2+1:indice_virgule_3]
                niveau_monstre = message[indice_virgule_3+1:len(message)]
                monstre = equipe.reset_equipe(nom_monstre)
                if (monstre != 0 and attribut_monstre in ['Feu', 'Eau', 'Vent', 'Lumière', 'Ténèbres'] and classe_monstre in ['1','2','3','4','5','6'] and charToNumber(niveau_monstre) >= 1 and charToNumber(niveau_monstre) <= 5*charToNumber(classe_monstre)+10):
                    while (monstre.attribut != attribut_monstre):
                        monstre = equipe.reset_equipe(nom_monstre)
                    while (monstre.classe < charToNumber(classe_monstre)):
                        monstre.evoluer()
                    while (monstre.niveau < charToNumber(niveau_monstre)):
                        monstre.monter_en_niveau_sans_affichage()

                    # print("\n\n Monstre reçu côté serveur : ")
                    # print(monstre)
                    # print("\n\n")
                    liste_de_monstres.append(monstre)
                    if (len(liste_de_monstres) == 3):
                        continuer = False
                        client.send(bytes(message_to_send, encoding = "utf-8"))
                        #client.send(bytes("Tous les monstres ont bien été reçus. Merci d'attendre la réouverture de la connexion. Connection closed.", encoding = "utf-8"))
                    else:
                        client.send(bytes(message_to_send, encoding = "utf-8"))
                        index_monster += 1
                else:
                    if (not attribut_monstre in ['Feu', 'Eau', 'Vent', 'Lumière', 'Ténèbres']):
                        client.send(bytes("Attribut de monstre : " + attribut_monstre + " invalide. Connection closed.", encoding = "utf-8"))
                    elif (not classe_monstre in ['1','2','3','4','5','6']):
                        client.send(bytes("Classe de monstre : " + classe_monstre + " invalide. Connection closed.", encoding = "utf-8"))
                    elif (charToNumber(niveau_monstre) < 1 or charToNumber(niveau_monstre) > 5*charToNumber(classe_monstre)+10):
                        client.send(bytes("Niveau de monstre : " + str(niveau_monstre) + " invalide." + str(charToNumber(niveau_monstre) < 1) + " ou " + str(charToNumber(niveau_monstre) > 5*charToNumber(classe_monstre)+10) + "Connection closed.", encoding = "utf-8"))
                    elif (monstre == 0):
                        client.send(bytes("Nom de monstre : " + nom_monstre + " invalide. Connection closed.", encoding = "utf-8"))
                    contineur = False

                if ("close" in message):
                    continuer = False

        connexion.shutdown(socket.SHUT_RDWR)
        connexion.close()
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        return [address,liste_de_monstres]



    elif (statut == 'client'):
        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion.connect((serveur, port))

        liste_de_monstres = []
        liste_messages_to_send = []
        index_monster = 0
        while (index_monster < equipe.len):
            message_to_send = equipe.membres[index_monster].nom + ',' + equipe.membres[index_monster].attribut + ',' + str(equipe.membres[index_monster].classe) + ',' + str(equipe.membres[index_monster].niveau)
            liste_messages_to_send.append(message_to_send)
            index_monster += 1

        index_message = 0
        while (len(liste_de_monstres) < 3):
            to_send = bytes(str(liste_messages_to_send[index_message]), encoding = "utf-8")
            to_send = bytes(to_send.decode("utf-8"), encoding = "utf-8")
            # print (liste_de_monstres)
            # print("\n Until here it is okay (len(liste_de_monstres) = " + str(len(liste_de_monstres)) + ") \n\n")
            connexion.send(to_send)

            response = connexion.recv(512)
            if (response != ""):
                response = response.decode("utf-8")
                message = str(response)
            
            if (message != ""):
                indice_virgule_1 = 0
                caractere_tmp = message[indice_virgule_1:indice_virgule_1+1]

                while(indice_virgule_1 < len(message) and caractere_tmp != ','):
                    indice_virgule_1 += 1
                    caractere_tmp = message[indice_virgule_1:indice_virgule_1+1]
        
                indice_virgule_2 = indice_virgule_1 + 1
                caractere_tmp = message[indice_virgule_2:indice_virgule_2+1]

                while(indice_virgule_2 < len(message) and caractere_tmp != ','):
                    indice_virgule_2 += 1
                    caractere_tmp = message[indice_virgule_2:indice_virgule_2+1]

                indice_virgule_3 = indice_virgule_2 + 1
                caractere_tmp = message[indice_virgule_3:indice_virgule_3+1]
        
                while(indice_virgule_3 < len(message) and caractere_tmp != ','):
                    indice_virgule_3 += 1
                    caractere_tmp = message[indice_virgule_3:indice_virgule_3+1]


                nom_monstre = message[0:indice_virgule_1]
                attribut_monstre = message[indice_virgule_1+1:indice_virgule_2]
                classe_monstre = message[indice_virgule_2+1:indice_virgule_3]
                niveau_monstre = message[indice_virgule_3+1:len(message)]
                monstre = equipe.reset_equipe(nom_monstre)
                if (monstre != 0 and attribut_monstre in ['Feu', 'Eau', 'Vent', 'Lumière', 'Ténèbres'] and classe_monstre in ['1','2','3','4','5','6'] and charToNumber(niveau_monstre) >= 1 and charToNumber(niveau_monstre) <= 5*charToNumber(classe_monstre)+10):
                    while (monstre.attribut != attribut_monstre):
                        monstre = equipe.reset_equipe(nom_monstre)
                    while (monstre.classe < charToNumber(classe_monstre)):
                        monstre.evoluer()
                    while (monstre.niveau < charToNumber(niveau_monstre)):
                        monstre.monter_en_niveau_sans_affichage()

                    # print("\n\n Monstre reçu côté client : ")
                    # print(monstre)
                    # print("\n\n")
                    liste_de_monstres.append(monstre)
                    if (len(liste_de_monstres) == 3):
                        continuer = False
                    else:
                        index_message += 1 # l'envoi se fait juste après le retour du while
                else:
                    if (not attribut_monstre in ['Feu', 'Eau', 'Vent', 'Lumière', 'Ténèbres']):
                        connexion.send(bytes("Attribut de monstre : " + attribut_monstre + " invalide. Connection closed.", encoding = "utf-8"))
                    elif (not classe_monstre in ['1','2','3','4','5','6']):
                        connexion.send(bytes("Classe de monstre : " + classe_monstre + " invalide. Connection closed.", encoding = "utf-8"))
                    elif (charToNumber(niveau_monstre) < 1 or charToNumber(niveau_monstre) > 5*charToNumber(classe_monstre)+10):
                        connexion.send(bytes("Niveau de monstre : " + str(niveau_monstre) + " invalide." + str(charToNumber(niveau_monstre) < 1) + " ou " + str(charToNumber(niveau_monstre) > 5*charToNumber(classe_monstre)+10) + "Connection closed.", encoding = "utf-8"))
                    elif (monstre == 0):
                        connexion.send(bytes("Nom de monstre : " + nom_monstre + " invalide. Connection closed.", encoding = "utf-8"))
                    contineur = False

                if ("close" in message):
                    continuer = False

        connexion.shutdown(socket.SHUT_RDWR)
        connexion.close()
        return [(serveur,port),liste_de_monstres]


'''
def make_a_choice(possibilites):
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind(('', 17777))
    continuer = True
    nb_max_connections_autorisées = 1

    socket.listen(nb_max_connections_autorisées)
    client, address = socket.accept()

    while continuer:
        response = client.recv(64)
        if (response != ""):
            if (charToNumber(response) in possibilites):
'''








def listen_a_single_message(address_J2, statut_initial):
    #if (statut_initial == 'client'):
    #    address_J2 = (client, port_client)

    # print ("\n\n Adresse reçue : ")
    # print(address_J2)
    # print("\n\n")

    if (statut_initial == 'client'):
        port_to_listen = port_client
    elif (statut_initial == 'serveur'):
        port_to_listen = port

    # print ("\n\n Port to listen : ")
    # print(str(port_to_listen))
    # print("\n\n")

    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connexion.bind(('', port_to_listen))
    nb_max_connections_autorisées = 1
    connexion.listen(nb_max_connections_autorisées)
    client, address = connexion.accept()

    if (address[0] == address_J2[0]):
        response = client.recv(128)
        response = response.decode("utf-8")
        message = str(response)

        to_return = []
        indice_char = 0
        while(message[indice_char] != ']'):
            if (str.isdecimal(message[indice_char])):
                to_return.append(charToInt(message[indice_char]))
            indice_char += 1

        return to_return

    else:
        '''
        print ("\n\n Adresse attendue : ")
        print(address_J2)
        print("\n\n")
        print ("\n\n Adresse reçue : ")
        print(address)
        print("\n\n")
        exit(0)
        '''


# l'adresse donnée en paramètre est un couple (adresse IP, port)
def send_a_single_message(address, message, statut_initial):
    # print ("\n\n Adresse reçue pour envoi : ")
    # print(address)
    # print("\n\n")

    if (statut_initial == "serveur"):
        address = (client, port_client)
    elif (statut_initial == "client"):
        address = (address[0], port)

    # print ("\n\n Nouvelle adresse reçue pour envoi : ")
    # print(address)
    # print("\n\n")

    connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # print("\n Début connexion \n")
    connexion.connect(address)
    # print("\n Bien connecté \n")

    to_send = bytes(str(message), encoding = "utf-8")
    to_send = bytes(to_send.decode("utf-8"), encoding = "utf-8")
    # print("\n Début envoi \n")
    connexion.send(to_send)

    # print("\n Bien envoyé \n")

    connexion.shutdown(socket.SHUT_RDWR)
    connexion.close()



def charToInt(char):
    to_return = -1
    if (char == '0'):
        to_return = 0
    elif (char == '1'):
        to_return = 1
    elif (char == '2'):
        to_return = 2
    elif (char == '3'):
        to_return = 3
    elif (char == '4'):
        to_return = 4
    elif (char == '5'):
        to_return = 5
    elif (char == '6'):
        to_return = 6
    elif (char == '7'):
        to_return = 7
    elif (char == '8'):
        to_return = 8
    elif (char == '9'):
        to_return = 9
    return to_return

# Ne traite volontairement pas les nombres plus grand que 99 
# car l'appel se fait sur un nombre à max deux chiffres 
def charToNumber(char):
    if (len(char) == 2):
        result = charToInt(char[0:1])*10 + charToNumber(char[1:2])
    elif (len(char) == 1):
        result = charToInt(char)
    return result