class ListNode():
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

def reverse_linkedlist(head:[ListNode]):
    head_node = ListNode(head[0])
    current = head_node

    for node in range(1, len(head)):
        next_node = ListNode(head[node])
        current.next = next_node
        current = next_node
    current = head_node
    while current:
        print(current.val, end = "->" if current.next else "\n")
        current = current.next

    prev = None
    curr = head_node
    while curr:
        new_node = curr.next
        curr.next = prev
        prev = curr
        curr = new_node
    #return prev.next
    while prev:
        print(prev.val, end = "," if prev.next else "\n")
        prev = prev.next





print(reverse_linkedlist([1,3,2,4]))