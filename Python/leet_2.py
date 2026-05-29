# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_Number(ll):
            my_string = ""
            curr = ll
            while curr:
                my_string += str(curr.val)
                curr = curr.next
            my_string = my_string[::-1]
            return int(my_string)
        mySum = get_Number(l1) + get_Number(l2)
        my_string = str(mySum)[::-1]
        dummy = ListNode(0)
        curr = dummy
        for item in my_string:
            curr.next = ListNode(int(item))
            curr = curr.next
        return dummy.next

        
        
