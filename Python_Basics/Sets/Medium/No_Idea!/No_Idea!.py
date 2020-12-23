# Link: https://www.hackerrank.com/challenges/no-idea/problem

Idea = '''
Create a set, main_set, from the root_array to eliminate duplicate elements.
Then create plus_set and minus_set as intersection of main_set with plus_array and minus_array respectively.
Then create plus_point_array and minus_point_array from common elements between root_array and plus_set and minus_set respectively.
return the subtraction between length of plus_point_array and minus_point_array'''


def happiness_point(root_array, plus_array, minus_array):
    main_set = set(root_array)
    plus_set = main_set.intersection(plus_array)
    plus_point_array = [value for value in root_array if value in plus_set]
    minus_set = main_set.intersection(minus_array)
    minus_point_array = [value for value in root_array if value in minus_set]
    return len(plus_point_array) - len(minus_point_array)


if __name__ == '__main__':
    f = open("Input")
    n_m_string = f.readline().split()
    n = int(n_m_string[0])
    m = int(n_m_string[1])
    print(n, m)
    main_array = list(map(int, f.readline().split()))
    print(main_array)
    A = list(map(int, f.readline().split()))
    B = list(map(int, f.readline().split()))
    result = happiness_point(main_array, A, B)
    print(result)
    f.close()