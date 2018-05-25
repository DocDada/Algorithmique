# coding: utf-8

class Automate:
    """classe permettant de manipuler des automates finis,
    déterministes ou non, avec ou sans epsilon-transitions"""


    def __init__(self, alphabet, etats, transition, initiaux, finals):
        """fonction d'initialisation (constructeur) de l'automate"""
        
        # l'alphabet est une liste (list) de symboles 
        # (généralement des int ou str).
        # on réserve le mot 'eps' comme symbole des epsilon-transitions
        self.alphabet = alphabet

        # ensemble (set) d'etats (généralement des int ou str)
        self.etats = etats

        # ensemble (set) des etats initiaux
        self.initiaux = initiaux

        # ensemble (set) des etats final
        self.finals = finals

        # fonction de transition : c'est un dict de dict de set !
        # plus simplement si auto est un automate, q un etat et s un symbole
        # alors auto.transition[q][s] est un ensemble (set) contenant
        # les etats de transition possibles depuis q pour le symbole s
        # on pourra aussi prendre s='eps' pour les epsilon-transitions
        if transition != None:
            self.transition = transition
        else:
            # on initialise des ensembles de transitions vides
            self.transition = initialiser_transition(alphabet, etats)

    @staticmethod
    def initialiser_transition(alphabet, etats):
        """méthode statique permettant d'initialiser la fonction
        de transition a partir de l'ensemble d'etats et de l'alphabet
        (deux 'list'). Pour chaque etat q et symbole s et pour s='eps',
        transition[q][s] sera un set (ensemble) vide au depart."""

        transition = {}
        for q in etats :
            transition[q] = {}
            for a in alphabet + ['eps'] :
                transition[q][a] = set([])
        return transition


    def __str__(self):
        """conversion en str : permet d'afficher un automate auto dans 
        la console a en faisant simplement 'print a'     """

        texte = "AUTOMATE\n   ALPHABET\n     "
        for symb in self.alphabet:
            texte += " " + str(symb)
        texte +="\n   ETATS\n     "
        for e in self.etats:
            texte += " " + str(e)
        texte +="\n   TRANSITIONS\n"
        for q in self.transition:
            for symb in self.transition[q]:
                if len(self.transition[q][symb]) > 0 :
                    texte += "      " + str(q) + " --" + str(symb) + "-->"
                    for q2 in self.transition[q][symb] :
                        texte += " " + str(q2)
                    texte +="\n"
     
        texte +="   INITIAUX\n     "
        for e in self.initiaux:
            texte += " " + str(e)
            texte +="\n   FINALS\n     "
        for e in self.finals:
            texte += " " + str(e)
        return texte

    # marche pas
    def est_complet(self):
        """renvoie un booleen indiquant si le graphe est complet ou non"""
        for q in self.transition:
            for symb in self.alphabet:
                if symb not in self.transition[q]:
                    return False
        return True

    def est_deterministe(self):
        """renvoie un booleen indiquant si le graphe est deterministe ou non"""
        if len(self.initiaux)!=1:
            return False
        for q in self.transition:
            for symb in self.transition[q]:
                if len(self.transition[q][symb]) > 1:
                    return False
                if symb =='eps' and len(self.transition[q])==0:
                    return False
        return True

    def contient_epsilon_transitions(self):
        for q in self.transition:
            for symb in self.transition[q]:
                if symb =='eps' and len(self.transition[q][symb])!=0:
                    return True
        return False

    def reconnait_v1(self, mot):
        """determine si un mot est reconnu ou non par l'automate
        (cas deterministe complet sans epsilon transitions"""
        if self.contient_epsilon_transitions():
            raise Exception("L'automate doit être sans epsilon transitions.")
        if not self.est_deterministe():
            raise Exception("L'automate doit être deterministe.")
        trans, = self.initiaux# recupere l'etat initial (premier element)
        final, = self.finals
        for char in mot:
            trans, = self.transition[trans][char]
        return trans==final

    def mots_reconnus(self):
        """renvoie la liste des mots de taille au plus n reconnus par
        l'automate"""




    def verification(self):
        """méthode qui vérifie que l'automate est convenablement formé
        assert renvoie une exception si la condition
        n'est pas vérifiée"""

        #verifie les types des champs de l'automate
        assert type(self.alphabet) is list
        assert type(self.etats) is set
        assert type(self.initiaux) is set
        assert type(self.finals) is set

        #verifie que 'eps' ne soit pas dans l'alphabet
        assert 'epys' not in self.alphabet

        #on verifie que la fonction de transition contient toutes les entrees
        #etat * symbole exactement et que les ensembles correspondants
        #sont bien des ensembles d'états
        assert type(self.transition) is dict
        assert set(self.transition.keys()) == self.etats

        for q in self.etats:
            assert set(self.transition[q].keys()) \
                    == set(self.alphabet + ["eps"])

            for symb in self.alphabet + ['eps']:
                for q2 in self.transition[q][symb]:
                    assert q2 in self.etats

        #etats initiaux non vide et sont des etats
        assert self.initiaux and self.initiaux.issubset(self.etats)

        #etats finals non vide et sont des etats
        assert self.finals and self.initiaux.issubset(self.etats)


def lire_automate(nomfichier):
    """lit un fichier contenant un automate et renvoie l'automate
    correspondant. 

    FORMAT D'UN FICHIER AUTOMATES
    commentaires au debut puis dans l'ordre :

    1. une ligne 
    ALPHABET s1 s2 ... 
    où s1, s2, ... sont les symboles (str) de l'alphabet

    2. une ligne 
    ETATS q1 q2 ...
    où q1, q2, etc. sont les noms (str) des états

    3. autant de lignes 
    TRANSITION  etat_depart  symbole  etat_arrivee 
    que nécessaire

    4. une ligne 
    INITIAUX i1 i2 ...
    liste des etats initiaux
   
    5. une ligne 
    FINALS f1 f2 ... 
    liste des etats finals
    """


    #lit et met toutes les lignes du fichier dans un tableau de str
    fichier = open(nomfichier,"r")
    lignes = fichier.readlines()
    fichier.close()

    i = 0 # numero de ligne

    #recherche de la première ligne commençant par "ALPHABET"
    mots = lignes[i].split()
    while len(mots)==0 or mots[0] != "ALPHABET":
        i +=1 
        mots = lignes[i].split()
    alphabet = mots[1:]

    #idem pour "ETATS"
    i +=1
    mots = lignes[i].split()
    while mots[0] != "ETATS":
        i +=1 
        mots = lignes[i].split()
    etats = set(mots[1:])

    #idem pour "TRANSITION"
    i+=1
    mots = lignes[i].split()
    while mots[0] != "TRANSITION":
        i +=1 
        mots = lignes[i].split()

    
    transition = Automate.initialiser_transition(alphabet, etats)
    #pour chaque ligne "TRANSITION" on ajoute ce qui crresipond
    while mots[0] == "TRANSITION":
        depart = mots[1]
        symbole = mots[2]
        arrivee = mots[3]
        transition[depart][symbole].add(arrivee)
        i +=1 
        mots = lignes[i].split()
 
    while mots[0] != "INITIAUX":
        i +=1 
        mots = lignes[i].split()
    initiaux = set(mots[1:])

    while mots[0] != "FINALS":
        i +=1 
        mots = lignes[i].split()
    finals = set(mots[1:])

    resultat = Automate(alphabet, etats, transition, initiaux, finals)

    #on lance une verification de l'automate
    try:
        resultat.verification()
    except AssertionError as e:
        raise 

    return resultat


def mots_taille_au_plus(n, alphabet):
    """renvoie la liste des mots de taille de 0 à n compris
    dans l'alphabet fourni"""

    mots = [ [''] ] + [ [] for i in range(n)]
    for i in range(1,n+1):
        for symb in alphabet:
            mots[i].extend([m+symb for m in mots[i-1]])
    return [x for ligne in mots for x in ligne]








########
# MAIN #
########

for i in range(1,5):
    auto1 = lire_automate("auto"+str(i)+".txt")
    print auto1
    print "EST IL COMPLET ? ", auto1.est_complet()
    print "EST IL DETERMINISTE ? ", auto1.est_deterministe()
    print "CONTIENT IL DES EPSILON TRANSITIONS ? ", auto1.contient_epsilon_transitions()
    if i==1:
        print "RECONNAIT V1 : ", auto1.reconnait_v1("bbbbbaba")

