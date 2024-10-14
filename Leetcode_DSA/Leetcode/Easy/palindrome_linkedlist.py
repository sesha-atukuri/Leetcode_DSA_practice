from poetry.console.commands import self


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def ispalindome(self,head:[ListNode]):
        head_node = ListNode(head[0])
        current = head_node
        for i in range(1, len(head)):
            new_node = ListNode(head[i])
            current.next = new_node
            current = current.next


        slow = head_node
        fast = head_node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next



        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        #return prev.next

        left, right = head_node, prev

        # print(left.val)
        '''while left:
            print(left.val, end="," if left.next else "\n")
            left = left.next

        while right:
            print(right.val, end="," if right.next else "\n")
            right = right.next'''

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


print(Solution.ispalindome(self,[1,3,2,1]))