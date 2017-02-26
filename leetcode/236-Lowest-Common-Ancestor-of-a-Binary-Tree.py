'''
leetcode
236. Lowest Common Ancestor of a Binary Tree  AC
zhao xiaodong
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root in [None,p,q]:  return root
                
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        
        return root if left and right else left or right
        

'''
Note:
    后序遍历
    左右根

    返回若左右都有子，返回根，否则返回左右有子的那个
'''
        