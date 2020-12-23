'''Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem?h_r=internal-search'''

'''
    s="1234"
    Code: for i in range(len(s)//2) -> i=0,1
    i=0:
        result=""
        index=i+1
        while True:
            if index > len(s)//2:
                break

            a=int(s[:index]) -> a=1 -> a+1=2
            diff= len(str(b))-len(str(a)) -> diff=1-1=0

            #Compare b with the next number in the string.
            #next number: s[index:index+len(str(a))+diff] -> s[0+1:0+1+1+0]=s[1:2]="2"
            b=int(s[i+1:i+1+len(str(a))+diff]) -> b=2
            if a+1!=b:
                result=False
                break
            else:
                a=b
                index=index+len(str(a))+diff -> index=2
        if result!=False:
            result=True
        if result=True:
            break
    print result
        #with this code and s=


#Need explaination for each line of code

'''
s = "1234"
print(len(s))


def separateNumbers(s):
    result = ""
    x = 0
    if len(s) <= 1:
        return "NO"
    for i in range(len(s) // 2):
        print("New for: {}".format(1 + i))
        result = ""
        index = i + 1
        print("i:", i, "index:", index)
        a = int(s[:index])
        x = a
        while True:
            if len(str(a)) + index > len(s):
                break
            diff = len(str(a + 1)) - len(str(a))
            b = int(s[index:index + len(str(a)) + diff])
            print("Index: {} and index +len(str(a))+ diff: {}".format(index, index + len(str(a)) + diff))
            print("a: {} b: {} diff: {}".format(a, b, diff))
            if a + 1 != b:
                result = "NO"
                print("Break here")
                break
            else:
                a = b
                index = index + len(str(a))
                print("Index in while loop: {}".format(index))
        if index != len(s):
            # as index=i+1
            result = "NO"
        if result != "NO":
            result = "YES"
        if result == "YES":
            break
        print("Result after while loop: {}", result)
        print("")
    if result == "YES":
        arr = [str(result), str(x)]
        return " ".join(arr)
    else:
        return result


print("Final Result:", separateNumbers(s))
print("")

