# Diese Funktion tauscht zwei Variabeln aus einer Liste--> input: Liste Index1, Index2
def swap(liste, index1, index2):
    if (index1 >= 0 and index2 >= 0 and index1 < len(liste) and index2 < len(liste)) :
        liste[index1], liste[index2] = liste[index2], liste[index1]
    else:
        print("NONONOOO I can not swap that!")


'#---------------------------------------------------------------------------------------------------------------------'
# Diese Funktion sorttiert die Ihr gegebenen Liste --> input: Liste
def bubblesort (list):
    didswap = True

    while (didswap) :
        didswap = False

        for i in range(1, len(list)) :

            if (list[i - 1] > list[i]) :
                swap(list, i - 1, i)
                didswap = True