# Link: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
if __name__ == '__main__':
    f = open("Input")
    set_length = int(f.readline())
    s = set(map(int, f.readline().split()))
    number_of_commands = int(f.readline())
    for i in range(number_of_commands):
        command_array = f.readline().split()
        if len(command_array) == 1 and len(s) > 0:  # to avoid set has no element left
            s.pop()
        else:
            command = command_array[0]
            value = int(command_array[1])
            if command == "discard" and value in s:  # to avoid KeyError
                s.discard(value)
            elif command == "remove" and value in s:  # to avoid KeyError
                s.remove(value)
    print(sum(s))
    f.close()