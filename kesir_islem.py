# -*- coding: cp1254 -*-

class Kesiryap():
    def __init__(self):
        self.pay1=0
        self.payda1=0
        self.pay2=0
        self.payda2=0
        
    def yap(self):
        self.pay1=input("pay� giriniz: ")
        self.payda1=input("payday� girin: ")
        print "yazd���n�z ilk kesir...."
        print self.pay1,"/",self.payda1

        self.pay2=input("pay� giriniz: ")
        self.payda2=input("payday� girin: ")
        print "yazd���n�z ikinci kesir...."
        print self.pay2,"/",self.payda2

    def islem(self):
        print "1....TOPLAMA"
        print "2....�IKARMA"
        print "3....�ARPMA"
        print "4....B�LME"
        a=input("yapaca��n�z i�lemin kodunu girin")
        if (a==1):
            print "toplama i�lemi yap�lacak"
            b = self.pay1*self.payda + self.pay2*self.payda1
            c = self.payda1*self.payda2
            print b,"/",c
        elif(a==2):
            print "��karma i�lemi yap�lacak"
            b = self.pay1*self.payda2 - self.pay2*self.payda1
            c = self.payda1*self.payda2
            print b,"/",c
        elif(a==3):
            print "�arpma i�lemi yap�lacak"
            b = self.pay1*self.pay2
            c = self.payda1*self.payda2
            print b,"/",c
        else :
            print "b�lme i�lemi yap�lacak"
            b = self.pay1*self.payda2
            c = self.payda1*self.pay2
            print b,"/",c


            
kesir=Kesiryap()
