# Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
# What we need:
# 1. A dictionary containing chars and their occurrence
# 2. Define the occurrence:
#       Valid if the occurrences are the same
#           or only one is different from the other but only 1 unit larger (not smaller)
#                   as we can only reduce not increase
#           or the char has different occurrence to the other and == 1 -> make it disappear


def occurrence_dict(string) -> dict:
    od = {}  # occurrence_dictionary
    for char in string:
        if char in od:
            od[char] += 1

        else:
            od[char] = 1
    print("Occurrence_dictionary:", od)
    return od


def isValid(string):  # od: occurrence_dictionary
    od = occurrence_dict(string)
    values = list(od.values())
    print("Occurrence_values:", values)

    unique_set = list(set(values))
    if len(unique_set) <= 1:
        return "YES"
    if len(unique_set) >= 3:
        return "NO"
    else:  # len(unique_set) == 2
        # example: [3, 3, 3, 2] -> YES
        # or [3, 3, 3, 4] -> YES
        # or [3, 3, 3, 1] -> YES
        first_number = unique_set[0]  # 3
        second_number = unique_set[1]  # 2 or 4 or 1

        # the number from the value list
        print("First number: {}, second number: {}".format(first_number, second_number))

        count1 = values.count(first_number)  # 3
        count2 = values.count(second_number)  # 1

        # consider larger and smaller amount of occurrence:
        # larger and smaller occurrence
        if count1 > count2:
            larger_occurrence = count1
            larger_occurrence_number = first_number
            smaller_occurrence = count2
            smaller_occurrence_number = second_number
        else:
            larger_occurrence = count2
            larger_occurrence_number = second_number
            smaller_occurrence = count1
            smaller_occurrence_number = first_number

        print("larger_occurrence_number: {}, smaller_occurrence_number: {}".format(larger_occurrence_number, smaller_occurrence_number))
        print("Larger: {}, smaller: {}".format(larger_occurrence, smaller_occurrence))

        if smaller_occurrence == 1:
            if smaller_occurrence_number - larger_occurrence_number == 1:
                print("Able to reduce one character")
                return "YES"
            elif smaller_occurrence_number == 1:
                print("Reduce one char to make that char disappear from the string")
                return "YES"
            else:
                print("Not able to reduce one char")
                return "NO"
        else:
            print("Too many occurrence, no reduction is possible")
            return "NO"


if __name__ == '__main__':
    input0 = "aabbc"
    input1 = "aabbcccc"
    input2 = "abcdefghhgfedecba"

    # test define_the_standout_occurrence function
    result0 = isValid(input0)
    print("Result:", result0)
    print()
    result1 = isValid(input1)
    print("Result:", result1)
    print()
    result2 = isValid(input2)
    print("Result:", result2)
    print()

    Output = '''
    Input 0: "aabbc"
    Occurrence_dictionary: {'a': 2, 'b': 2, 'c': 1}
    Occurrence_values: [2, 2, 1]
    First number: 1, second number: 2
    larger_occurrence_number: 2, smaller_occurrence_number: 1
    Larger: 2, smaller: 1
    Reduce one char to make that char disappear from the string
    Result: YES
    
    Input 1: "aabbcccc"
    Occurrence_dictionary: {'a': 2, 'b': 2, 'c': 4}
    Occurrence_values: [2, 2, 4]
    First number: 2, second number: 4
    larger_occurrence_number: 2, smaller_occurrence_number: 4
    Larger: 2, smaller: 1
    Not able to reduce one char
    Result: NO
    
    Input 2: "abcdefghhgfedecba"
    Occurrence_dictionary: {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 3, 'f': 2, 'g': 2, 'h': 2}
    Occurrence_values: [2, 2, 2, 2, 3, 2, 2, 2]
    First number: 2, second number: 3
    larger_occurrence_number: 2, smaller_occurrence_number: 3
    Larger: 7, smaller: 1
    Able to reduce one character
    Result: YES
    '''
