#!/usr/bin/env python
# ================================================================
# Bruch: Implementation of a Bruch using Python
# ----------------------------------------------------------------

import sys


class Bruch:
    def __init__(self, zaehler=0, nenner=1):
        if isinstance(zaehler, int) and isinstance(nenner, int):
            if nenner != 0:
                self.zaehler = zaehler
                self.nenner = nenner
            else:
                raise ZeroDivisionError
        elif isinstance(zaehler, Bruch):
            self.zaehler = zaehler.zaehler
            self.nenner = zaehler.nenner
        else:
            raise TypeError("Incompatible input type")

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, Bruch):
            return float(self) + other
        else:
            raise TypeError("Incompatible input type")

    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, Bruch):
            return self + other
        else:
            raise TypeError("Incompatible input type")

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError("Incompatible input type")

    def __sub__(self, other):
        if isinstance(other, Bruch):
            return Bruch(self.zaehler - other.zaehler, self.nenner)
        elif isinstance(other, int):
            return Bruch(self.zaehler - other, self.nenner)
        else:
            raise TypeError("Incompatible input type")

    def __isub__(self, other):
        return self - Bruch(other)

    def __mul__(self, other):
        if isinstance(other, Bruch):
            return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)
        elif isinstance(other, int):
            return Bruch(self.zaehler * other, self.nenner)
        else:
            raise TypeError("Incompatible input type")

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, Bruch):
            return float(self) * float(other)

    def __imul__(self, other):
        if isinstance(other, int):
            return self * other
        elif isinstance(other, Bruch):
            return self * other
        else:
            raise TypeError("Incompatible input type")

    def __itruediv__(self, other):

        return self / Bruch(other)

    def __iter__(self):
        return (self.zaehler, self.nenner).__iter__()

    def __rtruediv__(self, other):
        if isinstance(other, int):
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(other * self.nenner, self.zaehler)
        else:
            raise TypeError("Incompatible input type")

    def __rsub__(self, other):
        if isinstance(other, int):
            return Bruch(self.nenner, other * self.nenner - self.zaehler)
        else:
            raise TypeError("Incompatible input type")

    def __truediv__(self, other):
        if isinstance(other, Bruch):
            z2, n2 = other
        elif isinstance(other, int):
            z2, n2 = other, 1
        else:
            raise TypeError("Incompatible input type")
        if z2 == 0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(n2, z2))

    def __gcd__(self, m, n):  # m can be negative
        while m % n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm % oldn
        return n

    def __str__(self):
        return str(self.zaehler) + "/" + str(self.nenner)

    def __eq__(self, other):
        if isinstance(other, Bruch):
            if self.zaehler == other.zaehler and self.nenner == other.nenner:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.zaehler == other:
                return True
            else:
                return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        firstnum = self.zaehler * other.nenner
        secondnum = other.zaehler * self.nenner
        return firstnum < secondnum

    def __le__(self, other):
        return self.__lt__(other) or \
               self.__eq__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __abs__(self):
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __radd__(self, other):
        return float(self) + float(other)

    def __invert__(self):
        return Bruch(self.nenner, self.zaehler)

    def float(self):
        return float(self.zaehler / self.nenner)

    def getzaehler(self):
        return self.zaehler

    def getnenner(self):
        return self.nenner

    def show(self):
        sys.stdout.write(str(self.zaehler) + "/" + str(self.nenner))
