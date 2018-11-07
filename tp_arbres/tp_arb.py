#coding: utf-8
# REPAIN Paul
# DUT INFO

from affiche_arbre import *
from saisie import *


################################################################################


def input_bst():
    """let the user input the values for a bst"""
    bst = Arbre(None, None, None)
    inp = input("Value : ")
    if inp != "":
        bst.val = inp
        inp = input("Value : ")
        while inp != "":
            insert_leaf(bst, inp)
            inp = input("Value : ")
    return bst

def create_bst(numbers):
    """create a bst from a list"""
    if numbers:
        bst = Arbre(numbers.pop(0), None, None)
        for i in numbers:
            insert_leaf(bst, i)
        return bst

def search(bst, x):
    """search the value x in a binary search tree bst
    recursive version"""
    if bst:
        if bst.val == x:
            return bst
        if bst.val < x:
            return search(bst.D, x)
        else:
            return search(bst.G, x)


def search_v2(bst, x):
    """searches an element x in a bst
    iterative version"""
    courant = bst
    while courant:
        if bst.val == x:
            return courant
        elif bst.val < x:
            courant = courant.D
        else:
            courant = courant.G

def insert_leaf(bst, x):
    """insert a leaf in a bst, with the value x
    recursive version"""
    if bst == None:
        return create_leaf(x)
    else:
        if bst.val >= x:
            bst.G = insert_leaf(bst.G, x)
        else:
            bst.D = insert_leaf(bst.D, x)
    return bst

def insert_leaf_v2(bst, x):
    """insert a leaf in a bst, with the value x
    iterative version"""
    if not bst:
        return create_leaf(x)
    courant = bst
    temp = courant
    while courant:
        print "TEMP : ", temp
        print "COURANT : ", courant
        temp = courant
        if courant.val >= x:
            courant = courant.G
        else:
            courant = courant.D
    if temp and temp.val >= x:
        temp.G = create_leaf(x)
    else:
        temp.D = create_leaf(x)
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
    """searches an element x in a bst, and returns the depth in which is the
    knot"""
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
    """returns the number of occurences of x in bst"""
    if bst:
        if bst.val == x:
            return 1 + occurence(bst.G, x) + occurence(bst.D, x)
        elif bst.val > x:
            return occurence(bst.G, x)
        else:
            return occurence(bst.D, x)
    else:
        return 0

def delete_all_occurences(bst, x):
    """deletes all occurences of x in bst"""
    if bst:
        if bst.val == x:
            bst = delete_root(bst)
        bst.G = delete_all_occurences(bst.G, x)
        bst.D = delete_all_occurences(bst.D, x)
    return bst

def interval(bst, x, y):
    """returns the number of elements which are between x and y"""
    if bst:
        if bst.val >= x and bst.val < y:
            return 1 + interval(bst.G, x, y) + interval(bst.D, x, y)
        else:
            return interval(bst.G, x, y) + interval(bst.D, x, y)
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

def delete_v2(bst, x):
    """deletes an element x from a bst
    iterative version"""
    if bst and bst.val == x:
        return delete_root(bst)
    elif bst:
        courant = bst
        temp = courant
        while courant and courant.val:
            temp = courant
            if courant.val < x:
                courant = courant.D
            else:
                courant = courant.G
        if courant:
            if temp.val < x:
                temp.D = delete_root(courant)
            else:
                temp.G = delete_root(courant)
    return bst


def delete_root(bst):
    """deletes the root and re arranges the bst"""
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


def subset(a, b):
    """returns True if all elements of a are also elements of b"""
    if b == None:
        return False
    if a:
        if a.val == b.val:
            return True and subset(a.G, b) and subset(a.D, b)
        if a.val > b.val:
            return subset(a, b.D) and subset(a.G, b) and subset(a.D, b)
        else:
            return subset(a, b.G) and subset(a.G, b) and subset(a.D, b)
    return True

def delete_repetitions(bst):
    """deletes redundant elements in the bst"""
    if bst:
        val = bst.val
        o = occurence(bst, bst.val)
        if o > 1:# si le nombre d'occurences > 1, il y a repetition
            for x in range(o-1):
                bst = delete(bst, val)
            if val != bst.val:
                bst = delete_repetitions(bst)
        bst.G = delete_repetitions(bst.G)
        bst.D = delete_repetitions(bst.D)
    return bst


################################################################################

class TST:
    """Implementation of Ternary Search Tree
    d = droite; g = gauche; m = milieu"""
    val = None
    g = None
    m = None
    d = None
    
    def __init__(self, value, tstG, tstM, tstD):
        self.val = value
        self.g = tstG
        self.m = tstM
        self.d = tstD

def tst_search(tst, x):
    if tst:
        if tst.val == x:
            return tst
        elif tst.val > x:
            return tst_search(tst.g, x)
        elif tst.val < x:
            return tst_search(tst.d, x)

def tst_insert(tst, x):
    if tst == None:
        return create_leaf(x)
    else:
        if tst.val > x:
            tst.g = tst_insert(tst.g, x)
        elif tst.val < x:
            tst.d = tst_insert(tst.d, x)
        else:
            tst.m = tst_insert(tst.m, x)
    return tst


def tst_delete(tst, x):
    """deletes an element x from a tst"""
    if tst:
        if tst.val == x:
            return delete_root(tst)
        else:
            if bst.val > x:
                tst.g = tst_delete(tst.g, x)
            elif tst.val < x:
                tst.d = tst_delete(tst.d, x)
    return tst

################################################################################

def main():
    treeDrawer = TreeDrawer()
    #bst = input_bst()
    liste = []
    bst = create_bst(liste)
    #parcours_prefixe(bst)
    treeDrawer.dessiner_arbre(bst)
    #
    search(bst, 2)
    search_v2(bst, 2)
    #
    a, p = search_depth(bst, 2, 0)
    print "PROFONDEUR : ", p
    #
    occ = occurence(bst, 2)
    print "OCCURENCE : ", occ
    #
    n = interval(bst, 3, 5)
    print "INTERVAL = ", n
    #
    ascending_order(bst)
    print "SECONDE CLEF PLUS GRANDE : ", second_key(bst)
    #
    #bst = insert_leaf_v2(bst, input("ENTER A NUMBER : "))
    #treeDrawer.dessiner_arbre(bst)
    #
    bst = delete_v2(bst, input("ENTER A NUMBER : "))
    #
    treeDrawer.dessiner_arbre(bst)
    treeDrawer.wait()

def main2():
    treeDrawer = TreeDrawer()
    #bst = input_bst()
    liste = [1, 0, 2, 5, 0, 1, 3]
    bst = create_bst(liste)
    #
    treeDrawer.dessiner_arbre(bst)
    #
    #bst = delete(bst, 1)
    bst = delete_all_occurences(bst, 1)
    bst = delete_all_occurences(bst, 1)
    #
    #treeDrawer.dessiner_arbre(bst)
    #bst = delete(bst, 1)
    treeDrawer.dessiner_arbre(bst)
    treeDrawer.wait()

def main3():
    treeDrawer = TreeDrawer()
    liste = [2, 0,3,2,1, 2, 5, 0]
    #liste2 = [1,3,5]
    bst = create_bst(liste)
    #bst2 = create_bst(liste2)
    #
    treeDrawer.dessiner_arbre(bst)
    #treeDrawer.dessiner_arbre(bst2)
    delete_repetitions(bst)
    #
    treeDrawer.dessiner_arbre(bst)
    #print subset(bst2, bst)
    #
    treeDrawer.wait()




################################################################################

#main()
#main2()
main3()
