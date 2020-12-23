#Link: https://www.hackerrank.com/challenges/encryption/problem
import math

def rowAndColumn():
    arr=[]
    global m,L,L_ceil,L_floor
    m = s.replace(" ", "")
    L=math.sqrt(len(m))
    L_floor=math.floor(L)
    L_ceil=math.ceil(L)
    if L_floor==L_ceil:
        arr.append(L_floor)
        arr.append(L_ceil)
    else:
        if L_floor*L_floor>=len(m):
            print("Run through L")
            arr.append(L_floor)
            arr.append(L_floor)
        elif L_floor*L_ceil>=len(m):
            print("Run through L2")
            arr.append(L_floor)
            arr.append(L_ceil)
        else:
            print("Run through L3")
            arr.append(L_ceil)
            arr.append(L_ceil)
    return arr

def encrytion():
    global r,c
    r = rowAndColumn()[0]
    c = rowAndColumn()[1]
    # print("Rows: {} and Columns: {}".format(r, c))
    result=[]
    # create the message base on:
    # row1: s[0:7]; row2: s[8:15];... row 7: s[8*6:len(s)]
    # then the first string needed to be print out is: s[0]+s[8]+s[16]+...+s[48]: sum of s[8*i] for i in range(0,7)

    # determine remainder after divide len(m)/row -> run to print out arr.
    # the other array will be for i in range(c-remainder): arr[m[8*j+i]for j in range(r-1)]
    if c * r == len(m):
        for i in range(c):
            arr = [m[c*j + i] for j in range(r)]
            result.append("".join(arr))
    else:
        #print("Run through")
        lines = len(m) % c
        #print(lines)
        try:
            for i in range(lines):
                #print("Run through 2")
                arr = [m[c * j + i] for j in range(r)]
                result.append("".join(arr))
            for i in range(lines, c):
                arr = [m[c * j + i] for j in range(r - 1)]
                result.append("".join(arr))
        except:
            print(Exception)
    return " ".join(result)

if __name__=="__main__":
    #need to know how many rows and columns
    #know what in each rows and columns
    #print the message out correctly -> may use 2 dimensional array

    s="iuo"
    rowAndColumn()
    print(m)
    print("Len(m):",len(m))
    print("L:",L)
    print("Floor F: {} and Ceil F: {}".format(L_floor,L_ceil))
    print()
    encrytion()
    print("Rows: {} and Columns: {}".format(r, c))
    #print(encrytion())

