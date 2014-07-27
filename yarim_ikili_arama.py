def ikili(liste,sayi):
    first=0
    last=len(liste)-1
    found= False
    while first <= last and not found :
        indis=0
        middle=(len(liste)+1)/2.0
        if sayi >= first and sayi <= middle :
            last=middle
            if sayi==liste[indis]            
            found=False
