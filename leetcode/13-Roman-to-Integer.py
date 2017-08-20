'''
leetcode
13. Roman to Integer
zhao xiaodong
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000 }
		
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]    	
    
So = Solution()
a = So.romanToInt('IV')
print(a)

"""
神坑：
    tab与空格混用导致compiler error
    Line 23: IndentationError: unindent does not match any outer indentation level
"""