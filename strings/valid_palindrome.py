# LeetCode: Valid Palindrome
# Idea: Remove non-alphanumeric characters and compare with reverse

class Solution:
    def isPalindrome(self, s):
        clean = ""

        for ch in s:
            if ch.isalnum():
                clean += ch.lower()

        return clean == clean[::-1]
