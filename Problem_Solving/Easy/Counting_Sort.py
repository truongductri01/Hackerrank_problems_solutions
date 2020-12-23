arr = list(map(int, input("arr: ").rstrip().split()))
result = list(map(int, input("result: ").rstrip().split()))

for i in range(len(result)):
    if arr[i] != result[i]:
        print(i, arr[i], result[i])

print("len arr:", len(arr))
print("len result:", len(result))
