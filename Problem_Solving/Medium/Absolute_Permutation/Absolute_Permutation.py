# Link: https://www.hackerrank.com/challenges/absolute-permutation/problem

# The basic idea is that we need a pair of numbers to swap with each other
# in order to create a lexicographically smallest absolute permutation.

# And the distance between that pair of numbers is k.
# So we need an amount of pairs with k distance. Or k*pairs*2 numbers.
# So k*2 will be a divisor of n. So that n have to be an even number and divisible by k*2.

# For example k=2 and we have [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] as an array
# So pairs will be (1, 3) (2, 4) (5, 7) (6, 8) (9, 11) (10, 12)
# Result will be [3, 4, 1, 2, 7, 8, 5, 6, 11, 12, 9, 10]

# As we can see, there are 6 pairs and for each of two pairs,
# the smallest number and the largest number that can satisfy the condition
# are k*2 units away from each other (in index).
# Therefore we just swap the number around in a group of 4.
# As if we swap it with another group then it is no longer the smallest one.
# From the above array: we have 3 groups of 4:
# [1, 2, 3, 4] with the index from [1 -> 4]
# [5, 6, 7, 8] with the index from [5 -> 8]
# [9, 10, 11, 12] with the index from [9 -> 12]

# So we will divide the journey into parts of k*2.
# Then in each part of k*2, we divide it into 2 parts of k numbers.
# The first part is for numbers that equal to index plus 1 plus k (u+1 + k).
# The second part is for numbers that equal to index plus 1 minus k (v+1 - k).


def absolutePermutation(n, k):
    initial_array = [x for x in range(1, n + 1)]
    if k == 0:
        return initial_array
    elif n % k != 0 or (n / k) % 2 != 0:
        return [-1]
    else:
        result_array = []
        range_of_swap = k * 2
        amount_of_range_of_swap = int(n / (k * 2))
        for x in range(amount_of_range_of_swap):
            for u in range(range_of_swap * x, range_of_swap * x + k):  # half range of swap
                result_array.append(u + 1 + k)
            for v in range(range_of_swap * x + k, range_of_swap * (x + 1)):  # other half
                result_array.append(v + 1 - k)
        return result_array


if __name__ == "__main__":
    input_file = open("Input")
    cases = int(input_file.readline())
    for i in range(cases):
        input_array = input_file.readline().rstrip().split()
        upper_limit = int(input_array[0])  # n in the function's parameter
        k = int(input_array[1])  # the difference
        print(absolutePermutation(upper_limit, k))
