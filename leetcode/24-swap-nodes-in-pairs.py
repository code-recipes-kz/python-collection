# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # If the list has 0 or 1 nodes, return the head.
        if not head or not head.next:
            return head
        
        # Initialize the current node to the head of the list.
        curr = head
        
        # Initialize the new head of the list to the second node.
        new_head = head.next
        
        # Initialize the previous node to None.
        prev = None
        
        # Traverse the list in pairs and swap the nodes.
        while curr and curr.next:
            # Get the next node.
            next_node = curr.next
            
            # Swap the nodes.
            curr.next = next_node.next
            next_node.next = curr
            
            # Update the pointers.
            if prev:
                prev.next = next_node
            
            prev = curr
            curr = curr.next
        
        # Return the new head of the list.
        return new_head