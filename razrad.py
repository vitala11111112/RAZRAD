class Razrad():

    #метод(принимает список)
    def __init__(self,MyList:list[int]): 
        self.MyList = MyList
    
    #нахождение максимального разряда в списке
    def max_value_searching(self):
        max = 0
        for i in range(len(self.MyList)):
            if len(str(self.MyList[i])) > max:
                max = len(str(self.MyList[i]))
        return max
    
    #усовершенствуем все числа до максимального разряда
    def max_lvl(self,max):
        for i in range(len(self.MyList)):
            if len(str(self.MyList[i])) != max:
                diff = max-len(str(self.MyList[i]))
                self.MyList[i] = "0"*diff+str(self.MyList[i])
            else:
                self.MyList[i] = str(self.MyList[i])
        return self.MyList
    
    #реализация поразрядной сортировки
    def RAZRAAAAD(self):
        for i in range(len(self.MyList[0])-1,-1,-1):
            for j in range(len(self.MyList)):
                for k in range(j+1,len(self.MyList)):
                    if int(self.MyList[j][i]) > int(self.MyList[k][i]):
                        self.MyList[j],self.MyList[k]=self.MyList[k],self.MyList[j]
                        
        for i in range(len(self.MyList)):
            self.MyList[i] = int(self.MyList[i])
        return self.MyList


if __name__ == "__main__":
    obj = Razrad([0,768,1,6,170,12,22,222])
    obj.max_lvl(obj.max_value_searching())
    print(obj.RAZRAAAAD())
        
    