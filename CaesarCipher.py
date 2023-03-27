text = input('enter text: ')
key = int(input('enter the key: '))
list = list(text)

def szyfr(text, key):
    change = ""
    for n in range(len(list)):
        ord1 = ord(list[n])
        ord1 = ord1 + key
        if 97 <= ord1 - key < 123:
            if ord1 < 123:
                chr1 = chr(ord1)
                change = change + chr1
            else:
                ord1 = ord1 - 26
                chr1 = chr(ord1)
                change = change + chr1
        elif 65 <= ord1 - key < 91:
            if ord1 < 91:
                chr1 = chr(ord1)
                change = change + chr1
            else:
                ord1 = ord1 - 26
                chr1 = chr(ord1)
                change = change + chr1
    return change

run = szyfr(text, key)
print(run)

