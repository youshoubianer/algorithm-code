'''
leetcode
9. Palindrome Number AC
zhao xiaodong
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #再算一遍看是否相等
        newNum = 0
        a = x
        while(x>0):
            newNum = newNum*10 + int(x % 10)
            x = math.floor(x / 10)
        return True if newNum == a else False
    
'''
Note:

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #再算一遍看是否相等
        newNum = 0
        a = x
        while(x>0):
            newNum = newNum*10 + int(x % 10)
            x = math.floor(x / 10)
        return newNum == a  #去掉if else 竟然更慢了！
				
				
c版：
	三目运算符竟然比if else还要快好多
'''