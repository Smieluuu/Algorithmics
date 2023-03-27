n = int(input())

def check(word1, word2):
    dict = {}
    for letter in word1:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1

    for letter in word2:
        if letter in dict:
            dict[letter] -= 1
        else:
            dict[letter] = 1

    if all(value == 0 for value in dict.values()): 
        print('True')
    else:
        print('False')

for i in range(n):
    word1, word2 = input().split()
    check(word1, word2)