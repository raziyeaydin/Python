def arama(liste,sayi):
    first=0
    last=len(liste)-1
    found=False

    while first<=last and not found :
        midpoint=(last+first)/2  
        for i in range(first,midpoint): 
            if liste[i]==sayi :
                found=False
            else:
                midpoint=midpoint+1

        for i in range(midpoint,last):
            if sayi==liste[i]:
                found=True
    return found
