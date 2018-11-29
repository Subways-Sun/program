class num:
    """
    class num

    Creator: Subway
    Version: 3.0
    
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
        try:
            everyMinus=self.str.find('-')
            if everyMinus==-1:
                del everyMinus
            everyDecimal=self.str.find('.')
            if everyDecimal==-1:
                del everyDecimal
            i=0
            for j in self.str:
                a1=self.str[i]
                i=i+1
                if a1=='-' or a1=='.':
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
                decimalExist=0
                if '-' in everyDigitOfNumber:
                    everyDigitOfNumber.remove('-')
                    minusExist=1
                everyDigitOfNumber.reverse()
                if '.' in everyDigitOfNumber:
                    decimalPosition=everyDigitOfNumber.index('.')
                    everyDigitOfNumber.remove('.')
                    decimalExist=1
                if everyDigitOfNumber.count('-')>1:
                    raise AssertionError
                if everyDigitOfNumber.count('.')>1:
                    raise ArithmeticError
                everyNumber=0
                index=-1
                stepOfEachNumber=[]
                while True:
                    index=index+1
                    everyNumber=everyNumber+int(everyDigitOfNumber[index])*10**index
                    stepOfEachNumber.append(everyNumber)
                    if len(stepOfEachNumber)==len(everyDigitOfNumber):
                        number=stepOfEachNumber[-1]
                        if minusExist==1:
                            number=number*(-1)
                        if decimalExist==1:
                            number=number/(10**decimalPosition)
                        break
                data.append(number)
                if findCommaPosition==-1:
                    break
        except ArithmeticError:
            print("\nMore than 1 decimal points in a number.")
        except AssertionError:
            print("\nMore than 1 minus symbols in a number.")
        except UnboundLocalError:
            print("\nPlease enter at least 2 numbers.")
        return data
