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

s = "Hello, my name is John"

len(s.split())

s = "5F3Z-2e-9-w"

s = s.replace('-', '').upper()

nums = [2,5,1,3,4,7]

first = nums[:len(nums)//2]
second = nums[len(nums)//2:]

result = []

for i in range(len(first)):
    result.append(first[i])
    result.append(second[i])

result