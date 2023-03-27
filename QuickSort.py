arr = [3, 7, 1, 6, 2, 5]
low = 0
high = len(arr) - 1


def sorting(arr, low, high):
    i = low - 1
    if low < high:
        pi = pivot(arr, low, high)
        sorting(arr, low, pi-1)
        sorting(arr, pi+1, high)

def pivot(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1


sorting(arr, low, high)
print(arr)