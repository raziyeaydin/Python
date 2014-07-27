def insertionSort(liste):

    for index in range(1,len(liste)):

        currentvalue=liste[index]
        position=index

        while position>0 and liste[position-1]>currentvalue:
            liste[position]=liste[position-1]
            position=position-1

        liste[position]=currentvalue

    return liste
