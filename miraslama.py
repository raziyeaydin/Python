#!/usr/bin/env python
#-*- coding:utf8 -*-

class Oyun:
    def __init__(self):
        self.enerji=50
        self.para=100
        self.fabrika=4
        self.isci=10
        
    def goster(self):
        print"enerji:",self.enerji
        print"para:",self.para
        print"fabrika:",self.fabrika
        print"isci:",self.isci

    def fabrikakur(self,miktar):
        if self.enerji>3 and self.para>10:
            self.enerji=self.enerji-3*miktar
            self.para=self.para-10*miktar
            self.fabrika=self.fabrika+miktar
            self.isci=self.isci+5*miktar
            print miktar, "adet fabrikaniz kuruldu."
            print "TEBRiKLER!!!!"
        else :
            print "yeni fabrika kuramazsiniz."
            
macera=Oyun()

class Dusman(Oyun):
    pass
dsman=Dusman()
