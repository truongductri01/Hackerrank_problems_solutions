# Link: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# idea is to keep changing the position of the highest value (if not in correct position)
'''
Need?
    1. The position of the highest number
    2. the position of those numbers after changing position with the highest number (maximum 2)
    Because we only need to care about maximum 2 numbers after changing positions so it will not cost much time

How?
    1. Create 2 dictionaries:
        1: key is items' values and value is the index of each item
        2: key is items' indexes and value is the value of each item
    2. each time we change the position of the highest number, conduct swaps in those 2 dictionaries
'''


# create a map to manage position
def valueKey(arrayOfInt):  # create a dictionary object with item's value as key and index as value
    dictionary = {}
    for index, item in enumerate(arrayOfInt):
        if item - (index + 1) > 2:
            raise ValueError("Too Chaotic")
            # return "Fail at item: {}".format(item)

        dictionary.update({item: index + 1})
    return dictionary


def positionKey(arrayOfInt):  # create a dictionary object with index as key and item's value as value
    dictionary = {}
    for index, item in enumerate(arrayOfInt):
        if item - (index + 1) > 2:
            raise ValueError("Too Chaotic")

        dictionary.update({index + 1: item})  # we can do this as none integer is duplicated
    return dictionary

class Solution:
    def arrangeSteps(self, arrayOfGuests):
        counter = 0
        highestNumber = len(arrayOfGuests)
        print("Higher number", highestNumber)
        try:
            dictionaryValue = valueKey(array)
            print("Based on value:", dictionaryValue)

            dictionaryPosition = positionKey(array)
            print("Based on Position", dictionaryPosition)

            # now test each number based on their position and value
            while highestNumber >= 1:
                position = dictionaryValue[highestNumber]
                temp = position  # is now 1
                subtraction = highestNumber - position  # see how far is it from its original position
                if subtraction != 0:
                    counter += subtraction
                    # swap the other numbers' positions (maximum: 2) followed the highest number we just test
                    # how to?
                    for i in range(position + 1, highestNumber + 1):
                        valueOfTheNextPosition = dictionaryPosition[i]

                        # now swap in Position dictionary
                        dictionaryPosition[temp] = valueOfTheNextPosition
                        dictionaryPosition[i] = highestNumber

                        # now swap in Value dictionary
                        dictionaryValue[highestNumber] = i
                        dictionaryValue[valueOfTheNextPosition] = temp

                        temp += 1

                        print("Position:", dictionaryPosition)
                        print("Value:", dictionaryValue)
                highestNumber -= 1
            print("Counter:", counter)

        except ValueError as e:
            print(e)


if __name__ == '__main__':
    with open("Input") as f:
        cases = int(f.readline())
        for i in range(cases):
            length = int(f.readline())
            array = list(map(int, f.readline().split()))
            print(array)

            S = Solution()
            S.arrangeSteps(array)

            print()
