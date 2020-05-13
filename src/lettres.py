# Créé par BEN HAMOUDA Amel et PEMODJO Marylin, TDa TP2 le 23/04/2016

def mot_possible(tirage, mot):
    """Anagrammes :  renvoye True si mot peut être composé
       avec les lettres de tirage, et False sinon."""
    #Si la liste "tirage" posséde un nombre de lettre inferieure a celui de "mot" alors on ne peux pas former le mot avec cette liste.
    if len(mot) > len(tirage) :
        return False
    #On compare le nombre d'occurrences de chacune des lettres apparaissant dans "mot" au nombre d'occurrences de cette lettre dans tirage.
    #Si une lettre de "mot" est présente plusieurs fois et que celle-ci n'est pas présente dans la liste le même nobre de fois..
    #..on renvoie false car on ne peux pas utiliser deux fois une même lettre de la liste.
    for lettre in mot :
        if mot.count(lettre) > tirage.count(lettre) :
            return False
    #On regarde si toutes les lettres de "mot" sont dans la liste tirage.
    #Si c'est pas le cas, alors on peut pas formet le mot avec la liste donnée donc on renvoie False
    #Sinon on renvoie True
    for lettre in mot :
        if lettre not in tirage :
            return False
    return True

def tous_mots_possibles(tirage, liste_mots):
    """Recherche exhaustive : renvoye la liste complète de tous
       les mots de liste_mots que l’on peut composer avec le tirage donné."""
    #liste_mots = []
    fichier = open('dico.txt','r')  # Ouverture du fichier texte dico en mode lecture.
    lst = fichier.readlines()   # Insertion de chaque ligne du fichier dans une liste.
    fichier.close()  # Fermeture du fichier.
    for i in range(0, len(lst)):  # Boucle commencent de 0 jusqu'à  la longueur de la liste créer juste au-dessus.
        lst[i] = lst[i].replace("\n","")  # On remplace chaque retour à la ligne par rien.
        if mot_possible(tirage, lst[i]):  # Si le mot est composée par les lettres du tirage alors ...
            liste_mots.append(lst[i])  # ...l'ajouter à une autre liste qui contiendra tout les mots possibles par rapport au tirage.
    return liste_mots  # Retouner la liste contenant tout les mots possibles.

def tri_liste(liste):
    for i in range(0,len(liste)-1) : #Boucle commence de 0 à la longeur de la liste - 1.
        for j in range(len(liste)-1,i,-1): # Parcours des n-i élements depuis la fin.
            if len(liste[j-1]) < len(liste[j]) : # Comparaison.
                liste[j-1],liste[j] = liste[j],liste[j-1] #On échange les voisins qui sont pas ordonnés
            if len(liste[j-1]) == len(liste[j]): #Si deux mot ont la même longeur on compare les lettres qui les composent.
                if liste[j-1] > liste[j]: # Comparaison.
                    liste[j-1],liste[j] = liste[j],liste[j-1] #On échange les voisins qui sont pas ordonnés.
    return liste
    
######## SI LE TIRAGE EST DEJA DONNEE C'EST SA
##mots_francais = []
##tirage = ['e', 's', 't']
##print("".join(tirage)) # On fait une jointure du tirage pour pouvoir l'afficher comme souhaiter dans le programme principal.
##liste = tous_mots_possibles(tirage, mots_francais) #doit renvoyer la liste ['es', 'est', 'et', 'se', 'set', 'te', 'tes']

####### SI LE TIRAGE DEPEND DU MOT DE L'UTILISATEUR C'EST SA
mot = input()
tirage = list(mot)
mots_francais = []
liste = tous_mots_possibles(tirage, mots_francais) #doit renvoyer la liste ['es', 'est', 'et', 'se', 'set', 'te', 'tes']
print(tri_liste(liste))# Affiche la liste dans l'ordre décroissant.
