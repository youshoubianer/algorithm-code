'''
leetcode
53 Maximum Subarray  AC
zhao xiaodong
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        weight = [nums[0]]
        maxn = nums[0]
        for n in nums[1:]:
            weight.append( n + ( weight[-1] if weight[-1] > 0 else 0))
            maxn = max(maxn,weight[-1])
        return maxn
