# Link: hackerrank.com/challenges/py-check-subset/problem


if __name__ == '__main__':
    f = open("Input")
    cases = int(f.readline())
    for i in range(cases):
        lenA = int(f.readline())
        set_A = set(f.readline().split())
        lenB = int(f.readline())
        set_B = set(f.readline().split())
        if len(set_B.intersection(set_A)) == lenA:
            print(True)
        else:
            print(False)