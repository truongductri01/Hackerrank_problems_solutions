def nonDivisibleSubset(k, s):
    # Write your code here
    remainer = []
    for i in s:  # gather a list of remainer when divide each element to k
        remainer.append(i % k)
    short_list = list(set(remainer))  # create a short list with distinct remainers
    result = 0  # counter
    arr = []
    l = len(short_list)
    for i in short_list:
        if i != 0:
            remain = (k - i) % k
            if i * 2 != k:
                if remainer.count(i) >= remainer.count(remain):
                    # want the longest list, so we need to find the remainer with the larest occurence. Then add them to the last result
                    result += remainer.count(i)
                else:
                    pass
            else:
                result += 1  # this means that there are 2 numbers in the original list when add up will be divisible by k.

    if 0 in short_list:
        result += 1  # if there are 2 0 remainer in the result -> sum % k == 0 -> Fail
    # print(result)
    print("Remainder:", remainer)
    print("Short_list:", short_list)


# k = 100


input_info = "1 7 2 4"
k = 3
s = list(map(int, input_info.rstrip().split()))
nonDivisibleSubset(k, s)
