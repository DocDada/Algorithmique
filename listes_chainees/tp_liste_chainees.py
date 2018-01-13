#coding:utf-8
from listes_base import *
import os
os.system('clear')

#ALGORITHMIQUE

#TP - Listes chainées

l = constructionClavier()
affichageIteratif(l)

#Question 0

def longueurListeIterative(l):
    """renvoie la longueur d'une liste chainée (iterative) """
    compteur = 0
    courant = l.premier
    while courant :# <==> while courant != None :
        compteur += 1
        courant = courant.suivant
    return compteur
#print "Question 0 : (itératif) ", longueurListeIterative(l)

def longueurListeRecursive_p(l):
    """fait appel à la fonction auxiliaire"""
    if l.premier:
        return longueurListeRecursive(l.premier)
    else:
        return 0

m = l.premier
def longueurListeRecursive(m):
    """renvoie la longueur d'une liste chainée (recursive) """
    if m:
        return 1 + longueurListeRecursive(m.suivant)
    else:
        return 0
#print "Question 0 : (récursif) ", longueurListeRecursive_p(l)

#Question 1



#Question 2

def recherche_It(l, k):
    """renvoit la valeur de l'élément qui est dans la k-ième case d'une liste
    EXCEPTION : la liste peut avoir moins de k éléments"""
    compteur = 0
    courant = l.premier
    while compteur != k :
        if courant == None:
            raise Exception("La position saisie est trop grande")
        courant = courant.suivant
        compteur += 1
    return courant.valeur
#print "Question 2 : (itératif) ", recherche_It(l, 1)

#Correction question 2 (itératif)
"""def valeur_It(l, k):
    courant = l.premier
    for i in range(k):
        if courant.suivant == None:
            raise Exception("AAAAAAAAAAAAAAAAAAAAAAAAAA")
        else:
            courant = courant.suivant
    return courant.valeur
print "Correction question 2 : (itératif)", valeur_It(l, 1)"""

def recherche_Re_p(l, k):
    """appel un maillon si non vide"""
    if l.premier and k>=0 :
        return recherche_Re(l.premier, k)
    else:
        return "Position saisie trop grande"

def recherche_Re(m, k):
    """renvoit la valeur de l'élément qui est dans la k-ième case d'une liste
    EXCEPTION : la liste peut avoir moins de k éléments"""
    if k == 0:
        return m.valeur
    elif m.suivant == None :
        raise Exception("La position saisie est trop grande")
    else:
        return recherche_Re(m.suivant, k - 1)
#print "Question 2 : (récursif) ", recherche_Re_p(l, 1)

#Correction question 2 (récursif)

def valeur_rec(l, k):
    """renvoie la kième valeur de la liste chaînée"""
    if l.premier:
        return valeur_rec_M(l.premier, k)
    else:
        raise Exception("liste vide")

def valeur_rec_M(m, k):
    """renvoie la valeur du kième élément après m (k=0 donne la valeur de m)
    m ne doit pas être None"""
    if k==0:
        return m.valeur
    else:
        if m.suivant:
            return valeur_rec_M(m, k-1)
        else:
            raise Exception("liste trop courte")
#print "Correction question 2 : (récursif) ", valeur_rec(l, 1)


#Question 3

def rechercheElementDistinctIteratif(l, k):
    #marche?
    """recherche du k-ième élément distinct
    dans une liste chaînée (version itérative) """
    courant=l.premier
    compteur = 1# compteur = 0 pour une liste qui par de 0
    if courant != None:
        courantSuiv=courant.suivant
    else:
        raise Exception("La liste chainee est vide")
    while compteur != k and courantSuiv != None:
        while courant.valeur == courantSuiv.valeur:
            courantSuiv = courantSuiv.suivant
        courant = courantSuiv
        courantSuiv = courant.suivant
        compteur += 1
    return courant.valeur
#print "Question 3 : (itératif) ", rechercheElementDistinctIteratif(l, 1)


# identique à la correction
def recherche_element_distinct_Re_p(l, k):
    """recherche du k-ième élément distinct dans
    une liste chaînée (récursif)"""
    if l.premier and k>=1 :# k>=0 pour une liste qui commence à 0
        return recherche_element_distinct_Re(l.premier, k)
    else:
        raise Exception("La liste est vide")

def recherche_element_distinct_Re(m, k):
    """fonction auxiliaire"""
    courant = m.suivant
    if k==1:# k==0 pour une liste qui part de 0
        return m.valeur
    elif courant != None:
        if courant.valeur == m.valeur:
            return recherche_element_distinct_Re(courant, k)
        else:
            return recherche_element_distinct_Re(courant, k-1)
    else:
        raise Exception("La valeur saisie est trop grande !")
#print "Question 3 : (récursif) ", recherche_element_distinct_Re_p(l, 1)




#Correction question 3

def kiemedistinct_it(maliste, k):
    """fonction qui renvoi la kième valeur différente
    qui est dans la liste chaînée maliste"""
    if not maliste.premier:
        raise Exception("Liste trop courte")

    courant = maliste.premier
    compteur = 1# la liste part de 1 !!!!

    while courant.suivant and compteur < k:
        if courant.valeur < courant.suivant.valeur:
            compteur += 1
    if compteur == k:
        return courant.valeur
    else:
        raise Exception("Liste trop courte")
        courant = courant.suivant

#print "Correction question 3 : (itératif) ", kiemedistinct_it(l, 1)




#Question 4

def xElementDeLaListe_It(l, x):
    """renvoit True si l'élément x est dans la liste l (version itérative) """
    courant = l.premier
    while courant:
        if int(courant.valeur) == int(x):
            return True
        courant=courant.suivant
    return False# l'élément x n'est pas dans la liste

#print "Question 4 : (itératif) ", xElementDeLaListe_It(l, 1)

def xElementDeLaListe_Re_p(l, x):
    """renvoit True si l'élément x est dans la liste l (version récursive) """
    if l.premier:
        return xElementDeLaListe_Re(l.premier, x)
    else:
        return False

def xElementDeLaListe_Re(m, x):
    """fonction auxiliaire"""
    if int(m.valeur) == int(x):
        return True
    elif m.suivant:
        return xElementDeLaListe_Re(m.suivant, x)
    else:
        return False
#print "Question 4 : (récursif) ", xElementDeLaListe_Re_p(l, 1)



        ############
        #Question 5#
        ############

def xElementListeTriee_It(l, x):
    """recherche un element x dans une liste croissante/triée
    (version itérative)"""
    if l.premier:
        courant=l.premier
    else:
        return False
    while courant != None:
        if int(x) > int(courant.valeur):
            return False
        elif int(x)==int(courant.valeur):
           return True
        courant = courant.suivant
    return False
#print "Question 5 : (itératif) ", xElementListeTriee_It(l, 1)

def xElementListeTriee_Re_p(l, x):
    """regarde si la liste l est vide, si non recherche de x dans liste"""
    if l.premier:
        return xElementListeTriee_Re(l.premier, x)
    else:
        return False

def xElementListeTriee_Re(m, x):
    """si x> m.valeur, alors x pas dans la liste, sinon appel à partir de
    m.suivant"""
    if int(x) > int(m.valeur):
        return False
    elif int(x)==int(m.valeur):
        return True
    elif m.suivant:
        xElementListeTriee_Re(m.suivant, x)
    else:
        return False
#print "Question 5 : (récursif) ", xElementListeTriee_Re_p(l, 1)




        ############
        #Question 6#
        ############

#marche
#propre
def nbrElementDistinct_It(l):
    """compte le nombre d'éléments distinct
    dans une liste triée (version itérative)"""
    courant=l.premier
    compteur=0
    if courant:
        while courant:
            courantSuiv = courant
            compteur += 1
            while courantSuiv != None and courant.valeur==courantSuiv.valeur:
                courantSuiv=courantSuiv.suivant
            courant=courantSuiv
    return compteur
#print "Question 6 : (itératif) ", nbrElementDistinct_It(l)


#Correction question 6 (versions itérative et récursive)




# marche
# propre
def nbrElementDistinct_Re_p(l):
    """compte le nombre d'éléments distinct
    dans une liste triée (version récursive)"""
    if l.premier:
        return nbrElementDistinct_Re(l.premier)
    else:
        return 0# la liste est vide

def nbrElementDistinct_Re(m):
    """fonction auxiliaire à nbrElementDistinct_Re_p
    renvoi le nombre de valeurs distinctes qui apparaissent
    à partir du maillon m"""
    if m.suivant:
        if m.valeur == m.suivant.valeur:
            return nbrElementDistinct_Re(m.suivant)
        else:
            return 1+nbrElementDistinct_Re(m.suivant)
    else:
        return 1
#print "Question 6 : (récursif) ", nbrElementDistinct_Re_p(l)



        ############
        #Question 7#
        ############

# marche presque
def copie_it(l):
    """renvoie une nouvelle liste chainee copiee"""

    copie = ListeChainee(None)
    if l.premier:
        # le cas du premier maillon est traité à part
        copie.premier = Maillon(l.premier.valeur, None)
        val_precedente = copie.premier.valeur

        courant_lecture = l.premier.suivant
        courant_ecriture = copie.premier
        while courant_lecture:# maillon à copier
            if courant_lecture.valeur > val_precedente:
                courant_ecriture.suivant = Maillon(courant_lecture.valeur, None)
                courant_lecture = courant_lecture.suivant
                courant_ecriture = courant_ecriture.suivant
            if courant_lecture:
                val_precedente = courant_lecture.suivant
                courant_lecture = courant_lecture.suivant
    return copie
print "Question 7 : (itératif) "
#copie = copie_it(l)
#affichageIteratif(copie)



# marche presque
# n'affiche la dernière valeur si aucune répétitions
def copie_re_p(l):
    """renvoie une copie de l en enlevant les répétitions"""
    copie = ListeChainee(None)
    if l.premier:
        copie.premier = copie_re(l.premier)
    return copie# retourne la liste dans tous les cas (vide ou pas)

def copie_re(m):
    """renvoie le premier maillon d'une chaine de maillons
    qui constituent une copie de la chaîne à partir de m"""
    if m.suivant:
        if m.valeur < m.suivant.valeur:
            return Maillon(m.valeur, copie_re(m.suivant))
        else:
            return copie_re(m.suivant)
    else:
        return Maillon(m.valeur, None)
print "Question 7 : (récursif) "
#copie2 = copie_re_p(l)
#affichageIteratif(copie)

#Correction question 7

def copie_rec(l):
    """renvoie une copie de la liste de l"""
    if l.premier:
        prems_copie = copie_rec_M(l.premier)
        return ListeChainee(prems_copie)
    else:
        return ListeChainee(None)

def copie_rec_M(m):
    """copie la chaine de maillons à partir de m
    renvoie le premier maillon de la copie
    m doit etre non None"""

    if m.suivant:
        copie_du_suivant = copie_rec_M(m.suivant)
        nouveau = Maillon(m.valeur, copie_du_suivant)
        return nouveau
    else:
        return Maillon(m.valeur, None)
print "Correction question 7 : (récursif) "
#copie = copie_rec(l)
#affichageIteratif(copie)



        ############
        #Question 8#
        ############

# marche
def supprRepetitions_It(l):
    """supprime les repetitions d'une liste l (version iterative)"""
    courant=l.premier
    while courant:# si la liste n'est pas vide
        if courant.suivant:# si le maillon suivant existe
            courantSuiv=courant.suivant
            while courantSuiv and courant.valeur == courantSuiv.valeur:
                # tant que le maillon au devant sera == à courant
                courantSuiv = courantSuiv.suivant
            courant.suivant = courantSuiv
        else:
            break
        courant = courant.suivant
    affichageIteratif(l)
print "Question 8 : (itératif) "
#supprRepetitions_It(l)

# marche
# propre
def supprRepetitions_re_l(l):
    """supprime les répétitions d'une liste l (version récursive)"""
    if l.premier:
        supprRepetitions_re(l.premier.valeur, l.premier)
        affichageIteratif(l)
    else:
        raise Exception("Liste vide")

def supprRepetitions_re(val, m):
    """si la valeur du maillon suivant est ==
    à celle du maillon courant (et que ce maillon
    suivant existe), alors on redirige le maillon actuel"""
    if m and m.valeur == val:
        m.suivant = supprRepetitions_re(val, m.suivant)
    elif m == None or m.valeur != val:# else
        return m
print "Question 8 : (récursif) "
#supprRepetitions_re_l(l)



        ############
        #Question 9#
        ############

# marche (2)
# propre (2)
def rangerEntier_it(l, entier):
    """range un entier dans une liste triée (version itérative)"""
    courant = l.premier
    if courant:
        while courant.suivant and (int(courant.suivant.valeur)<entier):
            courant = courant.suivant
        courant.suivant = Maillon(entier, courant.suivant)
    affichageIteratif(l)

entier = 5
print "Question 9 : (iteratif) | insertion de", entier
rangerEntier_it(l, entier)

def rangerEntier_re_l(l, entier):
    """range un entier dans une liste triée (version recursive)"""
    if l.premier and int(l.premier.valeur) < entier:
        rangerEntier_re(l.premier, entier)
    else:
        l.premier = Maillon(entier, l.premier)
    affichageIteratif(l)

def rangerEntier_re(m, entier):
    """si l'entier est supérieur au m.suivant.valeur
    ou que m.suivant est None, alors on l'implémente
    sinon, appel récursif sur m.suivant"""
    if m.suivant and int(m.suivant.valeur)<entier:
        rangerEntier_re(m.suivant, entier)
    else:
        m.suivant = Maillon(entier, m.suivant)

entier = 2
print "Question 9 : (récursif) | insertion de", entier
rangerEntier_re_l(l, entier)




        #############
        #Question 10#
        #############


# marche (2)
# propre (2)
def inverseElement_it(l):
    """inverse les éléments d'une liste chaînée
    par groupe de 2 (version itérative)"""
    cour = l.premier
    while cour and cour.suivant:
        cour.valeur, cour.suivant.valeur = cour.suivant.valeur, cour.valeur
        cour = cour.suivant.suivant
    affichageIteratif(l)
print "Question 10 : (itératif) "
inverseElement_it(l)


def inverseElement_re_l(l):
    """inverse les éléments d'une liste chaînée
    par groupe de 2 (version récursive)"""
    if l.premier:
        inverseElement_re(l.premier)
    affichageIteratif(l)

def inverseElement_re(m):
    """pour inverser, il faut une paire"""
    if m and m.suivant:
        m.valeur, m.suivant.valeur = m.suivant.valeur, m.valeur
        inverseElement_re(m.suivant.suivant)

print "Question 10 : (récursif) "
inverseElement_re_l(l)




        #############
        #Question 11#
        #############

# marche (2)
# propre (0)
def supprPremiereOccurence_it(l, entier):
    """supprime la premiere occurence d'un entier
    dans une liste chaînée (version itérative)"""
    courant = l.premier
    if courant and int(courant.valeur) == entier:
        l.premier = courant.suivant
    elif courant:
        while courant.suivant:
            if int(courant.suivant.valeur) == entier:
                courant.suivant = courant.suivant.suivant
                break
            courant = courant.suivant
    affichageIteratif(l)

entier = 1
print "Question 11 : (itératif) | on enleve la premiere occurence de", entier
#supprPremiereOccurence_it(l, entier)

def supprPremiereOccurence_re_l(l, entier):
    """supprime la premiere occurence d'un entier
    dans une liste chaînée (version récursive)"""
    if l.premier and int(l.premier.valeur) != entier:
        supprPremiereOccurence_re(l.premier, entier)
    elif l.premier and int(l.premier.valeur) == entier:
        l.premier = l.premier.suivant
    affichageIteratif(l)

def supprPremiereOccurence_re(m, entier):
    """si la valeur du maillon suivant est
    == à celle de l'entier, on raccorde
    sinon, appel du maillon suivant"""
    if m == None:
        return
    elif m.suivant and int(m.suivant.valeur) == entier:
        m.suivant = m.suivant.suivant
    else:
        supprPremiereOccurence_re(m.suivant, entier)

entier = 1
print "Question 11 : (récursif) | on enleve la premiere occurence de", entier
#supprPremiereOccurence_re_l(l, entier)





        #############
        #Question 12#
        #############


# marche (2)

def delFirstOcc_triee_it(l, entier):
    """supprime la premiere occurence d'un entier
    dans une liste chaînée >> triée << (version itérative)"""
    courant = l.premier
    if courant and int(courant.valeur) == entier:
        l.premier = l.premier.suivant
    elif courant:
        while courant.suivant and int(courant.suivant.valeur)<entier:
            courant = courant.suivant
        if courant.suivant.valeur == entier:
            courant.suivant = courant.suivant.suivant
    affichageIteratif(l)

entier = 2
print "Question 12 : (itérative) | on enleve la premiere occurence de", entier
delFirstOcc_triee_it(l, entier)


def delFirstOcc_triee_re_l(l, entier):
    """supprime la premiere occurence d'un entier
    dans une liste chaînée >> triée << (version récursive)"""
    if l.premier and int(l.premier.valeur) != entier:
        delFirstOcc_triee_re(l.premier, entier)
    elif l.premier and int(l.premier.valeur) == entier:
        l.premier = l.premier.suivant
    affichageIteratif(l)

def delFirstOcc_triee_re(m, entier):
    """si le maillon suivant est == à l'entier :
    raccorde, sinon appel maillon suivant
    si maillon suivant n'existe pas :
    ont arrête la fonction"""
    if m.suivant == None or int(m.suivant.valeur) > entier:
        return
    if int(m.suivant.valeur) == entier:
        m.suivant = m.suivant.suivant
    else:
        delFirstOcc_triee_re(m.suivant, entier)

entier = 7
print "Question 12 : (récursif) | on enleve la premiere occurence de", entier
delFirstOcc_triee_re_l(l, entier)








        #############
        #Question 13#
        #############

# marche (2)
def fusionCroissante_it(l1, l2):
    """réalise la fusion croissante de 2 listes
    création d'une 3me liste (version itérative)"""
    courant1 = l1.premier
    courant2 = l2.premier
    l = ListeChainee(None)
    if int(courant1.valeur) > int(courant2.valeur):
        l.premier = Maillon(courant2.valeur, None)
        courant2 = courant2.suivant
    else:
        l.premier = Maillon(courant1.valeur, None)
        courant1 = courant1.suivant
    courant = l.premier

    while courant1 != None and courant2 != None:
        if int(courant1.valeur) > int(courant2.valeur):
            courant.suivant = Maillon(courant2.valeur, None)
            courant2 = courant2.suivant
        else:
            courant.suivant = Maillon(courant1.valeur, None)
            courant1 = courant1.suivant
        courant = courant.suivant

    if courant1 == None:
        while courant2:
            courant.suivant = Maillon(courant2.valeur, None)
            courant = courant.suivant
            courant2 = courant2.suivant
    else:
        while courant1:
            courant.suivant = Maillon(courant1.valeur, None)
            courant = courant.suivant
            courant1 = courant1.suivant
    affichageIteratif(l)
    return l

l1 = constructionClavier()
l2 = constructionClavier()
print "Question 13 : (itératif) "
#l = fusionCroissante_it(l1, l2)


def fusionCroissante_re_l(l1, l2):
    """réalise la fusion croissante de 2 listes
    création d'une 3me liste (version itérative)"""
    if l1.premier and l2.premier:
        if int(l2.premier.valeur) > int(l1.premier.valeur):
            l.premier = Maillon(l1.premier.valeur,fusionCroissante_re(l1.premier.suivant, l2.premier))
        else:
            l.premier = Maillon(l2.premier.valeur,fusionCroissante_re(l1.premier, l2.premier.suivant))
        return l

def fusionCroissante_re(m1, m2):
    if m1 and m2:
        if int(m1.valeur) < int(m2.valeur):
            return Maillon(m1.valeur, fusionCroissante_re(m1.suivant,m2))
        else:
            return Maillon(m2.valeur, fusionCroissante_re(m1,m2.suivant))
    elif m1:
        if m1.suivant:
            return Maillon(m1.valeur, fusionCroissante_re(m1.suivant, None))
        else:
            return Maillon(m1.valeur,None)
    elif m2:
        if m2.suivant:
            return Maillon(m2.valeur, fusionCroissante_re(None, m2.suivant))
        else:
            return Maillon(m2.valeur,None)

print "Question 13 : (récrusif) "
l = fusionCroissante_re_l(l1, l2)
affichageIteratif(l)






        #############
        #Question 14#
        #############

# marche (2)
def suppr1sur2_it(l):
    """supprime un élément sur deux d'une
    liste chaînée, commence par le 1er
    (version (itérative)"""
    if l.premier:
        l.premier = l.premier.suivant
        courant = l.premier
        while courant:
            if courant.suivant:
                courant.suivant = courant.suivant.suivant
            courant = courant.suivant
    affichageIteratif(l)

print "Question 14 : (itératif) "
suppr1sur2_it(l)


def suppr1sur2_re_l(l):
    """supprime un élément sur deux d'une
    liste chaînée, commence par le 1er
    (version (récursive)"""
    if l.premier:
        l.premier = l.premier.suivant
        suppr1sur2_re(l.premier)
    affichageIteratif(l)

def suppr1sur2_re(m):
    """"""
    if m and m.suivant:
        m.suivant = m.suivant.suivant
        suppr1sur2_re(m.suivant)
    else:
        return

print "Question 14 : (récursif) "
suppr1sur2_re_l(l)




        #############
        #Question 15#
        #############















# Fin du TP listes chaînées
