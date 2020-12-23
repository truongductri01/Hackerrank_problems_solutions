# Link: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?h_r=internal-search

criteria = '''David wants to perform some number of swap operations such that:
1. Each container contains only balls of the same type.
2. No two balls of the same type are located in different containers.'''


def organizingContainers(container):
    a = []
    b = []
    for i in range(len(container)):
        a.append(sum(container[i]))  # The total ball in one row.
        s = 0
        for j in range(len(container)):
            s += container[j][i]  # Calculate the total of balls of each color
        b.append(s)  # b will contains element each represent a total of number of balls of each color
    c = a.copy()  # Create a copy of a and b to modify
    d = b.copy()
    # Because the same color balls cannot be in 2 different containers, So:
    for x in b:  # The amount of one color collection of balls. Ex: 8 blue balls
        if x in a:  # If there is a container that is big enough for that type of ball -> remove the number from c and d
            c.remove(x)
            d.remove(x)
    if len(c) == 0 and len(d) == 0:
        return "Possible"
    else:
        return "Impossible"


if __name__ == "__main__":
    f = open("Input")
    q = int(f.readline().rstrip())
    for _ in range(q):
        n = int(f.readline().rstrip())
        container = []
        for _ in range(n):
            container.append(list(map(int, f.readline().rstrip().split())))
        print(container)
        result = organizingContainers(container)
        print(result)
    f.close()

'''
    What I have learned today?
    1. Instead of using del c[index], use  c.remove(element) to avoid being out of range 
    when c is a copy of another array 
'''