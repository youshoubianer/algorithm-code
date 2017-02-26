'''
leetcode
476 Number Complement  AC
zhao xiaodong
'''

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        flag = 1
        while(num > 0):
            n = int(not num % 2)
            num = num // 2
            res += n* flag
            flag *=2
        return res