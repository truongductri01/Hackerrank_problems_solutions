# Link: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

import math

Input = '''
2 1
5 6'''
Ouput = '''
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
'''

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no):
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary
        return Complex(real, imaginary)

    def __mul__(self, no):
        real = self.real*no.real - self.imaginary*no.imaginary
        imaginary = self.real*no.imaginary + self.imaginary*no.real
        return Complex(real, imaginary)

    def __truediv__(self, no):
        den = no.real**2 + no.imaginary**2
        real = (self.real*no.real + self.imaginary*no.imaginary) / den
        imaginary = (self.imaginary*no.real - self.real*no.imaginary) / den
        return Complex(real, imaginary)

    def mod(self):
        real = pow(self.real**2 + self.imaginary**2, 0.5)
        imaginary = 0
        return Complex(real, imaginary)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')