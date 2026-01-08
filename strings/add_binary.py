# LeetCode: Add Binary
# Idea: Convert binary to integer, add, convert back to binary

class Solution:
    def addBinary(self, a, b):
        x = int(a, 2)
        y = int(b, 2)
        total = x + y
        return bin(total)[2:]
