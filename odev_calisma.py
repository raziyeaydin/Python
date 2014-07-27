# -*- coding: cp1254 -*-


class SoruCTS():
    def __init__(self):
        self.soru1="Asagidakilerden hangisi dunyanin en yuksek dagidir ?"
        self.secenek11="Mc Kinley"
        self.secenek12="Everest"
        self.secenek13="Annapurna"
        self.secenek14="Makalu"
        self.secenek15="Mauna Kea"
        
    def sor(self):
        print "SORU :",self.soru1
        print "A)",self.secenek11
        print "B)",self.secenek12
        print "C)",self.secenek13
        print "D)",self.secenek14
        print "E)",self.secenek15
        a=raw_input("cevabinizi girin:  ")
        if a=="E":
            print "TEBRiKLER  !!!"
            print "puan=1"
        else:
            print "cevabiniz...",a,"dogru cevap...E"
            print "puan=0"
s1=SoruCTS()


class SoruCCS():
    def __init__(self):
        self.soru2="Asagidaki balina familyalarindan hangileri dişsiz balina alt takimlarina aittir ?"  
        self.secenek21="Beyaz balinagiller"
        self.secenek22="Oluklu balinagiller"
        self.secenek23="Boz balinagiller"
        self.secenek24="Gagali balinagiller"
        self.secenek25="Gercek balinagiller"

    def sor(self):
        print "SORU :",self.soru2
        print "A)",self.secenek21
        print "B)",self.secenek22
        print "C)",self.secenek23
        print "D)",self.secenek24
        print "E)",self.secenek25

        print "cevaplarınızı sırasıyla girin..."
        print "cevaplarınızı yazdıktan sonra diğer cevap seçenek/seçeneklerini doldurmayın"
        b=raw_input("1.cevabiniz...")
        c=raw_input("2.cevabiniz...")
        d=raw_input("3.cevabiniz...")
        e=raw_input("4.cevabiniz...")
        f=raw_input("5.cevabiniz...")
        if (b=="B" or b=="C" or b=="E"):
            if (c=="B" or c=="C" or c=="E"):
                if (d=="B" or d=="C" or d=="E"):
                    print "TEBRiKLER !!!"
                    print "puan=3"
                else:
                    print "puan=2"
                    print "dogru cevaplar sırasıyla... B-C-E"
            else:
                print "puan=1"
                print "dogru cevaplar sırasıyla... B-C-E"
        else:
            print "puan=0"
            print "dogru cevaplar sırasıyla... B-C-E"

            
s2=SoruCCS()
