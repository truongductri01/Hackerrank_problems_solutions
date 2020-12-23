#Link: https://www.hackerrank.com/challenges/cavity-map/problem

def cavityMap(arr):
    index=[]
    #do not count the border line:
    for i in range(1,len(arr)-1): #if len is 4 then i will only be 1,2
        for j in range(1,len(arr[i])-1):
            #the position is [i][j]
            if int(arr[i][j])>int(arr[i-1][j]) and int(arr[i][j])>int(arr[i][j-1]) and int(arr[i][j])>int(arr[i][j+1]) and int(arr[i][j])>int(arr[i+1][j]):
                index.append([i,j])
                # print(index, i, j)
            # print(i,j)

    for x in index:
        arr[x[0]][x[1]]="X"
    result=[]
    for i in range(len(arr)):
        result.append("".join(arr[i]))
    s="\n".join(result)
    return s

if __name__=="__main__":
    f=open("Input")
    n=int(f.readline().rstrip())
    arr=[]
    for _ in range(n):
        s=list(f.readline().rstrip())
        arr.append(s)
    print(arr)
    print(cavityMap(arr))
    f.close()

'''
    What I have learn after this?
    1. Dict will not allow same keys.
    So if you have dict={1:2} then dict.update({1:3}) -> dict={1:5}
    Instead, use array.append([1,2])
    2. When you create a copy of a list by using list.copy(), there is a problem. 
    If you have arr=[1,2,3]
    b=arr.copy()
    b[1]=4
    -> b=[1,4,3] and arr will also be [1,4,3]
    Why? arr will not be affected if we use b.append but if we change the element's value, arr will be affected
'''