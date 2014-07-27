class KesirOlustur():
    
    def __init__(self):
        self.pay=0
        self.payda=0
        
    def Olustur(self):
        self.pay = input("pay: ")
        self.payda = input("payda: ")
        print (self.pay,"/",self.payda)
        
kesir=KesirOlustur()
