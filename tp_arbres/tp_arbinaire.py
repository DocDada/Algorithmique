# coding: utf-8

from affiche_arbre import *

class Arbre:
	""" Implémentation des Arbres binaires ( D = droite; G = gauche)"""
	
	val = None	#valeur du noeud
	G = None		#sous arbre Gauche
	D = None		#sous arbre Droit
	
	def __init__(self, valeur, aG, aD):
		self.val = valeur
		self.G = aG
		self.D = aD
	
	def ajouterFils(self, a, cote):
		if cote == "G":
			self.G = a
		elif cote == "D":
			self.D = a


def entrerArbre(p):
	print "    "*(p-1),
	valeur = raw_input("Valeur : ")
	if valeur == "":
		return None
	else:
		return Arbre(valeur, entrerArbre(p+1), entrerArbre(p+1))



oper = ['+', '-', '*', '/', '**', '%']
"""

def is_expr(t, op=False):
    if t.val == None:
        return True
    if op:
        if t.val in oper:
            return False
        else:
            return is_expr(t.G, True) & is_expr(t.D, True)
    elif t.val in oper:
        return is_expr(t.G, False) & is_expr(t.D, False)
    elif t.val not in oper:
        return False
    return True

"""
"""
def is_expr(t):
    if t:
        return True
    if op:
        if t.val not in oper:
            return False
        else:
            return is_expr(t.G, False) & is_expr(t.D, False)
    else:
        if t.val in oper:
            return is_expr(t.G, False) & is_expr(t.D, False)
        else:
            return is_expr(t.G, True) & is_expr(t.D, True)
    return True
"""

"""renvoie un booleen si l'arbre represente une expression arithmetique"""

def has_double_knot(t):
    if t:
        if t.G == None | t.D == None:
            return False
        else:
            return has_double_knot(t.G) & has_double_knot(t.D)
    return False

def right_expr(t):
    if t:
        if t.G == None & t.D == None:
            if t.val in oper or t.val.is_integer():
                return True
        else:
            if t.val in oper:
                return right_expr(t.G) & right_expr(t.D)
    return False
    
def is_expr(t):
    return has_double_knot(t) & right_expr(t)
    
def main():
    t = entrerArbre(3)
    #treeDrawer.dessiner_arbre(t)
    print(is_expr(t))

################################################################################

main()





