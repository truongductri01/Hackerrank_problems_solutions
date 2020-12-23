# Link: https://www.hackerrank.com/challenges/countingsort4/problem

#  The first half of the strings encountered in the inputs
#  are to be replaced with the character "-".

#  If two strings are associated with the same integer,
#  they must be printed in their original order so
#  your sorting algorithm should be stable

'''
Example:
    i	string	converted	list
    0				        [[],[],[]]
    1 	a 	    -		    [[-],[],[]]
    2	b	    -		    [[-],[-],[]]
    3	c		    	    [[-,c],[-],[]]
    4	d			        [[-,c],[-,d],[]]
'''

def printArray(arr):
    resultString = ""
    for sub_array in arr:
        if len(sub_array) == 0:
            continue
        else:
            for word in sub_array:
                resultString += word + " "

    resultString.strip()
    return resultString


def countSort(arr):
    length = len(arr)
    sort_array = [[] for i in range(length)]

    for i in range(length):
        # for the first half
        sub_array = arr[i]
        index = int(sub_array[0])  # the index to sort
        value = sub_array[1]  # the value

        if i < length // 2:
            print("Index >>>", index)
            print("Value >>>", value)
            print()

            sort_array[index].append("-")

            if i == length // 2 - 1:
                print("First half >>>", sort_array)
                print()

        else:
            print("Index >>>", index)
            print("Value >>>", value)
            print()
            sort_array[index].append(value)
    print("Final >>>", sort_array)

    print("String >>>", printArray(sort_array))


if __name__ == '__main__':
    print("Full Counting Sort")
    with open("input") as f:
        lines = int(f.readline())
        print("Lines >>>", lines)
        print()
        # maximum empty arrays according to the number of lines
        arr = []
        for i in range(lines):
            arr.append(f.readline().rstrip().split())

        countSort(arr)
