def atlamali(liste):
    dizi=[]
    for i in range(0,len(liste),2):
        dizi.append(liste[i])

    for k in range(0,len(dizi)-1,1): # len(dizi)-1 dememizin nedeni aþaðýdaki dizi[k+1] ifadesinin k=len(dizi) olduðunda range aralýðýnda olmamasý
        buyuk=dizi[k]

        if buyuk < dizi[k+1]:

            buyuk=dizi[k+1]

    print"dizinin buyuk sayisi..."

    return buyuk
