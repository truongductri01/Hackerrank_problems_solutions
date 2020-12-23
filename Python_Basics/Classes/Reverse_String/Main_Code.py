#  Write a Python class to reverse a string word by word.


class string_reverse:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        result_string = ''
        length = len(self.string)
        for i in range(length - 1, -1, -1):
            char = self.string[i]
            result_string += char
        return result_string


if __name__ == '__main__':
    string = input()
    sr = string_reverse(string)
    string_reversed = sr.reverse()
    print(string_reversed)