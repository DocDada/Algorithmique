# Algorithmique
# TP 1
# Tri

def TriRapide(tab, gauche, droite):
    if gauche < droite:
        tab, k = Placer(tab, gauche, droite)
        tab = TriRapide(tab, gauche, k-1)
        tab = TriRapide(tab, k+1, droite)
    return tab

def Placer(tab, gauche, droite):
    bas = gauche +1
    haut = droite
    print tab
    while bas <= haut:
        while tab[bas] <= tab[gauche]:
            print "BAS : ", bas, "GAUCHE : ", gauche
            bas = bas + 1
        while tab[haut] > tab[gauche]:
            print "HAUT : ", haut, "GAUCHE : ", gauche
            haut = haut - 1
        if bas < haut:
            tab[bas], tab[haut] = tab[haut], tab[bas]
            bas = bas + 1
            haut = haut - 1
    tab[gauche], tab[haut] = tab[haut], tab[gauche]
    k = haut
    print "K : ", k
    return tab, k

def saisie_tableau():
    taille = input("Entrez la taille du tableau : ")
    tab = []
    for e in range(taille-1):
        #tab[e] = input("Entrez une valeur : ")
        tab.append(input("Entrez une valeur : "))
    tab.append(max(tab)+1)
    print tab
    TriRapide(tab, 0, taille-1)
    print tab


#
# MAIN
#




saisie_tableau()






"""

def ex1(tab, i1, i2):
    # gestion des exceptions
    if i1<0 or i1>=len(tab) or i2<0 or i2>=len(tab):
        return
    sentinelle = max(tab)+1
    tab.append(sentinelle)# placement de la sentinelle en T[n+1]
    sous_tab = [sentinele]

    gauche = i1
    bas = gauche + 1
    haut = i2
    while bas <= haut:
        while tab[bas] <= tab[gauche]:
            bas += 1
        while tab[haut] > tab[gauche]:
            haut -= 1
        if bas < haut:
            #tab[bas], tab[haut] = tab[haut], tab[bas]
            sous_tab.append(tab.pop[haut])
            bas += 1
            haut -= 1
    tab[gauche], tab[haut] = tab[haut], tab[gauche]
    return tab
"""

