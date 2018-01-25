#coding: utf-8

#QUESTION 0

def somme(tab):
    """renvoie la somme des éléments d'un tableau d'entiers"""
    somm = 0
    for i in range(len(tab)):
        somm = somm + tab[i]
    return somm
tab = range(7)
print "La somme des entiers de",range(7),"est", somme(tab)
# on peut aussi mettre tab à la place de range(7)

#QUESTION 1

def maximum(tab):
    for i in range(1,len(tab)):
        if tab[i]>tab[i-1]:
            maxi = tab[i]
        else:
            maxi = tab[i-1]
    return maxi
print "\nLe maximum du tableau d'entiers",tab,"est :", maximum(tab)

#QUESTION 2

def indice_maxi(tab):
    for i in range(1,len(tab)):
        if tab[i]>tab[i-1]:
            maxi = tab[i]
            indice = i
        else:
            maxi = tab[i-1]
            indice = i - 1
    return indice
print "\nL'indice du maximum du tableau d'entiers",tab,"est :", indice_maxi(tab)

#QUESTION 3

def palindrome(chaine):
    for i in range(len(chaine)/2 + 1):
        if chaine[i] != chaine[len(chaine) - 1 - i]:# indice le + grand : len(liste) - 1
            return False
    return True
chaine = ['a','b','c']
print "\nLa chaine de caractères",chaine,"est-elle un palindrome ?", palindrome(chaine)

#QUESTION 4

def inversion(chaine):
    for i in range(len(chaine)/2):
        stock = chaine[i]
        chaine[i] = chaine[len(chaine) - 1- i]
        chaine[len(chaine) - 1 - i] = stock
    return chaine
print "\nLa chaine de caractères", chaine,"inversée, donne ceci :",inversion(chaine)

#QUESTION 5 NE MARCHE PAS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def prefixe(tab, tab3):
    if len(tab) < len(tab3):
        tableau = tab
        grand = tab3
    else:
        tableau = tab3
        grand = tab
    """for i in range(len(tableau)):
    if tableau[i] != grand[i]:
    return tableau[:i+1]"""
    """if tableau[i] == grand[i]:
    tablea = tableau[:i+1]
    return tablea"""###CECI MARCHE
tab3=range(5)
print "\nLe plus long préfixe des chaines",tab,tab3,"est : ",prefixe(tab, tab3)

#QUESTION 6



#QUESTION 7

def croissant(tab):
    """vérifie si un tableau est en ordre croissant"""
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            return False
    return True
tab2 = [ 1, 2, 6, 4, 5, 6 ]
print "\nLe tableau",tab,"est-il croissant ?",croissant(tab),"\nLe tableau",tab2,"est-il croissant ?",croissant(tab2)

#QUESTION 8

def fusion_tableaux(tab1, tab2):
    """fusionne deux tableaux et retourne un tableaux
    dont les éléments sont triés"""
    tab1.extend(tab2)
    tab1.sort()
    return tab1
tab1 = [ 1, 2, 3, 4, 5, 6 ]
tab2 = [ 1, 2, 6, 4, 5, 6 ]
print fusion_tableaux(tab1, tab2)

#QUESTION 9 & 10

def tableaux(p, q):
    """renvoie un tableau p*q, qui va des entiers de 0 à
    pq - 1
    renvoie la moyenne des entiers du tableaux hormis les coins"""
    compteur = 0
    liste = []
    lis = []
    moy = 0.0# .0 nécessaire pour que ce soit une moyenne(si impair)
    for e in range(1, p+1):
        while compteur < q*e:
            liste.append(compteur)
            if (compteur != 0) & (compteur != q-1) & (compteur!=q*p -1) & (compteur != (q*p)-q):
                moy = moy + compteur
            compteur += 1
        lis.append(liste)
        liste = []
    moy = moy/((p*q)-4)
    return moy
    #return lis
p = 3
q = 4
print tableaux(p, q)

#QUESTION 11
