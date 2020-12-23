def wrapper(f):
    def fun(l):
        # complete the function
        arr = []
        for number in l:
            length = len(number)
            data = "+91 {} {}".format(number[length - 10: length - 5], number[length - 5: length])
            arr.append(data)
        x = f(arr)
        return x

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
