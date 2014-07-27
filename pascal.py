import doctest
def fk(j): # �ncelikle bir fakt�riyel hesaplay�c�m�z olmal�
    i = j # girilen de�erden i isimli bir kopya olu�tural�m
    while True: # do�ru oldu�u s�rece d�ng�ye gir
        i -= 1 # her defas�nda i de�erini 1 eksilt
        j = i * j # j ile son i de�erini �arp ve yeni j de�erini olu�tur
        if i <= 1: # e�er i de�eri 1 'e ula�t� ise
            break # d�ng�den ��kmal� art�k
        if j==0: # e�er j ba�tan 0 a e�it ise fakt�riyel hesab� gere�i
            j=1 # fk(0) 'i 1 e e�itle
    return j # ve fakt�riyelin sonucunu d�nd�r

def pascal(m): # �imdi as�l fonksiyonumuza gelelim
    """\
    >>> pascal(5)
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    """
    liste=[] # bo� bir liste olu�turuyoruz
    n=m # girilen arg�man�n bir kopyas�n� olu�turuyoruz
    i , j =0 , 0 # i ve j ad�nda 0 de�erlerinde de�i�kenler olu�turduk
    while j<=i: # j, i den k���k veya e�it oldu�u s�rece d�ng�deyiz
        a=fk(i)/( fk(i-j)*fk(j) ) # i de�erinin kombinasyonunu ald�k ve a ya e�itledik
        liste.append(a) # listeye bu a de�erini ekledik
        j += 1 # j de�erini 1 art�rd�k
        if j == i+1: # e�er j i de�erinin 1 fazlas�na e�it oldu�unda
            i += 1
            j = 0
            print " "*n , liste # buraya dikkat n say�s� burada �ok i�imize yar�yor!!
            n -= 1
            liste=[]
            if i==m: # i de�erimiz m de�erimize e�it oldu�unda
                break # art�k i�i b�rakal�m
doctest.testmod()
