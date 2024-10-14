
class ListNode:
    pass
    def __init__(self, x=0, next = None):
        self.value = x
        self.next = next

class solution:
    def addnums(self,l1: [ListNode], l2: [ListNode]):
        dummyhead = ListNode(0)
        current = dummyhead
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)

            carry, out = divmod(val1 + val2 + carry, 10)
            current.next = ListNode(out)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummyhead.next

#test = solution()

#print(test.addnums([2 -> 4 -> 3 -> None], [5 -> 6 -> 4 -> None]))