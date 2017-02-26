'''
leetcode
153. Find Minimum in Rotated Sorted Array AC
zhao xiaodong
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return min(nums)
        flag = True if nums[1]-nums[0] > 0 else False
        for i in range(1,len(nums)):
            if flag and nums[i]-nums[i-1] < 0:
                return min(min(nums[i],nums[i-1]),nums[i-2])
            elif not flag and nums[i]-nums[i-1] > 0:
                return min(min(nums[i],nums[i-1]),nums[i-2])
        return min(nums[0],nums[len(nums)-1])