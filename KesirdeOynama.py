class KesirdeOynama():
    
    def __init__(self):
        self.pay=0
        self.payda=0
        self.sonuc=0
        
    def Olustur(self):
        self.pay = input("pay: ")
        self.payda = input("payda: ")
        self.sonuc=int(self.pay) + int(self.payda)
        print (self.pay,"/",self.payda)
        print (self.sonuc)
        
kesir=KesirOlustur()
