'''
leetcode
292. Nim Game AC
zhao xiaodong
'''

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0