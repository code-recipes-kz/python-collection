# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # reverse a group of k nodes starting from the given head
        def reverse(head, k):
            prev = None
            curr = head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev, curr
        
        # count the number of nodes in the linked list
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        # base case: if the number of nodes is less than k, return the head
        if count < k:
            return head
        
        # reverse the first group of k nodes
        new_head, next_group_head = reverse(head, k)
        
        # recursively reverse the remaining groups of k nodes
        head.next = self.reverseKGroup(next_group_head, k)
        
        return new_head