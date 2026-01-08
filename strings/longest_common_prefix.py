class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        result = ""

        for letters in zip(*strs):
            if len(set(letters)) == 1:
                result += letters[0]
            else:
                break

        return result
