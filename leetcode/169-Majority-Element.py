'''
leetcode
169. Majority Element AC
zhao xiaodong
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] +=1
            else:
                dict[i] = 1        
            if dict[i] > math.floor(len(nums)/2):
                return i
                