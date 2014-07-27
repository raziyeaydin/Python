def sirala(dizi):
    k=len(dizi)-1
    for a in range(k):
        for i in range(a):
            if dizi[i]>dizi[i+1] :
                dizi[i],dizi[i+1]=dizi[i+1],dizi[i]
    return dizi
