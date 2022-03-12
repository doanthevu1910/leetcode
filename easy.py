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


class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """

        count = 0

        for i in range(len(items)):
            if ruleKey == "type" and items[i][0] == ruleValue:
                count += 1

            if ruleKey == "color" and items[i][1] == ruleValue:
                count += 1

            if ruleKey == "name" and items[i][2] == ruleValue:
                count += 1

        return count

s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"

s.isdigit()

import re

numbers = re.findall(r'\d+', s)

sorted(numbers) == numbers

set('ab')

set('aab')

numbers

if all(x == numbers[0] for x in numbers):
    return False

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return ''.join(word1) == ''.join(word2)

sentence = "thequickbrownfoxjumpsoverthelazydog"

sentence1 = "quickbrownfoxjumpsoverthelazydog"

a = list(set(sentence))

b = list(set(sentence1))

a == b

s = "Hello how are you Contestant"

' '.join(s.split()[0:4])


def replaceDigits(s):
    """
    :type s: str
    :rtype: str
    """
    new_string = ''

    for i in range(len(s)):
        if i % 2:
            new_string += str(chr(ord(s[i - 1]) + int(s[i])))
    else:
        new_string += s[i]

    return new_string

replaceDigits("a1c1e1")

gain = [-5,1,5,0,-7]

nums = [int(x) for x in gain]

int(gain[0])

number = 122322

def getdigits(number):
    num_str = str(number)
    ans = []
    for num in num_str:
      ans.append(num)
    return ans

getdigits(number)

digits = getdigits(number)

a = sorted(digits, reverse=True)

int(''.join(a))

class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """

        def getdigits(number):
            num_str = str(number)
            ans = []
            for num in num_str:
                ans.append(num)
            return ans

        digits = getdigits(num)

        ans = sorted(digits, reverse=True)

        return int(''.join(ans))


