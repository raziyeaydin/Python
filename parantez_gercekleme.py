class Stack():
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return self.item==[]
    def push(self,item):
        return self.item.append(item)
    def pop(self):
        return self.item.pop()
    def peek(self):
        return self.item[len(self.item)-1]
    def size(self):
        return len(self.item)
    
    def parChecker(sembolkatari):

            balanced=True
            index=0

            while index<len(sembolkatari) and balanced :
                sembol=sembolkatari[index]

                if sembol=='(' :
                    s.push(sembol)
                else:
                    if s.isEmpty():
                        balanced=False
                    else:
                        s.pop()
                        index=index+1
            if balanced and s.isEmpty():
                return True
            else :
                return False
s=Stack()
