def acmTeam(topic):
    l = len(topic)
    max_t = 0
    count = 0
    for i in range(l - 1):
        a = topic[i]
        for j in range(i + 1, l):
            print("i:", i, "j:", j)
            b = topic[j]
            s = str(int(a) + int(b))
            print("s1:", s)
            if a[0] == "0" and b[0] == "0":
                s = "0" + s
            print("s:", s)
            t = m - (s.count("0")+m-len(s))
            if t > max_t:
                max_t = t
                count = 0
            if t == max_t:
                count += 1
            print("max:", max_t, "count:", count)
            print("/")
        print("")
    # return 1


n = 4
m = 5
topic = ["00101", "11100", "11010", "00101"]
acmTeam(topic)
