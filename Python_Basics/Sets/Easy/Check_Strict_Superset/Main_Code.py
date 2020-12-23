# Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem


def check_strict_superset(main_set, sub_set):
    length = len(sub_set.intersection(main_set))
    if length == len(sub_set) and len(sub_set) < len(main_set):
        return True
    else:
        return False


if __name__ == '__main__':
    f = open("Input")
    setA = set(f.readline().split())
    cases = int(f.readline())
    for i in range(cases):
        setN = set(f.readline().split())
        if not check_strict_superset(setA, setN):
            print(False)
            break
    else:
        print(True)