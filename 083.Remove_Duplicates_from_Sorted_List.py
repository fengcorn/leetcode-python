# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next

# Test
# Create singly-linked list
a1 = ListNode(1)
a2 = ListNode(1)
a3 = ListNode(2)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(1)
b3 = ListNode(2)
b4 = ListNode(3)
b5 = ListNode(3)
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5

# Print the sorted list
t = Solution()
t1 = t.deleteDuplicates(a1)
while t1 != None:
    print(t1.val, end = ' ')
    t1 = t1.next
t2 = t.deleteDuplicates(b1)
while t2 != None:
    print(t2.val, end = ' ')
    t2 = t2.next


