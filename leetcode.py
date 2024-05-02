#Index for some of two element in array
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in num_to_index:
                return [num_to_index[remainder], i]
            num_to_index[num] = i
        return [] 


# --------------------------------------------------------------------------------------
# Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        return len(a[-1])
    
# --------------------------------------------------------------------------------------
# Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanat

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=[]
        for i in str(x):
            y.append(i)
        if y[0:] == y[::-1]:
            return True
        else:
            return False

# --------------------------------------------------------------------------------------
# Roman to Integer
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.

class Solution:
    def romanToInt(self, s: str) -> int:
        value={"I":1, "V":5, "X":10, "L": 50, "C": 100, "D": 500, "M":1000}
        total=0
        prev=0
        for i in reversed(s):
            number=value[i]
            if number < prev:
                total=total-number
            else:
                total=total+number
            
            prev=number

        return total



# --------------------------------------------------------------------------------------



# Longest Common Prefix
# Easy
# Topics
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix=prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

# --------------------------------------------------------------------------------------
# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        character = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in character.values():
                stack.append(char)
            elif char in character:
                if not stack or stack.pop() != character[char]:
                    return False
        return not stack

# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------
