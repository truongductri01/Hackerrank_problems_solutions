# Link: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

'''
two strings to be anagrams of each other
if the first string's letters can be rearranged
to form the second string.

aba and baa are anagrams
Requirements: return the minimum of deletion to form 2 anagrams:
    a = cde, b = dcf -> need to delete 1 char from each string -> 2 deletion
Idea:
    1. Create a union set which gather all unique chars from a and b
    2. compare each frequencies of each char from a and b
    3. return the counter
'''

import timeit


def makeAnagram1(a, b):
    # method 1: compare arrays: cost more time
    start1 = timeit.default_timer()
    counter = 0
    arrA = sorted(list(a))
    arrB = sorted(list(b))
    iA = iB = 0
    lengthA = len(arrA)
    lengthB = len(arrB)

    tempA = lengthA
    tempB = lengthB
    # without using tempA and tempB, there will be a logical error

    while True:
        if iA >= lengthA or iB >= lengthB:
            # if using lengthA and lengthB only:
            # iA may stop at 2 whereas lengthA was 3 as we reduce it somewhere in the code.

            # check if lengths are different
            counter += abs(tempA - tempB)
            # print("Break at iA: {}, iB: {}".format(iA, iB))
            break
        charA = arrA[iA]
        charB = arrB[iB]
        if charA > charB:
            counter += 1
            tempB -= 1  # reduce lengthB
            iB += 1
            # print("A > B, counter:", counter)
        elif charA == charB:
            # print("Equals")
            iB += 1
            iA += 1
        else:  # charB > charA
            counter += 1
            tempA -= 1  # reduce lengthA
            iA += 1

            # print("B > A, counter:", counter)
    print("Method 1:", counter)

    stop1 = timeit.default_timer()

    print("Time 1: {:.10f}".format(stop1 - start1))


def makeAnagram2(a, b):
    # method 2:
    start2 = timeit.default_timer()
    counter = 0
    setA = set(list(a))
    setB = set(list(b))
    unionSet = list(setA.union(setB))

    print(unionSet)

    for element in unionSet:
        counter += abs(a.count(element) - b.count(element))
    print("Method 2:", counter)
    stop2 = timeit.default_timer()

    print("Time 2: {:.10f}".format(stop2 - start2))


if __name__ == '__main__':
    a = "cde" * 100
    b = "abc" * 100

    makeAnagram1(a, b)
    makeAnagram2(a, b)
