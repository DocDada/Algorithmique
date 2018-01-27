#coding:utf-8

# ALGORITHMIQUE

# TP2 TABLEAUX



    ##############
    #            #
    # QUESTION 0 #
    #            #
    ##############

def somme(tab):
    """renvoit la somme d'un tableau d'entiers
    FONCTION SUM"""
    somme = 0
    for i in tab:
        somme += i
    return somme

tab = range(10)
print "Question 0 : la somme des elements de ", tab," donne :", somme(tab)



    ##############
    #            #
    # QUESTION 1 #
    #            #
    ##############

def maximum(tab):
    """renvoie le maximum d'un tableau d'entiers
    FONCTION MAX"""
    maximum = None
    for i in tab:
        if i > maximum:
            maximum = i
    return maximum

print "Question 1 : le maximum de ", tab," est :", maximum(tab)



    ##############
    #            #
    # QUESTION 2 #
    #            #
    ##############

def indice_maxi(tab):
    """renvoie la liste des indices correspondant
    au maximum"""
    maximum = None
    indice = []*10
    for i in range(len(tab)):
        if tab[i] > maximum:
            indice = tab[i]
        elif i == maximum:
            indice += i
    return indice

print "Question 2 : la liste des contenant les indices des maximums de ", tab," est : ", indice_maxi(tab)



    ##############
    #            #
    # QUESTION 3 #
    #            #
    ##############

def estPalindrome(tab):
    """verifie si la chaine est un palindrome
    ex : eluparcettecrapule
    si vrai return True, sinon False"""
    for i in range(len(tab)):
        if tab[i] != tab[len(tab) - i- 1]:
            return False
    return True

chaine = raw_input()
print "Question 3 : cette chaine est-elle un palindrome ? ", estPalindrome(chaine)



    ##############
    #            #
    # QUESTION 4 #
    #            #
    ##############

def inversion(tab):
    """inverse un tableau d'entiers sur place et le retourne
    FONCTION REVERSE"""
    for i in range(len(tab)/2):
        tab[i], tab[len(tab) - i - 1] = tab[len(tab) - i - 1] ,tab[i]
    return tab

print "Question 4 : ", tab," inverse, donne : ", inversion(tab)

def inversionV2(tab):
    """inverse un tableau d'entiers sur place
    version propre"""
    return [tab[len(tab)-i-1] for i in range(len(tab))]

print "Question 4 : ", tab," inverse, donne : ", inversionV2(tab)



    ##############
    #            #
    # QUESTION 5 #
    #            #
    ##############

def plusLongPrefixe(tab1, tab2):
    """renvoie le plus long prefixe commun
    de deux tableaux"""
    if len(tab1)<len(tab2):
        tab = tab1
        tableau = tab2
    else:
        tab = tab2
        tableau = tab1
    for i in range(len(tab)):
        if tab[i] != tableau[i]:
            if i == 0:
                return None
            return tab[:i-1]
    return tab

tab = range(10)
tab2 = range(0)
print "Question 5 : le plus long prefixe commun de ", tab," et de ", tab2," est : ", plusLongPrefixe(tab, tab2)



    ##############
    #            #
    # QUESTION 6 #
    #            #
    ##############

def plusLongSousMot(tab1, tab2):
    """renvoie le plus long sous mot commun
    de deux tableaux"""
    sousMot = []
    for i in range(len(tab1)):
        for j in range(len(tab2)):
            prefixe = plusLongPrefixe(tab1[i], tab2[j])
            if len(prefixe)==len(tab1[i]) and len(prefixe)>len(sousMot):
                sousMot = prefixe
    return sousMot

tab=[range(3), range(2), range(6)]
tab2=[range(1), range(4), range(2)]
print "Question 6 : le plus long sous mot de ", tab," et de ", tab2," est : ", plusLongSousMot(tab, tab2)



    ##############
    #            #
    # QUESTION 7 #
    #            #
    ##############

def estCroissant(tab):
    """teste si un tableau d'entiers
    est en ordre croissant ou non
    si oui return True, sinon False"""
    for i in range(len(tab)-1):
        if tab[i]>tab[i+1]:
            return False
    return True

tab =range(10, -6, -2)
print "Question 7 : la liste ", tab," est-elle croissante ? ",estCroissant(tab)



    ##############
    #            #
    # QUESTION 8 #
    #            #
    ##############

def fusion_croissante(tab1, tab2):
    """realise la fusion croissante de deux
    tableaux d'entiers, supposés croissants"""
    tab=[]*30
    i=0
    j=0
    while(tab1[i] or tab2[j]):
        if tab1[i]>tab2[j]:
            tab.append(tab2[j])
            j+=1
        else:
            tab.append(tab1[i])
            i+=1
        if i==len(tab1):
            tab+=tab2[j:]
            return tab
        elif j==len(tab2):
            tab+=tab1[i:]
            return tab

tab = range(2,6)
tab2 = range(4)
print "Question 8 : fusion croissante de ", tab," et de ", tab2," : ", fusion_croissante(tab, tab2)



    ##############
    #            #
    # QUESTION 9 #
    #            #
    ##############

def tableauSpec(p, q):
    """renvoie un tableau p*q
    les arguments sont supposés != 0"""
    tableau = []
    for i in range(0,q*p, q):
        tableau.append(range(i, i+q))
    return tableau

ligne=3
colonne = 4
print "Question 9 : ", tableauSpec(ligne, colonne)

def tableauSpecV2(p, q):
    """renvoie un tableau p*q
    les arguments sont supposés != 0
    version propre"""
    return [range(i, i+q) for i in range(0, q*p, q)]

tab = tableauSpec(ligne, colonne)



    ###############
    #             #
    # QUESTION 10 #
    #             #
    ###############

def moy8CasesAutour(tab, posx, posy):
    """renvoie la moyenne des huits cases
    autour d'une case donnée d'un tableau
    bidimensionnel"""
    somme = 0
    compteur = 0
    for x in range(posy-1, posy+2):
        for y in range(posx-1, posx+2):
            if x!=posx and y!=posy:
                somme+=tab[x][y]
                compteur += 1
    return somme/compteur

print "Question 10 : ", moy8CasesAutour(tab, 1, 1)



    ###############
    #             #
    # QUESTION 11 #
    #             #
    ###############

def minimax(tab):
    """renvoie le minimum du maximum des lignes d'un tableau"""
    liste_max=[]*5
    for i in tab:
        liste_max.append(maximum(i))
    maxi = liste_max[0]
    for j in liste_max:
        if j<maxi:
            maxi=j
    return maxi

print "Question 11 : le minimax est : ", minimax(tab)



    ###############
    #             #
    # QUESTION 12 #
    #             #
    ###############

def permutCirculaire(tab):
    """permute circulairement les elements d'une
    liste de gauche a droite, de haut en bas"""
    stock = tab[len(tab)-1][len(tab[len(tab)-1]) -1]
    for i in range(len(tab)-1, -1, -1):
        for j in range(len(tab[i])-1, 0, -1):
            tab[i][j] = tab[i][j-1]
        tab[i][j-1] = tab[i-1][len(tab[i-1])-1]
    tab[0][0] = stock
    return tab

print "Question 12 : permutation circulaire de ", tab," donne : ", permutCirculaire(tab)


        #####################
        #-------------------#
        #|                 |#
        #|  TP2 TABLEAUX   |#
        #|   |  SUITE  |   |#
        #|   |    |    |   |#
        #-------------------#
        #####################



    ##############
    #            #
    # QUESTION 0 #
    #            #
    ##############

def zerosConsecutifs(tab):
    """renvoie la plus longue suite de
    zeros consecutifs dans ce tableau"""
    compteur=0
    for i in tab:
        if i==0:
            compteur+=1
        elif i!=0:
            tab.append(compteur)
            compteur=0
    maxi = maximum(tab)
    return [0]*maxi

tab = [0,0,0,1,2,3,0,0,0,0,1]
print "\nQuestion 0 : plus longue suite de zeros consecutifs dans ", tab," : ", zerosConsecutifs(tab)



    ##############
    #            #
    # QUESTION 1 #
    #            #
    ##############

def plusLongSousTableau(tab):
    """renvoie la longueur du plus long sous tableau
    strictement croissant"""
    longueur=[]*20
    for i in tab:
        compteur=0
        for j in range(len(i)-1):
            if i[j]<i[j+1]:
                compteur += 1
            else:
                break
        longueur.append(compteur)
    return maximum(longueur)

tab=[range(4), range(0,-6,-1), [0]]
print "Question 1 : ", plusLongSousTableau(tab)



    ##############
    #            #
    # QUESTION 2 #
    #            #
    ##############

def plusGrandEcart(tab):
    """renvoie le plus grand ecart entre
    les elements du tableau d'entiers"""
    ecart=[]*30
    for i in range(len(tab)):
        for j in range(i+1, len(tab)):
            ecart.append(abs(i-j))
    return maximum(ecart)

tab=range(7)
print "Question 2 : le plus grand ecart est : ", plusGrandEcart(tab)



    ##############
    #            #
    # QUESTION 3 #
    #            #
    ##############

def supprRepetitions(tab):
    """supprime les répétitions et le
    remplie de None"""
    i=1
    while tab[i] !=None:
        if tab[i]==tab[i-1]:
            tab.pop(i)
            tab.append(None)
        else:
            i+=1
    return tab

tab=[0,0,0,1,2,2,2,3,3,4]
print "Question 3 : ", tab," en supprimant les repetitions, donne : ", supprRepetitions(tab)



    ##############
    #            #
    # QUESTION 4 #
    #            #
    ##############

class Etudiant:
    """un etudiant a un nom et un genre"""
    nom = "inconnu"
    genre = "n"

    def toString(self):
        """affiche proprement l'etudiant :
        nom et genre"""
        print self.nom, ":",self.genre

def rangementFeminin(tab):
    """on place les femmes devant les
    hommes"""
    for i in range(len(tab)):
        if tab[i].genre=='h':
            for j in range(i+1, len(tab)):
                # on parcourt la classe
                if tab[j].genre=='f':# si femme il y a ...
                    tab[j], tab[i] = tab[i], tab[j]#echange entre un h et une f
    return tab


def afficheClasse(tab):
    """lit un tableau d'etudiants"""
    for i in tab:
        i.toString()

toto = Etudiant()
toto.nom = "toto"
toto.genre = 'h'

tito=Etudiant()
tito.nom = "tito"
tito.genre = 'h'

tete=Etudiant()
tete.nom = "tete"

tyty=Etudiant()
tyty.nom = "tyty"

tata=Etudiant()
tata.nom="tata"
tata.genre='f'

titi=Etudiant()
titi.nom="titi"
titi.genre='f'

# classe d'etudiants
tableau = [toto, tete, titi, tata, tito, tyty]
print "La classe dans son entierete : "
afficheClasse(tableau)
print "Question 4 : une classe, range, donne "
afficheClasse(rangementFeminin(tableau))



    ##############
    #            #
    # QUESTION 5 #
    #            #
    ##############

def rangementOmni(tab):
    """on place les genres indetermines
    devant, puis les femmes"""
    compteur = 0
    for i in range(len(tab)):
        if tab[i].genre != 'n':
            for j in range(i+1, len(tab)):
                if tab[j].genre=='n':
                    tab[i], tab[j] = tab[j], tab[i]
                    compteur = i
    #rangementFeminin(tab[compteur:]) ne marche pas
    for i in range(compteur, len(tab)):
        if tab[i].genre=='h':
            for j in range(i+1, len(tab)):
                if tab[j].genre=='f':
                    tab[j], tab[i] = tab[i], tab[j]
    return tab

print "La classe dans son entierete : "
afficheClasse(tableau)
print "Question 5 : une classe, range, donne "
afficheClasse(rangementOmni(tableau))
































# Fin du TP2 TABLEAUX
