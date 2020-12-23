# Link: https://www.hackerrank.com/challenges/np-shape-reshape/problem
import numpy


txt = '1 2 3 4 5 6 7 8 9'
arr = txt.split()
arr = numpy.array(arr, int)
print(arr)
arr.shape = (3, 3)
print(arr)
