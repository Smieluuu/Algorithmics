text = input("type text to check if it is a palindrome: ")

if text == text[::-1]:
    print('text is a palindrome')
else:
    print('text isnt palindrome')
