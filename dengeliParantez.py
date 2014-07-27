class Stack:

     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


    
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
                

sonuc=parChecker()

