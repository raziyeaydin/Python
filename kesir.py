class Kesiryap():
    def __init__(self):
        self.pay=0
        self.payda=0
        
    def yap(self):
        self.pay=input("payı giriniz: ")
        self.payda=input("paydayı girin: ")

        print "yazdığınız kesir...."
        print self.pay+("/")+self.payda

kesir=Kesiryap()

