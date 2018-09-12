#!/usr/bin/python
# Algorithmique S3
# TP 1
# Implementation d'algorithmes de tri

import random

def tri_rapide(tab, gauche, droite, r):
    cp = 0
    cp2 = 0
    cp3 = 0
    if droite - gauche > r:
        tab, k, cp = placer(tab, gauche, droite)
        tab, cp2 = tri_rapide(tab, gauche, k-1, r)
        tab, cp3 = tri_rapide(tab, k+1, droite, r)
    return tab, (cp + cp2 + cp3)

def placer(tab, gauche, droite):
    cp = 0
    bas = gauche +1
    haut = droite
    while bas <= haut:
        while tab[bas] <= tab[gauche]:
            cp += 1
            bas = bas + 1
        while tab[haut] > tab[gauche]:
            cp += 1
            haut = haut - 1
        if bas < haut:
            tab[bas], tab[haut] = tab[haut], tab[bas]
            bas = bas + 1
            haut = haut - 1
    tab[gauche], tab[haut] = tab[haut], tab[gauche]
    k = haut
    return tab, k, cp

def saisie_tableau(sentinelle_gauche, sentinelle_droite):
    """demande a l'utilisateur d'entrer la taille d'un tableau, et ses
    elements"""
    taille = input("Entrez la taille du tableau : ")
    tab = [0] * taille
    if sentinelle_gauche and sentinelle_droite:
        fin = taille - 1
        debut = 1
    if sentinelle_droite:
        fin = taille - 1
        debut = 0
    if sentinelle_gauche:
        fin = taille
        debut = 1
    for e in range(debut, fin):
        tab[e] = input("Entrez une valeur : ")

    if sentinelle_gauche and sentinelle_droite:
        tab[len(tab) - 1] = max(tab) + 1# ajout de la sentinelle
        tab[0] = min(tab) - 1# sentinelle en T[0]
        return tab
    if sentinelle_droite:
        tab[len(tab) - 1] = max(tab) + 1# ajout de la sentinelle
        return tab, taille
    else:
        tab[0] = min(tab) - 1# sentinelle en T[0]
    return tab

def tableau_aleatoire(n):
    """renvoie de taille n, dont les elements sont aleatoires"""
    if n <= 0:
        return []
    tab = [None] * n
    for e in range(n - 1):
        tab[e] = random.randint(-5000, 5000)
    tab[n - 1] = max(tab) + 1# ajout de la sentinelle
    return tab

def comparaisons_cles(n, p, tri_rap):
    """taille de tableau n, nombre de tableaux p
    renvoie le nombre moyen de comparaisons des tris des tableaux aleatoires"""
    cp = 0
    cpbis = 0
    for t in range(p):
        tab = tableau_aleatoire(n)
        if tri_rap:
            tab, cpbis = tri_rapide(tab, 0, n - 1, 0)
        else:
            tab, cpbis = tri_insertion(tab)
        cp += cpbis
    return cp/p

def tri_insertion(tab):
    """effectue le tri par insertion sur un tableau tableau
    rajoute une sentinelle en T[0]
    renvoie le tableau trie"""
    cp = 0
    for i in range(2, len(tab)):
        j = i - 1
        x = tab[i]
        while j > 1 and tab[j] > x:
            cp += 1
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = x
    return tab, cp

def tri_hybride(tab, gauche, droite, r):
    """tri rapide de sous tableaux de taille r au plus, dont les elements
    doivent etre inferieurs aux elements du sous tableau suivant
    le tableau intermediaire est ensuite trie par insertion
    """
    cp = 0
    cp2 = 0
    if r <= 0:
        return tab
    tab, cp = tri_rapide(tab, gauche, droite, r)
    tab, cp2 = tri_insertion(tab)
    return tab, (cp + cp2)

def comparaisons_cles_tri_hybride(n, p, r):
    """taille de tableau n, nombre de tableaux p
    renvoie le nombre moyen de comparaisons des tris des tableaux aleatoires"""
    cp = 0
    cpbis = 0
    for t in range(p):
        tab = tableau_aleatoire(n)
        tab, cpbis = tri_hybride(tab, 0, n - 1, r)
        cp += cpbis
    return cp/p

##########################
#          MAIN          #
##########################

def main():
    #tab, taille = saisie_tableau(False, True)
    #tab, cp = tri_rapide(tab, 0, taille - 1, 0)
    #print tab, cp
    
    print comparaisons_cles(10, 10, True)#15
    print comparaisons_cles(100, 10, True)#430
    print comparaisons_cles(500, 50, True)#3300
    print comparaisons_cles(1000, 50, True)#7500
    #tab2, cp = tri_insertion(saisie_tableau(True, False))
    #print tab2, cp
    print comparaisons_cles(10, 10, False)#10
    print comparaisons_cles(100, 10, False)#2300
    print comparaisons_cles(500, 50, False)#61300
    print comparaisons_cles(1000, 50, False)#248000
    """
    tab3 = saisie_tableau(True, True)
    tab3, cp = tri_hybride(tab3, 0, len(tab3) - 1, 3)
    print tab3, cp"""
    print comparaisons_cles_tri_hybride(10, 10, 3)#15
    print comparaisons_cles_tri_hybride(100, 10, 3)#430
    print comparaisons_cles_tri_hybride(500, 50, 50)#5600
    print comparaisons_cles_tri_hybride(1000, 50, 50)#12500
    print comparaisons_cles_tri_hybride(500, 50, 5)#3100
    print comparaisons_cles_tri_hybride(1000, 50, 5)#7400

##########################

main()


