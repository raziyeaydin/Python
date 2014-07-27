#class Stack :
 #   def __init__(self):
   #     self.item=[]
    #def ...


    
def parChecker(symbolString):
    s=Stack()

    balanced=True
    index=0

    while index<len(symbolString) and balanced :
        sembol=symbolString[index]

        if sembol=='(' :
            s.push(sembol)
        else:

            if s.isEmpty() :
                balanced=False
            else:
                s.pop()
        index=index+1
    if s.isEmpty() and balanced :
        return True
    else:
        return False
            
