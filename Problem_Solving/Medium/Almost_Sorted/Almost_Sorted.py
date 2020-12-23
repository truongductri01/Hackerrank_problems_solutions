# link: https://www.hackerrank.com/challenges/almost-sorted/problem

explanation = ''' Output Format
If the array is already sorted, output yes on the first line. You do not need to output anything else.
If you can sort this array using one single operation (from the two permitted operations)
                                                then output yes on the first line and then:
a. If elements can be swapped,  and , output swap l r in the second line.
l and r are the indices of the elements to be swapped, assuming that the array is indexed from l to r.
b. Otherwise, when reversing the segment , output reverse l r in the second line.
l and r are the indices of the first and last elements of the subsequence to be reversed, assuming that the array is indexed from l to r.
represents the sub-sequence of the array, beginning at index  and ending at index , both inclusive.
If an array can be sorted by either swapping or reversing, choose swap.
If you cannot sort the array either way, output no on the first line.
'''


# left = index + 1
# right = index (in reverse way) + len(arr) + 1


def almostSorted(arr):
    copy_array = arr.copy()
    copy_array.sort()
    # print(copy_array)
    # print(arr)
    if arr == copy_array:
        print("yes")
    else:
        count = 0
        for i in range(len(copy_array)):
            if arr[i] != copy_array[i]:
                count += 1
        for i in range(len(copy_array)):
            if arr[i] != copy_array[i]:
                left = i
                break
        for i in range(-1, -len(copy_array) - 1, -1):
            if arr[i] != copy_array[i]:
                right = i
                break
        # print(left, right)
        # print(count)
        if count == 2:
            print("yes")
            print("swap", left+1, right+len(copy_array)+1)
        else:
            # reverse case
            sub_array = arr[left:right+len(copy_array)+1]
            # print(sub_array)
            sub_array.reverse()
            # print(sub_array)
            if sub_array == copy_array[left:right+len(copy_array)+1]:
                print("yes")
                print("reverse", left+1, right+len(copy_array)+1)
            else:  # no case
                print("no")


if __name__ == "__main__":
    f = open("Input")
    number = int(f.readline())
    array = list(map(int, f.readline().rstrip().split()))
    almostSorted(array)
    f.close()