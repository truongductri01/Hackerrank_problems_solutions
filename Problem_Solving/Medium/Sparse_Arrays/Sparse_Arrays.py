def Input():
    f = open("Input")
    strings_count = int(f.readline())
    global strings,queries
    strings = []
    for _ in range(strings_count):
        strings_item = f.readline()
        strings.append(strings_item.rstrip())

    queries_count = int(f.readline())
    queries = []
    for _ in range(queries_count):
        queries_item = f.readline()
        queries.append(queries_item.rstrip())
    # print("Strings:", strings)
    # print("Queries:", queries)
    f.close()

def matchingStrings(strings, queries):
    result=[0 for _ in range(len(queries))]
    for x in range(len(queries)):
        if queries[x] in strings:
            result[x]+=strings.count(queries[x])
            print("Result {} at {}: {}".format(queries[x],x,result))
    return result
if __name__=="__main__":
    Input()
    print("Strings:", strings)
    print("Queries:", queries)
    matchingStrings(strings,queries)


