# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = 

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        prev = None
        temp1 = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow.next
        slow.next = None 

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        while temp1 and prev:
            temp1_next = temp1.next
            prev_next = prev.next

            temp1.next = prev
            prev.next = temp1_next
            temp1 = temp1_next
            prev = prev_next
        return 
        


            


        