# link: https://www.hackerrank.com/challenges/bigger-is-greater/problem

# whenever changing happens, begin sorting the right of the array counting after the swapped character to make the smallest string meet the critea


def biggerIsGreater(string):
    length = len(string)
    arr = list(string)
    for i in range(-1, -length, -1):  # traverse through the array in a backwards manner
        if string[i-1] < string[i]:  # compare two adjacent element. When the condition is True, the element with the index i-1 will be the want needed to be swapped.
            back_list = arr[i-1:]
            large = []
            # check the smallest element in the back_list that is larger than the element we want to swap before swapping to make the smallest string.
            for x in back_list:
                if x > string[i-1]:
                    large.append(x)
            smallest_element = min(large)
            index = back_list.index(smallest_element)
            # swap first
            char = string[i-1]
            back_list[i-1] = smallest_element
            back_list[index] = char
            print(back_list)
            # then sort the list
            list_for_sort = back_list[i:]
            list_for_sort.sort()
            # then join
            return string[:i-1]+back_list[i-1]+"".join(list_for_sort)  # join the string.
            break
    return "no answer"


if __name__=="__main__":
    f = open("Input")
    t = int(f.readline().rstrip())
    for _ in range(t):
        string = f.readline().rstrip()
        print(string)
        print(biggerIsGreater(string))
        print("")
    f.close()
