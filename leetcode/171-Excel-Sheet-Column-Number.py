'''
leetcode
171. Excel Sheet Column Number AC
zhao xiaodong
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        numDict='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        sum=0
        #k=0
        #for i in reversed(s):
        #    sum = sum + (numDict.index(i)+1) * 26 ** k
        #    k = k + 1
        #return sum
        k=len(s)
        p = 0
        while(k>0):
            sum = sum + (numDict.index(s[k-1])+1)*26 ** p
            k = k - 1
            p = p + 1
            
        return sum