# Link: https://www.hackerrank.com/challenges/py-set-add/problem


if __name__ == '__main__':
    f = open("Input")
    number_of_country = int(f.readline())
    country_set = set()
    for i in range(number_of_country):
        country_name = f.readline().rstrip()
        country_set.add(country_name)
    print(len(country_set))
    f.close()