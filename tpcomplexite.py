#coding: utf-8

import time
import math

## VARIABLES GLOBALES #########################################################

N = 100 #nb de repetitions
UNITE = 1000000  #pour avoir les resultats en micro-secondes

## FONCTION POUR ECRIRE UN TABLEAU DANS UN FICHIER #############################

def ecrire_tableau_dans_fichier(tab, nomfichier):
    """écrit dans le fichier donné (chaîne de caractères !)
    les éléments du tableau, un élément par ligne si c'est un nombre
    ou séparés par des espaces si c'est un tableau de nombres
    Vous n'êtes pas censés maîtriser cette partie"""
    f= open(nomfichier, 'w')
    for e in tab:
        if type(e)==list or type(e)==tuple:
            for x in e:
                f.write(str(x)+' '*(20-len(str(x))))
            f.write('\n')
        else:
            f.write(str(e) + '\n')
    f.close()

## ACCES AUX ELEMENTS D'UN TABLEAU #############################################

def acces_tableau_mesure(i,n):
    """Définit un tableau de n zéros et renvoie le temps
    nécessaire pour changer l'element d'indice i en 1
    """

    duree = 0   #variable qui va contenir la duree

    tab = [0]*n

    #ici commence la mesure
    debut = time.time()            #'heure' de départ en secondes
    tab[i] =1
    duree += time.time() - debut   #temps ecoulé en secondes

    return duree * UNITE

def acces_tableau_experience():
    """expérience de mesure du temps nécessaire à l'acces
    aux indices dans un tableau de taille n
    L'expérience est répétée N fois
    """

    n = 100000
    step = 5000

    #valeurs que prendra i pour le graphique
    valeurs_i = range(0,n,step)

    #dictionnaire qui va pour chaque indice stocker
    #les résultats de acces_tableau_mesure
    mesures = {}
    for i in valeurs_i:
        mesures[i] = 0

    ancienpourcent = -1 #voir ci-dessous

    for repet in range(N):

        #on affiche le pourcentage de l'experience ecoulée au fur et
        #à mesure. Permet de se rendre compte si c'est trop long.
        #(si c'est trop long changer N,n ou step)
        pourcent = int(float(repet)/N*100)
        if pourcent > ancienpourcent:
            print pourcent,"%"
            ancienpourcent = pourcent


        #appel de la fonction de mesure et on somme les résultats
    #    for i in valeurs_i:
    #        mesures[i] +=  acces_tableau_mesure(i,n)
        
    #    for i in valeurs_i:
    #        mesures[i] +=  acces_dico_mesure(i,n)
        for i in valeurs_i:
            mesures[i] += acces_tab_et_dico_experience(i,n)
    
    #à la fin des N répétitions on divise par N pour obtenir
    #le temps moyen
    for i in valeurs_i:
        mesures[i] /= N

    #on utilise la fonction ecrire_tableau_dans_fichier
    #pour produire un fichier des résultats
    resultats = [ [i,mesures[i]] for i in range(0,n,step)]
    ecrire_tableau_dans_fichier(resultats, "acces_tabdico.txt")


## A VOUS ######################################################################

def acces_dico_mesure(i,n):
    dico={}
    for j in range(n):
        dico[j]=0
    duree = 0   #variable qui va contenir la duree
    #ici commence la mesure
    debut = time.time()            #'heure' de départ en secondes
    dico[i] =1
    duree += time.time() - debut   #temps ecoulé en secondes
    return duree * UNITE




def acces_tab_et_dico_experience(i,n):
    dico={}
    tab = [0]*n
    for j in range(n):
        dico[j]=0
    Tab=[[0]*3]*i

    duree = 0   #variable qui va contenir la duree
    #ici commence la mesure
    debut = time.time()            #'heure' de départ en secondes
    dico[i] =1
    duree += time.time() - debut   #temps ecoulé en secondes
    duree=duree * UNITE
    Tab[i][1]=duree

    duree = 0   #variable qui va contenir la duree
    #ici commence la mesure
    debut = time.time()            #'heure' de départ en secondes
    tab[i] =1
    duree += time.time() - debut   #temps ecoulé en secondes
    duree=duree * UNITE
    Tab[i][2]=duree


## PROG PRINCIPAL ("MAIN") ####################################################

acces_tableau_experience()
