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

def create_bst(numbers):
    """create a bst from a list"""
    if numbers:
        bst = Arbre(numbers.pop(0), None, None)
        for i in numbers:
            insert_leaf(bst, i)
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


def search_v2(bst, x):
    courant = bst
    while courant:
        if bst.val == x:
            return courant
        elif bst.val < x:
            courant = courant.D
        else:
            courant = courant.G

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

def search_depth(bst, x, p):
    if bst:
        if bst.val == x:
            return bst, p - 1
        elif bst.val > x:
            return search_depth(bst.G, x, p + 1)
        else:
            return search_depth(bst.D, x, p + 1)
    else:
        return bst, p - 1

def occurence(bst, x):
    if bst:
        if bst.val == x:
            return 1 + occurence(bst.G, x) + occurence(bst.D, x)
        elif bst.val > x:
            return occurence(bst.G, x)
        else:
            return occurence(bst.D, x)
    else:
        return 0

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
    elif bst.D == None:
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
    #bst = input_bst()
    liste = [1,2,4,5,0,3,4,1,9,3,2]
    bst = create_bst(liste)
    #parcours_prefixe(bst)
    treeDrawer.dessiner_arbre(bst)
    search(bst, 2)
    search_v2(bst, 2)
    a, p = search_depth(bst, 2, 0)
    print "PROFONDEUR : ", p
    occ = occurence(bst, 2)
    print "OCCURENCE : ", occ
    ascending_order(bst)
    print "SECONDE CLEF PLUS GRANDE : ", second_key(bst)
    bst = insert_leaf(bst, int(raw_input("ENTER A NUMBER : ")))
    treeDrawer.dessiner_arbre(bst)
    bst = delete(bst, int(raw_input("ENTER A NUMBER : ")))
    treeDrawer.dessiner_arbre(bst)
    treeDrawer.wait()





################################################################################

main()
