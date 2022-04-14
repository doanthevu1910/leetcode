x = 25

print(x if x >= 40 else 0)

def CallOption(x):
    if x >= 40:
        return x
    return 0

CallOption(50)

x = [[1, 0], [0, 1]]
y = []

for element in x:
    y.append(element[::-1])

y = []

import numpy as np

for element in x:
    y.append(np.flip(element))

x = True
y = False

True * y

def function(x):
    return 'ghi'*x

function(True)

x = [10, 20, 30]

x.index(30)

lst = [0, 2, 'a', 'A', 'B', 'c', 8]

a = type(lst[3])

def count_character(lst):
    countupper = 0
    countlower = 0
    countnumber = 0

    for i in range(len(lst)):

        if type(lst[i]) == int:
            countnumber += 1

        else:
            if lst[i].isupper():
                countupper += 1

            elif lst[i].islower():
                countlower += 1

    return f'upper: {countupper}, lower: {countlower}, number: {countnumber}'

count_character(lst)

x = ['1', 'a', 'X', '2', 'a']

from collections import Counter

lower = [char for char in x if char.islower()]

y = Counter(lower)

x = [1, 2, 3]
y = ['v', 't', 'd']

dict(zip(x, y))

