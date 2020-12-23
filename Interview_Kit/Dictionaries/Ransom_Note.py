# Link: https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def createDict(note):
    dictionary = {}
    for word in note:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary


def checkMagazine(magazine, note):
    ndict = createDict(note)
    for word in magazine:
        if word in ndict:
            ndict[word] -= 1

    for i in ndict.values():
        if i > 0:
            print("No")
            return
    print("Yes")
    return


if __name__ == '__main__':
    magazine = "two times three is not four".rstrip().split()
    note = "two times two is four".rstrip().split()
    print(createDict(note))
    checkMagazine(magazine, note)
