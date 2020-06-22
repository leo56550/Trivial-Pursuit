#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:42:17 2020

@author: thierry
"""

from random import randint
 
#Cette fonction permet de lancer un de a 6 faces et de retourner une valeur au hasard
def random_de() :
    return randint(1,6)


 
#Programme principal

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
                        "score" : 0})

    
print("Voici les joueurs" + str(liste_joueurs) ) 



# calculer le gagnant       
score_max = 0
for joueur in  liste_joueurs :
    if joueur["score"] > score_max:
        score_max = joueur["score"]
        gagnant =  joueur
        
print("Le gagnant est : " + gagnant["nom"] + " et son score est : " + str(gagnant["score"]) ) 