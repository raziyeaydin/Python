def bubbleSort(dizi):
    for k in range(len(dizi)-1,0,-1):
        for a in range(k):
            if dizi[a] > dizi[a+1] :
                dizi[a],dizi[a+1]=dizi[a+1],dizi[a]
    return dizi
        
