arr = [-2, 10, 15, 17, 22, 1, 5]

def minmax(tab):
    tab_min = []
    tab_max = []
    for i in range(0, len(tab)-1, 2):
        if tab[i] > tab[i+1]:
            tab_max.append(tab[i])
            tab_min.append(tab[i+1])
        else:
            tab_max.append(tab[i+1])
            tab_min.append(tab[i])
    if len(tab) % 2 == 1:
        tab_max.append(tab[-1])
        tab_min.append(tab[-1])
    return tab_min, tab_max

arr_min, arr_max = minmax(arr)
minimum = arr_min [0]
maximum = arr_max [0]
for n in arr_min:
    if n < minimum:
        minimum = n
for n in arr_max:
    if n > maximum:
        maximum = n
print(minimum)
print(maximum)