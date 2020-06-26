#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:42:17 2020

@author: leo
"""

import math
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sqlite3


conn = sqlite3.connect('trivia.sqlite3')

cur =conn.cursor()

# TODO -> find lowest and highest IDs with "select"

nbquestions=cur.execute('select count(*) from question').fetchall()
print('nb:' + str(nbquestions))

rand_question=random.randint(1, nbquestions[0][0])

print("nb rand  "+ str(rand_question))

for row in cur.execute('select q.input from question q where q.id_question = ' + str(rand_question)).fetchall():
    print(row)

for row in cur.execute('select a.text,a.is_correct from answer a,question q where a.id_question = q.id_question and q.id_question = ' + str(rand_question)).fetchall():
    print(row)


img = mpimg.imread('./img/plateau2.png')
imgplot = plt.imshow(img)

plt.ion()
plt.show()




#Pour que le joueur ait plusieurs choix, il aurait fallu tirer au hasard
#les réponses dans une liste de choix


    

#Programme principal avec la fonction "jeu" demandée
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
    {"type" :"intersection", "couleur" : "red", "coord" : (26 , 260 ) },
    {"type" :"normal", "couleur" : "orange", "coord" : (30 , 215) },
    {"type" :"normal", "couleur" : "white", "coord" : (41 , 188  ) },
    {"type" :"normal", "couleur" : "green", "coord" : (49 ,154 ) },
    {"type" :"normal", "couleur" : "red" , "coord" : (70 , 132)},
    {"type" :"normal", "couleur" : "white", "coord" : (89 , 108 ) },
    {"type" :"normal", "couleur" : "blue" , "coord" : (110 ,88 )},
    {"type" :"intersection", "couleur" : "blue", "coord" : (150 ,57 ) },
    {"type" :"normal", "couleur" : "blue", "coord" : ( 184,42 ) },
    {"type" :"normal", "couleur" : "white" , "coord" : (211 ,32 )},
    {"type" :"normal", "couleur" : "orange" , "coord" : (242 ,32 )},
    {"type" :"normal", "couleur" : "yellow" , "coord" : (273 ,31 )},
    {"type" :"normal", "couleur" : "white", "coord" : ( 310,36 ) },
    {"type" :"normal", "couleur" : "red" , "coord" : (338 ,40 )},
    {"type" :"intersection", "couleur" : "orange", "coord" : (373 , 57 ) },
    {"type" :"normal", "couleur" : "red", "coord" : (411 , 85 ) },
    {"type" :"normal", "couleur" : "white", "coord" : (433 , 108 ) },
    {"type" :"normal", "couleur" : "blue" , "coord" : (452 , 129 )},
    {"type" :"normal", "couleur" : "purple" , "coord" : ( 467,126 )},
    {"type" :"normal", "couleur" : "white" , "coord" : ( 477,195 )},
    {"type" :"normal", "couleur" : "yellow" , "coord" : (488 ,216 )},
    {"type" :"intersection", "couleur" : "yellow" , "coord" : ( 493,261 )},
    {"type" :"normal", "couleur" : "yellow" , "coord" : (486 ,303 )},
    {"type" :"normal", "couleur" : "white", "coord" : ( 480,337 ) },
    {"type" :"normal", "couleur" : "red" , "coord" : (470 ,361 )},
    {"type" :"normal", "couleur" : "green", "coord" : (453 ,392 ) },
    {"type" :"normal", "couleur" : "white", "coord" : (432 ,417 ) },
    {"type" :"normal", "couleur" : "purple" , "coord" : ( 411, 436 )},
    {"type" :"intersection", "couleur" : "purple" , "coord" : (376 ,464 )},
    {"type" :"normal", "couleur" : "purple", "coord" : ( 335,478 ) },
    {"type" :"normal", "couleur" : "white", "coord" : (301 ,488 ) },
    {"type" :"normal", "couleur" : "yellow", "coord" : ( 274,492 ) },
    {"type" :"normal", "couleur" : "orange", "coord" : ( 254,492 ) },
    {"type" :"normal", "couleur" : "white" , "coord" : (215 ,484 )},
    {"type" :"normal", "couleur" : "green" , "coord" : (183 ,482 )},
    {"type" :"intersection", "couleur" : "green" , "coord" : (146 ,460 )},
    {"type" :"normal", "couleur" : "green" , "coord" : ( 107,440 )},
    {"type" :"normal", "couleur" : "white" , "coord" : ( 89,415 )},
    {"type" :"normal", "couleur" : "purple", "coord" : ( 65,391 ) },
    {"type" :"normal", "couleur" : "blue" , "coord" : ( 54,361 )},
    {"type" :"normal", "couleur" : "white" , "coord" : ( 38,334 )},
    {"type" :"normal", "couleur" : "orange", "coord" : ( 35,309 ) }

]

# Tip: select from sqlite

# sqlite> select a.text from answer a,question q where a.id_question = q.id_question and q.id_question = 2800;
#Lava Axe
#Stone-Throwing Devils
#Ember Shot
#Throwing Knife

# 

couleurs_jetons = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple',
                   'tab:yellow']
#Cette variable globale représente le rayon du cercle sur lequel les jetons évoluent
R = img.shape[0] / 2 - 28;

NbCases = 42


#Cette fonction pose une question de la couleur donnée au joueur courant, s'il répond correctement, la fonction
#retourne True sinon False
def poserQuestion(color) : 
    
    if color == "white":
        color = "red" # TODO ask the teacher what to do in this case
    
    questions = base_questions[color]
    index_question = random.randint(1,len(questions))
    question = questions[index_question-1]
    print(question["q"] )
    

#Melange des choix afin que la premiere reponse ne soit pas
#toujours la bonne.
    
    all_choices = [ (question["rc"], True),
                    (question["ri_lst"][0], False),
                    (question["ri_lst"][1], False),
                    (question["ri_lst"][2], False) ]
    
    random.shuffle(all_choices)
    
    print(" Here are 4 possibilities : "+ 
       all_choices[0][0] +  "(1), " + 
       all_choices[1][0] +  "(2), " + 
       all_choices[2][0] +  "(3), " + 
       all_choices[3][0] +  "(4) "  )
       
    
    reponse = input("1/2/3/4 ?").lstrip()
    num = int(reponse)
    
    if all_choices[num-1][1] == True :
        print("You are right")
        return True
    
    return False
#Cette fonction permet de lancer un de a 6 faces et de retourner une valeur au hasard

def random_de() :
    return random.randint(1,6)

#Cette fonction déroule un coup pour le joueur courant (passé entre paramètre), elle retourne 1 si il doit rejouer, et 2 sinon.
def deroulement_d1_coup (joueur) :
    valeur_de = random_de()
    print(joueur["nom"] +  " is playing and made a "+ str(valeur_de) + " with the dice")


    while True : 
        deplacement = input("To what direction ?  (C)lockwise or (A)nticlockwise").lstrip().upper()
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
    
    positionner_pion(joueur)

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

    
    plt.show()
    return 2
    


#La fonction "jeu" demandée dans les consignes
def jeu () : 
    
    
    
    liste_joueurs = []    
    nb_max_joueurs = 6
      
# Saisir le nombre de joueurs
    while True : 
        nombre_de_joueurs = input("Veuillez saisir le nombre de joueurs svp :  (maximum " + str(nb_max_joueurs) + ")" ).lstrip()
        nombre_de_joueurs = int(nombre_de_joueurs)
        if nombre_de_joueurs > nb_max_joueurs :
            print("Veuillez saisir un nombre inférieur ou égal à " + str(nb_max_joueurs))     
        else : 
            break 
          
    # Saisir les noms des joueurs  
    for i in range(0,nombre_de_joueurs) : 
        nom_du_joueur = input("Veuillez saisir le nom du joueur " + str(i+1)+":").lstrip().upper()
        circle= plt.Circle((0,0), radius =10)
        circle.set_edgecolor('black')
        circle.set_facecolor(couleurs_jetons[i])
        
        ax = plt.gca()
        ax.add_artist(circle)
        
        joueur = {"nom" : nom_du_joueur , 
                            "token position" : 0 ,
                            "score" : 0 ,
                            "token" : circle}
        liste_joueurs.append(joueur)
        positionner_pion(joueur)
    
        
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

            
#Cette fonction sert à afficher le pion du joueur donné à sa postion courante
def positionner_pion(joueur) : 
    global R, NbCases
    pos = joueur['token position']
    x = R * math.cos(math.pi+NbCases*pos/(2*math.pi)) + R
    y = R * math.sin(math.pi+NbCases*pos/(2*math.pi)) + R
    circle = joueur['token']
    circle.center = x , y ;
            
 
    
jeu()












