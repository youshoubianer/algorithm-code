'''
leetcode
65. Valid Number AC
zhao xiaodong
'''

import re
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = re.compile('^[\s]*[+-]?(\d+\.?\d*|\d*\.?\d+)(e[+-]?\d+)?[\s]*$')
        # pattern = re.compile('^[\ ]*[+-]?(\d+\.?\d*|\d*\.?\d+)(e[+-]?\d+)?[\ ]*$')
        
        res = pattern.match(s)
        return True if res else False
