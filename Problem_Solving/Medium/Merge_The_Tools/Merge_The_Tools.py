# Link: https://www.hackerrank.com/challenges/merge-the-tools/problem


requirements = '''
Consider the following:

A string, s, of length k where s = C0C1C2C3...Cn-1.
An integer, k, where k is a factor of n.
We can split  into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in n. 
Then, use each ti to create string ui such that:
1. The characters in ui are a subsequence of the characters in ti.
2. Any repeat occurrence of a character is removed from the string such that each character in ui occurs exactly once. 
In other words, if the character at some index j in ti occurs at a previous index <j in ti, 
then do not include the character in string ui.
3. Given s and k, print n/k lines where each line i denotes string ui.'''


Idea = '''
1. Divide the string into segments
2. For each segment, create a string and add char in if char is not in the string yet.
    Create an array for unique char.
    If the char is not the string yet, append it to an array and add it to the string
    Else, continue to the other case'''


def divide_string_into_substring(string, length_of_each_segment):
    global array_of_segments
    array_of_segments = []
    for i in range(0, len(string), length_of_each_segment):
        array_of_segments.append(string[i:i+length_of_each_segment])
    # print(array_of_segments)


def merge_the_tools(string, length_of_each_segment):
    divide_string_into_substring(string, k)
    for segment in array_of_segments:
        char_array = []
        output_string = ""
        for i in range(length_of_each_segment):
            char = segment[i]
            if char in char_array:
                continue
            else:
                char_array.append(char)
                output_string += char
        print(output_string)


if __name__ == "__main__":
    f = open("Input")
    for x in f:
        line = x.strip()
        k = int(f.readline())
        print(line, k)
        merge_the_tools(line, k)
        # divide_string_into_substring(line, k)
    f.close()