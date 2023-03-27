arr = [9, 8, 5, 10, 11, 22]
n = len(arr)

for i in range(n-1):
    print("loop", i)
    suspend = False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            suspend = True
    if not suspend:
        break

print(arr)
