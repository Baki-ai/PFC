from random import randint 

jeu = ["pierre", "papier", "ciseaux"]
ordinateur = jeu[randint(0,2)]

Pointjoueur = 0
Pointordinateur= 0

continuer  = True

while (continuer):
    joueur = input ("pierre , papier , ciseaux ? ou Fin pour terminer le jeu\n")

    if( joueur == 'Fin'):
        continuer = False 
    elif (joueur == ordinateur ):
        print("Egalité , Recommencer !")
    elif (joueur == "pierre"):
        if(ordinateur == "papier"):
            print("Perdu" , ordinateur , "recouvre", joueur )
            Pointordinateur = Pointordinateur + 1
        else:
            print("Victoire" , joueur, "ecrase" , ordinateur)
            PointJoueur = Pointjoueur + 1
    elif (joueur == "papier"):
        if (ordinateur == "ciseaux"):
            print ("Defaite !" , ordinateur , "coupe", joueur)
            Pointordinateur = Pointordinateur + 1 
        else:
            print ("Victory" , joueur , "recouvre", ordinateur )
            PointJoueur = Pointjoueur + 1
    elif (joueur == "ciseaux"):
        if (ordinateur == "pierre"):
            print ("Defaite !" , ordinateur , "detruit", joueur)
            Pointordinateur = Pointordinateur + 1 
        else:
            print ("Victory" , joueur , "slash", ordinateur )
            PointJoueur = Pointjoueur + 1 
    else:
        print ("Votre choix n'est pas correct , recommencer ")
    ordinateur = jeu[randint(0 , 2)]
    print ("****Tour suivant****")

print ("***Point***")
print ("joueur :"  , Pointjoueur)
print ("ordinateur:", Pointordinateur )




