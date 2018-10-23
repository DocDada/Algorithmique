#coding: utf-8

from affiche_arbre import * 
from saisie import * 


################################################################################


def input_bst():
    """let the user input the values for a bst"""
    bst = Arbre(None, None, None)
    inp = raw_input("Value : ")
    if inp != "":
        bst.val = inp
        inp = raw_input("Value : ")
        while inp != "":
            insert_leaf(bst, inp)
            inp = raw_input("Value : ")
    return bst


def search(bst, x):
    """search the value x in a binary search tree bst"""
    if bst:
        if bst.val == x:
            return bst
        if bst.val < x:
            return search(bst.D, x)
        else:
            return search(bst.G, x)


def insert_leaf(bst, x):
    if bst == None:
        return create_leaf(x)
    else:
        if bst.val >= x:
            bst.G = insert_leaf(bst.G, x)
        else:
            bst.D = insert_leaf(bst.D, x)
    return bst


def create_leaf(x):
    return Arbre(x, None, None)


def parcours_prefixe(a):
    """parcours d'un arbre en ordre prefixe"""
    if a != None:
        print a.val,
        parcours_prefixe(a.G)
        parcours_prefixe(a.D)


def ascending_order(bst):
    """prints values of bst in ascending order"""
    if bst:
        ascending_order(bst.G)
        print bst.val
        ascending_order(bst.D)


def second_key(bst):
    """returns the second largest key in a bst"""
    if bst:
        if bst.D:
            if bst.D.D == None:
                if bst.D.G == None:
                    return bst.val
            return second_key(bst.D)
        elif bst.G:
            if bst.G.G == None:
                if bst.G.D == None:
                    return bst.G.val
            return second_key(bst.G)
        return bst.val

def delete(bst, x):
    """deletes an element x from a bst"""
    if bst == None:
        return bst
    if bst.val == x:
        return delete_root(bst)
    else:
        if bst.val > x:
            bst.G = delete(bst.G, x)
        else:
            bst.D = delete(bst.D, x)
        return bst


def delete_root(bst):
    if bst.G == None:
        bst = bst.D
    else:
        if bst.D == None:
            bst = bst.G
        else:
            b = bst.G
            if b.D == None:
                bst.val = b.val
                bst.G = b.G
            else:
                temp = b.D
            while temp.D != None:
                b = temp
                temp = temp.D
            bst.val = temp.val
            b.D = temp.G
    return bst

################################################################################

def main():
    treeDrawer = TreeDrawer()
    bst = input_bst()
    #parcours_prefixe(bst)
    treeDrawer.dessiner_arbre(bst)
    search(bst, 2)
    ascending_order(bst)
    print "SECONDE CLEF PLUS GRANDE : ", second_key(bst)
    bst = insert_leaf(bst, raw_input("ENTER A NUMBER : "))
    treeDrawer.dessiner_arbre(bst)
    bst = delete(bst, raw_input("ENTER A NUMBER : "))
    treeDrawer.dessiner_arbre(bst)
    treeDrawer.wait()





################################################################################

main()
