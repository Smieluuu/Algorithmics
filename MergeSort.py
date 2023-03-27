tab = [8, 2, 1, 9, 5]
print(tab)

def mergeSort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        left = tab[:mid]
        right = tab[mid:]
        print("left: ", left)
        print("right: ", right)
        mergeSort(left) 
        mergeSort(right)

#       lewa = prawa = główna  = index 0 
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                tab[k] = left[i]
                i += 1
            else:
                tab[k] = right[j]
                j += 1
            k  += 1

        while i < len(left):
            tab[k] = left[i]
            i += 1
            k += 1 

        while j < len(right):
            tab[k] = right[j]
            j += 1 
            k += 1
        print("Po: ", tab)

mergeSort(tab)
print(tab) 