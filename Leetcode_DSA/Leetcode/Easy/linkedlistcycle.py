from poetry.console.commands import self


class ListNode:
    def __init__(self, val =0 , next = None):
        self.val = val
        self.next = next


    def hascycle(self,head):

        head_node = ListNode(head[0])
        curr = head_node
        for i in range(1, len(head)):
            new_node = ListNode(head[i])
            curr.next = new_node
            curr = curr.next

        visited = set()
        current = head_node
        while current:
            if current in visited:
                return True

            visited.add(current)
            current = current.next
        return False

        '''fast = head_node
        slow = head_node

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False'''








print(ListNode.hascycle(self, [3,2,0,-4]))