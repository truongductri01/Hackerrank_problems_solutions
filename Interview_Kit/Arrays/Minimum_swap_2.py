# Link: https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

'''
Idea:
1. Swap the position of the highest number first (if not in the right order)
2. Create a map to manage the position and value at each index
'''


def createDictionary(arr):
    valueKey = {}
    indexKey = {}
    for index, item in enumerate(arr):
        valueKey.update({item: index + 1})
        indexKey.update({index + 1: item})
    return valueKey, indexKey


def minimumSwaps(arr):
    valueKey, indexKey = createDictionary(arr)

    highestNumber = len(arr)
    counter = 0

    # check the position of the highestNumber
    while highestNumber >= 1:
        hNPosition = valueKey[highestNumber]
        if highestNumber != hNPosition:
            # swap and increase count

            # swap with the one at the index which is equal to the value of the highestNumber
            valueAtWantedIndex = indexKey[highestNumber]

            # now swap in valueKey map
            valueKey[highestNumber] = highestNumber
            valueKey[valueAtWantedIndex] = hNPosition
            # swap in indexKey map
            indexKey[hNPosition] = valueAtWantedIndex
            indexKey[highestNumber] = highestNumber

            counter += 1
        print(valueKey)
        print(indexKey)

        highestNumber -= 1  # change to another number and check

    print(counter)


if __name__ == '__main__':
    arr = [4, 3, 1, 2]
    minimumSwaps(arr)
