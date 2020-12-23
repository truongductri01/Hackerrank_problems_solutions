# Link: https://www.hackerrank.com/challenges/two-characters/problem


def alternate(s):
    character_set = list(set(list(s)))
    character_set.sort()
    print(character_set)
    max_length = 0
    if len(character_set) < 2:
        return 0
    else:
        for i in range(len(character_set) - 1):
            for j in range(i + 1, len(character_set)):
                string_copy = s
                # print("Copy at the beginning", string_copy)
                first_character_to_keep = character_set[i]
                second_character_to_keep = character_set[j]
                print(first_character_to_keep, second_character_to_keep)
                for x in character_set:
                    if x != first_character_to_keep and x != second_character_to_keep:
                        string_copy = string_copy.replace(x, "")
                        # print(string_copy)
                print(string_copy, "\n")
                while True:
                    boolean_value = True
                    for k in range(len(string_copy) - 1):
                        first_char = string_copy[k]
                        second_char = string_copy[k + 1]
                        if first_char == second_char:
                            boolean_value = False
                            break
                    if boolean_value:
                        if len(string_copy) > max_length:
                            max_length = len(string_copy)
                            result = string_copy
                        break
                    else:
                        break
            print(max_length, result)
        return max_length


if __name__ == "__main__":
    f = open("Input")
    length_of_string = int(f.readline().rstrip())
    string = f.readline().rstrip()
    print(string)
    print(alternate(string))
    f.close()