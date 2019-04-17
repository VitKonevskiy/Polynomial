import copy


class Polynomial:
    def __init__(self, arg):

        if isinstance(arg, Polynomial):
            self.coeffs = copy.deepcopy(arg.coeffs)
        elif not arg:
            raise TypeError()
        else:
            for item in arg:
                if not isinstance(item, int):
                    raise TypeError()

            self.coeffs = arg
#           remove redundant 0
            while self.coeffs[0] == 0 and len(self.coeffs) > 1:
                del self.coeffs[0]

    def _get_size(self):
        return len(self.coeffs)

    def _get_monom_coeff(self, monom_degree):
        return self.coeffs[monom_degree]

    def _change_signs(self):
        for i in range(0, len(self.coeffs)):
            self.coeffs[i] *= -1
        return self

    def print_internal_view(self):
        return '{0}({1})'.format(self.__class__.__name__, self.coeffs)

    def __str__(self):
        resultStr = ''
        isFirst = True
        degree = len(self.coeffs) - 1
        if len(self.coeffs) == 1 and self.coeffs[0] == 0:
            resultStr = '0'
        for item in self.coeffs:
            if item != 0:
                # Detect and write into resultStr sign of current monom
                if isFirst:
                    if item < 0:
                        resultStr += '- '
                else:
                    resultStr += ' + ' if item > 0 else ' - '
                absValue = abs(item)

                if degree > 0:
                    if degree > 1:
                        resultStr += '{0}x^{1}'.format(absValue if absValue > 1 else '', degree)
                    else:
                        resultStr += '{0}x'.format(absValue if absValue > 1 else '')
                    # resultStr += '{0}x^{1}'.format(absValue if absValue > 1 else '',
                    #                                degree) if degree > 1 else '{0}x'.format(absValue)
                else:
                    resultStr += '{0}'.format(absValue)
                isFirst = False
            degree = degree - 1
        return resultStr

    def __add__(self, other):
        result = None
        if isinstance(other, Polynomial):
            newCoeff = list()
            if self._get_size() >= other._get_size():
                # self is bigger
                newCoeff.extend(self.coeffs)
                i = 0
                while i < other._get_size():
                    index = -1 - i
                    newCoeff[index] += other._get_monom_coeff(index)
                    i = i + 1

            else:
                # other is bigger
                newCoeff.extend(other.coeffs)
                i = 0
                while i < self._get_size():
                    index = -1 - i
                    newCoeff[index] += self._get_monom_coeff(index)
                    i = i + 1

#           remove redundant 0
            while newCoeff[0] == 0 and len(newCoeff) > 1:
                del newCoeff[0]

            result = Polynomial(newCoeff)
        elif isinstance(other, int):
            result = copy.deepcopy(self.coeffs)
            result[-1] = result[-1] + other
            result = Polynomial(result)
        else:
            raise TypeError()

        return result

    def __sub__(self, other):
        secondArg = None
        if isinstance(other, Polynomial):
            secondArg = Polynomial(copy.deepcopy(other.coeffs))
            secondArg._change_signs()
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
            newSize = (self._get_size() - 1) * (other._get_size() - 1) + 2
            resultList = list()
            for i in range(0, newSize):
                resultList.append(0)

            for i in range(0, len(self.coeffs)):
                for j in range(0, len(other.coeffs)):
                    selfDegree = self._get_size() - i - 1
                    otherDegree = other._get_size() - j - 1

                    currDegree = selfDegree + otherDegree

                    resultList[newSize - 1 - currDegree] = resultList[newSize - 1 - currDegree] + self._get_monom_coeff(
                        i) * other._get_monom_coeff(j)

            # Remove redundant zeroes
            while resultList[0] == 0 and len(resultList) > 1:
                del resultList[0]
            result = Polynomial(resultList)
        elif isinstance(other, int):
            result = copy.deepcopy(self.coeffs)
            for i in range(0, len(result)):
                result[i] = result[i] * other
            result = Polynomial(result)
        else:
            raise TypeError
        return result

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coeffs == other.coeffs
        elif not (isinstance(other, int)):
            raise TypeError()
        else:
            return len(self.coeffs) == 1 and self.coeffs[0] == other
