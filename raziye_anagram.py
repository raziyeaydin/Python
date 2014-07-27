def anag(s1,s2):
    alist=list(s1)
    blist=list(s2)
    
    alist.sort()
    blist.sort()
    
    durum=True

    if len(alist)!=len(blist):
        durum=False
       
    else:
        indis=0
        
        while indis<len(alist) and durum:

            if alist[indis]!=blist[indis]:
                durum=False

            else:
                indis=indis+1

        return durum
            
            
    
