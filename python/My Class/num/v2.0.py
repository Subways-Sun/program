class str:
    """
    class num

    Creator: Subway
    Version: 2.0
    
    A class used to deal with number problems.
    """
    def __init__(self,str):
        self.str=str
    def __add__(self,other):
        return
    def sep(self):
        """
        Separate numbers from strings.

        Example:
        >>> a='1,2,3,4,5'
        >>> b=num.str(a)
        >>> c=b.sep()
        >>> c
        [1, 2, 3, 4, 5]
        """
        data=[]
        findCommaPosition=-1
        findMinusPosition=-1
        try:
            everyMinus=self.str.find('-')
            if everyMinus==-1:
                del findMinusPosition,everyMinus    
            i=0
            for j in self.str:
                a1=self.str[i]
                i=i+1
                if a1=='-':
                    continue
                a2=int(a1)
        except ValueError:
            b=self.str[i-1]
        try:
            for i in self.str:
                commaPositionBefore=findCommaPosition+1
                findCommaPosition=self.str.find(b,findCommaPosition+1)
                if findCommaPosition>=0:
                    commaPositionNext=findCommaPosition
                else:
                    commaPositionNext=None
                everyDigitOfNumber=list(self.str[commaPositionBefore:commaPositionNext])
                minusExist=0
                if '-' in everyDigitOfNumber:
                    everyDigitOfNumber.remove('-')
                    minusExist=1
                everyDigitOfNumber.reverse()
                everyNumber=0
                index=-1
                stepOfEachNumber=[]
                while True:
                    index=index+1
                    everyNumber=everyNumber+int(everyDigitOfNumber[index])*10**index
                    if minusExist==1:
                        everyNumber=everyNumber*(-1)
                    stepOfEachNumber.append(everyNumber)
                    if len(stepOfEachNumber)==len(everyDigitOfNumber):
                        break
                data.append(stepOfEachNumber[-1])
                if findCommaPosition==-1:
                    break
        except UnboundLocalError:
            print("\nPlease enter at least 2 numbers.")
        return data
