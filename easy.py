strs = ["flower","flow","flight"]

a = list(zip(*strs))

a[0]

set(a[2])

len(set(a[0]))

s = "   fly me   to   the moon  "

len(s.split()[len(s.split())-1])

bin(1010+1011)

int('12', 2)

# result, freq = 0, sorted([s.count(i) for i in set(s)])
# for i in freq:
#     if i % 2 == 0:
#         result += i
#     else:
#         if result % 2 == 0:
#             result += 1
#         result += i - 1
# return result