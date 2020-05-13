def operations_possibles(tirage):
    """ Operations :  renvoyant une liste de tuples(x, op, y, res) où x et y
        sont des valeurs du tirage, op est le caractère correspondant à
        une opération ('+', '-', '*' ou '/') et res est le résultat de
        l’opération x op y. """
    #On vérifie que tout les nombres sont positifs.
    for chiffre in tirage :
        if chiffre < 0 :
            return False
    op = ["+","-","*","/"]
    lst = []
    for i in range(0,len(tirage)) : # Parcoure le tirage de 0 jusqu'à la longueur du tirage.
        for j in range(i+1,len(tirage)) : # Parcoure le tirage de i+1 jusqu'à la longueur du tirage.
            x, y = tirage[i], tirage[j] # Affectation des valeurs.
            if x != 0 : 
                if y != 0 : 
                    res = x + y
                    if res != 0 :
                        lst.append((x, op[0], y, res))
                    if x != 1 :
                        if y != 1 :
                            res = x * y
                            lst.append((x, op[2], y, res))
                    if x >= y : #Si x >= y alors les seules opérations possibles sont - et /.
                        res = x - y
                        if res != 0 :
                            lst.append((x, op[1], y, res))
                        if y != 1 :
                            # Si la division réelle donne le même resultat que la division euclidienne alors le resultat est un entier.
                            if float(x // y) == (x/y) : 
                                res = x // y
                                if res != 0:
                                    lst.append((x, op[3], y, res)) # On peut ajouter cette opération à la liste.
                    else :
                        res = y - x
                        if res != 0 :
                            lst.append((y, op[1], x, res))
                        if x != 1 :
                            # Si la division réelle donne le même resultat que la division euclidienne alors le resultat est un entier.
                            if float(y // x) == (y / x):
                                res = y // x
                                if res != 0 :
                                    lst.append((y, op[3], x, res)) # On peut ajouter cette opération à la liste. 
    return lst
#print(operations_possibles([1, 2, 3, 4]))

def suites_possibles(tirage):
    """ Recherche exhaustive : renvoye la liste de tous les couples
        (suite_d_operations, nombres) tels que suite_d_operation est une liste
        d’opérations possibles depuis tirage, et nombres est la liste de nombres
        obtenue après avoir effectué cette suite d’opérations. """
    liste_finale = []
    liste_d_operations_possibles = operations_possibles(tirage)
    # Condition d'arrêt : si le tirage contient moins de deux nombres.
    if len(tirage) < 2 :
        return []
    else : # Sinon :
        # Pour chaque opération possible depuis le tirage
        for i in range(len(liste_d_operations_possibles)):
            new_tirage = tirage*1
            # Calculer la liste de nombres obtenue en effectuant l’opération ;
            for x in range(len(new_tirage)):
                if new_tirage[x] == liste_d_operations_possibles[i][0]:
                    new_tirage.pop(x)
                    break
            for y in range(len(new_tirage)):
                if new_tirage[y] == liste_d_operations_possibles[i][2]:
                    new_tirage.pop(y)
                    break
            new_tirage = [liste_d_operations_possibles[i][3]] + new_tirage
            # Chercher toutes les suites possibles à partir de cette nouvelle liste de nombres ;
            liste_suites_possibles = suites_possibles(new_tirage)
            liste_finale = liste_finale + [([liste_d_operations_possibles[i]], new_tirage)]
            # En déduire la liste des suites possibles depuis le tirage courant (sans oublier d’inclure la suite déjà obtenue).
            for j in range(len(liste_suites_possibles)):
                operation_suivante, resultat_suivant = liste_suites_possibles[j]
                operation_suivante = [liste_d_operations_possibles[i]] + operation_suivante
                liste_finale = liste_finale + [(operation_suivante, resultat_suivant)]
    return liste_finale

#print(suites_possibles([1,2,3,4]))

def solutions(tirage,cible) :
    """ Solutions exactes : renvoie la liste des suites d’opérations permettant
        d’atteindre exactement le résultat cible. """
    lst_suit_op = []
    # On crée une liste de toutes les opérations possibles sur le tirage.
    liste_complete = suites_possibles(tirage)
    for i in range(len(liste_complete)): # On parcoure la liste.
        # On crée une variable qui correspond à la longueur - 1, du première élement (tuple) du i-ème élement de la liste qui contient toutes les opérationds possibles du tirage.
        # C'est a dire la position du dernier tuple du i-ème element de la liste. 
        k = len(liste_complete[i][0])-1
        # Si le dernier element du k-ème element, du premier element, du i-ème element de la liste qui contient toutes les opérationts possibles,
        # c'est-à-dire, si le résultat de la dernière opération est identique à cible alors on ajoute a la liste, la liste du premiere élèment
        # du i-ème element de la liste qui contient toutes les opérationds possibles, c'est-à-dire la liste qui contient tout les tuples, donc toutes
        # les opérations qui aboutissent au résultat.
        if liste_complete[i][0][k][3]  == cible :
            lst_suit_op = lst_suit_op + [liste_complete[i][0]]
    # Partie trie
    n = len(lst_suit_op)
    for i in range(0, n-1): # Parcours de chaque élément de la liste.
        for j in range(n-1, i, -1): # On fait remonter la "bulle" dans la portion non triée.
            if len(lst_suit_op[j-1]) > len(lst_suit_op[j]): # Comparaison des voisins.
                lst_suit_op[j-1], lst_suit_op[j] = lst_suit_op[j], lst_suit_op[j-1] # Echange des voisins mal ordonnés.
    return lst_suit_op

#print(solutions([1,2,3,4],24))

#########################################################
###############PROGRAMME PRINCIPALE######################
#########################################################


chaine = input() # Entrée d'une chaine de plusieurs nombres.
tirage = []
for caractere in chaine : # Parcours de la chaine.
    # On ajoute à la liste uniquement les nombres de la chaine qui sont convertis en entier.
    if caractere != " ": 
        tirage.append(int(caractere))
    # La chaine de caractére entrée par l'utilisateur est maintenant convertie en liste.
cible = int(input()) # Entrée du résultat cherché.
sol = solutions(tirage,cible) # Création d'une liste qui contient toutes les opérations qui ont pour résultat le nombre cherché.

chaine=""
for elem in sol : # Parcours des éléments de la liste qui sont eux-même des listes.
    for tuples in elem : # Parcours de chaques tuple dans les éléments.
        for i in range(len(tuples)) : # Parcours de chaque élément dans les tuples.
            if i == len(tuples) - 1 : # Si on arrive au dernier élément du tuple.
                chaine+="=" # Alors on ajoute "=" car le nombre à l'indice i est le résultat de l'opération éffectué.
            chaine+=str(tuples[i]) # On ajoute le i-ème élément de la liste converti en chaîne de caractère.
        chaine +=" "
    chaine += "\n" # On passe au prochaine élément donc on saute une ligne.
print(chaine)
