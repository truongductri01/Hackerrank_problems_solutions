arr = [2 ,1 ,2 ,3,2 ]
count = 0
for i in range(0, len(arr)-1):
    print ("i:",i)
    l1 = arr[:]
    l2 = arr[i:]
    print("l1:",l1,"l2:",l2)

    for j in range(i):
        #print(j)
        l1[j] = 0
        #print(l1)
    m = min(l2)
    print("min:",m)
    # print ("min:",m)
    # print (arr[i])
    print("/")
    if arr[i]!= m:
        index = l1.index(m)
        print("i:",i,"index:",index)
        arr.pop(index)
        arr.insert(i,m)
        # print (arr[i],arr[index])
        # print (arr[index])
        # print (arr[i])
        count = count + abs(index - i)
    print("/")
    print("arr:", arr)
    print("count: ",count)
    print("")
# print (count)
