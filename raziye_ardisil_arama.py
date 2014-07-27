def arama(liste,sayi):

    indis=0
    sonuc = False

    while indis<len(liste) and not sonuc :
        
        if liste[indis]==sayi :
            sonuc = True
            
        else:
            indis= indis+1

    return sonuc
