from tkinter import *

cases = [ [0,0,0],
          [0,0,0],
          [0,0,0]]
drapeau=True
n = 1

def afficher(event):
    """Entrée : le clique effectuer par la souris
    Sortie : Affiche en temps réel les coordonnées sur lesquels l'utilisateur clique"""
   
    global drapeau,cases,n
    l = (event.y-2)//100
    c = (event.x-2)//100

    if (n < 10) and (cases[l][c] == 0):
        if drapeau:
            dessin.create_line(100*c+8,100*l+8,100*c+96,100*l+96,width=5,fill = 'blue')
            dessin.create_line(100*c+8,100*l+96,100*c+96,100*l+8,width=5,fill='blue')
            cases[l][c] = 1
            message.configure(text="les ronds à l'attaque")

        else:
            dessin.create_oval(100*c+8,100*l+8,100*c+96,100*l+96,width=5,outline = 'red')
            cases[l][c] = -1
            message.configure(text="Les croixs à l'attaque")

        
        drapeau = not(drapeau)
            
        if (n >= 5) and (n <= 9):
            somme = verif(cases)
            if somme == 1 or somme == -1:
                n = gagner(somme)
            elif n == 9:
                n = gagner(0)
        n += 1

def verif(tableau):
    """ Entrées : un tbleau "carré"
        Sorties : Calcule les sommes de chaque ligne/colonne/diago """
    sommes=[0,0,0,0,0,0,0,0]
    #Les lignes
    sommes[0] = sum(tableau[0])
    sommes[1] = sum(tableau[1])
    sommes[2] = sum(tableau[2])
    #les colonnes
    sommes[3] = tableau[0][0] + tableau[1][0] + tableau[2][0]
    sommes[4] = tableau[0][1] + tableau[1][1] + tableau[2][1]
    sommes[5] = tableau[0][2] + tableau[1][2] + tableau[2][2]
    #les diagonales
    sommes[6] = tableau[0][0] + tableau[1][1] + tableau[2][2]
    sommes[7] = tableau[0][2] + tableau[1][1] + tableau[2][0]

    for i in range(8):
        if sommes[i] == 3:
            return 1 # Trois croix sont alignées
        elif sommes[i] == -3:
            return -1 #Trois ronds sont alignés
    return 0


def gagner(a):
    if a == 1:
        message.configure(text="Les croixs ont gagné !")
    elif a == -1:
        message.configure(text="Les ronds ont gagné !")
    elif a == 0:
        message.configure(text="C'est un match nul !")
    return 9



def reinit():
    global drapeau,cases,n
    cases = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    
    drapeau = True
    n = 1 

    message.configure(text="Les croix à l'attaque")
    dessin.delete(ALL)
    lignes = []
    for i in range(4):
        lignes.append(dessin.create_line(0,100*i+2,303,100*i+2,width=3))
        lignes.append(dessin.create_line(100*i+2,0,100*i+2,303,width=3))


fen=Tk()
fen.title=('Morpion')

message=Label(fen,text="Au croix de jouer")
message.grid(row=0,column=0,columnspan=2,padx=3,pady=3,sticky=W+E)

button_quitter = Button(fen,text="Quitter",command=fen.destroy)
button_quitter.grid(row=2,column=1,padx=3,pady=3,sticky=S+W+E)

button_recommencer = Button(fen,text="Recommencer",command=reinit)
button_recommencer.grid(row=2,column=0,padx=3,pady=3,sticky=S+W+E)

dessin = Canvas(fen,bg='white',width=301,height=301)
dessin.grid(row=1,column=0,columnspan=2,padx=5,pady=5)

lignes=[]

dessin.bind('<Button-1>',afficher)

reinit()
fen.mainloop()

