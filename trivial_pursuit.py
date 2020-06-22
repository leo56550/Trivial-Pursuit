#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:42:17 2020

@author: thierry
"""

from random import randint
 

plateau = [
    {"type" :"intersection", "couleur" : "white" },
    {"type" :"normal", "couleur" : "orange" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "green" },
    {"type" :"normal", "couleur" : "red" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "blue" },
    {"type" :"intersection", "couleur" : "white" },
    {"type" :"normal", "couleur" : "blue" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "orange" },
    {"type" :"normal", "couleur" : "yellow" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "red" },
    {"type" :"intersection", "couleur" : "white" },
    {"type" :"normal", "couleur" : "red" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "blue" },
    {"type" :"normal", "couleur" : "purple" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "yellow" },
    {"type" :"intersection", "couleur" : "white" },
    {"type" :"normal", "couleur" : "yellow" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "red" },
    {"type" :"normal", "couleur" : "green" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "purple" },
    {"type" :"intersection", "couleur" : "white" },
    {"type" :"normal", "couleur" : "purple" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "yellow" },
    {"type" :"normal", "couleur" : "orange" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "green" },
    {"type" :"intersection", "couleur" : "white" },
    {"type" :"normal", "couleur" : "green" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "purple" },
    {"type" :"normal", "couleur" : "blue" },
    {"type" :"normal", "couleur" : "white" },
    {"type" :"normal", "couleur" : "orange" }
     ]

print (plateau)


#Cette fonction permet de lancer un de a 6 faces et de retourner une valeur au hasard

def random_de() :
    return randint(1,6)

#Cette fonction déroule un coup pour le joueur courant (passé entre paramètre), elle retourne 1 si il doit rejouer, et 2 sinon.
def deroulement_d1_coup (joueur) :
    valeur_de = random_de()   
    print(joueur["nom"] +  " is playing and made a "+ str(valeur_de) + " with the dice")


    while True : 
        deplacement = raw_input("To what direction ?  (C)lockwise or (A)nticlockwise").lstrip()
        if deplacement == "C" :
            forward = True
            break;
        if deplacement == "A" :
            forward = False
            break;
    
        print("Please say 'C' or 'A'")
        
    position_courante = joueur["token position"]
    if forward == True :
        position_courante += valeur_de
        if position_courante >= 42 : 
            position_courante -= 42 
    else :
        position_courante -= valeur_de 
        if position_courante < 0 :
            position_courante += 42
    joueur["token position"] = position_courante

    case = plateau[position_courante]
    color = case["couleur"]
    print("It's a " + color )
    
#Si le joueur tombe sur une case blanche
    if color == "white" :
        return 1 
    
    
    return 2
    
    

            



def jeu () : 
    
    liste_joueurs = []    
    nb_max_joueurs = 4 
      
# Saisir le nombre de joueurs
    while True : 
        nombre_de_joueurs = raw_input("Veuillez saisir le nombre de joueurs svp :  (maximum " + str(nb_max_joueurs) + ")" ).lstrip()
        nombre_de_joueurs = int(nombre_de_joueurs)
        if nombre_de_joueurs > nb_max_joueurs :
            print("Veuillez saisir un nombre inférieur ou égal à " + str(nb_max_joueurs))     
        else : 
            break 
          
    # Saisir les noms des joueurs  
    for i in range(0,nombre_de_joueurs) : 
        nom_du_joueur = raw_input("Veuillez saisir le nom du joueur " + str(i+1)+":").lstrip()
        liste_joueurs.append({"nom" : nom_du_joueur , 
                            "token position" : 0})
    
        
    print("Voici les joueurs" + str(liste_joueurs) ) 
    
    #Cette variable pointe vers le joueur à qui c'est le tour de jouer 
    numero_joueur_courant = 0
    
    #La partie commence
    while True :
        joueur_courant = liste_joueurs[numero_joueur_courant]
        ret = deroulement_d1_coup(joueur_courant)
        if ret == 2 : 
            numero_joueur_courant +=1 
        if numero_joueur_courant >= nombre_de_joueurs : 
            numero_joueur_courant -= nombre_de_joueurs
    
    

#PP
    
jeu()