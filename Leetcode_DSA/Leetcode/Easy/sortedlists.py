class ListNode:
    pass
def sortedLists(l1: [ListNode], l2: [ListNode]):
    #ew_l1 = Node(l1)
    head = ListNode()
    curr = head

    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
        curr.next = l1 if l1 != [] else l2
        return head.next





print(sortedLists([1,2,4],[7,9]))