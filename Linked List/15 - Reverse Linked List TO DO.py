# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
                
# two helper functions

# this function translates lists to linked list
def to_linked_list(iterable):
    head = None
    for val in reversed(iterable):
        head = ListNode(val, head)
    return head

# this function translates linked list to lists
def to_native_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

        
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        


l1 = to_linked_list([1,2,4])
result = Solution().reverseList(l1)
print(to_native_list(result))




