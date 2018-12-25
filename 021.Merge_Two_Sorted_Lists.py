# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next

# Test
# Create singly-linked list
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

# Print merged singly-linked list
t = Solution()
tt = t.mergeTwoLists(a1,b1)
while tt != None:
    print(tt.val, end = ' ')
    tt = tt.next