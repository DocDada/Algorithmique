class ListeChainee:
    """classe pour manipuler les listes chainees, contient
    une reference au premier maillon"""
    def __init__(self, prem):
        self.premier = prem     # premier maillon


class Maillon:
    """maillon pour les listes chainees"""
    def __init__(self, val, suiv):
        self.valeur = val
        self.suivant = suiv

class ListeDoublementChainee:
    def __init__(self, prem, der):
        self.premier = prem   # premier maillon
        self.dernier = der

class MaillonDouble:
    """maillons de liste doublement chainee"""
    def __init__(self, val, suiv, prec):
        self.valeur = val     # valeur du maillon
        self.suivant = suiv   # maillon suivant
        self.precedent = prec # maillon precedent



###############################################################

def affichageIteratif(maliste):
    """affiche dans l'ordre les valeurs
    des maillons d'une liste chainee """
    courant = maliste.premier
    while courant:
        print courant.valeur
        courant = courant.suivant

def affichageIteratifLDC(maliste):
    """affiche dans l'ordre les valeurs
    des maillons d'une liste chainee """
    courant = maliste.premier
    while courant:
        print courant.valeur,
        courant = courant.suivant
    print '\n'

###############################################################

def affichageRecursifListe(maliste):
    """lance l'affichage recursif des valeurs des
    maillons de la liste"""
    if maliste.premier:
        affichageRecursifMaillon(maliste.premier)

def affichageRecursifMaillon(m):
    """affichage recursif des valeurs des maillons
    m est un maillon (non None)"""
    print m.valeur
    if m.suivant:
        affichageRecursifMaillon(m.suivant)


###############################################################

def constructionClavierOrdreInverse():
    """renvoie une liste chainee de str dont les valeurs
    sont entrees au clavier dans l'ordre inverse
    entree vide pour terminer la saisie"""

    courant = None  # premier maillon de la liste, vide au depart
    fini = False
    while not fini:
        val = raw_input("Entrez la donnee (rien pour terminer) : ")
        if val == "":
            fini = True
        else:       # ajout du nouveau maillon avant
            nouveau = Maillon(val, courant)
            courant = nouveau

    return ListeChainee(courant)


def constructionClavier():
    """renvoie une liste chainee de str dont les valeurs
   sont entrees au clavier dans l'ordre
   entree vide pour terminer la saisie"""

    # on traite separement le cas ou aucun maillon n'est cree
    val = raw_input("Entrez la donnee (rien pour terminer) : ")
    if val == "":    # aucun maillon cree
        return ListeChainee(None)
    else:
        # on cree le premier maillon et on garde la reference
        premier = Maillon(val, None)
        courant = premier
        # courant va avancer au fur et a mesure
        fini = False
        while not fini:
            val = raw_input("Entrez la donnee (rien pour terminer) : ")
            if val == "":
                fini = True
            else:
                nouveau = Maillon(val, None)
                courant.suivant = nouveau
                courant = nouveau
    return ListeChainee(premier)



def constructionClavierLDC():
    """renvoie une liste doublement chainee
    de str dont les valeurs
    sont entrees au clavier dans l'ordre
    entree vide pour terminer la saisie"""

    # on traite separement le cas ou aucun maillon n'est cree
    val = raw_input("Entrez la donnee (rien pour terminer) : ")
    if val == "":    # aucun maillon cree
        return ListeDoublementChainee(None, None)
    else:
        # on cree le premier maillon et on garde la reference
        premier = MaillonDouble(val, None, None)
        dernier = MaillonDouble(val, None, None)
        courant = premier
        # courant va avancer au fur et a mesure
        fini = False
        while not fini:
            val = raw_input("Entrez la donnee (rien pour terminer) : ")
            if val == "":
                fini = True
            else:
                courant.suivant = MaillonDouble(val, None, courant)
                courant = courant.suivant
                dernier = courant
    return ListeDoublementChainee(premier, dernier)






###############################################################

#maliste = constructionClavierOrdreInverse()
#affichageRecursifListe(maliste)
