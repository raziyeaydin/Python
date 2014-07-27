class Polinom():
    def __init__(self):
        self.pol1=0
        self.pol2=0
        
    def terim(self):
        self.a1=input("3.derece deðiþkenin katsayýsý: ")
        self.a2=input("2.derece deðiþkenin katsayýsý: ")
        self.a3=input("1.derece deðiþkenin katsayýsý: ")
        self.a4=input("0.derece deðiþkenin katsayýsý: ")

        print("ilk polinomunuz .....")
        print(self.a1,"x^3+",self.a2,"x^2+",self.a3,"x+",self.a4)

        self.b1=input("3.derece deðiþkenin katsayýsý: ")
        self.b2=input("2.derece deðiþkenin katsayýsý: ")
        self.b3=input("1.derece deðiþkenin katsayýsý: ")
        self.b4=input("0.derece deðiþkenin katsayýsý: ")

        print("ikinci polinomunuz .....")
        print(self.b1,'x^3+',self.b2,'x^2+',self.b3,'x+',self.b4)

    def topla(self):
        self.c1=self.a1+self.b1
        self.c2=self.a2+self.b2
        self.c3=self.a3+self.b3
        self.c4=self.a4+self.b4

        print("iki polinomun toplamý .....")
        print(self.c1,"x^3+",self.c2,"x^2+",self.c3,"x+",self.c4)

    def cikar(self):
        self.d1=self.a1-self.b1
        self.d2=self.a2-self.b2
        self.d3=self.a3-self.b3
        self.d4=self.a4-self.b4

        print("iki polinomun farký .....")
        print(self.d1,"x^3+",self.d2,"x^2+",self.d3,"x+",self.d4)

pol=Polinom()
        
        
        
