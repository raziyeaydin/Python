# -*- coding: cp1254 -*-

class Kesiryap():
    def __init__(self):
        self.pay1=0
        self.payda1=0
        self.pay2=0
        self.payda2=0
        
    def yap(self):
        self.pay1=input("payı giriniz: ")
        self.payda1=input("paydayı girin: ")
        print "yazdığınız ilk kesir...."
        print self.pay1,"/",self.payda1

        self.pay2=input("payı giriniz: ")
        self.payda2=input("paydayı girin: ")
        print "yazdığınız ikinci kesir...."
        print self.pay2,"/",self.payda2

    def islem(self):
        print "1....TOPLAMA"
        print "2....ÇIKARMA"
        print "3....ÇARPMA"
        print "4....BÖLME"
        a=input("yapacağınız işlemin kodunu girin")
        if (a==1):
            print "toplama işlemi yapılacak"
            b = self.pay1*self.payda + self.pay2*self.payda1
            c = self.payda1*self.payda2
            print b,"/",c
        elif(a==2):
            print "çıkarma işlemi yapılacak"
            b = self.pay1*self.payda2 - self.pay2*self.payda1
            c = self.payda1*self.payda2
            print b,"/",c
        elif(a==3):
            print "çarpma işlemi yapılacak"
            b = self.pay1*self.pay2
            c = self.payda1*self.payda2
            print b,"/",c
        else :
            print "bölme işlemi yapılacak"
            b = self.pay1*self.payda2
            c = self.payda1*self.pay2
            print b,"/",c


            
kesir=Kesiryap()
