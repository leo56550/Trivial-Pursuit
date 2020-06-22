#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:42:17 2020

@author: thierry
"""

from random import randint


yellow_questions = [{
"q" : "What color is pikachu ?",
"rc" : "Yellow",
"ri_lst" : ["black", "red", "green"],
}]

orange_questions = [{
"q" : "What city is the capital of Japan",
"rc" : "Tokyo",
"ri_lst" : ["Hiroshima", "Kyoto",
"Hosaka"],
}]

purple_questions = [{
"q" : "What is the title of the most famous song of Prince ?",
"rc" : "Purple rain",
"ri_lst" : ["deep purple", "thriller","let it be"],
}]

red_questions = [{
"q" : "What is the toughest communist country ?",
"rc" : "North Corea",
"ri_lst" : ["Russia", "Cuba","Poland"],
}]

green_questions = [{
"q" : "What color is alien blood ?",
"rc" : "Green",
"ri_lst" : ["Red", "Blue","Brown"],
}]

blue_questions = [{
"q" : "Of what color is Depardieu's nose ?",
"rc" : "red ",
"ri_lst" : ["green", "blue","gray"],
}]






base_questions = { 
 "yellow" :  yellow_questions ,
 "red" :     red_questions  ,    
 "orange" :  orange_questions ,
 "green" :   green_questions ,
 "blue" :    blue_questions ,
 "purple" :  purple_questions 
 
 } 



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

#Cette fonction pose une question de la couleur donnée au joueur courant, s'il répond correctement, la fonction
#retourne True sinon False
def poserQuestion(color) : 
    
    if color == "white":
        color = "red" # TODO ask the teacher what to do in this case
    
    questions = base_questions[color]
    index_question = randint(1,len(questions))
    question = questions[index_question-1]
    print(question["q"] )
    
    # TODO randomize the choices proposal order
    
    print(" Here are 4 possibilities : "+ 
          question["rc"] +  "(1), " + 
          question["ri_lst"][0] + "(2) , "+
          question["ri_lst"][1] + "(3) , "+
          question["ri_lst"][2]) + "(4)" 
    reponse = raw_input("1/2/3/4 ?").lstrip()
    
    if reponse == "1" :
        print("You are right")
        return True
    
    return False
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
    print("It's a " + color + " question."  )
    
    #Si le joueur tombe sur une case blanche
    if color == "white" and case["type"] ==  "normal" : 
        return 1 
    # Pose une question pour la couleur donnée.  
    ret = poserQuestion(color)
    
    if ret == True : 
        if case["type"] == "intersection" : 
            joueur["score"] += 1 
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
                            "token position" : 0 ,
                            "score" : 0})
    
        
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