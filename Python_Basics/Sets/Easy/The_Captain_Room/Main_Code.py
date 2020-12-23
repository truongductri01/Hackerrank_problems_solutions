# Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem
Input = '''
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
'''

Idea = '''
Sort the room numbers array, A1, (with duplicate number)
Starting index at 0
While True:
    compare the value at the index position with the variable next to it if index is not equal to len(A1)-1.
    if those values are equal, increase the index by K -> move to another different number.
    else, print the number as it is unique, break the while loop.
'''

if __name__ == '__main__':
    K = int(input())
    array_of_rooms = list(map(int, input().split()))
    array_of_rooms.sort()

    # Set method:
    # list_of_unique_rooms = list(set(array_of_rooms))
    # list_of_unique_rooms.sort()
    # index = 0
    # for i in list_of_unique_rooms:

    # No set:
    index = 0
    while True:
        if index == len(array_of_rooms)-1:
            print(array_of_rooms[index])
            break
        else:
            first = array_of_rooms[index]
            second = array_of_rooms[index+1]
            if first == second:
                index += K
            else:
                print(first)
                break