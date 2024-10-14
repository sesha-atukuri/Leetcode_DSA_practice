class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def intersection_linkedlist(headA,headB):
    head_nodeA = ListNode(headA[0])
    head_nodeB = ListNode(headB[0])
    currA = head_nodeA
    currB = head_nodeB

    for i in range(1, len(headA)):
        newnodeA = ListNode(headA[i])
        currA.next = newnodeA
        currA = currA.next

    for j in range(1, len(headB)):
        newnodeB = ListNode(headB[j])
        currB.next = newnodeB
        currB = currB.next

    first_set = set()
    curr = headA
    while curr:
        first_set.add(curr)
        curr = curr.next

    curr = headB
    while curr:
        if curr in first_set:
            return curr
        curr = curr.next
    return None

print(intersection_linkedlist([4,1,8,4,5],[5,6,1,8,4,5]))

