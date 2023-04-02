class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create two pointers
        slow_ptr = fast_ptr = head
        
        # Move fast_ptr n steps ahead of slow_ptr
        for i in range(n):
            fast_ptr = fast_ptr.next
            
        # If fast_ptr is None, it means we need to remove the head node
        if not fast_ptr:
            return head.next
        
        # Move both pointers until fast_ptr reaches the end of the list
        prev = None
        while fast_ptr:
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        
        # Remove the node pointed by slow_ptr
        prev.next = slow_ptr.next
        
        return head