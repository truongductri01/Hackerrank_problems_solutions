# Link: https://www.hackerrank.com/challenges/3d-surface-area/problem

# first create an array which consists of the following things
# for even indexed element represent the common side of two adjacent block in a row
# for the odd indexed element represent the common side of two adjacent block in each column of two continuous row

def difArray(A):
    result = []
    if len(A) == 1:
        if len(A[0]) == 1:
            return 0
        else:
            for i in range(len(A[0]) - 1):
                result.append(min(A[0][i], A[0][i + 1]))
            return sum(result)
    else:
        for i in range(len(A) - 1):
            r = []
            c = []
            if len(A[i]) == 1:
                r.append(0)
            else:
                for j in range(len(A[i]) - 1):
                    r.append(min(A[i][j], A[i][j + 1]))
            for j in range(len(A[i])):
                c.append(min(A[i][j], A[i + 1][j]))
            result.append(r)
            result.append(c)
        if len(A[-1]) == 1:
            result.append([
                              0])  # as later we do sum for each small array in the big result array, so we need array typr for every element
        else:
            arr = []
            for i in range(len(A[-1]) - 1):
                arr.append(min(A[-1][i], A[-1][i + 1]))
            result.append(arr)
        # calculate sum of result
        s = 0
        for i in result:
            s += sum(i)
        # print(result)
        return s


def surfaceArea(A):
    s = 0
    for i in A:
        for j in i:
            s += 6 * j - (j - 1) * 2
    # print(s)
    return s - difArray(A) * 2


if __name__ == "__main__":
    f = open("Input")
    arr = f.readline().rstrip().split()
    H = int(arr[0])
    W = int(arr[1])
    A = []
    for _ in range(H):
        A.append(list(map(int, f.readline().rstrip().split())))
    # print(H,W)
    # print(A)
    print(surfaceArea(A))
    # print(difArray(A))

    # difArray(A)
    f.close()

'''
    What I have learned:
    1. Be careful with sum.
    If I use code:
        arr=[[1,2], 2]
        for i in arr:
            print(sum(i))
    then there will be an error as the last element is not array.
    So I have to use:
        arr=[[1,2], [2]]

    2. Be aware of return statement in function, especially with if and esle condition.
    If return appear in a if branch, it has to appear in the elif and else branch to, vice versa.
'''