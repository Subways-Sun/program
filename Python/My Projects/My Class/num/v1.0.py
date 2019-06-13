class num:
    """
    class num

    Creator: Subway
    Version: 1.0
    
    A class used to deal with number problems.
    """
    def __init__(self,ipt):
        self.ipt=ipt
    def sep(self):
        """
        Separate numbers from strings. (Positive numbers ONLY)

        Example:
        >>> a='1,2,3,4,5'
        >>> b=num.ipt(a)
        >>> c=b.sep()
        >>> c
        [1, 2, 3, 4, 5]
        """
        data=[]
        findCommaPosition=-1
        try:
            i=0
            for j in self.ipt:
                a=int(self.ipt[i])
                i=i+1
        except ValueError:
            b=self.ipt[i]
        for i in self.ipt:
            commaPositionBefore=findCommaPosition+1
            findCommaPosition=self.ipt.find(b,findCommaPosition+1)
            if findCommaPosition>=0:
                commaPositionNext=findCommaPosition
            else:
                commaPositionNext=None
            everyDigitOfNumber=list(self.ipt[commaPositionBefore:commaPositionNext])
            everyDigitOfNumber.reverse()
            everyNumber=0
            index=-1
            stepOfEachNumber=[]
            while True:
                index=index+1
                everyNumber=everyNumber+int(everyDigitOfNumber[index])*10**index
                stepOfEachNumber.append(everyNumber)
                if len(stepOfEachNumber)==len(everyDigitOfNumber):
                    break
            data.append(stepOfEachNumber[-1])
            if findCommaPosition==-1:
                break
        return data
