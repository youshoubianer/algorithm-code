'''
leetcode
168. Excel Sheet Column Title AC
zhao xiaodong
'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ''
        while(n>0):
            idx = int((n-1) % 26)
            ans = charset[idx] + ans
            n = math.floor((n-1) / 26)
        return ans