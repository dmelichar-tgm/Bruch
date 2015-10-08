#!/usr/bin/env python
#================================================================
# Bruch: Implementation of a Bruch using Python
#----------------------------------------------------------------

import sys

def gcd(m,n):  # m can be negative
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

class Bruch:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
        #sys.stdout.write("New: ")
        #Bruch.show(self)
        #sys.stdout.write("\n")

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        sys.stdout.write(str(self.num) + "/" +
          str(self.den))

    def __add__(self,other):
        newnum = self.num*other.den + \
                      self.den*other.num
        newden = self.den * other.den
        com = gcd(newnum,newden)
        return Bruch(newnum//com,newden//com)

    def __sub__(self,other):
        newnum = self.num*other.den - \
                      self.den*other.num
        newden = self.den * other.den
        com = gcd(newnum,newden)
        return Bruch(newnum//com,newden//com)

    def __mul__(self, fract):
        newnum = self.num*fract.num
        newden = self.den*fract.den
        common = gcd(newnum, newden)
        return Bruch(newnum//common,
          newden//common)

    def __div__(self, other):
        sign = 1
        if other.num == 0:
            return None # divide by 0
        if other.num < 0:
            sign = -1
            othernum = -other.num
        else:
            othernum = other.num
        newnum = self.num*other.den
        newden = self.den*othernum
        common = gcd(newnum, newden)
        return Bruch(sign*newnum//common,
          newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum < secondnum

    def __le__(self, other):
        return self.__lt__(other) or \
          self.__eq__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def float(self):
        return float(self.num) / float(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den