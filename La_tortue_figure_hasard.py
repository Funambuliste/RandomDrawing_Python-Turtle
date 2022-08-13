import turtle
import random
from math import gcd # fonction du module math qui calcule le pgcd de 2 nombres

def figure () :
    #""" l'utilisateur peut choisir le type de forme désirée : polygone, étoile, spirale ou cercle."""
    choix = input ("P pour polygone, E pour étoile, S pour spirale, C pour cercle ? ",)
    choix = choix.upper ()
    if choix == "P" :
        polygone_turtle ()
    elif choix == "E" :
        star ()
    elif choix == "S" :
        spirale () 
    elif choix == "C" :
        pass
    else :
        print ("désolé pas en stock")
        
def coordonnees () :
    #"""fonction déterminant aléatoirement la position de la forme. La forme du curseur est aussi indiquée."""
    coord_x = random.randint (-200, 200)
    coord_y = random.randint (-200, 200)
    turtle.shape("turtle")
    turtle.up()
    turtle.goto (coord_x, coord_y)
    turtle.down()
    
def couleur_choix () :
    #"""fonction déterminant aléatoirement la couleur de la forme."""
    couleur_int = random.randint (1,10)
    if couleur_int == 1 :
        couleur = "black"
    elif couleur_int == 2 :
        couleur = "blue"
    elif couleur_int == 3 :
        couleur = "red"
    elif couleur_int == 4 :
        couleur = "green"
    elif couleur_int == 5 :
        couleur = "yellow"
    elif couleur_int == 6 :
        couleur = "orange"
    elif couleur_int == 7 :
        couleur = "pink"
    elif couleur_int == 8 :
        couleur = "grey"
    elif couleur_int == 9 :
        couleur = "purple"
    elif couleur_int == 10 :
        couleur = "brown"     
    turtle.color (couleur)
  

def polygone_turtle () :
    #""" fonction permettant de tracé un polygone régulier aléatoire."""
    nbre_cote = random.randint (3, 10)
    rayon = random.randint (10,200)
    angle = 360 / nbre_cote #calcul de l'angle
    turtle.begin_fill()
    for i in range (1, nbre_cote+1) :
        turtle.forward (rayon)
        turtle.left(angle)
        i=i+1
    turtle.end_fill()

def star () :
    #""" fonction permettant de tracé une étoile aléatoire."""
    nombre_de_branches = random.randint (5, 20)
    longueur = random.randint (10, 200)
    inc = (nombre_de_branches-1) // 2
    turtle.begin_fill()
    if nombre_de_branches % 2 != 0 :
        for b in range (nombre_de_branches) :
            turtle.forward (longueur)
            turtle. left ((nombre_de_branches-1)*(180/nombre_de_branches))
            b +=1
    elif nombre_de_branches % 2 == 0 :
        while gcd(nombre_de_branches, inc) > 1:
            inc = inc - 1
        if inc == 1 :
            print("Impossible de dessiner une étoile à", nombre_de_branches, "branches en un tenant")
        else:
            angle =  180 - (nombre_de_branches - 2 * inc) * 180 / nombre_de_branches
            for i in range(nombre_de_branches):
                turtle.forward(longueur)
                turtle.left(angle)
                i += 1
    turtle.end_fill()
    
def spirale () :
    #""" fonction permettant de tracé une spirale aléatoire."""
    tour = random.randint (4, 50)
    largeur = random.randint (1, 10)
    for i in range(tour) :
        turtle.circle (i*(largeur/2), -90)
    turtle.done
   
#""" code d'appel des fonctions qui permet à l'utilisateur de déterminer combien de formes il souhaite voir apparaître.
# Si le nombre est supérieur à 10, il est automatiquement réduit."""                
dessin = int(input ("Combien de formes voulez-vous ?",))
while dessin > 10 :
    print ("C'est trop ! On va réduire.")
    dessin = dessin %10
if 0 < dessin <=10 :
    for j in range (1, dessin+1) :
        coordonnees ()
        couleur_choix ()
        figure ()
        dessin +=1

