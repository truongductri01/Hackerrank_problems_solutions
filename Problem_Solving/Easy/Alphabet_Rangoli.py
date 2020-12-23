def print_rangoli(size):
    n = (size + size - 1) + 2 * size - 2
    #print("N:",n)
    index=n//2
    #print("Index:", index)
    for i in range(size + size -1):
        if i <size:
            num = 97 + size - 1 - (i % size)
        else:
            num=97+i+1-size
        right = ["-" for _ in range(n // 2)]
        #print(num)
        mid=chr(num)
        for j in range(1,n//2,2):
            if (num+1)<=(97 + size - 1):
                num+=1
                right[j]=chr(num)
        left=right.copy()
        left.reverse()
        #print(right)
        print("".join(left)+mid+"".join(right))
size = 5
print_rangoli(size)