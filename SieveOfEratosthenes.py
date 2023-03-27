from math import sqrt

n = int(input("n = "))
t = [True] * (n+1)
t[0] = False
t[1] = False
for i in range(2,int(sqrt(n))+1):
    print(i)
    if t[i]:
        for j in range(i*i, n+1, i):
            t[j] = False
for k in range(len(t)):
    if t[k] == True:
        print(k)