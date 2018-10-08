# coding: utf-8

#from affiche_arbre import *

from saisie import *


oper = ['+', '-', '*', '/', '**', '%']


################################################################################

def has_double_knot(t):
    """renvoie un booleen indiquant si l'arbre ne contient que des noeuds
    doubles'"""
    if t:# si l'arbre n'est pas vide
        if t.G == None and t.D == None:
            return True
        elif t.G != None and t.D != None:# un seul fils ou aucun
            return has_double_knot(t.G) and has_double_knot(t.D)
        else:
            return False
    return False

def has_double_knot_v2(t):
    """renvoie un booleen indiquant si l'arbre ne contient que des noeuds
    doubles'"""
    if t:# si l'arbre n'est pas vide
        if (t.G == None and t.D) or (t.G and t.D == None):
            return False
        elif t.G != None and t.D != None:# un seul fils ou aucun
            return has_double_knot(t.G) and has_double_knot(t.D)
    return True


def right_expr(t):
    """NE MARCHE PAS avec un and 3e if"""
    if t:# si l'arbre n'est pas vide
        if t.G == None and t.D == None:# si aucun fils
            if isinstance(t.val, str):# qu est ce qui n est pas valide ?
                return True
            return False
        elif t.val in oper:# s'il reste des fils
            return right_expr(t.G) & right_expr(t.D)
    return False

def is_expr(t):
    return has_double_knot_v2(t) and right_expr(t)

def parcours_profondeur(a):
    """parcours en profondeur d'un arbre
    l'objet passe en parametre doit bien etre un arbre"""
    if a != None:
        print a.val,
        parcours_profondeur(a.G)
        print a.val,
        parcours_profondeur(a.D)
        print a.val,

def parcours_prefixe(a):
    """parcours d'un arbre en ordre prefixe"""
    if a != None:
        print a.val,
        parcours_prefixe(a.G)
        parcours_prefixe(a.D)

def parcours_symetrique(a):
    """parcours d'un arbre en ordre symetrique"""
    if a != None:
        parcours_symetrique(a.G)
        print a.val,
        parcours_symetrique(a.D)

def parcours_symetrique_parentheses(a):
    """parcours d'un arbre en ordre symetrique"""
    if a != None:
        if a.val == '*' or a.val == '-' or a.val == '/' or a.val == '**':
            print "(",
        parcours_symetrique(a.G)
        print a.val,
        parcours_symetrique(a.D)
        if a.val == '*' or a.val == '-' or a.val == '/' or a.val == '**':
            print ")"


def parcours_suffixe(a):
    """parcours d'un arbre en ordre suffixe"""
    if a != None:
        parcours_suffixe(a.G)
        parcours_suffixe(a.D)
        print a.val,


def tree_fusion_with_operand(e1, e2, op):
    """return a tree representing the expression e1 op e2"""
    if op not in oper or not ((is_expr(e1) and is_expr(e2))):
        return None
    else:
        return Arbre(op, e1, e2)


def replace_values(e, xa):
    """replace in the arithmetical expression the variables by their value 
    listed in xa
    We can assume that e is a well-formed expression tree
    on suppose que e est bien formée -- donc non vide, entre autres """
    if e.D == None and e.G == None:
        for value in xa:# on parcourt la liste de couples
            if e.val in value:# si jamais une variable correspond
                e.val = value[1]# on change avec la valeur correpsondante
    else:# si e n'est pas une feuille
        e.G = replace_values(e.G, xa)# on fait de meme sur les enfants
        e.D = replace_values(e.D, xa)
    return e


# A VERIFIER
def value_of_expression(e, value):
    """on suppose que l'expression est sans variable
    1/0 a exclure; 0**0 a exclure"""
    if e.val in oper:# si c'est un operateur
        op1 = value_of_expression(e.G, value)
        op2 = value_of_expression(e.D, value)
        if e.val == '+':
            return value + op1 + op2
        elif e.val == '-':
            return value + op1 - op2
        elif e.val == '*':
            return value + (op1 * op2)
        elif e.val == '**':
            if op1 == 0 and op2 == 0:
                raise Exception("0 puissance 0")
            else:
                return value + (op1 ** op2)
        elif e.val == '/':
            if op1 == 1 and op2 == 0:
                raise Exception("Division par 0")
            else:
                return value + (op1 / op2)
    else:# la valeur est une constante
        return int(e.val)
    return value

def derivative(t, x):
    if t.val in oper:# si c'est un operateur
        if t.val == '**' and t.G.val == x:
            return Arbre('*', Arbre(t.D.val, None, None), Arbre(t.val, Arbre('x', None, None), Arbre(int(t.D.val) - 1, None, None)))
        elif t.val == '*' and t.D.val == x:
            return Arbre(t.G.val, None, None)
        else:
            return Arbre(t.val, derivative(t.G, x), derivative(t.D, x))
    else:
        if t.val == x:
            return Arbre(1, None, None)
        else:# la valeur est une constante
            return Arbre(0, None, None)



################################################################################

def main():
    #treeDrawer = TreeDrawer()
    t = entrerArbre(1)
    t2 = entrerArbre(1)
    #treeDrawer.dessiner_arbre(t)

    parcours_symetrique_parentheses(t)
    parcours_symetrique_parentheses(t2)
    op = raw_input("\nEntrez l'operateur : ")
    t3 = tree_fusion_with_operand(t, t2, op)
    #treeDrawer.dessiner_arbre(t3)
    parcours_symetrique_parentheses(t3)
    xa = [['a',1],['b', 2]]
    #t4 = replace_values(t3, xa)
    t5 = derivative(t3, 'x')
    parcours_symetrique_parentheses(t5)

    #treeDrawer.dessiner_arbre(t4)
    #print " = ", value_of_expression(t4, 0)
    
    #treeDrawer.wait()

################################################################################

main()


