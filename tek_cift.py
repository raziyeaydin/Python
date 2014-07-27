def tek_cift(sayi):
    sayi=str(sayi)
    for i in sayi:
        cift_liste=[]
        tek_liste=[]
        i=int(i)
        if i%2==0 :
            cift_liste.append(i)
            return cift_liste
