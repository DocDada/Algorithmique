#coding:utf-8
import os
        #######################
        #                     #
        #    TP1 - GRAPHES    #
        #     ET LANGAGES     #
        #                     #
        #######################

class GrapheNO:
    """graphe code par liste d'adjacence. Sommets numérotés
    entre numerotes 0,1,...,n-1"""

    def __init__(self, l_adj):
        """initialise un graphe d'apres la liste d'adjacence
        l_adj et son ordre n"""
        self.ordre = len(l_adj)# nombre de sommets
        self.adj = l_adj# liste adjacence

    # correction
    def __str__(self):
        """permet de faire un print sur le graphe"""
        s = "Ordre du graphe : " + str(self.ordre) + "\n"
        s += "Taille du graphe : " + str(self.taille()) + "\n"
        for v in range(self.ordre):
            s += "voisins de " + str(v) + " -> " + str(self.adj[v]) + "\n"
        return s


    def affiche(self):
        """affiche le graphe et son ordre"""
        print ("Ordre du graphe : ", self.ordre)
        for i in self.adj:
            print (i)

    def degre(self, sommet):
        """nombre de voisins du sommet somm"""
        if (sommet<len(self.adj)):# gere exception
            return len(self.adj[sommet])
        return "Le sommet ", sommet, " n'existe pas pour ce graphe"

    def taille(self):
        """renvoie nombre d'aretes du graphe"""
        nombreAretes = 0# nombre d'aretes
        for aretesSommet in self.adj:
            nombreAretes = nombreAretes + len(aretesSommet)
        return int(nombreAretes/2)

    def degreMax(self):
        """renvoie degre/voisins max d'un graphe"""
        return max(max(i) for i in self.adj)

    # correction 1
    def nombreTrianglesV1(self):
        """compte le nombre de triangles version basique"""
        compteur = 0
        for v1 in range(self.ordre):
            for v2 in range(self.ordre):
                for v3 in range(self.ordre):
                    if v2 in self.adj[v1] and v3 in self.adj[v2] and v1 in self.adj[v3]:
                        compteur += 1
        return int(compteur/6)

    # correction 2
    def nombreTrianglesV2(self):
        """renvoie le nombre de triangles dans un
        graphe"""
        n = 0
        for i in range(len(self.adj)):
            for j in self.adj[i]:
                for k in self.adj[j]:
                    if k in self.adj[i]:
                        n += 1
        return int(n/6)

    def ajoutSommet(self, sommet):
        """ajoute un sommet n au graphe
        ancien ordre : n ; nouvel ordre : n+1"""
        for i in sommet:
            if i<self.ordre:# gere exception
                self.adj[i].append(self.ordre)
        self.adj.append(sommet)

    def supprSommet(self, s):
        """supprime un sommet d'un graphe"""
        longueur = self.ordre
        for i in self.adj:
            for j in range(len(i)):
                if i[j]>s:# renumerote les sommets
                    i[j] = i[j] - 1
                elif i[j]==s:# supprime aretes liees à s
                    del i[j]
        del self.adj[s]

    def composanteConnexe(self, i):
        """renvoie pour un sommet i la liste des sommets
        de la composante connexe de i"""
        if self.taille()==0:# gere exception
            return []
        connu = [i==j for j in range(self.ordre)]
        compConx=[i]# file d'attente
        while len(compConx) != 0:# tant que la file d'attente n'est pas vide
            enAttente = compConx.pop()#recupère sommet
            for i in self.adj[enAttente]:
                if connu[i] == False:
                    compConx.append(i)
                    connu[i]=True
        return [i for i in range(len(connu)) if connu[i]==True]

    def nbComposantesConnexes(self):
        """retourne le nombre de composantes connexes du graphe
        utilise composanteConnexe"""
        listeC = []# on ne connait pas la taille de la liste
        for i in range(self.ordre):
            booleen = True
            for j in listeC:
                if i in j:
                    booleen = False
            if booleen:
                liste = self.composanteConnexe(i)
                if liste not in listeC:
                    listeC.append(liste)
        return len(listeC)

    # correction
    def nb_composantes_connexes(self):
        """renvoie le nb de composantes connexes dans le graphe"""
        compteur_comp = 0
        composantes = [None]*self.ordre
        for v in range(self.ordre):
            if composantes[v] == None:  #s'il est inconnu encore
                compteur_comp += 1
                composantes[v] = compteur_comp
                #lance un parcours depuis v
                attente = [v]
                while attente:
                    courant = attente.pop()
                    for voisin in self.adj[courant]:
                        if composantes[voisin] == None : #il est inconnu
                            composantes[voisin] = compteur_comp
                            attente.append(voisin)
                #parcours fini
        return compteur_comp


def grapheComplet(n):
    """renvoie grapheNo complet à n sommet"""
    liste=[[]*n for i in range(n)]
    for i in range(len(liste)):
        for j in range(n):
            if i!=j:
                liste[i].append(j)
    return GrapheNO(liste)

# correction
def grapheCompletCorrection(n):
    """ne marche pas pour n=1, =2, =0"""
    l_adj = []
    for v in range(n):
        voisinage = []
        for voisin in range(n):
            if voisin != v:
                voisinage.append(voisin)
        l_adj.append(voisinage)
    return GrapheNO(l_adj)

# correction
def grapheCompletDesStars(n):
    """version pour les ptits champions"""
    return GrapheNO( [ range(i)+ range(i+1,n) for i in range(n)])

def cycle(n):
    """renvoie cycle à n sommets"""
    liste = [[]*n for i in range(n)]
    if n>2:
        liste[0] = [n-1, 1]
        for v in range(1, n):
            liste[v]=[v-1, v+1]
        liste[n-1] = [n-2, 0]
        return GrapheNO(liste)
    elif n==1:
        return GrapheNO([[]])
    elif n==2:
        return GrapheNO([[1][0]])

# correction
def cycleCorrection(n):
    l_adj = [[1, n-1]]
    for v in range(1, n-1):
        l_adj.append([v-1, v+1])
    l_adj.append([n-2, 0])
    return GrapheNO(l_adj)




def ordreArete(arete):
    """renvoie ordre d'une liste d'aretes"""
    maxi = [max(i) for i in arete]
    return max(maxi)+1

# marche ?
def aretes_vers_liste_adj(ordre, li_a):
    """renvoie liste adjacence à partir
    d'une liste d'aretes"""
    liste = [[]*ordre for i in range(ordre)]
    for i in li_a:
        liste[i[0]].append(i[1])
        liste[i[1]].append(i[0])
    return liste

def lireAretesEtOrdre(nomDuFichier):
    """lit le fichier et renvoie la liste des aretes qui s'y trouvent
    ainsi que l'ordre"""
    #f = file(nomDuFichier, 'r')# ouverture du fichier python 2.7
    f = open(nomDuFichier, 'r')# python 3.6
    lignes = f.readlines()
    #on extrait les lignes qui commencent par 'E'
    #si c'est bon on cree une nouvelle arete
    aretes = []
    ordre = 0
    for l in lignes:
        mots = l.split()
        if len(mots) >= 3 and mots[0]=='E':
            aretes.append([int(mots[1]), int(mots[2])])# conversion str en int
        if len(mots) > 0 and mots[0]=="ordre":
            ordre = int(mots[1])# récupère l'ordre du graphe
    return aretes, ordre

def lireGrapheNO(nomDuFichier):
    """renvoie graphe à partir du nom du fichier
    utilise la fonction lireAretesEtOrdre"""
    arete, ordre = lireAretesEtOrdre(nomDuFichier)
    return GrapheNO(aretes_vers_liste_adj(ordreArete(arete), arete))



#      #
# MAIN #
#      #


os.system('clear')
liste = [[2,4],[2,3,4],[0,1,3,4],[1,2],[0,1,2]]
graphe = GrapheNO(liste)
graphe.affiche()
grapheVide = GrapheNO([[]])
print ("Nombre de voisins : ",graphe.degre(0))
print ("Nombre de voisins d'un grpahe vide : ", grapheVide.degre(1))
print ("Nombre d'arêtes", graphe.taille())
print ("GRAPHE COMPLET")
graphe2 = grapheComplet(4)
graphe2.affiche()
graphe2c = grapheComplet(4)
graphe2c.affiche()

graphe3 = cycle(5)
graphe3.affiche()

#arete = [[0,2],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4]]
arete = [[0, 3],[1,2]]
graphe4 = aretes_vers_liste_adj(ordreArete(arete), arete)
graphe4.affiche()

#graphe5 = lireGrapheNO("metro.txt")
#graphe5.affiche()
"""
listeTriangles2 = [[2,1], [0,2,3], [0,1, 3], [1,2]]
listeTriangles1 = [[1,2], [0], [0]]
grapheTriangle = GrapheNO(listeTriangles1)
print ("Nombre de triangle", grapheTriangle.nomb())
grapheTriangle.ajoutSommet([2])
grapheTriangle.affiche()
grapheTriangle.supprSommet(3)
grapheTriangle.affiche()
grapheTriangle.ajoutSommet([])
grapheTriangle.affiche()
listeComp = graphe3.composanteConnexe(3)
print ("Composante connexe : ", listeComp)
"""

print ("Nombre de triangle vide", grapheVide.nomb())
print ("Nombre de triangle dans un cycle", graphe3.nomb())
print ("Nombre de triangle dans ", graphe2.nomb())


grapheCycle1 = cycle(1)
print ("Cycle 1")
grapheCycle1.affiche()

grapheCycle2 = cycle(2)
print ("Cycle 2")
grapheCycle2.affiche()

grapheCycle3 = cycle(3)
print ("Cycle 3")
grapheCycle3.affiche()
"""
print ("Correction CYCLE")


grapheCycle0 = cycleCorrection(0)
print ("Cycle 0")
grapheCycle0.affiche()

grapheCycle2 = cycleCorrection(2)
print ("Cycle 2")
grapheCycle2.affiche()

grapheCycle3 = cycleCorrection(3)
print ("Cycle 3")
grapheCycle3.affiche()
"""
print ("Lecture des fichiers composantes.txt")



for i in range(10):
    fichier="composantes"+ str(i)+".txt"
    grapheTxt = lireGrapheNO(fichier)
    listeCompTxt = grapheTxt.composanteConnexe(333)
    print ("Composante connexe : ", len(listeCompTxt))
    print ("Nombre de composantes : ", grapheTxt.nbComposantesConnexes())
