'''
leetcode
2. Add Two Numbers AC
zhao xiaodong
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = sum = ListNode(-1)
        tmp = 0
        while l1 != None or l2 != None or tmp!=0:
            
            a = l1.val if l1 != None else 0
            b = l2.val if l2 != None else 0
                
            x = int((a + b + tmp)%10)
            tmp = math.floor((a + b + tmp)/10)
            print x
            sum.next = ListNode(x)
            
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

            sum = sum.next
        return ans.next
        
'''
Note:
    1. 注意每次的更新和取值
    2. python的class实例是传址 ans -> sum -> ListNode(-1)
    3. 预设一个头指针
    4. 不要忘了注意末尾的进位
'''
