# Complete the weightedUniformStrings function below.
# def createDictForWeights(weights: list):
#     dictionary = {}
#     uniqueSet = list(set(weights))
#     for i in uniqueSet:
#         # logical error:
#         # aaabaa => will return a: 5 which is not correct though
#         dictionary.update({i: weights.count(i)})
#     return dictionary


def createArrayForWeightsOccurrence(weights):
    result = []
    index = 0
    count = 1
    while True:
        if index >= len(weights) - 1:
            print("Break at", index)
            result.append([weights[index], count])
            break
        if weights[index] == weights[index + 1]:
            # two adjacent element with the same values
            print("Equal at index:", index)
            count += 1
        else:
            result.append([weights[index], count])
            count = 1
            print("Arr at", index, ":", result)
        index += 1

    return result


def testEachCase(arr, q):
    for element in arr:
        quotient = q / element[0]
        if quotient.is_integer() and quotient <= element[1]:
            return "Yes"
    return "No"


def weightedUniformStrings(s, queries):
    weights = [ord(char) - 96 for char in s]

    # logical error method
    # dictionary = createDictForWeights(weights)
    # keys = list(dictionary.keys())
    arr = createArrayForWeightsOccurrence(weights)
    print(arr)
    result = []
    for q in queries:
        tempResult = testEachCase(arr, q)
        result.append(tempResult)
    return result


if __name__ == '__main__':
    with open("Input") as f:
        s = f.readline()
        queries = [1, 3, 12, 5, 9, 10]
        print(weightedUniformStrings(s, queries))
