import timeit
import random


def createDict(length):
    dictionary = {}
    for i in range(1, length + 1):
        dictionary.update({i: 0})
    return dictionary


def arrayManipulation(length, queriesArray):
    qdict = createDict(length)
    maximum = 0
    for case in queriesArray:
        [i1, i2, increment] = case
        for i in range(i1, i2 + 1):
            value = qdict[i]
            value += increment
            qdict[i] = value
            if value > maximum:
                maximum = value

            # print(qdict)

    # print(maximum)
    return maximum


if __name__ == '__main__':
    with open("Input") as f:
        [length, queries] = list(map(int, f.readline().split()))
        queriesArray = []
        for _ in range(queries):
            queriesArray.append(list(map(int, f.readline().rstrip().split())))

        start = timeit.default_timer()
        result = arrayManipulation(length, queriesArray)
        stop = timeit.default_timer()

        print("Time: ", stop - start)
        print("Result: ", result)

    # create random queries
    # rangeNumb = 1000000
    # for i in range(rangeNumb):
    #     a = b = random.randint(1, rangeNumb)
    #     increment = random.randint(1, rangeNumb // 100)
    #
    #     print(a, b, increment)
