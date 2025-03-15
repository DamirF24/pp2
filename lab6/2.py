string = input("To count the letters enter the word: ")
cnt1 = 0
cnt2 = 0
for str in string:
    if str.isupper():
        cnt1+=1
    elif str.islower():
        cnt2+=1

print(f"Uppercase letter: " , cnt1)
print(f"Lowercase letters: " , cnt2)