# Link: https://www.hackerrank.com/challenges/palindrome-index/problem

def palindromeIndex(s):
    print(s)
    if len(s) == 1:
        return -1

    # check outside in
    # compare the left and right side of the string.
    # if different, increase counter.
    # then decide which index to increase before keep going.
    #   only if the next index (left or right) has the same value of the other side.
    #   ex: baa => b (at 0) != a (at 2) => increase left side to 1 (as at 1 is also a)
    #   if ex: bca => b != a then c != a => break and return -1

    length = len(s)
    iL = 0
    iR = length - 1
    counter = 0
    mid = length // 2
    result = 0

    while True:
        if iL == mid or iR == mid - 1:
            print("Limit reach")
            break
        if counter > 1:
            print("Counter too large")
            return -1

        leftChar = s[iL]
        rightChar = s[iR]

        if leftChar == rightChar:
            iL += 1
            iR -= 1
        else:
            counter += 1
            print("Not equal at, iL: {}  ;  iR: {}".format(iL, iR))

            # check and move the right index
            # ex: aaaab => b (iR=4) != a (iL=0) => but a (iR = 3) == a (iL = 0)  && a (iR = 2) == a (iL = 1)
            if s[iR - 1] == leftChar and s[iR - 2] == s[iL + 1]:
                print("Right equal")
                result = iR
                iR -= 1

            # if the right side does not work,
            # then check the next side
            elif s[iL + 1] == rightChar and s[iL + 2] == s[iR - 1]:
                print("Left equal")
                result = iL
                iL += 1
            else:
                # if both of them does not work then that means more than a single char will need to be deleted
                print("No change is possible")
                return -1
    if counter == 0:
        print("Counter is 0")
        return -1
    else:
        print("Result:", result)
        return result


if __name__ == '__main__':
    resultArr = []
    with open("Input") as f:
        cases = int(f.readline())
        for i in range(cases):
            print("Cases:", i)
            s = f.readline().rstrip()
            result = palindromeIndex(s)
            resultArr.append(result)
            print()

    print()
    print("Output array:", resultArr)
