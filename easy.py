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


class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                count += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1

        return count


class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def gcd(a, b):
            """Calculate the Greatest Common Divisor of a and b.

            Unless b==0, the result will have the same sign as b (so that when
            b is divided by it, the result comes out positive).
            """
            while b:
                a, b = b, a % b
            return a

        return gcd(max(nums), min(nums))

coordinates = "a1"

coordinates[0]

nums = [12,345,2,6,7896]

len(str(nums[0]))

class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return True
        else:
            return num % 10 != 0

 s = "aaabb"

 from collections import Counter

a = Counter(s)

len(a)

a['a']

return num in (6, 28, 496, 8128, 33550336)

import string

def int_to_base(n, N):
    """ Return base N representation for int n. """
    base_n_digits = digits + ascii_lowercase + ascii_uppercase
    result = ""
    if n < 0:
        sign = "-"
        n = -n
    else:
        sign = ""
    while n > 0:
        q, r = divmod(n, N)
        result += base_n_digits[r]
        n = q
    if result == "":
        result = "0"
    return sign + "".join(reversed(result))

int_to_base(34, 6)

nums = [1,2,3,2]

import numpy as np

np.unique(nums)

nums.count(item) == 1

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
array = np.reshape(grid, (1, len(grid) * len(grid[0])))[0]

array

num = [1,2,0,0]
k = 34

new = int(''.join([str(x) for x in num])) + k

[int(x) for x in str(new)]


class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        return [int(x) for x in str(int(''.join([str(x) for x in num])) + k)]

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]

new = nums1 + nums2 + nums3

from collections import Counter

Counter(new)[new]

import numpy as np

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        reshaped = np.reshape(matrix, (1, len(matrix) * len(matrix[0])))
        reshaped = reshaped[0]
        return any(element == target for element in reshaped)

