'''
leetcode
20. Valid Parentheses AC
zhao xiaodong
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = []
        for i in range(len(s)):
            length = len(p)
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                p.append(s[i])
            elif length <= 0:
                return False
            elif p[length-1] == '(' and s[i]==')' or p[length-1] == '[' and s[i]==']' or p[length-1] == '{' and s[i]=='}':
                p.pop()
            else:
                return False
            print p
        return True if len(p) == 0 else False

