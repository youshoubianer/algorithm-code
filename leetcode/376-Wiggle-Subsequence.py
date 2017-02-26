'''
leetcode
376. Wiggle Subsequence AC
zhao xiaodong
'''

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        if len(nums) ==2:
            return 1 if nums[0]==nums[1] else 2
            
        small = True if nums[0] < nums[1] else False
        cnt=1;
        j=1;
        while(j<len(nums)):
            if small and nums[j-1] < nums[j]:
                cnt += 1
                small = False
            elif not small and nums[j-1] > nums[j]:
                cnt += 1
                small = True
            j += 1
            
        return cnt
        
'''
Note: 
    感觉题目不太严谨
    虽然有这么一句

    The first difference (if one exists) may be either positive or negative. 

    但并没有明确说明一定要从第一个开始

    对这样的数据
    1000 999 100 980 50 900 20 800 10

    最长的波动子序列应该为
    999 100 980 50 900 20 800 10

    但是按照AC代码来解的话，结果是
    1000 999

    并不是最长的。

    不知道有没有理解错误
'''