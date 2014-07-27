import doctest
def fk(j): # öncelikle bir faktöriyel hesaplayýcýmýz olmalý
    i = j # girilen deðerden i isimli bir kopya oluþturalým
    while True: # doðru olduðu sürece döngüye gir
        i -= 1 # her defasýnda i deðerini 1 eksilt
        j = i * j # j ile son i deðerini çarp ve yeni j deðerini oluþtur
        if i <= 1: # eðer i deðeri 1 'e ulaþtý ise
            break # döngüden çýkmalý artýk
        if j==0: # eðer j baþtan 0 a eþit ise faktöriyel hesabý gereði
            j=1 # fk(0) 'i 1 e eþitle
    return j # ve faktöriyelin sonucunu döndür

def pascal(m): # þimdi asýl fonksiyonumuza gelelim
    """\
    >>> pascal(5)
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]
    """
    liste=[] # boþ bir liste oluþturuyoruz
    n=m # girilen argümanýn bir kopyasýný oluþturuyoruz
    i , j =0 , 0 # i ve j adýnda 0 deðerlerinde deðiþkenler oluþturduk
    while j<=i: # j, i den küçük veya eþit olduðu sürece döngüdeyiz
        a=fk(i)/( fk(i-j)*fk(j) ) # i deðerinin kombinasyonunu aldýk ve a ya eþitledik
        liste.append(a) # listeye bu a deðerini ekledik
        j += 1 # j deðerini 1 artýrdýk
        if j == i+1: # eðer j i deðerinin 1 fazlasýna eþit olduðunda
            i += 1
            j = 0
            print " "*n , liste # buraya dikkat n sayýsý burada çok iþimize yarýyor!!
            n -= 1
            liste=[]
            if i==m: # i deðerimiz m deðerimize eþit olduðunda
                break # artýk iþi býrakalým
doctest.testmod()
