nums = [2,2,1,1,1,2,2]

from collections import Counter

if Counter(nums)[nums[0]] > len(nums)/2:
    print(nums[0])

def isPalindrome(s):
    s = ''.join(ch for ch in s if ch.isalnum()).lower()
    return s == s[::-1]

s = 'babad'

sub = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

isPalindrome(sub[0])

def longestPalindrome(s):
    sub = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

    palin = []

    for i in range(len(sub)):
        if isPalindrome(sub[i]) == True:
            palin.append(sub[i])

    return max(palin, key=len)

longestPalindrome(s)