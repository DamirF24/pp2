import os
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for letter in letters:
    os.mkdir(f"lab6/{letter}.txt")
