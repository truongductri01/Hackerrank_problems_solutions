def closestNumbers(arr):
    arr.sort()
    f_list = []
    l = len(arr)
    m = max(arr) - min(arr)
    for i in range (l-1):
        a = arr[i]
        b = arr[i+1]
        print("a:", a, "b:", b)
        if abs(a-b) == m:
            f_list.append(a)
            f_list.append(b)
            print("Equal:", f_list)
        elif abs(a-b) < m:
            m = abs(a-b)
            f_list.clear()
            f_list.append(a)
            f_list.append(b)
            print("Less:", f_list)
    print(f_list)
    #return f_list

this_list = "-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470 "


arr = list(map(int, this_list.rstrip().split()))
print("arr:", arr)
#result = closestNumbers(arr)
#print(result)

closestNumbers(arr)