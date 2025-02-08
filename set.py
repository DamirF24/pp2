myset = {'Batman', 'Wonder Woman', 'Superman'}
myset.add('Flash')
print(myset)


myset.add('Joker')
print(myset)



if 'Lex Luthor' in myset:
    print('Lex is here')
else:
    print('Lex is not here')


Heroes = {'Batman', 'Superman', 'Wonder Woman', 'Flash', 'Cyborg', 'Aquaman'}
Villains = {'Superman', 'Lex Luthor', 'Joker', 'Harley Queen', 'Deadlock', 'Darksied'}
print(Heroes | Villains)
print(Heroes & Villains)