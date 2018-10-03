# coding: utf-8

from affiche_arbre import *

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
            if t.val in oper or isinstance(t.val, str):# qu est ce qui n est pas valide ?
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

# A VERIFIER
def replace_variable_by_value(e, xa):
    """replace in the arithmetical expression the variables by their value
    listed in xa"""
    if e:
        e_b = e
        return replace_values(e_b, xa)
    return e

# A VERIFIER
def replace_values(e, xa):
    if e:
        if e.val not in oper:
            for v in xa:
                if e.val in v:
                    e.val = v[1]
        e.G = replace_values(e.G, xa)
        e.D = replace_values(e.D, xa)
    return e

# A VERIFIER
def eval_expression(e):
    """calcule la valeur d'une expression. Les valeurs des noeuds sont des
    constantes, non des variables"""
    if e:
        return value_of_expression(e, 0)
    return 0

# A VERIFIER
def value_of_expression(e, v):
    if e:
        if e.val in oper:
            if e.val == '+':
                return v + value_of_expression(e.G, v) + value_of_expression(e.D, v)
            elif e.val == '-':
                return value_of_expression(e.G, v) - value_of_expression(e.D, v)
            elif e.val == '*':
                return value_of_expression(e.G, v) * value_of_expression(e.D, v)
            elif e.val == '/':
                return value_of_expression(e.G, v) / value_of_expression(e.D, v)
        return int(e.val)
    return v



################################################################################

def main():
    treeDrawer = TreeDrawer()
    t = entrerArbre(1)
    t2 = entrerArbre(1)
    #treeDrawer.dessiner_arbre(t)

    parcours_symetrique(t)
    parcours_symetrique(t2)
    op = raw_input("\nEntrez l'operateur : ")
    t3 = tree_fusion_with_operand(t, t2, op)
    treeDrawer.dessiner_arbre(t3)
    parcours_symetrique(t3)
    xa = [['a',1],['b', 2]]
    t4 = replace_variable_by_value(t3, xa)
    parcours_symetrique(t4)
    treeDrawer.dessiner_arbre(t4)
    print " = ", eval_expression(t4)
    
    treeDrawer.wait()

################################################################################

main()

