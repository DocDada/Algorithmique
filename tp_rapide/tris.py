#!/usr/bin/python
#coding:utf-8
# Algorithmique S3
# TP 1
# Implementation d'algorithmes de tri

import random

################################################################################

def tri_rapide(tab, gauche, droite, r):
    cp = cp2 = cp3 = 0
    if droite - gauche > r:
        tab, k, cp = placer(tab, gauche, droite)
        tab, cp2 = tri_rapide(tab, gauche, k - 1, r)
        tab, cp3 = tri_rapide(tab, k + 1, droite, r)
    return tab, (cp + cp2 + cp3)

def placer(tab, gauche, droite):
    cp = 0
    bas = gauche + 1
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
        cp += 2
    tab[gauche], tab[haut] = tab[haut], tab[gauche]
    return tab, haut, cp

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

    tab = ajout_sentinelle(sentinelle_gauche, sentinelle_droite)
    if not sentinelle_gauche and sentinelle_droite:
        return tab, taille
    return tab

def ajout_sentinelle(tab, s_gauche, s_droite):
    """ajoute les sentinelles"""
    if s_gauche:
        tab[0] = min(tab) - 1
    if s_droite:
        tab[len(tab) - 1] = max(tab) + 1
    return tab

def ajout_sentinelle2(tab, s_gauche, s_droite):
    """ajoute les sentinelles"""
    if s_gauche:
        tab.insert(0, min(tab) - 1)
    if s_droite:
        tab.append(max(tab) + 1)
    return tab

def tableau_aleatoire(n):
    """renvoie de taille n, dont les elements sont aleatoires"""
    if n <= 0:# gestion des exceptions
        return []
    tab = [0] * n
    for e in range(n - 1):
        tab[e] = random.randint(-5000, 5000)
    return tab

def comparaisons_cles(n, p, tri_rap):
    """taille de tableau n, nombre de tableaux p renvoie le nombre moyen de
    comparaisons des tris des tableaux aleatoires"""
    cp = cpbis = 0
    for t in range(p):
        tab = tableau_aleatoire(n)
        if tri_rap:
            tab = ajout_sentinelle(tab, False, True)
            tab, cpbis = tri_rapide(tab, 0, n - 1, 0)
        else:
            tab = ajout_sentinelle(tab, True, False)
            tab, cpbis = tri_insertion(tab)
        cp += cpbis
    return cp / p

def ecrire_comparaisons_fichier(nom_fichier, tri):
    f = open(nom_fichier, 'w')
    r = 20
    for t in range(10, 500):
        tab = tableau_aleatoire(t)
        tab = ajout_sentinelle(tab, False, True)
        if tri == 'i':
            tab, cpbis = tri_insertion(tab)
        if tri == 'r':
            tab, cpbis = tri_rapide(tab, 0, t - 1, 0)
        if tri == 'h':
            tab, cpbis = tri_hybride(tab, 0, t - 1, r)
        f.write(str(t) + ' ' + str(cpbis) + '\n')
    f.close()

def tri_insertion(tab):
    """effectue le tri par insertion sur un tableau tableau rajoute une
    sentinelle en T[0] renvoie le tableau trie"""
    cp = 0
    for i in range(2, len(tab)):
        j = i - 1
        x = tab[i]
        while j > 1 and tab[j] > x:
            cp += 1
            tab[j + 1] = tab[j]
            j -= 1
        cp += 1
        tab[j + 1] = x
    return tab, cp

def tri_hybride(tab, gauche, droite, r):
    """tri rapide de sous tableaux de taille r au plus, dont les elements
    doivent etre inferieurs aux elements du sous tableau suivant le tableau
    intermediaire est ensuite trie par insertion"""
    cp = cp2 = 0
    if r <= 0:
        return tab
    tab, cp = tri_rapide(tab, gauche, droite, r)
    tab, cp2 = tri_insertion(tab)
    return tab, (cp + cp2)

def comparaisons_cles_tri_hybride(n, p, r):
    """taille de tableau n, nombre de tableaux p; renvoie le nombre moyen de
    comparaisons des tris des tableaux aleatoires"""
    cp = cpbis = 0
    for t in range(p):
        tab = tableau_aleatoire(n)
        tab = ajout_sentinelle(tab, True, True)
        tab, cpbis = tri_hybride(tab, 0, n - 1, r)
        cp += cpbis
    return cp / p

##########################
#          MAIN          #
##########################

def main():
    #tab, taille = saisie_tableau(False, True)
    #tab, cp = tri_rapide(tab, 0, taille - 1, 0)
    #print tab, cp
    print "TRI RAPIDE"
    print comparaisons_cles(10, 10, True)#33
    print comparaisons_cles(100, 10, True)#750
    print comparaisons_cles(500, 50, True)#5600
    print comparaisons_cles(1000, 50, True)#12700
    #tab2, cp = tri_insertion(saisie_tableau(True, False))
    #print tab2, cp
    print "TRI INSERTION"
    print comparaisons_cles(10, 10, False)#10
    print comparaisons_cles(100, 10, False)#2300
    print comparaisons_cles(500, 50, False)#61300
    print comparaisons_cles(1000, 50, False)#248000
    """
    tab3 = saisie_tableau(True, True)
    tab3, cp = tri_hybride(tab3, 0, len(tab3) - 1, 3)
    print tab3, cp"""
    print "TRI HYBRIDE"
    """
    print comparaisons_cles_tri_hybride(50, 10, 3)#38
    print comparaisons_cles_tri_hybride(50, 10, 3)#800
    print comparaisons_cles_tri_hybride(50, 50, 50)#7000
    print comparaisons_cles_tri_hybride(50, 50, 50)#14000
    """

    print comparaisons_cles_tri_hybride(10, 10, 3)#38
    print comparaisons_cles_tri_hybride(100, 10, 3)#800
    print comparaisons_cles_tri_hybride(500, 50, 50)#7000
    print comparaisons_cles_tri_hybride(1000, 50, 50)#14000
    print comparaisons_cles_tri_hybride(500, 50, 5)#5800
    print comparaisons_cles_tri_hybride(1000, 50, 5)#15400
    print comparaisons_cles_tri_hybride(5000, 50, 5)#15400

    print "CHANGEMENT DE R"
    # plus R (taille des sous tableaux) augmente, plus le nombre de comparaisons
    # augmente
    print comparaisons_cles_tri_hybride(20000, 50, 2)#390000
    print comparaisons_cles_tri_hybride(20000, 50, 4)#370000
    print comparaisons_cles_tri_hybride(20000, 50, 8)#370000#
    print comparaisons_cles_tri_hybride(20000, 50, 16)#370000
    print comparaisons_cles_tri_hybride(20000, 50, 32)#400000
    print comparaisons_cles_tri_hybride(20000, 50, 64)#480000
    print comparaisons_cles_tri_hybride(20000, 50, 128)#670000
    print comparaisons_cles_tri_hybride(20000, 50, 256)#1000000
    print "CHANGEMENT DE N"
    # plus N (taille du tableau) est petit, plus le nombre de comparaisons
    # est petit
    print comparaisons_cles_tri_hybride(10, 50, 8)#30
    print comparaisons_cles_tri_hybride(100, 50, 8)#800
    print comparaisons_cles_tri_hybride(1000, 50, 8)#12000
    print comparaisons_cles_tri_hybride(10000, 50, 8)#175000
    print comparaisons_cles_tri_hybride(100000, 50, 8)#2200000
    # R depend t elle de la valeur de N ?
    print "CHANGEMENT DE R pour un N different"
    print comparaisons_cles_tri_hybride(100, 50, 2)#888
    print comparaisons_cles_tri_hybride(100, 50, 5)#850
    print comparaisons_cles_tri_hybride(100, 50, 10)#823#
    print comparaisons_cles_tri_hybride(100, 50, 20)#882
    print comparaisons_cles_tri_hybride(100, 50, 30)#970
    print comparaisons_cles_tri_hybride(100, 50, 40)#
    print comparaisons_cles_tri_hybride(100, 50, 50)#

    # La valeur de R pour laquelle on obtient un nombre de comparaisons minimal
    # pas en fonction de N (autour de 10)

    #tab = [0,5,12,1,9999]
    #tab, cp = tri_rapide(tab, 0, 4, 0)
    #tab = [0,5,12,1,9999]
    #tab, cp = tri_rapide(tab, 0, 4, 0)
    #print tab, cp

def main2():
    ecrire_comparaisons_fichier("compi.txt", 'i')
    ecrire_comparaisons_fichier("compr.txt", 'r')
    ecrire_comparaisons_fichier("comph.txt", 'h')

def nombre_comp_moy_tris_rap_hyb(n, p, d, f):
    cp = cp2 = 0
    for i in range(d, f):
        cp += comparaisons_cles(n, p, True)#61300

    for i in range(d, f):
        cp2 += comparaisons_cles_tri_hybride(n, p, i)#38
    cp2 = cp2 / (f - d + 1)
    cp = cp / (f - d + 1)
    print "hybride : ", cp2
    print "rapide : ", cp
    print "rapport hybride / rapide : ", float(cp2) / cp

################################################################################

#main()
#main2()
nombre_comp_moy_tris_rap_hyb(1000, 10, 2, 10)
nombre_comp_moy_tris_rap_hyb(1000, 10, 20, 50)
