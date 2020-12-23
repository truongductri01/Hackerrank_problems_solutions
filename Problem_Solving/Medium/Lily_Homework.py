# Link: https://www.hackerrank.com/challenges/lilys-homework/problem

# Given an arr. Example = [7, 15, 12, 3]
# Turns it into a beautiful arr: [3, 7, 12, 15]
# Beautiful: sum of ( a[i] - a[i-1] ) for 0 < i < len(arr) is minimal
# then return the number of swapping needed.

# Complete the lilysHomework function below.

# Answer these questions:
# 1. What is a beautiful arr?
#   it is the sorted list.
# 2. How to manage the swapping amount.
#         Use a dictionary to keep track of element in input arr(as keys)
#             and their positions (as values)
#
#         We get the input arr:
#             a. We create a sorted_arr = sorted(arr)
#             b. We create a reversed_arr = sorted(arr)
#                             reversed_arr.reverse()
#
#         We compare each element in original arr with the one in sorted_arr:
#             count = 0
#
#             We call the element of the sorted_arr as "standard"
#             If they are the same -> move to the next one.
#             Else:
#                 increase the count by 1
#                 we use the map to look for the index of standard in the dictionary.
#                 We use dictionary as it saves time better than using arr.index(standard)
#
#                 We swap the position of the standard with current element in the input arr.
#                 Also, update the position of the current element in the dictionary,
#                   as we do not need to care about the standard in input arr anymore.
#
#         We do the similar thing with the reversed_arr. Get the count of that.
#
#         Finally, we return the smaller count.
#
#

def prepare_dictionary(arr):
    dictionary = {}
    for i in range(len(arr)):
        dictionary[arr[i]] = i

    return dictionary


def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def update(index_dict, arr, index, standard):
    standard_index_in_original = index_dict[
        standard]  # using dictionary help reduce the time to find the index of wanted value.
    # as using arr.index(standard is time consuming)
    index_dict[arr[index]] = standard_index_in_original  # update index of the current element.
    swap(arr, standard_index_in_original, index)  # swap standard with current element in arr
    del index_dict[standard]


def forward(index_dict, arr):
    sorted_arr = sorted(arr)  # sorted list
    print("Begin with arr:", arr)
    print("Begin with dict:", index_dict)

    count = 0
    index = 0

    while index < len(sorted_arr):
        standard = sorted_arr[index]
        if arr[index] != standard:
            count += 1

            update(index_dict, arr, index, standard)
            print("arr after swapping:", arr)
            print("dictionary after swapping:", index_dict)

        index += 1
    print("Final result for forward:", count)
    print()
    return count


def backward(index_dict, arr):
    reversed_arr = sorted(arr)  # reversed list
    reversed_arr.reverse()
    print("Begin with arr:", arr)
    print("Begin with dict:", index_dict)
    print("reverse:")

    count = 0
    index = 0

    while index < len(reversed_arr):
        standard = reversed_arr[index]
        if arr[index] != standard:
            count += 1

            update(index_dict, arr, index, standard)

            print("arr after swapping:", arr)
            print("dictionary after swapping:", index_dict)

        index += 1
    print("Final result for backward:", count)
    return count


def lilysHomework(arr):
    index_dict = prepare_dictionary(arr)
    c_dict = index_dict.copy()
    c_arr = arr.copy()
    f = forward(index_dict, arr)
    b = backward(c_dict, c_arr)
    return min(f, b)


if __name__ == '__main__':
    # test the prepare function
    a = [3, 4, 2, 5, 1]
    # index_dict = prepare_dictionary(a)
    # d = prepare_dictionary(a)
    # # print(d)
    #
    # # test forward function
    # # forward(index_dict, a)
    # backward(index_dict, a)

    arr = [7, 15, 12, 3]
    arr1 = [2, 5, 3, 1]
    arr2 = [3, 4, 2, 5, 1]  # for this one you have to swap backwards
    # [3, 4, 2, 5, 1] -> [3, 4, 5, 2, 1] -> [5, 4, 3, 2, 1]
    result = lilysHomework(arr2)
    print(result)
