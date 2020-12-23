# Link: https://www.hackerrank.com/challenges/py-set-mutations/problem


if __name__ == '__main__':
    f = open("Input")
    length_of_A = int(f.readline())
    A = set(map(int, f.readline().split()))
    # print(A)
    length_of_lines_next = int(f.readline())
    for i in range(length_of_lines_next):
        command = f.readline().split()[0]
        N = set(map(int, f.readline().split()))
        # print(N)
        if command == "update":
            A.update(N)
        elif command == "intersection_update":
            A.intersection_update(N)
        elif command == "difference_update":
            A.difference_update(N)
        elif command == "symmetric_difference_update":
            A.symmetric_difference_update(N)
        # print(A)
    print(sum(A))
    f.close()