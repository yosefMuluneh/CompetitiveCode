# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = None
        carry = 0
        while l1 or l2:
            if l1 is None:
                a = 0
            else:
                a = l1.val
                l1 = l1.next
            if l2 is None:
                b = 0
            else:
                b = l2.val
                l2 = l2.next
            sum = a + b + carry
            carry = 0
            if sum > 9:
                sum = str(sum)
                sum, carry = int(sum[1]), int(sum[0])
            ans = ListNode(sum, ans)
        if carry:
            ans = ListNode(carry, ans)
        new = None
        while ans:
            new = ListNode(ans.val, new)
            ans = ans.next
        return new
        

