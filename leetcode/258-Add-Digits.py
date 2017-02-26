'''
leetcode
258. Add Digits AC
zhao xiaodong
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num % 9 or 9) if num else 0