class Polynomial:
    def __init__(self, coeffList: list):
        if not coeffList:
            raise TypeError()
        for item in coeffList:
            if not isinstance(item,int):
                raise TypeError()

        self.coeffList = coeffList

#       remove redundant 0
        while self.coeffList[0] == 0 and len(self.coeffList) > 1:
            del self.coeffList[0]

    def _getSize(self) -> int:
        return len(self.coeffList)

    def _getMonomCoef(self, monomDegree: int) -> int:
        return self.coeffList[monomDegree]

    def _changeSigns(self):
        for i in range(0, len(self.coeffList)):
            self.coeffList[i] *= -1
        return self

    def toString(self) -> str:

        resultStr = ''
        isFirst = True
        degree = len(self.coeffList) - 1
        if len(self.coeffList)==1 and self.coeffList[0] == 0:
            resultStr = '0'
        for item in self.coeffList:
            if item != 0:
                # Определяем и пишем в строку знак текущего монома
                if isFirst:
                    if item < 0:
                        resultStr += '- '
                else:
                    resultStr += ' + ' if item > 0 else ' - '
                absValue = abs(item)

                if degree > 0:
                    resultStr += '{0}x^{1}'.format(absValue if absValue > 1 else '',
                                                   degree) if degree > 1 else '{0}x'.format(absValue)
                else:
                    resultStr += '{0}'.format(absValue)
                isFirst = False
            degree = degree - 1
        return resultStr

    def printInternalView(self):
        return '{0}({1})'.format(self.__class__.__name__, self.coeffList)

    def __str__(self):
        return self.toString()

    def __add__(self, other):
        result = None
        if isinstance(other, Polynomial):
            newCoeff = list()
            if self._getSize() >= other._getSize():
                # self is bigger
                newCoeff.extend(self.coeffList)
                i = 0
                while i < other._getSize():
                    index = -1 - i
                    newCoeff[index] += other._getMonomCoef(index)
                    i = i + 1

            else:
                # other is bigger
                newCoeff.extend(other.coeffList)
                i = 0
                while i < self._getSize():
                    index = -1 - i
                    newCoeff[index] += self._getMonomCoef(index)
                    i = i + 1

#           remove redundant 0
            while newCoeff[0] == 0 and len(newCoeff) > 1:
                del newCoeff[0]

            result = Polynomial(newCoeff)
        elif isinstance(other, int):
            result = self.coeffList.copy()
            result[-1] = result[-1] + other
            result = Polynomial(result)
        else:
            raise TypeError()

        return result

    def __sub__(self, other):
        secondArg = None
        if isinstance(other, Polynomial):
            secondArg = Polynomial(other.coeffList.copy())
            secondArg._changeSigns()
        elif isinstance(other, int):
            secondArg = other * (-1)
        else:
            raise TypeError
        return self.__add__(secondArg)

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def __mul__(self, other):
        result = None
        if isinstance(other, Polynomial):
            newSize = (self._getSize() - 1) * (other._getSize() - 1) + 2
            resultList = list()
            for i in range(0, newSize):
                resultList.append(0)

            for i in range(0, len(self.coeffList)):
                for j in range(0, len(other.coeffList)):
                    selfDegree = self._getSize() - i - 1
                    otherDegree = other._getSize() - j - 1

                    currDegree = selfDegree + otherDegree

                    resultList[newSize - 1 - currDegree] = resultList[newSize - 1 - currDegree] + self._getMonomCoef(
                        i) * other._getMonomCoef(j)

            # Удаляем лишние нули
            while resultList[0] == 0 and len(resultList) > 1:
                del resultList[0]
            result = Polynomial(resultList)
        elif isinstance(other, int):
            result = self.coeffList.copy()
            for i in range(0, len(result)):
                result[i] = result[i] * other
            result = Polynomial(result)
        else:
            raise TypeError
        return result

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffList == other.coeffList
        elif not (isinstance(other, int)):
            raise TypeError()
        else:
            return len(self.coeffList) == 1 and self.coeffList[0] == other
