# Link: https://www.hackerrank.com/challenges/np-arrays/problem
import numpy


def arrays(arr):
    array = arr.copy()
    # array.reverse()
    array = numpy.array(array, float)  # with numpy, no need to use map to convert a list to a specific data type
    return array


if __name__ == '__main__':
    txt = '''1 2 3 4 -8 -10'''
    arr = txt.strip().split()
    print(arr)
    result = arrays(arr)
    print(result)


lesson = '''
1. To turn a list into a particular data type, we can either use map or numpy.
2. To apply a self defined, function to each element of a list, map is needed.'''