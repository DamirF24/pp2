strorint = input("Paste your number or word to check whether its palindrome:")

if strorint.isdigit():
    str1 = str(strorint)
    if str1 == str1[ : :-1]:
        print(f"Your number is palindrome!")
    else :
        print(f"Your number is not palindrome(")
else:
    if strorint == strorint[ : :-1]:
        print(f"Your word is palindrome!")
    else:
        print(f"Your word is not palindrome(")