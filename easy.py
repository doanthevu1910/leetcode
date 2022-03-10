strs = ["flower", "flow", "flight"]

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

from collections import Counter

jewels = "aA"
stones = "aAAbbbb"

Counter(jewels)
sum += Counter(stones)[jewels[i]]

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        answer = ''

        for i in range(len(indices)):
            answer += s[indices.index(i)]

        return answer

def function(head):
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """

        steps = 0

        while num > 0:
            if num % 2 == 0:
                num //= 2
                steps += 1
            else:
                num -= 1
                steps += 1

        return steps