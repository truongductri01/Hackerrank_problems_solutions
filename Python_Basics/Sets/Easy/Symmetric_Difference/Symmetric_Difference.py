# Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    f = open("Input")
    m_number = int(f.readline())
    m_string = f.readline().rstrip()
    n_number = int(f.readline())
    n_string = f.readline().rstrip()
    M = set(m_string.split())
    N = set(n_string.split())
    difference_M = M.difference(N)
    difference_N = N.difference(M)
    difference = list(difference_M.union(difference_N))
    difference = list(map(int, difference))
    difference.sort()
    for i in difference:
        print(i)