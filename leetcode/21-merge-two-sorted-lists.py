class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy head node to simplify the code
        dummy_head = ListNode(0)
        current = dummy_head
        
        # iterate over both lists until one of them becomes None
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        # add the remaining nodes from the non-empty list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy_head.next