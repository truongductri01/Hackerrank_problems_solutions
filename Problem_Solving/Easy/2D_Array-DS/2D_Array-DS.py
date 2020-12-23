#Link: https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

if __name__=="__main__":
    f=open("Input")
    # for x in f:
    #     print(x)
    arr = []
    for x in f:
        arr.append(list(map(int, x.rstrip().split())))
    print(arr)
    result=[]
    for i in range(4):
        inner_s=0
        for j in range(4):
            inner_s=sum(arr[i][j:j+3])+sum(arr[i+1][j:j+3])+sum(arr[i+2][j:j+3])-arr[i+1][j]-arr[i+1][j+2]
            result.append(inner_s)
            #print("i: {}, j: {}, inner_s: {}".format(i,j,inner_s))

    print(max(result))
    # print(f.read())
    f.close()