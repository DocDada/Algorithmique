#coding:utf-8

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
        self.ordre = len(l_adj)# nb sommets
        self.adj = l_adj# liste adjacence

    def affiche(self):
        """affiche le graphe"""
        #print "Ordre du graphe : ", self.ordre
        print ("Ordre du graphe : ", self.ordre)
        for i in self.adj:
            #print i
            print (i)

    def degre(self, somm):
        """nombre de voisins du sommet somm"""
        if (somm<len(self.adj)):
            return len(self.adj[somm])
        return "Le sommet n'existe pas pour ce graphe"

    def taille(self):
        """renvoie nombre d'aretes du graphe"""
        nb = 0# nombre d'aretes
        for i in self.adj:
            nb = nb + len(i)
        return int(nb/2)

    def degreMax(self):
        """renvoie degre/voisins max d'un graphe"""
        return max(max(i) for i in self.adj)

    def nombreTriangle(self):
        """renvoie nombre de triangle dans un grapheNO"""
        nb = 0# nombre de triangles
        sommet = 0
        for i in range(len(self.adj)-1):
            if self.degre(i)>=2:# gere exception
                sommet = i
                for j in self.adj[i+1]:
                    if j==sommet:
                        nb += 1
        if nb>0:#gere exception
            return nb-1
        return 0

    # correction
    def nomb(self):
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



def grapheComplet(n):
    """renvoie grapheNo complet à n sommet"""
    liste=[[]*n for i in range(n)]
    for i in range(len(liste)):
        for j in range(n):
            if i!=j:
                liste[i].append(j)
    return GrapheNO(liste)

def cycle(n):
    """renvoie cycle à n sommets"""
    liste = [[]*n for i in range(n)]
    if n!=0:
        liste[0] = [n-1, 1]
        for i in range(1, n):
            liste[i]=[i-1, i+1]
        liste[n-1] = [n-2, 0]
        return GrapheNO(liste)
    return GrapheNO([])

def ordreArete(arete):
    """renvoie ordre d'une liste d'aretes"""
    maxi = [max(i) for i in arete]
    return max(maxi)+1

def aretes_vers_liste_adj(n, li_a):
    """renvoie liste adjacence à partir
    d'une liste d'aretes"""
    liste = [[]*n for i in range(n)]
    for i in li_a:
        liste[i[0]].append(i[1])
        liste[i[1]].append(i[0])
    return GrapheNO(liste)

def lireAretesEtOrdre(nomdufichier):
    """lit le fichier et renvoie la liste des aretes qui s'y trouvent
    ainsi que l'ordre"""
    #f = file(nomdufichier, 'r')# ouverture du fichier
    f = open(nomdufichier, 'r')
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

def lireGrapheNO(nomdufichier):
    """renvoie graphe à partir du nom du fichier
    utilise la fonction lireAretesEtOrdre"""
    arete, ordre = lireAretesEtOrdre(nomdufichier)
    return aretes_vers_liste_adj(ordreArete(arete), arete)



#      #
# MAIN #
#      #



liste = [[2,4],[2,3,4],[0,1,3,4],[1,2],[0,1,2]]
graphe = GrapheNO(liste)
graphe.affiche()
grapheVide = GrapheNO([[]])
print ("Nombre de voisins : ",graphe.degre(0))
print ("Nombre de voisins d'un grpahe vide : ", grapheVide.degre(1))
print ("Nombre d'arêtes", graphe.taille())
graphe2 = grapheComplet(4)
graphe2.affiche()

graphe3 = cycle(5)
graphe3.affiche()

arete = [[0,2],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4]]
graphe4 = aretes_vers_liste_adj(ordreArete(arete), arete)
graphe4.affiche()

#graphe5 = lireGrapheNO("metro.txt")
#graphe5.affiche()

listeTriangles2 = [[2,1], [0,2,3], [0,1, 3], [1,2]]
listeTriangles1 = [[1,2], [0], [0]]
grapheTriangle = GrapheNO(listeTriangles1)
print ("Nombre de triangle", grapheVide.nombreTriangle())
print ("Nombre de triangle", grapheTriangle.nomb())
grapheTriangle.ajoutSommet([2])
grapheTriangle.affiche()
grapheTriangle.supprSommet(3)
grapheTriangle.affiche()
