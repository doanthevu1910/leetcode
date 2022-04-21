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

buyers = {'buyer1': [24, 16, 13, 6, 5], 'buyer2': [23, 21, 19, 10, 7], 'buyer3': [21, 20, 15, 13, 10], 'buyer4': [20, 17, 9, 6, 5]}

sellers = {'seller1': [8, 10, 14, 19, 21], 'seller2': [6, 13, 16, 21, 23], 'seller3': [8, 12, 13, 22, 23], 'seller4': [8, 9, 13, 21, 24]}

sum()

x = buyers['buyer1']
y = sellers['seller1']

x
y

def CountSubtract(set1, set2):
    count = 0
    for i in range(len(set1)):
        if set1[i] - set2[i] >= 0:
            count += 1

    return count

ans = 0

buyers = {'buyer1': [15, 14, 12, 5, 3], 'buyer2': [20, 13, 6, 3, 2], 'buyer3': [15, 13, 11, 7, 4], 'buyer4': [19, 17, 16, 11, 3]}
sellers = {'seller1': [2, 6, 8, 11, 21], 'seller2': [6, 7, 12, 15, 17], 'seller3': [5, 6, 7, 11, 19], 'seller4': [3, 5, 7, 12, 13]}

CountSubtract(buyers['buyer1'], sellers['seller1'])
CountSubtract(buyers['buyer2'], sellers['seller2'])
CountSubtract(buyers['buyer3'], sellers['seller3'])
CountSubtract(buyers['buyer4'], sellers['seller4'])

buyers = {'buyer1': [15, 14, 12, 5, 3], 'buyer2': [20, 13, 6, 3, 2], 'buyer3': [15, 13, 11, 7, 4], 'buyer4': [19, 17, 16, 11, 3]}
sellers = {'seller1': [2, 6, 8, 11, 21], 'seller2': [6, 7, 12, 15, 17], 'seller3': [5, 6, 7, 11, 19], 'seller4': [3, 5, 7, 12, 13]}

demand = sorted(buyers['buyer1'] + buyers['buyer2'] + buyers['buyer3'] + buyers['buyer4'], reverse=True)

supply = sorted(sellers['seller1'] + sellers['seller2'] + sellers['seller3'] + sellers['seller4'])

count = 0

for i in range(len(demand)):
    if demand[i] >= supply[i]:
        count += 1

count

dict = {'melon': 6, 'r': 9}

dict['melon']

for key in dict:
    print(key)
    print(dict[key])

def f(x):
    return 5*x + 6

lst = [5, 10, 15]

sum(map(f, lst))